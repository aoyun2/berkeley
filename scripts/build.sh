#!/usr/bin/env bash
# Build a handout: scripts/build.sh path/to/file.tex
# Runs pdflatex twice with the repo's templates/ on the TeX search path.
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FILE="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
cd "$(dirname "$FILE")"
export TEXINPUTS="$ROOT/templates//:"
pdflatex -interaction=nonstopmode "$(basename "$FILE")" >/dev/null || true
pdflatex -interaction=nonstopmode "$(basename "$FILE")" >/dev/null || true
LOG="${FILE%.tex}.log"
if grep -q '^!' "$LOG"; then grep -A4 '^!' "$LOG"; exit 1; fi
grep -c 'Overfull' "$LOG" | xargs -I{} echo "overfull boxes: {}"
echo "built ${FILE%.tex}.pdf"
