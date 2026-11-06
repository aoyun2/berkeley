# STAT 20 official source cache

Retrieved 2026-11-06. This is source preparation only; no dated handout folders have been created. The user requires CS 61A to finish before STAT 20 authoring starts. All prior materials are preserved.

## Canonical sources and extraction

- Course schedule: https://stat20.berkeley.edu/fall-2026/ (`official-homepage.html` and `.txt`; also `official/index.html` and `.txt`).
- Syllabus: https://stat20.berkeley.edu/fall-2026/syllabus.html (`official/syllabus.html` and `.txt`).
- Source tree preserves the original course URL paths beneath `official/`. Every derived text starts with its source URL and retrieval date. PDFs have adjacent `pdftotext -layout` extractions; HTML originals are retained.
- `source-manifest.json` lists every fetched page/PDF, source URL, local original and text path, and failures. `asset-manifest.json` identifies downloaded source figures. `data-manifest.json` records publicly linked datasets.
- `schedule-extracted.json` retains all schedule dates, topics, day-level links and the exact “Due tomorrow” assignment lists. All 15 official instructional weeks are in `../course.toml`; RRR/finals are retained in this raw schedule but are not invented homework weeks.
- `content-identifiers.json` lists each page’s original headings/anchors and callouts. Definitions/results in these notes are usually unnumbered; cite their original heading and lecture path. Preserve numbered examples when the original heading uses a number; do not invent theorem numbering.
- Interactive tutorial code is embedded as base64 JSON in `<script type="webr-N-contents">`. All 279 such blocks are decoded in place in the `.txt` files and separately in `interactive-r-blocks.json`, with original exercise attributes. Some are deliberately erroneous exercises or browser grading setup; do not execute every block indiscriminately.
- The syllabus explicitly calls its online notes/tutorials the textbook. External texts are optional; no separate book or numbered chapter reading is assigned. Therefore the dated notes/tutorials, including Intro-to-Coding Parts 1, 2 and 3, are the primary textbook coverage.

Cache totals: 126 official pages/PDFs (25 PDFs), 273 source figures, 279 decoded interactive R blocks.

## Week mapping

Monday is the week of lectures covered, rather than the week displaying the deadline. Worksheets/labs are due 08:00 America/Los_Angeles on the next Tuesday; the next Monday’s “Due tomorrow” list gives the exact packet name. Reading questions are due 08:00 before each Wednesday/Friday class (Aug 26 explicitly has none). Their actual five questions are private on Gradescope.

| Week | Monday | Lectures covered | Homework due | Assignment |
|---|---|---|---|---|
| 1 | 2026-08-24 | Aug 26: Understanding the World with Data; Aug 28: Taxonomy of Data (and Intro to Coding) | 2026-09-01 | Class Surveys (links are in the Gradescope assignment); Worksheet Packet 1 (Understanding the world + Taxonomy of Data); Lab: Getting Started |
| 2 | 2026-08-31 | Sep 2: Summarizing Categorical Data; Sep 4: Summarizing Numerical Data | 2026-09-08 | Worksheet Packet 2; Lab: Class Survey |
| 3 | 2026-09-07 | Sep 9: A Grammar of Graphics; Sep 11: Data Wrangling | 2026-09-15 | Worksheet Packet 3; Lab: Flights I |
| 4 | 2026-09-14 | Sep 16: Summarizing Numerical Associations; Sep 18: Data Visualization | 2026-09-22 | Worksheet Packet 4; Lab: Flights II |
| 5 | 2026-09-21 | Sep 23: Intro to Probability; Sep 25: Computing Probabilities | 2026-09-29 | Worksheet Packet 5; Lab 5 |
| 6 | 2026-09-28 | Sep 30: Probability Distributions; Oct 2: Random Variables | 2026-10-06 | Worksheet Packet 6; Lab 6 |
| 7 | 2026-10-05 | Oct 7: Expected Value and Variance; Oct 9: Normal Approximation | 2026-10-13 | Worksheet Packet 7; Lab: Elections |
| 8 | 2026-10-12 | Oct 14: From Samples to Populations; Oct 16: Confidence Intervals | 2026-10-20 | Worksheet Packet 8; Lab: People's Park I |
| 9 | 2026-10-19 | Oct 21: Bootstrapping; Oct 23: Intro to Hypothesis Tests | 2026-10-27 | Worksheet Packet 9; Lab: People's Park II; Survey: Mid-semester |
| 10 | 2026-10-26 | Oct 28: Hypothesis Tests II; Oct 30: Wrong By Design | 2026-11-03 | Worksheet Packet 10; Lab: Arbuthnot |
| 11 | 2026-11-02 | Nov 4: Intro to Prediction and Least Squares; Nov 6: Improving Predictions and Overfitting | 2026-11-10 | Worksheet Packet 11; Lab: Baseball |
| 12 | 2026-11-09 | Nov 11: Holiday: Veterans Day; Nov 13: Logistic Regression | 2026-11-17 | Worksheet Packet 12; Lab: Diagnosing Cancer |
| 13 | 2026-11-16 | Nov 18: Defining Causation; Nov 20: Randomized Experiments | 2026-11-24 | Worksheet Packet 13; Lab: A Matter of Taste |
| 14 | 2026-11-23 | Nov 25: Holiday: Thanksgiving; Nov 27: Holiday: Thanksgiving | Not applicable: no new assignment announced | No new worksheet packet or lab announced (Thanksgiving week) |
| 15 | 2026-11-30 | Dec 2: Causal Effects in Observational Studies; Dec 4: Impromptu Science | 2026-12-08 | Worksheet Packet 15 |

