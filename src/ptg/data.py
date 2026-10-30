"""Load TinyStories, clean it, remove duplicates and split it at the story level.

Only the HF row indices of each split are saved in the repo (data.splits_file); the cleaned
texts go to data/cache/, which is git-ignored and never submitted.
"""
import random
import re
import unicodedata
from pathlib import Path

from .utils import load_jsonl, save_json, save_jsonl

# Mis-decoded UTF-8 sequences that occur in TinyStories, checked longest first.
MOJIBAKE = {
    "â€™": "'", "â€˜": "'", "â€œ": '"', "â€\x9d": '"', "â€”": " - ", "â€“": " - ",
    "â€¦": "...", "â€": '"', "Â": "",
}
PUNCT_MAP = {
    "‘": "'", "’": "'", "“": '"', "”": '"', "–": " - ", "—": " - ",
}


def clean_text(text):
    for bad, good in MOJIBAKE.items():
        text = text.replace(bad, good)
    text = unicodedata.normalize("NFKC", text)
    for bad, good in PUNCT_MAP.items():
        text = text.replace(bad, good)
    text = re.sub(r"[^\x20-\x7E]", " ", text)  # drop any remaining non-ASCII characters
    return re.sub(r"\s+", " ", text).strip()


def dedupe_key(text):
    return re.sub(r"\s+", " ", text.lower()).strip()


def stream_pool(cfg):
    from datasets import load_dataset

    dcfg = cfg["data"]
    stream = load_dataset(dcfg["hf_name"], split=dcfg["hf_split"], streaming=True)
    pool = []
    for idx, row in enumerate(stream):
        if idx >= dcfg["pool_size"]:
            break
        pool.append({"hf_index": idx, "text": row["text"]})
    return pool


def prepare_splits(cfg):
    """Stream -> clean -> drop short -> exact dedupe -> shuffle -> story-level split."""
    dcfg = cfg["data"]
    pool = stream_pool(cfg)
    stats = {"streamed": len(pool)}

    seen, kept, n_short, n_dup = set(), [], 0, 0
    for row in pool:
        text = clean_text(row["text"])
        if len(text.split()) < dcfg["min_words"]:
            n_short += 1
            continue
        key = dedupe_key(text)
        if key in seen:
            n_dup += 1
            continue
        seen.add(key)
        kept.append({"hf_index": row["hf_index"], "text": text})
    stats.update(dropped_short=n_short, dropped_duplicates=n_dup, unique_clean=len(kept))

    needed = dcfg["n_train"] + dcfg["n_val"] + dcfg["n_test"]
    if len(kept) < needed:
        raise ValueError(f"Only {len(kept)} unique stories in the pool, need {needed}; raise data.pool_size")

    random.Random(cfg["seed"]).shuffle(kept)
    splits = {
        "train": kept[: dcfg["n_train"]],
        "val": kept[dcfg["n_train"]: dcfg["n_train"] + dcfg["n_val"]],
        "test": kept[dcfg["n_train"] + dcfg["n_val"]: needed],
    }

    # Story-level split: no HF row (and, after dedupe, no identical text) can be in two splits.
    index_sets = {name: {r["hf_index"] for r in rows} for name, rows in splits.items()}
    assert not (index_sets["train"] & index_sets["val"] or index_sets["train"] & index_sets["test"]
                or index_sets["val"] & index_sets["test"])

    cache = Path(dcfg["cache_dir"])
    for name, rows in splits.items():
        save_jsonl(rows, cache / f"{name}.jsonl")
    stats.update({f"n_{name}": len(rows) for name, rows in splits.items()})
    save_json({
        "source": f"{dcfg['hf_name']} ({dcfg['hf_split']} split), first {dcfg['pool_size']} rows streamed in order",
        "seed": cfg["seed"],
        "stats": stats,
        "hf_indices": {name: sorted(index_sets[name]) for name in splits},
    }, dcfg["splits_file"])
    return splits, stats


def load_splits(cfg):
    cache = Path(cfg["data"]["cache_dir"])
    return {name: load_jsonl(cache / f"{name}.jsonl") for name in ("train", "val", "test")}
