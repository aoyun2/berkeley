# Packet Audit: CS 61A Week 4 — Recursion & Tree Recursion (`2026-09-14-recursion`)

- **Scope:** Week 4 (Lectures 9--10); `solutions.tex` P2 (`sum_b`) fix + Python coding package (`week04.py`).
- **Objectives:** Digit recursion (`digit_product`, replacing `sum_digits`), check adjacent digits recursively without loops (`has_adjacent_equal_digits`), parameterize staircase tree recursion (`count_stairs`), and compute `(final digit, steps)` recursively (`persistence`, replacing `digital_root_steps`).
- **Provenance & Publication:** Original tasks and `sum_b` analysis verified against Python (`sum_b(7) == 7`, `sum_b(12) is None`, `sum_b(123)` raises `TypeError`). `publish_solutions: false`; left unlinked on `index.html`.
- **Acceptance Record (2026-11-23):**
  - Fresh-ZIP extraction: starter `python tests.py` fails 4/4 (`rc=1`); reference passes 4/4.
  - PDF build: `solutions.pdf` compiled cleanly (`pdflatex` x2, 2 pages).
  - Browser checks: `not applicable`.

## Revision 2026-11-25 (sweep: teach every procedure, revisit, meta commentary, proofs of facts used)
- Question boxes added to "which frames an expression sees", iteration and recursion, order of events, helpers and mutual recursion; every question box has `\revisit` with a concrete answer (there was one, no revisits).
- Method boxes: tell which frames an expression sees (new), check a recursive function with the leap of faith, write a recursive function, convert a while loop into recursion (new), trace the output of a recursive function (new), count with tree recursion (new).
- Proofs added: induction proof that `fact(n)` returns n! (new example box); exponential lower bound C(n) >= 2^floor(n/2) on the number of calls of tree-recursive `fib` (previously asserted). Facts W1-W6 link to the week that shows them; W6 (smallest factor is prime) added because `unique_prime_factors` uses it.
- Examples one per box: streak, fact_k/fact_tail (with `fact_tail(0)`), cascade (with `cascade(5)`), smallest_factor (with the `n = 1` RecursionError domain edge), unique_prime_factors (with a prime input), parking, partitions, Fibonacci. New trap: base case `n == 0` against `n < 10` for digit recursion.
- Figures: pale gray dotted "Caller" box and black!65 labels made black and solid; dotted blue return rails made solid blue with haloed blue labels; negative-leaf boxes in the call tree made solid with black text; captions shortened.
- Meta removed from the problem-set lead-in.
- **Policy fix (5b):** exercise `sum_digits` was CS 61A Lab 1 Q9 "Sum Digits" (and `digital_root_steps` required writing it). Replaced by original `digit_product` and `persistence` (multiplicative persistence). Starter 4/4 fail, reference 4/4 pass, fresh-ZIP extraction checked; a base case `n == 0 -> 1` fails the `digit_product(0)` contract.
- Pages: handout 7 -> 10, solutions 2 -> 2. `check_handout.py`: 0 findings.
