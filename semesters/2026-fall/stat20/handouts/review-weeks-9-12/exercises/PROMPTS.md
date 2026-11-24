# Weeks 9-12 Prompts, Data Notes, and Self-Review Criteria

1. **Ice Cream (`icecream.csv`, n=12 train; `new_icecream.csv`, n=4 test):** slope, extrapolation limit (`temp_f = 30`), held-out test RMSE (`1.878`). Blocks `c1a`, `c1b`.
2. **Stopping Distance (`driving.csv`, n=18; `new_driving.csv`, n=6):** quadratic `I(speed_mph^2)` vs linear RMSE (`8.03` vs `0.99`), indicator interpretation (`+28.2 ft`). Blocks `c2a`, `c2b`.
3. **Used Cars (`cars_train.csv`, n=24; `cars_test.csv`, n=12):** Compare additive (`test RMSE = 1.455`), interaction (`0.913`), and rank-17 polynomial (`train R^2 = 0.9963`, `train RMSE = 0.415`, `test RMSE = 0.953`). Blocks `c3a`, `c3b`.
4. **Palmer Penguins (`penguins_sample.csv`, n=36 simulated subset):** Group stats & 1,000-replicate bootstrap (`replace = TRUE`, `seed = 20`, 95% CI `[37.058, 39.817]`). Blocks `c4a`, `c4b`.
5. **Resume Callbacks (`resumes.csv`, n=40 simulated):** Logistic regression (`m_log`, `odds_ratios`), threshold `0.5` (`mcr = 0.275`, `precision = 0.727`, `recall = 0.762`). Blocks `c5a`, `c5b`.
6. **Independent Transfer (`c6`):** Select cutoff `th_c6` from `{0.3, 0.5, 0.7}` achieving `recall >= 0.85` while keeping precision as high as possible (`th_c6 = 0.3`, `recall = 0.905`, `precision = 0.655`, `mcr = 0.300`) and interpret the tradeoff.
