# Offline behavioral checks for STAT 20 exercises.
# Run locally with Rscript (with tidyverse installed) after sourcing exercises or solutions.
suppressPackageStartupMessages(library(tidyverse))
salaries <- read_csv("data/salaries.csv", show_col_types = FALSE)
notes_study <- read_csv("data/notes_study.csv", show_col_types = FALSE)
gym_warmup <- read_csv("data/gym_warmup.csv", show_col_types = FALSE)
outreach_sim <- read_csv("data/outreach_sim.csv", show_col_types = FALSE)

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
  w1a = function(env) {
    assert_true(exists('sal_by_group', envir = env), 'Assign sal_by_group')
    assert_true(exists('sal_by_dept', envir = env), 'Assign sal_by_dept')
    sg <- get('sal_by_group', envir = env)
    sd_df <- get('sal_by_dept', envir = env)
    assert_true(nrow(sg) == 2 && 'mean_sal' %in% names(sg), 'sal_by_group must have 2 rows and mean_sal column')
    gb <- sg$mean_sal[sg$group == 'Group_B']
    assert_true(length(gb) == 1 && abs(gb - 106.66667) < 0.05, 'Group_B pooled mean mismatch')
    assert_true(nrow(sd_df) == 4 && all(c('dept','group','mean_sal') %in% names(sd_df)), 'sal_by_dept must stratify by dept and group (4 rows)')
    op_b <- sd_df$mean_sal[sd_df$dept == 'Operations' & sd_df$group == 'Group_B']
    assert_true(length(op_b) == 1 && abs(op_b - 93.78571) < 0.05, 'Operations Group_B mean mismatch')
  },
  w1b = function(env) {
    assert_true(exists('m_sal_raw', envir = env) && exists('m_sal_adj', envir = env), 'Fit m_sal_raw and m_sal_adj')
    r <- get('m_sal_raw', envir = env); a <- get('m_sal_adj', envir = env)
    assert_true(abs(unname(coef(r)['groupGroup_B']) - (-31.31061)) < 0.05, 'm_sal_raw Group_B slope wrong')
    assert_true(abs(unname(coef(a)['groupGroup_B']) - 4.298734) < 0.05, 'm_sal_adj Group_B slope wrong')
  },
  w2a = function(env) {
    assert_true(exists('notes_bal', envir = env) && exists('obs_ate', envir = env), 'Assign notes_bal and obs_ate')
    nb <- get('notes_bal', envir = env)
    assert_true(nrow(nb) == 2 && all(c('mean_gpa','mean_score') %in% names(nb)), 'notes_bal missing columns')
    assert_true(abs(nb$mean_gpa[nb$method == 'Longhand'] - 3.158) < 0.01, 'Longhand mean_gpa mismatch')
    oa <- get('obs_ate', envir = env)
    assert_true(is.numeric(oa) && length(oa) == 1 && abs(oa - 5.453333) < 0.02, 'obs_ate must equal Longhand - Laptop mean score (~5.453)')
  },
  w2b = function(env) {
    assert_true(exists('obs_ate', envir = env) && abs(get('obs_ate', envir = env) - 5.453333) < 0.02, 'Run or fix w2a so obs_ate ~ 5.453 first')
    assert_true(exists('perm_ates', envir = env) && exists('p_add1', envir = env), 'Assign perm_ates, exceed, p_mc, p_add1')
    pa <- get('perm_ates', envir = env)
    assert_true(length(pa) == 1000 && sd(pa) > 1.0, 'perm_ates must have 1000 non-degenerate shuffles')
    ex <- get('exceed', envir = env); pmc <- get('p_mc', envir = env); padd <- get('p_add1', envir = env)
    assert_true(ex == sum(abs(pa) >= abs(get('obs_ate', envir = env))), 'exceed count mismatch')
    assert_true(ex == 0 && pmc == 0 && abs(padd - 1/1001) < 1e-6, 'With seed 20, expect exceed=0, p_mc=0, p_add1=1/1001')
  },
  w3a = function(env) {
    assert_true(exists('cells', envir = env) && exists('did_est', envir = env), 'Assign cells and did_est')
    cl <- get('cells', envir = env); de <- get('did_est', envir = env)
    assert_true(nrow(cl) == 4 && 'mean_visits' %in% names(cl), 'cells must have 4 rows')
    assert_true(is.numeric(de) && length(de) == 1 && abs(de - 0.5775) < 0.02, 'did_est should be ~0.5775')
  },
  w3b = function(env) {
    assert_true(exists('m_did', envir = env), 'Assign m_did')
    md <- get('m_did', envir = env)
    assert_true('treated:post' %in% names(coef(md)), 'Model must include treated:post interaction')
    assert_true(abs(unname(coef(md)['treated:post']) - 0.5775) < 0.02, 'Interaction coefficient should equal ~0.5775')
  },
  w4 = function(env) {
    assert_true(exists('outreach_est', envir = env), 'Assign numeric scalar outreach_est')
    oe <- unname(get('outreach_est', envir = env))
    assert_true(is.numeric(oe) && length(oe) == 1 && abs(oe - 2.99) < 0.05, 'outreach_est does not match valid two-group pre/post estimate (~ +2.99)')
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
