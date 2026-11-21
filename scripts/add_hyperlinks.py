#!/usr/bin/env python3
"""
add_hyperlinks.py
-----------------
For each of the 10 Math 110 handout .tex files (Weeks 1-10):
  1. Add \\hypertarget{slug}{} directly before each \\label{slug} so the PDF
     named-destination tree gets an entry for every label.
  2. Wrap in-text citations (Prop.~N, Def.~N, Ex.~N, HWX PY) with
     \\hyperref[slug]{...} so they render in RoyalBlue when compiled with
     colorlinks=true (set in handout.sty).

Then recompile all 10 weeks with pdflatex.
"""

import os
import re
import subprocess
import sys

BASE = r"C:\Users\aaron\OneDrive\Documents\GitHub\berkeley\semesters\2026-fall\math110\handouts"
TEMPLATE_DIR = r"C:\Users\aaron\OneDrive\Documents\GitHub\berkeley\templates"
MIKTEX = r"C:\Users\aaron\AppData\Local\Programs\MiKTeX\miktex\bin\x64"

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

# ------------------------------------------------------------------
# Step 1: Build the citation → label map from every .tex file.
# Pattern: \begin{env*}[Display text ...]\\label{slug}
# We extract from the display text things like:
#   "Prop.~7"  -> prop-7
#   "Def.~5"   -> def-5
#   "Ex.~19"   -> ex-19
#   "HW1 P3"   -> prob-HW1-P3
# ------------------------------------------------------------------

# Maps citation text (what appears in body, e.g. "Prop.~7") -> label slug
citation_map = {}  # {citation_text: slug}

# Also build a set of all labels (slug -> week_index) for hypertarget pass
all_labels = set()

LABEL_RE = re.compile(r'\\label\{([^}]+)\}')
# Matches \begin{anything*}[...content...]\label{slug} possibly on same line
BEGIN_LABEL_RE = re.compile(r'\\begin\{[^}]+\}\[([^\]]*)\].*?\\label\{([^}]+)\}')

def extract_citation_keys(display_text):
    """
    Given a display text like 'Prop.~7 / LADR 1.41, 1.45', extract
    all citation strings that might appear in the body.
    Returns list of strings like ['Prop.~7'].
    """
    keys = []
    # Prop.~N or Prop.~N--M (we link to the first)
    for m in re.finditer(r'Prop\.\~(\d+)', display_text):
        keys.append(f'Prop.~{m.group(1)}')
    # Def.~N
    for m in re.finditer(r'Def\.\~(\d+)', display_text):
        keys.append(f'Def.~{m.group(1)}')
    # Ex.~N
    for m in re.finditer(r'Ex\.\~(\d+)', display_text):
        keys.append(f'Ex.~{m.group(1)}')
    return keys


for week in WEEKS:
    tex_path = os.path.join(BASE, week, "handout.tex")
    if not os.path.exists(tex_path):
        continue
    with open(tex_path, encoding="utf-8") as f:
        content = f.read()

    # Collect all labels
    for m in LABEL_RE.finditer(content):
        slug = m.group(1)
        all_labels.add(slug)

    # For each \begin{env}[display]\label{slug}, extract citation keys
    for m in BEGIN_LABEL_RE.finditer(content):
        display = m.group(1)
        slug = m.group(2)
        for key in extract_citation_keys(display):
            if key not in citation_map:
                citation_map[key] = slug

    # Also handle HW labels: prob-HW1-P3 etc.
    # These appear as "HW1 P3" in body text
    for m in re.finditer(r'\\label\{prob-(HW\d+-P\d+)\}', content):
        raw = m.group(1)  # e.g. HW1-P3
        cite_text = raw.replace('-', ' ')  # "HW1 P3"
        if cite_text not in citation_map:
            citation_map[cite_text] = m.group(0).replace('\\label{', '').replace('}', '')

# Fix: re-extract prob-HW labels properly
citation_map_hw = {}
for week in WEEKS:
    tex_path = os.path.join(BASE, week, "handout.tex")
    if not os.path.exists(tex_path):
        continue
    with open(tex_path, encoding="utf-8") as f:
        content = f.read()
    for m in re.finditer(r'\\label\{(prob-HW(\d+)-P(\d+))\}', content):
        slug = m.group(1)   # prob-HW1-P3
        hw_num = m.group(2) # 1
        p_num = m.group(3)  # 3
        cite_text = f'HW{hw_num} P{p_num}'
        citation_map_hw[cite_text] = slug

citation_map.update(citation_map_hw)

print(f"Built citation map with {len(citation_map)} entries:")
for k, v in sorted(citation_map.items()):
    print(f"  {k!r} -> {v!r}")

# ------------------------------------------------------------------
# Step 2: Process each .tex file.
# ------------------------------------------------------------------

