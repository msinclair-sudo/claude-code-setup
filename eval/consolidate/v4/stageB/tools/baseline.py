"""Stage B, B2: re-score v3 (the new baseline) and measure the hint effect (plan.md, stage B steps 3 and 4).
The checker is frozen at B1's setup (B1b): skills/consolidate/references/checker.md and the v4 hints.

    python3 baseline.py draw       seeded stratified draw of 300 v3 entries -> baseline/sample.json,
                                   baseline/packet-1..5.md (60 entries each, with hints)
    python3 baseline.py score      after baseline/verdicts-1..5.md -> baseline/results.md
    python3 baseline.py hints      the hint subset: 100 of the 300 (60 hinted, 40 not) -> hints/subset.json,
                                   hints/packet-W2.md (with hints), hints/packet-N.md (without; for N1 and N2)
    python3 baseline.py hscore     after hints/verdicts-W2, N1, N2 (.md) -> hints/adjudicate-packet.md (no hints) and,
                                   with hints/adjudication.md, hints/results.md

Strata. The B1 and B1b planted pools (330 claims) were drawn at random, within each note, from the claims the v3
first-pass checker passed, and are excluded here. Each note is therefore split into two strata, its v3-passed claims
and the rest (do-not-say entries and v3-faulted claims); each stratum is drawn from its entries outside the pools,
and weighted back to its full size, pool members included. The estimate is a whole-note rate.
"""
import json
import math
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import v3notes  # noqa: E402
from planted import key, verdict_lines, wilson  # noqa: E402

B = HERE.parent / "baseline"
H = HERE.parent / "hints"
SEED_DRAW, SEED_ORDER, SEED_HINTS, SEED_HORDER, SEED_ADJ, SEED_BOOT = (20261032, 20261033, 20261034, 20261035,
                                                                      20261036, 20261037)
N_SAMPLE, MIN_NOTE, PER_PACKET = 300, 10, 60
N_HINTED, N_UNHINTED = 60, 40
KINDS = ("stronger", "conf", "numbers", "absent", "critic", "merged", "holds")


def stratum(r):
    return "passed" if r["type"] == "claim" and r["verdict"] == set() else "rest"


def pools():
    out = set()
    for d in ("planted", "planted2"):
        out |= set(json.loads((HERE.parent / d / "pool.json").read_text()))
    return out


def largest_remainder(total, sizes, floor=0):
    """Allocate `total` over keys in proportion to `sizes`, each at least `floor` (when its size allows)."""
    base = {k: min(floor, s) for k, s in sizes.items()}
    left = total - sum(base.values())
    room = {k: s - base[k] for k, s in sizes.items()}
    tot = sum(room.values())
    quota = {k: left * room[k] / tot if tot else 0 for k in sizes}
    alloc = {k: base[k] + min(room[k], int(quota[k])) for k in sizes}
    rest = sorted(sizes, key=lambda k: quota[k] - int(quota[k]), reverse=True)
    i = 0
    while sum(alloc.values()) < total and any(alloc[k] < sizes[k] for k in sizes):
        k = rest[i % len(rest)]
        if alloc[k] < sizes[k]:
            alloc[k] += 1
        i += 1
    return alloc


def packet(r, with_hints):
    t = "do not say" if r["type"] == "dns" else "claim"
    return f"## {key(r)} ({t})\n\n" + v3notes.block(r, with_hints) + "\n"


def cmd_draw():
    rows = v3notes.load()
    excl = pools()
    full = defaultdict(Counter)                     # note -> stratum -> full size
    avail = defaultdict(lambda: defaultdict(list))  # note -> stratum -> rows outside the pools
    for r in rows:
        full[r["note"]][stratum(r)] += 1
        if key(r) not in excl:
            avail[r["note"]][stratum(r)].append(r)
    notes = sorted(full)
    per_note = largest_remainder(N_SAMPLE, {n: sum(full[n].values()) for n in notes}, MIN_NOTE)
    rng = random.Random(SEED_DRAW)
    sample, plan = [], {}
    for n in notes:
        # within a note, proportional to the full strata, capped by what is outside the pools
        want = largest_remainder(per_note[n], {s: full[n][s] for s in ("passed", "rest")}, 1)
        for s, t in (("passed", "rest"), ("rest", "passed")):
            over = want[s] - len(avail[n][s])
            if over > 0:
                want[s] -= over
                want[t] += over
        plan[n] = {s: {"full": full[n][s], "available": len(avail[n][s]), "drawn": want[s]} for s in want}
        for s in ("passed", "rest"):
            pick = rng.sample(sorted(avail[n][s], key=lambda r: r["id"]), want[s])
            sample += [(key(r), s) for r in pick]
    random.Random(SEED_ORDER).shuffle(sample)
    B.mkdir(exist_ok=True)
    (B / "sample.json").write_text(json.dumps({"seeds": {"draw": SEED_DRAW, "order": SEED_ORDER},
                                               "strata": plan, "sample": sample}, indent=1), encoding="utf-8")
    by = {key(r): r for r in rows}
    for i in range(0, len(sample), PER_PACKET):
        part = sample[i:i + PER_PACKET]
        (B / f"packet-{i // PER_PACKET + 1}.md").write_text(
            f"# Faithfulness check: {len(part)} entries\n\n" + "".join(packet(by[k], True) for k, _ in part),
            encoding="utf-8")
    print(f"sample {len(sample)} ({dict(Counter(s for _, s in sample))}); per note "
          f"{ {n: per_note[n] for n in notes} }; hinted {sum(bool(by[k]['hints']) for k, _ in sample)}")