Historical authoring scope: **11 weeks**: 2026-08-24, 2026-08-31, 2026-09-07, 2026-09-14, 2026-09-21, 2026-09-28, 2026-10-05, 2026-10-12, 2026-10-19, 2026-10-26, 2026-11-02. Do not author Nov 9 or later.

## Exact source links and original exercise identifiers by week

### Week 1 — 2026-08-24

- Aug 26: Understanding the World with Data.
  - Notes: [official/1-questions-and-data/01-understanding-the-world/notes.html](official/1-questions-and-data/01-understanding-the-world/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/1-questions-and-data/01-understanding-the-world/notes.html)).
  - Slides: [official/1-questions-and-data/01-understanding-the-world/slides.html](official/1-questions-and-data/01-understanding-the-world/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/1-questions-and-data/01-understanding-the-world/slides.html)).
  - Worksheet: [official/1-questions-and-data/01-understanding-the-world/ws.pdf](official/1-questions-and-data/01-understanding-the-world/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/1-questions-and-data/01-understanding-the-world/ws.pdf)).
- Aug 28: Taxonomy of Data (and Intro to Coding).
  - Notes: [official/1-questions-and-data/02-taxonomy-of-data/notes.html](official/1-questions-and-data/02-taxonomy-of-data/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/1-questions-and-data/02-taxonomy-of-data/notes.html)).
  - Tutorial: [official/1-questions-and-data/02-taxonomy-of-data/tutorial.html](official/1-questions-and-data/02-taxonomy-of-data/tutorial.html) ([source](https://stat20.berkeley.edu/fall-2026/1-questions-and-data/02-taxonomy-of-data/tutorial.html)).
  - Slides: [official/1-questions-and-data/02-taxonomy-of-data/slides.html](official/1-questions-and-data/02-taxonomy-of-data/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/1-questions-and-data/02-taxonomy-of-data/slides.html)).
  - Worksheet: [official/1-questions-and-data/02-taxonomy-of-data/ws.pdf](official/1-questions-and-data/02-taxonomy-of-data/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/1-questions-and-data/02-taxonomy-of-data/ws.pdf)).
  - Lab: Getting Started: [official/1-questions-and-data/labs/unvotes/part-2.html](official/1-questions-and-data/labs/unvotes/part-2.html) ([source](https://stat20.berkeley.edu/fall-2026/1-questions-and-data/labs/unvotes/part-2.html)). Original identifiers: Question 0, Question 1, Question 2, Question 3, Question 4, Question 5, Question 6 - UN Votes.
- Extra published practice/resource: [Types of claims](https://stat20.berkeley.edu/fall-2026/extras/types-of-claims.html).
- Extra published practice/resource: [Data types and data frames](https://stat20.berkeley.edu/fall-2026/extras/data-types-data-frames.html).
- Extra published practice/resource: [Coding basics](https://stat20.berkeley.edu/fall-2026/extras/coding-basics.html).
- Extra published practice/resource: [▶️ Website and Tools Overview](https://www.youtube.com/watch?v=vqELFcehTUk).
- Extra published practice/resource: [▶️ RStudio Tour and Lab 1](https://www.youtube.com/watch?v=Q86Yf2MlRZU).
- Complete Intro-to-Coding required continuation: `official/1-questions-and-data/02-taxonomy-of-data/tutorial-part-2.txt`, `tutorial-part-3.txt`; additional genuine practice `tutorial-part-ex.txt`.

### Week 2 — 2026-08-31

- Sep 2: Summarizing Categorical Data.
  - Notes: [official/2-summarizing-data/01-summarizing-categorical-data/notes.html](official/2-summarizing-data/01-summarizing-categorical-data/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/01-summarizing-categorical-data/notes.html)).
  - Tutorial: [official/2-summarizing-data/01-summarizing-categorical-data/tutorial.html](official/2-summarizing-data/01-summarizing-categorical-data/tutorial.html) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/01-summarizing-categorical-data/tutorial.html)).
  - Slides: [official/2-summarizing-data/01-summarizing-categorical-data/slides.html](official/2-summarizing-data/01-summarizing-categorical-data/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/01-summarizing-categorical-data/slides.html)).
  - Worksheet: [official/2-summarizing-data/01-summarizing-categorical-data/ws.pdf](official/2-summarizing-data/01-summarizing-categorical-data/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/01-summarizing-categorical-data/ws.pdf)).
  - Lab: Class Survey: [official/2-summarizing-data/labs/class-survey/part-2.html](official/2-summarizing-data/labs/class-survey/part-2.html) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/labs/class-survey/part-2.html)). Original identifiers: Question 1, Question 2, Question 3, Question 4, Question 5, Question 6, Question 7, Question 8.
