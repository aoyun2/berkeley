# Packet Audit: CS 61A Week 3 — Lambda, Currying & Midterm 1 Review (`2026-09-07-lambda-midterm1-review`)

- **Scope:** Week 3 (Lectures 6--8); 35-minute timed Midterm 1 practice package (`exercises/README.md`, `week03.py`).
- **Objectives:** Currying (`curry_binary`), $n$-fold composition with `n = 0` identity (`compose_n`), parity-dispatch closures (`make_alternator`), and range optimization across negative values (`max_over_range`).
- **Provenance & Publication:** Original timed coding exercises; exam problems in `handout.tex` (`publish_solutions: false`; left unlinked on `index.html`).
- **Acceptance Record (2026-11-23):**
  - Fresh-ZIP extraction: starter `python tests.py` fails 4/4 (`rc=1`); reference passes 4/4.
  - Misconception check: replacing `best = fn(lo)` with `best = 0` in `max_over_range` is rejected (`max_over_range: FAIL`) on all-negative ranges.
  - PDF build: `solutions.pdf` compiled cleanly (`pdflatex` x2, 2 pages).
  - Browser checks: `not applicable`.

## Revision 2026-11-25 (sweep: teach every procedure, revisit, meta commentary, proofs of facts used)
- Question boxes added to currying, zero-argument functions, conditional expressions, environment diagram review and exam writing; every question box has `\revisit` with a concrete answer (there were none).
- Method boxes: rewrite between lambda and def (new), evaluate a chain of calls (new), fix one argument of a two-argument function (new), evaluate a conditional expression (new), draw lambda functions and rebound names in a diagram (new), the lectures' fill-in-the-blank procedure.
- Examples one per box: nested lambda (lecture), nested lambda rewritten with def (new), common_ratio (lecture), reverse (Lecture 8), die as a zero-argument function (new, with the `dice()` error case), if statement to conditional expression (new), Fall 2022 MT1 Q2, nearest_prime, all_digits (now with the `n = 0` edge case), prefix_digits (split from all_digits).
- Facts from Weeks 1-2 (W1-W5) now each link to the week that shows them, and each use of (W3), (W4) links to the item. Meta removed from the problem-set lead-in ("your exam", provenance). Metaphor "bridges the gap" removed.
- **Policy fix (5b):** exercise `compose_n(f, n)` was CS 61A HW2 Q3 "Make Repeater" and its reference solution answered it. Replaced by the original `repeat_until(f, stop)` (returned function, loop until a condition, zero applications when `stop(x)` holds). Starter 4/4 fail, reference 4/4 pass, fresh-ZIP extraction checked; wrong answers "apply f before the first check" and "loop while stop(x)" each fail with a named contract.
- Pages: handout 7 -> 10, solutions 2 -> 2. `check_handout.py`: 0 findings.
