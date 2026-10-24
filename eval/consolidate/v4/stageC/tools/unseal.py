"""Stage C, after the owner has graded: open the key and compare conditions. Run ONLY after the owner says grading is
done (heldout/criteria.md, "The owner"; plan.md revision 7).

    python3 unseal.py       owner's sheets (<vault>/temp/stage-C/*.sheet.md), the key, blind sheets and fact-checks
                            -> usability/unsealed.md

Owner's per-piece sheet: each "A<n> ... _ /3" line with the _ replaced by a digit (0-3); Part B lines with one of
Yes / Partly / No left (or marked). Pair sheet: "Preferred:" with A, B or "no preference" left. Anything not parseable
is reported as unclear, never guessed.
"""
import re
import statistics as st
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import compile as cp  # noqa: E402
import usability as us  # noqa: E402

U = HERE.parent / "usability"
OWN = us.VAULT / "temp" / "stage-C"
CRIT = [f"A{i}" for i in range(1, 11)]


def owner_piece(p):
    t = (OWN / f"{p}.sheet.md").read_text(encoding="utf-8")
    sc = {}
    for ln in t.splitlines():
        m = re.match(r"\s*(A(?:10|[1-9]))\b\D*?([0-3])\s*/\s*3", ln)
        if m:
            sc[m.group(1)] = int(m.group(2))
    sc["total"] = sum(sc[c] for c in CRIT) if all(c in sc for c in CRIT) else None
    b = {}
    for ln in t.splitlines():
        m = re.match(r"\s*(B[1-5])\b[^:]*?\s{2,}(.+)$", ln)
        if m:
            left = [w for w in ("Yes", "Partly", "No") if re.search(rf"\b{w}\b", m.group(2))]
            b[m.group(1)] = left[0] if len(left) == 1 else "unclear"
    return sc, b


def owner_pair(k, n):
    t = (OWN / f"T{k}-pair{n}.sheet.md").read_text(encoding="utf-8")
    m = re.search(r"Preferred:\s*(.+)", t)
    v = m.group(1) if m else ""
    left = [x for x in ("no preference", "A", "B") if re.search(rf"(?<![\w]){re.escape(x)}(?![\w])", v)]
    if "no preference" in left and len(left) > 1:
        left = [x for x in left if x != "no preference"] if "/" in v else left
    return left[0] if len(left) == 1 else "unclear"


def mean(xs):
    xs = [x for x in xs if x is not None]
    return f"{st.mean(xs):.2f}" if xs else "?"


def main():
    key = us._key()
    L = ["# Stage C usability: unsealed (after the owner graded)\n", "## The key\n", "| Piece | Input |", "|---|---|"]
    L += [f"| {p} | {key[p]} |" for p in cp.PIECES]
    own = {p: owner_piece(p) for p in cp.PIECES}
    blind = {p: cp.blind_scores(p) for p in cp.PIECES}
    fc = {p: cp.fc_counts(p) for p in cp.PIECES}
    by = {c: [p for p in cp.PIECES if key[p] == c] for c in ("raw", "view")}
    L += ["", "## Scores by condition (means over 6 pieces)\n",
          "| Measure | Raw: owner | View: owner | Raw: blind | View: blind |", "|---|---|---|---|---|"]
    for c in CRIT + ["total"]:
        L.append(f"| {c} | {mean(own[p][0].get(c) for p in by['raw'])} | {mean(own[p][0].get(c) for p in by['view'])} | "
                 f"{mean(blind[p].get(c) for p in by['raw'])} | {mean(blind[p].get(c) for p in by['view'])} |")
    L += ["", "## Fact-check counts by condition (sums over 6 pieces)\n", "| Class | Raw | View |", "|---|---|---|"]
    for c in cp.CLASSES + ["faults"]:
        g = (lambda p: sum(fc[p][x] for x in cp.FAULTS)) if c == "faults" else (lambda p, c=c: fc[p][c])
        L.append(f"| {c} | {sum(g(p) for p in by['raw'])} | {sum(g(p) for p in by['view'])} |")
    L += ["", "## Each pair: which input was preferred, and totals\n",
          "| Pair | Owner prefers | Blind prefers | Owner totals raw, view | Blind totals raw, view | Faults raw, view |",
          "|---|---|---|---|---|---|"]
    for k in (1, 2, 3):
        for n in (1, 2):
            a, b = f"T{k}-{n}A", f"T{k}-{n}B"
            cond = {"A": key[a], "B": key[b], "no preference": "none", "unclear": "unclear"}
            op = owner_pair(k, n)
            bp_raw = cp.pair(k, n)[0]
            bp = next((x for x in ("no preference", "A", "B") if re.match(rf"\s*{re.escape(x)}\b", bp_raw)), "unclear")
            raw_p, view_p = (a, b) if key[a] == "raw" else (b, a)
            L.append(f"| T{k} pair {n} | {cond[op]} | {cond[bp]} | {own[raw_p][0]['total']}, {own[view_p][0]['total']} | "
                     f"{blind[raw_p]['total']}, {blind[view_p]['total']} | "
                     f"{sum(fc[raw_p][x] for x in cp.FAULTS)}, {sum(fc[view_p][x] for x in cp.FAULTS)} |")
    L += ["", "## Owner against blind readers, criterion by criterion (12 pieces)\n",
          "| Criterion | Owner mean | Blind mean | Mean of (owner minus blind) | Same score | Within 1 |",
          "|---|---|---|---|---|---|"]
    for c in CRIT + ["total"]:
        pairs = [(own[p][0].get(c), blind[p].get(c)) for p in cp.PIECES]
        pairs = [(o, b) for o, b in pairs if o is not None and b is not None]
        if not pairs:
            L.append(f"| {c} | ? | ? | ? | ? | ? |")
            continue
        L.append(f"| {c} | {st.mean(o for o, _ in pairs):.2f} | {st.mean(b for _, b in pairs):.2f} | "
                 f"{st.mean(o - b for o, b in pairs):+.2f} | {sum(o == b for o, b in pairs)}/{len(pairs)} | "
                 f"{sum(abs(o - b) <= 1 for o, b in pairs)}/{len(pairs)} |")
    L += ["", "## Part B (owner, recorded not scored)\n", "| Piece | Input | B1 | B2 | B3 | B4 | B5 |",
          "|---|---|---|---|---|---|---|"]
    for p in cp.PIECES:
        b = own[p][1]
        L.append(f"| {p} | {key[p]} | " + " | ".join(b.get(f"B{i}", "?") for i in range(1, 6)) + " |")
    unclear = [p for p in cp.PIECES if own[p][0]["total"] is None]
    L += ["", f"Owner sheets not fully parsed (a score missing): {', '.join(unclear) or 'none'}."]
    (U / "unsealed.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"usability/unsealed.md written; unparsed owner sheets: {unclear or 'none'}")


if __name__ == "__main__":
    main()
