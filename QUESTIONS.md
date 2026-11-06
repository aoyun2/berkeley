# Backfill status and questions

## Source access

- The requested MATH 54, CS 61A and STAT 20 course sites currently return proxy `403 Forbidden` before a page can be fetched. Required network domains have been saved in the environment configuration draft: `math.berkeley.edu`, `cs61a.org`, `stat20.berkeley.edu`, `composingprograms.com`, and `www.composingprograms.com`. Saving the draft does not apply the policy to this running environment; enable these domains in environment settings to unblock source collection. No schedules or exercise statements have been invented.
- MATH 54 needs `semesters/2026-fall/math54/materials/textbook.pdf` to reproduce the assigned exercise statements. Without it, the requested concept-only handouts still require the actual calendar and homework section/exercise lists.
- STAT 20's final date remains unconfirmed.

## Work in progress

- Removed the two obsolete MATH 110 packet directories requested by Aaron. Preserved all materials and the Weak spots section of the log.
- Corrected `scripts/build.sh` so an explicitly requested handout or solutions source takes precedence over a template with the same filename, and TeX failures propagate.
- Completed and pushed MATH 110 weeks 1–5 (2026-08-31 through 2026-09-28): paired handouts and solutions, exact computation checks, independent audits and all-page inspections. Week 6 is drafted and under review; weeks 7–10 remain in progress. Other courses remain blocked on source access.
- Added the two MATH 54 midterm dates supplied in the request; weekly schedules still need the inaccessible source pages.
