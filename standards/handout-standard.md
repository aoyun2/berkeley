# Handout standard

For the restarted backfill, also follow [teaching-quality.md](teaching-quality.md) and Aaron's supplied reference PDF. His latest instruction is to follow that PDF directly, including its compact illustrative figures and concise explanations. Earlier audit approvals do not establish teaching quality; every previously generated packet needs revision and a new review.

Every handout, review packet and solutions file, in every course, follows this. Aaron set each rule after seeing what went wrong without it.

## Scope
- **One handout per week**, covering only that week's lectures and that week's homework. Cumulative material only in exam reviews.
- **Nothing that could come up on an exam is left out.** Every definition, proposition, theorem and example in the course notes for that week, by number, plus the textbook results in the matching sections. Cross-check the notes' numbering before finishing. Include standard examples, counterexamples and every computing method.
- **Real problems first.** Extra practice comes from real past exams and the course's practice exams when they exist; invent problems only to fill gaps.

## Writing
- No intro or overview paragraph, no "how to use this handout", no meta sections. Start with content.
- Plain, literal language. No metaphors or mannered phrasing ("kills", "dies", "shadow", "earns its keep"). If a shorthand helps, define it once in plain words.
- **No forward references.** Never use a term, notation or result before the handout defines or proves it (e.g. no "largest Jordan block" in the minimal polynomial section when Jordan form comes later). A fact that needs later material goes in the later section, where everything it uses is already defined. This also applies to a cut-down handout: anything referring to a section that was cut is removed or rewritten.
- Every claim derivable from first principles. Any fact used is proved in the handout or in a "Tools" list with its own reason. Deep results that need outside machinery (e.g. the fundamental theorem of algebra) are marked as cited.

## Every result
1. **Statement** in a theorem box, labelled with the notes number and textbook number.
2. **"Where the proof comes from"** box (`motive`), with labelled lines:
   - *Want.* what has to be shown, concretely.
   - *Know.* the facts available that are relevant.
   - *First try.* the obvious attempt and exactly why it fails (when there is one).
   - *Key step.* the idea that works, and why it is the natural thing to try given the above.
   - *Example.* a small case that shows the idea (when it helps).
   The point is how someone would come up with the proof, not a restatement of it.
3. **Proof as numbered steps**, one or two lines each, each citing what it uses.
- Results built from parts: give the parts descriptive names that say what they are ("Step B: if b^2 < 4c then dim null p(T) is even") and a *Plan* line saying how they connect. Never bare "Lemma"/"Theorem" inside running text.
- Never cram reasoning into one paragraph or into small or italic print. Any reason longer than a sentence becomes numbered steps.

## Each section
- Opens with a **"The question."** box: the problem the section solves, with a small example.
- **Shortcuts** box: every trick that saves time on an exam (ways to avoid computation, quick tests, formulas), each with a one-line reason.
- **Computing methods**: every method for each standard computation, each on a worked example. Verify every number with computer algebra (sympy).
- **Traps** box: common wrong claims, each with a counterexample.
- **Figures** wherever they show an idea well (TikZ/pgfplots): chains of vectors, plots, geometric pictures, block shapes of matrices. The caption says in plain words what to see.

## Layout
- LaTeX with `templates/evan.sty` and `templates/handout.sty` (all box styles are there). Start from `templates/handout.tex` and `templates/solutions.tex`. Build with `scripts/build.sh`.
- Nothing split across pages: boxes are `nobreak`, headings keep with what follows, problems and solutions go in `prob` environments.
- **Problem set** at the end: the week's homework problems, each with a one-line hint naming the result it uses, then extra exam-style problems.
- **Solutions** in a separate PDF: an *Idea.* line (the key step and why it is natural), then numbered steps.

## Checking before sending
1. Verify every numeric example and answer with sympy.
2. Render every page and look at it: no split boxes, no overfull lines, figures readable.
3. Independent audit by a separate agent that has not seen the work being produced: math errors, proof gaps, wrong cross-references, omissions against the notes, metaphorical wording. Fix everything it finds.
