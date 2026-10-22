#!/usr/bin/env python3
"""Stage A: score change 1's lint rules (R1 numbers and names; R2 holds words, three variants) against the v3
first-pass checker verdicts, as defined in rules.md. Read-only on the notes; writes only into this folder.

    python3 score_lint.py --sanity     parse, resolve and the known cases; no scores
    python3 score_lint.py              flags.tsv and scores.md
    python3 score_lint.py --sample     the false-positive sample packets (fp/), seed in rules.md
"""
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "skills" / "consolidate" / "scripts"))
import kn  # noqa: E402

VAULT = Path("/mnt/a/Obsidian Vault/Michael.md")
EV = ROOT / "eval" / "consolidate"
SEED = 20261023
KINDS = ("stronger", "conf", "numbers", "absent", "critic", "merged", "holds")

V3, HO = EV / "v3", EV / "heldout"
NOTES = [  # (id, as-built note, first-pass verdict files)
    ("16S", V3 / "as-built/16S amplicon sequencing from sample to count table.md",
     [V3 / "verdicts/MB-packets-01-04.md", V3 / "verdicts/MB-packets-05-08.md"]),
    ("H2-01", V3 / "as-built/Dimensionality and cross-habitat stability of microbial functional profiles.md",
     [V3 / "verdicts/H2-01.md"]),
    ("TSL", V3 / "as-built/Term specificity and multi-level labelling.md", [V3 / "verdicts/TSL.md"]),
    ("CB1", V3 / "as-built/Agricultural liming rates, supply, energy and carbon dioxide.md",
     [V3 / "verdicts/CB1-LIMING.md"]),
    ("CB2", V3 / "as-built/Recovery of rRNA genes from metagenome assemblies and MAGs.md",
     [V3 / "verdicts/CB2-RRNA.md"]),
    ("NFERT", V3 / "as-built/Synthetic nitrogen fertiliser and soil microbial nitrogen cycling.md",
     [V3 / "verdicts/NFERT.md"]),
    ("H2-04", HO / "as-built/Sources of functional covariation and cross-level functional axes.md",
     [HO / "verdicts/H2-04.md"]),
    ("H1-05", HO / "as-built/Functional and taxonomic turnover in soil microbial communities.md",
     [HO / "verdicts/H1-05.md"]),
    ("H1-02", HO / "as-built/Recovery artefacts in the gene content of metagenome-assembled genomes.md",
     [HO / "verdicts/H1-02.md"]),
    ("H1-06", HO / "as-built/Phylogenetic depth of prokaryotic traits and rank-wise environmental structuring.md",
     [HO / "verdicts/H1-06.md"]),
    ("GHOST", HO / "as-built/Positioning graph nodes that lack features.md", [HO / "verdicts/GHOST.md"]),
    ("CB3", HO / "as-built/Agriculture's share of global greenhouse gas emissions.md", [HO / "verdicts/CB3.md"]),
    ("TAXRES", HO / "as-built/Reference taxonomies and taxon-name resolution.md", [HO / "verdicts/TAXRES.md"]),
    ("H1-RES", HO / "as-built/Decoupling of microbial function from taxonomy.md", [HO / "verdicts/H1-RES.md"]),
]
R2_FP_EXCLUDE = {"CB3"}


def wordlist(name):
    return {w.strip().lower() for w in (HERE / name).read_text(encoding="utf-8").splitlines() if w.strip()}


CONNECTIVES = wordlist("connectives.txt")
STOPWORDS = wordlist("stopwords.txt") | CONNECTIVES
COMMON_CAPS = {w.strip() for w in (HERE / "capitalised-common.txt").read_text(encoding="utf-8").splitlines()
               if w.strip()}
NUMWORDS = ("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen "
            "sixteen seventeen eighteen nineteen twenty").split()

# ---------------------------------------------------------------- normalisation (rules.md)
DASH = re.compile(r"[‐-―−]")
# Mechanical fix after the first run (results.md): letters and digits as Python's \w sees them, so that a token
# with sub- or superscript digits (CaCO₃, R²) is cut the same way in the entry and in the cited text.
WORD = re.compile(r"[^\W_]+(?:[.\-'][^\W_]+)*")
NUM = re.compile(r"(?<![A-Za-z0-9.])\d+(?:\.\d+)?(?![A-Za-z0-9])")
BRACKET = re.compile(r"\[(\s*\d+(?:\s*[-,]\s*\d+)*\s*)\]")
CAP = re.compile(r"(?<![\w'\-])[A-Z][\wÀ-ɏ'\-]*")
QUOTE = re.compile(r'"([^"]{3,}?)"')


