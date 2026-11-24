# Course Profile: STAT 20 (Fall 2026)

- **Term:** Fall 2026
- **Course:** STAT 20 — Introduction to Probability and Statistics
- **Runtimes & Libraries:**
  - Local execution: R with `library(tidyverse)` (scripts in `exercises/` and `solutions/`).
  - Browser execution: `webr` (`webr.r-wasm.org`) preloading a documented custom subset of tidy-like verbs (`filter`, `mutate`, `group_by`, `summarize`/`summarise`, `arrange`, `select`, `count`, `pull`, `slice_head`, `slice_sample`, `|>`, `%>%`) plus base `lm`, `glm`, `predict`, `sample`, `replicate`, `quantile`. This subset is a teaching helper, not a full replacement for `dplyr` or `infer`.
- **Datasets:** All embedded tables and CSVs in `exercises/data/` are simulated teaching datasets created specifically for these packets.
- **Covered Packets:**
  - `2026-11-16-causation-experiments` (Simpson's paradox, randomization balance, permutation testing, difference-in-differences, independent transfer)
  - `review-weeks-9-12` (OLS, nonlinearity, interaction vs high-degree regression, percentile bootstrap, logistic regression, threshold selection transfer)

## Publication Settings
`publish_solutions: false`

- **Default rule:** Do not expose new unapproved solution bundles automatically.
- **Observed existing state:** `semesters/2026-fall/stat20/index.html` and the existing `exercises.html` / `exercises.zip` / `solutions.pdf` artifacts predate this profile and remain intact with their disclosures and added behavioral tests; self-review solutions inside `exercises.html` remain gated behind explicit `<details>` disclosures (`Show solution`).
