# Week 13 Exercises — Causation, Experiments & Difference-in-Differences (STAT 20)

All four datasets in `data/` (`salaries.csv`, `notes_study.csv`, `gym_warmup.csv`, `outreach_sim.csv`) are simulated teaching datasets created for this packet.

## Browser vs. Local Runtime
- `exercises.html` uses WebR with a custom documented subset of tidy verbs (`filter`, `mutate`, `group_by`, `summarize`, `arrange`, `select`, `count`, `pull`, `|>`, `%>%`), not full `dplyr` or `infer`.
- Local execution uses `library(tidyverse)`:

    Rscript tests.R exercises.R
    Rscript tests.R ../solutions/solutions.R

See `PROMPTS.md` for all conceptual questions, expected console outputs, and self-review criteria (kept synchronized with `exercises.html`).