- Sep 4: Summarizing Numerical Data.
  - Notes: [official/2-summarizing-data/02-summarizing-numerical-data/notes.html](official/2-summarizing-data/02-summarizing-numerical-data/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/02-summarizing-numerical-data/notes.html)).
  - Tutorial: [official/2-summarizing-data/02-summarizing-numerical-data/tutorial.html](official/2-summarizing-data/02-summarizing-numerical-data/tutorial.html) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/02-summarizing-numerical-data/tutorial.html)).
  - Slides: [official/2-summarizing-data/02-summarizing-numerical-data/slides.html](official/2-summarizing-data/02-summarizing-numerical-data/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/02-summarizing-numerical-data/slides.html)).
  - Worksheet: [official/2-summarizing-data/02-summarizing-numerical-data/ws.pdf](official/2-summarizing-data/02-summarizing-numerical-data/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/02-summarizing-numerical-data/ws.pdf)).
- Extra published practice/resource: [Summarization and coding](https://stat20.berkeley.edu/fall-2026/extras/summarization_code.html).
- Extra published practice/resource: [▶️ Quiz 1 Solution](https://youtu.be/PeiFgj4Lo_A).

### Week 3 — 2026-09-07

- Sep 9: A Grammar of Graphics.
  - Notes: [official/2-summarizing-data/03-a-grammar-of-graphics/notes.html](official/2-summarizing-data/03-a-grammar-of-graphics/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/03-a-grammar-of-graphics/notes.html)).
  - Tutorial: [official/2-summarizing-data/03-a-grammar-of-graphics/tutorial.html](official/2-summarizing-data/03-a-grammar-of-graphics/tutorial.html) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/03-a-grammar-of-graphics/tutorial.html)).
  - Slides: [official/2-summarizing-data/03-a-grammar-of-graphics/slides.html](official/2-summarizing-data/03-a-grammar-of-graphics/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/03-a-grammar-of-graphics/slides.html)).
  - Worksheet: [official/2-summarizing-data/03-a-grammar-of-graphics/ws.pdf](official/2-summarizing-data/03-a-grammar-of-graphics/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/03-a-grammar-of-graphics/ws.pdf)).
  - Lab: Flights I: [official/2-summarizing-data/labs/flights/part-1.html](official/2-summarizing-data/labs/flights/part-1.html) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/labs/flights/part-1.html)). Original identifiers: Question 1, Question 2, Question 3, Question 4, Question 5, Question 6, Question 7, Question 8, Question 9.
- Sep 11: Data Wrangling.
  - Notes: [official/2-summarizing-data/04-data-wrangling/notes.html](official/2-summarizing-data/04-data-wrangling/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/04-data-wrangling/notes.html)).
  - Tutorial: [official/2-summarizing-data/04-data-wrangling/tutorial.html](official/2-summarizing-data/04-data-wrangling/tutorial.html) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/04-data-wrangling/tutorial.html)).
  - Slides: [official/2-summarizing-data/04-data-wrangling/slides.html](official/2-summarizing-data/04-data-wrangling/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/04-data-wrangling/slides.html)).
  - Worksheet: [official/2-summarizing-data/04-data-wrangling/ws.pdf](official/2-summarizing-data/04-data-wrangling/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/04-data-wrangling/ws.pdf)).
