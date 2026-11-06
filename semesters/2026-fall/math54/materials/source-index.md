# MATH 54 source inventory

Retrieved 2026-11-06. Original user material `request-schedule.txt` is preserved.

| Local source | Public source URL | Content |
| --- | --- | --- |
| `official/Syllabus54-FA26.txt` and `.html` | https://math.berkeley.edu/~kwohm/Syllabus54-FA26.html | Textbook/edition/ISBN; homework policy; midterm dates and 45-minute duration; both lecture sections' final times; general course topics. |
| `official/Calendar54-FA26.txt` and `.html` | https://math.berkeley.edu/~kwohm/Calendar54-FA26.html | Exact dated lecture sections Aug 26–Dec 4, holidays, ten quizzes, HW submission dates, two midterm dates; Dec 7–11 reading week. |
| `official/Homework54-FA26.txt` and `.html` | https://math.berkeley.edu/~kwohm/Homework54-FA26.html | Exact HW1–11 section/exercise lists and deadlines. HW12 and HW13 are not posted in the retrieved page. |
| `official/Math54-FA26.txt` and `.html` | https://math.berkeley.edu/~kwohm/Math54-FA26.html | Instructor/GSI information; bCourses link. No public lecture notes or practice exams linked. |
| `homework-inventory.json` | Derived from the saved official homework page | Machine-readable, verbatim section/exercise lists for all posted assignments, independent of the lecture-week allocation. |
| `lecture-week-inventory.json` | Derived from the saved official calendar and homework pages | Every lecture week with dated section coverage, matching assignment subsets and each assignment's unchanged deadline. |

The `.txt` versions omit styling/scripts and retain visible content. Raw HTML is retained to verify extraction and table structure. These are publicly available sources, without authenticated bCourses content.

## Week and homework allocation

The schedule has 15 Monday-based lecture weeks Aug 24–Nov 30, not 13 submission weeks. The eleven backfill weeks are **Aug 24, Aug 31, Sep 7, Sep 14, Sep 21, Sep 28, Oct 5, Oct 12, Oct 19, Oct 26 and Nov 2**. The remaining four are scheduled future work. Dec 7–11 is a reading week with no new lecture sections or homework, so it has no packet entry.

`course.toml` maps each posted homework section to the week(s) in which the calendar actually teaches that section. Different assignments may appear in the same week, with their distinct original due dates. The `due` field is the earliest of those deadlines; `homework_due` and the assignment labels retain all deadlines. Homework is due at 23:59 Pacific Time, as stated in the homework page. The 24-hour grace policy is not treated as the deadline.

| Week start | Assignment sections from that week's lectures |
| --- | --- |
| 2026-08-24 | HW1 Lay 1.1–1.2 |
| 2026-08-31 | HW1 Lay 1.3–1.4; HW2 Lay 1.5, 1.7 |
| 2026-09-07 | HW2 Lay 1.7–1.9; HW3 Lay 1.8 |
| 2026-09-14 | HW3 Lay 2.1–2.3; HW4 Lay 3.1–3.2 |
| 2026-09-21 | HW4 Lay 3.2–3.3, 4.1; HW5 Lay 4.2 |
| 2026-09-28 | HW5 Lay 4.3; HW6 Lay 4.5 |
| 2026-10-05 | HW6 Lay 4.4, 4.6; HW7 Lay 5.1–5.2 |
| 2026-10-12 | HW7 Lay 5.3–5.4; HW8 Lay 5.5 |
| 2026-10-19 | HW8 Lay 6.1–6.3; HW9 Lay 6.4 |
| 2026-10-26 | HW9 Lay 6.4–6.5; HW10 Lay 6.7 |
| 2026-11-02 | HW10 Lay 7.1, 7.4 and Nagle 4.2; HW11 Nagle 4.3 |
| 2026-11-09 | HW11 Nagle 4.3–4.4. Nagle 4.5 is lectured Nov 13, but no posted assignment names it. HW11 also assigns Chapter 6 supplementary review, recorded here with its submission assignment and explicitly without a claimed lecture-week allocation. |
| 2026-11-16 | Lectures Nagle 9.1, 9.4, 9.5; HW12 due Nov 23, but assigned sections/exercises are unpublished. |
| 2026-11-23 | Lecture Nagle 9.6; HW13 due Dec 4, but assigned sections/exercises and division between Nov 23 and Nov 30 are unpublished. |
| 2026-11-30 | Lectures Nagle 10.3–10.4; HW13 due Dec 4, with the same unpublished mapping. |

