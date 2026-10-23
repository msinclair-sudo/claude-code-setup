"""Stage B, B1b: the omission hint confirmed on a fresh planted set (plan.md, revision 4, B1b). B1's tool and records
(planted.py, ../planted/) are untouched; this tool imports its helpers. The agents' steps sit between the commands.

    python3 planted2.py info      the omission hint's firing rate on the v3 entries, and on B1's plants (information)
    python3 planted2.py pool      seeded draw of 200 v3-passed claims, excluding B1's pool -> planted2/pool.json,
                                  planted2/screen-packets.md (no hints)
    python3 planted2.py clean     after planted2/screen-verdicts.md -> planted2/clean.json, planted2/planter-input.md
    python3 planted2.py assign    after planted2/applicable.json -> planted2/assign.json, planted2/planter-edits-input.md
    python3 planted2.py judge     after planted2/edits.json and validated.json -> judge-packets-W.md (with the omission
                                  hint), judge-packets-N.md (B1's setup), key.json (sealed)
    python3 planted2.py score     after judge-W1, W2, N1, N2 (.md) -> scores.md, adjudicate-packets.md; with
                                  adjudication.md, its readings too
"""
import json
import math
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import planted  # noqa: E402
import v3notes  # noqa: E402
from planted import key, wilson, verdict_lines  # noqa: E402

kn4 = v3notes.kn4
OUT = HERE.parent / "planted2"
B1 = HERE.parent / "planted"
SEED_POOL, SEED_ASSIGN, SEED_JUDGE, SEED_CONTROLS = 20261028, 20261029, 20261030, 20261031
POOL = 200
CONTROLS = 45
QUOTA = {"scope": 24, "counter": 12, "hedge": 8, "setting": 4, "number": 4, "standing": 4}
OMISSION = ("scope", "counter", "hedge")
INTENDED = {"scope": {"stronger"}, "counter": {"stronger"}, "hedge": {"stronger"}, "setting": {"holds", "absent"},
            "number": {"numbers"}, "standing": {"stronger", "conf"}}
JUDGES = {"W": ("W1", "W2"), "N": ("N1", "N2")}


def edited(r, ed):
    """The row with an edit applied, its hints recomputed by the v4 code as a real check would show them."""
    rr = dict(r)
    if ed is not None:
        e = json.loads(json.dumps(r["entry"]))
        e["statement"] = ed.get("statement", e["statement"])
        e["fields"].update(ed.get("fields", {}))
        rr["entry"] = e
        rr["hints"] = kn4.hints(e, r["cited"], r["bib"])
        rr["omit"] = v3notes.omission_hint.omission_hints(e, r["cited"])
    return rr


def visible(clean, plant):
    """An edit is hint-visible when the omission hint lists an item for the edited entry that it did not list for
    the clean one."""
    return bool(set(plant["omit"]) - set(clean["omit"]))


def packet(k, r, with_hints, omit=False):
    return f"## {k}\n\n" + v3notes.block(r, with_hints, omit) + "\n"


