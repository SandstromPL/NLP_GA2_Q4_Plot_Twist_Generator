# Implementation Flow: Plot-Twist Generator (NLP GA2, Q4)

This file follows the implementation from raw data to final report: what runs, in what order,
which file does it, and which part of the brief it answers. It is updated as the work progresses.

## 1. Pipeline at a glance

```
TinyStories (HF, streamed)
   │  prepare        clean → drop short → exact dedupe → shuffle(seed 42) → 20k / 1k / 1k stories
   ▼
word tokenizer (train split only, min_freq 3)  →  outputs/vocab.json
   │                one sequence per story: <bos> … <eos>, windows of ≤512 tokens inside a story
   ▼
train --model rnn   Embedding(256) → RNN(512, 2 layers, tanh) → Linear(V)    ┐ same data, vocab,
train --model lstm  Embedding(256) → LSTM(512, 2 layers)      → Linear(V)    ┘ optimiser, seed
   │                                                    → outputs/checkpoints/{rnn,lstm}.pt
   ▼
evaluate            val + test perplexity, loss by position in story       → outputs/eval/
   ▼
generate            10 prompts × 10 decoding configs × 5 seeds × 2 models   → outputs/generations/
llm (optional)      Qwen2.5-0.5B-Instruct, zero-shot, Part 4 prompts
   ▼
metrics             Distinct-1/2, rep-4, sentence repeats, length failures  → outputs/tables/
   ▼                readable story dumps                                    → outputs/stories/
human-sheet         blinded sheet (25 samples) + hidden key                 → outputs/human_eval/
   ▼   (evaluators fill ratings/<name>.csv)
human-analyze       means, Krippendorff's α, disagreements, Wilcoxon, metric↔human correlation
   ▼
report-assets       figures (PNG) + LaTeX tables                            → outputs/figures, tables
   ▼
report/             LaTeX report on Overleaf; README; submission zip
```

Run everything: `PYTHONPATH=src .venv/bin/python -m ptg.cli all` (then `human-analyze` once
ratings exist). Each stage can also be run alone, e.g. `python -m ptg.cli train --model lstm`.

## 2. Stage-by-stage mapping to the brief

| Step | Stage / file | Brief requirement covered | Output |
|---|---|---|---|
| 1 | `prepare` · `data.py` | Part 1: documented subset; story-level split **before** sequences; cleaning | `data/splits.json`, `outputs/data_stats.json` |
| 2 | `prepare` · `tokenizer.py` | Part 1: tokenisation, vocabulary, rare/unknown words, `<pad> <unk> <bos> <eos>` | `outputs/vocab.json` |
| 3 | `prepare` · `dataset.py` | Part 1: ids, input→target pairs, padding handling | `outputs/examples/input_target_pairs.txt` |
| 4 | `train` · `models.py`, `train.py` | Part 2: both architectures, cross-entropy, loss curves, params, time | `outputs/training/*`, checkpoints |
| 5 | `evaluate` · `train.py` | Part 2 + Part 5: final val perplexity, test perplexity | `outputs/eval/perplexity.json` |
| 6 | `generate` · `generate.py`, `prompts.py` | Part 3: greedy, temperature (0.5/0.8/1.0/1.2), top-k (10/40) + extra top-p, rep. penalty; ≥5 prompts | `outputs/generations/generations.jsonl` |
| 7 | `generate` (Part 4 prompts) | Part 4: 5 twist openings × both models × ≥2 strategies | `outputs/stories/part4_stories.md` |
| 8 | `llm` · `llm_baseline.py` | Optional extension: checkpoint, template, decoding, precision, hardware recorded | `llm_generations.jsonl`, `llm_settings.json` |
| 9 | `metrics` · `metrics.py` | Part 5: Distinct-1/2, repetition rate, length + premature/runaway rates | `outputs/tables/*.csv` |
| 10 | `human-sheet` · `human_eval.py` | Part 5: blinded set of ≥10 samples, 5-point scale, 4 criteria | `outputs/human_eval/sheet.html/.csv` |
| 11 | `human-analyze` · `human_eval.py` | Part 5: averages, disagreement, PPL vs human ratings | `outputs/human_eval/results_*.csv` |
| 12 | `report-assets` · `figures.py` | Deliverables: curves, comparison tables | `outputs/figures/`, `outputs/tables/*.tex` |
| 13 | `report/` | Part 6: answers to the 7 analysis questions | `report/main.tex` |

