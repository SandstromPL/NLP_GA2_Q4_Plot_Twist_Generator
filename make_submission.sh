#!/usr/bin/env bash
# Builds submission/Q4_Plot_Twist_Generator.zip: code, notebook, checkpoints, vocab, all outputs and
# the report. The TinyStories data itself (data/cache/) is deliberately left out.
set -euo pipefail
cd "$(dirname "$0")"
name=Q4_Plot_Twist_Generator
mkdir -p submission
rm -f "submission/$name.zip"
zip -qr "submission/$name.zip" \
  README.md IMPLEMENTATION.md requirements.txt make_submission.sh configs src notebooks data/splits.json \
  outputs report \
  -x '*__pycache__*' '*.ipynb_checkpoints*' 'report/*.aux' 'report/*.log' 'report/*.out' \
     'report/*.toc' 'report/*.fls' 'report/*.fdb_latexmk' 'report/*.synctex.gz'
ls -lh "submission/$name.zip"
