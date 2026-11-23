---
name: berkeley-latex
description: Author and visually audit UC Berkeley math, statistics, and CS LaTeX handouts and textbook-grade TikZ, tikz-cd, pgfplots figures, and tabularx code breakdown tables matching templates/handout.sty. Use whenever creating, editing, or reviewing .tex handouts or figures.
---

# Berkeley LaTeX & Textbook Figure Standard

Follow this guide whenever authoring or fixing `.tex` handouts, commutative diagrams, matrix illustrations, geometric plots, environment diagrams, statistical plots, or code breakdown tables in `semesters/`.

## 1. Visual Gold Standard: Classic Mathematics Textbook & Functional Ink Palette
Every figure across all courses must look like a classic mathematics textbook (Springer GTM, Halmos, Axler, Strang, *SICP*, *JASA*):
- **Zero "toy block" rounded rectangles**: never use `rounded corners` on boxes, cards, or frames inside `\begin{fig}...\end{fig}`.
- **Functional, information-organizing color only (`templates/handout.sty`)**: use the muted textbook ink palette (`figblue` `#1B4F8A`, `figred` `#A82820`, `figgreen` `#1E6B40`, `figamber` `#A66314`, `figpurple` `#643882`, `figslate` `#525C68`) **only when color organizes distinct mathematical layers**:
  - Multi-curve or multi-vector plots (e.g., `figblue` for primary subspace / projection / row & column spaces, `figred` for orthogonal complement / nullspace / residual error / critical rejection tail, `figgreen` for eigenvectors / secondary invariant subspace).
  - Always pair color with distinct line styles (`solid`, `dashed`, `densely dotted`, `dash dot`) and point markers (`•`, `o`, `×`) so the figure remains completely legible in grayscale print.
- **Zero stroke-vs-glyph collisions & `halo` white knockout**: place labels cleanly in open whitespace away from curves, axes, and borders. Whenever a label sits near a grid line, axis, or curve, apply the `halo` style (`halo/.style={fill=white, inner sep=1.3pt}` in `templates/handout.sty`, or `fill=figgreen!7, inner sep=1.2pt` inside a tinted plane) so a white outline prevents any stroke from crossing text glyphs.

## 2. Geometry by Figure Type (Ban Circle/Oval Set-Blob Diagrams)
- **NEVER draw concentric or overlapping oval/circle "blob" diagrams around text blocks**: curved ellipses collide with rectangular text blocks near their poles while wasting space on the sides. Instead:
  - **Operator class hierarchies** (e.g., $\mathcal{L}(V) \supset \text{Normal} \supset \text{Self-adjoint}, \text{Unitary} \supset \text{Positive}$): draw a **Hasse inclusion lattice** with sharp-cornered rectangular nodes, $2\times 2$ witness matrices, and upward inclusion arrows.
  - **Nested invariant flags** ($\{0\} \subset U_1 \subset U_2 \subset \dots \subset U_n = V$): draw a **true geometric flag** showing the 1D line $U_1 = \spn(v_1)$ (`figred`) lying inside the 2D slanted parallelogram plane $U_2 = \spn(v_1, v_2)$ (`figgreen`), color-matched to the columns of the upper-triangular matrix $\mathcal{M}(T)$.
  - **Domain/codomain decompositions & Strang Four Fundamental Subspaces**: use **sharp-cornered (`0pt` radius) thin hairline rectangles** (`draw=figblue, fill=figblue!6` for $\range T^* = \Row A$ and $\range T = \Col A$; `draw=figred!80!black, dashed, fill=figred!4` for $\nul T = \Nul A$ and $\nul T^* = \Nul A^{\mathsf T}$), showing $\range T^* \perp \nul T$ in $V$, $\range T \perp \nul T^*$ in $W$, the bijection $\range T^* \xrightarrow{\sim} \range T$, and nullspace collapse $\nul T \to \{0_W\}$.
  - **Reserve circles and ellipses strictly for true geometric conic sections**: unit circles $\|v\|=1$, SVD/symmetric image ellipses, quadratic-form level sets, and Gershgorin disks in $\CC$.

