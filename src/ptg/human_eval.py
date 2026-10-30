"""Blinded human evaluation: build the rating sheet, then aggregate the returned ratings.

Selection rule (fixed before looking at any output): every Plot-Twist (Part 4) prompt x each
system x each config in human_eval.configs, seed human_eval.seed only. Every system's text is
rendered with the same word tokenizer, lowercasing, detokenizer and length cap, so surface
form does not reveal which system wrote it.
"""
import html
import math
import random
from pathlib import Path

import numpy as np
import pandas as pd

CRITERIA = ["coherence", "grammar", "relevance", "creativity"]
RUBRIC = {
    "coherence": "Does the continuation make sense and hang together? (1 = nonsense, 5 = fully coherent)",
    "grammar": "Grammatical, fluent sentences? (1 = mostly broken, 5 = no errors)",
    "relevance": "Is it connected to the opening prompt? (1 = unrelated, 5 = clearly continues the prompt)",
    "creativity": "Is there an interesting development, twist or surprise? (1 = none/dull, 5 = genuinely surprising)",
}


def select_samples(rows, cfg):
    hcfg = cfg["human_eval"]
    chosen = [r for r in rows if r["group"] == hcfg["prompt_group"] and r["config"] in hcfg["configs"]
              and r["seed"] == hcfg["seed"]]
    rng = random.Random(hcfg["shuffle_seed"])
    rng.shuffle(chosen)
    width = len(str(len(chosen)))
    return [{"sample_id": f"S{i + 1:0{width}d}", **r} for i, r in enumerate(chosen)]


def build_sheet(rows, cfg, out_dir):
    out_dir = Path(out_dir)
    (out_dir / "ratings").mkdir(parents=True, exist_ok=True)
    samples = select_samples(rows, cfg)
    pd.DataFrame([{"sample_id": s["sample_id"], "prompt": s["prompt"], "continuation": s["text"]}
                  for s in samples]).to_csv(out_dir / "sheet.csv", index=False)
    pd.DataFrame([{"sample_id": s["sample_id"], "system": s["system"], "config": s["config"],
                   "seed": s["seed"], "prompt_id": s["prompt_id"]} for s in samples]
                 ).to_csv(out_dir / "key_DO_NOT_SHARE.csv", index=False)
    pd.DataFrame({"sample_id": [s["sample_id"] for s in samples], **{c: "" for c in CRITERIA},
                  "comment": ""}).to_csv(out_dir / "ratings" / "TEMPLATE.csv", index=False)

    rubric_html = "".join(f"<li><b>{c}</b>: {html.escape(t)}</li>" for c, t in RUBRIC.items())
    cards = "".join(
        f"<section><h2>{s['sample_id']}</h2><p class='p'><b>Opening (human-written):</b> {html.escape(s['prompt'])}</p>"
        f"<p><b>Continuation (machine-generated, unedited):</b> {html.escape(s['text'])}</p></section>"
        for s in samples)
    (out_dir / "sheet.html").write_text(
        "<!doctype html><html><head><meta charset='utf-8'><title>Story rating sheet</title>"
        "<style>body{font:16px/1.5 system-ui,sans-serif;max-width:46rem;margin:2rem auto;padding:0 1rem}"
        "section{border-top:1px solid #ccc;padding:.5rem 0}.p{color:#444}</style></head><body>"
        "<h1>Story continuation rating</h1><p>Each sample is an opening followed by a machine-generated "
        "continuation. You are not told which system wrote it. Rate every sample from 1 to 5 on:</p>"
        f"<ul>{rubric_html}</ul><p>Fill in your copy of <code>TEMPLATE.csv</code> (one row per sample) and "
        "save it as <code>ratings/&lt;your_name&gt;.csv</code>. Rate independently; do not discuss "
        "samples with other evaluators.</p>" + cards + "</body></html>")
    return samples


def load_ratings(out_dir):
    frames = []
    for path in sorted(Path(out_dir, "ratings").glob("*.csv")):
        if path.stem == "TEMPLATE":
            continue
        df = pd.read_csv(path)
        df["evaluator"] = path.stem
        for c in CRITERIA:
            df[c] = pd.to_numeric(df[c], errors="raise")
            if not df[c].between(1, 5).all():
                raise ValueError(f"{path.name}: {c} has values outside 1-5")
        frames.append(df)
    if not frames:
        raise FileNotFoundError(f"No rating files in {Path(out_dir, 'ratings')} (besides TEMPLATE.csv)")
    return pd.concat(frames, ignore_index=True)


