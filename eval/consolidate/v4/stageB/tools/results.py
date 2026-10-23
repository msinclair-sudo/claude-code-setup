"""Stage B, B8: the gate B report (plan.md, "Gate B: criteria", fixed at revision 3; measurement as revision 5).

    python3 results.py      after every rebuild/<NOTE>/ has its first pass and re-checks -> stageB/results.md

v4 is a census: every entry of the 14 rebuilt notes, first pass by two fresh checkers per 60-entry packet, a fault
from either counted (rebuild/<NOTE>/verdicts-a, verdicts-b). v3 is the re-scored baseline (baseline/, the same
procedure on a stratified sample of 300, weighted to whole notes). Intervals: Wilson for v4's pooled rates; the
baseline's own bootstrap (seed 20261037) for v3's; for each v4/v3 ratio a bootstrap of 10,000 resamples with seed
20261038 (fixed at B8, before scoring), resampling v3's entries within note and stratum and v4's notes as clusters.
"""
import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import baseline  # noqa: E402
import notestats  # noqa: E402
import rebuild  # noqa: E402
from planted import wilson  # noqa: E402

S = HERE.parent
R = S / "rebuild"
SEED_RATIO, REPS = 20261038, 10000
ORDER = ["16S", "H2-01", "TSL", "CB1", "CB2", "NFERT", "CB3", "GHOST", "TAXRES", "H1-RES", "H2-04", "H1-05", "H1-02",
         "H1-06"]
ALL = list(ORDER)
MEASURES = [("First-pass fault rate", lambda v: bool(v)),
            ("holds + absent", lambda v: bool(v & {"holds", "absent"})),
            ("stronger + numbers", lambda v: bool(v & {"stronger", "numbers"})),
            ("conf", lambda v: bool(v & {"conf"}))]


def v4_note(n):
    """[(id, union kinds, reasons)] in packet order for one rebuilt note."""
    d = R / n
    a, b = {}, {}
    for side, store in (("a", a), ("b", b)):
        for f in sorted((d / f"verdicts-{side}").glob("packet-*.md")):
            store.update(rebuild.read(f))
    out = []
    for _, ids in rebuild.packet_ids(d):
        for i in ids:
            out.append((i, a[i][0] | b[i][0], [x[1] for x in (a[i], b[i]) if x[0]]))
    return out


def v3_rows():
    s = json.loads((baseline.B / "sample.json").read_text())
    v1 = baseline.baseline_verdicts(s["sample"])
    v2 = baseline.baseline_verdicts(s["sample"], baseline.B / "second")
    rows = [(k, st, k.split("/")[0], v1[k] | v2[k]) for k, st in s["sample"]]
    return rows, s["strata"]


def v3_reasons(keys):
    out = defaultdict(list)
    for f in sorted(baseline.B.glob("verdicts-*.md")) + sorted((baseline.B / "second").glob("verdicts-*.md")):
        for ln in f.read_text(encoding="utf-8").splitlines():   # baseline IDs are <NOTE>/<id>, as baseline.py reads
            ln = ln.strip().lstrip("-* ").replace("`", "")
            k, _, rest = ln.partition(":")
            if k in keys and rest.strip() != "ok":
                out[k].append(rest.strip())
    return out


def ratio_boot(v3, plan, v4, test):
    rng = random.Random(SEED_RATIO)
    cells = defaultdict(list)
    for x in v3:
        cells[(x[2], x[1])].append(x)
    notes = list(v4)
    per = {n: (sum(test(k) for _, k, _ in v4[n]), len(v4[n])) for n in notes}
    out = []
    for _ in range(REPS):
        rs = [rng.choice(xs) for xs in cells.values() for _ in xs]
        b3 = baseline.weighted(rs, plan, test)
        pick = [rng.choice(notes) for _ in notes]
        b4 = sum(per[n][0] for n in pick) / sum(per[n][1] for n in pick)
        out.append(b4 / b3 if b3 else float("inf"))
    out.sort()
    return out[int(0.025 * REPS)], out[int(0.975 * REPS) - 1]


def omission(n):
    """Criterion 4 for one note, read-only: the lint checks on each input, re-run through detect."""
    k = rebuild.kn()
    vp = R / n / "vault-path.txt"
    rel = vp.read_text(encoding="utf-8").strip() if vp.exists() else rebuild.NOTES[n]
    text = (rebuild.VAULT / rel).read_text(encoding="utf-8")
    fm = k.frontmatter(text)
    decls = k.declared_answers(fm)
    res = []
    for item in fm.get("inputs") or []:
        nid, p = (list(item.items())[0] if isinstance(item, dict) else [x.strip() for x in str(item).split(":", 1)])
        ft = k.detect(rebuild.VAULT / str(p).strip().strip('"'), nid, decls.get(nid))[0]
        bad = [s for s in ft["unaddressed sections"] if not k.SKIP_TITLE.search(s)]
        res.append((nid, ft["omission check"], ft["body addresses"], bad))
    return res


