# Packet Audit: CS 61A Week 1 — Expressions, Names & Functions (`2026-08-24-functions`)

- **Scope:** Week 1 (Lectures 1--2); *Composing Programs* Ch. 1.1--1.3 concepts (`handout.tex`, `solutions.tex`, `exercises/week01.py`, `solutions/week01.py`, `exercises.zip`).
- **Objectives:** Distinguish pure return values from printed output (`trace_step`); compose min/max expressions (`clamp_value`); implement domain-safe helpers (`ring_area_units`, `clamp_distance`).
- **Provenance & Publication:** All paper and coding tasks are original (`publish_solutions: false`; `cs61a/index.html` leaves Week 1 `not yet posted`).
- **Acceptance Record (2026-11-23):**
  - Fresh-ZIP extraction (`exercises.zip` -> Python 3): starter `python tests.py` fails 4/4 (`rc=1`); reference `python tests.py ../solutions` passes 4/4 (`ring_area_units`, `trace_step`, `middle_number` [since replaced, see below], `clamp_distance`).
  - PDF build: `solutions.pdf` compiled cleanly (`pdflatex` x2, 2 pages).
  - Browser checks: `not applicable` (no `exercises.html` in Week 1).

## Revision 2026-11-25 (sweep: teach every procedure, revisit, meta commentary)
- Method boxes added or converted: evaluate a call expression, execute an assignment, call a user-defined function, write a function from its description (new, with two original worked examples `distance_to_nearer`, `triangle_area`), draw an environment diagram, answer a What Would Python Display question (new; formerly a Shortcuts item).
- Examples split one per box: hand evaluation of the lecture expression (new), multiple vs separate assignment (new), evaluating `g(3)` (new), lecture trace, function called through a second name (new), parameter named like its function, nested print, `noisy`, `noisy` with print.
- Edge cases added: negative `//` and `%`, `n = 0` and one-digit `n`, float operands, division by zero, `UnboundLocalError` trap. New problem P9 (negative floor division) with solution.
- Every question box now has `\revisit` with a concrete answer (there were none). Meta commentary removed from the problem-set lead-in and the closing search example. Figure captions rewritten; diagram label "Return value" now black, emphasis-by-line-weight removed.
- **Policy fix (5b):** exercise `middle_number` duplicated CS 61A Lab 1 Q4 "Middle Number" and its reference solution was the lab answer. Replaced by the original `clamp_value(x, low, high)` (min/max composition). Tests: starter 4/4 fail, reference 4/4 pass, fresh-ZIP extraction checked; wrong answers `min(max(x, high), low)`, `max(x, low)`, `min(x, high)` each fail with a named contract.
- Pages: handout 8 -> 11, solutions 2 -> 2. `check_handout.py`: 0 findings.
