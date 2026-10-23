"""Stage B, B3 to B7: first-pass scoring of a rebuilt note under the frozen checking procedure (plan.md revision 5):
two fresh checkers per 60-entry packet (`kn.py packets --hints`), a fault from either counted.

    python3 rebuild.py first <dir>     after <dir>/verdicts-a/ and verdicts-b/ -> <dir>/first-pass.md, and
                                       <dir>/fixes-1.md (the verdict lines the builder gets: faulted entries only)
    python3 rebuild.py recheck <dir> <n>   after <dir>/recheck-<n>/verdicts.md -> prints still-faulted entries and
                                       writes <dir>/fixes-<n+1>.md if any
<dir> is stageB/rebuild/<NOTE>/, holding packets/ from `kn.py packets <note> <dir>/packets --hints`.
"""
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from planted import wilson  # noqa: E402

KINDS = ("stronger", "conf", "numbers", "absent", "critic", "merged", "holds")
LINE = re.compile(r"^\s*[-*]?\s*`?([A-Za-z0-9][A-Za-z0-9-]*\.[A-Za-z0-9]+)`?(?:\s*\([^)]*\))?:\s*(.*)$")


def packet_ids(d):
    out = []
    for f in sorted((d / "packets").glob("packet-*.md")):
        ids = re.findall(r"^## (\S+) \(", f.read_text(encoding="utf-8"), re.M)
        out.append((f.name, ids))
    return out


def read(f):
    """{id: (kinds, the line's text)} from one verdict file."""
    out = {}
    for ln in Path(f).read_text(encoding="utf-8").splitlines():
        m = LINE.match(ln.strip())
        if not m:
            continue
        rest = m.group(2).strip()
        if re.match(r"ok\b", rest, re.I):
            out[m.group(1)] = (set(), "ok")
        else:
            head = rest.split(":", 1)[0].lower()
            out[m.group(1)] = ({x for x in re.split(r"[\s,/+]+", head) if x in KINDS} or {"other"}, rest)
    return out


def cmd_first(d):
    d = Path(d)
    packs = packet_ids(d)
    a, b, missing = {}, {}, []
    for name, ids in packs:
        for side, store in (("a", a), ("b", b)):
            f = d / f"verdicts-{side}" / name
            v = read(f) if f.exists() else {}
            store.update(v)
            missing += [f"{side}/{name}: {i}" for i in ids if i not in v]
    if missing:
        sys.exit(f"missing verdicts ({len(missing)}): {missing[:8]}")
    ids = [i for _, xs in packs for i in xs]
    union = {i: a[i][0] | b[i][0] for i in ids}
    n, f = len(ids), sum(bool(union[i]) for i in ids)
    lo, hi = wilson(f, n)
    per100 = lambda ks: 100 * sum(bool(union[i] & ks) for i in ids) / n
    L = [f"# First pass: {d.name}\n",
         "Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a "
         "fault from either counted.\n",
         f"- **First-pass fault rate: {f}/{n} = {f / n:.1%}** (Wilson {lo:.1%} to {hi:.1%}).",
         f"- Checker A alone {sum(bool(a[i][0]) for i in ids)}, checker B alone {sum(bool(b[i][0]) for i in ids)}, "
         f"both {sum(bool(a[i][0]) and bool(b[i][0]) for i in ids)}; agree (ok against fault) on "
         f"{sum(bool(a[i][0]) == bool(b[i][0]) for i in ids)} of {n}.",
         f"- Per 100 entries: holds + absent {per100({'holds', 'absent'}):.1f}; stronger + numbers "
         f"{per100({'stronger', 'numbers'}):.1f}; conf {per100({'conf'}):.1f}; critic {per100({'critic'}):.1f}; "
         f"merged {per100({'merged'}):.1f}.",
         f"- Kinds (entries): {', '.join(f'{k} {c}' for k, c in Counter(k for i in ids for k in union[i]).most_common())}.",
         "", "| Packet | Entries | A | B | Either | Agree |", "|---|---|---|---|---|---|"]
    for name, xs in packs:
        L.append(f"| {name} | {len(xs)} | {sum(bool(a[i][0]) for i in xs)} | {sum(bool(b[i][0]) for i in xs)} | "
                 f"{sum(bool(union[i]) for i in xs)} | {sum(bool(a[i][0]) == bool(b[i][0]) for i in xs)} |")
    L += ["", "## Every `stronger` and `numbers` fault (gate B, criterion 3)\n", "| Entry | Kinds | Checkers' reasons |",
          "|---|---|---|"]
    for i in ids:
        if union[i] & {"stronger", "numbers"}:
            rs = " / ".join(x[1] for x in (a[i], b[i]) if x[0])
            L.append(f"| {i} | {', '.join(sorted(union[i]))} | {rs.replace('|', '/')} |")
    (d / "first-pass.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    fx = [f"{i}: {x[1]}" for i in ids if union[i] for x in (a[i], b[i]) if x[0]]
    (d / "fixes-1.md").write_text(f"# Faults to fix ({f} entries)\n\n" + "\n".join(fx) + "\n", encoding="utf-8")
    print("\n".join(L[2:7]))


def cmd_recheck(d, n):
    d, n = Path(d), int(n)
    fixed = [ln.split(":", 1)[0] for ln in (d / f"fixes-{n}.md").read_text(encoding="utf-8").splitlines()
             if LINE.match(ln)]
    fixed = list(dict.fromkeys(fixed))
    v = read(d / f"recheck-{n}" / "verdicts.md")
    miss = [i for i in fixed if i not in v]
    if miss:
        sys.exit(f"re-check missing {len(miss)}: {miss[:8]}")
    still = [i for i in fixed if v[i][0]]
    print(f"round {n}: {len(fixed)} fixed entries re-checked, {len(still)} still faulted "
          f"({len(still) / len(fixed):.0%})")
    if still:
        (d / f"fixes-{n + 1}.md").write_text(f"# Faults to fix ({len(still)} entries)\n\n" +
                                             "\n".join(f"{i}: {v[i][1]}" for i in still) + "\n", encoding="utf-8")


if __name__ == "__main__":
    {"first": lambda: cmd_first(sys.argv[2]), "recheck": lambda: cmd_recheck(sys.argv[2], sys.argv[3])}[sys.argv[1]]()