- Extra published practice/resource: [Data Wrangling](https://stat20.berkeley.edu/fall-2026/extras/data-wrangling.html).
- Extra published practice/resource: [▶️ Grammar of Graphics WS solution](https://youtu.be/xSaetGObPfo).
- Extra published practice/resource: [▶️ Data Wrangling ("Conditioning") WS solution](https://youtu.be/wKiZ8CavX80).
- Extra published practice/resource: [▶️ Lab 3: Flights I solution](https://youtu.be/0rAZ4pyGbrM).

### Week 4 — 2026-09-14

- Sep 16: Summarizing Numerical Associations.
  - Notes: [official/2-summarizing-data/05-summarizing-associations/notes.html](official/2-summarizing-data/05-summarizing-associations/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/05-summarizing-associations/notes.html)).
  - Tutorial: [official/2-summarizing-data/05-summarizing-associations/tutorial.html](official/2-summarizing-data/05-summarizing-associations/tutorial.html) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/05-summarizing-associations/tutorial.html)).
  - Slides: [official/2-summarizing-data/05-summarizing-associations/slides.html](official/2-summarizing-data/05-summarizing-associations/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/05-summarizing-associations/slides.html)).
  - Worksheet: [official/2-summarizing-data/05-summarizing-associations/ws.pdf](official/2-summarizing-data/05-summarizing-associations/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/05-summarizing-associations/ws.pdf)).
  - Lab: Flights II: [official/2-summarizing-data/labs/flights/part-2.html](official/2-summarizing-data/labs/flights/part-2.html) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/labs/flights/part-2.html)). Original identifiers: Question 1, Question 2, Question 3, Question 4, Question 5, Question 6.
- Sep 18: Data Visualization.
  - Notes: [official/2-summarizing-data/06-data-visualization/notes.html](official/2-summarizing-data/06-data-visualization/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/06-data-visualization/notes.html)).
  - Tutorial: [official/2-summarizing-data/06-data-visualization/tutorial.html](official/2-summarizing-data/06-data-visualization/tutorial.html) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/06-data-visualization/tutorial.html)).
  - Slides: [official/2-summarizing-data/06-data-visualization/slides.html](official/2-summarizing-data/06-data-visualization/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/06-data-visualization/slides.html)).
  - Worksheet: [official/2-summarizing-data/06-data-visualization/ws.pdf](official/2-summarizing-data/06-data-visualization/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/2-summarizing-data/06-data-visualization/ws.pdf)).
- Extra published practice/resource: [▶️ Summarizing Numerical Associations WS solution](https://youtu.be/5kx9SgBpAxw).
- Extra published practice/resource: [▶️ Data Visualization WS solution](https://www.youtube.com/watch?v=LTm0FPds8nw).
- Extra published practice/resource: [▶️ Lab 4: Flights II solution](https://youtu.be/V0D0ykS2Hjk).

### Week 5 — 2026-09-21

- Sep 23: Intro to Probability.
  - Notes: [official/3-generalization/01-prob-foundations/notes.html](official/3-generalization/01-prob-foundations/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/01-prob-foundations/notes.html)).
  - Tutorial: [official/3-generalization/01-prob-foundations/tutorial.html](official/3-generalization/01-prob-foundations/tutorial.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/01-prob-foundations/tutorial.html)).
  - Slides: [official/3-generalization/01-prob-foundations/slides.html](official/3-generalization/01-prob-foundations/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/01-prob-foundations/slides.html)).
  - Worksheet: [official/3-generalization/01-prob-foundations/ws.pdf](official/3-generalization/01-prob-foundations/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/01-prob-foundations/ws.pdf)).
  - Lab: Probability Foundations: [official/3-generalization/labs/prob-foundations/lab.html](official/3-generalization/labs/prob-foundations/lab.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/labs/prob-foundations/lab.html)). Original identifiers: Question 1, Question 2, Question 3, Question 4, Question 5 (The birthday problem).
- Sep 25: Computing Probabilities.
  - Notes: [official/3-generalization/02-computing-probs/notes.html](official/3-generalization/02-computing-probs/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/02-computing-probs/notes.html)).
  - Tutorial: [official/3-generalization/02-computing-probs/tutorial.html](official/3-generalization/02-computing-probs/tutorial.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/02-computing-probs/tutorial.html)).
  - Slides: [official/3-generalization/02-computing-probs/slides.html](official/3-generalization/02-computing-probs/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/02-computing-probs/slides.html)).
  - Worksheet: [official/3-generalization/02-computing-probs/ws.pdf](official/3-generalization/02-computing-probs/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/02-computing-probs/ws.pdf)).
