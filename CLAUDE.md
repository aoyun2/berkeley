# Repository Instructions for Claude

Read and follow [`standards/handout-standard.md`](standards/handout-standard.md) before creating or editing any weekly packet, handout, figure, solutions file, or coding exercise set.

## Non-Negotiable Quality Gate for Every Weekly Packet

1. **Direct Intuition & Natural Prose (All Courses)**
   - Lead with concrete intuition and motivation: state *why* a definition or construction works and *how* someone finds it.
   - Write natural, direct explanatory sentences. Ban mannered, clipped, or aphoristic slogans (e.g., `"One pipeline per interval; each function adds one step."`, `"Listing them is hopeless; counting them is a short function."`, or telegraphic semicolon fragments).
   - Zero exclamation marks (`!`), zero contractions, zero banter, zero rhetorical `Why?` / `How?` filler prompts.
   - Never pack multi-sentence `(i)/(ii)` or `(1)/(2)` walls of text inside a paragraph; use proper LaTeX `itemize` / `enumerate` lists.

2. **Zero Page Cutoffs**
   - Keep `templates/handout.sty` `\Needspace` guards intact (`14\baselineskip` on theorem/prop/lemma/corollary environments).
   - Add `\Needspace{14\baselineskip}`–`\Needspace{16\baselineskip}` before tall figures, multi-line code listings, piece-by-piece code tables, or coupled theorem/idea pairs so headings and short boxes are never stranded at a page bottom.

3. **1980s Monochrome Textbook Figures (`TikZ` / `tikz-cd` / `pgfplots`) — Follow [`.claude/skills/berkeley-latex/SKILL.md`](.claude/skills/berkeley-latex/SKILL.md)**
   - Every figure across all 4 courses must look like a **1980s mathematics textbook or journal paper** (Springer GTM, Halmos, Axler, Strang, *SICP* 1985, *JASA*): pure black-and-gray ink on white paper (`black`, `black!75`, `black!55`, light `black!4`–`black!14` shading, or `pattern=north east lines` hatching), **zero colors inside figures** (and zero color words in `\figcap`), and **zero `rounded corners` "toy block" boxes**.
   - **Authentic 1980s geometry**: use smooth ovals/ellipses (`ellipse`) for nested flags, domain/codomain sets, and operator hierarchies; use sharp-cornered (`0pt`) thin black hairline rectangles for Strang four-subspace diagrams, matrix blocks ($A=CR$, REF/RREF), and *SICP* environment frames. Distinguish curves, vectors, and points via `solid` / `dashed` / `densely dotted` / `dash dot` line styles and filled `•` vs hollow `o` vs `×` markers.
   - **Ban "vibecoded slop" cards & side walls**: never use chunky rounded-rectangle cards, never add side bullet-list walls inside TikZ (put explanations in `\figcap` or crisp 1–2 line black legends), and never use `fill=white` / `fill=figbg` label pills.
   - **Commutative diagrams (`tikz-cd`)**: `templates/handout.sty` loads `tikz-cd`. Use `\begin{tikzcd}...\end{tikzcd}` with plain black math nodes, thin arrows, generous `column sep`, and `"{...}"` inner braces around any arrow label containing a comma.
   - **Genuine LaTeX matrices in figures**: never hand-draw TikZ bracket lines around positioned nodes. Put genuine `\begin{pmatrix}...\end{pmatrix}` / `\begin{bmatrix}...\end{bmatrix}` inside display math (`\begin{minipage}{Xcm}\[...\]\end{minipage}` inside a TikZ `\node`, never `$3\times 3+$` inline `$...$`).
   - **Strict 4-layer draw order for overlapping disks/regions**: (1) ALL faint monochrome fills first (`fill=black,fill opacity=0.045`), (2) axes & origin, (3) thin black outlines (`solid`/`dashed`) & dashed radii/vectors, (4) ALL text/math labels last.
   - Render high-res (`210 dpi`) tight-crop PNG zoom sheets of **every** new or edited figure and inspect them visually for overlaps, clipping, or clutter before committing.

4. **CS 61A & STAT 20 Code Breakdowns & Interactive Website (`cs61a.org` / `stat20.berkeley.edu` Standard)**
   - **Piece-by-piece code breakdowns everywhere**: both `handout.tex` (via structured breakdown tables) and `exercises.html` (via `<section class="code-guide">` + `<table class="code-anatomy">`) must break down every recurring SQL clause (`SELECT`, `FROM`, `JOIN ... ON`, self-join aliases, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `LIMIT`) and every R verb/pipeline (`dplyr`, `infer` `specify`/`hypothesize`/`generate`/`calculate`/`get_p_value`/`get_ci`, `lm`, `glm(..., family = "binomial")`, `predict(..., type = "response")`, `ifelse`), explaining every argument, input/output table shape, execution order, and common pitfall.
   - **Widened readable layout**: keep root/course index containers at `max-width: 56rem` (`10px 16px` table cell padding) and `assets/exercises.css` at `max-width: 60rem` with `68ch` prose measure and `line-height: 1.65`.
   - **Flat scrollable UI**: use a `.toc-bar` index at the top and plain `<section>` flow for every task, code guide, case study, and SQL table schema. Never hide tasks or schemas inside collapsible dropdowns (`<details>`).
   - **Syntax highlighting & Light/Dark theme sync**: enable CodeMirror 5 (`mode/r`, `mode/sql`) for editors and `highlight.js` for static code blocks, and load `assets/exercises.css` **LAST** among `<link rel="stylesheet">` tags in `<head>` so `@media (prefers-color-scheme: dark)` matches `index.html` cleanly in both light and dark modes.
   - **High-standard content**: frame STAT 20 exercises as contextualized Berkeley-style data-science / causal / prediction / inference case studies with visible schemas and tidy-R/WebR compatibility. Frame CS 61A SQL/Python tasks with visible schemas and course-faithful prompts (respecting CS 61A's no-graded-solutions rule in [`standards/handout-standard.md`](standards/handout-standard.md) Section 5b).
   - Verify live in a headless browser (executing WebR/SQLite cells with 0 JS/R/SQL errors).

5. **Build & Git Hygiene**
   - When running `pdflatex` inside a handout directory, always put `.` first in `TEXINPUTS`:
     `TEXINPUTS=".;<repo-root>/templates;"` (PowerShell: `$env:TEXINPUTS = ".;$repoRoot\templates;"`) so `templates/handout.tex` never shadows `./handout.tex`.
   - Never leave `.aux`, `.log`, `.out`, `.toc`, scratch PNGs, or temporary directories tracked or committed in the repository.
   - Update `semesters/<term>/<course>/log.md` as required, keep `audit.md` out of student PDFs, verify all built PDFs and exercises, then commit cleanly per packet.
