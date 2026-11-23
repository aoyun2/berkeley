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
  grain to meaningful filled regions and `\InkStroke` to suitable paths. Curves
  must follow their equations; grain must not imply a nonexistent region or subspace.
- Use `inkblue`, `inkred`, `inkgreen`, `inkamber`, and `inkslate` (the matching
  `fig*` colors are also available). Assign colors by mathematical role.
- Use exact `ink line`/`ink arrow` styles for tiny circles and sampled plot paths;
  the random-step fringe can exceed PGF arithmetic limits on those paths. Keep
  labels separate from `\InkStroke` paths, since that macro draws the path twice.
- Keep slender ink strokes and narrow filled dart arrowheads. The exact core
  path and endpoints take precedence over texture. Label finite patches as
  portions of unbounded planes where appropriate.
- Use `\InkLabel{$...$}` for a tight white glyph outline, not a white rectangle.
  For a multicolor matrix, halo each colored entry with `\InkLabel[color]{$...$}`;
  nested text colors inside a halo defeat its white outline. Put labels in empty
  space whenever possible. Keep text and matrices in native Computer Modern.
- Draw regions first, then construction lines and outlines, then labels.
  `\InkRegion` has an opaque white base: use a transparent `ink grain` path
  explicitly when drawing overlapping transparent planes, and explain that convention.
- Keep explanatory sentences in the caption. Use only the labels needed to
  identify objects and operations inside a diagram. No decorative blobs or cards.

## 2. Semantic Geometry & Line Textures
- **Consistent solid lines for symmetric peers**: never assign different dash patterns (`solid` / `dashed` / `dash dot`) to symmetric peer curves, planes, or unit balls. Reserve `dashed` / `dotted` strictly for reference lines ($y=0$, sum $=1$), orthogonal complements, drop/projection guides, residuals, or hidden back edges.
- **Ban circle/oval set-blob diagrams**: reserve circles/ellipses strictly for true geometric conic sections (unit circles, SVD/symmetric image ellipses, level sets, Gershgorin disks).

## 3. Commutative Diagrams (`tikz-cd`) & Matrices
- Use `\begin{tikzcd}...\end{tikzcd}` with plain math nodes, thin arrows, generous `column sep`, and `"{...}"` around any arrow label with a comma `,`.
- Put genuine `\begin{pmatrix}...\end{pmatrix}` / `\begin{bmatrix}...\end{bmatrix}` inside display math (`\begin{minipage}{Xcm}\[...\]\end{minipage}` inside a TikZ `\node`).

## 4. `pgfplots` & `tabularx` Conventions
- Always include `bar shift=0pt` on multi-series `ybar` plots.
- Prefer `axis lines*=left` with a subtle dashed `y=0` reference line when curves cross zero, and borderless legends (`draw=none,fill=none`).
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