- Extra published practice/resource: [Intro to Probability](https://stat20.berkeley.edu/fall-2026/extras/intro-prob.html).
- Extra published practice/resource: [Box Models](https://stat20.berkeley.edu/fall-2026/extras/box-models.html).
- Extra published practice/resource: [Mutually Exclusive vs. Independent](https://stat20.berkeley.edu/fall-2026/extras/mutually-exclusive-vs-independent.html).
- Extra published practice/resource: [▶️ Intro to Probability WS solution](https://www.youtube.com/watch?v=N--HSHts8bo).

### Week 6 — 2026-09-28

- Sep 30: Probability Distributions.
  - Notes: [official/3-generalization/03-probability-dsns/notes.html](official/3-generalization/03-probability-dsns/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/03-probability-dsns/notes.html)).
  - Tutorial: [official/3-generalization/03-probability-dsns/tutorial.html](official/3-generalization/03-probability-dsns/tutorial.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/03-probability-dsns/tutorial.html)).
  - Slides: [official/3-generalization/03-probability-dsns/slides.html](official/3-generalization/03-probability-dsns/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/03-probability-dsns/slides.html)).
  - Worksheet: [official/3-generalization/03-probability-dsns/ws.pdf](official/3-generalization/03-probability-dsns/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/03-probability-dsns/ws.pdf)).
  - Lab: Probability Distributions: [official/3-generalization/labs/prob-distributions/lab.html](official/3-generalization/labs/prob-distributions/lab.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/labs/prob-distributions/lab.html)). Original identifiers: Part I: Are you Psychic?, Question 1, Question 2, Question 3, Question 4, Part II: Let’s roll some dice!.
- Oct 2: Random Variables.
  - Notes: [official/3-generalization/04-random-variables/notes.html](official/3-generalization/04-random-variables/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/04-random-variables/notes.html)).
  - Tutorial: [official/3-generalization/04-random-variables/tutorial.html](official/3-generalization/04-random-variables/tutorial.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/04-random-variables/tutorial.html)).
  - Slides: [official/3-generalization/04-random-variables/slides.html](official/3-generalization/04-random-variables/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/04-random-variables/slides.html)).
  - Worksheet: [official/3-generalization/04-random-variables/ws.pdf](official/3-generalization/04-random-variables/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/04-random-variables/ws.pdf)).
- Extra published practice/resource: [Distributions, Parameters, Probabilities](https://stat20.berkeley.edu/fall-2026/extras/distributions-parameters-probabilities.html).
- Extra published practice/resource: [Coding Probability](https://stat20.berkeley.edu/fall-2026/extras/coding-probability.html).
- Extra published practice/resource: [Reading CDFs](https://stat20.berkeley.edu/fall-2026/extras/reading-cdfs.html).
- Extra published practice/resource: [▶️ Probability Distributions WS solution](https://www.youtube.com/watch?v=dGXuOY9Kkx4).
- Extra published practice/resource: [CDF Probability Monster](https://stat20.berkeley.edu/fall-2026/extras/standalone/probability-eating-monster.html).

### Week 7 — 2026-10-05

- Oct 7: Expected Value and Variance.
  - Notes: [official/3-generalization/05-ev-se/notes.html](official/3-generalization/05-ev-se/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/05-ev-se/notes.html)).
  - Slides: [official/3-generalization/05-ev-se/slides.html](official/3-generalization/05-ev-se/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/05-ev-se/slides.html)).
  - Worksheet: [official/3-generalization/05-ev-se/ws.pdf](official/3-generalization/05-ev-se/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/05-ev-se/ws.pdf)).
  - Lab: Elections: [official/3-generalization/labs/elections/lab.html](official/3-generalization/labs/elections/lab.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/labs/elections/lab.html)). Original identifiers: Question 1, Question 2, Question 3, Question 4, Question 5, Question 6.
- Oct 9: Normal Approximation.
  - Notes: [official/3-generalization/06-normal-approx/notes.html](official/3-generalization/06-normal-approx/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/06-normal-approx/notes.html)).
  - Tutorial: [official/3-generalization/06-normal-approx/tutorial.html](official/3-generalization/06-normal-approx/tutorial.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/06-normal-approx/tutorial.html)).
  - Slides: [official/3-generalization/06-normal-approx/slides.html](official/3-generalization/06-normal-approx/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/06-normal-approx/slides.html)).
  - Worksheet: [official/3-generalization/06-normal-approx/ws.pdf](official/3-generalization/06-normal-approx/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/06-normal-approx/ws.pdf)).
- Extra published practice/resource: [Box Models (also linked in Week 5)](https://stat20.berkeley.edu/fall-2026/extras/box-models.html).
- Extra published practice/resource: [EV, Var, SD](https://stat20.berkeley.edu/fall-2026/extras/ev-var-sd.html).

### Week 8 — 2026-10-12

- Oct 14: From Samples to Populations.
  - Notes: [official/3-generalization/07-from-samps-to-pops/notes.html](official/3-generalization/07-from-samps-to-pops/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/07-from-samps-to-pops/notes.html)).
  - Slides: [official/3-generalization/07-from-samps-to-pops/slides.html](official/3-generalization/07-from-samps-to-pops/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/07-from-samps-to-pops/slides.html)).
  - Worksheet: [official/3-generalization/07-from-samps-to-pops/ws.pdf](official/3-generalization/07-from-samps-to-pops/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/07-from-samps-to-pops/ws.pdf)).
  - Lab: People's Park: [official/3-generalization/labs/peoples-park/lab.html](official/3-generalization/labs/peoples-park/lab.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/labs/peoples-park/lab.html)). Original identifiers: Question 1, Question 2, Question 3, Question 4, Question 5, Question 6, Question 7, Question 8.