def cmd_info():
    rows = v3notes.load()
    claims = [r for r in rows if r["type"] == "claim"]
    fired = [r for r in claims if r["omit"]]
    passed = [r for r in claims if r["verdict"] == set()]
    out = ["# The omission hint on the v3 notes (information only; not used to tune)\n",
           f"- Claims: {len(claims)}. The hint fires on {len(fired)} ({len(fired) / len(claims):.0%}); "
           f"items per hinted claim: mean {sum(len(r['omit']) for r in fired) / max(1, len(fired)):.1f}, "
           f"capped at 8 on {sum(len(r['omit']) == 8 for r in fired)}.",
           f"- On claims the v3 checker passed: {sum(bool(r['omit']) for r in passed)} of {len(passed)}. On claims it "
           f"faulted `stronger`: {sum(bool(r['omit']) for r in claims if 'stronger' in r['verdict'])} of "
           f"{sum('stronger' in r['verdict'] for r in claims)}.", ""]
    by = {key(r): r for r in rows}
    keymap = json.loads((B1 / "key.json").read_text())
    edits = json.loads((B1 / "edits.json").read_text())
    j = [verdict_lines(B1 / f"judge-{n}.md") for n in (1, 2)]
    out.append("## B1's omission plants: would the hint have listed the dropped words? (a code check)\n")
    out.append("| Claim | Type | B1 judges | New items the hint lists for the edited entry |\n|---|---|---|---|")
    vis = Counter()
    for k, v in sorted(keymap.items()):
        if v["type"] not in ("hedge", "counter"):
            continue
        c, p = by[k], edited(by[k], edits[k])
        new = [x for x in p["omit"] if x not in c["omit"]]
        vis[(v["type"], bool(new))] += 1
        caught = sum(bool(x.get(k)) for x in j)
        out.append(f"| {k} | {v['type']} | {caught} of 2 caught | {'; '.join(new) or '(none)'} |")
    out.append("")
    out.append(f"Hint-visible: hedge {vis[('hedge', True)]} of {vis[('hedge', True)] + vis[('hedge', False)]}, "
               f"counter {vis[('counter', True)]} of {vis[('counter', True)] + vis[('counter', False)]}.")
    ctrl = [k for k, v in keymap.items() if v["type"] == "control"]
    out.append(f"B1's controls with an omission line: {sum(bool(by[k]['omit']) for k in ctrl)} of {len(ctrl)}.")
    OUT.mkdir(exist_ok=True)
    (OUT / "hint-info.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out[:4] + out[-2:]))


def cmd_pool():
    b1 = set(json.loads((B1 / "pool.json").read_text()))
    rows = [r for r in v3notes.load() if r["type"] == "claim" and r["verdict"] == set() and key(r) not in b1]
    by = defaultdict(list)
    for r in rows:
        by[r["note"]].append(r)
    total = len(rows)
    alloc = {n: min(len(v), max(4, round(POOL * len(v) / total))) for n, v in by.items()}
    while sum(alloc.values()) > POOL:
        alloc[max(alloc, key=alloc.get)] -= 1
    rng = random.Random(SEED_POOL)
    pick = []
    for n in sorted(by):
        pick += rng.sample(sorted(by[n], key=lambda r: r["id"]), alloc[n])
    OUT.mkdir(exist_ok=True)
    (OUT / "pool.json").write_text(json.dumps([key(r) for r in pick], indent=1), encoding="utf-8")
    (OUT / "screen-packets.md").write_text(
        f"# Screening packet: {len(pick)} claims\n\n" + "".join(packet(key(r), r, False) for r in pick),
        encoding="utf-8")
    print(f"pool {len(pick)} of {total} passed claims outside B1's pool; per note "
          f"{dict(Counter(r['note'] for r in pick))}")


def cmd_clean():
    pool = json.loads((OUT / "pool.json").read_text())
    ver = verdict_lines(OUT / "screen-verdicts.md")
    missing = [k for k in pool if k not in ver]
    if missing:
        sys.exit(f"screen verdicts missing for {len(missing)}: {missing[:5]}")
    clean, faulted = [k for k in pool if ver[k] == set()], [k for k in pool if ver[k]]
    random.Random(SEED_POOL + 1).shuffle(clean)
    rows = planted.rows_by_key()
    (OUT / "clean.json").write_text(json.dumps({"clean": clean, "set_aside": faulted}, indent=1), encoding="utf-8")
    (OUT / "planter-input.md").write_text(
        f"# Clean claims ({len(clean)}), in seeded order\n\n" + "".join(packet(k, rows[k], False) for k in clean),
        encoding="utf-8")
    print(f"clean {len(clean)}, set aside {len(faulted)} ({dict(Counter(x for k in faulted for x in ver[k]))})")


def cmd_assign():
    order = json.loads((OUT / "clean.json").read_text())["clean"]
    app = json.loads((OUT / "applicable.json").read_text())
    rng = random.Random(SEED_ASSIGN)
    assign, left = {}, dict(QUOTA)
    for t in sorted(QUOTA, key=lambda t: sum(t in app.get(k, []) for k in order)):     # scarcest first
        cands = [k for k in order if t in app.get(k, []) and k not in assign]
        rng.shuffle(cands)
        for k in cands[:left[t]]:
            assign[k] = t
            left[t] -= 1
    rest = [k for k in order if k not in assign]
    controls = random.Random(SEED_CONTROLS).sample(rest, min(CONTROLS, len(rest)))
    (OUT / "assign.json").write_text(json.dumps({"plants": assign, "controls": controls, "short": left,
                                                 "unused": [k for k in rest if k not in controls]}, indent=1),
                                     encoding="utf-8")
    rows = planted.rows_by_key()
    (OUT / "planter-edits-input.md").write_text(
        "# Claims to edit, one edit each, of the type named\n\n" +
        "".join(f"**Edit type: {assign[k]}**\n\n" + packet(k, rows[k], False) for k in assign), encoding="utf-8")
    print(f"applicable {dict(Counter(t for k in order for t in app.get(k, [])))}; assigned {dict(Counter(assign.values()))}; "
          f"short {left}; controls {len(controls)}")


def cmd_judge():
    a = json.loads((OUT / "assign.json").read_text())
    edits = json.loads((OUT / "edits.json").read_text())
    valid = json.loads((OUT / "validated.json").read_text())
    rows = planted.rows_by_key()
    items = [(k, t, edited(rows[k], edits[k])) for k, t in a["plants"].items() if k in edits and valid.get(k) is True]
    items += [(k, "control", rows[k]) for k in a["controls"]]
    random.Random(SEED_JUDGE).shuffle(items)
    keymap = {k: {"type": t, "hint": bool(r["hints"]), "omit": bool(r["omit"]),
                  "visible": t in OMISSION and visible(rows[k], r)} for k, t, r in items}
    (OUT / "key.json").write_text(json.dumps(keymap, indent=1), encoding="utf-8")
    head = f"# Faithfulness check: {len(items)} claims\n\n"
    (OUT / "judge-packets-W.md").write_text(head + "".join(packet(k, r, True, True) for k, t, r in items),
                                            encoding="utf-8")
    (OUT / "judge-packets-N.md").write_text(head + "".join(packet(k, r, True, False) for k, t, r in items),
                                            encoding="utf-8")
    print(f"judge packets: {len(items)} claims ({dict(Counter(t for _, t, _ in items))}); with an omission line "
          f"{sum(v['omit'] for v in keymap.values())}; omission plants hint-visible "
          f"{sum(v['visible'] for v in keymap.values())} of {sum(v['type'] in OMISSION for v in keymap.values())}")


def mcnemar(b, c):
    """Exact two-sided McNemar p for b and c discordant pairs."""
    n = b + c
    if not n:
        return 1.0
    return min(1.0, 2 * sum(math.comb(n, i) for i in range(min(b, c) + 1)) / 2 ** n)


def cmd_score():
    keymap = json.loads((OUT / "key.json").read_text())
    v = {}
    for js in JUDGES.values():
        for name in js:
            v[name] = verdict_lines(OUT / f"judge-{name}.md")
            miss = [k for k in keymap if k not in v[name]]
            if miss:
                print(f"{name}: no verdict for {len(miss)}: {miss[:5]}")
    caught = lambda name, k: bool(v[name].get(k))
    either = lambda c, k: any(caught(n, k) for n in JUDGES[c])
    groups = list(QUOTA) + ["omissions", "control"]
    members = lambda g: [k for k, x in keymap.items() if (x["type"] in OMISSION if g == "omissions" else x["type"] == g)]
    pct = lambda a, n: f"{a}/{n} = {a / n:.0%} ({wilson(a, n)[0]:.0%} to {wilson(a, n)[1]:.0%})" if n else "-"
    L = ["## Catch rates by condition (W: with the omission hint; N: without, B1's setup)\n",
         "| Edit type | n | Hint-visible | W1 | W2 | W either | W both | N1 | N2 | N either | N both | Intended kind, "
         "W / N (either) |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for g in groups:
        ks = members(g)
        if not ks:
            continue
        n = len(ks)
        cell = lambda name: str(sum(caught(name, k) for k in ks))
        ei = {c: sum(either(c, k) for k in ks) for c in JUDGES}
        bo = {c: sum(all(caught(x, k) for x in JUDGES[c]) for k in ks) for c in JUDGES}
        it = {c: sum(bool(set().union(*(v[x].get(k, set()) for x in JUDGES[c])) & INTENDED.get(keymap[k]["type"], set()))
                     for k in ks) for c in JUDGES}
        name = "**Controls (unedited): faulted**" if g == "control" else ("**Omissions, pooled**" if g == "omissions" else g)
        vis = "" if g in ("control", "setting", "number", "standing") else str(sum(keymap[k]["visible"] for k in ks))
        L.append(f"| {name} | {n} | {vis} | {cell('W1')} | {cell('W2')} | {pct(ei['W'], n)} | {bo['W']} | "
                 f"{cell('N1')} | {cell('N2')} | {pct(ei['N'], n)} | {bo['N']} | "
                 f"{'' if g == 'control' else str(it['W']) + ' / ' + str(it['N'])} |")
    om, ct = members("omissions"), members("control")
    sumj = lambda c, ks: sum(caught(x, k) for x in JUDGES[c] for k in ks)
    L += ["", "## Paired, with versus without (judge-pair either)\n", "| | Only W | Only N | Both | Neither | "
          "Exact McNemar p |", "|---|---|---|---|---|---|"]
    for label, ks in (("Omission plants caught", om), ("Hint-visible omission plants caught",
                                                        [k for k in om if keymap[k]["visible"]]),
                      ("Controls faulted", ct)):
        b = sum(either("W", k) and not either("N", k) for k in ks)
        c = sum(either("N", k) and not either("W", k) for k in ks)
        both = sum(either("W", k) and either("N", k) for k in ks)
        L.append(f"| {label} | {b} | {c} | {both} | {len(ks) - b - c - both} | {mcnemar(b, c):.2f} |")
    # the decision rule, fixed before drawing (plan.md, revision 4, B1b)
    wo, no = sumj("W", om), sumj("N", om)
    wc, nc = sumj("W", ct), sumj("N", ct)
    per = {x: sum(caught(x, k) for k in ct) for x in JUDGES["W"]}
    noisy = wc - nc >= 3 or any(per[x] > 0.05 * len(ct) for x in per)
    verdict = ("NOT ADOPTED, STOP: noticeably more false alarms" if noisy else
               "ADOPT" if wo > no else "NOT ADOPTED: no gain in omissions caught")
    L += ["", "## Decision rule (fixed before drawing)\n",
          f"- Omission catches summed over each condition's two judges: W {wo}, N {no} (of {2 * len(om)}).",
          f"- Control faults summed over two judges: W {wc}, N {nc} (of {2 * len(ct)}); W per judge "
          f"{', '.join(f'{x} {per[x]}' for x in per)} (5% of {len(ct)} is {0.05 * len(ct):.2f}).",
          f"- **{verdict}.**"]
    L += ["", "## Every claim\n", "| Claim | Type | Old hint | Omission line | Visible | W1 | W2 | N1 | N2 |",
          "|---|---|---|---|---|---|---|---|---|"]
    f = lambda s: ", ".join(sorted(s)) if s else "ok"
    for k, x in sorted(keymap.items(), key=lambda y: (y[1]["type"], y[0])):
        L.append(f"| {k} | {x['type']} | {'yes' if x['hint'] else ''} | {'yes' if x['omit'] else ''} | "
                 f"{'yes' if x['visible'] else ''} | " + " | ".join(f(v[n].get(k, {'?'})) for n in ("W1", "W2", "N1", "N2")) + " |")
    faulted = [k for k in ct if either("W", k) or either("N", k)]
    rows = planted.rows_by_key()
    (OUT / "adjudicate-packets.md").write_text(
        f"# Faithfulness check: {len(faulted)} claims\n\n" + "".join(packet(k, rows[k], False) for k in faulted),
        encoding="utf-8")
    adj = OUT / "adjudication.md"
    if adj.exists():
        a = verdict_lines(adj)
        L += ["", "## Controls faulted by any judge: the adjudicator's reading (information only)\n",
              "| Control | Faulted by | Adjudicator |", "|---|---|---|"]
        for k in faulted:
            by = ", ".join(n for n in ("W1", "W2", "N1", "N2") if caught(n, k))
            L.append(f"| {k} | {by} | {f(a.get(k, {'?'}))} |")
    (OUT / "scores.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L[:L.index("## Every claim\n")]))


if __name__ == "__main__":
    {"info": cmd_info, "pool": cmd_pool, "clean": cmd_clean, "assign": cmd_assign, "judge": cmd_judge,
     "score": cmd_score}[sys.argv[1]]()
