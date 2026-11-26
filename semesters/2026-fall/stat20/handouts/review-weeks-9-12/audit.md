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

## Revision 2026-11-25/26 (sweep: teach every procedure, revisit, meta commentary, proofs of facts used)
- Method boxes (new): bootstrap percentile interval (simulation and exact binomial), the four-step hypothesis test (converted from a list), exact permutation p-value for a difference in proportions, point-null tests for a proportion and for category counts, size and power of a test with a discrete statistic (with a six-toss worked example), least-squares line by hand, evaluating a model on held-out data, logistic prediction and classification, classifier metrics from a confusion matrix.
- Revisits added for the five question boxes that had none (hypothesis tests, Type I/II, least squares, overfitting, logistic regression).
- Proofs added: least-squares formulas (best constant is the mean, intercept, slope by completing the square, residuals sum to 0; previously only an idea box); 0 <= training R^2 <= 1, R^2 = r^2 for one feature, adding features never lowers training R^2; chi-squared = z^2 for two categories; p-hat >= 0.5 iff h >= 0; the hypergeometric formula for the permutation distribution; the miss probability of the sample maximum. New final section "Proofs of the facts used" proves W1-W5 (complements, binomial coefficient, binomial formula, linearity, Var identity, Var(aX), E(XY) and Var(X+Y) for independent variables, mean of n draws and its SE, SE of a proportion, unbiasedness of an SRS mean). The normal approximation (central limit theorem) is not proved; instead every normal-based p-value is accompanied by the exact binomial value (coin example: 0.0016 normal, 0.0017 exact), and W4 says so.
- Type I error statement made precise (size of the rejection region). The vague "constant test" and "sample SE formula" wordings fixed; inline computations moved to displays.
- Figures: gray labels (black!55/60/75/80) made black; the baseline line in the OLS figure is now bold dotted dark gray; negative residual labels moved off the stems (label-on-line finding); captions shortened.
- Pages: handout 14 -> 18. `check_handout.py`: 0 findings. `solutions.pdf` has no source and was not changed; exercises unchanged.
