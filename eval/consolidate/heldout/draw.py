"""The held-out draw (criteria.md): categories from the frame's detected features, one note per category,
random.Random(20261022). Usage: python3 draw.py frame.tsv > draw.md"""
import csv
import random
import re
import sys

SEED = 20261022
rows = [r for r in csv.DictReader(open(sys.argv[1]), delimiter="\t") if not r["excluded"]]


def unit(r):
    """Parts of one research set are one unit (Slice1_part1, Slice1_part2)."""
    return re.sub(r"[_ -]part\d+$", "", r["path"].rsplit("/", 1)[-1].removesuffix(".md"), flags=re.I).lower()


def category(r):
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


NAMES = {1: "Critiqued, labelled citations with standing", 2: "Critiqued, labelled citations without standing",
         3: "Critiqued, numbered citations (research workflow)", 4: "Critiqued, author-year citations (research workflow)",
         5: "Critiqued harness note", 6: "Uncritiqued, with an answers section", 7: "Uncritiqued harness note",
         8: "Uncritiqued, no answers section"}
units = {}
for r in rows:
    units.setdefault((category(r), unit(r)), []).append(r)
rng = random.Random(SEED)
print(f"# Held-out draw (seed {SEED})\n")
for c in sorted(NAMES):
    members = sorted((k for k in units if k[0] == c), key=lambda k: units[k][0]["path"])
    print(f"## {c}. {NAMES[c]} ({len(members)})\n")
    if not members:
        print("No members.\n")
        continue
    pick = rng.choice(members)
    for k in members:
        rs = units[k]
        print(f"- {'**DRAWN** ' if k == pick else ''}{' + '.join(r['path'] for r in rs)} "
              f"({sum(int(r['words']) for r in rs)} words; {rs[0]['citations']}; answers {rs[0]['answers']})")
    print()
