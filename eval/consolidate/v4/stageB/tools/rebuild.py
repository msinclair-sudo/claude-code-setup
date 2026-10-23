"""Stage B, B3 to B7: first-pass scoring of a rebuilt note under the frozen checking procedure (plan.md revision 5):
two fresh checkers per 60-entry packet (`kn.py packets --hints`), a fault from either counted.

    python3 rebuild.py first <dir>     after <dir>/verdicts-a/ and verdicts-b/ -> <dir>/first-pass.md, and
                                       <dir>/fixes-1.md (the verdict lines the builder gets: faulted entries only)
    python3 rebuild.py recheck <dir> <n>   after <dir>/recheck-<n>/verdicts.md -> prints still-faulted entries and
                                       writes <dir>/fixes-<n+1>.md if any
<dir> is stageB/rebuild/<NOTE>/, holding packets/ from `kn.py packets <note> <dir>/packets --hints`.
"""
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from planted import wilson  # noqa: E402

KINDS = ("stronger", "conf", "numbers", "absent", "critic", "merged", "holds")
LINE = re.compile(r"^\s*[-*]?\s*`?([A-Za-z0-9][A-Za-z0-9-]*\.[A-Za-z0-9]+)`?(?:\s*\([^)]*\))?:\s*(.*)$")


def packet_ids(d):
    out = []
    for f in sorted((d / "packets").glob("packet-*.md")):
        ids = re.findall(r"^## (\S+) \(", f.read_text(encoding="utf-8"), re.M)
        out.append((f.name, ids))
    return out


def read(f):
    """{id: (kinds, the line's text)} from one verdict file."""
    out = {}
    for ln in Path(f).read_text(encoding="utf-8").splitlines():
        m = LINE.match(ln.strip())
        if not m:
            continue
        rest = m.group(2).strip()
        if re.match(r"ok\b", rest, re.I):
            out[m.group(1)] = (set(), "ok")
        else:
            head = rest.split(":", 1)[0].lower()
            out[m.group(1)] = ({x for x in re.split(r"[\s,/+]+", head) if x in KINDS} or {"other"}, rest)
    return out