def recheck_round(n, r):
    d = R / n
    f = d / f"fixes-{r}.md"
    if not f.exists():
        return 0, 0
    ids = list(dict.fromkeys(ln.split(":", 1)[0] for ln in f.read_text(encoding="utf-8").splitlines()
                             if rebuild.LINE.match(ln)))
    v = rebuild.read(d / f"recheck-{r}" / "verdicts.md")
    return len(ids), sum(bool(v[i][0]) for i in ids)


def main():
    v4 = {n: v4_note(n) for n in ORDER}
    v3, plan = v3_rows()
    all4 = [x for n in ORDER for x in v4[n]]
    N4 = len(all4)
    L = ["# Stage B results: gate B\n",
         "v4's first pass on the 14 rebuilt notes against the re-scored v3, with the same frozen checking procedure "
         "(checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either "
         "counted). v4 is every entry of every note "
         f"({N4} entries); v3 is the B2 baseline (300 entries, stratified, weighted to whole notes). The criteria "
         "are judged on the point estimates.\n",
         "Intervals (95%): Wilson for v4's pooled rates; the baseline's bootstrap (seed 20261037) for v3; for each "
         f"ratio, a bootstrap of {REPS:,} resamples (seed {SEED_RATIO}, fixed before scoring) resampling v3 within "
         "note and stratum and v4's notes as clusters.\n",
         "16S was built before revision 6 (the `src`/`conf` fix and the clarified builder rule) and was not rebuilt.\n",
         "## Criteria 1 to 3\n",
         "| Measure (per 100 entries) | v4 | v4 95% | Re-scored v3 | v3 95% | v4/v3 | Ratio 95% | Criterion | Met |",
         "|---|---|---|---|---|---|---|---|---|"]
    crit = {"First-pass fault rate": ("at most 2/3", lambda r: r <= 2 / 3),
            "holds + absent": ("at most 1/2", lambda r: r <= 0.5),
            "stronger + numbers": ("not above v3", lambda r: r <= 1),
            "conf": ("not above v3", lambda r: r <= 1)}
    met, reach1 = {}, []
    for name, t in MEASURES:
        k4 = sum(t(x[1]) for x in all4)
        lo4, hi4 = wilson(k4, N4)
        p3 = baseline.weighted(v3, plan, t)
        lo3, hi3 = baseline.boot(v3, plan, t)
        rl, rh = ratio_boot(v3, plan, v4, lambda v: t(v))
        r = (k4 / N4) / p3 if p3 else float("inf")
        label, ok = crit[name]
        met[name] = ok(r)
        if rh >= 1:
            reach1.append(name)
        L.append(f"| {name} | {100 * k4 / N4:.1f} ({k4}/{N4}) | {100 * lo4:.1f} to {100 * hi4:.1f} | {100 * p3:.1f} | "
                 f"{100 * lo3:.1f} to {100 * hi3:.1f} | {r:.2f} | {rl:.2f} to {"unbounded" if rh == float("inf") else f"{rh:.2f}"} | {label} | "
                 f"{'yes' if met[name] else '**no**'} |")
    rows3 = {baseline.key(r): r for r in baseline.v3notes.load()}
    rep3 = sum(bool(r["verdict"]) for r in rows3.values())
    L += ["", f"v3 as it reported itself (one checker, its own packets): {rep3}/{len(rows3)} = {rep3 / len(rows3):.1%} "
              "first-pass faults, against the re-scored rate above.", ""]
    if reach1:
        L.append(f"Ratio intervals that reach 1 (no difference): {', '.join(reach1)}. For criterion 3 that is the "
                 "test's direction (not above v3); for criteria 1 and 2 it would mean the improvement is not "
                 "distinguishable from none.")
    else:
        L.append("No ratio interval reaches 1.")

    # criterion 4
    L += ["", "## Criterion 4: omission\n", "| Note | Input | Omission check | Body addresses | Unaddressed sections "
          "outside the allow-list |", "|---|---|---|---|---|"]
    c4 = True
    for n in ORDER:
        for nid, mode, body, bad in omission(n):
            ok = not mode.startswith("not run") and body > 0 and not bad
            c4 &= ok
            L.append(f"| {n} | {nid} | {mode} | {body} | {', '.join(bad) or 'none'} |")
    L.append(f"\nMet: {'yes' if c4 else '**no**'}.")

    # criterion 5
    L += ["", "## Criterion 5: re-check\n", "| Note | Round 1: fixed, still faulted | Later rounds: still faulted of fixed |", "|---|---|---|"]
    t1 = s1 = 0
    for n in ORDER:
        f1, st1 = recheck_round(n, 1)
        t1, s1 = t1 + f1, s1 + st1
        later, r = [], 2
        while (R / n / f"fixes-{r}.md").exists():
            later.append("{1} of {0}".format(*recheck_round(n, r)))
            r += 1
        L.append(f"| {n} | {f1}, {st1} | {'; '.join(later) or 'none needed'} |")
    lo5, hi5 = wilson(s1, t1)
    c5 = s1 / t1 <= 0.15
    L.append(f"\nRound 1, pooled: {s1} of {t1} fixed entries still faulted = {s1 / t1:.1%} (Wilson {lo5:.1%} to "
             f"{hi5:.1%}), against at most 15% (v3: 11% development, 14% held-out). Met: {'yes' if c5 else '**no**'}.")

    # per note
    L += ["", "## By note\n",
          "| Note | Entries | First pass | Re-scored v3 estimate | holds + absent | stronger + numbers | conf |",
          "|---|---|---|---|---|---|---|"]
    for n in ORDER:
        xs = v4[n]
        f = sum(bool(x[1]) for x in xs)
        est = baseline.weighted([x for x in v3 if x[2] == n], {n: plan[n]}, lambda v: bool(v))
        c = lambda ks: sum(bool(x[1] & ks) for x in xs)
        L.append(f"| {n} | {len(xs)} | {f} ({f / len(xs):.1%}) | {est:.0%} | {c({'holds', 'absent'})} | "
                 f"{c({'stronger', 'numbers'})} | {c({'conf'})} |")
    L.append(f"\nKinds, v4 (entries): {', '.join(f'{k} {c}' for k, c in Counter(k for x in all4 for k in x[1]).most_common())}.")

    # every stronger / numbers fault
    L += ["", "## Every `stronger` and `numbers` fault (criterion 3)\n", "### v4\n", "| Note | Entry | Kinds | Checkers' reasons |",
          "|---|---|---|---|"]
    for n in ORDER:
        for i, ks, rs in v4[n]:
            if ks & {"stronger", "numbers"}:
                L.append(f"| {n} | {i} | {', '.join(sorted(ks))} | {' / '.join(rs).replace('|', '/')} |")
    L += ["", "### Re-scored v3 (the baseline sample)\n", "| Note | Entry | Kinds | Checkers' reasons |", "|---|---|---|---|"]
    sn = [x for x in v3 if x[3] & {"stronger", "numbers"}]
    reasons = v3_reasons({x[0] for x in sn})
    for k, st, n, ver in sorted(sn, key=lambda x: (ALL.index(x[2]), x[0])):
        L.append(f"| {n} | {k.split('/', 1)[1]} | {', '.join(sorted(ver))} | "
                 f"{' / '.join(reasons.get(k, [])).replace('|', '/')} |")

    # information
    L += ["", "## Information (not gate criteria)\n", "### Settings kept and near-copies (`tools/notestats.py`)\n"]
    import io
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        notestats.main(ORDER)
    L.append(buf.getvalue().rstrip())
    L += ["", "### The 16S removals\n",
          "From the 16S builder's own edit scripts (`rebuild/16S/removed-settings.md`), before the revision 6 "
          "clarification: 76 removals in 72 entries, all dropped and none kept with an added address. By the builder's "
          "account, 42 of the removed details are stated elsewhere in the inputs, 6 partly, 8 not at all and 20 "
          "unchecked. Its 16 other fixes added an address. The later builders, given the clarified rule, kept "
          "details with addresses; their removals (own wording, or details no addressable sentence gives) are listed "
          "per batch in `state.md`."]
    dr = S / "dns-readability" / "results.md"
    L += ["", "### Do-not-say readability\n",
          dr.read_text(encoding="utf-8").strip() if dr.exists() else "Not yet run."]

    L += ["", "## Gate B\n"]
    allmet = all(met.values()) and c4 and c5
    L.append(f"- Criterion 1 (first-pass rate): {'met' if met['First-pass fault rate'] else 'missed'}.")
    L.append(f"- Criterion 2 (holds + absent): {'met' if met['holds + absent'] else 'missed'}.")
    L.append(f"- Criterion 3 (stronger + numbers; conf): "
             f"{'met' if met['stronger + numbers'] and met['conf'] else 'missed'} "
             f"(stronger + numbers {'met' if met['stronger + numbers'] else 'missed'}, conf "
             f"{'met' if met['conf'] else 'missed'}).")
    L.append(f"- Criterion 4 (omission): {'met' if c4 else 'missed'}.")
    L.append(f"- Criterion 5 (re-check): {'met' if c5 else 'missed'}.")
    L.append(f"\n**{'All five criteria are met.' if allmet else 'At least one criterion is missed: stop and report.'}** "
             "The development notes informed this plan, so passing here is necessary, not sufficient; stage C is the "
             "real test. The owner decides.")
    (S / "results.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L[6:12]))


if __name__ == "__main__":
    main()
