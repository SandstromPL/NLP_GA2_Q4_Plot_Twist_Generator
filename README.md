# Plot-Twist Generator: Vanilla RNN vs LSTM story generation

NLP Group Assignment 2, Question 4. Two word-level neural language models (Vanilla RNN and LSTM)
are trained from scratch on a 20k-story TinyStories subset. They continue story openings using
several decoding strategies, and the results are evaluated with automatic metrics and a blinded
human study. Qwen2.5-0.5B-Instruct is an optional, zero-shot comparison baseline.

See `IMPLEMENTATION.md` for the step-by-step pipeline and design decisions, and `report/` for the
technical report.

## Layout

```
configs/default.yaml   every hyper-parameter, seed and decoding setting
src/ptg/               data.py tokenizer.py dataset.py models.py train.py generate.py demo.py
                       metrics.py prompts.py human_eval.py llm_baseline.py figures.py cli.py
notebooks/             results walkthrough notebook (executed, with outputs)
data/splits.json       HF row indices of the train/val/test stories (the dataset itself is NOT included)
outputs/
  vocab.json           tokenizer vocabulary (needed to reload the checkpoints)
  checkpoints/         rnn.pt, lstm.pt (best validation loss)
  training/            per-epoch / per-step history and run summaries
  eval/                validation + test perplexity, loss by position
  generations/         raw generations (JSONL, write-once) + exact generation settings
  stories/             every generation, readable, grouped by prompt (unedited)
  tables/              metric tables (CSV + LaTeX)
  figures/             loss curves, gradient norms, diversity/repetition plots
  human_eval/          blinded sheet, hidden key, ratings/, analysis results
  analysis/            human-written judgements (Part 4 criteria), kept apart from generated text
  run_log.txt          timestamped log of every stage
report/                LaTeX source of the report (upload the folder to Overleaf)
```

## Setup

Local (what we used: Ubuntu, Python 3.12, RTX 3050 Ti 4 GB, CUDA 12.6 wheels):

```bash
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python torch --index-url https://download.pytorch.org/whl/cu126
uv pip install --python .venv/bin/python -r requirements.txt
```

Google Colab (GPU runtime): upload/unzip the project, `cd` into it, then
`pip install -r requirements.txt` and use `python` instead of `.venv/bin/python` below.

## Reproduce

```bash
export PYTHONPATH=src
.venv/bin/python -m ptg.cli all             # prepare → train → evaluate → generate → length-test → llm → metrics → human-sheet → report-assets
```

or stage by stage:

```bash
.venv/bin/python -m ptg.cli prepare         # stream TinyStories, clean, dedupe, split, build vocab
.venv/bin/python -m ptg.cli train --model rnn
.venv/bin/python -m ptg.cli train --model lstm
.venv/bin/python -m ptg.cli evaluate        # val/test perplexity
.venv/bin/python -m ptg.cli generate        # all prompts × decoding configs × seeds (refuses to overwrite; --force)
.venv/bin/python -m ptg.cli length-test     # termination check: first sentence of 100 test stories, up to 600 tokens
.venv/bin/python -m ptg.cli llm             # optional Qwen baseline (set llm.enabled: false to skip)
.venv/bin/python -m ptg.cli metrics         # Distinct-n, repetition, length; story dumps
.venv/bin/python -m ptg.cli human-sheet     # blinded rating sheet
.venv/bin/python -m ptg.cli human-analyze   # after ratings/<name>.csv files are filled in
.venv/bin/python -m ptg.cli report-assets   # figures + LaTeX tables
```

Any config value can be overridden from the command line, e.g. a quick smoke test:
`.venv/bin/python -m ptg.cli all --set output_dir=/tmp/smoke data.n_train=1000 data.n_val=100 data.n_test=100 data.pool_size=3000 train.epochs=2`.
Use a separate `data.cache_dir`/`data.splits_file` too so the real split is not overwritten.

## Try the trained models

```bash
export PYTHONPATH=src
.venv/bin/python -m ptg.demo "One day, a little girl found a door in a tree."
.venv/bin/python -m ptg.demo "The detective solved the murder before the crime had even happened." --model lstm --decoding temp_0.8 --seed 3
```

Prints the RNN and LSTM continuations (or one model with `--model`). `--decoding` takes any config
name from `generation.configs` (default `topk_40`), and the same opening, config and seed reproduce
the saved generations. Words outside the vocabulary are listed. Nothing is written to `outputs/`.
The last cell of the notebook does the same with `plot_twist(...)`.

## Final assembly

```bash
./finalize.sh
```

Runs `human-analyze` (only if rating files exist), rebuilds figures and tables, compiles
`report/main.pdf`, re-executes the notebook, and writes the submission folder
`submission/Q4_Plot_Twist_Generator/` plus `submission/Q4_Plot_Twist_Generator.zip`
(`./make_submission.sh` does only the packaging step).

## Human evaluation procedure

1. `human-sheet` writes `outputs/human_eval/sheet.html` (what evaluators read), `sheet.csv`, and
   `ratings/TEMPLATE.csv`. The sample → system key is in `key_DO_NOT_SHARE.csv`; never send it.
2. Each evaluator rates every sample 1-5 for coherence, grammar, relevance and creativity, on
   their own, and returns the template saved as `ratings/<name>.csv`.
3. `human-analyze` validates the files and reports per-system means ± sd, Krippendorff's α
   (ordinal), the most-disputed samples, a paired Wilcoxon test (LSTM vs RNN), and Spearman
   correlations between automatic metrics and human scores.

## Reproducibility

- Seed 42 for data shuffling, initialisation and batching; generation seeds 0-4 (one sample each).
  Sampling uses a CPU `torch.Generator`, so generations do not depend on GPU kernels.
- The exact config, CLI arguments and hardware of every run are saved in `outputs/configs_used/`.
- cuDNN RNN kernels are not bit-for-bit deterministic, so retraining can change the last decimals
  of the loss. The submitted checkpoints reproduce the reported numbers exactly.
- The dataset is not included. `prepare` rebuilds the identical subset from the Hugging Face hub
  (first 40,000 rows of the train split, then the seeded shuffle); `data/splits.json` lists the row
  indices for verification.
