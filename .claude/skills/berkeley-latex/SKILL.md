---
name: berkeley-latex
description: Author and visually audit UC Berkeley math, statistics, and CS LaTeX handouts and 1980s monochrome textbook-grade TikZ, tikz-cd, and pgfplots figures matching templates/handout.sty. Use whenever creating, editing, or reviewing .tex handouts or figures.
---

# Berkeley LaTeX & 1980s Monochrome Textbook Figure Standard

Follow this guide whenever authoring or fixing `.tex` handouts, commutative diagrams, matrix illustrations, geometric plots, environment diagrams, or statistical plots in `semesters/`.

## 1. Visual Gold Standard: 1980s Mathematics Textbook & AMS Paper
Every figure across all courses must look like it came out of a classic **1980s mathematics textbook or journal paper** (Springer GTM, Halmos, Axler, Strang, Hoffman & Kunze, MIT Press *SICP* 1985, Knuth *TAOCP*, *JASA*):
- **Pure monochrome black-and-gray ink on white paper**: use only `black`, `black!75`, `black!55`, light gray tints (`black!4`--`black!14`), or diagonal hatching (`pattern=north east lines, pattern color=black!50`).
- **Zero colors inside figures**: never use `blue`, `red`, `green`, `orange`, `purple`, `OliveGreen`, or colored `fig*` tokens inside `\begin{fig}...\end{fig}` or mention colors (`"red line"`, `"green box"`, `"blue dots"`) in `\figcap{...}`.
- **Zero "toy block" rounded rectangles**: never use `rounded corners` on boxes, cards, or nested flags.

## 2. Geometry by Figure Type (No Toy Blocks)
- **Nested flags, abstract domain/codomain sets, & operator hierarchies**: use **smooth concentric or overlapping ellipses/ovals** (`\draw[draw=black,line width=0.6pt] (x,y) ellipse (a and b);`, solid vs `dashed`, with at most subtle `fill=black!4` on a focal inner oval). Ensure generous radii so text never touches an ellipse arc.
- **Strang four-subspace diagrams, matrix factorizations ($A=CR$, REF/RREF), & SICP environment frames**: use **sharp-cornered (`0pt` radius) thin black hairline rectangles** (`draw=black,line width=0.55pt` solid for row/column/range spaces, `draw=black!65,dashed,line width=0.55pt` for null spaces/orthogonal complements).
- **Multi-curve plots & vector diagrams**: distinguish curves, lines, and regions using **1980s print differentiation**:
  - Line styles: `solid` (`very thick` / `thick`), `dashed`, `densely dotted`, `dash dot`.
  - Point markers: filled dots (`mark=*`, `\fill[black] ... circle`), hollow open circles (`mark=o`, `\draw[fill=white,draw=black] ... circle`), and crosses (`\times`).
  - Shaded regions (e.g., Type I $\alpha$ vs Type II $\beta$ error): pair solid gray shading (`fill=black!35`) with diagonal line hatching (`pattern=north east lines,pattern color=black!55`).

## 3. Commutative Diagrams (`tikz-cd`)
`\RequirePackage{tikz-cd}` is loaded in `templates/handout.sty`.
- Always draw commutative squares/triangles with `\begin{tikzcd}...\end{tikzcd}`, plain black math nodes, and thin arrows.
- **Comma trap**: Always wrap any arrow label containing a comma `,` in inner braces inside quotes:
  ```latex
  \arrow[r, "{\MM(T,B') = A^{-1}\MM(T,B)A}"]
  \arrow[r, "{T'\colon \varphi\mapsto \varphi\circ T}"']
  ```
- **Prevent label-on-corner collisions**: When an arrow label is wide, set generous separation (`[column sep=6.5em, row sep=3.4em]` up to `column sep=9.5em`) so the arrow label never touches adjacent corner nodes.

## 4. Matrices Inside Figures
- Always typeset matrices with genuine LaTeX `\begin{pmatrix}...\end{pmatrix}` or `\begin{bmatrix}...\end{bmatrix}` in pure black ink.
- Inside a TikZ `\node`, wrap display math in a minipage so `verify_handout.py` never flags an inline $3\times 3+$ matrix warning:
  ```latex
  \node[anchor=west] at (6.95,1.65) {%
    \begin{minipage}{5.2cm}\[
      \MM(T) = \begin{pmatrix}
        \lambda_1 & a_{12} & \cdots & a_{1n} \\
        0         & \lambda_2 & \cdots & a_{2n} \\
        \vdots    & \vdots    & \ddots & \vdots \\
        0         & 0         & \cdots & \lambda_n
      \end{pmatrix}
    \]\end{minipage}};
  ```

## 5. Strict 4-Layer Order for Overlapping Disks / Regions
Whenever disks or regions overlap (e.g., Gershgorin disks):
1. **Layer 1 --- Faint monochrome fills FIRST**: `\fill[black,fill opacity=0.045] ...;`
2. **Layer 2 --- Coordinate axes & origin**: `\draw[figaxis] ...;`
3. **Layer 3 --- Thin black outlines (`solid` / `dashed`) & dashed radii/vectors**: point radii away from neighboring disks.
4. **Layer 4 --- ALL text/math labels LAST**: ensures intersecting circles never obscure labels or eigenvalues.

## 6. `pgfplots` Conventions
- Prefer `axis lines*=left` with a dashed `y=0` reference line when curves cross zero (`\draw[dashed,black!35] (axis cs:xmin,0) -- (axis cs:xmax,0);`), and borderless transparent legends (`legend style={draw=none,fill=none}`).
- When using `axis lines=middle` (e.g., polar plots), ensure `ymin` / `ymax` leave room so callout labels never cross the axis line.

## 7. Build, Verification & Mandatory 210 dpi Visual QA
1. **TEXINPUTS**: Always compile with `.` first so `templates/handout.tex` cannot shadow `./handout.tex`:
   - PowerShell: `$env:TEXINPUTS = ".;$repoRoot\templates;"`
   - Bash: `TEXINPUTS=".;$repoRoot/templates;"`
2. **Verify & Inspect**: Run the handout verifier (`0` errors, `0` warnings), scan for zero figure color tokens and zero `rounded corners`, render EVERY new or modified figure at `210 dpi` tight-crop PNG, and inspect every rendered crop visually before committing.
3. **Hygiene**: Remove `.aux`, `.log`, `.out`, `.toc`, and temporary PNGs before staging commits.
