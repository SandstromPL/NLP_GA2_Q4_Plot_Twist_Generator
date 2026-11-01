#!/usr/bin/env bash
# Final assembly after the experiments: human-eval analysis (if ratings exist), report assets,
# report PDF, executed notebook, and the submission folder + zip.
set -euo pipefail
cd "$(dirname "$0")"
export PYTHONPATH=src
PY=.venv/bin/python

if find outputs/human_eval/ratings -name '*.csv' ! -name TEMPLATE.csv | grep -q .; then
  $PY -m ptg.cli human-analyze
else
  echo "No rating files in outputs/human_eval/ratings/ yet: skipping human-analyze"
fi
$PY -m ptg.cli report-assets

(cd report && for _ in 1 2; do pdflatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null; done)
echo "report/main.pdf: $(pdfinfo report/main.pdf | awk '/Pages/ {print $2}') pages"

$PY notebooks/make_notebook.py
.venv/bin/jupyter nbconvert --to notebook --execute --inplace notebooks/Q4_Plot_Twist_Generator.ipynb 2>/dev/null

./make_submission.sh
