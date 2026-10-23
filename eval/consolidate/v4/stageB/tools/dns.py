"""Stage B, B8: do-not-say readability (plan.md, stage B step 6). Information, not a gate criterion.

    python3 dns.py prep     every rebuilt note's writer's view -> rebuild/<NOTE>/writer.md; their Do not say
                            sections, entries numbered <NOTE>/<n> -> dns-readability/packet.md
    python3 dns.py score    after dns-readability/verdicts.md (one line per entry, `<NOTE>/<n>: usable: ...` or
                            `<NOTE>/<n>: fragment: ...`) -> dns-readability/results.md (target: at least 90% usable)
"""
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import rebuild  # noqa: E402
from planted import wilson  # noqa: E402
from results import ORDER  # noqa: E402

D = HERE.parent / "dns-readability"
R = HERE.parent / "rebuild"


def section(text):
    m = re.search(r"^## Do not say\n(.*?)(?=^## )", text, re.S | re.M)
    return m.group(1) if m else ""


def entries(sec):
    """The bullet blocks of a Do not say section, each from its '- Do not write:' line to the next."""
    out, cur = [], None
    for ln in sec.splitlines():
        if ln.startswith("- Do not write:"):
            cur = [ln]
            out.append(cur)
        elif cur is not None and (ln.startswith("  ") or not ln.strip()):
            if ln.strip():
                cur.append(ln)
        elif cur is not None and ln.strip():
            cur = None
    return ["\n".join(x) for x in out]


def cmd_prep():
    k = rebuild.kn()
    D.mkdir(exist_ok=True)
    L = ["# Do not say, from the writer's view of each note\n"]
    total = 0
    for n in ORDER:
        vp = R / n / "vault-path.txt"
        rel = vp.read_text(encoding="utf-8").strip() if vp.exists() else rebuild.NOTES[n]
        out = R / n / "writer.md"
        k.view(rebuild.VAULT / rel, out)
        es = entries(section(out.read_text(encoding="utf-8")))
        total += len(es)
        L.append(f"## {n} ({len(es)} entries)\n")
        for i, e in enumerate(es, 1):
            L.append(f"### {n}/{i}\n\n{e}\n")
    (D / "packet.md").write_text("\n".join(L), encoding="utf-8")
    print(f"{total} do-not-say entries in {len(ORDER)} notes -> {D / 'packet.md'}")


def cmd_score():
    ids = re.findall(r"^### (\S+/\d+)$", (D / "packet.md").read_text(encoding="utf-8"), re.M)
    v = {}
    for ln in (D / "verdicts.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*[-*]?\s*`?(\S+/\d+)`?:\s*(usable|fragment)\b:?\s*(.*)$", ln.strip(), re.I)
        if m:
            v[m.group(1)] = (m.group(2).lower(), m.group(3).strip())
    miss = [i for i in ids if i not in v]
    if miss:
        sys.exit(f"missing verdicts ({len(miss)}): {miss[:8]}")
    u = sum(v[i][0] == "usable" for i in ids)
    lo, hi = wilson(u, len(ids))
    L = [f"One fresh reader, given only the Do not say sections of the 14 writer's views, marked each entry usable by a "
         f"writer as it stands, or a fragment, with a reason.\n",
         f"- **Usable: {u}/{len(ids)} = {u / len(ids):.1%}** (Wilson {lo:.1%} to {hi:.1%}), against the target of at "
         f"least 90%.", "", "| Note | Entries | Usable |", "|---|---|---|"]
    per = Counter(i.split("/")[0] for i in ids)
    for n in ORDER:
        if per[n]:
            L.append(f"| {n} | {per[n]} | {sum(v[i][0] == 'usable' for i in ids if i.startswith(n + '/'))} |")
    fr = [i for i in ids if v[i][0] == "fragment"]
    L += ["", "Fragments, with the reader's reason:", ""] + [f"- {i}: {v[i][1]}" for i in fr] if fr else ["", "No fragments."]
    (D / "results.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L[:2]))


if __name__ == "__main__":
    {"prep": cmd_prep, "score": cmd_score}[sys.argv[1]]()
