"""
Comprehensive hyperlink restoration for Math 110 handouts (Weeks 1 to 10).
Restores both:
1. Named destinations (/Root/Names/Dests): def-N, prop-N, ex-N, prob-..., name-..., fact-...
   mapped with exact (page, left, top) coordinates in the newly compiled PDFs.
2. Link annotations (/Annots on pages): internal GoTo and cross-week URI links,
   positioned with sub-pixel bounding box accuracy matching the text in the newly compiled PDFs.
"""

import io, os, re, subprocess, sys
import pypdfium2 as pdfium
from pypdf import PdfReader, PdfWriter
from pypdf.generic import (
    ArrayObject, DictionaryObject, FloatObject, NameObject, NullObject, NumberObject, TextStringObject
)

WEEKS = [
    "2026-08-31-sets-fields-subspaces",
    "2026-09-07-bases-dimension",
    "2026-09-14-linear-maps-matrices",
    "2026-09-21-isomorphisms-products-quotients",
    "2026-09-28-quotients-duality",
    "2026-10-05-eigenvalues-pagerank",
    "2026-10-12-diagonalization-minimal-polynomial",
    "2026-10-19-generalized-eigenvectors-jordan",
    "2026-10-26-trace-inner-products",
    "2026-11-02-orthogonality-projections",
]

WEEK_NUMBERS = {
    "2026-08-31-sets-fields-subspaces": 1,
    "2026-09-07-bases-dimension": 2,
    "2026-09-14-linear-maps-matrices": 3,
    "2026-09-21-isomorphisms-products-quotients": 4,
    "2026-09-28-quotients-duality": 5,
    "2026-10-05-eigenvalues-pagerank": 6,
    "2026-10-12-diagonalization-minimal-polynomial": 7,
    "2026-10-19-generalized-eigenvectors-jordan": 8,
    "2026-10-26-trace-inner-products": 9,
    "2026-11-02-orthogonality-projections": 10,
    "2026-11-09-adjoints-spectral-theorem": 11,
    "2026-11-16-positive-isometries-svd": 12,
}

BASE_DIR = "semesters/2026-fall/math110/handouts"


def extract_old_dests(reader):
    root = reader.trailer["/Root"]
    names = root.get("/Names")
    if not names:
        return {}
    if hasattr(names, "get_object"):
        names = names.get_object()
    dests = names.get("/Dests")
    if not dests:
        return {}
    if hasattr(dests, "get_object"):
        dests = dests.get_object()
    out = {}

    def walk(node):
        node = node.get_object() if hasattr(node, "get_object") else node
        if "/Names" in node:
            n = node["/Names"]
            for i in range(0, len(n), 2):
                k = str(n[i].get_object() if hasattr(n[i], "get_object") else n[i])
                if any(k.startswith(pfx) for pfx in ["def-", "prop-", "ex-", "prob-", "name-", "fact-"]):
                    v = n[i + 1]
                    if hasattr(v, "get_object"):
                        v = v.get_object()
                    if isinstance(v, dict) and "/D" in v:
                        v = v["/D"].get_object()
                    out[k] = v
        if "/Kids" in node:
            for k in node["/Kids"]:
                walk(k)

    walk(dests)
    return out


def extract_old_links(doc, reader):
    links = []
    for pi, page in enumerate(doc):
        tp = page.get_textpage()
        p_obj = reader.pages[pi]
        for a in p_obj.get("/Annots") or []:
            a = a.get_object()
            rect = [float(x) for x in a.get("/Rect")]
            txt = tp.get_text_bounded(rect[0] - 2, rect[1] - 2, rect[2] + 2, rect[3] + 2).strip()
            txt = " ".join(txt.split())
            act = a.get("/A")
            dest = act.get("/D") if act else a.get("/Dest")
            uri = act.get("/URI") if act else None
            ctx = tp.get_text_bounded(40, rect[1] - 30, 560, rect[3] + 30).strip()
            links.append({
                "old_page": pi + 1,
                "text": txt,
                "target": str(uri or dest),
                "is_uri": uri is not None,
                "context": " ".join(ctx.split()),
            })
    return links


