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