- Oct 16: Confidence Intervals.
  - Notes: [official/3-generalization/08-confidence-intervals/notes.html](official/3-generalization/08-confidence-intervals/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/08-confidence-intervals/notes.html)).
  - Slides: [official/3-generalization/08-confidence-intervals/slides.html](official/3-generalization/08-confidence-intervals/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/08-confidence-intervals/slides.html)).
  - Worksheet: [official/3-generalization/08-confidence-intervals/ws.pdf](official/3-generalization/08-confidence-intervals/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/08-confidence-intervals/ws.pdf)).

### Week 9 — 2026-10-19

- Oct 21: Bootstrapping.
  - Notes: [official/3-generalization/09-bootstrapping/notes.html](official/3-generalization/09-bootstrapping/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/09-bootstrapping/notes.html)).
  - Tutorial: [official/3-generalization/09-bootstrapping/tutorial.html](official/3-generalization/09-bootstrapping/tutorial.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/09-bootstrapping/tutorial.html)).
  - Slides: [official/3-generalization/09-bootstrapping/slides.html](official/3-generalization/09-bootstrapping/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/09-bootstrapping/slides.html)).
  - Worksheet: [official/3-generalization/09-bootstrapping/ws.pdf](official/3-generalization/09-bootstrapping/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/09-bootstrapping/ws.pdf)).
  - Survey: Mid-semester: https://forms.gle/sQbYpDmHNsyW3Xk69.
  - Lab: People's Park II: [official/3-generalization/labs/peoples-park/lab-2.html](official/3-generalization/labs/peoples-park/lab-2.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/labs/peoples-park/lab-2.html)). Original identifiers: Question 1 (People’s Park), Question 2 (People’s Park), Question 3 (MythBusters).
- Oct 23: Intro to Hypothesis Tests.
  - Notes: [official/3-generalization/10-hypothesis-tests/notes.html](official/3-generalization/10-hypothesis-tests/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/10-hypothesis-tests/notes.html)).
  - Tutorial: [official/3-generalization/10-hypothesis-tests/tutorial.html](official/3-generalization/10-hypothesis-tests/tutorial.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/10-hypothesis-tests/tutorial.html)).
  - Slides: [official/3-generalization/10-hypothesis-tests/slides.html](official/3-generalization/10-hypothesis-tests/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/10-hypothesis-tests/slides.html)).
  - Worksheet: [official/3-generalization/10-hypothesis-tests/ws.pdf](official/3-generalization/10-hypothesis-tests/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/10-hypothesis-tests/ws.pdf)).
- Extra published practice/resource: [▶️ Quiz 3 Solution](https://youtu.be/2vQ0if7YtTg).
- Extra published practice/resource: [Alpacas and hypothesis tests](https://www.jwilber.me/permutationtest/).

### Week 10 — 2026-10-26

- Oct 28: Hypothesis Tests II.
  - Notes: [official/3-generalization/11-hypothesis-tests-2/notes.html](official/3-generalization/11-hypothesis-tests-2/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/11-hypothesis-tests-2/notes.html)).
  - Slides: [official/3-generalization/11-hypothesis-tests-2/slides.html](official/3-generalization/11-hypothesis-tests-2/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/11-hypothesis-tests-2/slides.html)).
  - Worksheet: [official/3-generalization/11-hypothesis-tests-2/ws.pdf](official/3-generalization/11-hypothesis-tests-2/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/11-hypothesis-tests-2/ws.pdf)).
  - Lab: Arbuthnot: [official/3-generalization/labs/review-lab/lab.html](official/3-generalization/labs/review-lab/lab.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/labs/review-lab/lab.html)). Original identifiers: Question 1, Question 2, Question 3, Question 4, Question 5, Question 6, Question 7, Question 8, Question 9, Question 10, Question 11.
- Oct 30: Wrong By Design.
  - Notes: [official/3-generalization/12-wrong-by-design/notes.html](official/3-generalization/12-wrong-by-design/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/12-wrong-by-design/notes.html)).
  - Slides: [official/3-generalization/12-wrong-by-design/slides.html](official/3-generalization/12-wrong-by-design/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/12-wrong-by-design/slides.html)).
  - Worksheet: [official/3-generalization/12-wrong-by-design/ws.pdf](official/3-generalization/12-wrong-by-design/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/3-generalization/12-wrong-by-design/ws.pdf)).

