"""Automatic metrics for generated continuations (prompt tokens are never counted).

Definitions (as reported):
- Word tokens: alphabetic tokens and clitics; punctuation is excluded from diversity/repetition.
- Distinct-n (per sample): unique n-grams / total n-grams of word tokens in one continuation.
- Distinct-n (pooled): same ratio over all continuations of one system+config; n-grams never
  cross sample boundaries.
- Repetition rate (rep-4): 1 - Distinct-4 of one continuation, i.e. the share of its 4-grams
  that repeat an earlier 4-gram of the same continuation. Undefined for < 4 word tokens.
- Sentence repetition: share of sentences that exactly repeat an earlier sentence of the sample.
- Premature termination: <eos> generated within `premature_threshold` tokens.
- Runaway: the max_new_tokens limit was reached without <eos>.
- Prompt overlap: share of the prompt's content words that reappear in the continuation
  (a crude relevance proxy; it cannot detect paraphrase).
"""
import math

import numpy as np
import pandas as pd

from .tokenizer import is_word

STOPWORDS = set("""
a an the and or but if then so to of in on at by for with from up down out over under again into
is am are was were be been being have has had do does did will would can could should may might must
i me my we our you your he him his she her it its they them their this that these those there here
what which who whom when where why how all any both each few more most other some such no not only
own same than too very just also as about after before because while once said says say one went
""".split())


def ngrams(seq, n):
    return list(zip(*(seq[i:] for i in range(n))))


def distinct_n(seq, n):
    grams = ngrams(seq, n)
    return len(set(grams)) / len(grams) if grams else math.nan


def repetition_rate(seq, n=4):
    d = distinct_n(seq, n)
    return math.nan if math.isnan(d) else 1.0 - d


def sentences(tokens):
    out, cur = [], []
    for tok in tokens:
        cur.append(tok)
        if tok in (".", "!", "?"):
            out.append(tuple(cur))
            cur = []
    if cur:
        out.append(tuple(cur))
    return [s for s in out if any(is_word(t) for t in s)]


def sentence_repeat_rate(tokens):
    sents = sentences(tokens)
    if not sents:
        return math.nan
    seen, repeats = set(), 0
    for s in sents:
        repeats += s in seen
        seen.add(s)
    return repeats / len(sents)


def prompt_overlap(prompt_tokens, tokens):
    content = {t for t in prompt_tokens if is_word(t) and t not in STOPWORDS}
    if not content:
        return math.nan
    return len(content & set(tokens)) / len(content)


def sample_metrics(row, premature_threshold):
    words = [t for t in row["tokens"] if is_word(t)]
    return {
        "n_tokens": row["n_tokens"],
        "n_words": len(words),
        "distinct_1": distinct_n(words, 1),
        "distinct_2": distinct_n(words, 2),
        "rep_4": repetition_rate(words, 4),
        "sent_repeat": sentence_repeat_rate(row["tokens"]),
        "premature": row["stop_reason"] == "eos" and row["n_tokens"] < premature_threshold,
        "runaway": row["stop_reason"] == "max_len",
        "prompt_overlap": prompt_overlap(row["prompt_tokens"], row["tokens"]),
    }


def pooled_distinct(token_lists, n):
    unique, total = set(), 0
    for toks in token_lists:
        words = [t for t in toks if is_word(t)]
        grams = ngrams(words, n)
        total += len(grams)
        unique.update(grams)
    return len(unique) / total if total else math.nan


def sample_table(rows, premature_threshold):
    keys = ["system", "prompt_id", "group", "config", "seed", "stop_reason"]
    return pd.DataFrame([{**{k: r[k] for k in keys}, **sample_metrics(r, premature_threshold)} for r in rows])


def group_table(rows, premature_threshold, by=("system", "config")):
    samples = sample_table(rows, premature_threshold)
    out = []
    for key, grp in samples.groupby(list(by), sort=False):
        idx = grp.index
        toks = [rows[i]["tokens"] for i in idx]
        out.append({
            **dict(zip(by, key)),
            "n": len(grp),
            "distinct_1_pooled": pooled_distinct(toks, 1),
            "distinct_2_pooled": pooled_distinct(toks, 2),
            "distinct_1_mean": grp["distinct_1"].mean(),
            "distinct_2_mean": grp["distinct_2"].mean(),
            "rep_4": grp["rep_4"].mean(),
            "sent_repeat": grp["sent_repeat"].mean(),
            "len_mean": grp["n_tokens"].mean(),
            "len_std": grp["n_tokens"].std(ddof=0),
            "premature_pct": 100 * grp["premature"].mean(),
            "runaway_pct": 100 * grp["runaway"].mean(),
            "prompt_overlap": grp["prompt_overlap"].mean(),
        })
    return pd.DataFrame(out)


def describe_lengths(values):
    arr = np.asarray(values)
    return {"mean": float(arr.mean()), "median": float(np.median(arr)), "p95": float(np.percentile(arr, 95)),
            "max": int(arr.max()), "min": int(arr.min())}
