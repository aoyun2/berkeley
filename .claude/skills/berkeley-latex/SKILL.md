---
name: berkeley-latex
description: Author and visually audit UC Berkeley math, statistics, and CS LaTeX handouts and textbook-grade TikZ, tikz-cd, and pgfplots figures matching templates/handout.sty. Use whenever creating, editing, or reviewing .tex handouts or figures.
---

# Berkeley LaTeX & Textbook Figure Standard

Follow this guide whenever authoring or fixing `.tex` handouts, commutative diagrams, matrix illustrations, geometric plots, or schematic diagrams in `semesters/`.

## 1. Visual Gold Standard
Match the typography, spacing, and restraint of `standards/reference/math110-quiz-minpoly-geneig.pdf` (`Nilpotent chain extension` and the `g_1, g_2, g_3` interpolation plot): pure white paper, crisp thin strokes, plain black mathematics, and visual breathing room.

## 2. Banned "Slop" Patterns (Never Emit)
- **Chunky pastel dashboard cards**: Never wrap commutative-diagram vertices, subspace pairs, or formula cases in `figbox` rounded-rectangle filled cards (`fill=figblue!8`, `fill=figpurple!8`, etc.).
- **Gray `figslate` side bullet walls**: Never park multi-line gray bullet lists inside TikZ figures. Put takeaways in `\figcap{...}` or a crisp 1--2 line normal-black legend (`\scriptsize`).
- **Label background pills**: Never use `fill=white`, `fill=figbg`, or halos behind text labels. Place labels cleanly in open whitespace. Always write `text=<color>` in TikZ node options so `<color>` does not overwrite font/anchor options.
- **Hand-drawn matrix brackets**: Never use `\draw` strokes to mimic matrix brackets around manually placed entries.
- **Opaque overlapping fills**: Never draw solid or opaque-looking disk fills after strokes/labels.
- **Confusing bare notation**: Avoid giant standalone shorthand such as bare `\bigcup` without context.

## 3. Commutative Diagrams (`tikz-cd`)
`\RequirePackage{tikz-cd}` is loaded in `templates/handout.sty`.
- Always draw commutative squares/triangles with `\begin{tikzcd}...\end{tikzcd}`, plain black math nodes, and thin arrows.
- **Comma trap**: Always wrap any arrow label containing a comma `,` in inner braces inside quotes:
  ```latex
  \arrow[r, "{\MM(T,B') = A^{-1}\MM(T,B)A}"]
  \arrow[r, "{T'\colon \varphi\mapsto \varphi\circ T}"']
  ```
  Without the inner `{...}`, `pgfkeys` splits on `,` and fails to compile.
- **Prevent label-on-corner collisions**: When an arrow label is wide, set generous separation (`[column sep=6.5em, row sep=3.4em]` up to `column sep=9.5em`) so the arrow label never touches adjacent corner nodes.

## 4. Matrices Inside Figures
- Always typeset matrices with genuine LaTeX `\begin{pmatrix}...\end{pmatrix}` or `\begin{bmatrix}...\end{bmatrix}`.
- Inside a TikZ `\node`, wrap display math in a minipage so `verify_handout.py` never flags an inline $3\times 3+$ matrix warning:
  ```latex
  \node[anchor=west] at (7.10,1.62) {%
    \begin{minipage}{5.2cm}\[
      \MM(T) = \begin{pmatrix}
        \lambda_1 & a_{12} & \cdots & a_{1n} \\
        0         & \lambda_2 & \cdots & a_{2n} \\
        \vdots    & \vdots    & \ddots & \vdots \\
        0         & 0         & \cdots & \lambda_n
      \end{pmatrix}
    \]\end{minipage}};
  ```
- Place $3\times 3$ or larger matrices in display math (`\[...\]`) or such minipage nodes, never inline `$...$`.

## 5. Strict 4-Layer Order for Overlapping Regions / Disks
Whenever disks, ellipses, or regions overlap (e.g., Gershgorin disks, SVD operator hierarchy):
1. **Layer 1 --- Translucent fills FIRST**: `\fill[figblue,fill opacity=0.07] ...;`
2. **Layer 2 --- Coordinate axes & origin**: `\draw[figaxis] ...;`
3. **Layer 3 --- Outlines & dashed radii/vectors**: point arrows/radii away from overlapping disks (e.g., `150` degrees for left disk $D_1$ away from right disk $D_2$).
4. **Layer 4 --- ALL text/math labels LAST**: ensures intersecting circles or fills never obscure labels, eigenvalues, or radius formulas.

## 6. Subspace & Grouping Diagrams
- Use thin outlines (`rounded corners=3pt`--`5pt`, solid or dashed `black!55` for complements/old chains, `fill=none` or at most a subtle single focal highlight `fill=figgreen!12, fill opacity=0.7`) in the style of the Nilpotent chain diagram.
- Leave comfortable inner margins around interior arrows and text so nothing kisses or crosses a border line.

## 7. `pgfplots` Conventions
- Prefer `axis lines*=left` with a dashed `y=0` reference line when curves cross zero (`\draw[dashed,black!40] (axis cs:xmin,0) -- (axis cs:xmax,0);`), and borderless transparent legends (`legend style={draw=none,fill=none}`).
- When using `axis lines=middle` (e.g., polar plots), ensure `ymin` / `ymax` leave room so callout labels never cross the axis arrow or line.

## 8. Build, Verification & Mandatory 210 dpi Visual QA
1. **TEXINPUTS**: Always compile with `.` first so `templates/handout.tex` cannot shadow `./handout.tex`:
   - PowerShell: `$env:TEXINPUTS = ".;$repoRoot\templates;"`
   - Bash: `TEXINPUTS=".;$repoRoot/templates;"`
2. **Anti-cutoff guards**: Preserve `\Needspace{14\baselineskip}` on theorem/prop/lemma/corollary environments and add explicit `\Needspace{14\baselineskip}`--`\Needspace{16\baselineskip}` before tall figures or coupled heading/box pairs.
3. **Verify & Inspect**: Run the handout verifier (`0` errors, `0` warnings), render EVERY new or modified figure at `210 dpi` tight-crop PNG, and inspect every rendered crop visually for overlapping labels, clipped math, or cramped arrows before committing.
4. **Hygiene**: Remove `.aux`, `.log`, `.out`, `.toc`, and temporary PNGs before staging commits.