def norm(s):
    s = s.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    s = DASH.sub("-", s)
    s = re.sub(r"[*`]", "", s)
    s = re.sub(r"(?<=\d),(?=\d{3}(?!\d))", "", s)
    s = re.sub(r"'s\b", "", s)
    return s


def stem(w):
    for suf in ("ing", "ed", "es", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            return w[:-len(suf)]
    return w


def canon(x):
    try:
        return format(float(x), ".10g")
    except ValueError:
        return x


def markers(text):
    out = set()
    for m in BRACKET.finditer(text):
        for part in re.split(r"\s*,\s*", m.group(1).strip()):
            a, _, b = part.partition("-")
            a = a.strip()
            b = b.strip() or a
            if a.isdigit() and b.isdigit() and int(b) - int(a) < 200:
                out.update(str(n) for n in range(int(a), int(b) + 1))
    return out


class Cited:
    """The cited text of one entry, prepared for matching."""

    def __init__(self, text):
        self.raw = text
        n = norm(text)
        self.low = re.sub(r"\s+", " ", n.lower())
        words = WORD.findall(self.low)
        self.words = {stem(w) for w in words} | set(words)
        for w in words:
            if "-" in w:
                self.words |= {stem(p) for p in w.split("-") if p}
        self.nums = {canon(x) for x in NUM.findall(BRACKET.sub(" ", n))} | {canon(x) for x in NUM.findall(n)}
        self.markers = markers(n)

    def has_word(self, w):
        w = w.strip(".'-")
        if not w:
            return True
        if stem(w) in self.words or w in self.words:
            return True
        if "-" in w:
            return all(stem(p) in self.words for p in w.split("-") if p)
        return False

    def has_num(self, x):
        c = canon(x)
        if c in self.nums:
            return True
        if c.isdigit() and int(c) <= 20 and re.search(rf"\b{NUMWORDS[int(c)]}\b", self.low):
            return True
        return False

    def has_phrase(self, p):
        parts = [x.strip(" .,;:") for x in re.split(r"\.\.\.|…", re.sub(r"\s+", " ", p.lower()))]
        return all(x in self.low for x in parts if x)


# ---------------------------------------------------------------- parsing
def parse_note(path):
    text = path.read_text(encoding="utf-8")
    fm = kn.frontmatter(text)
    body = text.split("\n---\n", 1)[1] if text.startswith("---") else text
    lines, part, entries, i = body.splitlines(), None, [], 0
    while i < len(lines):
        ln = lines[i]
        h2 = re.match(r"##\s+(.*)", ln)
        if h2 and not ln.startswith("###"):
            part = h2.group(1).strip().lower()
        e = kn.ENTRY.match(ln)
        if e:
            f, j = {}, i + 1
            while j < len(lines) and kn.FIELDLINE.match(lines[j]):
                f.update(kn.split_fields(lines[j]))
                j += 1
            kind = {"do not say": "dns", "gaps": "gap"}.get(part, "claim")
            if part == "concepts" and f.get("kind") == "background":
                kind = "background"
            entries.append({"id": e.group(1), "type": kind, "statement": e.group(2), "fields": f})
            i = j
            continue
        i += 1
    bib = kn.parse_bib("\n".join(re.findall(r"```bibtex\n(.*?)```", body, re.S)))
    inputs = {}
    for item in fm.get("inputs") or []:
        if isinstance(item, dict):
            (nid, rel), = item.items()
        else:
            nid, rel = [x.strip() for x in str(item).split(":", 1)]
        inputs[nid] = VAULT / str(rel).strip().strip('"')
    return entries, bib, inputs


def inventory(inputs):
    items = {}
    for nid, p in inputs.items():
        _, inv = kn.detect(p, nid)
        for x in inv:
            items[f"{nid}:{x['id']}"] = x
    return items


VLINE = re.compile(r"^([A-Za-z0-9][A-Za-z0-9-]*\.[A-Za-z0-9]+):\s*(.*)$")


def verdicts(files):
    out, dup = {}, []
    for f in files:
        for ln in f.read_text(encoding="utf-8").splitlines():
            m = VLINE.match(ln.strip())
            if not m:
                continue
            eid, rest = m.group(1), m.group(2).strip()
            if eid in out:
                dup.append(eid)
                continue
            if re.match(r"ok\b", rest, re.I):
                out[eid] = set()
            else:
                head = rest.split(":", 1)[0].lower()
                ks = {k for k in re.split(r"[\s,/+]+", head) if k in KINDS}
                out[eid] = ks or {"other"}
    return out, dup


def src_people(src, bib):
    names, years = set(), set()
    for k, e in bib.items():
        if re.search(rf"(?<![\w]){re.escape(k)}(?![\w])", src or ""):
            for a in re.split(r"\s+and\s+", e.get("author", "")):
                s = kn.fold(kn.surname(a)).lower().strip("{} ")
                if s:
                    names.add(re.sub(r"[^a-z]", "", s))
                    names.update(re.sub(r"[^a-z]", "", w) for w in re.split(r"[\s\-]+", s) if w)
            if e.get("year"):
                years.add(canon(re.sub(r"\D", "", e["year"])[:4]))
    return names - {""}, years


# ---------------------------------------------------------------- the rules
def sentence_start(text, pos):
    pre = text[:pos].rstrip(" \"'([")
    return pre == "" or bool(re.search(r"[.!?][\"')\]]*$", pre))


def r1_tokens(text):
    """[(kind, token)] from a statement or a why, as rules.md defines them."""
    n = norm(text)
    toks = [("marker", x) for x in sorted(markers(n), key=int)]
    for x in NUM.findall(BRACKET.sub(" ", n)):
        toks.append(("year" if x.isdigit() and 1800 <= int(x) <= 2099 else "number", x))
    for m in CAP.finditer(n):
        w = m.group(0).rstrip("'-")
        if len(w) < 2 or w in COMMON_CAPS or w.rstrip("s") in COMMON_CAPS:
            continue
        if sentence_start(n, m.start()):
            continue
        toks.append(("name", w))
    for m in QUOTE.finditer(n):
        toks.append(("quote", m.group(1)))
    return toks


def r1(entry, cited, bib):
    names, years = src_people(entry["fields"].get("src", ""), bib)
    texts = [entry["statement"]] + ([entry["fields"].get("why", "")] if entry["type"] == "dns" else [])
    miss, via_src = [], 0
    for t in texts:
        for kind, tok in r1_tokens(t):
            if kind == "marker":
                ok = tok in cited.markers
            elif kind in ("number", "year"):
                ok = cited.has_num(tok) or (kind == "year" and canon(tok) in years)
                if not ok and kind == "year" and canon(tok) in years:
                    via_src += 1
            elif kind == "name":
                low = tok.lower()
                ok = cited.has_word(low)
                if not ok:
                    key = re.sub(r"[^a-z]", "", kn.fold(low))
                    parts = [re.sub(r"[^a-z]", "", kn.fold(p)) for p in low.split("-")]
                    if key in names or (len(parts) > 1 and all(p in names for p in parts if p)):
                        ok, via_src = True, via_src + 1
            else:
                ok = cited.has_phrase(tok)
            if not ok:
                miss.append(f"{kind}:{tok}")
    return miss, via_src


LEX = {stem(w) for w in wordlist("setting-lexicon.txt")} | wordlist("setting-lexicon.txt")


def r2(entry, cited):
    holds = entry["fields"].get("holds")
    if not holds or entry["type"] != "claim":
        return None
    n = norm(holds)
    caps = {m.group(0).lower().rstrip("'-") for m in CAP.finditer(n) if len(m.group(0)) >= 2}
    out = {"full": [], "content": [], "setting": []}
    for w in WORD.findall(n.lower()):
        w = w.strip(".'-")
        if not w:
            continue
        numeric = bool(re.fullmatch(r"\d+(?:\.\d+)?", w))
        found = cited.has_num(w) if numeric else cited.has_word(w)
        if found:
            continue
        if w not in CONNECTIVES:
            out["full"].append(w)
        if w not in STOPWORDS:
            out["content"].append(w)
        setting = (w in caps or numeric or bool(re.search(r"\d", w)) or "-" in w
                   or stem(w) in LEX or w in LEX)
        if setting:
            out["setting"].append(w)
    return out


# ---------------------------------------------------------------- run
def load():
    rows, problems = [], []
    for nid, path, vfiles in NOTES:
        entries, bib, inputs = parse_note(path)
        items = inventory(inputs)
        judged = [e for e in entries if e["type"] in ("claim", "dns")]
        ver, dup = verdicts(vfiles)
        ids = {e["id"] for e in judged}
        problems.append((nid, len(judged), len(ver), sorted(set(ver) - ids), sorted(ids - set(ver)), dup))
        default = next(iter(inputs)) if len(inputs) == 1 else "?"
        for e in judged:
            refs = kn.entry_refs(e["fields"], default)
            texts, unresolved = [], []
            for ref in refs:
                for g in kn.expand(ref) or [ref]:
                    x = items.get(g)
                    (texts.append(x["text"]) if x else unresolved.append(g))
            cited = Cited("\n".join(texts))
            miss1, via = r1(e, cited, bib)
            rows.append({"note": nid, "id": e["id"], "type": e["type"], "verdict": ver.get(e["id"]),
                         "r1": miss1, "r1_via_src": via, "r2": r2(e, cited), "unresolved": unresolved,
                         "entry": e, "cited": texts, "refs": refs})
    return rows, problems


def sanity(rows, problems):
    print("note        entries  verdicts  verdict-not-entry  entry-not-verdict  duplicates")
    for nid, ne, nv, a, b, d in problems:
        print(f"{nid:10} {ne:8} {nv:9}  {len(a):17}  {len(b):17}  {len(d):10}"
              + (f"   e.g. {a[:3]} {b[:3]}" if a or b else ""))
    print("total entries", sum(p[1] for p in problems), "total verdicts", sum(p[2] for p in problems))
    unres = [(r["note"], r["id"], u) for r in rows for u in r["unresolved"]]
    print("unresolved from references:", len(unres), unres[:10])
    print("entries with no cited text:", sum(1 for r in rows if not r["cited"]))

    def show(note, pred, label):
        for r in rows:
            if r["note"] == note and pred(r):
                f2 = r["r2"] or {}
                print(f"  {label}: {note} {r['id']} verdict={sorted(r['verdict'] or [])} r1={r['r1']} "
                      f"r2-full={f2.get('full')} r2-setting={f2.get('setting')}")
    print("known cases:")
    show("H1-05", lambda r: re.search(r"steppe|coastal", r["entry"]["fields"].get("holds", ""), re.I), "R2 expected")
    show("H2-04", lambda r: r["id"] == "covariation-sources.1", "R2 expected")
    show("CB1", lambda r: r["id"] == "lime-resource.7", "R1 expected (2020)")
    print("  R1 tokens accepted only through src authors or years:", sum(r["r1_via_src"] for r in rows),
          "in", sum(1 for r in rows if r["r1_via_src"]), "entries")


def score(rows):
    rule_sets = {"R1": ("absent", "numbers"), "R2-full": ("holds",), "R2-content": ("holds",),
                 "R2-setting": ("holds",)}

    def flagged(r, rule):
        if rule == "R1":
            return bool(r["r1"])
        return bool(r["r2"] and r["r2"][rule.split("-")[1]])

    res = {}
    for rule, kinds in rule_sets.items():
        per = defaultdict(Counter)
        for r in rows:
            if r["verdict"] is None:
                continue
            c = per[r["note"]]
            fl, v = flagged(r, rule), r["verdict"]
            target = bool(v & set(kinds))
            if target:
                c["tp" if fl else "fn"] += 1
            elif not v:
                c["passed"] += 1
                c["fp"] += fl
            else:
                c["other_faults"] += 1
                c["flag_other"] += fl
            c["flags"] += fl
        res[rule] = per
    return res


def write(rows, res):
    with (HERE / "flags.tsv").open("w", encoding="utf-8") as w:
        w.write("note\tid\ttype\tverdict\tR1\tR2-full\tR2-content\tR2-setting\n")
        for r in rows:
            f2 = r["r2"] or {}
            w.write("\t".join([r["note"], r["id"], r["type"],
                               "unmatched" if r["verdict"] is None else (",".join(sorted(r["verdict"])) or "ok"),
                               "; ".join(r["r1"]), " ".join(f2.get("full", [])), " ".join(f2.get("content", [])),
                               " ".join(f2.get("setting", []))]) + "\n")
    th = {"R1": (0.40, 0.03), "R2-full": (0.60, 0.05), "R2-content": (0.60, 0.05), "R2-setting": (0.60, 0.05)}
    out = ["# Stage A scores\n\nGenerated by `score_lint.py` from the v3 as-built notes and first-pass verdicts "
           "(`rules.md`). R1 is scored against `absent` and `numbers` faults; R2 against `holds` faults. "
           "False positives are flagged entries the checker passed, over all entries it passed (R2 without "
           f"{', '.join(sorted(R2_FP_EXCLUDE))}).\n\n## Overall\n\n"
           "| Rule | Caught (TP) | Missed (FN) | Catch rate | False positives | Entries passed | FP rate | "
           "Flags on other faults | Threshold (catch / FP) | Meets |\n|---|---|---|---|---|---|---|---|---|---|\n"]
    summary = {}
    for rule, per in res.items():
        tot = Counter()
        for nid, c in per.items():
            tot["tp"] += c["tp"]
            tot["fn"] += c["fn"]
            tot["flag_other"] += c["flag_other"]
            if not (rule.startswith("R2") and nid in R2_FP_EXCLUDE):
                tot["fp"] += c["fp"]
                tot["passed"] += c["passed"]
        catch = tot["tp"] / max(1, tot["tp"] + tot["fn"])
        fpr = tot["fp"] / max(1, tot["passed"])
        lo, hi = th[rule]
        ok = catch >= lo and fpr <= hi
        summary[rule] = (catch, fpr, ok, tot)
        out.append(f"| {rule} | {tot['tp']} | {tot['fn']} | {catch:.1%} | {tot['fp']} | {tot['passed']} | "
                   f"{fpr:.1%} | {tot['flag_other']} | {lo:.0%} / {hi:.0%} | {'yes' if ok else 'no'} |\n")
    for rule in ("R2-full", "R2-content", "R2-setting"):
        c = res[rule].get("CB3", Counter())
        out.append(f"\nCB3 alone, {rule}: {c['fp']} of {c['passed']} passed entries flagged "
                   f"({c['fp'] / max(1, c['passed']):.1%}); {c['tp']} of {c['tp'] + c['fn']} holds faults caught.")
    out.append("\n\n## Per note\n\n| Note | Rule | TP | FN | FP | Passed | Flags on other faults |\n"
               "|---|---|---|---|---|---|---|\n")
    for nid, *_ in NOTES:
        for rule, per in res.items():
            c = per.get(nid, Counter())
            out.append(f"| {nid} | {rule} | {c['tp']} | {c['fn']} | {c['fp']} | {c['passed']} | {c['flag_other']} |\n")
    (HERE / "scores.md").write_text("".join(out), encoding="utf-8")
    for rule, (catch, fpr, ok, tot) in summary.items():
        print(f"{rule:11} catch {catch:6.1%} ({tot['tp']}/{tot['tp'] + tot['fn']})  FP {fpr:5.1%} "
              f"({tot['fp']}/{tot['passed']})  meets: {ok}")


def packet(r, family):
    e, f = r["entry"], r["entry"]["fields"]
    lost = "; ".join(r["r1"]) if family == "R1" else " ".join(r["r2"]["full"])
    tags = "" if family == "R1" else " (also flagged by: " + ", ".join(
        v for v in ("content", "setting") if r["r2"][v]) + ")"
    s = [f"## {r['note']} {e['id']} ({'do not say' if e['type'] == 'dns' else 'claim'})\n\n{e['statement']}\n\n"]
    s += [f"- {k}: {v}\n" for k, v in f.items() if k != "from"]
    s.append(f"\n**Lint could not find:** {lost}{tags}\n\nCited text (`from` and named critique):\n\n")
    s += [f"> {t}\n>\n" for t in r["cited"]]
    return "".join(s) + "\n"


def sample(rows):
    rng = random.Random(SEED)
    fp1 = [r for r in rows if r["verdict"] == set() and r["r1"]]
    fp2 = [r for r in rows if r["verdict"] == set() and r["r2"] and r["r2"]["full"] and r["note"] not in R2_FP_EXCLUDE]
    d = HERE / "fp"
    d.mkdir(exist_ok=True)
    for fam, pool in (("R1", fp1), ("R2", fp2)):
        pick = rng.sample(pool, min(30, len(pool)))
        (d / f"{fam}-packets.md").write_text(
            f"# False-positive sample, {fam}: {len(pick)} of {len(pool)} (seed {SEED})\n\n"
            + "".join(packet(r, fam) for r in pick), encoding="utf-8")
        print(fam, len(pick), "of", len(pool), "->", d / f"{fam}-packets.md")


if __name__ == "__main__":
    rows, problems = load()
    if "--sanity" in sys.argv:
        sanity(rows, problems)
    elif "--sample" in sys.argv:
        sample(rows)
    else:
        write(rows, score(rows))
