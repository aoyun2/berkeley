# Packet Audit: STAT 20 Week 13 — Causation, Experiments & DID (`2026-11-16-causation-experiments`)

- **Scope:** `handout.tex`, `exercises.html`, `exercises/{README.md,PROMPTS.md,exercises.R,tests.R,data/*.csv}`, `solutions/solutions.R`, `exercises.zip`.
- **Datasets:** All four datasets (`salaries.csv`, `notes_study.csv`, `gym_warmup.csv`, `outreach_sim.csv`) are course-created simulated teaching datasets.
- **Objectives:** Stratify confounded tables (`w1a`/`w1b`), separate conditional association from causal claims (`Q1.2`), distinguish design-based randomization from realized balance (`Q2.1`), compute Monte Carlo & add-one vs exact permutation p-values (`w2a`/`w2b`), compute 2x2 DID (`w3a`/`w3b`), and transfer independently to `outreach_sim` (`w4`).
- **Acceptance Record (2026-11-23):**
  - Runtime: Node `webr 0.6.1` (R `4.6.0`, scratch Windows worker URL shim outside repo).
  - Starter checks: 7/7 fail cleanly. Reference solutions: 7/7 pass behavioral checks (`CHECKS`).
  - Misconceptions: `obs_ate <- 0` (in `w2a`/`w2b`) and naive post-only (`-7.86`) or pre/post (`-2.85`) estimates (in `w4`) rejected.
  - Parity & JS: Exact block/data parity between `exercises.html` and `exercises.zip` verified; inline `<script type="module">` syntax checked via `node --check`.
  - Limits: Live browser DOM/CDN/localStorage interaction and native local `Rscript` with `tidyverse` `not tested`.

## Revision 2026-11-25 (sweep: teach every procedure, revisit, meta commentary, proofs of facts used)
- Method boxes (new): decide whether an event or variable is a cause (with the backup-route edge case); compute tau and tau-hat; evaluate or redesign a study; check unbiasedness by listing every assignment; decide whether a variable is a covariate; compute an SMD (binary conventions, zero-variance and equal-means edge cases); exact permutation p-value by listing (ties, cap at 1, both-tails vs doubling); Monte Carlo p-value with the add-one estimate and its 1/R resolution; probability that k special units land in the same group; stratified comparison; difference in differences.
- New subsection 2.3 "Adjusting for confounding without randomization": Simpson's reversal with simulated numbers and the weighted-average explanation, stratification (and what the `group` coefficient of `lm(y ~ group + dept)` means), difference in differences with a proved parallel-trends theorem, and a proof that the `treated:post` coefficient of `lm(y ~ treated * post)` equals the DID (cell means minimize squared error). These are what exercises w1, w3 and w4 require and were previously not taught; the sharp null now justifies the permutation test (w2).
- Proofs: new final section "Proofs of the facts used" (binomial count, linearity of expectation, indicator expectation), linked from W4; the m/n step of the unbiasedness proof is now computed; the covariate-balance claim is derived from the theorem with Y_t = Y_c = x. W5 links to the review of Weeks 9-12. Earlier STAT 20 weekly handouts do not exist, so W1-W3 are stated as definitions with an example.
- Inline computations moved to displays; provenance flourish ("Thucydides and Hume") removed; every W reference linked. Figure: hollow dots darkened from black!65, the "0" label moved off the zero line, caption shortened.
- Pages: handout 7 -> 13. `check_handout.py`: 0 findings. `solutions.pdf` has no source and was not changed; exercises unchanged.
