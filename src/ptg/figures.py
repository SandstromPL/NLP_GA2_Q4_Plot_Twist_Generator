"""Figures (PNG) and LaTeX tables for the report, built only from files under outputs/."""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from .utils import load_json, out_path

COLORS = {"rnn": "#d95f02", "lstm": "#1b9e77", "llm": "#7570b3"}
LABELS = {"rnn": "Vanilla RNN", "lstm": "LSTM", "llm": "Qwen2.5-0.5B"}


def _save(fig, cfg, name):
    fig.tight_layout()
    fig.savefig(out_path(cfg, "figures", name), dpi=160)
    plt.close(fig)


def make_figures(cfg):
    hist = {c: load_json(out_path(cfg, "training", f"{c}_history.json")) for c in ("rnn", "lstm")}

    fig, axes = plt.subplots(1, 2, figsize=(10, 3.6))
    for c, h in hist.items():
        ep = [r["epoch"] for r in h["epochs"]]
        axes[0].plot(ep, [r["train_loss"] for r in h["epochs"]], "--o", ms=3, color=COLORS[c], label=f"{LABELS[c]} train")
        axes[0].plot(ep, [r["val_loss"] for r in h["epochs"]], "-o", ms=3, color=COLORS[c], label=f"{LABELS[c]} val")
        axes[1].plot(ep, [r["val_ppl"] for r in h["epochs"]], "-o", ms=3, color=COLORS[c], label=LABELS[c])
    axes[0].set(xlabel="epoch", ylabel="cross-entropy loss", title="Training and validation loss")
    axes[1].set(xlabel="epoch", ylabel="perplexity", title="Validation perplexity")
    for ax in axes:
        ax.legend(fontsize=8)
        ax.grid(alpha=0.3)
    _save(fig, cfg, "loss_curves.png")

    fig, ax = plt.subplots(figsize=(6, 3.4))
    for c, h in hist.items():
        steps = [s["step"] for s in h["steps"]]
        ax.plot(steps, [s["train_loss"] for s in h["steps"]], color=COLORS[c], lw=1, label=LABELS[c])
    ax.set(xlabel="optimizer step", ylabel="train loss (batch)", title="Training loss per step")
    ax.legend()
    ax.grid(alpha=0.3)
    _save(fig, cfg, "train_loss_steps.png")

    fig, ax = plt.subplots(figsize=(6, 3.4))
    for c, h in hist.items():
        ax.plot([s["step"] for s in h["steps"]], [s["grad_norm"] for s in h["steps"]], color=COLORS[c], lw=1,
                label=LABELS[c])
    ax.axhline(cfg["train"]["grad_clip"], color="grey", ls=":", label="clip threshold")
    ax.set(xlabel="optimizer step", ylabel="gradient norm (before clipping)", yscale="log",
           title="Gradient norms during training")
    ax.legend()
    ax.grid(alpha=0.3)
    _save(fig, cfg, "grad_norms.png")

    ppl = load_json(out_path(cfg, "eval", "perplexity.json"))
    fig, ax = plt.subplots(figsize=(6, 3.4))
    bin_size = 16
    for c in ("rnn", "lstm"):
        loss = np.array(ppl[c]["test_per_position_loss"], dtype=float)
        cnt = np.array(ppl[c]["test_per_position_count"], dtype=float)
        n_bins = len(loss) // bin_size
        xs, ys = [], []
        for b in range(n_bins):
            sl = slice(b * bin_size, (b + 1) * bin_size)
            if cnt[sl].sum() >= 200:
                xs.append(b * bin_size + bin_size / 2)
                ys.append(np.nansum(loss[sl] * cnt[sl]) / cnt[sl].sum())
        ax.plot(xs, ys, "-o", ms=3, color=COLORS[c], label=LABELS[c])
    ax.set(xlabel="token position in story", ylabel="mean test loss",
           title="Loss vs. position (more context ->?)")
    ax.legend()
    ax.grid(alpha=0.3)
    _save(fig, cfg, "loss_by_position.png")

    dec = pd.read_csv(out_path(cfg, "tables", "decoding_metrics.csv"))
    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    for system, grp in dec.groupby("system"):
        ax.scatter(grp["distinct_2_pooled"], grp["rep_4"], color=COLORS[system], label=LABELS[system], s=30)
        for _, r in grp.iterrows():
            ax.annotate(r["config"], (r["distinct_2_pooled"], r["rep_4"]), fontsize=6, xytext=(3, 2),
                        textcoords="offset points")
    ax.set(xlabel="Distinct-2 (pooled)", ylabel="repetition rate (rep-4)", title="Diversity vs. repetition by decoding config")
    ax.legend()
    ax.grid(alpha=0.3)
    _save(fig, cfg, "diversity_vs_repetition.png")

    temp_cfgs = ["greedy", "temp_0.5", "temp_0.8", "temp_1.0", "temp_1.2"]
    temp_x = [0.0, 0.5, 0.8, 1.0, 1.2]
    fig, axes = plt.subplots(1, 3, figsize=(11, 3.3))
    for system in ("rnn", "lstm"):
        sub = dec[dec.system == system].set_index("config").reindex(temp_cfgs)
        axes[0].plot(temp_x, sub["distinct_2_pooled"], "-o", color=COLORS[system], label=LABELS[system])
        axes[1].plot(temp_x, sub["rep_4"], "-o", color=COLORS[system], label=LABELS[system])
        axes[2].plot(temp_x, sub["runaway_pct"], "-o", color=COLORS[system], label=f"{LABELS[system]} runaway")
        axes[2].plot(temp_x, sub["premature_pct"], ":s", color=COLORS[system], label=f"{LABELS[system]} premature")
    for ax, title in zip(axes, ["Distinct-2 (pooled)", "Repetition rate (rep-4)", "Length failures (%)"]):
        ax.set(xlabel="temperature (0 = greedy)", title=title)
        ax.grid(alpha=0.3)
    axes[2].legend(fontsize=7)
    axes[0].legend(fontsize=8)
    _save(fig, cfg, "temperature_effect.png")

    lens = pd.read_csv(out_path(cfg, "examples", "train_story_lengths.csv"))["tokens"]
    fig, ax = plt.subplots(figsize=(6, 3.2))
    ax.hist(lens, bins=60, color="#666")
    ax.axvline(cfg["sequences"]["max_len"] + 1, color="red", ls="--", label="window size")
    ax.set(xlabel="tokens per story (incl. <bos>/<eos>)", ylabel="stories", title="Train story lengths")
    ax.legend()
    _save(fig, cfg, "story_lengths.png")


