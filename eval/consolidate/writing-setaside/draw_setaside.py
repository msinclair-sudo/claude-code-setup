"""The writing-stage set-aside (criteria.md): six units drawn by seed from the unseen pool, metadata only.
Usage: python3 draw_setaside.py ../heldout/frame.tsv ../heldout/draw.md > setaside.md"""
import csv
import random
import re
import sys

SEED = 20261024
TAKE = {3: 2, 6: 1, 7: 2, 8: 1}
PREFER = re.compile(r"soil|microb|bacteri|archae|fung|16s|metagenom|genom|gene|nitrogen|denitrif|taxonom|communit",
                    re.I)
NAMES = {3: "Critiqued, numbered citations (research workflow)", 6: "Uncritiqued, with an answers section",
         7: "Uncritiqued harness note", 8: "Uncritiqued, no answers section"}

drawn = set(re.findall(r"\*\*DRAWN\*\* (.+?\.md)", open(sys.argv[2], encoding="utf-8").read()))
rows = [r for r in csv.DictReader(open(sys.argv[1], encoding="utf-8", newline=""), delimiter="\t")
        if not r["excluded"].strip() and r["path"] not in drawn]


def unit(r):
    return re.sub(r"[_ -]part\d+$", "", r["path"].rsplit("/", 1)[-1].removesuffix(".md"), flags=re.I).lower()


def category(r):  # as heldout/draw.py
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


units = {}
for r in rows:
    units.setdefault((category(r), unit(r)), []).append(r)
rng = random.Random(SEED)
print(f"# Writing-stage set-aside (seed {SEED})\n\nPool after excluding development, read and v3 held-out notes: "
      f"{len(units)} units.\n")
for c in sorted(TAKE):
    members = sorted((k for k in units if k[0] == c), key=lambda k: units[k][0]["path"])
    pref = [k for k in members if PREFER.search(units[k][0]["path"].rsplit("/", 1)[-1])]
    pool = pref if len(pref) >= TAKE[c] else members
    pick = rng.sample(pool, TAKE[c])
    print(f"## {c}. {NAMES[c]}: {TAKE[c]} of {len(members)} "
          f"({'from the ' + str(len(pref)) + ' with soil or microbiology titles' if pool is pref else 'from all'})\n")
    for k in pick:
        rs = units[k]
        print(f"- {' + '.join(r['path'] for r in rs)} ({sum(int(r['words']) for r in rs)} words)")
    print()
