"""Pipeline entry point:  python -m ptg.cli <stage> [--config ...] [--set key=value ...]

Stages (in order): prepare, train --model rnn|lstm, evaluate, generate, llm, metrics,
human-sheet, human-analyze, report-assets.  `all` runs everything except human-analyze.
"""
import argparse
import os
import sys
import time

import pandas as pd
import yaml

from . import data as data_mod
from .dataset import StoryLMDataset, make_loader
from .metrics import describe_lengths, group_table, sample_table
from .prompts import get_prompts
from .tokenizer import WordTokenizer
from .utils import (get_device, hardware_info, load_config, load_jsonl, out_path, save_json, save_jsonl,
                    set_seed, timestamp)

MODELS = ("rnn", "lstm")
MODEL_LABEL = {"rnn": "Vanilla RNN", "lstm": "LSTM", "llm": "Qwen2.5-0.5B-Instruct"}


class Logger:
    def __init__(self, cfg):
        self.path = out_path(cfg, "run_log.txt")

    def __call__(self, msg):
        line = f"[{timestamp()}] {msg}"
        print(line, flush=True)
        with open(self.path, "a") as f:
            f.write(line + "\n")


def write_once(path, force):
    if path.exists() and not force:
        raise FileExistsError(f"{path} exists. Generated text is write-once; pass --force to regenerate.")


# ---------------------------------------------------------------------------------- stages
def stage_prepare(cfg, log, args):
    splits, stats = data_mod.prepare_splits(cfg)
    log(f"splits: {stats}")
    tcfg = cfg["tokenizer"]
    tok, vstats = WordTokenizer.build([r["text"] for r in splits["train"]], tcfg["min_freq"], tcfg["max_vocab"],
                                      tcfg["lowercase"])
    tok.save(out_path(cfg, "vocab.json"))
    vstats.update({f"unk_rate_{name}": tok.unk_rate([r["text"] for r in rows]) for name, rows in splits.items()})
    log(f"vocab: {vstats}")

    seq_stats = {}
    for name, rows in splits.items():
        ds = StoryLMDataset([r["text"] for r in rows], tok, cfg["sequences"]["max_len"])
        lens = [len(tok.tokenize(r["text"])) + 2 for r in rows]
        seq_stats[name] = {"stories": ds.n_stories, "windows": len(ds), "target_tokens": ds.n_target_tokens,
                           "stories_split_into_windows": ds.n_split_stories,
                           "pct_split": 100 * ds.n_split_stories / ds.n_stories,
                           "story_length_tokens": describe_lengths(lens)}
    log(f"sequences: {seq_stats}")

    prompt_oov = {p["id"]: tok.oov_words(p["text"]) for p in get_prompts()}
    save_json({"splits": stats, "vocab": vstats, "sequences": seq_stats, "prompt_oov": prompt_oov,
               "config": {k: cfg[k] for k in ("data", "tokenizer", "sequences")}, "seed": cfg["seed"]},
              out_path(cfg, "data_stats.json"))

    # Part 1 evidence: what the next-token training pairs look like.
    story = splits["train"][0]["text"]
    ids = tok.encode(story, add_bos=True, add_eos=True)
    lines = [f"Story (train[0], first 40 tokens): {' '.join(tok.decode_tokens(ids[:40]))}", "",
             "Input-target pairs (model sees input[:t+1], must predict target[t]):"]
    for t in range(12):
        ctx = " ".join(tok.decode_tokens(ids[max(0, t - 5): t + 1]))
        lines.append(f"  t={t:2d}  context ...{ctx:<45s} -> target: {tok.itos[ids[t + 1]]}")
    lines += ["", f"Tensor view: input = ids[:-1] (len {len(ids) - 1}), target = ids[1:] (len {len(ids) - 1})",
              f"First 15 input ids : {ids[:15]}", f"First 15 target ids: {ids[1:16]}",
              f"Special ids: pad={tok.pad_id} unk={tok.unk_id} bos={tok.bos_id} eos={tok.eos_id}"]
    out_path(cfg, "examples", "input_target_pairs.txt").write_text("\n".join(lines) + "\n")
    lens = [len(tok.tokenize(r["text"])) + 2 for r in splits["train"]]
    pd.Series(lens).to_csv(out_path(cfg, "examples", "train_story_lengths.csv"), index=False, header=["tokens"])


def build_loaders(cfg, tok, splits):
    scfg = cfg["sequences"]
    datasets = {name: StoryLMDataset([r["text"] for r in rows], tok, scfg["max_len"]) for name, rows in splits.items()}
    loaders = {name: make_loader(ds, tok.pad_id, scfg["max_tokens_per_batch"], shuffle=(name == "train"),
                                 seed=cfg["seed"]) for name, ds in datasets.items()}
    return loaders


