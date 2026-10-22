"""Stage B, B1: the planted-fault test (plan.md, stage B step 2). Scripted steps; the agents' steps sit between them.

    python3 planted.py pool        seeded draw of about 130 v3 claims the first-pass checker passed -> planted/pool.json,
                                   planted/screen-packets.md (no hints: the screener checks they are clean)
    python3 planted.py clean       after planted/screen-verdicts.md: the clean claims, in seeded order, with their cited
                                   text -> planted/planter-input.md
    python3 planted.py assign      after planted/applicable.json (the planter: which edit types fit each claim):
                                   edit types by seed, to the quotas -> planted/assign.json, planted/planter-edits-input.md
    python3 planted.py judge       after planted/edits.json and planted/validated.json: planted and control claims in
                                   seeded order, hints recomputed -> planted/judge-packets.md, planted/key.json (sealed)
    python3 planted.py score       after planted/judge-1.md and judge-2.md -> planted/results.md
"""
import json
import math
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import v3notes  # noqa: E402

OUT = HERE.parent / "planted"
SEED_POOL, SEED_ASSIGN, SEED_JUDGE = 20261025, 20261026, 20261027
POOL = 130
QUOTA = {"hedge": 20, "counter": 20, "setting": 8, "number": 8, "standing": 8}
INTENDED = {"hedge": {"stronger"}, "counter": {"stronger"}, "setting": {"holds", "absent"},
            "number": {"numbers"}, "standing": {"stronger", "conf"}}
KINDS = ("stronger", "conf", "numbers", "absent", "critic", "merged", "holds")


def key(r):
    return f"{r['note']}/{r['id']}"


def rows_by_key():
    return {key(r): r for r in v3notes.load()}


def packet_entry(k, r, with_hints, entry=None):
    rr = dict(r)
    if entry is not None:
        rr["entry"] = entry
        rr["hints"] = v3notes.kn4.hints(entry, r["cited"], r["bib"])
    return f"## {k}\n\n" + v3notes.block(rr, with_hints) + "\n"


def wilson(k, n, z=1.96):
    if not n:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def verdict_lines(path):
    out = {}
    for ln in Path(path).read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*[-*]?\s*`?([A-Za-z0-9-]+/[A-Za-z0-9][A-Za-z0-9-]*\.[A-Za-z0-9]+)`?:\s*(.*)$", ln.strip())
        if not m:
            continue
        rest = m.group(2).strip()
        if re.match(r"ok\b", rest, re.I):
            out[m.group(1)] = set()
        else:
            head = rest.split(":", 1)[0].lower()
            out[m.group(1)] = {x for x in re.split(r"[\s,/+]+", head) if x in KINDS} or {"other"}
    return out


def cmd_pool():
    rows = [r for r in v3notes.load() if r["type"] == "claim" and r["verdict"] == set()]
    by = defaultdict(list)
    for r in rows:
        by[r["note"]].append(r)
    total = len(rows)
    alloc = {n: max(4, round(POOL * len(v) / total)) for n, v in by.items()}
    while sum(alloc.values()) > POOL:                      # trim the largest allocations to the pool size
        alloc[max(alloc, key=alloc.get)] -= 1
    rng = random.Random(SEED_POOL)
    pick = []
    for n in sorted(by):
        pick += rng.sample(sorted(by[n], key=lambda r: r["id"]), min(alloc[n], len(by[n])))
    OUT.mkdir(exist_ok=True)
    (OUT / "pool.json").write_text(json.dumps([key(r) for r in pick], indent=1), encoding="utf-8")
    (OUT / "screen-packets.md").write_text(
        f"# Screening packet: {len(pick)} claims\n\n" + "".join(packet_entry(key(r), r, False) for r in pick),
        encoding="utf-8")
    print(f"pool {len(pick)} of {total} passed claims; per note {dict(Counter(r['note'] for r in pick))}")


def clean_keys():
    pool = json.loads((OUT / "pool.json").read_text())
    ver = verdict_lines(OUT / "screen-verdicts.md")
    missing = [k for k in pool if k not in ver]
    if missing:
        sys.exit(f"screen verdicts missing for {len(missing)}: {missing[:5]}")
    return [k for k in pool if ver[k] == set()], [k for k in pool if ver[k]]


def cmd_clean():
    clean, faulted = clean_keys()
    rows = rows_by_key()
    order = clean[:]
    random.Random(SEED_POOL + 1).shuffle(order)
    (OUT / "clean.json").write_text(json.dumps({"clean": order, "set_aside": faulted}, indent=1), encoding="utf-8")
    (OUT / "planter-input.md").write_text(
        f"# Clean claims ({len(order)}), in seeded order\n\n" + "".join(packet_entry(k, rows[k], False) for k in order),
        encoding="utf-8")
    print(f"clean {len(order)}, set aside {len(faulted)}")


