# Section-topic lookup and edition limits

Retrieved 2026-11-06. This is a source inventory, not a handout or verification of textbook content coverage.

The official syllabus controls the required edition: **Lay–Nagle–Saff–Snider, Linear Algebra and Differential Equations, 2nd Custom Edition for UC Berkeley, ISBN 9780137114030**. The exact-ISBN Google Books record confirms the custom MATH 54 title and ISBN, but offers **no table of contents, preview, or browsable pages**. Its metadata lists Pearson (2021) and a shortened author list; it does not establish which editions of the component texts were used. Do not treat this metadata as proof of the component editions.

## Saved evidence

| Saved `.txt` and raw `.html` pair in `topic-sources/` | URL | What it establishes |
| --- | --- | --- |
| `custom-isbn-record` | https://books.google.com/books?vid=ISBN9780137114030 | Exact custom title and ISBN; no TOC/preview. |
| `lay-4e-toc-record` | https://books.google.com/books?vid=ISBN9780321385178 | Full numbered TOC in the book description, for David C. Lay, 4th ed., Addison-Wesley (2012). |
| `lay-5e-record` | https://books.google.com/books?vid=ISBN9780321982384 | Pearson (2016), 5th ed.; broad chapter sequence, without numbered section TOC. |
| `lay-6e-record` | https://books.google.com/books?vid=ISBN9780135851258 | Pearson (2021), 6th ed.; bibliographic and descriptive information, without numbered section TOC. The description itself discusses fifth-edition features, so it cannot certify sixth-edition section numbering. |
| `nagle-bvp-5e-record` | https://books.google.com/books?vid=ISBN9780321419217 | Nagle–Saff–Snider, 5th boundary-value edition, Pearson/Addison-Wesley (2008): ordered broad topic list but no usable numbered section TOC. |
| `nagle-bvp-6e-record` | https://books.google.com/books?vid=ISBN9780321747747 | Pearson Addison-Wesley (2012), 6th boundary-value edition; bibliographic metadata but no usable TOC. |
| `saff-author-bibliography` | https://my.vanderbilt.edu/edsaff/books/ | Author's bibliography confirms distinct standalone-DE and boundary-value editions and publication years. It provides no TOC. Its entries (23)/(24) appear to exchange the ISBNs relative to the Google Books/library records, so they are not used to prove ISBN-to-edition matching. |

The Google Books descriptions are bibliographic records containing publisher-style descriptions, not downloaded textbook pages. No exercise statement, theorem numbering or worked example is available from these records. The Lay TOC is authoritative for the **fourth edition**. Matching it to Berkeley's custom edition remains **provisional**. The later-edition chapter lists support the broad chapter sequence but do not prove section equivalence. The official syllabus itself warns that exercise numbering can differ across editions.

## Scheduled Lay sections: verified headings in the fourth-edition TOC

All 33 scheduled Lay section numbers occur in the retrieved fourth-edition TOC. These labels can guide source lookup and concept planning, subject to the custom-edition limitation above. They do not establish a complete list of definitions, theorems or examples for authoring.

