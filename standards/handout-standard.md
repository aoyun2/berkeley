# Handout standard

Every handout, review packet and solutions file, in every course, follows this document. It replaces all earlier versions and notes.

**Purpose.** Aaron uses a handout to understand the ideas well enough to rebuild every result from memory, and to solve exam problems quickly. A rule below exists only to serve that. A longer handout is not a better one.

**Reference.** `standards/reference/math110-quiz-minpoly-geneig.pdf` is the model for page layout, figures, worked computations, Shortcuts and Traps. Do **not** copy its Want / Know / Key step labels; explain ideas as described under "Explaining where an idea comes from".

## 1. Scope
- **One handout per week**: only that week's lectures and that week's homework. Cumulative material only in exam reviews.
- **Complete coverage.** Every definition, result and example in the course notes for those lectures (by number), plus the textbook results in the matching sections, standard counterexamples, and every method for the standard computations. Keep the coverage checklist in `audit.md` next to the handout, not in the handout.
- **Real problems first.** Extra practice comes from real past exams and the course's practice exams; invent problems only to fill a gap.

## 2. Organization
- Each section opens with **"The question."**: a concrete task with a small example. Good: "For A = [[2,1],[1,2]], A² = 4A − 3I. Can every power of A be written as a combination of I and A?" Bad: "Which polynomial relations contain all relations?"
- **Group results by the argument that proves them.** Explain and prove each central argument once. Results that follow from it come right after, each with a short explicit derivation and no repeated motivation.
- **State useful criteria explicitly**, even when they are hidden inside a theorem. Example: for subspaces U, W of V, any two of dim U + dim W = dim V, U ∩ W = {0}, U + W = V imply the third.
- **No forward references.** Never use a term, notation or result before the handout defines or proves it. A fact that needs later material goes in the later section. A cut-down handout must not point to a section that was cut. Earlier weeks may be used: name the fact and the week, and restate the part that is needed.
- Every claim is derivable from first principles: anything used is proved in the handout or listed (with its reason) from an earlier week. Deep results with outside machinery (e.g. the fundamental theorem of algebra) are marked as cited.

## 3. Explaining where an idea comes from
Write this as ordinary sentences, in whatever form makes the **choice** of argument understandable. There is no template to fill in. Common forms:
- **A small worked case** that shows the pattern, then one sentence saying how the general proof does the same thing.
- **The obvious first attempt**, exactly why it fails, and what change fixes it.
- **A picture** of the structure (a chain of vectors, a block matrix, a projection).

Rules:
- Say concretely why this subspace, polynomial, basis or index is chosen. Define the notation and display the key equation.
- Do not restate the goal, and do not paraphrase the proof that follows.
- Length matches difficulty. A routine check ("unwind the definition of subspace") needs one sentence or nothing; a real idea gets a paragraph or a worked example. If the idea is obvious, leave the box out.

- **Guide the discovery; leave no gap for the reader to fill.** For each step that is not a routine check, say what question the step answers, what could go wrong, and why it does not. If a reader would have to stop and ask "why is that true?" or "what is this saying?", the answer belongs in the text at that point. Order the explanation the way someone would find the proof: the question first, then the attempt, then the obstacle, then the fix.

Example of the required level of detail (independence in the Jordan chain construction). Not acceptable: "Extend the bottoms to a basis of null N; the new list is independent." Required: "The bottoms of the chains already lie in null N, and they span L = null N ∩ range N. We add vectors w_1, …, w_p so that bottoms plus the w's are a basis of null N. Why can a w_i not be a combination of chain vectors? Suppose a combination of the w's equals a combination of chain vectors. Apply N: the w's go to 0, so the chain part goes to 0, which forces it to be a combination of bottoms only (shown in step 3). Then the w's and the bottoms would be dependent, contradicting that together they are a basis of null N."

Bad (rejected): "*Want.* Decide whether the available eigenspaces provide a full basis. *Know.* Eigenvectors with distinct eigenvalues are independent. *Key step.* Group a relation by eigenvalue." This fills in labels and explains nothing.

