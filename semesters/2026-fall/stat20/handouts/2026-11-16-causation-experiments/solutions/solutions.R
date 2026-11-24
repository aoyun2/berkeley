# STAT 20 Week 13 solutions (Causation, Experiments, DID)
library(tidyverse)
salaries <- read_csv("data/salaries.csv", show_col_types = FALSE)
notes_study <- read_csv("data/notes_study.csv", show_col_types = FALSE)
gym_warmup <- read_csv("data/gym_warmup.csv", show_col_types = FALSE)
outreach_sim <- read_csv("data/outreach_sim.csv", show_col_types = FALSE)

# --- w1a ---
sal_by_group <- salaries |> group_by(group) |> summarize(n = n(), mean_sal = mean(salary_k))
sal_by_group

sal_by_dept <- salaries |>
  group_by(dept, group) |>
  summarize(n = n(), mean_sal = mean(salary_k))
sal_by_dept

# --- w1b ---
m_sal_raw <- lm(salary_k ~ group, data = salaries)
m_sal_adj <- lm(salary_k ~ group + dept, data = salaries)
coef(m_sal_raw)
coef(m_sal_adj)

# --- w2a ---
notes_bal <- notes_study |>
  group_by(method) |>
  summarize(n = n(), mean_gpa = mean(prior_gpa), mean_score = mean(quiz_score))
notes_bal

obs_ate <- with(notes_study, mean(quiz_score[method == "Longhand"]) - mean(quiz_score[method == "Laptop"]))
obs_ate

# --- w2b ---
set.seed(20)
perm_ates <- replicate(1000, {
  shuffled <- sample(notes_study$method)
  mean(notes_study$quiz_score[shuffled == "Longhand"]) - mean(notes_study$quiz_score[shuffled == "Laptop"])
})
exceed <- sum(abs(perm_ates) >= abs(obs_ate))
p_mc <- exceed / 1000
p_add1 <- (exceed + 1) / (1000 + 1)
c(exceed = exceed, p_mc = p_mc, p_add1 = p_add1)

# --- w3a ---
cells <- gym_warmup |>
  group_by(treated, post) |>
  summarize(n = n(), mean_visits = mean(visits_wk))
cells
did_est <- (cells$mean_visits[4] - cells$mean_visits[3]) - (cells$mean_visits[2] - cells$mean_visits[1])
did_est

# --- w3b ---
m_did <- lm(visits_wk ~ treated * post, data = gym_warmup)
coef(m_did)
coef(m_did)["treated:post"]

# --- w4 ---
outreach_cells <- outreach_sim |>
  group_by(treated, post) |>
  summarize(n = n(), mean_chk = mean(checkups))
outreach_est <- (outreach_cells$mean_chk[4] - outreach_cells$mean_chk[3]) -
  (outreach_cells$mean_chk[2] - outreach_cells$mean_chk[1])
outreach_est