def stage_train(cfg, log, args):
    from .train import train_model

    device = get_device()
    tok = WordTokenizer.load(out_path(cfg, "vocab.json"))
    loaders = build_loaders(cfg, tok, data_mod.load_splits(cfg))
    cells = MODELS if args.model == "both" else (args.model,)
    for cell in cells:
        log(f"training {cell} on {device} ({len(loaders['train'])} batches/epoch)")
        history, summary = train_model(cell, cfg, tok, loaders["train"], loaders["val"], device,
                                       out_path(cfg, "checkpoints", f"{cell}.pt"), log)
        save_json(history, out_path(cfg, "training", f"{cell}_history.json"))
        save_json(summary, out_path(cfg, "training", f"{cell}_summary.json"))
        log(f"{cell}: best val ppl {summary['best_val_ppl']:.2f} at epoch {summary['best_epoch']}, "
            f"{summary['train_seconds'] / 60:.1f} min")


def stage_evaluate(cfg, log, args):
    from .train import evaluate, load_model

    device = get_device()
    tok = WordTokenizer.load(out_path(cfg, "vocab.json"))
    loaders = build_loaders(cfg, tok, data_mod.load_splits(cfg))
    results = {}
    for cell in MODELS:
        model, ckpt = load_model(out_path(cfg, "checkpoints", f"{cell}.pt"), cfg, tok, device)
        res = {"best_epoch": ckpt["epoch"]}
        for split in ("val", "test"):
            r = evaluate(model, loaders[split], tok.pad_id, device, cfg, max_len=cfg["sequences"]["max_len"])
            res[split] = {"loss": r["loss"], "ppl": r["ppl"], "tokens": r["tokens"]}
            res[f"{split}_per_position_loss"] = r["per_position_loss"]
            res[f"{split}_per_position_count"] = r["per_position_count"]
        results[cell] = res
        log(f"{cell}: val ppl {res['val']['ppl']:.2f}  test ppl {res['test']['ppl']:.2f}")
    save_json(results, out_path(cfg, "eval", "perplexity.json"))


def stage_generate(cfg, log, args):
    from .generate import run_generation_grid
    from .train import load_model

    path = out_path(cfg, "generations", "generations.jsonl")
    write_once(path, args.force)
    device = get_device()
    tok = WordTokenizer.load(out_path(cfg, "vocab.json"))
    models = {cell: load_model(out_path(cfg, "checkpoints", f"{cell}.pt"), cfg, tok, device)[0] for cell in MODELS}
    start = time.time()
    rows = run_generation_grid(models, tok, get_prompts(), cfg, device, log)
    save_jsonl(rows, path)
    save_json({"generation": cfg["generation"], "device": str(device), "seconds": time.time() - start,
               "created": timestamp()}, out_path(cfg, "generations", "generation_settings.json"))
    log(f"saved {len(rows)} generations to {path}")


def stage_llm(cfg, log, args):
    from .llm_baseline import run_llm

    if not cfg["llm"]["enabled"]:
        log("llm.enabled is false; skipping")
        return
    path = out_path(cfg, "generations", "llm_generations.jsonl")
    write_once(path, args.force)
    tok = WordTokenizer.load(out_path(cfg, "vocab.json"))
    rows, meta = run_llm(cfg, get_prompts("part4"), tok, get_device(), log)
    save_jsonl(rows, path)
    save_json(meta, out_path(cfg, "generations", "llm_settings.json"))
    log(f"saved {len(rows)} LLM generations")


def all_generations(cfg):
    rows = load_jsonl(out_path(cfg, "generations", "generations.jsonl"))
    llm_path = out_path(cfg, "generations", "llm_generations.jsonl")
    if llm_path.exists():
        rows += load_jsonl(llm_path)
    return rows


def stage_metrics(cfg, log, args):
    rows = all_generations(cfg)
    thr = cfg["generation"]["premature_threshold"]
    sample_table(rows, thr).to_csv(out_path(cfg, "tables", "sample_metrics.csv"), index=False)
    group_table(rows, thr).to_csv(out_path(cfg, "tables", "decoding_metrics.csv"), index=False)
    group_table(rows, thr, by=("system",)).to_csv(out_path(cfg, "tables", "system_metrics_all_configs.csv"),
                                                  index=False)
    p4 = [r for r in rows if r["group"] == "part4"]
    group_table(p4, thr).to_csv(out_path(cfg, "tables", "plot_twist_metrics.csv"), index=False)
    write_story_files(cfg, rows)
    log("metrics + story files written")