## 3. Key design decisions (and why)

- **Story-level split before sequences.** Stories are shuffled and split as whole units, and
  windows are only cut afterwards, inside one story. No text can leak across splits. Exact
  duplicates are removed first; 50 were found in the 40k pool.
- **One sequence per story, `<bos>`/`<eos>` on every story.** The model never sees story A run
  into story B. That is what lets it learn when a story *ends*, which the premature/runaway
  metrics depend on. Stories longer than 512 tokens (≈2%) become windows of the same story.
- **Padding.** Batches are right-padded with `<pad>` (id 0). Targets at pad positions are ignored
  by the loss (`ignore_index=0`). Because the models are causal (left-to-right), padding placed
  after the real tokens cannot change any real prediction, so packing is not needed. A
  token-budget sampler groups windows of similar length to keep padding small.
- **Same everything for both models.** Same vocabulary, emb 256, hidden 512, 2 layers, dropout
  0.3, AdamW 1e-3, grad-clip 1.0, ReduceLROnPlateau, early stopping (patience 2), seed 42.
  The one unavoidable difference: the LSTM has 4× the recurrent weights (4 gates), so it has
  more parameters overall. This is reported in the model table.
- **`<unk>` is banned while decoding** (along with `<pad>`, `<bos>`). It can still appear in a
  *prompt*: out-of-vocabulary prompt words are listed for every prompt.
- **Write-once generations.** `generate` refuses to overwrite its JSONL without `--force`.
  Story dumps quote the saved text verbatim, and every failure is included.
- **Blinding.** Every system, LLM included, goes through the same word tokenizer, lowercasing,
  detokeniser and 150-token cap before evaluators see it. The sample → system key lives in
  `key_DO_NOT_SHARE.csv`. The selection rule (Part 4 prompts, `temp_0.8` + `topk_40`, seed 0) was
  fixed in the config before any output was read.
- **LLM decoding is fully explicit.** Qwen's own `generation_config` would otherwise switch on
  top-p and a repetition penalty. We force `repetition_penalty=1.0`, `top_p=1.0`, and the same
  temperature and top-k as `topk_40`.

## 4. Metric definitions (exactly as implemented in `metrics.py`)

- Perplexity = exp(mean NLL over non-pad target tokens, `<eos>` included; `<bos>` is never a target).
- Word tokens = alphabetic tokens and clitics; punctuation is excluded from diversity and repetition.
- Distinct-n per sample = unique n-grams / total n-grams of one continuation. **Pooled** = the same
  over all continuations of one system+config (n-grams never cross samples).
- Repetition rate (rep-4) = 1 − Distinct-4 of a continuation.
- Sentence repetition = share of sentences that exactly repeat an earlier sentence of the sample.
- Premature = `<eos>` within 20 tokens. Runaway = reached 150 tokens without `<eos>`.
- Prompt overlap = share of the prompt's content words reused in the continuation (relevance proxy).

## 5. Status log

| Time (2026-10-30) | Done |
|---|---|
| 13:37 | Decisions locked: word-level tokens, laptop GPU (Colab-compatible), Qwen2.5-0.5B, LaTeX |
| 13:50 | Environment: `.venv` with torch 2.14.1+cu126 on RTX 3050 Ti; git initialised by user |
| 13:57 | Smoke test of the full pipeline on 1k stories (2 epochs) passed, LLM included |
| 13:59 | Human-eval analysis exercised with throwaway random ratings (scratch folder only) |
| 14:00 | Code committed (`8ce6ad4`); full run started on GPU |
| 14:03 | README, requirements, report skeleton, notebook builder, submission script (`d0c8037`) |
| 14:04 | `report-assets` now also writes verbatim LaTeX example boxes and copies figures/tables into `report/`; report skeleton compiles with pdflatex |

## 6. Remaining

- [ ] Full run finishes; sanity-check numbers and generations
- [ ] Send `outputs/human_eval/sheet.html` + `ratings/TEMPLATE.csv` to 3 evaluators
- [ ] Run `human-analyze` once ratings return
- [ ] Results notebook (executed, with outputs)
- [ ] README with setup and reproduce commands
- [ ] LaTeX report (Overleaf) answering Part 6 Q1–Q7
- [ ] Submission zip (code, notebook, checkpoints, vocab, outputs, report; no dataset)
