# Course standard

This document defines requirements shared by all courses. Use `handout-standard.md` for written instruction and figures, and `programming-exercise-standard.md` for executable practice. Course-specific requirements supplement these documents; record conflicts and resolve them using the user's instructions and the applicable course policy.

## Course and packet scope

Maintain a course profile with the term, official source locations, syllabus version, topic sequence, prerequisites, assessment formats, programming languages and permitted libraries where relevant, and assignment/AI/publication restrictions. Distinguish verified source requirements from author choices. Do not claim alignment with a course website from appearance alone.

Store this profile at `semesters/<term>/<course>/course-profile.md`. Include `publish_solutions: false` or `publish_solutions: true` with the authorization date and scope. An absent profile means publication permission is unverified; it does not establish that previously published material was unauthorized. Existing automation must check the profile before adding solution content. A prose setting alone does not filter a deployment bundle; validate the actual publishing process as well.

For each packet, record in `audit.md`:

- The week or review interval and source sections actually examined.
- Observable learning objectives: what the student should explain, derive, implement, debug, or interpret independently.
- A mapping from each required objective to instruction, a worked example where needed, and an independent practice opportunity. Identify omissions explicitly.
- Prerequisites and new terminology. Restate only the earlier facts needed for the task.
- Provenance and assignment status of practice problems, including whether a solution may be authored or published.
- Validation evidence and unresolved findings, with severity and concrete acceptance criteria.

Do not manufacture unavailable course notes or silently substitute generic material for the week's scope. Mark unavailable evidence and limit claims accordingly.

## Instruction and practice

Teach a difficult idea with a concrete example and an explanation of the relevant choices. Follow supported practice with at least one task that requires choosing the method independently. Use a timed mixed set when preparing for an assessment, with a stated time estimate and coverage rationale.

Preserve detail that supports understanding. Remove repeated narration rather than hypotheses or reasoning. Explain a concept fully at its first useful occurrence and refer precisely to it later. A code guide, Idea box, shortcut, or warning is optional when it would merely repeat nearby material. Do not fill a template for its own sake.

Separate exercise prompts from permitted hints and solutions. A task intended to assess method selection must not disclose that method in its title, starter comments, or immediately adjacent guide. Guided tasks may provide it, but must be identified as guided.

## Review and release

Review correctness, coverage, instructional sequence, independent practice, and usability separately. State which conclusions are supported by execution or source comparison and which are editorial judgments. Do not describe an untested runtime as verified or repeated agent approval as evidence of student learning.

Record commands, runtime versions, results, visual checks, and limitations. For a missing tool or source, record the blocked check and the exact remaining action. Critical correctness defects and misleading correctness feedback prevent a packet from being marked verified.

Inspect the files actually made public, including HTML source, JavaScript, ZIP members, PDFs, and repository-hosting rules. Follow handout-standard section 5b for course restrictions. `publish_solutions` defaults to false; an explicit recorded authorization is required to change it. Removing a link or collapsing a solution does not remove it from publication. Do not silently remove existing public content during an audit; report it and handle remediation within the user's scope.