def _fmt_int(n):
    return f"{n / 1e6:.2f}M"


def make_tables(cfg):
    ppl = load_json(out_path(cfg, "eval", "perplexity.json"))
    rows = []
    for c in ("rnn", "lstm"):
        s = load_json(out_path(cfg, "training", f"{c}_summary.json"))
        p = s["parameters"]
        rows.append({"Model": LABELS[c], "Params (total)": _fmt_int(p["total"]),
                     "Recurrent params": _fmt_int(p["recurrent"]), "Epochs run": s["epochs_run"],
                     "Best epoch": s["best_epoch"], "Train time (min)": f"{s['train_seconds'] / 60:.1f}",
                     "Val PPL": f"{ppl[c]['val']['ppl']:.2f}", "Test PPL": f"{ppl[c]['test']['ppl']:.2f}"})
    pd.DataFrame(rows).to_latex(out_path(cfg, "tables", "model_summary.tex"), index=False)
    pd.DataFrame(rows).to_csv(out_path(cfg, "tables", "model_summary.csv"), index=False)

    cols = {"system": "System", "config": "Config", "distinct_1_pooled": "D-1", "distinct_2_pooled": "D-2",
            "rep_4": "Rep-4", "sent_repeat": "Sent.rep", "len_mean": "Len", "premature_pct": "Prem.\\%",
            "runaway_pct": "Runaway\\%", "prompt_overlap": "Overlap"}
    for name in ("decoding_metrics", "plot_twist_metrics"):
        df = pd.read_csv(out_path(cfg, "tables", f"{name}.csv"))
        df["system"] = df["system"].map(LABELS)
        df["config"] = df["config"].str.replace("_", r"\_", regex=False)
        df[list(cols)].rename(columns=cols).to_latex(out_path(cfg, "tables", f"{name}.tex"), index=False,
                                                     float_format="%.2f", escape=False)

    stats = load_json(out_path(cfg, "data_stats.json"))
    v, sp = stats["vocab"], stats["splits"]
    seq = stats["sequences"]
    data_rows = [
        ("Stories streamed (HF train, in order)", sp["streamed"]),
        ("Dropped: too short / exact duplicates", f"{sp['dropped_short']} / {sp['dropped_duplicates']}"),
        ("Train / val / test stories", f"{sp['n_train']} / {sp['n_val']} / {sp['n_test']}"),
        ("Train tokens", f"{v['train_tokens']:,}"),
        ("Word types in train / vocabulary size", f"{v['train_types']:,} / {v['vocab_size']:,}"),
        ("Train tokens covered by vocabulary", f"{100 * v['train_tokens_covered']:.2f}\\%"),
        ("\\texttt{<unk>} rate val / test", f"{100 * v['unk_rate_val']:.2f}\\% / {100 * v['unk_rate_test']:.2f}\\%"),
        ("Mean / max train story length (tokens)",
         f"{seq['train']['story_length_tokens']['mean']:.0f} / {seq['train']['story_length_tokens']['max']}"),
        ("Train stories split into >1 window", f"{seq['train']['stories_split_into_windows']} "
                                               f"({seq['train']['pct_split']:.2f}\\%)"),
    ]
    pd.DataFrame(data_rows, columns=["Quantity", "Value"]).to_latex(
        out_path(cfg, "tables", "data_stats.tex"), index=False, escape=False)