| Lay section | Fourth-edition heading | Confidence for custom edition |
| --- | --- | --- |
| 1.1 | Systems of Linear Equations | Provisional; exact custom TOC missing. |
| 1.2 | Row Reduction and Echelon Forms | Provisional; exact custom TOC missing. |
| 1.3 | Vector Equations | Provisional; exact custom TOC missing. |
| 1.4 | The Matrix Equation Ax = b | Provisional; exact custom TOC missing. |
| 1.5 | Solution Sets of Linear Systems | Provisional; exact custom TOC missing. |
| 1.7 | Linear Independence | Provisional; exact custom TOC missing. |
| 1.8 | Introduction to Linear Transformations | Provisional; exact custom TOC missing. |
| 1.9 | The Matrix of a Linear Transformation | Provisional; exact custom TOC missing. |
| 2.1 | Matrix Operations | Provisional; exact custom TOC missing. |
| 2.2 | The Inverse of a Matrix | Provisional; exact custom TOC missing. |
| 2.3 | Characterizations of Invertible Matrices | Provisional; exact custom TOC missing. |
| 3.1 | Introduction to Determinants | Provisional; exact custom TOC missing. |
| 3.2 | Properties of Determinants | Provisional; exact custom TOC missing. |
| 3.3 | Cramer's Rule, Volume, and Linear Transformations | Provisional; exact custom TOC missing. |
| 4.1 | Vector Spaces and Subspaces | Provisional; exact custom TOC missing. |
| 4.2 | Null Spaces, Column Spaces, and Linear Transformations | Provisional; exact custom TOC missing. |
| 4.3 | Linearly Independent Sets; Bases | Provisional; exact custom TOC missing. |
| 4.4 | Coordinate Systems | Provisional; exact custom TOC missing. |
| 4.5 | The Dimension of a Vector Space | Provisional; exact custom TOC missing. |
| 4.6 | Rank | Provisional; exact custom TOC missing. |
| 5.1 | Eigenvectors and Eigenvalues | Provisional; exact custom TOC missing. |
| 5.2 | The Characteristic Equation | Provisional; exact custom TOC missing. |
| 5.3 | Diagonalization | Provisional; exact custom TOC missing. |
| 5.4 | Eigenvectors and Linear Transformations | Provisional; exact custom TOC missing. |
| 5.5 | Complex Eigenvalues | Provisional; exact custom TOC missing. |
| 6.1 | Inner Product, Length, and Orthogonality | Provisional; exact custom TOC missing. |
| 6.2 | Orthogonal Sets | Provisional; exact custom TOC missing. |
| 6.3 | Orthogonal Projections | Provisional; exact custom TOC missing. |
| 6.4 | The Gram-Schmidt Process | Provisional; exact custom TOC missing. |
| 6.5 | Least-Squares Problems | Provisional; exact custom TOC missing. |
| 6.7 | Inner Product Spaces | Provisional; exact custom TOC missing. |
| 7.1 | Diagonalization of Symmetric Matrices | Provisional; exact custom TOC missing. |
| 7.4 | The Singular Value Decomposition | Provisional; exact custom TOC missing. |

The complete machine-readable `section-topic-map.json` additionally preserves all 52 numbered Lay sections in Chapters 1–7 from this TOC, including unscheduled sections. Unscheduled sections are lookup references only and must not be added to weekly packets.

## Differential-equation topics still unresolved

No obtained publisher/author/library source gives the exact **numbered Nagle section titles** needed for this custom edition. The ordered publisher topic list mentions “Linear Second-Order Equations,” “Matrix Methods for Linear Systems,” and “Partial Differential Equations.” Their positions suggest Chapters 4, 9 and 10, but this description does not explicitly number the chapters; those associations are retained only as unverified search aids in the JSON.

Specific missing headings/content:

- Historical Nov 2 packet: **Nagle 4.2 and 4.3**, taught Nov 6. Both exact headings and their definition/result/example scope remain unverified.
- Future Nov 9 packet: **Nagle 4.3, 4.4 and 4.5**.
- Future Nov 16 packet: **Nagle 9.1, 9.4 and 9.5**.
- Future Nov 23 packet: **Nagle 9.6**.
- Future Nov 30 packet: **Nagle 10.3 and 10.4**.

These numbers are differential equations. Never substitute Lay 4.2–4.5, Lay 9.x, or a different author's numbered sections. The textbook or an exact custom-edition TOC plus the appropriate notes is still needed to certify topic coverage.

## Lookup attempts and limits

The exact custom-ISBN Google Books page is nonbrowsable. The Lay author domain currently presents a domain-sale page. Guessed Pearson catalog product IDs returned unrelated books despite HTTP 200; those responses were rejected and are not saved as MATH 54 evidence. Known old Pearson sample-chapter paths returned 404. The current public Pearson search page does not include server-rendered book results. Library of Congress TOC endpoints returned 403, and public search-engine results did not yield a usable textbook TOC. No authenticated source or access restriction was bypassed.

No exercise statements were inferred from any other edition, and no handout was produced during this lookup.
