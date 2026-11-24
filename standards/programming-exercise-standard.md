# Programming exercise standard

Applies to CS 61A, STAT 20, and future courses with programming. Read `course-standard.md` and the assignment restrictions in handout-standard section 5b. This standard defines acceptance criteria; it does not assert that existing packets already satisfy them.

## 1. Exercise design and contract

Each exercise has a stable ID, learning objective, prerequisites, provenance, difficulty, and approximate time. A set progresses from a small guided task to independent implementation, debugging or explanation, and transfer to a changed input. Include method selection rather than only filling in a named recipe.

The prompt specifies inputs, outputs, data types and shapes, allowed tools, and relevant edge behavior. State ordering, ties, duplicate handling, missing values, numeric tolerance, randomness, and mutation only where they affect the answer. Show a small example without revealing the implementation. Ask for an interpretation when the computation alone does not demonstrate the objective.

Explain new syntax and execution behavior once in a worked example. Later tasks explain only new features and refer to the relevant guide. Do not reproduce a full argument-by-argument breakdown at every occurrence. Optional hints appear separately from prompts. Starter comments must not accidentally solve an independent task.

## 2. Required artifacts and parity

Provide editable starter files, data or a reproducible data-loading script, tests, and a README with setup and exact run commands. Keep reference implementations separate and subject to the publication rules. Where a browser page or ZIP is provided, its tasks, IDs, data, contracts, and tests must agree with the editable source. Prefer generating these variants from one source; otherwise record an explicit parity check.

The ZIP must work after extraction into a fresh directory. Check its actual members, relative paths, dependencies, and commands. An archive is not a substitute for maintainable source files. Include a small manifest listing exercise IDs, objectives, files, runtime/dependency versions, data provenance, and the browser/download capabilities. Do not imply that a browser runner checks answers if only the downloaded test suite does.

## 3. Tests that assess behavior

Run the reference answer against every test. Also run the untouched starter and plausible incorrect answers. Record which misconception each negative case detects. A positive reference run alone does not validate a checker.

- Test ordinary inputs, a materially changed input, and relevant boundary cases. Avoid testing irrelevant edge cases simply to increase counts.
- Reject hard-coded answers with at least one different fixture. Accept equivalent correct implementations within the stated constraints; do not grade code by matching source text unless syntax itself is the objective.
- Check types, shapes, names and order when the contract requires them. Use numeric tolerances justified by the computation.
- Make failures actionable: identify the violated contract or case. Distinguish syntax/runtime errors from incorrect results and incomplete work.
- Keep starter failures controlled and informative. A placeholder must not count as a passing answer or prevent the rest of the test suite from being collected.

## 4. Course-specific requirements

### CS 61A: Python

Use course-appropriate function signatures, docstrings, and small examples or doctests. Check returned values separately from printed output, and test closure behavior, recursion, mutation, and evaluation order when those are the objective. State implementation restrictions explicitly. Pair tracing questions with implementation and explanation; a trace alone is not programming practice. Use original exercises under the restrictions in handout-standard section 5b.

### CS 61A: SQL

Provide schemas, sample rows, keys, and join cardinalities. Specify result columns and ordering, treatment of ties, duplicate rows and NULLs where applicable. Test joins with unmatched rows and multiple matches, aggregation at the intended grouping level, and DISTINCT only where relevant. Include fixtures that expose a missing join condition or incorrect grouping.

Execute each query against a fresh database. Compare ordered rows only when order is requested; otherwise compare multisets, preserving duplicates. Validate the selected column contract. Do not rely on insertion order or `SELECT *` from a materialized result to establish SQL ordering. A downloadable script must match its checkerâ€™s required table/query interface.

### STAT 20: R

Specify the observational unit, dataset provenance, variable meanings, missing-data policy, target population, and estimand or prediction target. Clearly identify simulated data. Distinguish descriptive, predictive, and causal conclusions. In inference tasks, state the null model, statistic, direction of the tail, and assumptions. In prediction tasks, prevent training/test leakage and name the evaluation measure.

Use the course's R conventions and actual package behavior. A browser compatibility helper must document its supported subset and pass equivalence checks against the intended R operations; do not present a partial shim as full dplyr or infer. Supply deterministic small-data checks as well as justified tolerances for simulations. Fix seeds for reproducible examples without treating one simulated value as a universal answer. Test grouping, missing values, factor levels, and row/column shapes where relevant.

Require a short contextual interpretation and at least one limitation or assumption when it is part of the learning objective. Keep interpretation assessment separate from code execution; say explicitly when it requires self-review.

## 5. Browser behavior

Keep prompts, schemas, and tasks in a flat readable flow with a top index—omit boilerplate meta-paragraphs about WebR preloading, datasets, or session persistence so the page goes directly from the header to the exercises. Use the shared stylesheet, syntax highlighting, readable prose measure, and light/dark theme support. Preserve keyboard access, visible focus, labeled controls, and usable narrow-screen layouts.

Use distinct states: not run, running, executed without checking, checked correct, checked incorrect, and runtime error. Editing a previously checked answer invalidates its prior result and score. Runtime warnings are not automatically incorrect answers. Escape user-controlled output as text.

Define cell dependencies. Run independent tasks in clean environments; dependent tasks must clearly identify their prerequisites and support a reliable reset. Prevent concurrent runs or session restarts from corrupting state. Preserve edits across reloads, namespace saved work by packet and exercise version, and distinguish resetting code from restarting the runtime.

Test startup, a correct answer, a plausible wrong answer, a syntax error, edit-after-pass, reset, reload, runtime restart, and download. Check light and dark themes and keyboard interaction. Test the runtime over the same HTTP/HTTPS serving conditions expected in use, not only a local file URL. Record unavailable network dependencies and recovery behavior.

## 6. Acceptance record

Before marking a packet verified, record:

1. Objective coverage and independent-practice review.
2. Reference, starter, changed-fixture, and misconception-test results.
3. Actual runtime versions and commands; clean-session reproducibility.
4. Browser interaction results, separately from language-level tests.
5. Extracted-ZIP execution and browser/source/download parity.
6. Answer-publication check and known limitations.

Use pass, fail, not tested, or not applicable with a reason for each check. Browser and archive checks are not applicable only when those artifacts are neither provided nor promised. A missing runtime is not a pass. List defects by impact with file/exercise references and a reproducible example; distinguish proven defects from risks requiring live validation.