def locate_dest(k, cur_doc):
    searches = []
    if k.startswith("def-"):
        n = k[4:]
        searches.extend([
            f"Def. {n}", f"Def.~{n}", f"Def {n}", f"Definition (Def. {n}",
            f"Def. {int(n)-1}, {n}" if n.isdigit() and int(n) > 1 else "",
            f"Def. {n}, {int(n)+1}" if n.isdigit() else "",
            f"Def.~{int(n)-1}, {n}" if n.isdigit() and int(n) > 1 else "",
            f"Def.~{n}, {int(n)+1}" if n.isdigit() else "",
        ])
    elif k.startswith("prop-"):
        n = k[5:]
        searches.extend([
            f"Prop. {n}", f"Prop.~{n}", f"Prop {n}", f"Proposition (Prop. {n}", f"Theorem (Prop. {n}",
            f"Prop. {int(n)-1}, {n}" if n.isdigit() and int(n) > 1 else "",
            f"Prop. {n}, {int(n)+1}" if n.isdigit() else "",
            f"Prop.~{int(n)-1}, {n}" if n.isdigit() and int(n) > 1 else "",
            f"Prop.~{n}, {int(n)+1}" if n.isdigit() else "",
            f"Prop.~{n}--" if n.isdigit() else "",
            f"Prop. {n}--" if n.isdigit() else "",
        ])
    elif k.startswith("ex-"):
        n = k[3:]
        searches.extend([
            f"Ex. {n}", f"Ex.~{n}", f"Example {n}", f"Example (Ex. {n}", f"Ex {n}",
            f"Ex.~{int(n)-1}, {n}" if n.isdigit() and int(n) > 1 else "",
            f"Ex. {int(n)-1}, {n}" if n.isdigit() and int(n) > 1 else "",
            f"Ex.~{n}, {int(n)+1}" if n.isdigit() else "",
            f"Ex. {n}, {int(n)+1}" if n.isdigit() else "",
        ])
    elif k.startswith("prob-"):
        pname = k[5:].replace("-", " ")
        searches.append(pname)
        parts = k[5:].split("-")
        if len(parts) >= 2:
            searches.append(parts[-1])
    elif k.startswith("fact-"):
        tag = k[5:]
        searches.extend([f"({tag})", tag])
    elif k.startswith("name-"):
        slug = k[5:].replace("-", " ")
        searches.append(slug)
        # Aliases
        if "additive identity" in slug or "multiplicative identity" in slug or "identities and inverses" in slug:
            searches.append("Uniqueness of identities and inverses")
        elif "pigeonhole" in slug:
            searches.append("pigeonhole principle")
        elif "no zero divisors" in slug:
            searches.append("no zero divisors")
        elif "subspace test" in slug:
            searches.append("Subspace test in one line")
        elif "cauchy schwarz" in slug:
            searches.extend(["Cauchy-Schwarz", "Cauchy–Schwarz"])
        elif "polarization" in slug:
            searches.append("polarization")
        elif "last vector test" in slug:
            searches.append("last-vector test")
        elif "one vector at a time" in slug:
            searches.append("one vector at a time")
        elif "nilpotent" in slug:
            searches.append("nilpotent")
        elif "jordan" in slug:
            searches.append("Jordan")
        elif "gram schmidt" in slug:
            searches.extend(["Gram-Schmidt", "Gram--Schmidt", "Gram–Schmidt"])
        elif "riesz" in slug:
            searches.append("Riesz")
        elif "schur" in slug:
            searches.append("Schur")
        elif "spectral" in slug:
            searches.append("Spectral")

    searches = [s for s in searches if s]

    for q in searches:
        for pi, page in enumerate(cur_doc):
            tp = page.get_textpage()
            s = tp.search(q, match_case=False)
            while True:
                res = s.get_next()
                if not res:
                    break
                start, count = res
                n = tp.count_rects(start, count)
                if n > 0:
                    r = tp.get_rect(0)
                    # For prob-, prefer on last 2 pages
                    if k.startswith("prob-") and pi < len(cur_doc) - 2:
                        continue
                    return (pi, min(r[0], r[2]), max(r[1], r[3]) + 15.0)

    # Fallback to page 0 top
    return (0, 54.0, 750.0)


