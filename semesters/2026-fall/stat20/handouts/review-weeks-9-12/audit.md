# Packet Audit: STAT 20 Weeks 9--12 Review (`review-weeks-9-12`)

- **Scope:** `handout.tex`, `exercises.html`, `exercises/{README.md,PROMPTS.md,exercises.R,tests.R,data/*.csv}`, `solutions/solutions.R`, `exercises.zip`.
- **Datasets:** All eight datasets (`icecream`, `new_icecream`, `driving`, `new_driving`, `cars_train`, `cars_test`, `penguins_sample`, `resumes`) are simulated teaching tables.
- **Objectives:** Evaluate out-of-sample OLS RMSE (`c1a`--`c2b`), accurately interpret training vs held-out error (`train_over = 0.415`, `int_test = 0.913`, `over_test = 0.953`) in `c3a`/`c3b`/`Q3.2`, construct replacement percentile bootstrap CIs (`c4a`/`c4b`), fit/evaluate logistic models (`c5a`/`c5b`), and choose a recall-constrained cutoff (`c6`).
- **Acceptance Record (2026-11-23):**
  - Runtime: Node `webr 0.6.1` (R `4.6.0`).
  - Starter checks: 11/11 fail cleanly (including newly restored blanks in `c3a`, `c5a`, and transfer `c6`). Reference solutions: 11/11 pass behavioral checks (`CHECKS`).
  - Misconceptions: `replace = FALSE` degenerate bootstrap in `c4b` and `th_c6 <- 0.5` failing `recall >= 0.85` in `c6` rejected.
  - Parity & JS: Exact ZIP-to-HTML starter/solution/CSV parity verified; JS syntax checked via `node --check`.
  - Limits: Live browser DOM/CDN/localStorage interaction and native local `Rscript` with `tidyverse` `not tested`.
