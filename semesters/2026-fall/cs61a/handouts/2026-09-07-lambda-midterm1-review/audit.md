# Packet Audit: CS 61A Week 3 — Lambda, Currying & Midterm 1 Review (`2026-09-07-lambda-midterm1-review`)

- **Scope:** Week 3 (Lectures 6--8); 35-minute timed Midterm 1 practice package (`exercises/README.md`, `week03.py`).
- **Objectives:** Currying (`curry_binary`), $n$-fold composition with `n = 0` identity (`compose_n`), parity-dispatch closures (`make_alternator`), and range optimization across negative values (`max_over_range`).
- **Provenance & Publication:** Original timed coding exercises; exam problems in `handout.tex` (`publish_solutions: false`; left unlinked on `index.html`).
- **Acceptance Record (2026-11-23):**
  - Fresh-ZIP extraction: starter `python tests.py` fails 4/4 (`rc=1`); reference passes 4/4.
  - Misconception check: replacing `best = fn(lo)` with `best = 0` in `max_over_range` is rejected (`max_over_range: FAIL`) on all-negative ranges.
  - PDF build: `solutions.pdf` compiled cleanly (`pdflatex` x2, 2 pages).
  - Browser checks: `not applicable`.