## 3. Commutative Diagrams (`tikz-cd`)
`\RequirePackage{tikz-cd}` is loaded in `templates/handout.sty`.
- Always draw commutative squares/triangles with `\begin{tikzcd}...\end{tikzcd}`, plain math nodes, and thin arrows.
- **Comma trap**: Always wrap any arrow label containing a comma `,` in inner braces inside quotes:
  ```latex
  \arrow[r, "{\MM(T,B') = A^{-1}\MM(T,B)A}"]
  \arrow[r, "{T'\colon \varphi\mapsto \varphi\circ T}"']
  ```
- **Prevent label-on-corner collisions**: When an arrow label is wide, set generous separation (`[column sep=6.5em, row sep=3.4em]` up to `column sep=9.5em`) so the arrow label never touches adjacent corner nodes.

## 4. Matrices Inside Figures
- Always typeset matrices with genuine LaTeX `\begin{pmatrix}...\end{pmatrix}` or `\begin{bmatrix}...\end{bmatrix}`. Never overlay guessed TikZ rectangles behind matrix entries; highlight pivot columns or nonzero rows directly with `\textcolor{figblue}{\mathbf{...}}`.
- Inside a TikZ `\node`, wrap display math in a minipage so `verify_handout.py` never flags an inline $3\times 3+$ matrix warning:
  ```latex
  \node[anchor=west] at (6.75,1.65) {%
    \begin{minipage}{5.4cm}\[
      \MM(T) = \begin{pmatrix}
        \textcolor{figred!90!black}{\lambda_1} & \textcolor{figgreen!90!black}{a_{12}} & \cdots & \textcolor{figblue!90!black}{a_{1n}} \\
        0         & \textcolor{figgreen!90!black}{\lambda_2} & \cdots & \textcolor{figblue!90!black}{a_{2n}} \\
        \vdots    & \vdots    & \ddots & \vdots \\
        0         & 0         & \cdots & \textcolor{figblue!90!black}{\lambda_n}
      \end{pmatrix}
    \]\end{minipage}};
  ```

## 5. Strict 4-Layer Order for Overlapping Disks / Regions
Whenever disks or regions overlap (e.g., Gershgorin disks):
1. **Layer 1 --- Faint fills FIRST**: `\fill[figblue,fill opacity=0.07] ...;`
2. **Layer 2 --- Coordinate axes & origin**: `\draw[figaxis] ...;`
3. **Layer 3 --- Thin outlines (`solid` / `dashed`) & dashed radii/vectors**: point radii away from neighboring disks.
4. **Layer 4 --- ALL text/math labels LAST** (with `halo` where needed): ensures intersecting curves never obscure labels or eigenvalues.

## 6. `pgfplots` & `tabularx` Conventions
- **Multi-series `ybar` histograms (`bar shift=0pt`)**: whenever a `ybar` axis has two `\addplot` calls (e.g., non-tail bars and highlighted tail bars), always include `bar shift=0pt` in the `axis` options so `pgfplots` does not shift series 1 left and series 2 right off their true tick marks.
- Prefer `axis lines*=left` with a dashed `y=0` reference line when curves cross zero (`\draw[dashed,black!35] (axis cs:xmin,0) -- (axis cs:xmax,0);`), and borderless transparent legends (`legend style={draw=none,fill=none}`).
- **`tabularx` code breakdown tables**: always use `>{\raggedright\arraybackslash}X` on the description column (never bare `X`, which stretches huge whitespace gaps around inline `\cd{...}` code), add `\cmidrule(lr){1-3}` dividers between rows, and number pipeline stages in execution order.

## 7. Build, Verification & Mandatory 210 dpi Visual QA
1. **TEXINPUTS**: Always compile with `.` first so `templates/handout.tex` cannot shadow `./handout.tex`:
   - PowerShell: `$env:TEXINPUTS = ".;$repoRoot\templates;"`
   - Bash: `TEXINPUTS=".;$repoRoot/templates;"`
2. **Verify & Inspect**: Run `python scripts/verify_handout.py --all --no-compile --no-render` (`0` errors, `0` warnings), run a PyMuPDF geometric stroke-vs-glyph collision check (`0` collisions), and render EVERY new or modified figure at `210 dpi` tight-crop PNG to inspect visually before committing.
3. **Hygiene**: Remove `.aux`, `.log`, `.out`, `.toc`, and temporary PNGs before staging commits.