def cmd_assign():
    order = json.loads((OUT / "clean.json").read_text())["clean"]
    app = json.loads((OUT / "applicable.json").read_text())       # {claim key: [types that fit]}
    rng = random.Random(SEED_ASSIGN)
    assign, left = {}, dict(QUOTA)
    # scarcest type first, so that it is not starved by the commoner ones
    for t in sorted(QUOTA, key=lambda t: sum(t in app.get(k, []) for k in order)):
        cands = [k for k in order if t in app.get(k, []) and k not in assign]
        rng.shuffle(cands)
        for k in cands[:left[t]]:
            assign[k] = t
            left[t] -= 1
    controls = [k for k in order if k not in assign]
    (OUT / "assign.json").write_text(json.dumps({"plants": assign, "controls": controls, "short": left}, indent=1),
                                     encoding="utf-8")
    rows = rows_by_key()
    (OUT / "planter-edits-input.md").write_text(
        "# Claims to edit, one edit each, of the type named\n\n" +
        "".join(f"**Edit type: {assign[k]}**\n\n" + packet_entry(k, rows[k], False) for k in assign), encoding="utf-8")
    print(f"assigned {Counter(assign.values())}; short {left}; controls {len(controls)}")


def cmd_judge():
    a = json.loads((OUT / "assign.json").read_text())
    edits = json.loads((OUT / "edits.json").read_text())           # {key: {statement, fields: {changed}, ...}}
    valid = json.loads((OUT / "validated.json").read_text())       # {key: true/false}
    rows = rows_by_key()
    items = []
    for k, t in a["plants"].items():
        if k in edits and valid.get(k) is True:
            e = json.loads(json.dumps(rows[k]["entry"]))
            e["statement"] = edits[k].get("statement", e["statement"])
            e["fields"].update(edits[k].get("fields", {}))
            items.append((k, t, e))
    items += [(k, "control", None) for k in a["controls"]]
    random.Random(SEED_JUDGE).shuffle(items)
    keymap = {k: {"type": t, "hint": bool((v3notes.kn4.hints(e, rows[k]["cited"], rows[k]["bib"]) if e is not None
                                           else rows[k]["hints"]))} for k, t, e in items}
    (OUT / "key.json").write_text(json.dumps(keymap, indent=1), encoding="utf-8")
    (OUT / "judge-packets.md").write_text(
        f"# Faithfulness check: {len(items)} claims\n\n" + "".join(packet_entry(k, rows[k], True, e) for k, t, e in items),
        encoding="utf-8")
    print(f"judge packet: {len(items)} claims ({Counter(t for _, t, _ in items)})")


def cmd_score():
    keymap = json.loads((OUT / "key.json").read_text())
    j = [verdict_lines(OUT / f"judge-{n}.md") for n in (1, 2)]
    for n, v in enumerate(j, 1):
        miss = [k for k in keymap if k not in v]
        if miss:
            print(f"judge {n}: no verdict for {len(miss)}: {miss[:5]}")
    lines = ["| Edit type | Planted | Judge 1 caught | Judge 2 caught | Either | Both | Intended kind (either) | "
             "With a hint | Caught by either, 95% CI |\n|---|---|---|---|---|---|---|---|---|\n"]
    for t in list(QUOTA) + ["control"]:
        ks = [k for k, v in keymap.items() if v["type"] == t]
        if not ks:
            continue
        c1 = sum(bool(j[0].get(k)) for k in ks)
        c2 = sum(bool(j[1].get(k)) for k in ks)
        ei = sum(bool(j[0].get(k)) or bool(j[1].get(k)) for k in ks)
        bo = sum(bool(j[0].get(k)) and bool(j[1].get(k)) for k in ks)
        it = sum(bool((j[0].get(k, set()) | j[1].get(k, set())) & INTENDED.get(t, set())) for k in ks)
        hi = sum(keymap[k]["hint"] for k in ks)
        lo, up = wilson(ei, len(ks))
        name = "Controls (unedited): faulted" if t == "control" else t
        lines.append(f"| {name} | {len(ks)} | {c1} | {c2} | {ei} | {bo} | {'' if t == 'control' else it} | {hi} | "
                     f"{ei}/{len(ks)} = {ei / len(ks):.0%} ({lo:.0%} to {up:.0%}) |\n")
    detail = ["\n| Claim | Type | Hint | Judge 1 | Judge 2 |\n|---|---|---|---|---|\n"]
    for k, v in sorted(keymap.items(), key=lambda x: (x[1]["type"], x[0])):
        f = lambda s: ", ".join(sorted(s)) if s else "ok"
        detail.append(f"| {k} | {v['type']} | {'yes' if v['hint'] else ''} | {f(j[0].get(k, {'?'}))} | "
                      f"{f(j[1].get(k, {'?'}))} |\n")
    (OUT / "scores.md").write_text("".join(lines + detail), encoding="utf-8")
    print("".join(lines))


if __name__ == "__main__":
    {"pool": cmd_pool, "clean": cmd_clean, "assign": cmd_assign, "judge": cmd_judge, "score": cmd_score}[sys.argv[1]]()
