---
name: berkeley-latex
description: Author and visually audit UC Berkeley math, statistics, and CS LaTeX handouts and Michael Spivak (Calculus on Manifolds) artistic minimalist TikZ, tikz-cd, pgfplots figures matching templates/handout.sty.
---

# Berkeley LaTeX & Spivak Monograph Figure Standard

Follow this guide whenever authoring or fixing `.tex` handouts, diagrams, plots, or code breakdown tables in `semesters/`.

## 1. Reproducible spot-color ink figures

Use the approved deterministic style for all course handout figures. Load
`figure-ink` and follow [the reusable examples and build instructions](../../../samples/ink-figures/README.md).
The three initial pilot packets are worked references, not a scope restriction.

- Construct and verify mathematical relationships before styling: intersections,
  projections, vector endpoints, eigenvectors, probabilities, or combinatorial counts.
  Do not use image generation for mathematical geometry.
- Use native TikZ, tikz-cd, PGFPlots, and LaTeX tables/matrices. Apply fixed vector
  grain to meaningful filled regions and `\InkStroke` to suitable solid paths. Curves
  must follow their equations; grain must not imply a nonexistent region or subspace.
- Use `inkblue`, `inkred`, `inkgreen`, `inkamber`, and `inkslate` (the matching
  `fig*` colors are also available). Assign colors by mathematical role.
- Use exact `ink line`/`ink arrow` styles for tiny circles and sampled plot paths;
  the random-step fringe can exceed PGF arithmetic limits on those paths. Keep
  labels separate from `\InkStroke` paths, since that macro draws the path twice.
- **Guide/reference lines must be actual circular dots (`ink guide` / `ink guide arrow`)**:
  never use `dashed`, `densely dashed`, or `densely dotted` dashes, and never wrap
  `ink guide` inside `\InkStroke` or `\PacketInkPath` (their random-step preaction
  smears a fuzzy line behind dots). Draw dotted guides directly with
  `\draw[ink guide, draw=...]` or `\draw[ink guide arrow, draw=...]`.
- **Place curve/vector labels directly near their target using `\InkLabel{$...$}`**:
  use the 0.65pt white glyph halo for crisp overlap instead of drawing leader/pointer
  tick lines from distant labels.
- Keep slender ink strokes and narrow filled dart arrowheads. The exact core
  path and endpoints take precedence over texture. Label finite patches as
  portions of unbounded planes where appropriate.
- Use `\InkLabel{$...$}` for a tight white glyph outline, not a white rectangle.
  For a multicolor matrix, halo each colored entry with `\InkLabel[color]{$...$}`;
  nested text colors inside a halo defeat its white outline. Keep text and matrices in native Computer Modern.
- Draw regions first, then construction lines and outlines, then labels.
  `\InkRegion` has an opaque white base: use a transparent `ink grain` path
  explicitly when drawing overlapping transparent planes.
- **Crisp, direct `\figcap` prose**: write 1--2 clear sentences stating directly
  what the figure shows (plus color/dot key where needed). Do not restate theorem
  proofs or use mannered `"X, not Y"`, `"rather than"`, or `"Schematic: ..."` phrasing. Use only the labels needed to identify objects inside a diagram.

## 2. Semantic Geometry & Line Textures
- **Consistent solid lines for symmetric peers**: never assign different dash/dot patterns to symmetric peer curves, planes, or unit balls. Reserve `ink guide` (circular dots) strictly for reference lines ($y=0$, sum $=1$), orthogonal complements, drop/projection guides, residuals, or hidden back edges.
- **Nested Euler diagrams for subset inclusion**: draw concentric nested rounded containers (with concrete examples in each region) when illustrating set or class containment; do not use disconnected arrow-box stacks for subset inclusion.
- **Ban circle/oval set-blob diagrams**: reserve circles/ellipses strictly for true geometric conic sections (unit circles, SVD/symmetric image ellipses, level sets, Gershgorin disks).

## 3. Commutative Diagrams (`tikz-cd`) & Matrices
- Use `\begin{tikzcd}...\end{tikzcd}` with plain math nodes, thin arrows, generous `column sep`, and `"{...}"` around any arrow label with a comma `,`.
- Put genuine `\begin{pmatrix}...\end{pmatrix}` / `\begin{bmatrix}...\end{bmatrix}` inside display math (`\begin{minipage}{Xcm}\[...\]\end{minipage}` inside a TikZ `\node`).

## 4. `pgfplots` & `tabularx` Conventions
- Always include `bar shift=0pt` on multi-series `ybar` plots.
- **Never rotate y-axis labels (`ylabel`)**: always keep `ylabel` horizontal with `ylabel style={rotate=-90}` for short math symbols (`$y$`, `$s_j$`, `$R^2$`), and `ylabel style={rotate=-90, at={(axis description cs:0,1.03)}, anchor=south west}` flush above the y-axis for multi-word or equation labels (`Probability`, `Density`, `Stack count`, `Residual ...`).
- Prefer `axis lines*=left` with a subtle dotted `ink guide` $y=0$ reference line when curves cross zero, and borderless legends (`draw=none,fill=none`).
- For `tabularx` code breakdown tables, use `>{\raggedright\arraybackslash}X` on the explanation column, flush `\cmidrule{1-3}` dividers, and execution order.

## 5. Build, Verification & 240 DPI Inspection
1. **TEXINPUTS**: Always compile with `.` first:
   - PowerShell: `$env:TEXINPUTS = ".;$repoRoot\templates;"`
2. Inspect EVERY new or modified figure at **240 DPI** before committing.
3. Delete `.aux`, `.log`, `.out`, `.toc`, and temporary PNGs inside `semesters/` before committing.

## 6. Teaching structure

An Idea box should explain why the proof chooses a particular object or argument;
it should not reproduce the proof. Keep substantial computations and difficult
constructions. When several proofs are required, identify a principal proof, give
a worked application, and collect the remaining proofs as alternatives. Preserve
course coverage and references. Put permitted exercise hints in a separate keyed
section after the problems so the initial attempt does not reveal the method.
