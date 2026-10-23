"""Stage C usability topics (heldout/criteria.md, "The usability re-test"): three distinct drawn notes, one per slot,
soil or microbiology titles preferred, random.Random(20261041).choice per slot.

    python3 topics.py       heldout/draw.md -> usability/topics.md
"""
import re
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
S = HERE.parent
SEED = 20261041
PREFER = re.compile(r"soil|microb|bacteri|archae|fung|16s|metagenom|genom|gene|nitrogen|denitrif|taxonom|communit",
                    re.I)
SLOTS = [("critiqued", {1, 2, 3, 4}), ("harness", {7}), ("uncritiqued", {6, 8})]


def drawn():
    """[(category, path, size hint)] from draw.md."""
    out, cat = [], None
    for ln in (S / "heldout" / "draw.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"## (\d+)\.", ln)
        if m:
            cat = int(m.group(1))
        m = re.match(r"- \*\*DRAWN\*\* (.+?\.md(?: \+ .+?\.md)*) \(.*size ([^)]*)\)$", ln)
        if m:
            out.append((cat, m.group(1), m.group(2)))
    return out


def main():
    rows = drawn()
    ids = {}
    for ln in (S / "state.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"\| (C-[A-Z]+) \| \d \| `(.+?)` \|", ln)
        if m:
            ids[m.group(2)] = m.group(1)
    rng = random.Random(SEED)
    L = [f"# Stage C usability topics (seed {SEED})\n", "Rule: `../heldout/criteria.md`, \"The usability re-test\".\n"]
    used = set()
    for k, (slot, cats) in enumerate(SLOTS, 1):
        members = sorted(r for r in rows if r[0] in cats and r[1] not in used)
        if slot == "harness" and not members:
            members = sorted(r for r in rows if r[2] == "standard" and r[1] not in used)
        pref = [r for r in members if PREFER.search(r[1].rsplit("/", 1)[-1])]
        pool = pref or members
        pick = rng.choice(sorted(pool, key=lambda r: r[1]))
        used.add(pick[1])
        L += [f"## T{k}: {slot}\n",
              f"- Chosen: **{ids.get(pick[1], '?')}**, category {pick[0]}: `{pick[1]}`",
              f"- From {len(pool)} of {len(members)} ({'soil or microbiology titles' if pref else 'all; none matched'}): "
              + "; ".join(ids.get(r[1], r[1]) for r in sorted(pool, key=lambda r: r[1])), ""]
    out = S / "usability" / "topics.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(x for x in L if x.startswith("- Chosen")))


if __name__ == "__main__":
    main()
