# Repository instructions

Read [the course standard](standards/course-standard.md) before creating or revising course material. For handouts and figures, also follow [the handout standard](standards/handout-standard.md). For code exercises, follow [the programming-exercise standard](standards/programming-exercise-standard.md). These documents are the authoritative requirements; do not duplicate their detailed rules here.

## Required workflow

1. Establish the course, week, source material, learning objectives, prerequisites, and applicable assignment rules. Record missing evidence rather than inventing coverage.
2. Preserve required mathematical and programming detail. Remove repeated explanation, put reasons beside the steps they explain, and distinguish a main argument from optional alternatives.
3. Use the shared reproducible spot-color ink figures in `templates/figure-ink.sty` and [the LaTeX skill](.claude/skills/berkeley-latex/SKILL.md). Keep exact geometry, vector grain, ink strokes, and white glyph outlines. Inspect every changed figure at 240 DPI.
4. Validate content, tests, browser behavior, and downloadable files as applicable. Record commands, results, and untested behavior in the packet audit. Executing code without errors does not establish that an answer is correct.
5. Check the student-facing artifact for answer leakage and inspect the actual publication bundle. Apply the assignment restrictions in handout-standard section 5b; a hidden HTML element is still published content.
6. Build LaTeX twice with the current directory first in `TEXINPUTS`: PowerShell `$env:TEXINPUTS = ".;$repoRoot\templates;"`. Inspect pages and remove compilation scratch files.
7. Review the diff and commit only task files. Do not treat this document as authorization to push, deploy, or publish solutions; follow the user's requested scope.
