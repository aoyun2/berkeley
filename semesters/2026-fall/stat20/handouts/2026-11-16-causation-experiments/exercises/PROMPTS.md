# Week 13 Prompts, Data Notes, and Self-Review Criteria

1. **Case Study 1 (`salaries.csv`, simulated, n = 40):**
   - `Q1.1`: Why can pooled Group_B salary (-31.31k) reverse within Engineering (+2.57k) and Operations (+6.12k)?
   - `Q1.2`: Conditioning on `dept` yields a conditional association (+4.30k within department). Explain why claiming equal-pay causation requires a causal diagram/assumptions separating confounding from mediation and noting unmeasured job/tenure variables.
   - Code `w1a`, `w1b`: assign `sal_by_group`, `sal_by_dept`, `m_sal_raw`, `m_sal_adj`.

2. **Case Study 2 (`notes_study.csv`, simulated, n = 30 randomized):**
   - `Q2.1`: Randomization guarantees comparability in expectation across observed and unobserved traits **by design**; `prior_gpa` (3.158 vs 3.353) is an observed balance check only.
   - `Q2.2`: Sharp null $H_0: Y_i(\text{Longhand}) = Y_i(\text{Laptop})$ for every unit $i$.
   - Code `w2a`, `w2b`: compute `notes_bal`, `obs_ate` (+5.453), and 1,000-rep `perm_ates` (`seed = 20`) reporting `exceed = 0`, `p_mc = 0`, and add-one `p_add1 = 1/1001`. Distinguish Monte Carlo sampling resolution (~0.001) from exact tail probability ($79{,}434 / \binom{30}{15} \approx 0.000512$).

3. **Case Study 3 (`gym_warmup.csv`, simulated, n = 80):**
   - `Q3.1` & `Q3.2`: Naive before-and-after sign reversal (-0.206 vs DID +0.5775); state parallel trends and a concrete violation.
   - Code `w3a`, `w3b`: compute `cells`, `did_est` (+0.5775), and `m_did`.

4. **Case Study 4 — Independent Transfer (`outreach_sim.csv`, simulated, n = 40):**
   - Code `w4`: Choose an estimator accounting for baseline clinic differences and shared seasonal decline (`outreach_est`, expected ~ +2.99).
   - Self-review: State your identification assumption and why post-only (-7.86) and treated-only pre/post (-2.85) comparisons fail.
