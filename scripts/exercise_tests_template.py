"""Run from this folder: python3 tests.py   (or: python3 tests.py ../solutions)."""
import contextlib, doctest, importlib, io, os, sys

MODULE = "WEEKMODULE"
folder = sys.argv[1] if len(sys.argv) > 1 else "."
sys.path.insert(0, folder)
failed = 0

week = importlib.import_module(MODULE)
res = doctest.testmod(week, verbose=False)
print(f"{MODULE}.py: {res.attempted - res.failed} of {res.attempted} doctest lines pass")
failed += res.failed

if os.path.exists(os.path.join(folder, "predict.py")):
    predict = importlib.import_module("predict")
    def actual_output(code):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            try:
                exec(code, {"__name__": "snippet"})
            except Exception:
                print("ERROR")
        return buf.getvalue().strip()
    right = 0
    for name, code in predict.SNIPPETS.items():
        got = "\n".join(l.rstrip() for l in predict.PREDICTIONS[name].strip().splitlines())
        if got == actual_output(code): right += 1
        else: print(f"predict.py: {name} is not right yet")
    print(f"predict.py: {right} of {len(predict.SNIPPETS)} predictions correct")
    failed += len(predict.SNIPPETS) - right

print("ALL PASS" if failed == 0 else "not done yet")
sys.exit(1 if failed else 0)
