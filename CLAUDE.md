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

3. **Spivak Monograph Figures (`TikZ` / `tikz-cd` / `pgfplots`) — Follow [`.claude/skills/berkeley-latex/SKILL.md`](.claude/skills/berkeley-latex/SKILL.md)**
   - Every figure across all 4 courses must follow the calm, tasteful, artistic minimalism of **Michael Spivak (*Calculus on Manifolds*)**: **pure black ink + soft neutral gray washes (`fill=black!8`–`black!18`) on white paper**, with crisp typographic hierarchy (`0.35pt`–`0.45pt` construction/axes, borderless gray washes for regions, bold `1.0pt`–`1.4pt` black for the focal object, sleek `Stealth[length=4.0pt,width=2.3pt]` tips) and **zero `rounded corners` toy blocks** or **circle/oval set-blob diagrams**.
   - **Restrained color & white-interior boxes**: never build 4–5 color rainbows or pastel-filled UI cards. Allow at most **1 restrained accent color** (`figblue` or `figred`, and `figgreen` ONLY when 3 symmetric peer curves intersect on the same axes) where contrast genuinely clarifies the math, and keep symmetric peer curves uniform **solid** lines.
   - **Extreme label economy (atomic symbols only)**: delete verbose internal banners, bold titles inside diagrams, cartoon callouts, swoopy decorative arrows, and multi-line summary blocks inside TikZ. Use plain roman `(a)`, `(b)` centered beneath multi-panel figures, pure course-only terminology, and put all prose explanations in `\figcap`.
   - **Zero stroke-vs-glyph collisions & `bar shift=0pt`**: keep labels cleanly in open space (`halo` only when crossing an unavoidable line), and include `bar shift=0pt` on every multi-series `ybar` plot.
   - **Commutative diagrams (`tikz-cd`) & Genuine LaTeX matrices**: use `\begin{tikzcd}...\end{tikzcd}` with generous `column sep` and `"{...}"` around comma labels; wrap $3\times 3+$ matrices inside `\begin{minipage}{Xcm}\[...\]\end{minipage}` in a TikZ `\node`.
   - Render high-res (`220 dpi`) PNGs of **every** new or edited figure and inspect via `read_file` before committing.

4. **CS 61A & STAT 20 Code Breakdowns & Interactive Website (`cs61a.org` / `stat20.berkeley.edu` Standard)**
   - **Piece-by-piece code breakdowns everywhere**: both `handout.tex` (via structured `tabularx` breakdown tables using `>{\raggedright\arraybackslash}X` on the description column, `\cmidrule(lr){1-3}` dividers between rows, and numbered execution order) and `exercises.html` (via `<section class="code-guide">` + `<table class="code-anatomy">`) must break down every recurring SQL clause (`SELECT`, `FROM`, `JOIN ... ON`, self-join aliases, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `LIMIT`) and every R verb/pipeline (`dplyr`, `infer` `specify`/`hypothesize`/`generate`/`calculate`/`get_p_value`/`get_ci`, `lm`, `glm(..., family = "binomial")`, `predict(..., type = "response")`, `ifelse`), explaining every argument, input/output table shape, execution order, and common pitfall.
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
