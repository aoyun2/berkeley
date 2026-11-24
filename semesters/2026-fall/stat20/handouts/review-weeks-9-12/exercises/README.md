# Weeks 9-12 Review Exercises (STAT 20)

All 8 CSV files in `data/` are simulated teaching datasets synchronized with `exercises.html`.

## Browser vs. Local Runtime
- `exercises.html` uses WebR with a custom subset of tidy verbs (`filter`, `mutate`, `group_by`, `summarize`, `arrange`, `select`, `count`, `pull`, `|>`, `%>%`).
- Local execution uses `library(tidyverse)`:

    Rscript tests.R exercises.R
    Rscript tests.R ../solutions/solutions.R

See `PROMPTS.md` for all conceptual questions, expected summary values, and self-review criteria.
