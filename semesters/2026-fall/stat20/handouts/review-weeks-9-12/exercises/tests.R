# Offline behavioral checks for STAT 20 exercises.
# Run locally with Rscript (with tidyverse installed) after sourcing exercises or solutions.
suppressPackageStartupMessages(library(tidyverse))
icecream <- read_csv("data/icecream.csv", show_col_types = FALSE)
new_icecream <- read_csv("data/new_icecream.csv", show_col_types = FALSE)
driving <- read_csv("data/driving.csv", show_col_types = FALSE)
new_driving <- read_csv("data/new_driving.csv", show_col_types = FALSE)
cars_train <- read_csv("data/cars_train.csv", show_col_types = FALSE)
cars_test <- read_csv("data/cars_test.csv", show_col_types = FALSE)
penguins_sample <- read_csv("data/penguins_sample.csv", show_col_types = FALSE)
resumes <- read_csv("data/resumes.csv", show_col_types = FALSE)

assert_true <- function(cond, msg) {
  if (!isTRUE(cond)) stop(msg, call. = FALSE)
}

target_file <- commandArgs(trailingOnly = TRUE)
src <- if (length(target_file) >= 1) target_file[1] else 'exercises.R'
blocks <- list()
cur <- NULL
for (ln in readLines(src, warn = FALSE)) {
  m <- regmatches(ln, regexec('^# --- ([a-z0-9_]+) ---$', ln))[[1]]
  if (length(m) == 2) { cur <- m[2]; blocks[[cur]] <- character(0) }
  else if (!is.null(cur)) { blocks[[cur]] <- c(blocks[[cur]], ln) }
}

checks <- list(
  c1a = function(env) {
    assert_true(exists('ice_summary', envir = env) && exists('m_ice', envir = env), 'Assign ice_summary and m_ice')
    isum <- get('ice_summary', envir = env)
    assert_true(all(c('mean_temp','mean_cones','r') %in% names(isum)) && abs(isum$r[1] - 0.99864) < 0.002, 'ice_summary correlation wrong')
    mi <- get('m_ice', envir = env)
    assert_true(abs(unname(coef(mi)['temp_f']) - 5.07648) < 0.05, 'm_ice slope wrong')
  },
  c1b = function(env) {
    assert_true(exists('new_eval', envir = env) && exists('ice_test_rmse', envir = env), 'Assign new_eval and ice_test_rmse')
    rmse_val <- get('ice_test_rmse', envir = env)
    assert_true(is.numeric(rmse_val) && abs(rmse_val - 1.87777) < 0.02, 'ice_test_rmse should be ~1.878')
  },
  c2a = function(env) {
    assert_true(exists('m_lin', envir = env) && exists('m_quad', envir = env), 'Assign m_lin and m_quad')
    mq <- get('m_quad', envir = env)
    assert_true(summary(mq)$r.squared > 0.999 && length(coef(mq)) == 4, 'm_quad must include quadratic speed term and wet_road')
  },
  c2b = function(env) {
    assert_true(exists('stop_rmse', envir = env), 'Assign stop_rmse')
    sr <- get('stop_rmse', envir = env)
    assert_true(abs(sr['lin_test_rmse'] - 8.031609) < 0.05 && abs(sr['quad_test_rmse'] - 0.994606) < 0.05, 'stop_rmse mismatch')
  },
  c3a = function(env) {
    assert_true(exists('m_car_add', envir = env) && exists('m_car_int', envir = env), 'Assign m_car_add and m_car_int')
    ma <- get('m_car_add', envir = env); mi <- get('m_car_int', envir = env)
    assert_true(abs(summary(ma)$r.squared - 0.9750) < 0.002 && 'age_yr:hybrid' %in% names(coef(mi)), 'Check additive/interaction formulas')
  },
  c3b = function(env) {
    assert_true(exists('car_rmse', envir = env), 'Assign car_rmse')
    cr <- get('car_rmse', envir = env)
    assert_true(abs(cr['train_over'] - 0.41459) < 0.02 && abs(cr['over_test'] - 0.95313) < 0.02 && abs(cr['int_test'] - 0.91269) < 0.02, 'car_rmse values mismatch')
  },
  c4a = function(env) {
    assert_true(exists('peng_summary', envir = env), 'Assign peng_summary')
    ps <- get('peng_summary', envir = env)
    assert_true(nrow(ps) == 3 && all(c('mean_bill','sd_bill') %in% names(ps)), 'peng_summary missing columns')
    assert_true(abs(ps$mean_bill[ps$species == 'Adelie'] - 38.51667) < 0.02, 'Adelie mean_bill mismatch')
  },
  c4b = function(env) {
    assert_true(exists('boot_means', envir = env) && exists('ci_adelie', envir = env), 'Assign boot_means and ci_adelie')
    bm <- get('boot_means', envir = env); ci <- unname(get('ci_adelie', envir = env))
    assert_true(length(bm) == 1000, 'Need 1000 bootstrap replicates')
    assert_true(sd(bm) > 0.25 && (ci[2] - ci[1]) > 0.5, 'Bootstrap variance is ~0 -- make sure replace = TRUE!')
    assert_true(abs(ci[1] - 37.05792) < 0.05 && abs(ci[2] - 39.81708) < 0.05, 'With set.seed(20), CI should match ~[37.058, 39.817]')
  },
  c5a = function(env) {
    assert_true(exists('m_log', envir = env) && exists('odds_ratios', envir = env), 'Assign m_log and odds_ratios')
    ml <- get('m_log', envir = env); or <- get('odds_ratios', envir = env)
    assert_true(ml$family$family == 'binomial' && abs(unname(or['honors']) - 6.558) < 0.05, 'm_log/odds_ratios mismatch')
  },
  c5b = function(env) {
    assert_true(exists('cls_metrics', envir = env), 'Assign cls_metrics')
    cm <- get('cls_metrics', envir = env)
    assert_true(abs(cm['mcr'] - 0.275) < 1e-4 && abs(cm['precision'] - 0.7272727) < 1e-4 && abs(cm['recall'] - 0.7619048) < 1e-4, 'cls_metrics values wrong')
  },
  c6 = function(env) {
    assert_true(exists('th_c6', envir = env) && exists('c6_metrics', envir = env), 'Assign th_c6 and c6_metrics')
    th <- get('th_c6', envir = env); cm <- get('c6_metrics', envir = env)
    assert_true(th %in% c(0.3, 0.5, 0.7), 'Choose th_c6 from {0.3, 0.5, 0.7}')
    assert_true(abs(th - 0.3) < 1e-9 && abs(cm['recall'] - 0.9047619) < 1e-4 && abs(cm['precision'] - 0.6551724) < 1e-4, 'Only th_c6=0.3 achieves recall >= 0.85 (~0.905) with precision ~0.655')
  }
)

env <- new.env(parent = globalenv())
failed <- 0L
for (k in names(checks)) {
  ok <- tryCatch({
    exprs <- parse(text = paste(blocks[[k]], collapse = '\n'))
    for (ex in exprs) eval(ex, envir = env)
    checks[[k]](env)
    TRUE
  }, error = function(e) {
    cat(sprintf('%s: FAIL (%s)\n', k, conditionMessage(e)))
    FALSE
  })
  if (ok) cat(sprintf('%s: ok\n', k)) else failed <- failed + 1L
}
if (failed > 0L) { cat(sprintf('%d failed\n', failed)); quit(status = 1L) }
cat('all passed\n')
