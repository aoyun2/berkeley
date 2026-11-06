# Teaching quality for the regenerated backfill

Read alongside handout-standard.md. Aaron rejected the earlier backfill for opaque language, inadequate figures and vague explanations. Its old audit approvals do not approve it for use. Every existing handout and solutions file must be re-reviewed and revised or regenerated.

The positive reference is Aaron's supplied [quiz packet](reference/math110-quiz-minpoly-geneig.pdf). Read the PDF itself, including the worked computations and the figures on pages 5, 13 and 14. Match its concrete explanations and useful diagrams while retaining the existing rules against metaphors and forward references. The reference is a cumulative review; its later-topic content does not belong in an earlier weekly packet.

## What the explanation must do

Start a topic with an actual mathematical task and a small case. For example: “For this matrix, multiplying twice gives A² = 4A − 3I. Can every higher power be reduced to a combination of I and A?” Avoid questions such as “Which polynomial relations contain all relations?” Name the objects and state what the reader must find or prove.

The proof-motivation box must explain how to choose the argument, before presenting it. “Use the invariant kernel and its quotient” is insufficient. Explain the obstruction, the choice of U, and what the two operators do: “The relation q(T)v=0 may hold only on some vectors. Put all vectors satisfying it in U. A polynomial in the quotient maps every vector into U; a polynomial that is zero on U then maps each of those vectors to zero. Their product is therefore zero on the whole space.” Define the relevant notation first and write the equations beside the explanation. The reader must not have to reconstruct this reasoning from the proof that follows.

Do not compress a needed argument into a name such as “by an adapted basis,” “by coefficient comparison,” “by invariance,” “by degree,” or “repeat the argument.” Say which basis, coefficients, subspace or degree is involved and show the calculation or implication. A reference to a previous week must identify the fact and restate the part needed now.

Show the actual intermediate computations. For a matrix example, display the matrix and the multiplication or equations that determine the answer; for a proof, explain why the next object is chosen; for an algorithm, show the changing quantities at each step. A list of answers or a theorem followed by its paraphrase does not teach the method. Distinguish what an equation proves from what it does not prove, using an explicit counterexample when needed.

Figures must carry part of the explanation. Examples include an element-and-arrow function diagram for image/preimage, a picture showing why a union of two lines fails the subspace test, a vector chain labelled by the operator and the last nonzero vector, a plot of null-space dimensions with its stabilization explained, a decomposition diagram showing which map sends which set where, or an actual sampling distribution with its numerical quantities identified. Draw and annotate the example used in the text. A decorative arrow labelled with two abstract spaces is not sufficient. Add figures wherever the reader otherwise has to imagine a geometric or structural step; a figure count alone is not a quality test.

Use literal language and complete sentences. Do not use “kills,” “dies,” “survives,” “machinery,” “bridge,” “route,” “mode,” or “mass” as unexplained substitutes for the mathematical action. Define technical terms before use. Explain every shortcut with its reason, its conditions, and a worked instance. Solutions need an Idea line explaining the choice of argument, followed by explicit numbered steps, not just a compressed answer.

## Release review

Keep all source coverage, correctness checks and no-forward-reference requirements. Verify numerical examples and answers by computation, including actual code execution in CS 61A. Preserve accurate source identifiers and the distinction between published exercises and extra examples.

A fresh reviewer must read Aaron's reference packet, the sources, and the entire revised packet, with no authoring history inherited. The reviewer must separately judge (1) correctness and coverage, and (2) whether the explanations and figures actually teach the material at the reference's level. The review must quote specific weak passages, explain what reasoning they omit, and check the revised replacements. “All theorem numbers present,” “compiles,” and “no overfull boxes” are not teaching-quality approval.

Render and inspect every final page. Check the legibility of the smallest mathematical labels, the connection of each figure to its nearby explanation, sufficient space for readable matrices, and intact boxes, headings, problems and solutions. Avoid empty pages or large unexplained gaps caused by keeping too much content in a single unbreakable block; regroup the material instead of shrinking it into unreadable print.

Record revisions honestly in the course log. Mark a week regenerated only after both reviews and all final-page inspections pass. Commit, pull with rebase, and push one completed week at a time. The previously completed ten MATH 110 weeks are all awaiting this new review until individually revised. Preserve original materials and the Weak spots section. Do not create packets for weeks starting on or after November 9, 2026.

## Follow the supplied PDF directly

Aaron's latest correction is explicit: “i just need illustrative figures LIKE IN THE EXAMPLE PDF I SENT. LITERALLY JUST FOLLOW EVERYTHING IN THAT PDF”. This supersedes the earlier interpretation that called for staged full-page visual sequences and an interactive supplement.

Use the actual reference as the model for writing and presentation: short blue result boxes, concise green proof motivations, numbered proofs, concrete worked calculations, red example boxes, and grouped Shortcuts and Traps. Keep the relevant source identifiers and all assigned content. Match the reference's level of detail instead of expanding each point into repeated narration.

Figures are compact static illustrations placed beside the relevant mathematics, with ordinary mathematical labels, a few colours and a short caption stating the property or equation illustrated. The examples are the small interpolation plot on page 5, the single chain on page 13, the nullity plot on page 14, and the annotated block matrix on page 20. Size each picture to fit the surrounding text. The packet itself is the deliverable; omit the unrequested interactive supplement. A review must compare the result to the actual supplied PDF, not certify an invented interpretation of its style.