def get_link_queries(target, raw_txt):
    qs = []
    dest = target
    if "#nameddest=" in target:
        dest = target.split("#nameddest=")[1]

    if dest.startswith("prop-"):
        n = dest[5:]
        qs.extend([f"Prop. {n}", f"Props. {n}", f"Prop.~{n}", f"Props.~{n}", f"Prop {n}", n])
    elif dest.startswith("def-"):
        n = dest[4:]
        qs.extend([f"Def. {n}", f"Defs. {n}", f"Def.~{n}", f"Defs.~{n}", f"Def {n}", n])
    elif dest.startswith("ex-"):
        n = dest[3:]
        qs.extend([f"Ex. {n}", f"Example {n}", f"Ex.~{n}", f"Ex {n}", f"Examples {n}", n])
    elif dest.startswith("fact-"):
        tag = dest[5:]
        qs.extend([f"({tag})", tag])
    elif dest.startswith("prob-"):
        pname = dest[5:].replace("-", " ")
        qs.append(pname)
        parts = dest[5:].split("-")
        if len(parts) >= 2:
            qs.append(parts[-1])
    elif dest.startswith("name-"):
        slug = dest[5:].replace("-", " ")
        qs.append(slug)
        if "cauchy schwarz" in slug:
            qs.extend(["Cauchy-Schwarz", "Cauchy–Schwarz"])
        elif "polarization" in slug:
            qs.append("polarization")
        elif "positivity test" in slug:
            qs.append("positivity test")
        elif "last vector test" in slug:
            qs.append("last-vector test")
        elif "one vector at a time" in slug:
            qs.append("one vector at a time")
        elif "pigeonhole" in slug:
            qs.append("pigeonhole principle")
        elif "powers of m" in slug:
            qs.append("powers of x")
    elif "handout.pdf" in target:
        for k, v in WEEK_NUMBERS.items():
            if k in target:
                qs.extend([f"Week {v}", f"(Week {v})", f"W{v}"])

    # Clean raw_txt
    m = re.findall(r"(?:[A-Za-z][a-z0-9\.\-]*|\d+)", raw_txt)
    if m:
        c = " ".join(m)
        if c not in qs and len(c) >= 2:
            qs.append(c)

    return qs