LATEX_ESCAPES = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
                 "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}


def latex_escape(text):
    return "".join(LATEX_ESCAPES.get(ch, ch) for ch in text)


def make_example_snippets(cfg):
    """LaTeX boxes with generated text copied verbatim from the JSONL files (only LaTeX-escaped)."""
    from .prompts import get_prompts
    from .utils import load_jsonl

    rows = load_jsonl(out_path(cfg, "generations", "generations.jsonl"))
    llm_path = out_path(cfg, "generations", "llm_generations.jsonl")
    rows += load_jsonl(llm_path) if llm_path.exists() else []
    index = {(r["system"], r["prompt_id"], r["config"], r["seed"]): r for r in rows}

    def box(system, pid, config, seed=0):
        r = index.get((system, pid, config, seed))
        if r is None:
            return ""
        body = latex_escape(r["text"]) if r["text"] else r"\textit{(empty: \texttt{<eos>} generated immediately)}"
        title = f"{LABELS[system]}, {config.replace('_', ' ')}, seed {seed} ({r['n_tokens']} tokens, stop: {r['stop_reason']})"
        return f"\\begin{{modelout}}{{{latex_escape(title)}}}\n\\small {body}\n\\end{{modelout}}\n"

    specs = {
        "examples_part3": [(p["id"], ["greedy", "temp_0.5", "temp_0.8", "temp_1.2", "topk_40", "topk_40_rep1.2"])
                           for p in get_prompts("part3")[:2]],
        "examples_part4": [(p["id"], ["greedy", "temp_0.8", "topk_40"]) for p in get_prompts("part4")],
    }
    prompts = {p["id"]: p for p in get_prompts()}
    for name, items in specs.items():
        parts = []
        for pid, configs in items:
            p = prompts[pid]
            parts.append(f"\\subsubsection*{{{latex_escape(pid.replace('_', ' '))} ({latex_escape(p['theme'])})}}\n"
                         f"\\human{{Opening (human-written): {latex_escape(p['text'])}}}\n")
            for system in ("rnn", "lstm", "llm"):
                for config in configs:
                    parts.append(box(system, pid, config))
        out_path(cfg, "tables", f"{name}.tex").write_text("\n".join(parts))