def krippendorff_alpha(ratings, criterion):
    import krippendorff

    table = ratings.pivot_table(index="evaluator", columns="sample_id", values=criterion)
    if len(table) < 2:
        return math.nan
    return float(krippendorff.alpha(reliability_data=table.to_numpy(dtype=float),
                                    level_of_measurement="ordinal"))


def analyze(out_dir, sample_metrics=None):
    """Returns a dict of DataFrames; also writes them as CSV next to the ratings."""
    from scipy.stats import spearmanr, wilcoxon

    out_dir = Path(out_dir)
    key = pd.read_csv(out_dir / "key_DO_NOT_SHARE.csv")
    ratings = load_ratings(out_dir).merge(key, on="sample_id", validate="many_to_one")
    long = ratings.melt(id_vars=["sample_id", "evaluator", "system", "config", "prompt_id"],
                        value_vars=CRITERIA, var_name="criterion", value_name="score")

    by_system = long.groupby(["system", "criterion"])["score"].agg(["mean", "std", "count"]).unstack("criterion")
    by_config = long.groupby(["system", "config", "criterion"])["score"].mean().unstack("criterion")[CRITERIA]
    by_evaluator = long.groupby(["evaluator", "system", "criterion"])["score"].mean().unstack("criterion")[CRITERIA]

    agreement = pd.DataFrame([{"criterion": c, "krippendorff_alpha_ordinal": krippendorff_alpha(ratings, c),
                               "mean_within_sample_sd": ratings.groupby("sample_id")[c].std().mean()}
                              for c in CRITERIA])

    spread = long.groupby(["sample_id", "criterion"])["score"].agg(lambda s: s.max() - s.min()).unstack()
    disagreements = (spread.assign(max_range=spread.max(axis=1)).sort_values("max_range", ascending=False)
                     .merge(key, left_index=True, right_on="sample_id"))

    # Paired LSTM vs RNN test on (prompt, config) cells, using the mean over evaluators.
    cell = long.groupby(["system", "prompt_id", "config", "criterion"])["score"].mean().unstack("system")
    tests = []
    for c in CRITERIA:
        sub = cell.xs(c, level="criterion")
        if {"lstm", "rnn"} <= set(sub.columns):
            pair = sub[["lstm", "rnn"]].dropna()
            diff = pair["lstm"] - pair["rnn"]
            p = wilcoxon(pair["lstm"], pair["rnn"]).pvalue if (diff != 0).any() else math.nan
            tests.append({"criterion": c, "n_pairs": len(pair), "lstm_mean": pair["lstm"].mean(),
                          "rnn_mean": pair["rnn"].mean(), "wilcoxon_p": p})
    tests = pd.DataFrame(tests)

    tables = {"by_system": by_system, "by_config": by_config, "by_evaluator": by_evaluator,
              "agreement": agreement, "disagreements": disagreements, "lstm_vs_rnn": tests}

    if sample_metrics is not None:
        per_sample = long.groupby(["sample_id", "criterion"])["score"].mean().unstack()[CRITERIA].reset_index()
        merged = per_sample.merge(key, on="sample_id").merge(
            sample_metrics, on=["system", "prompt_id", "config", "seed"], how="left")
        corr = []
        for m in ["distinct_2", "rep_4", "n_tokens", "prompt_overlap"]:
            for c in CRITERIA:
                ok = merged[[m, c]].dropna()
                rho, p = spearmanr(ok[m], ok[c]) if len(ok) > 2 else (math.nan, math.nan)
                corr.append({"metric": m, "criterion": c, "spearman_rho": rho, "p": p, "n": len(ok)})
        tables["metric_vs_human"] = pd.DataFrame(corr)

    for name, df in tables.items():
        df.to_csv(out_dir / f"results_{name}.csv")
    return tables


def summary_for_latex(tables, labels=None):
    by = tables["by_system"]
    rows = []
    for system in by.index:
        rows.append({"System": (labels or {}).get(system, system), **{c.capitalize(): f"{by.loc[system, ('mean', c)]:.2f} $\\pm$ "
                                                       f"{by.loc[system, ('std', c)]:.2f}" for c in CRITERIA}})
    return pd.DataFrame(rows)


def overall_mean(tables):
    by = tables["by_system"]
    return {s: float(np.mean([by.loc[s, ("mean", c)] for c in CRITERIA])) for s in by.index}