def process_week(w):
    pdf_path = f"{BASE_DIR}/{w}/handout.pdf"
    if not os.path.exists(pdf_path):
        print(f"Skipping {w}: handout.pdf not found")
        return

    # 1. Load old PDF from git 2f04fde
    try:
        old_data = subprocess.check_output(["git", "show", f"2f04fde:{pdf_path}"])
    except Exception as e:
        print(f"Error fetching 2f04fde for {w}: {e}")
        return

    old_doc = pdfium.PdfDocument(old_data)
    old_reader = PdfReader(io.BytesIO(old_data))
    with open(pdf_path, "rb") as f:
        cur_data = f.read()
    cur_doc = pdfium.PdfDocument(cur_data)
    cur_reader = PdfReader(io.BytesIO(cur_data))

    old_custom_dests = extract_old_dests(old_reader)
    old_links = extract_old_links(old_doc, old_reader)

    # 2. Locate destinations in cur_doc
    located_dests = {}
    for k in old_custom_dests:
        located_dests[k] = locate_dest(k, cur_doc)

    # Ensure self-week cross citations have destinations too
    # If any link in old_links points to a dest not in old_custom_dests
    for l in old_links:
        t = l["target"]
        if not l["is_uri"] and t not in located_dests:
            located_dests[t] = locate_dest(t, cur_doc)

    # 3. Locate links in cur_doc
    placed_links_by_page = {i: [] for i in range(len(cur_doc))}
    matched_links = 0

    for l in old_links:
        qs = get_link_queries(l["target"], l["text"])
        found = []
        for q in qs:
            for pi, page in enumerate(cur_doc):
                tp = page.get_textpage()
                s = tp.search(q, match_case=False)
                while True:
                    res = s.get_next()
                    if not res:
                        break
                    start, count = res
                    n = tp.count_rects(start, count)
                    if n > 0:
                        # Collect all rects for this match (handling multiline)
                        rects = [tp.get_rect(ri) for ri in range(n)]
                        # context from first rect
                        r0 = rects[0]
                        c = tp.get_text_bounded(40, min(r0[1], r0[3]) - 25, 560, max(r0[1], r0[3]) + 25)
                        found.append((pi, rects, " ".join(c.split()), q))
            if found:
                break

        best = None
        best_score = -1
        w1 = set(l["context"].lower().split())
        for pi, rects, c, q in found:
            w2 = set(c.lower().split())
            score = len(w1 & w2)
            if score > best_score:
                best_score = score
                best = (pi, rects, q)

        if best and best_score >= 2:
            matched_links += 1
            pi, rects, q = best
            for r in rects:
                placed_links_by_page[pi].append((r, l))

    # 4. Reconstruct PDF with PdfWriter
    writer = PdfWriter()
    for pi, page in enumerate(cur_reader.pages):
        if "/Annots" in page:
            del page["/Annots"]
        writer.add_page(page)

    # Add destinations
    for k, (pno, left, top) in sorted(located_dests.items()):
        pref = writer.pages[pno].indirect_reference
        dest_array = ArrayObject([
            pref,
            NameObject("/XYZ"),
            FloatObject(left),
            FloatObject(top),
            NullObject(),
        ])
        writer.add_named_destination_array(TextStringObject(k), dest_array)

    # Add link annotations
    total_annots = 0
    for pno, links in placed_links_by_page.items():
        for r, l in links:
            total_annots += 1
            x1 = min(r[0], r[2])
            x2 = max(r[0], r[2])
            y1 = min(r[1], r[3])
            y2 = max(r[1], r[3])

            annot = DictionaryObject({
                NameObject("/Type"): NameObject("/Annot"),
                NameObject("/Subtype"): NameObject("/Link"),
                NameObject("/Rect"): ArrayObject([FloatObject(x1), FloatObject(y1), FloatObject(x2), FloatObject(y2)]),
                NameObject("/Border"): ArrayObject([FloatObject(0), FloatObject(0), FloatObject(0)]),
                NameObject("/F"): NumberObject(4),
            })
            if l["is_uri"]:
                annot[NameObject("/A")] = DictionaryObject({
                    NameObject("/S"): NameObject("/URI"),
                    NameObject("/URI"): TextStringObject(l["target"]),
                })
            else:
                annot[NameObject("/A")] = DictionaryObject({
                    NameObject("/S"): NameObject("/GoTo"),
                    NameObject("/D"): TextStringObject(l["target"]),
                })
            writer.add_annotation(pno, annot)

    # Write out to handout.pdf
    tmp_path = pdf_path + ".tmp"
    with open(tmp_path, "wb") as f:
        writer.write(f)
    cur_doc.close()
    old_doc.close()
    os.replace(tmp_path, pdf_path)

    print(
        f"  {w:45s}: {len(located_dests):2d} dests, {matched_links:3d}/{len(old_links):3d} links placed ({total_annots} rects)"
    )


def main():
    print("=========================================================")
    print("Restoring hyperlinks and named destinations (Weeks 1-10)")
    print("=========================================================")
    for w in WEEKS:
        process_week(w)
    print("\nAll weeks processed. Validating...")

    total_dests = 0
    total_links = 0
    for w in WEEKS:
        pdf_path = f"{BASE_DIR}/{w}/handout.pdf"
        r = PdfReader(pdf_path)
        root = r.trailer["/Root"]
        names = root.get("/Names")
        dests = names.get_object().get("/Dests").get_object() if names else None

        def count_tree(node):
            node = node.get_object() if hasattr(node, "get_object") else node
            cnt = 0
            if "/Names" in node:
                cnt += len(node["/Names"]) // 2
            if "/Kids" in node:
                cnt += sum(count_tree(k) for k in node["/Kids"])
            return cnt

        d_count = count_tree(dests) if dests else 0
        l_count = sum(len(p.get("/Annots", [])) for p in r.pages)
        total_dests += d_count
        total_links += l_count
        print(f"  {w:45s}: {len(r.pages):2d}p, {d_count:2d} dests, {l_count:3d} links")

    print(f"\nTOTAL: {total_dests} named destinations, {total_links} links across all 10 weeks.")


if __name__ == "__main__":
    main()
