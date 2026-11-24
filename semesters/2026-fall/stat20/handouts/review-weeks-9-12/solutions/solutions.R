# STAT 20 Weeks 9-12 Review solutions (Regression, Bootstrap, Classification)
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
ice_summary <- icecream |>
  summarize(
    mean_temp = mean(temp_f),
    mean_cones = mean(cones),
    r = cor(temp_f, cones)
  )
ice_summary

m_ice <- lm(cones ~ temp_f, data = icecream)
coef(m_ice)

# --- c1b ---
new_eval <- new_icecream |>
  mutate(
    pred = predict(m_ice, newdata = new_icecream),
    resid = cones - pred
  )
new_eval
ice_test_rmse <- sqrt(mean(new_eval$resid^2))
ice_test_rmse

# --- c2a ---
m_lin <- lm(dist_ft ~ speed_mph + wet_road, data = driving)
m_quad <- lm(dist_ft ~ speed_mph + I(speed_mph^2) + wet_road, data = driving)
c(lin_r2 = summary(m_lin)$r.squared, quad_r2 = summary(m_quad)$r.squared)
coef(m_quad)

# --- c2b ---
rmse <- function(y, yhat) sqrt(mean((y - yhat)^2))
stop_rmse <- c(
  lin_test_rmse = rmse(new_driving$dist_ft, predict(m_lin, newdata = new_driving)),
  quad_test_rmse = rmse(new_driving$dist_ft, predict(m_quad, newdata = new_driving))
)
stop_rmse

# --- c3a ---
m_car_add <- lm(price_k ~ age_yr + mileage_k + hybrid, data = cars_train)
m_car_int <- lm(price_k ~ age_yr * hybrid + mileage_k, data = cars_train)
coef(m_car_int)
c(add_r2 = summary(m_car_add)$r.squared, int_r2 = summary(m_car_int)$r.squared)

# --- c3b ---
m_car_over <- lm(price_k ~ poly(age_yr, 6, raw = TRUE) * hybrid + poly(mileage_k, 3, raw = TRUE), data = cars_train)
rmse <- function(y, yhat) sqrt(mean((y - yhat)^2))
car_rmse <- c(
  train_over = rmse(cars_train$price_k, predict(m_car_over)),
  add_test = rmse(cars_test$price_k, predict(m_car_add, newdata = cars_test)),
  int_test = rmse(cars_test$price_k, predict(m_car_int, newdata = cars_test)),
  over_test = rmse(cars_test$price_k, predict(m_car_over, newdata = cars_test))
)
car_rmse

# --- c4a ---
peng_summary <- penguins_sample |>
  group_by(species) |>
  summarize(
    count = n(),
    mean_bill = mean(bill_length_mm),
    sd_bill = sd(bill_length_mm)
  )
peng_summary

# --- c4b ---
adelie <- penguins_sample |> filter(species == "Adelie") |> pull(bill_length_mm)
set.seed(20)
boot_means <- replicate(1000, mean(sample(adelie, length(adelie), replace = TRUE)))
ci_adelie <- quantile(boot_means, c(0.025, 0.975))
ci_adelie

# --- c5a ---
m_log <- glm(callback ~ exp_years + honors, data = resumes, family = binomial)
coef(m_log)
odds_ratios <- exp(coef(m_log))
odds_ratios

# --- c5b ---
p_hat <- predict(m_log, type = "response")
y_hat <- as.integer(p_hat >= 0.5)
y <- resumes$callback
tp <- sum(y == 1 & y_hat == 1)
fp <- sum(y == 0 & y_hat == 1)
fn <- sum(y == 1 & y_hat == 0)
cls_metrics <- c(mcr = mean(y != y_hat), precision = tp / (tp + fp), recall = tp / (tp + fn))
cls_metrics

# --- c6 ---
th_c6 <- 0.3
p_hat <- predict(m_log, type = "response")
y_hat <- as.integer(p_hat >= th_c6)
y <- resumes$callback
tp <- sum(y == 1 & y_hat == 1)
fp <- sum(y == 0 & y_hat == 1)
fn <- sum(y == 1 & y_hat == 0)
c6_metrics <- c(mcr = mean(y != y_hat), precision = tp / (tp + fp), recall = tp / (tp + fn))
c6_metrics

