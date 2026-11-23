# Reproducible ink figure samples

This directory contains the initial review samples. The three pilot packets
listed below now use this package for all figures.
Load `figure-ink` from `templates/figure-ink.sty`. No image generator, API,
Python package, or external raster texture is needed to compile them.

## Scheduled Claude workflow

1. Specify the mathematical objects numerically before drawing. Compute vector
   sums, dot products, ranks, or intersections as appropriate. Do not infer
   geometry from an illustration.
2. Copy the relevant example from `samples.tex`. Use `\InkRegion[color]{closed
   TikZ path}` for grain and `\InkStroke[options]{TikZ path}` for outlines.
   Use `ink arrow` for vectors and `ink guide` for construction lines.
3. Draw all regions first, then strokes, then labels. Use native LaTeX labels
   in empty space, wrapped with `\InkLabel{$...$}` for a 0.65pt white glyph
   outline. For colored entries use `\InkLabel[inkblue]{$...$}` individually;
   do not put nested `\textcolor` inside the halo. State what a finite patch
   represents in the caption.
4. Run `build.ps1` in this directory. Inspect the compiled figure at 240 DPI.
   Fix collisions and overfull boxes before accepting a figure.
5. Preserve the shared texture and stroke settings. Change coordinates to
   express the mathematics; do not add arbitrary organic silhouettes.

## Fixed rendering parameters

The grain is a 12pt vector tile with 196 stratified, jittered dots, radii
0.105–0.160pt. Coordinates are stored directly in the package. The initial
construction used Python `random.Random(1965)`; builds never regenerate it.
Coverage is approximately 7.5%. The tile can repeat visibly at high magnification.

Each ink stroke has a precise 0.42pt core. Its 0.54pt fringe has 28% opacity,
0.045pt displacement and 0.65pt segments, with the seed reset per stroke.
Arrowheads remain exact, solid Stealth shapes, 4.6pt long and 2pt wide.
This is a subtle print texture, not a simulated hand sketch. Keep the same
TeX/PGF versions for identical rendering; PDF metadata may vary between builds.

## Mathematical checks for these samples

- In the ordered basis B=(v1,v2), M(T)=[[3,2],[0,2]]. With v1=(1,0)
  and v2=(1,1), Tv1=(3,0) and Tv2=(4,2). The ochre displacement is (2,0).
- For U=span((1,0)), v=(3,2) decomposes as p=(3,0) plus (0,2).
  Their dot product is zero.
- Jordan block sizes (3,2,2,1) give dim(null(N^k))=(0,4,7,8) for k=0,1,2,3.
  There are three blocks of size at least two and two of size exactly two.

## Pilot packets

All figure geometry is native TikZ, tikz-cd, or PGFPlots; no generated image
is used by these three packets. The glyph halos preserve the current text
color by default. The package is opt-in and does not restyle other handouts.

- Math 54: `2026-08-24-linear-systems-row-reduction` (3 figures).
- Math 110: `2026-10-19-generalized-eigenvectors-jordan` (5 figures).
- Math 110: `2026-11-09-adjoints-spectral-theorem` (4 figures).

In each packet directory, use the same two-pass build with the repository
`templates` directory on TEXINPUTS. These changes do not create or change
Claude's schedule; the shared source and instructions are available to its
existing scheduled workflow.
