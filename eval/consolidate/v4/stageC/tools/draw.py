"""The stage C held-out draw (heldout/criteria.md): v3's categories from the frame's detected features, category 5
dropped, one unit per category, random.Random(20261040).

    python3 draw.py         stageC/heldout/frame.tsv -> stageC/heldout/draw.md
"""
import csv
import random
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
H = HERE.parent / "heldout"
SEED = 20261040
NAMES = {1: "Critiqued, labelled citations with standing", 2: "Critiqued, labelled citations without standing",
         3: "Critiqued, numbered citations (research workflow)", 4: "Critiqued, author-year citations (research workflow)",
         5: "Critiqued harness note", 6: "Uncritiqued, with an answers section", 7: "Uncritiqued harness note",
         8: "Uncritiqued, no answers section"}
DROPPED = {5}


def unit(r):
    """Parts of one research set are one unit (Slice1_part1, Slice1_part2)."""
    return re.sub(r"[_ -]part\d+$", "", r["path"].rsplit("/", 1)[-1].removesuffix(".md"), flags=re.I).lower()


def category(r):  # as ../../../heldout/draw.py
    crit = r["critique"].startswith("yes")
    lab = r["citations"].startswith("labelled")
    harness = r["path"].startswith("PhD/biblion")
    if crit and lab:
        return 1 if r["labels"].startswith("yes") else 2
    if crit and harness:
        return 5
    if crit and r["citations"] == "numbered":
        return 3
    if crit:
        return 4
    if harness:
        return 7
    return 6 if r["answers"] == "yes" else 8


def main():
    rows = [r for r in csv.DictReader(open(H / "frame.tsv", encoding="utf-8", newline=""), delimiter="\t")
            if not r["excluded"].strip()]
    units = {}
    for r in rows:
        units.setdefault((category(r), unit(r)), []).append(r)
    rng = random.Random(SEED)
    L = [f"# Stage C held-out draw (seed {SEED})\n", f"{len(units)} eligible units from {len(rows)} notes.\n"]
    for c in sorted(NAMES):
        members = sorted((k for k in units if k[0] == c), key=lambda k: units[k][0]["path"])
        L.append(f"## {c}. {NAMES[c]} ({len(members)})\n")
        if c in DROPPED:
            L.append("Dropped (criteria.md)." + (f" Members: {len(members)}." if members else "") + "\n")
            continue
        if not members:
            L.append("No members.\n")
            continue
        pick = rng.choice(members)
        for k in members:
            rs = units[k]
            L.append(f"- {'**DRAWN** ' if k == pick else ''}{' + '.join(r['path'] for r in rs)} "
                     f"({sum(int(r['words']) for r in rs)} words; {rs[0]['citations']}; answers {rs[0]['answers']}; "
                     f"size {rs[0]['size_hint'] or 'not given'})")
        L.append("")
    (H / "draw.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(x for x in L if x.startswith("##") or "DRAWN" in x))


if __name__ == "__main__":
    main()