def add_hypertargets(content):
    """
    Insert \\hypertarget{slug}{} directly before \\label{slug}
    if not already present.
    """
    def replacer(m):
        slug = m.group(1)
        # Check if the char before this match is already \hypertarget{slug}{}
        return f'\\hypertarget{{{slug}}}{{}}\\label{{{slug}}}'
    # Only replace \label{...} not already preceded by \hypertarget on same line
    # We use a negative lookbehind for the hypertarget
    result = re.sub(r'\\label\{([^}]+)\}', replacer, content)
    return result


def wrap_citations(content, citation_map):
    """
    Wrap in-text citations with \\hyperref[slug]{text}.
    We must NOT wrap citations that are already inside:
      - \begin{...} lines (the [display text] argument)
      - \label{...} argument
      - \hypertarget{...} argument
      - Already inside a \hyperref[...]{...}
      - Inside a comment (% ...)
      - Inside \section, \subsection, \subsubsection titles
    
    Strategy: process line by line, skip lines that look like
    LaTeX command arguments.
    """
    lines = content.split('\n')
    result_lines = []
    
    for line in lines:
        # Skip comment lines
        stripped = line.strip()
        if stripped.startswith('%'):
            result_lines.append(line)
            continue
        # Skip \begin, \end, \section, \subsection lines (they contain display names)
        if re.match(r'\s*\\(begin|end|section|subsection|subsubsection|title|subtitle)\b', line):
            result_lines.append(line)
            continue
        # Skip lines that already have \hyperref or \hypertarget
        if '\\hyperref' in line or '\\hypertarget' in line:
            result_lines.append(line)
            continue
        # Skip lines that are \label{...} only
        if re.match(r'\s*\\label\{', line):
            result_lines.append(line)
            continue
        
        # For each citation key (sorted longest first to avoid partial matches)
        modified_line = line
        for cite_text in sorted(citation_map.keys(), key=len, reverse=True):
            slug = citation_map[cite_text]
            escaped = re.escape(cite_text)
            # Only wrap if NOT already inside a hyperref or similar command
            # and not inside a \label or \begin argument
            # Use word-boundary-like checks
            pattern = r'(?<!\\hyperref\[' + re.escape(slug) + r'\]\{)' + escaped
            # Simpler: just replace bare occurrences not preceded by { (already wrapped)
            # We replace "cite_text" with \hyperref[slug]{cite_text}
            # But avoid double-wrapping: skip if already wrapped
            new_line = re.sub(
                r'(?<!\{)' + escaped + r'(?!\})',
                r'\\hyperref[' + slug + r']{' + cite_text + r'}',
                modified_line
            )
            modified_line = new_line
        
        result_lines.append(modified_line)
    
    return '\n'.join(result_lines)


for week in WEEKS:
    tex_path = os.path.join(BASE, week, "handout.tex")
    if not os.path.exists(tex_path):
        print(f"SKIP (no tex): {week}")
        continue
    
    with open(tex_path, encoding="utf-8") as f:
        original = f.read()
    
    # Skip if already processed
    if '\\hypertarget' in original:
        print(f"SKIP (already has hypertarget): {week}")
        continue
    
    # Add hypertargets
    modified = add_hypertargets(original)
    # Wrap citations
    modified = wrap_citations(modified, citation_map)
    
    with open(tex_path, 'w', encoding="utf-8", newline='\r\n') as f:
        f.write(modified)
    
    print(f"PROCESSED: {week}")

print("\nAll .tex files processed.")

# ------------------------------------------------------------------
# Step 3: Recompile all 10 weeks with pdflatex (2 passes for refs).
# ------------------------------------------------------------------

env = os.environ.copy()
env['PATH'] = MIKTEX + ';' + env.get('PATH', '')
env['TEXINPUTS'] = f'.;{TEMPLATE_DIR};;'

PDFLATEX = os.path.join(MIKTEX, 'pdflatex.exe')

compile_errors = []

for week in WEEKS:
    week_dir = os.path.join(BASE, week)
    tex_path = os.path.join(week_dir, "handout.tex")
    if not os.path.exists(tex_path):
        print(f"SKIP compile (no tex): {week}")
        continue
    
    print(f"\nCompiling {week} ...")
    
    for pass_num in range(1, 3):
        result = subprocess.run(
            [PDFLATEX, '-halt-on-error', '-interaction=nonstopmode', 'handout.tex'],
            cwd=week_dir,
            env=env,
            capture_output=True,
            text=True,
            timeout=120,
        )
        if result.returncode != 0:
            print(f"  ERROR on pass {pass_num}:")
            # Show last 20 lines of output
            lines = (result.stdout + result.stderr).splitlines()
            for l in lines[-20:]:
                print(f"    {l}")
            compile_errors.append(week)
            break
        else:
            print(f"  Pass {pass_num} OK")

print("\n=== COMPILE SUMMARY ===")
if compile_errors:
    print(f"ERRORS in: {compile_errors}")
else:
    print("All 10 weeks compiled successfully!")
