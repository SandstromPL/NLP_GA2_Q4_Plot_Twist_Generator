#!/usr/bin/env bash
# Builds the final submission: the folder submission/Q4_Plot_Twist_Generator/ and the single
# compressed file submission/Q4_Plot_Twist_Generator.zip (code, notebook, checkpoints, vocab, all
# outputs and the report). The TinyStories data itself (data/cache/) is deliberately left out.
set -euo pipefail
cd "$(dirname "$0")"
name=Q4_Plot_Twist_Generator
dest="submission/$name"
rm -rf "$dest" "submission/$name.zip"
mkdir -p "$dest/data"
rsync -a \
  --exclude '__pycache__' --exclude '.ipynb_checkpoints' \
  --exclude '*.aux' --exclude '*.log' --exclude '*.out' --exclude '*.toc' --exclude '*.fls' \
  --exclude '*.fdb_latexmk' --exclude '*.synctex.gz' \
  README.md IMPLEMENTATION.md requirements.txt make_submission.sh finalize.sh configs src notebooks outputs report \
  "$dest/"
cp data/splits.json "$dest/data/"
(cd submission && zip -qr "$name.zip" "$name")
du -sh "$dest" "submission/$name.zip"