def cmd_first(d):
    d = Path(d)
    packs = packet_ids(d)
    a, b, missing = {}, {}, []
    for name, ids in packs:
        for side, store in (("a", a), ("b", b)):
            f = d / f"verdicts-{side}" / name
            v = read(f) if f.exists() else {}
            store.update(v)
            missing += [f"{side}/{name}: {i}" for i in ids if i not in v]
    if missing:
        sys.exit(f"missing verdicts ({len(missing)}): {missing[:8]}")
    ids = [i for _, xs in packs for i in xs]
    union = {i: a[i][0] | b[i][0] for i in ids}
    n, f = len(ids), sum(bool(union[i]) for i in ids)
    lo, hi = wilson(f, n)
    per100 = lambda ks: 100 * sum(bool(union[i] & ks) for i in ids) / n
    L = [f"# First pass: {d.name}\n",
         "Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a "
         "fault from either counted.\n",
         f"- **First-pass fault rate: {f}/{n} = {f / n:.1%}** (Wilson {lo:.1%} to {hi:.1%}).",
         f"- Checker A alone {sum(bool(a[i][0]) for i in ids)}, checker B alone {sum(bool(b[i][0]) for i in ids)}, "
         f"both {sum(bool(a[i][0]) and bool(b[i][0]) for i in ids)}; agree (ok against fault) on "
         f"{sum(bool(a[i][0]) == bool(b[i][0]) for i in ids)} of {n}.",
         f"- Per 100 entries: holds + absent {per100({'holds', 'absent'}):.1f}; stronger + numbers "
         f"{per100({'stronger', 'numbers'}):.1f}; conf {per100({'conf'}):.1f}; critic {per100({'critic'}):.1f}; "
         f"merged {per100({'merged'}):.1f}.",
         f"- Kinds (entries): {', '.join(f'{k} {c}' for k, c in Counter(k for i in ids for k in union[i]).most_common())}.",
         "", "| Packet | Entries | A | B | Either | Agree |", "|---|---|---|---|---|---|"]
    for name, xs in packs:
        L.append(f"| {name} | {len(xs)} | {sum(bool(a[i][0]) for i in xs)} | {sum(bool(b[i][0]) for i in xs)} | "
                 f"{sum(bool(union[i]) for i in xs)} | {sum(bool(a[i][0]) == bool(b[i][0]) for i in xs)} |")
    L += ["", "## Every `stronger` and `numbers` fault (gate B, criterion 3)\n", "| Entry | Kinds | Checkers' reasons |",
          "|---|---|---|"]
    for i in ids:
        if union[i] & {"stronger", "numbers"}:
            rs = " / ".join(x[1] for x in (a[i], b[i]) if x[0])
            L.append(f"| {i} | {', '.join(sorted(union[i]))} | {rs.replace('|', '/')} |")
    (d / "first-pass.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    fx = [f"{i}: {x[1]}" for i in ids if union[i] for x in (a[i], b[i]) if x[0]]
    (d / "fixes-1.md").write_text(f"# Faults to fix ({f} entries)\n\n" + "\n".join(fx) + "\n", encoding="utf-8")
    print("\n".join(L[2:7]))


def cmd_recheck(d, n):
    d, n = Path(d), int(n)
    fixed = [ln.split(":", 1)[0] for ln in (d / f"fixes-{n}.md").read_text(encoding="utf-8").splitlines()
             if LINE.match(ln)]
    fixed = list(dict.fromkeys(fixed))
    v = read(d / f"recheck-{n}" / "verdicts.md")
    miss = [i for i in fixed if i not in v]
    if miss:
        sys.exit(f"re-check missing {len(miss)}: {miss[:8]}")
    still = [i for i in fixed if v[i][0]]
    print(f"round {n}: {len(fixed)} fixed entries re-checked, {len(still)} still faulted "
          f"({len(still) / len(fixed):.0%})")
    if still:
        (d / f"fixes-{n + 1}.md").write_text(f"# Faults to fix ({len(still)} entries)\n\n" +
                                             "\n".join(f"{i}: {v[i][1]}" for i in still) + "\n", encoding="utf-8")


VAULT = Path("/mnt/a/Obsidian Vault/Michael.md")
NOTES = {  # note -> its knowledge note, vault-relative
    "16S": "Topics/Biology/Research/Knowledge/16S amplicon sequencing from sample to count table.md",
    "H2-01": "PhD/Proposal/Research/Knowledge/Dimensionality and cross-habitat stability of microbial functional "
             "profiles.md",
    "TSL": "PhD/biblion/research/knowledge/Term specificity and multi-level labelling.md",
    "CB1": "PhD/Proposal/Research/Knowledge/Agricultural liming rates, supply, energy and carbon dioxide.md",
    "CB2": "PhD/Proposal/Research/Knowledge/Recovery of rRNA genes from metagenome assemblies and MAGs.md",
    "NFERT": "PhD/Proposal/Research/Knowledge/Synthetic nitrogen fertiliser and soil microbial nitrogen cycling.md",
    "CB3": "PhD/Proposal/Research/Knowledge/Agriculture's share of global greenhouse gas emissions.md",
    "GHOST": "PhD/biblion/research/knowledge/Positioning graph nodes that lack features.md",
    "TAXRES": "PhD/biblion/research/knowledge/Reference taxonomies and taxon-name resolution.md",
    "H1-RES": "PhD/Proposal/Research/Knowledge/Decoupling of microbial function from taxonomy.md",
    "H2-04": "PhD/Proposal/Research/Knowledge/Sources of functional covariation and cross-level functional axes.md",
    "H1-05": "PhD/Proposal/Research/Knowledge/Functional and taxonomic turnover in soil microbial communities.md",
    "H1-02": "PhD/Proposal/Research/Knowledge/Recovery artefacts in the gene content of metagenome-assembled genomes.md",
    "H1-06": "PhD/Proposal/Research/Knowledge/Phylogenetic depth of prokaryotic traits and rank-wise environmental "
             "structuring.md",
}


def kn():
    sys.path.insert(0, str(HERE.parents[4] / "skills" / "consolidate" / "scripts"))
    import kn as k
    return k


def cmd_prep(note, rel=None):
    """Copy the first-pass note to rebuild/<note>/as-built.md, cut its 60-entry packets with hints, make the verdict
    folders."""
    rel = rel or NOTES[note]
    d = HERE.parent / "rebuild" / note
    for sub in ("verdicts-a", "verdicts-b"):
        (d / sub).mkdir(parents=True, exist_ok=True)
    src = VAULT / rel
    (d / "as-built.md").write_bytes(src.read_bytes())
    (d / "vault-path.txt").write_text(rel + "\n", encoding="utf-8")
    kn().packets(src, d / "packets", with_hints=True)


def cmd_repack(note, n):
    """Re-check packets for the entries in fixes-<n>.md, from the note as it now stands in the vault."""
    d = HERE.parent / "rebuild" / note
    rel = (d / "vault-path.txt").read_text(encoding="utf-8").strip() if (d / "vault-path.txt").exists() else NOTES[note]
    ids = [ln.split(":", 1)[0] for ln in (d / f"fixes-{n}.md").read_text(encoding="utf-8").splitlines() if LINE.match(ln)]
    kn().packets(VAULT / rel, d / f"recheck-{n}", only=set(ids), with_hints=True)


def cmd_final(note):
    d = HERE.parent / "rebuild" / note
    rel = (d / "vault-path.txt").read_text(encoding="utf-8").strip() if (d / "vault-path.txt").exists() else NOTES[note]
    (d / "final.md").write_bytes((VAULT / rel).read_bytes())
    print(f"{note}: final.md saved")


def cmd_ids(d, n):
    """The IDs in fixes-<n>.md, comma-separated, for `kn.py packets --only`."""
    ids = [ln.split(":", 1)[0] for ln in (Path(d) / f"fixes-{n}.md").read_text(encoding="utf-8").splitlines()
           if LINE.match(ln)]
    print(",".join(dict.fromkeys(ids)))


if __name__ == "__main__":
    {"first": lambda: cmd_first(sys.argv[2]), "recheck": lambda: cmd_recheck(sys.argv[2], sys.argv[3]),
     "ids": lambda: cmd_ids(sys.argv[2], sys.argv[3]),
     "prep": lambda: cmd_prep(*sys.argv[2:4]), "repack": lambda: cmd_repack(sys.argv[2], sys.argv[3]),
     "final": lambda: cmd_final(sys.argv[2])}[sys.argv[1]]()
