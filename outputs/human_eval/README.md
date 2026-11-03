# Blinded rating study

- `sheet.html` / `sheet.csv`: the 25 blinded samples (opening + continuation, anonymous IDs S01-S25).
- `key_DO_NOT_SHARE.csv`: sample ID → system, decoding config, seed, prompt. Never shown to raters.
- `ratings/TEMPLATE.csv`: the empty rating form (1-5 for coherence, grammar, relevance, creativity).
- `ratings/llm_judge_*.csv`: the ratings used in the report.
- `results_*.csv`: output of `python -m ptg.cli human-analyze`.

**The ratings are not from human evaluators.** A human study was not feasible before the deadline, so
three LLM judges (Claude Haiku 5.5, Claude Sonnet 5.5, Claude Opus 5.5) were used as a proxy. Each
judge ran as a separate agent, was given only `sheet.csv` and the same instructions written for
human raters, was told not to open any other project file, and wrote one CSV. The rating files are
kept exactly as the judges wrote them. To run the study with people, send `sheet.html` and
`ratings/TEMPLATE.csv` to each evaluator, save their files as `ratings/<name>.csv`, move the
`llm_judge_*.csv` files out, and re-run `human-analyze`.
