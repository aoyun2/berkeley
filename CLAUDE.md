# Repository Instructions for Claude

Read and follow [`standards/handout-standard.md`](standards/handout-standard.md) before creating or editing any weekly packet, handout, figure, solutions file, or coding exercise set.

## Non-Negotiable Quality Gate for Every Weekly Packet

1. **Direct Intuition & Clean Prose**
   - Lead with concrete intuition and motivation: state *why* a definition or construction works and *how* someone finds it.
   - Zero exclamation marks (`!`), zero contractions, zero banter, zero rhetorical `Why?` / `How?` filler prompts.
   - Never pack multi-sentence `(i)/(ii)` or `(1)/(2)` walls of text inside a paragraph; use proper LaTeX `itemize` / `enumerate` lists.

2. **Zero Page Cutoffs**
   - Keep `templates/handout.sty` `\Needspace` guards intact (`14\baselineskip` on theorem/prop/lemma/corollary environments).
   - Add `\Needspace{14\baselineskip}`–`\Needspace{16\baselineskip}` before tall figures, multi-line code listings, or coupled theorem/idea pairs so headings and short boxes are never stranded at a page bottom.

3. **Textbook-Grade Figures (`TikZ` / `pgfplots`)**
   - Use concrete, numerically verified examples where distinct points, eigenvectors, Gershgorin centers/disks, and eigenvalues have clear visual separation.
   - For `pgfplots` curves crossing zero, use bottom/left axes (`axis lines*=left`) with a dashed `y=0` line instead of `axis lines=middle`.
   - Protect labels overlapping lines/curves with opaque white/background pills (`fill=figbg` or `fill=white,inner sep=1.5pt`), and always write `text=<color>` (never bare `<color>` after `fill=white`).
   - Do **not** use `\usetikzlibrary{matrix}` (`handout.sty` does not load it); build annotated matrices with positioned TikZ `\node` entries. Put `3x3+` matrices in displays or TikZ node grids, never inline `$...$`.
   - Render high-res PNG crops / contact sheets of **every** new or edited figure and inspect them visually for overlaps, clipping, or unreadable clutter before committing.

4. **Interactive Coding Exercises (`STAT 20`, `CS 61A`, and future programming courses)**
   - **Flat scrollable layout**: use a `.toc-bar` index at the top and plain `<section>` flow for every task, case study, and SQL table schema. Never hide tasks or schemas inside collapsible dropdowns (`<details>`).
   - **Syntax highlighting & Light/Dark theme sync**: enable CodeMirror 5 (`mode/r`, `mode/sql`) for editors and `highlight.js` for static code blocks, and load `../../../../assets/exercises.css` **LAST** in `<head>` so `@media (prefers-color-scheme: dark)` matches `index.html` cleanly in both light and dark modes.
   - **High-standard STAT 20 / CS 61A content**: frame STAT 20 exercises as contextualized Berkeley-style data-science / prediction / inference case studies with visible dataset schemas, sample rows, and self-contained tidy-R / WebR compatibility. Frame CS 61A SQL/Python tasks with visible schemas and course-faithful prompts (respecting CS 61A's no-graded-solutions rule in `standards/handout-standard.md` Section 5b).
   - Verify live in a headless browser (executing WebR/SQLite cells with 0 JS/R/SQL errors in both light and dark modes).

5. **Build & Git Hygiene**
   - When running `pdflatex` inside a handout directory, always put `.` first in `TEXINPUTS`:
     `TEXINPUTS=".;<repo-root>/templates;"` (PowerShell: `$env:TEXINPUTS = ".;$repoRoot\templates;"`) so `templates/handout.tex` never shadows `./handout.tex`.
   - Never leave `.aux`, `.log`, `.out`, `.toc`, scratch PNGs, or temporary directories tracked or committed in the repository.
   - Update `semesters/<term>/<course>/log.md` as required, keep `audit.md` out of student PDFs, verify all built PDFs and exercises, then commit cleanly per packet.