def write_story_files(cfg, rows):
    """Readable dumps of every generation, grouped by prompt. Text is copied verbatim from the JSONL."""
    order = [c["name"] for c in cfg["generation"]["configs"]]
    for group, title in (("part3", "Part 3: decoding-strategy comparison"),
                         ("part4", "Part 4: Plot-Twist Challenge")):
        lines = [f"# {title}: all generated continuations", "",
                 "Everything inside a quote block is **model-generated and unedited** (detokenised from the "
                 "saved tokens). Failed, repetitive and incoherent outputs are included on purpose. "
                 "Source: `outputs/generations/*.jsonl`.", ""]
        for prompt in get_prompts(group):
            lines += [f"## {prompt['id']} ({prompt['theme']})", "", f"**Opening (human-written):** {prompt['text']}", ""]
            oov = next((r["prompt_oov"] for r in rows if r["prompt_id"] == prompt["id"] and r["system"] == "lstm"), [])
            lines += [f"Prompt words outside the RNN/LSTM vocabulary (seen as `<unk>`): {', '.join(oov) or 'none'}", ""]
            for system in ("rnn", "lstm", "llm"):
                sys_rows = [r for r in rows if r["prompt_id"] == prompt["id"] and r["system"] == system]
                if not sys_rows:
                    continue
                lines += [f"### {MODEL_LABEL[system]}", ""]
                sys_rows.sort(key=lambda r: (order.index(r["config"]) if r["config"] in order else 99, r["seed"]))
                for r in sys_rows:
                    lines += [f"**{r['config']}, seed {r['seed']}** ({r['n_tokens']} tokens, stop: {r['stop_reason']})", "",
                              "> " + (r["text"] or "*(empty: model emitted end-of-story immediately)*"), ""]
        out_path(cfg, "stories", f"{group}_stories.md").write_text("\n".join(lines))


def stage_human_sheet(cfg, log, args):
    from .human_eval import build_sheet

    samples = build_sheet(all_generations(cfg), cfg, out_path(cfg, "human_eval", "x").parent)
    counts = pd.Series([s["system"] for s in samples]).value_counts().to_dict()
    log(f"human-eval sheet: {len(samples)} samples {counts}")


def stage_human_analyze(cfg, log, args):
    from .human_eval import analyze, overall_mean, summary_for_latex

    samples = pd.read_csv(out_path(cfg, "tables", "sample_metrics.csv"))
    tables = analyze(out_path(cfg, "human_eval", "x").parent, samples)
    summary_for_latex(tables).to_latex(out_path(cfg, "tables", "human_eval.tex"), index=False, escape=False)
    tables["agreement"].to_latex(out_path(cfg, "tables", "human_agreement.tex"), index=False, float_format="%.2f")
    log(f"human eval overall means: {overall_mean(tables)}")
    log(f"agreement: {tables['agreement'].to_dict('records')}")


def stage_report_assets(cfg, log, args):
    from .figures import make_figures, make_tables

    make_figures(cfg)
    make_tables(cfg)
    log("figures + LaTeX tables written")


STAGES = {"prepare": stage_prepare, "train": stage_train, "evaluate": stage_evaluate, "generate": stage_generate,
          "llm": stage_llm, "metrics": stage_metrics, "human-sheet": stage_human_sheet,
          "human-analyze": stage_human_analyze, "report-assets": stage_report_assets}
ALL = ["prepare", "train", "evaluate", "generate", "llm", "metrics", "human-sheet", "report-assets"]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("stage", choices=[*STAGES, "all"])
    parser.add_argument("--config", default="configs/default.yaml")
    parser.add_argument("--model", default="both", choices=["rnn", "lstm", "both"])
    parser.add_argument("--set", nargs="*", default=[], metavar="KEY=VALUE",
                        help="override config values, e.g. --set train.epochs=1 data.n_train=500")
    parser.add_argument("--force", action="store_true", help="allow overwriting generated text")
    args = parser.parse_args(argv)

    overrides = dict(kv.split("=", 1) for kv in args.set)
    cfg = load_config(args.config, {k: yaml.safe_load(v) for k, v in overrides.items()})
    set_seed(cfg["seed"])
    log = Logger(cfg)
    save_json({"config": cfg, "args": vars(args), "hardware": hardware_info(), "time": timestamp()},
              out_path(cfg, "configs_used", f"{args.stage}_{time.strftime('%Y%m%d_%H%M%S')}.json"))
    for stage in (ALL if args.stage == "all" else [args.stage]):
        log(f"=== stage: {stage} ===")
        STAGES[stage](cfg, log, args)
    if args.stage in ("prepare", "all"):
        # The HF streaming reader leaves background threads that can crash the interpreter at
        # shutdown after all outputs are written; exit hard so the exit status stays 0.
        sys.stdout.flush()
        os._exit(0)


if __name__ == "__main__":
    main()
