#!/usr/bin/env python3
"""Build solutions/ for a week's exercises.

Usage: python3 scripts/make_solutions.py <handout folder> <module> <answers file>

<answers file> is a Python file defining ANSWERS, a list of function bodies (strings, already
indented) in the order of the "*** YOUR CODE HERE ***" markers in exercises/<module>.py.
Writes solutions/<module>.py, and solutions/predict.py with every prediction filled in by
actually running the snippet.
"""
import contextlib, importlib.util, io, os, sys

def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

folder, module, answers = sys.argv[1], sys.argv[2], sys.argv[3]
marker = '    "*** YOUR CODE HERE ***"'
src = open(os.path.join(folder, "exercises", module + ".py")).read()
parts = src.split(marker)
ans = load(answers, "answers").ANSWERS
assert len(parts) == len(ans) + 1, (len(parts) - 1, len(ans))
out = parts[0]
for a, p in zip(ans, parts[1:]):
    out += a.rstrip("\n") + p
os.makedirs(os.path.join(folder, "solutions"), exist_ok=True)
open(os.path.join(folder, "solutions", module + ".py"), "w").write(out)
pp = os.path.join(folder, "exercises", "predict.py")
if os.path.exists(pp):
    m = load(pp, "predict_src"); t = open(pp).read()
    for k, code in m.SNIPPETS.items():
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            try: exec(code, {"__name__": "snippet"})
            except Exception: print("ERROR")
        old = '"%s": """?""",' % k
        assert old in t, k
        t = t.replace(old, '"%s": """%s""",' % (k, buf.getvalue().strip()))
    open(os.path.join(folder, "solutions", "predict.py"), "w").write(t)
print("solutions written")
