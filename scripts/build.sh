#!/usr/bin/env bash
# Build a handout: scripts/build.sh path/to/file.tex
# Runs pdflatex twice with the repo's templates/ on the TeX search path.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FILE="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
cd "$(dirname "$FILE")"
export TEXINPUTS=".:$ROOT/templates//:"
for pass in 1 2; do
  if ! pdflatex -halt-on-error -interaction=nonstopmode "$FILE" >/dev/null; then
    tail -60 "${FILE%.tex}.log"
    exit 1
  fi
done
LOG="${FILE%.tex}.log"
if grep -q '^!' "$LOG"; then grep -A4 '^!' "$LOG"; exit 1; fi
awk '/Overfull/ { count++ } END { print "overfull boxes: " count+0 }' "$LOG"
echo "built ${FILE%.tex}.pdf"
