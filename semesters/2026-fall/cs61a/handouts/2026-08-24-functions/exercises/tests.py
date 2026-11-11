"""Run from this folder: python3 tests.py   (add a folder name to test another copy,
e.g. python3 tests.py ../solutions)."""
import contextlib, doctest, importlib, io, sys

folder = sys.argv[1] if len(sys.argv) > 1 else "."
sys.path.insert(0, folder)
week = importlib.import_module("week01")
predict = importlib.import_module("predict")

def actual_output(code):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try:
            exec(code, {"__name__": "snippet"})
        except Exception:
            print("ERROR")
    return buf.getvalue().strip()

failed = 0
res = doctest.testmod(week, verbose=False)
print(f"week01.py: {res.attempted - res.failed} of {res.attempted} doctests pass")
failed += res.failed

src = open(f"{folder}/week01.py").read()
body = src.split('"""', 2)[2]
for word in (" if ", "while ", "for ", " and ", " or ", "sorted("):
    code_lines = [l for l in body.splitlines() if not l.strip().startswith((">>>", "...", "#")) and '"""' not in l]
    in_doc = False; used = False
    for l in body.splitlines():
        if l.count('"""') == 1: in_doc = not in_doc; continue
        if not in_doc and '"""' not in l and word in l: used = True
    if used:
        print(f"week01.py: uses '{word.strip()}', which this week's rules do not allow"); failed += 1

right = 0
for name, code in predict.SNIPPETS.items():
    want = actual_output(code)
    got = "\n".join(l.rstrip() for l in predict.PREDICTIONS[name].strip().splitlines())
    if got == want: right += 1
    else: print(f"predict.py: {name} is not right yet")
print(f"predict.py: {right} of {len(predict.SNIPPETS)} predictions correct")
failed += len(predict.SNIPPETS) - right
print("ALL PASS" if failed == 0 else "not done yet")
sys.exit(1 if failed else 0)