### Week 11 — 2026-11-02

- Nov 4: Intro to Prediction and Least Squares.
  - Notes: [official/4-prediction/01-method-of-least-squares/notes.html](official/4-prediction/01-method-of-least-squares/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/4-prediction/01-method-of-least-squares/notes.html)).
  - Tutorial: [official/4-prediction/01-method-of-least-squares/tutorial.html](official/4-prediction/01-method-of-least-squares/tutorial.html) ([source](https://stat20.berkeley.edu/fall-2026/4-prediction/01-method-of-least-squares/tutorial.html)).
  - Slides: [official/4-prediction/01-method-of-least-squares/slides.html](official/4-prediction/01-method-of-least-squares/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/4-prediction/01-method-of-least-squares/slides.html)).
  - Worksheet: [official/4-prediction/01-method-of-least-squares/ws.pdf](official/4-prediction/01-method-of-least-squares/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/4-prediction/01-method-of-least-squares/ws.pdf)).
  - Lab: Baseball: [official/4-prediction/labs/baseball/lab.html](official/4-prediction/labs/baseball/lab.html) ([source](https://stat20.berkeley.edu/fall-2026/4-prediction/labs/baseball/lab.html)). Original identifiers: Question 1, Question 2, Question 3, Question 4, Question 5, Question 6, Question 7, Question 8, Question 9, Question 10.
- Nov 6: Improving Predictions and Overfitting.
  - Notes: [official/4-prediction/02-improving-predictions-overfitting/notes.html](official/4-prediction/02-improving-predictions-overfitting/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/4-prediction/02-improving-predictions-overfitting/notes.html)).
  - Tutorial: [official/4-prediction/02-improving-predictions-overfitting/tutorial.html](official/4-prediction/02-improving-predictions-overfitting/tutorial.html) ([source](https://stat20.berkeley.edu/fall-2026/4-prediction/02-improving-predictions-overfitting/tutorial.html)).
  - Slides: [official/4-prediction/02-improving-predictions-overfitting/slides.html](official/4-prediction/02-improving-predictions-overfitting/slides.html) ([source](https://stat20.berkeley.edu/fall-2026/4-prediction/02-improving-predictions-overfitting/slides.html)).
  - Worksheet: [official/4-prediction/02-improving-predictions-overfitting/ws.pdf](official/4-prediction/02-improving-predictions-overfitting/ws.pdf) ([source](https://stat20.berkeley.edu/fall-2026/4-prediction/02-improving-predictions-overfitting/ws.pdf)).

### Week 12 — 2026-11-09

- Nov 11: Holiday: Veterans Day.
- Nov 13: Logistic Regression.
  - Notes: [official/4-prediction/05-logistic-regression/notes.html](official/4-prediction/05-logistic-regression/notes.html) ([source](https://stat20.berkeley.edu/fall-2026/4-prediction/05-logistic-regression/notes.html)).
  - Tutorial: [official/4-prediction/05-logistic-regression/tutorial.html](official/4-prediction/05-logistic-regression/tutorial.html) ([source](https://stat20.berkeley.edu/fall-2026/4-prediction/05-logistic-regression/tutorial.html)).

### Week 13 — 2026-11-16

- Nov 18: Defining Causation.
- Nov 20: Randomized Experiments.

### Week 14 — 2026-11-23

- Nov 25: Holiday: Thanksgiving.
- Nov 27: Holiday: Thanksgiving.

### Week 15 — 2026-11-30

- Dec 2: Causal Effects in Observational Studies.
- Dec 4: Impromptu Science.

## Exams, practice and source discrepancies

- Final is confirmed by both schedule and syllabus: **Wednesday December 16, 2026, 19:00–22:00 America/Los_Angeles**. Alternate final remains TBD; the stated likely time is Dec 17, 08:00–11:00, so it is not recorded as a confirmed dated exam.
- Quizzes are randomized 50-minute CBTF/PrairieTest slots, not common-time exams. Windows: Quiz 1 Sep 8–11 (Weeks 1–2), Quiz 2 Sep 28–Oct 2 (Weeks 3–5), Quiz 3 Oct 19–23 (Weeks 6–8), Quiz 4 Nov 19–24 (Weeks 9–12). Retake windows are separately represented.
- **Conflicting Quiz 4 retake close date:** homepage says Nov 30–Dec 10; syllabus table says Nov 30–Dec 4. `course.toml` records homepage Dec 10 with explicit conflict. Verify PrairieTest/staff before relying on this deadline.
- **Conflicting registration dates:** homepage Quiz 2 opens Sep 21 (syllabus table Sep 26), Quiz 3 Oct 12 (table Oct 16), Quiz 4 Nov 12 (table Nov 7). The syllabus also attaches incorrect weekday names to several registration dates. These are not lecture or homework deadlines.
- **No Packet 14:** official Week 14 lists Thanksgiving on Nov 25 and 27, no new work, and no following-week deadline. Its schedule row says no new assignment and due not applicable, rather than inventing a date. Packet 15 is explicitly due Dec 8.
- **Week 7 Friday worksheet:** the official linked PDF is actually titled “Worksheet: Quiz Review” (not “Normal Approximation”). Preserve its title/numbering while covering the dated Normal Approximation notes.
- **People’s Park II lab naming:** the schedule uses that title, but the linked lab’s questions concern the MythBusters yawning experiment (`yawn` data). The actual question text, not the misleading title, determines solutions.
- Notes index has a broken generic `slides.html` link (404); actual 22 lecture slide links download successfully. Three From-Samples-to-Populations note reference links incorrectly point inside that lecture folder (404); the same documents download from the linked People’s Park lab reference folder.
- No actual public practice/past-exam PDF is linked from this semester homepage, notes index or Extras. Official quiz-solution videos exist (Quiz 1 and Quiz 3); the cache preserves those URLs but does not pretend videos are text exams. Use the real weekly worksheets, lab questions and published Extras as available genuine practice.
- A supplementary multiple-linear-regression note linked internally was preserved under `official/2-summarizing-data/06-multiple-linear-regression/notes.txt`. It is not in this official semester lecture calendar and must not be silently moved into historical week coverage.

## Missing private inputs and future materials

- **Week 2 / Aug 31:** Class Survey lab requires `class_survey_f26.csv` and `class_survey_questions_f26.pdf` from authenticated Ed resources: https://edstem.org/us/courses/101622/resources . Assignment questions are cached; data-specific numeric/plot solutions and exact survey-response wording cannot be recovered from the public course. Do not substitute the older `stat20data::class_survey` dataset.
- **Week 10 / Oct 26:** Arbuthnot lab Q1–3 depend on a parish birth-record image only at https://bcourses.berkeley.edu/courses/1557153/files . The questions are cached, but that image is missing. Its cited historical paper URL https://www.york.ac.uk/depts/maths/histstat/arbuthnot.pdf returned HTTP 403. `stat20data::arbuthnot` and `present` still support the later data questions.
- **Reading questions and surveys:** exact Gradescope-only questions/class surveys and survey submission links are not public. The calendar records the actual assignment names and deadlines; do not invent question statements.
- **Nov 9 onward:** logistic-regression notes/tutorial are published; its lab/worksheet/slides are not linked. Nov 18/20 causality notes, labs, worksheets, and Dec 2/4 materials are placeholders with no actual links. Refresh later; source-only schedule topics are recorded without invented documents.
- **Lab empirical data:** published class psychic scores, Russia 2018 precinct totals and Georgia 2020 election results have been cached in `data/` with full source URLs. The psychic scores are a snapshot of the actual published class sheet; treat it as dated data rather than a permanent theoretical distribution.

## R execution preparation

- No exact R version or package lockfile is specified by the public course. The native `|>` operator requires R >= 4.1.0.
- Course data repository verified: https://github.com/stat20/stat20data ; default branch `master`, version **0.1.7**, commit `2536a78879339a43296e2d9b8eb35e7dc6de8a0d`. Its DESCRIPTION is preserved in `data/stat20data-DESCRIPTION.txt`; it imports ggplot2, dplyr, rmarkdown, broom, gridExtra. This package is not available from CRAN under that name.
- Pinned install: `remotes::install_github("stat20/stat20data@2536a78879339a43296e2d9b8eb35e7dc6de8a0d")`.
- Actual historical code imports: `tidyverse`, `stat20data`, `palmerpenguins`, `ggthemes`, `gapminder`, `patchwork`, `infer`, `broom`, `Lahman`; `readxl` is introduced in Week 1 tutorial Part 3. `dplyr` and `ggplot2` are also loaded explicitly.
- `gradethis` and `webr::install` occur only in browser grading infrastructure; they are not necessary for desktop execution of the teaching examples. Future logistic regression uses `openintro`. See `r-package-inventory.json` for complete detected imports.
- Representative real smoke test sent to the tooling agent: run the Lab 1 `unvotes` filter/group/summarise pipeline for UK/US/Turkey, verify proportions in [0,1], and render the facet plot. This exercises real dataset loading, modern native pipes, dplyr, ggplot2 and loess; merely importing packages is insufficient.
