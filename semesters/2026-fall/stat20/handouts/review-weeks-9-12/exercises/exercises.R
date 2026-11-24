# STAT 20 Weeks 9-12 Review exercises (Regression, Bootstrap, Classification)
library(tidyverse)
icecream <- read_csv("data/icecream.csv", show_col_types = FALSE)
new_icecream <- read_csv("data/new_icecream.csv", show_col_types = FALSE)
driving <- read_csv("data/driving.csv", show_col_types = FALSE)
new_driving <- read_csv("data/new_driving.csv", show_col_types = FALSE)
cars_train <- read_csv("data/cars_train.csv", show_col_types = FALSE)
cars_test <- read_csv("data/cars_test.csv", show_col_types = FALSE)
penguins_sample <- read_csv("data/penguins_sample.csv", show_col_types = FALSE)
resumes <- read_csv("data/resumes.csv", show_col_types = FALSE)

# --- c1a ---
# Assign summary to ice_summary and OLS model to m_ice
ice_summary <- icecream |>
  summarize(
    mean_temp = ___,
    mean_cones = ___,
    r = ___
  )
ice_summary

m_ice <- lm(___, data = icecream)
coef(m_ice)

# --- c1b ---
# Predict on new_icecream in new_eval and assign ice_test_rmse
new_eval <- new_icecream |>
  mutate(
    pred = predict(m_ice, newdata = new_icecream),
    resid = ___
  )
new_eval
ice_test_rmse <- ___
ice_test_rmse

# --- c2a ---
# Fit m_lin and m_quad on driving
m_lin <- lm(dist_ft ~ speed_mph + wet_road, data = driving)
m_quad <- lm(___, data = driving)
c(lin_r2 = summary(m_lin)$r.squared, quad_r2 = summary(m_quad)$r.squared)
coef(m_quad)

# --- c2b ---
# Assign named vector stop_rmse on new_driving
rmse <- function(y, yhat) sqrt(mean((y - yhat)^2))
stop_rmse <- c(
  lin_test_rmse = rmse(new_driving$dist_ft, ___),
  quad_test_rmse = rmse(new_driving$dist_ft, ___)
)
stop_rmse

# --- c3a ---
# Fit additive model m_car_add and interaction model m_car_int on cars_train
m_car_add <- lm(___, data = cars_train)
m_car_int <- lm(___, data = cars_train)
coef(m_car_int)
c(add_r2 = summary(m_car_add)$r.squared, int_r2 = summary(m_car_int)$r.squared)

# --- c3b ---
# Fit high-degree polynomial m_car_over and compare test RMSEs in car_rmse
m_car_over <- lm(price_k ~ poly(age_yr, 6, raw = TRUE) * hybrid + poly(mileage_k, 3, raw = TRUE), data = cars_train)
rmse <- function(y, yhat) sqrt(mean((y - yhat)^2))
car_rmse <- c(
  train_over = rmse(cars_train$price_k, predict(m_car_over)),
  add_test = rmse(cars_test$price_k, predict(m_car_add, newdata = cars_test)),
  int_test = rmse(cars_test$price_k, predict(m_car_int, newdata = cars_test)),
  over_test = ___
)
car_rmse

# --- c4a ---
# Assign group-wise summary to peng_summary
peng_summary <- penguins_sample |>
  group_by(species) |>
  summarize(
    count = n(),
    mean_bill = ___,
    sd_bill = ___
  )
peng_summary

# --- c4b ---
# 1000-rep bootstrap 95% CI in ci_adelie (WITH replacement, set.seed(20))
adelie <- penguins_sample |> filter(species == "Adelie") |> pull(bill_length_mm)
set.seed(20)
boot_means <- replicate(1000, ___)
ci_adelie <- quantile(boot_means, c(0.025, 0.975))
ci_adelie

# --- c5a ---
# Fit logistic regression m_log and compute odds_ratios
m_log <- glm(___, data = resumes, family = ___)
coef(m_log)
odds_ratios <- exp(___)
odds_ratios

# --- c5b ---
# Classify at threshold 0.5 and assign named vector cls_metrics
p_hat <- predict(m_log, type = "response")
y_hat <- as.integer(p_hat >= 0.5)
y <- resumes$callback
tp <- sum(y == 1 & y_hat == 1)
fp <- sum(y == 0 & y_hat == 1)
fn <- sum(y == 1 & y_hat == 0)
cls_metrics <- c(mcr = ___, precision = ___, recall = ___)
cls_metrics

# --- c6 ---
# Independent transfer: recruiting team wants recall >= 0.85 among cutoffs {0.3, 0.5, 0.7}
# while keeping precision as high as possible. Choose th_c6 and compute c6_metrics.
th_c6 <- ___
p_hat <- predict(m_log, type = "response")
y_hat <- as.integer(p_hat >= th_c6)
y <- resumes$callback
tp <- sum(y == 1 & y_hat == 1)
fp <- sum(y == 0 & y_hat == 1)
fn <- sum(y == 1 & y_hat == 0)
c6_metrics <- c(mcr = ___, precision = ___, recall = ___)
c6_metrics