def baseline_verdicts(sample, d=B):
    """One checker set's verdicts: d = B (the first checker per packet) or B / "second"."""
    v = {}
    for f in sorted(d.glob("verdicts-*.md")):
        v.update(verdict_lines(f))
    miss = [k for k, _ in sample if k not in v]
    if miss:
        sys.exit(f"no verdict for {len(miss)}: {miss[:5]}")
    return v


def weighted(sample_rows, plan, test):
    """The whole-note rate of entries for which test(verdict) holds, strata weighted to their full sizes."""
    num = den = 0
    cells = defaultdict(list)
    for k, s, n, ver in sample_rows:
        cells[(n, s)].append(test(ver))
    for (n, s), xs in cells.items():
        num += plan[n][s]["full"] * sum(xs) / len(xs)
    den = sum(c["full"] for n in plan for s, c in plan[n].items() if c["drawn"])
    # a stratum with nothing drawn (none outside the pools) is left out of numerator and denominator alike
    return num / den


def boot(sample_rows, plan, test, reps=10000):
    rng = random.Random(SEED_BOOT)
    cells = defaultdict(list)
    for x in sample_rows:
        cells[(x[2], x[1])].append(x)
    out = []
    for _ in range(reps):
        rs = [rng.choice(xs) for xs in cells.values() for _ in xs]
        out.append(weighted(rs, plan, test))
    out.sort()
    return out[int(0.025 * reps)], out[int(0.975 * reps) - 1]


