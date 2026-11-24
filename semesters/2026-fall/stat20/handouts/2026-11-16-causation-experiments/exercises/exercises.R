# STAT 20 Week 13 exercises (Causation, Experiments, DID)
library(tidyverse)
salaries <- read_csv("data/salaries.csv", show_col_types = FALSE)
notes_study <- read_csv("data/notes_study.csv", show_col_types = FALSE)
gym_warmup <- read_csv("data/gym_warmup.csv", show_col_types = FALSE)
outreach_sim <- read_csv("data/outreach_sim.csv", show_col_types = FALSE)

# --- w1a ---
# Save pooled summary as sal_by_group and stratified summary as sal_by_dept
sal_by_group <- salaries |> group_by(group) |> summarize(n = n(), mean_sal = mean(salary_k))
sal_by_group

sal_by_dept <- salaries |>
  group_by(___, ___) |>
  summarize(n = n(), mean_sal = ___)
sal_by_dept

# --- w1b ---
# Fit unadjusted m_sal_raw and department-adjusted m_sal_adj
m_sal_raw <- lm(salary_k ~ group, data = salaries)
m_sal_adj <- lm(___, data = salaries)
coef(m_sal_raw)
coef(m_sal_adj)

# --- w2a ---
# Balance diagnostic on prior_gpa and observed ATE on quiz_score
notes_bal <- notes_study |>
  group_by(method) |>
  summarize(n = n(), mean_gpa = ___, mean_score = ___)
notes_bal

obs_ate <- with(notes_study, mean(quiz_score[method == "Longhand"]) - mean(quiz_score[method == "Laptop"]))
obs_ate

# --- w2b ---
# 1000-rep permutation test under sharp null (set.seed(20))
# Compute exceed count, Monte Carlo proportion p_mc, and add-one p_add1
set.seed(20)
perm_ates <- replicate(1000, {
  shuffled <- sample(notes_study$method)
  mean(notes_study$quiz_score[shuffled == "Longhand"]) - ___
})
exceed <- sum(abs(perm_ates) >= abs(obs_ate))
p_mc <- exceed / 1000
p_add1 <- (exceed + 1) / (1000 + 1)
c(exceed = exceed, p_mc = p_mc, p_add1 = p_add1)

# --- w3a ---
# 2x2 cell means table and hand calculation of did_est
cells <- gym_warmup |>
  group_by(treated, post) |>
  summarize(n = n(), mean_visits = mean(visits_wk))
cells

# Compute (T,Post - T,Pre) - (C,Post - C,Pre) from cells
did_est <- ___
did_est

# --- w3b ---
# Fit interaction model m_did on gym_warmup
m_did <- lm(___, data = gym_warmup)
coef(m_did)
coef(m_did)["treated:post"]

# --- w4 ---
# Independent transfer (outreach_sim: 40 simulated clinic records)
# Estimate the outreach program effect outreach_est accounting for clinic differences and time trend.
outreach_est <- ___
outreach_est