Lay 1.7, 3.2 and 6.4, and Nagle 4.3 each span two calendar weeks. The complete assigned section list is preserved in each relevant week, with an overlap note. This does **not** claim every exercise uses only the first part of the section: without the textbook, no exercise-level partition can be justified. Authors must preserve that limitation and must not introduce later concepts into an earlier packet.

## Availability and unresolved items

- `textbook.pdf` is absent. The official syllabus specifies *Linear Algebra and Differential Equations*, Lay–Nagle–Saff–Snider, Pearson Learning Solutions, **2nd Custom Edition for UC Berkeley**, ISBN 978-0-137-11403-0. Matching exercises from another edition cannot be assumed. Do not invent exercise statements or solutions. The user explicitly permits concept-only packets plus the exact assigned section/exercise lists until the textbook is supplied.
- Chapters 1–7 in the linear algebra portion are Lay. Sections 4.2–4.5, 9.1, 9.4–9.6 and 10.3–10.4 from Nov 6 onward are **Nagle–Saff–Snider differential equations**, not identically numbered Lay sections. This distinction comes from the user's original request and the homework page's explicit “Differential Eq.” labels.
- The calendar supplies section numbers, but no section titles, theorem/definition numbering, worked lecture examples or lecture-note files. Consequently, the schedule's topics retain those exact numerical identifiers rather than claiming unavailable lecture detail. Full note-level coverage and textbook result numbering cannot yet be certified.
- The syllabus promises practice problems and a practice test about ten days before each exam. None of the four public pages links those files. No notes/practice exams have been downloaded or used; authenticated bCourses materials were not available in this collection.
- HW12 and HW13 section/exercise lists are not published in the saved homework page. Their due dates, Nov 23 and Dec 4, agree between the user and calendar. They are retained without inventing assignment content or its lecture-week split.
- HW11 Chapter 6 Supplementary Exercises (pages 414–415), 6, 8, 13, 14, 16, 19, 23, 24, are an assigned review set not individually mapped to a dated lecture by the public sources. They remain in the full inventory and are labelled review in the Nov 9 assignment record; this does not authorize a cumulative weekly concept section.
- Midterm coverage is not stated in these public pages. Both midterm dates agree with the user (Sep 30 and Nov 4), and the syllabus specifies 45 minutes during lecture. Nov 4's 08:00 start is from the user's screenshot; no explicit end time is inferred.
- The final is Dec 14, **19:00–22:00 for LEC001 (08:00 lectures)** and 08:00–11:00 for LEC002 (10:00 lectures). The user's 19:00–22:00 final and 08:00 lecture screenshot agree with LEC001. No date contradiction was found.
- Quizzes are usually Wednesdays, but **Quiz 8 is Friday Nov 13** because Nov 11 is a holiday. Other quiz dates: Sep 9, Sep 16, Sep 23, Oct 7, Oct 14, Oct 21, Oct 28, Nov 18 and Dec 2.

The parent author should record the missing textbook, lecture-note/practice-exam access, unpublished assignments and exercise-level overlap limitations in root `QUESTIONS.md`. No handout has been built during source collection.

## Additional section-topic lookup

`section-topic-map.md` and `.json` document a later bibliographic lookup, with seven saved source records in `topic-sources/` (each text plus raw HTML). A Google Books description supplies the complete numbered Lay **fourth-edition** TOC, including all 33 scheduled Lay section numbers. Its labels are verified for that source edition and provisional for the Berkeley custom second edition; custom-edition equivalence and exercise equivalence are not established. The exact custom-ISBN record offers no TOC or preview. Exact Nagle section headings remain unavailable, specifically Nagle 4.2 and 4.3 in the historical Nov 2 week and all listed future Nagle sections. Read the edition/confidence notes before using this lookup to plan concept coverage.
