# Packet Audit: CS 61A Week 2 — Control & Higher-Order Functions (`2026-08-31-control-higher-order`)

- **Scope:** Week 2 (Lectures 3--5); original instructional handout, solutions, and Python coding package (`week02.py`).
- **Objectives:** Safe conditional division (`safe_ratio`), `while`-loop digit counting including `n = 0` (`count_matches`), two-argument closures (`make_bounded_scaler`), and threshold search transfer (`first_threshold`).
- **Provenance & Publication:** Original coding tasks + cited past-exam problems in handout (`publish_solutions: false`; left unlinked on `index.html`).
- **Acceptance Record (2026-11-23):**
  - Fresh-ZIP extraction: starter `python tests.py` fails 4/4 (`rc=1`); reference `python tests.py ../solutions` passes 4/4.
  - PDF build: `solutions.pdf` compiled cleanly (`pdflatex` x2, 2 pages).
  - Browser checks: `not applicable`.

## Revision 2026-11-25 (sweep: teach every procedure, revisit, meta commentary)
- Question boxes added to the sections that lacked one (print versus return, conditionals, while, designing functions); every question box now has `\revisit` with a concrete answer (there were none).
- Method boxes: execute a conditional, evaluate `and`, evaluate `or`, execute `while`, write a loop that computes a result (new: names and meanings, starting values, condition and `<` against `<=`, zero-pass and one-pass checks), test with doctests (new), write similar functions once as a higher-order function (new), write a function that returns a function (new), draw an environment diagram with higher-order functions.
- Examples one per box: print-then-return, Fall 2022 MT1 Q1(c), prime factorisation, digit loop with `num_digits` and the `n = 0` edge case (new), `classify` with off-by-one and `n = 1` checks, default argument with doctests (new), `summation`, `make_adder`, `compose1` (now its own box, with order-of-composition values), make_adder variations.
- Added: operator precedence for `not`/`and`/`or`, `while n:`, augmented assignment (used by E2), zero-pass loops; traps for `while n > 0` with `n = 0` and `return adder(k)`.
- Meta removed from the problem-set lead-in. Figure: light-gray "lookup n" label and pale dotted guide replaced by a solid red arrow with a red haloed label; "Return value" labels now black; caption shortened.
- Pages: handout 9 -> 13, solutions 2 -> 2. Exercises unchanged. `check_handout.py`: 0 findings.