def cmd_score():
    s = json.loads((B / "sample.json").read_text())
    plan, sample = s["strata"], s["sample"]
    v1 = baseline_verdicts(sample)
    two = bool(list((B / "second").glob("verdicts-*.md")))
    v2 = baseline_verdicts(sample, B / "second") if two else {}
    v = {k: v1[k] | v2.get(k, set()) for k in v1}            # the measurement: a fault from either checker counts
    rows = {key(r): r for r in v3notes.load()}
    sr = [(k, st, k.split("/")[0], v[k]) for k, st in sample]
    faulted = lambda ver: bool(ver)
    k_f = sum(bool(x[3]) for x in sr)
    lo, hi = wilson(k_f, len(sr))
    w = weighted(sr, plan, faulted)
    wl, wh = boot(sr, plan, faulted)
    v3 = sum(bool(r["verdict"]) for r in rows.values())
    L = ["# B2: the re-scored v3 baseline\n",
         f"Checking procedure (frozen): checker.md and hints as at 7b5a0b3; 60-entry packets; "
         f"{'two fresh checkers per packet, a fault from either counted' if two else 'one fresh checker per packet'}. "
         f"{len(sr)} entries, seeds draw {SEED_DRAW}, order {SEED_ORDER}, bootstrap {SEED_BOOT} (10,000 resamples "
         f"within note and stratum).\n",
         "## First-pass fault rate\n",
         f"- **Re-scored v3, whole-note estimate (strata weighted): {w:.1%} (bootstrap 95% {wl:.1%} to {wh:.1%}).**",
         f"- In the sample, unweighted: {k_f}/{len(sr)} = {k_f / len(sr):.1%} (Wilson {lo:.1%} to {hi:.1%}).",
         f"- v3 as reported (its own first-pass checkers, all {len(rows)} entries): {v3}/{len(rows)} = "
         f"{v3 / len(rows):.1%}.", ""]
    if two:
        s1 = [(k, st, k.split("/")[0], v1[k]) for k, st in sample]
        s2 = [(k, st, k.split("/")[0], v2[k]) for k, st in sample]
        agree_n = sum(bool(v1[k]) == bool(v2[k]) for k, _ in sample)
        L += [f"- Each checker set alone (whole-note estimate): first {weighted(s1, plan, faulted):.1%}, second "
              f"{weighted(s2, plan, faulted):.1%}. In the sample: first {sum(bool(x[3]) for x in s1)}, second "
              f"{sum(bool(x[3]) for x in s2)}, either {k_f}, both {sum(bool(v1[k]) and bool(v2[k]) for k, _ in sample)}.",
              f"- The two checkers agree (ok against fault) on {agree_n} of {len(sample)} entries.", "",
              "| Packet | First checker | Second checker | Either | Agree |", "|---|---|---|---|---|"]
        for i in range(0, len(sample), PER_PACKET):
            ks = [k for k, _ in sample[i:i + PER_PACKET]]
            L.append(f"| {i // PER_PACKET + 1} | {sum(bool(v1[k]) for k in ks)} | {sum(bool(v2[k]) for k in ks)} | "
                     f"{sum(bool(v[k]) for k in ks)} | {sum(bool(v1[k]) == bool(v2[k]) for k in ks)} |")
        L.append("")
    L += [
         "## Per 100 entries, by fault kind (whole-note estimate, bootstrap 95%)\n",
         "| Kinds | Per 100 | 95% interval | In the sample |", "|---|---|---|---|"]
    for name, ks in (("holds + absent", {"holds", "absent"}), ("stronger + numbers", {"stronger", "numbers"}),
                     ("conf", {"conf"}), ("critic", {"critic"}), ("merged", {"merged"})):
        t = lambda ver, ks=ks: bool(ver & ks)
        a, b = boot(sr, plan, t)
        L.append(f"| {name} | {100 * weighted(sr, plan, t):.1f} | {100 * a:.1f} to {100 * b:.1f} | "
                 f"{sum(t(x[3]) for x in sr)} |")
    L += ["", "## By note and stratum\n",
          "| Note | Entries | Passed by v3: full, drawn, faulted | Rest: full, drawn, faulted | Note estimate |",
          "|---|---|---|---|---|"]
    for n in sorted(plan):
        cell = {}
        for st in ("passed", "rest"):
            xs = [x for x in sr if x[2] == n and x[1] == st]
            cell[st] = f"{plan[n][st]['full']}, {len(xs)}, {sum(bool(x[3]) for x in xs)}"
        xs = [x for x in sr if x[2] == n]
        L.append(f"| {n} | {sum(c['full'] for c in plan[n].values())} | {cell['passed']} | {cell['rest']} | "
                 f"{weighted(xs, {n: plan[n]}, faulted):.0%} |")
    L += ["", "## Faults on entries the v3 checker passed, and on those it faulted\n"]
    for st, label in (("passed", "v3 passed"), ("rest", "the rest (do-not-say and v3-faulted)")):
        xs = [x for x in sr if x[1] == st]
        L.append(f"- {label}: {sum(bool(x[3]) for x in xs)}/{len(xs)} faulted now")
    vf = [x for x in sr if rows[x[0]]["verdict"]]
    L.append(f"- of v3-faulted entries in the sample, faulted again: {sum(bool(x[3]) for x in vf)}/{len(vf)}")
    L += ["", "## Every `stronger` and `numbers` fault (gate B, criterion 3)\n", "| Entry | Kinds | Checker's reason |",
          "|---|---|---|"]
    reasons = defaultdict(list)
    for f in sorted(B.glob("verdicts-*.md")) + sorted((B / "second").glob("verdicts-*.md")):
        for ln in f.read_text(encoding="utf-8").splitlines():
            ln = ln.strip().lstrip("-* ").replace("`", "")
            k = ln.split(":", 1)[0]
            if k in v and ln.split(":", 1)[1].strip() != "ok":
                reasons[k].append(ln.split(":", 1)[1].strip())
    reasons = {k: " / ".join(x) for k, x in reasons.items()}
    for x in sorted(sr):
        if x[3] & {"stronger", "numbers"}:
            L.append(f"| {x[0]} | {', '.join(sorted(x[3]))} | {reasons.get(x[0], '').replace('|', '/')} |")
    L += ["", "## Kinds in the sample\n", ", ".join(f"{k} {c}" for k, c in
                                                   Counter(k for x in sr for k in x[3]).most_common())]
    (B / "results.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L[:12]))


def cmd_hints():
    s = json.loads((B / "sample.json").read_text())
    rows = {key(r): r for r in v3notes.load()}
    keys = [k for k, _ in s["sample"]]
    rng = random.Random(SEED_HINTS)
    hinted = sorted(k for k in keys if rows[k]["hints"])
    plain = sorted(k for k in keys if not rows[k]["hints"])
    sub = rng.sample(hinted, min(N_HINTED, len(hinted))) + rng.sample(plain, min(N_UNHINTED, len(plain)))
    random.Random(SEED_HORDER).shuffle(sub)
    H.mkdir(exist_ok=True)
    (H / "subset.json").write_text(json.dumps({"seeds": {"subset": SEED_HINTS, "order": SEED_HORDER},
                                               "subset": sub}, indent=1), encoding="utf-8")
    head = f"# Faithfulness check: {len(sub)} entries\n\n"
    (H / "packet-W2.md").write_text(head + "".join(packet(rows[k], True) for k in sub), encoding="utf-8")
    (H / "packet-N.md").write_text(head + "".join(packet(rows[k], False) for k in sub), encoding="utf-8")
    print(f"subset {len(sub)}: hinted {sum(bool(rows[k]['hints']) for k in sub)}, not {sum(not rows[k]['hints'] for k in sub)}")


def agree(a, b, ks):
    return sum(bool(a[k]) == bool(b[k]) for k in ks)


def cmd_hscore():
    sub = json.loads((H / "subset.json").read_text())["subset"]
    s = json.loads((B / "sample.json").read_text())
    rows = {key(r): r for r in v3notes.load()}
    v = {"W1": {k: x for k, x in baseline_verdicts(s["sample"]).items() if k in sub}}
    for n in ("W2", "N1", "N2"):
        v[n] = verdict_lines(H / f"verdicts-{n}.md")
        miss = [k for k in sub if k not in v[n]]
        if miss:
            sys.exit(f"{n}: no verdict for {len(miss)}: {miss[:5]}")
    runs = ("W1", "W2", "N1", "N2")
    disc = [k for k in sub if len({bool(v[n][k]) for n in runs}) > 1]
    order = disc[:]
    random.Random(SEED_ADJ).shuffle(order)
    (H / "adjudicate-packet.md").write_text(
        f"# Faithfulness check: {len(order)} entries\n\n" + "".join(packet(rows[k], False) for k in order),
        encoding="utf-8")
    adj_f = H / "adjudication.md"
    if not adj_f.exists():
        print(f"discordant {len(disc)} of {len(sub)} -> hints/adjudicate-packet.md")
        return
    adj = verdict_lines(adj_f)
    hinted = [k for k in sub if rows[k]["hints"]]
    plain = [k for k in sub if not rows[k]["hints"]]
    L = ["# B2: the hint effect\n",
         f"100 of the 300 baseline entries ({len(hinted)} with a hint line, {len(plain)} without), seeds subset "
         f"{SEED_HINTS}, order {SEED_HORDER}, adjudication order {SEED_ADJ}. W1 is the baseline checker's verdict; W2 a "
         "fresh checker with hints; N1 and N2 fresh checkers without hints, packets identical apart from the hint "
         "lines. Agreement is on ok against fault.\n",
         "## Agreement\n", "| Pair | All 100 | Hinted | Not hinted |", "|---|---|---|---|"]
    for a, b in (("W1", "W2"), ("N1", "N2"), ("W1", "N1"), ("W1", "N2"), ("W2", "N1"), ("W2", "N2")):
        L.append(f"| {a} and {b} | {agree(v[a], v[b], sub)} | {agree(v[a], v[b], hinted)}/{len(hinted)} | "
                 f"{agree(v[a], v[b], plain)}/{len(plain)} |")
    L += ["", "## Fault rates by run\n", "| Run | All | Hinted | Not hinted | Kinds |", "|---|---|---|---|---|"]
    for n in runs:
        f = lambda ks: sum(bool(v[n][k]) for k in ks)
        L.append(f"| {n} | {f(sub)}/{len(sub)} | {f(hinted)}/{len(hinted)} | {f(plain)}/{len(plain)} | "
                 f"{', '.join(f'{k} {c}' for k, c in Counter(x for k in sub for x in v[n][k]).most_common())} |")
    L += ["", f"## Discordant entries ({len(disc)}), with the adjudicator's reading (no hints, blind to condition)\n",
          "| Entry | Hint | W1 | W2 | N1 | N2 | Adjudicator |", "|---|---|---|---|---|---|---|"]
    fmt = lambda x: ", ".join(sorted(x)) if x else "ok"
    tally = Counter()
    for k in sorted(disc):
        a = adj.get(k, {"?"})
        for n in runs:
            c = n[0]
            if v[n][k] and not a:
                tally[(c, "faulted, adjudicator ok")] += 1
            elif not v[n][k] and a:
                tally[(c, "passed, adjudicator fault")] += 1
        L.append(f"| {k} | {'yes' if rows[k]['hints'] else ''} | " + " | ".join(fmt(v[n][k]) for n in runs) +
                 f" | {fmt(a)} |")
    L += ["", "## On the discordant entries, runs against the adjudicator (summed over each condition's two runs)\n",
          "| | With hints (W1, W2) | Without (N1, N2) |", "|---|---|---|"]
    for what in ("faulted, adjudicator ok", "passed, adjudicator fault"):
        L.append(f"| {what} | {tally[('W', what)]} | {tally[('N', what)]} |")
    (H / "results.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    {"draw": cmd_draw, "score": cmd_score, "hints": cmd_hints, "hscore": cmd_hscore}[sys.argv[1]]()
