---
name: berkeley-latex
description: Author and visually audit UC Berkeley math, statistics, and CS LaTeX handouts and Michael Spivak (Calculus on Manifolds) artistic minimalist TikZ, tikz-cd, pgfplots figures matching templates/handout.sty.
---

# Berkeley LaTeX & Spivak Monograph Figure Standard

Follow this guide whenever authoring or fixing `.tex` handouts, diagrams, plots, or code breakdown tables in `semesters/`.

## Reproducible ink pilot (November 2026)

For the following packets only, the user's approved grain-and-ink pilot supersedes
this skill's monochrome/one-accent defaults:

- `math54/handouts/2026-08-24-linear-systems-row-reduction`
- `math110/handouts/2026-10-19-generalized-eigenvectors-jordan`
- `math110/handouts/2026-11-09-adjoints-spectral-theorem`

Paths are under `semesters/2026-fall/`. Load `figure-ink` and follow
[the reproducible examples and build instructions](../../../samples/ink-figures/README.md).
Use exact native TikZ/PGFPlots geometry, the fixed vector grain, and
`\InkLabel` glyph-shaped white halos. Do not regenerate geometric drawings
with image generation. For a multicolor matrix, halo each colored entry using
`\InkLabel[color]{$...$}`; nested text colors inside a halo defeat its white outline.
Check the mathematical relationships before drawing, then inspect the PDF at
240 DPI after two compilation passes. The user is reviewing this pilot before
any collection-wide conversion; do not expand its scope automatically.

## 1. Visual Gold Standard: Michael Spivak (*Calculus on Manifolds*, 1965)
Every figure across all courses must have the calm, understated, artistic monograph elegance of **Michael Spivak (*Calculus on Manifolds*)**:
- **Pure black ink + soft neutral gray washes (`fill=black!8`–`black!18`) on stark white paper** is the default visual language. Use **zero** 4–5 color rainbows and **zero** pastel-filled UI cards. Allow at most **1 restrained accent color** (`figblue` or `figred`, or `figgreen` ONLY when 3 symmetric peer curves intersect on the same axes) where contrast genuinely clarifies the math.
- **Pure white interiors on boxes and frames**: never use stacked pastel-filled cards with colored borders and bold colored headers; use crisp thin black outlines (`0.45pt`–`0.5pt`) on white, or Spivak's signature soft borderless/whisper-edged gray washes (`fill=black!8, draw=none`) for regions and planes.
- **Hierarchy via line weight & gray value**: hair-thin construction lines and axes (`0.35pt`–`0.45pt`), soft gray washes for regions, bold pure black (`1.0pt`–`1.4pt`) for the focal curve, boundary, or transformation image. Sleek arrowheads (`Stealth[length=4.0pt,width=2.3pt]`).
- **Extreme label economy (atomic symbols only)**: delete verbose internal banners, bold headers inside diagrams, cartoon callouts, swoopy decorative arrows, and multi-line summary blocks inside TikZ. Keep inside-figure labels to atomic math symbols ($v_1, Tv_1, U_1, U_2, \lambda_1, 0$) plus at most 1–2 short words where essential. Put plain roman `(a)`, `(b)` subtly beneath multi-panel figures, and let `\figcap` carry all prose explanations.
- **Course-only terminology & generous whitespace**: zero non-course jargon, zero `rounded corners` toy blocks, zero circle/oval set-blob diagrams, zero collisions.

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

## 5. Build, Verification & 220 DPI Inspection
1. **TEXINPUTS**: Always compile with `.` first:
   - PowerShell: `$env:TEXINPUTS = ".;$repoRoot\templates;"`
2. Inspect EVERY new or modified figure at **220 DPI** via `read_file` before committing.
3. Delete `.aux`, `.log`, `.out`, `.toc`, and temporary PNGs inside `semesters/` before committing.