Good: "One vector is easy: v, Tv, …, Tⁿv are n + 1 vectors in an n-dimensional space, so q(T)v = 0 for some q of degree ≤ n. The problem is that q(T) may not be 0 on other vectors. So collect every vector q(T) sends to 0 into U = null q(T). A polynomial p that is 0 for the quotient T/U sends every vector into U, and a polynomial r that is 0 on U then sends it to 0. So r(T)p(T) = 0, and its degree is at most dim U + dim V/U = n."

### Proof steps are full sentences
Every proof step states what is being assumed, what is being shown, and the reason, in complete sentences. No noun-phrase shorthand that the reader has to decode ("Existence is spanning", "Same argument", "the other inclusion is clear", "swap the roles"). When a proof has two directions, each direction opens with its assumption in bold ("Assume the list is a basis.") and labels each sub-goal ("The list spans V."). If a step repeats an earlier argument, write it out again.

## 4. Writing
- Complete sentences, ordinary words, literal statements. No metaphors ("kills", "dies", "survives", "machinery", "bridge", "shadow"). A shorthand is allowed only if defined once in plain words (e.g. "q kills T means q(T) = 0").
- Never hide an argument behind a name: not "by invariance", "by degree", "by an adapted basis", "repeat the argument". Say which subspace, degree or basis, and show the step.
- Show intermediate computations: the matrix, the multiplication, the equations solved.
- Say what an equation does **not** prove when that is a common mistake, with a counterexample.
- No irrelevant provenance ("whose analytic input was the extreme-value theorem"). Cite only what a step uses.
- Edge cases (V = {0}, empty lists) at most one line, and only if an exam could ask.
- Examples use small, clean numbers.
- No intro or overview paragraph, no "how to use this handout", no meta sections.

## 5. Page elements (all in `templates/handout.sty`)
- **Statement** in a theorem box, labelled with the notes number and textbook number.
- **The idea** (`ideabox`, free text) before the proof, when the proof has a real idea (Section 3).
- **Proof** as numbered steps (`steps`), one or two lines each, each citing what it uses. A proof with parts: give each part a name that says what it proves and one line saying how the parts connect; never bare "Lemma"/"Theorem" in running text.
- **Examples** in example boxes, with the computation shown.
- **Figures** (`fig`, TikZ/pgfplots): compact, placed next to the mathematics they illustrate, drawing the example used in the text, with a short caption saying what to see. Models: the interpolation plot, the vector chain, the null-space-dimension plot and the annotated block matrix in the reference. Add one wherever the reader would otherwise have to imagine a geometric or structural step.
- **Shortcuts** box per section: every time-saving trick, each with its reason, its conditions and a worked instance.
- **Traps** box per section: common wrong claims, each with a counterexample.
- **Problem set** at the end: the week's homework, each with a one-line hint naming the result it uses, then real exam problems.
- **Solutions** in a separate PDF: an *Idea.* line explaining the choice of argument, then numbered steps.
- **Layout.** Nothing split across pages (boxes are `nobreak`, headings stay with what follows, problems and solutions in `prob`). Avoid big blank gaps: split long material into several boxes instead of one huge one. Never shrink type to fit.

## 5a. Courses with programming (CS 61A, STAT 20, and later ones)
Theory and written problems are not enough. Every week's folder also has `exercises/`:
- **Programming exercises Aaron implements himself**: starter files with function signatures, docstrings and doctests (CS 61A: Python, in the style of the course's labs and homework; STAT 20: R or the course's language, on the course's kind of data), ordered from warm-up to exam level. No solutions in the starter files.
- **A test file** that checks his answers (`python3 -m doctest`, or a test script), and a separate `solutions/` folder.
- **Before every quiz and exam**: a timed set that mixes writing code by hand with code to run, covering each topic on that quiz.
- Run every solution and every test before committing.

## 6. Checks before sending
1. Verify every number and answer by computation (sympy; for code, run it).
2. Render every page and look at it: intact boxes, readable labels, no overfull lines, no large gaps.
3. One fresh review pass against the sources and this standard: (a) correctness and coverage, (b) teaching quality: quote each passage where a reader would have to fill a gap, and fix it.
4. Append to the course `log.md`; commit, `git pull --rebase`, push. One week per commit.
