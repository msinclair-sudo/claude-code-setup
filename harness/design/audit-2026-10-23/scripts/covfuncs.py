"""Never-run lines grouped by top-level function, from coverage json. One file per slice."""
import json, re, sys, pathlib
J = pathlib.Path(sys.argv[1])
cov = json.loads((J / "cov.json").read_text())["files"]
def funcs(path):
    lines = pathlib.Path(path).read_text().splitlines()
    out, cur = [], None
    for i, l in enumerate(lines, 1):
        m = re.match(r"(?:def|class) (\w+)", l)
        if m:
            cur = [m.group(1), i, i]; out.append(cur)
        elif cur and (l.strip() and not l.startswith((" ", "\t", "#", ")"))):
            cur = None
        if cur: cur[2] = i
    return out
def report(path, key, lo, hi, dest):
    miss = set(cov[key]["missing_lines"]); exe = set(cov[key]["executed_lines"])
    rows = ["# never-run lines by function, %s lines %d-%d (suite: 592 tests)" % (key, lo, hi),
            "# NOT RUN = whole function never executed by the suite; else missed/total statements",
            "# name start-end | status | missed line ranges"]
    for name, a, b in funcs(path):
        if b < lo or a > hi: continue
        m = sorted(x for x in miss if a <= x <= b); e = [x for x in exe if a <= x <= b]
        if not m: continue
        rng, s = [], m[0]; p = s
        for x in m[1:] + [None]:
            if x != p + 1 if x else True:
                rng.append(f"{s}" if s == p else f"{s}-{p}");
                if x: s = x
            if x: p = x
        status = "NOT RUN" if len(e) <= 1 else f"{len(m)}/{len(m)+len(e)} missed"
        rows.append(f"{name} {a}-{b} | {status} | {' '.join(rng)}")
    (J / dest).write_text("\n".join(rows) + "\n")
    return len(rows) - 3
H = "setup/harness/bin/harness"
for tag, lo, hi in [("A", 1, 5543), ("B", 5544, 12010), ("C", 12011, 20109), ("D", 20110, 10**6)]:
    print(tag, report(H, "harness/bin/harness", lo, hi, f"cov_{tag}.txt"))
print("gui", report("setup/harness/bin/harness-gui", "harness/bin/harness-gui", 1, 10**6, "cov_gui.txt"))
print("mail", report("setup/harness/bin/harness-mail", "harness/bin/harness-mail", 1, 10**6, "cov_mail.txt"))
