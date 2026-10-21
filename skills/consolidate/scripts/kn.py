#!/usr/bin/env python3
"""consolidate: read research result notes as they are, and check the knowledge note built from them.

  kn.py detect NOTE [--id ID] [--inventory OUT.md]   what the note has, which checks can run, and the
                                                     inventory of items the knowledge note must account for
  kn.py lint KNOWLEDGE.md                            check the knowledge note; write KNOWLEDGE.index.json
  kn.py packets KNOWLEDGE.md OUTDIR                  each claim and do-not-say entry beside the note text it
                                                     came from, for the faithfulness checker
  kn.py citekey --author A --title T --year Y [--doi D --refs BIB]
                                                     the source's key: its key in BIB if the DOI is there,
                                                     else auth.lower + shorttitle(3,3) + year

Detection never requires a format. A note with labelled citations (`[FT; meas; repl]` after each citation,
research-brief protocol rule 3a, or MB-01's earlier form) gets the exact omission check over every labelled
sentence; any other note gets the fallback over its answers. Critique items are inventoried whenever a critique
is present. Standard library only (PyYAML used if installed).
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# ---------------------------------------------------------------- reading a result note

BRACKET = re.compile(r"\[([^\[\]\n]{2,140})\]")
ACCESS_TOK = re.compile(r"^(?:FT|AB|SEC|full[ _-]?text|abstract(?:[ _-]only)?|secondary)\b", re.I)
CLASS_TOK = re.compile(r"^(?:meas(?:ured)?|deriv(?:ed)?|model(?:led)?|assert(?:ed)?)\b", re.I)
STAND_TOK = re.compile(r"^(?:repl(?:icated)?|single(?:[ _-](?:source|study|dataset))?|cont(?:ested)?|unclear)\b", re.I)


def label_parts(inner):
    """A citation label is a bracket of ';'- or ','-separated parts with an access token among them:
    `[FT; meas; repl]` (rule 3a), `[FT, re-opened; deriv/model; single dataset]` (MB-01),
    `[Jiang2012; FT; measured; SINGLE SOURCE]` (H2-01). Returns (is_label, standing part or None)."""
    parts = [x.strip() for x in re.split(r"[;,]", inner) if x.strip()]
    stand = next((x for x in parts if STAND_TOK.match(x)), None)
    if not any(ACCESS_TOK.match(x) for x in parts) or not (stand or any(CLASS_TOK.match(x) for x in parts)):
        return False, None        # "[3, FT]" and a reference list's "[peer reviewed; FT]" are not labels
    return True, stand


def labels_in(s):
    return [m.group(1) for m in BRACKET.finditer(s) if label_parts(m.group(1))[0]]
STYLES = {
    "numbered": re.compile(r"(?<![\w\]])\[\d{1,3}(?:\s*[,\u2013\-]\s*\d{1,3})*(?:,\s*(?:FT|AB|SEC))?\]"),
    "bracket keys": re.compile(r"\[[A-Z]{1,3}\d{1,3}\]"),
    "compact author-year": re.compile(r"\b[A-Z][a-z]+(?:[A-Z][a-z]+)?\d{4}[a-z]?\b"),
    "parenthetical author-year": re.compile(
        r"\([A-Z][A-Za-z\-'\u00C0-\u017F]+(?: (?:and|&) [A-Z][A-Za-z\-'\u00C0-\u017F]+| et al\.?)?,? \d{4}[a-z]?[;)]"),
    "narrative author-year": re.compile(
        r"\b[A-Z][A-Za-z\-'\u00C0-\u017F]+(?: (?:and|&) [A-Z][A-Za-z\-'\u00C0-\u017F]+| et al\.?)? \(?\d{4}[a-z]?\b"),
}
CRITIC_TITLE = re.compile(r"critic|critique|adversarial|refuted|killed in verification", re.I)
ANSWER_TITLE = re.compile(r"^(?:\d+\.\s*)?(?:answers?\b|verdicts?\b)|answers as delivered|answers in brief", re.I)
NO_CRITIC = re.compile(r"\bno\b|not run|without|was not", re.I)
REF_TITLE = re.compile(r"^(?:\d+\.\s*)?(?:references?|reference list|bibliography|sources)\b", re.I)
SKIP_TITLE = re.compile(r"note role|provenance|search record|sources not obtained|references?$|reference list|"
                        r"bibliography|stage.?2|conventions|verification log", re.I)
SENT = re.compile(r"(?<=[.!?])[\"')\]]*\s+(?=[A-Z(\[\"*])")
ABBR = re.compile(r"(?:\b(?:St|Dr|Mr|Ms|Mrs|Prof|Fig|Figs|Eq|No|Vol|cf|vs|al|approx|ca|Inc|Ltd|Co|sp|spp|e\.g|i\.e)\.)$")


def bare(kind, title):
    """A callout's title without its type ('quote: Verdict' -> 'Verdict')."""
    return re.sub(r"^\w+:\s*", "", title) if kind == "callout" else title


def read(path):
    t = Path(path).read_text(encoding="utf-8", errors="replace")
    fm = re.match(r"---\n.*?\n---\n", t, re.S)
    return t, (t[fm.end():] if fm else t), (len(t[:fm.end()].splitlines()) if fm else 0)


def sections(body):
    """[(kind, title, level, lines)]: callouts and heading sections, in order; kind 'callout' or 'heading'."""
    lines = body.splitlines()
    out, i, cur = [], 0, None
    while i < len(lines):
        ln = lines[i]
        m = re.match(r">\s*\[!(\w+)\][-+]?\s*(.*)", ln)
        if m:
            j = i + 1
            while j < len(lines) and lines[j].startswith(">"):
                j += 1
            out.append(("callout", f"{m.group(1)}: {m.group(2)}".strip(), 9,
                        [re.sub(r"^>\s?", "", x) for x in lines[i + 1:j]], i))
            i = j
            continue
        h = re.match(r"(#{1,6})\s+(.*)", ln)
        if h:
            cur = ["heading", h.group(2).strip(), len(h.group(1)), [], i]
            out.append(cur)
        elif cur is not None:
            cur[3].append(ln)
        i += 1
    return [tuple(s) for s in out]


def region_lines(secs, want, default=False):
    """Lines of the sections `want` picks. want(kind, title) is True, False, or None to inherit from the enclosing
    heading (default at the top), so an excluded section excludes its subsections and an included one includes
    them. A callout belongs to the heading above it unless want decides it."""
    out, stack = [], []          # (level, included)
    for kind, title, level, lines, _ in secs:
        if kind == "heading":
            while stack and stack[-1][0] >= level:
                stack.pop()
        parent = stack[-1][1] if stack else default
        w = want(kind, title)
        inc = parent if w is None else bool(w)
        if kind == "heading":
            stack.append((level, inc))
        if inc:
            out.append((title, lines))
    return out


def units(lines):
    """Bullets, table rows and paragraphs, each as one string."""
    out, buf = [], []

    def flush():
        if buf:
            out.append(" ".join(buf).strip())
            buf.clear()
    bullet = False
    for ln in lines:
        s = ln.strip()
        if not s or s.startswith("```"):
            flush()
            bullet = False
            continue
        if bullet and buf and not ln[:1].isspace():   # an unindented line after a bullet starts a new unit
            flush()
            bullet = False
        if re.match(r"([-*+]|\d+[.)])\s+", s) or s.startswith("|"):
            flush()
            bullet = not s.startswith("|")
            if s.startswith("|") and re.fullmatch(r"[|\s:\-]+", s):
                continue
            buf.append(s)
            flush() if s.startswith("|") else None
            continue
        buf.append(s)
    flush()
    return [u for u in out if u]


def sentences(u):
    out = []
    for s in SENT.split(u):
        if out and ABBR.search(out[-1]):      # "St. Luce", "et al. Found"
            out[-1] += " " + s
        else:
            out.append(s)
    return [s.strip() for s in out if len(s.split()) >= 2]     # "*Strength:* Moderate." is a finding too


def detect(path, nid=None):
    full, body, _ = read(path)
    secs = sections(body)
    title = next((t for k, t, lv, _, _ in secs if k == "heading" and lv == 1), Path(path).stem)
    labels = [label_parts(m.group(1)) for m in BRACKET.finditer(body)]
    labels = [st for ok, st in labels if ok]
    with_standing = sum(1 for st in labels if st)
    labelled = len(labels) >= 10          # a few stray labels (MB-02 has 3) do not make a labelling convention
    style_counts = {k: len(p.findall(body)) for k, p in STYLES.items()}
    style = "labelled (access; class; standing)" if labelled else (
        max(style_counts, key=style_counts.get) if max(style_counts.values()) >= 5 else "none found")
    is_crit = lambda t: bool(CRITIC_TITLE.search(t)) and not re.search(r"stage.?2", t, re.I) and not NO_CRITIC.search(t)
    is_ans = lambda k, t: bool(ANSWER_TITLE.search(bare(k, t))) or (k == "callout" and "answer" in t.lower())
    crit = region_lines(secs, lambda k, t: True if is_crit(t) else (False if is_ans(k, t) else None))
    said_none = any(CRITIC_TITLE.search(t) and NO_CRITIC.search(t) for _, t, *_ in secs)
    answers = region_lines(secs, lambda k, t: False if CRITIC_TITLE.search(t) else (True if is_ans(k, t) else None))
    refs_only = lambda k, t: False if (REF_TITLE.search(bare(k, t)) or "not obtained" in t.lower()) else None
    bib = len(re.findall(r"^@\w+\{", body, re.M))
    if not nid:
        m = re.search(r"(?:review for|brief|Brief)\s+\*{0,2}([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+)\b", full) or \
            re.search(r"\b([A-Z]{2,}[0-9]*-[0-9]{1,3}[A-Z]?)\b", full[:6000])
        nid = m.group(1) if m else re.sub(r"[^A-Za-z0-9]+", "-", Path(path).stem)[:24].strip("-")
    sidecar = Path(path).with_suffix(".run.json")

    inv = []
    for title_c, lines in crit:
        for u in units(lines):
            if re.fullmatch(r"\**[A-Za-z ,()\-]+\**\s*(\(\d+\))?:?\**", u) or len(u.split()) < 4:
                continue            # a category label such as "**Access errors** (10):"
            parts = sentences(u) if (len(sentences(u)) > 2 or not re.match(r"[-*+]|\d+[.)]", u)) else [u]
            for s in parts:
                inv.append({"id": f"C-{len([x for x in inv if x['id'][0] == 'C']) + 1:03d}", "where": title_c,
                            "text": s})
    seen = set()
    norm = lambda s: re.sub(r"\W+", " ", s.lower()).strip()
    if labelled:
        ver = "exact (every labelled sentence, every answer sentence, and the critique)"
        keep = region_lines(secs, lambda k, t: False if (CRITIC_TITLE.search(t) or SKIP_TITLE.search(t)) else None,
                            default=True)
        n = 0
        for where, lines in keep:
            for u in units(lines):
                for s in sentences(u):
                    if labels_in(s) and norm(s) not in seen:
                        seen.add(norm(s))
                        n += 1
                        inv.append({"id": f"I-{n:04d}", "where": where, "text": s, "labels": labels_in(s)})
    if answers:
        if not labelled:
            ver = "fallback (answers and critique; the note has no labelled citations)"
        n = 0
        for where, lines in answers:
            for u in units(lines):
                for s in sentences(u):
                    if norm(s) in seen:      # the same answer in the callout and in the body
                        continue
                    seen.add(norm(s))
                    n += 1
                    inv.append({"id": f"A-{n:03d}", "where": where, "text": s})
    elif not labelled:
        ver = ("critique only (no labelled citations and no answers section found)" if crit
               else "not run (no labelled citations, answers or critique found)")
    # every other sentence of the note gets an address: not required, but a claim's `from` can point to it
    taken = {norm(x["text"]) for x in inv}
    n = 0
    for where, lines in region_lines(secs, refs_only, default=True):
        for u in units(lines):
            for s in sentences(u):
                if norm(s) not in taken:
                    taken.add(norm(s))
                    n += 1
                    inv.append({"id": f"B-{n:04d}", "where": where, "text": s})
    feats = {
        "id": nid, "path": str(path), "title": title,
        "critique": "yes" if crit else ("no (the note says none ran)" if said_none else "no"),
        "citations": style,
        "standing labels": f"yes ({with_standing} of {len(labels)} labels)" if with_standing else "no",
        "answers section": "yes" if answers else "no",
        "references": f"bibtex ({bib})" if bib else ("list" if any(REF_TITLE.search(s[1]) for s in secs)
                                                     else "not found"),
        "run record": "yes" if sidecar.exists() else "no",
        "omission check": ver,
        "inventory": Counter(x["id"][0] for x in inv if x["id"][0] != "B"),
        "body addresses": sum(1 for x in inv if x["id"][0] == "B"),
    }
    return feats, inv


def cmd_detect(argv):
    path = argv[0]
    nid = argv[argv.index("--id") + 1] if "--id" in argv else None
    feats, inv = detect(path, nid)
    for k, v in feats.items():
        print(f"{k:16} {dict(v) if isinstance(v, Counter) else v}")
    if "--inventory" in argv:
        out = Path(argv[argv.index("--inventory") + 1])
        with out.open("w", encoding="utf-8") as f:
            f.write(f"# Inventory of {feats['id']}\n\nOmission check: {feats['omission check']}\n\n"
                    "## Required: every item below must be accounted for\n\n")
            for x in inv:
                if x["id"][0] != "B":
                    f.write(f"- {feats['id']}:{x['id']} [{x['where'][:50]}] {x['text']}\n")
            f.write("\n## Body addresses: not required; cite them in `from` for findings the list above lacks\n\n")
            for x in inv:
                if x["id"][0] == "B":
                    f.write(f"- {feats['id']}:{x['id']} [{x['where'][:50]}] {x['text']}\n")
        print(f"inventory        {len(inv)} items -> {out}")


# ---------------------------------------------------------------- the knowledge note

CONF = re.compile(r"^(repl|single|cont|unclear|mixed|not stated)(?:\s*\((marker|critic: [^)]+|inputs: [^)]+|note: \"[^\"]+\")\))?$")
KLASS = re.compile(r"^(meas|deriv|model|assert|reading|search|not stated)(?:/(meas|deriv|model|assert))?"
                   r"(?:\s*\((marker|critic: [^)]+|note: \"[^\"]+\")\))?$")
FIELDS = {
    "claim": ({"conf", "class", "holds", "src", "trail", "from"}, {"rating"}),
    "background": ({"kind", "ref", "check"}, set()),
    "dns": ({"why", "instead", "from"}, {"trail"}),
    "gap": ({"blocks", "origin"}, {"from", "trail", "src"}),
}
INPUT_COLS = ("id", "note", "critique", "citations", "standing labels", "run record", "omission check")
ENTRY = re.compile(r"^- \*\*([a-z0-9][a-z0-9._-]*)\*\*\s+(.*)$")
FIELDLINE = re.compile(r"^\s{2,}(\w+):\s")
IDREF = re.compile(r"([A-Za-z0-9][A-Za-z0-9-]*):([ABCI])-(\d+)(?:\.\.(\d+))?")


def vault_root(p):
    for d in [p.parent, *p.parents]:
        if (d / ".obsidian").exists():
            return d
    return p.parent


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    try:
        import yaml
        return yaml.safe_load(m.group(1)) or {}
    except ImportError:
        out, key = {}, None
        for ln in m.group(1).splitlines():
            if re.match(r"\s+-\s", ln) and key:
                out.setdefault(key, []).append(ln.split("-", 1)[1].strip().strip('"'))
            elif ":" in ln:
                key, v = [x.strip() for x in ln.split(":", 1)]
                out[key] = v.strip('"') if v else []
        return out


def parse_bib(text):
    out = {}
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", text):
        start, depth, i = m.end(), 1, m.end()
        while i < len(text) and depth:
            depth += {"{": 1, "}": -1}.get(text[i], 0)
            i += 1
        body, fields, j = text[start:i - 1], {}, 0
        for fm in re.finditer(r"(\w+)\s*=\s*", body):
            if fm.start() < j:
                continue
            k, j = fm.group(1).lower(), fm.end()
            if j < len(body) and body[j] == "{":          # a braced value, braces nested to any depth
                depth, s = 0, j
                while j < len(body):
                    depth += {"{": 1, "}": -1}.get(body[j], 0)
                    j += 1
                    if depth == 0:
                        break
                fields[k] = body[s + 1:j - 1].strip()
            else:                                          # a bare value: 2020, or a quoted string
                v = re.match(r'"([^"]*)"|([^,\n]+)', body[j:])
                fields[k] = (v.group(1) if v.group(1) is not None else v.group(2)).strip() if v else ""
                j += v.end() if v else 0
        out[m.group(2)] = {"type": m.group(1).lower(), **fields}
    return out


# The vault's key formula (PhD/Proposal/Refs/Citation Key Format.md): auth.lower + shorttitle(3,3) + year. For
# research references the vault already has an implementation, PhD/Proposal/.hb/websearch/build_bibs.py make_key,
# which built collected.bib and not_obtained.bib; this mirrors it so keys from both agree. Sources already in
# Refs.bib keep their Zotero key (refs_keys, by DOI).
STOP = set("a an the of and or in on for to with from by at as into is are be its their this that these those via "
           "between within without under over versus vs than about across after before during some among".split())


def fold(s):
    """ASCII for accented letters, BibTeX accent commands included: Tun{\\aa} -> Tuna, Mar{\\'e}chal -> Marechal."""
    import unicodedata
    s = re.sub(r"\\(?:emph|textit|textbf|textsubscript|textsuperscript)\b", "", s)
    s = re.sub(r"\{?\\(?:aa|AA)\}?", "a", s).replace("\u00df", "ss").replace("\\ss", "ss")
    s = re.sub(r"\\[`'^\"~=.uvHckrb]\s*\{?(\w)\}?", r"\1", s)
    s = re.sub(r"\\[oO]\b", "o", s)
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()


def surname(name):
    """'Family, Given' keeps the whole family name (Gomez Exposito -> gomezexposito); 'Given Family' takes the
    last word; an organisation ({Name}, or more than two words without a comma) takes its first word."""
    name = name.strip()
    if name.startswith("{") and name.endswith("}") and "," not in name:
        name = name[1:-1]
        return name.split()[0] if name.split() else ""
    head, _, tail = name.partition(",")
    words = head.split()
    if not words:
        return ""
    if tail.strip():
        return head
    return words[-1] if len(words) <= 2 else words[0]


def citekey(author, title, year):
    """The key for a source not already in Refs.bib. author: a BibTeX author field; title and year as given."""
    first = re.split(r"\s+and\s+", (author or "").strip(), maxsplit=1)[0]
    sur = re.sub(r"[^a-z]", "", fold(surname(first)).lower()) or "anon"
    words = [w for w in re.findall(r"[A-Za-z0-9]+", fold(re.sub(r"[{}$]", "", title or "")).replace("-", ""))
             if w.lower() not in STOP]
    return f"{sur}{''.join(w[0].upper() + w[1:] for w in words[:3])}{year or ''}"


def refs_keys(bibpath):
    """{doi: key} from an existing bibliography, so a source already there keeps its key."""
    out = {}
    for k, e in parse_bib(Path(bibpath).read_text(encoding="utf-8")).items():
        if e.get("doi"):
            out[e["doi"].lower().strip()] = k
    return out


def split_fields(s):
    out = {}
    for part in re.split(r"\s+\u00b7\s+", s.strip()):
        m = re.match(r"(\w+):\s*(.*)", part.strip())
        if m:
            out[m.group(1)] = m.group(2).strip()
        else:
            out.setdefault("_bad", []).append(part)
    return out


def expand(ref):
    m = IDREF.fullmatch(ref.strip())
    if not m:
        return None
    a, kind, lo, hi = m.group(1), m.group(2), int(m.group(3)), int(m.group(4) or m.group(3))
    w = 4 if kind in "IB" else 3
    return [f"{a}:{kind}-{n:0{w}d}" for n in range(lo, hi + 1)]


def resolve_trail(t, inputs, secs_by):
    """'MB-01 §2.2', '§critic', '§answers', or the start of a callout's title ('§Integration read');
    returns [(id, title, kind)] or raises ValueError."""
    out = []
    for part in [x.strip() for x in t.split(",")]:
        m = re.match(r"([A-Za-z0-9][A-Za-z0-9-]*)\s+\u00a7\s*(.+)", part)
        if not m:
            m2 = re.match(r"\u00a7\s*(.+)", part)
            if not (m2 and out):
                raise ValueError(f"trail '{part}': write '<input id> §<heading>'")
            nid, h = out[-1][0], m2.group(1)
        else:
            nid, h = m.group(1), m.group(2)
        if nid not in inputs:
            raise ValueError(f"trail '{part}': no input with id {nid}")
        hl = h.strip().lower()
        secs = secs_by[nid]
        if hl in ("critic", "critique"):
            hit = next(((t2, k) for k, t2, *_ in secs if CRITIC_TITLE.search(t2)), None)
        elif hl == "answers":
            hit = next(((t2, k) for k, t2, *_ in secs if not CRITIC_TITLE.search(t2) and
                        (ANSWER_TITLE.search(bare(k, t2)) or "answer" in t2.lower())), None)
        else:
            hit = next(((t2, k) for k, t2, *_ in secs if
                        (bare(k, t2).lower().startswith(hl) or re.sub(r"^[\d.]+\s*", "", t2.lower()).startswith(hl))),
                       None)
        if not hit:
            raise ValueError(f"trail '{part}': no heading or callout in {nid} starts with '{h}'")
        out.append((nid, hit[0], hit[1]))
    return out


def sccs(nodes, edges):
    idx, low, st, on, out, n = {}, {}, [], set(), [], [0]

    def go(v):
        idx[v] = low[v] = n[0]
        n[0] += 1
        st.append(v)
        on.add(v)
        for w in edges.get(v, ()):
            if w not in idx:
                go(w)
                low[v] = min(low[v], low[w])
            elif w in on:
                low[v] = min(low[v], idx[w])
        if low[v] == idx[v]:
            comp = set()
            while True:
                w = st.pop()
                on.discard(w)
                comp.add(w)
                if w == v:
                    break
            out.append(comp)
    sys.setrecursionlimit(10000)
    for v in nodes:
        if v not in idx:
            go(v)
    return out


def lint(path):
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    errs, warns = [], []
    err, warn = errs.append, warns.append
    fm = frontmatter(text)
    if fm.get("type") != "knowledge":
        err("frontmatter: type: knowledge")
    root = vault_root(path)
    inputs, feats, invs, secs_by, texts = {}, {}, {}, {}, {}
    for item in fm.get("inputs") or []:
        if isinstance(item, dict):
            (nid, rel), = item.items()
        else:
            nid, rel = [x.strip() for x in str(item).split(":", 1)]
        p = root / str(rel).strip().strip('"')
        if not p.exists():
            err(f"input {nid}: {rel} not found under {root}")
            continue
        inputs[nid] = p
        feats[nid], inv = detect(p, nid)
        invs[nid] = {x["id"]: x for x in inv}
        texts[nid] = read(p)[1]
        secs_by[nid] = sections(texts[nid])
    if not inputs:
        err("frontmatter: inputs (a list of 'ID: vault/relative/path.md')")

    body = text.split("\n---\n", 1)[1] if text.startswith("---") else text
    lines = body.splitlines()
    part, concept, concepts, order, entries, oos = None, None, {}, [], [], []
    bibtext = "\n".join(re.findall(r"```bibtex\n(.*?)```", body, re.S))
    i = 0
    while i < len(lines):
        ln = lines[i]
        h2 = re.match(r"##\s+(.*)", ln)
        if h2 and not ln.startswith("###"):
            part = h2.group(1).strip().lower()
            concept = None
        h3 = re.match(r"###\s+([a-z0-9][a-z0-9-]*):\s+(.+)", ln)
        if h3 and part == "concepts":
            concept = h3.group(1)
            if concept in concepts:
                err(f"concept {concept}: defined twice")
            concepts[concept] = {"name": h3.group(2).strip(), "needs": None, "group": None, "line": i}
            order.append(concept)
        m = re.match(r"(needs|group):\s*(.*)", ln)
        if m and concept and part == "concepts":
            v = m.group(2).strip()
            concepts[concept][m.group(1)] = ([x.strip() for x in v.split(",") if x.strip() and x.strip() != "none"]
                                             if m.group(1) == "needs" else v)
        e = ENTRY.match(ln)
        if e:
            eid, stmt, f = e.group(1), e.group(2), {}
            j = i + 1
            while j < len(lines) and FIELDLINE.match(lines[j]):
                f.update(split_fields(lines[j]))
                j += 1
            kind = {"do not say": "dns", "gaps": "gap"}.get(part, "claim")
            if part == "concepts" and f.get("kind") == "background":
                kind = "background"
            if part not in ("concepts", "do not say", "gaps"):
                err(f"{eid}: entry outside Concepts, Do not say or Gaps")
            entries.append({"id": eid, "type": kind, "concept": concept if part == "concepts" else None,
                            "statement": stmt, "fields": f, "line": i + 1})
            i = j
            continue
        o = re.match(rf"- ((?:{IDREF.pattern})(?:,\s*(?:{IDREF.pattern}))*):\s+(.+)$", ln)
        if o and part == "out of scope":
            refs = [x.strip() for x in o.group(1).split(",")]
            oos.append((refs, o.group(2)))
        i += 1

    for want in ("concepts", "do not say", "gaps", "out of scope", "sources", "inputs"):
        if not re.search(rf"^##\s+{want}\s*$", body, re.I | re.M):
            err(f"missing section '## {want.capitalize()}'")
    bib = parse_bib(bibtext)
    refbib = {}
    if fm.get("refs"):                       # an existing bibliography whose keys sources keep (by DOI)
        rp = root / str(fm["refs"])
        if rp.exists():
            refbib = refs_keys(rp)
        else:
            err(f"frontmatter: refs {fm['refs']} not found under {root}")
    if not bib:
        err("Sources: no ```bibtex block with entries")

    # concepts: the needs graph is the artefact; mutual dependence is declared as a group
    edges = {c: v["needs"] or [] for c, v in concepts.items()}
    for c, v in concepts.items():
        if v["needs"] is None:
            err(f"concept {c}: needs: line missing (write 'needs: none' for a root)")
        for n in edges[c]:
            if n not in concepts:
                err(f"concept {c}: needs '{n}', which is not a concept")
    comps = sccs(order, {c: [n for n in e if n in concepts] for c, e in edges.items()})
    comp_of = {c: k for k, comp in enumerate(comps) for c in comp}
    groups = defaultdict(set)
    for c, v in concepts.items():
        if v["group"]:
            groups[v["group"]].add(c)
    for comp in comps:
        if len(comp) > 1:
            gs = {concepts[c]["group"] for c in comp}
            if len(gs) != 1 or None in gs:
                err(f"concepts {', '.join(sorted(comp))} depend on each other: give them one shared 'group:'")
    for g, members in groups.items():
        if len({comp_of[c] for c in members}) > 1:
            err(f"group {g}: {', '.join(sorted(members))} are not mutually dependent; a group is for concepts "
                "that need each other")
    pos = {c: k for k, c in enumerate(order)}
    for c in order:
        for n in edges[c]:
            if n in pos and pos[n] > pos[c] and comp_of.get(n) != comp_of.get(c):
                err(f"concept {c} comes before {n}, which it needs: the file order must be a valid ordering")
    for g, members in groups.items():
        ps = sorted(pos[c] for c in members)
        if ps and ps[-1] - ps[0] + 1 != len(ps):
            err(f"group {g}: its concepts are not next to each other")

    # entries
    ids = Counter(e["id"] for e in entries)
    for k, v in ids.items():
        if v > 1:
            err(f"{k}: id used {v} times")
    known = {e["id"] for e in entries}
    covered = defaultdict(list)
    trails = {}
    for e in entries:
        f, eid, req_opt = e["fields"], e["id"], FIELDS[e["type"]]
        for bad in f.pop("_bad", []):
            err(f"{eid}: '{bad[:50]}' is not 'field: value' (fields are separated by ' \u00b7 ')")
        missing = req_opt[0] - set(f)
        if missing:
            err(f"{eid}: missing {', '.join(sorted(missing))}")
        for k in req_opt[0] & set(f):
            if not f[k].strip():
                err(f"{eid}: {k} is empty")
        if e["type"] in ("claim", "dns") and f.get("from", "").strip().lower().startswith("none"):
            err(f"{eid}: from: none; cite the note's own sentences (body addresses B-nnnn reach every sentence)")
        if f.get("src", "").startswith("none") and not re.match(r"none \(.+\)$", f["src"]):
            err(f"{eid}: src: none needs its reason in brackets, e.g. 'none (the reviewer's synthesis)'")
        if "rating" in f:
            q = re.fullmatch(r'"([^"]+)"', f["rating"].strip())
            if not q:
                err(f"{eid}: rating is the note's own words in quotes: rating: \"Moderate\"")
            elif not any(q.group(1).lower() in tx.lower() for tx in texts.values()):
                err(f'{eid}: rating "{q.group(1)}" is not in any input note')
        unknown = set(f) - req_opt[0] - req_opt[1]
        if unknown:
            err(f"{eid}: unknown field(s) {', '.join(sorted(unknown))}; the format has no others")
        if e["type"] == "claim" and not e["concept"]:
            err(f"{eid}: claim outside a concept")
        if e["type"] == "claim":
            for fld, rx in (("conf", CONF), ("class", KLASS)):
                v = f.get(fld, "")
                mm = rx.match(v)
                if not mm:
                    err(f"{eid}: {fld} '{v}' (values and basis: see references/format.md)")
                    continue
                basis = mm.groups()[-1]
                if mm.group(1) != "not stated" and not basis:
                    err(f"{eid}: {fld} {mm.group(1)} needs its basis: (marker), (critic: C-nnn) or "
                        "(note: \"words from the note\")")
                if basis and basis.startswith("critic:"):
                    for ref in re.split(r",\s*", basis[7:].strip()):
                        ref = ref if ":" in ref else (f"{next(iter(invs))}:{ref}" if len(invs) == 1 else ref)
                        got = expand(ref)
                        if not got:
                            err(f"{eid}: {fld} basis '{ref}': write critic: <ID>:C-nnn (the ID may be left off "
                                "when there is one input)")
                        elif any(g.split(":")[0] not in invs or g.split(":")[1] not in invs[g.split(":")[0]]
                                 for g in got):
                            err(f"{eid}: {fld} basis {ref} is not in the inventory")
                if basis and basis.startswith("note:"):
                    quote = basis[7:-1]
                    if not any(quote.lower() in t.lower() for t in texts.values()):
                        err(f"{eid}: {fld} quotes \"{quote}\", which is not in any input note")
                if basis == "marker" and not any(feats[n]["citations"].startswith("labelled") for n in feats):
                    err(f"{eid}: {fld} (marker) but no input has labelled citations")
        if e["type"] == "background":
            if f.get("kind") != "background":
                err(f"{eid}: kind: background")
            if f.get("ref") and f["ref"] not in bib:
                err(f"{eid}: ref {f['ref']} is not in Sources")
            elif f.get("ref") and "background" not in bib[f["ref"]].get("note", ""):
                err(f"{eid}: its source's note must say 'background'")
        srcs = re.sub(r"\([^)]*\)", "", f.get("src", ""))
        for key in re.split(r"[,;]\s*", srcs) if f.get("src") and not f["src"].startswith("none") else []:
            if key.strip() and key.split()[0] not in bib:
                err(f"{eid}: src {key.split()[0]} is not in Sources")
        if f.get("instead") and f["instead"] != "none":
            for x in re.split(r",\s*", f["instead"]):
                if x not in known:
                    err(f"{eid}: instead {x} is not an entry")
        if f.get("blocks"):
            for x in re.split(r",\s*", f["blocks"]):
                if x not in known and x not in concepts:
                    err(f"{eid}: blocks {x} is neither an entry nor a concept")
        if f.get("trail"):
            try:
                trails[eid] = resolve_trail(f["trail"], inputs, secs_by)
            except ValueError as ex:
                err(f"{eid}: {ex}")
        for ref in re.split(r",\s*", f.get("from", "")) if f.get("from") else []:
            got = expand(ref)
            if not got:
                err(f"{eid}: from '{ref}' (write ID:I-0012, ID:A-003 or ID:C-004, ranges ID:I-0012..0015)")
                continue
            for g in got:
                nid, iid = g.split(":")
                if nid not in invs or iid not in invs[nid]:
                    err(f"{eid}: from {g} is not in the inventory")
                else:
                    covered[g].append(eid)
    for refs, reason in oos:
        for ref in refs:
            got = expand(ref)
            if not got:
                err(f"out of scope '{ref}': not an inventory reference")
                continue
            for g in got:
                covered[g].append(f"out of scope: {reason[:40]}")

    # omission: every inventory item is a claim, a do-not-say entry, a gap, or out of scope with a reason
    required = {nid: [i for i in inv if not i.startswith("B-")] for nid, inv in invs.items()}
    omitted = {nid: [i for i in req if f"{nid}:{i}" not in covered] for nid, req in required.items()}
    for nid, miss in omitted.items():
        if miss:
            err(f"omission ({nid}, {feats[nid]['omission check'].split(' (')[0]}): {len(miss)} of {len(required[nid])} "
                f"items not accounted for: {', '.join(miss[:12])}{' ...' if len(miss) > 12 else ''}")
    for k, src in bib.items():
        used = any(k in re.split(r"[,;\s]+", e["fields"].get("src", "") + " " + e["fields"].get("ref", ""))
                   for e in entries)
        if not used and not re.search(r"not_obtained|not cited|listed only", src.get("note", "")):
            warn(f"source {k} is cited by no entry (if the note lists it without citing it, say so in its note)")
        reuse = refbib.get((src.get("doi") or "").lower().strip())
        year = re.search(r"\d{4}", src.get("year", "") or src.get("date", ""))
        want = reuse or citekey(src.get("author", ""), src.get("title", ""), year.group(0) if year else "")
        if re.sub(r"[a-z]$", "", k) != want and k != want:
            warn(f"source {k}: the key rule gives {want}" + (" (its key in the refs bibliography)" if reuse else ""))

    # the Inputs table must report what detection found
    head = next((k for k, ln in enumerate(lines) if ln.startswith("|") and re.search(r"\|\s*id\s*\|", ln, re.I)), None)
    cols = [c.strip().lower() for c in lines[head].strip("|").split("|")] if head is not None else []
    for want in INPUT_COLS:
        if want not in cols:
            err(f"Inputs table: column '{want}' missing (columns: {', '.join(INPUT_COLS)})")
    for nid, ft in feats.items():
        row = next((ln for ln in lines if ln.startswith("|") and re.match(rf"\|\s*{re.escape(nid)}\s*\|", ln)), None)
        if not row or not cols:
            err(f"Inputs: no row for {nid}")
            continue
        cell = dict(zip(cols, [c.strip().replace("**", "") for c in row.strip("|").split("|")]))
        for k in ("critique", "citations", "standing labels", "run record", "omission check"):
            want = ft[k].split(" (")[0]
            if k in cell and not cell[k].startswith(want):
                err(f"Inputs {nid}: {k} is '{cell[k]}', detected '{ft[k]}'")

    index = {
        "note": str(path.relative_to(root)) if root in path.parents else str(path),
        "inputs": {nid: {**{k: (dict(v) if isinstance(v, Counter) else v) for k, v in feats[nid].items()},
                         "path": str(inputs[nid].relative_to(root))} for nid in feats},
        "checks": {"errors": len(errs), "warnings": len(warns),
                   "omission": {nid: {"version": feats[nid]["omission check"], "items": len(required[nid]),
                                      "accounted": len(required[nid]) - len(omitted[nid])} for nid in invs}},
        "concepts": [{"id": c, **{k: v for k, v in concepts[c].items() if k != "line"}, "order": k}
                     for k, c in enumerate(order)],
        "groups": {g: sorted(m) for g, m in groups.items()},
        "entries": [{**{k: v for k, v in e.items() if k != "line"},
                     "trail_links": [f"[[{inputs[n].relative_to(root).with_suffix('')}#{h}]]" if k == "heading" else
                                     f"[[{inputs[n].relative_to(root).with_suffix('')}]] (callout: {bare(k, h)})"
                                     for n, h, k in trails.get(e["id"], [])]} for e in entries],
        "sources": bib,
    }
    out = path.with_suffix(".index.json")
    out.write_text(json.dumps(index, indent=1, ensure_ascii=False), encoding="utf-8")
    counts = Counter(e["type"] for e in entries)
    print(f"{path.name}: {len(concepts)} concepts ({len([g for g in groups])} groups), "
          f"{counts['claim']} claims, {counts['background']} background, {counts['dns']} do-not-say, "
          f"{counts['gap']} gaps, {len(bib)} sources")
    for nid in invs:
        print(f"  omission {nid}: {feats[nid]['omission check'].split(' (')[0]}, "
              f"{len(required[nid]) - len(omitted[nid])}/{len(required[nid])} accounted for")
    for w in warns:
        print("  warn:", w)
    for e in errs:
        print("  ERROR:", e)
    print(f"  index -> {out.name}; {len(errs)} errors, {len(warns)} warnings")
    return 1 if errs else 0


def packets(path, outdir, per=60):
    """For the faithfulness check: each entry beside the exact note text it says it came from."""
    path = Path(path)
    idx = path.with_suffix(".index.json")
    if not idx.exists():
        lint(path)
    index = json.loads(idx.read_text(encoding="utf-8"))
    root = vault_root(path)
    items = {}
    for nid, ft in index["inputs"].items():
        for x in detect(root / ft["path"], nid)[1]:
            items[f"{nid}:{x['id']}"] = x
    ents = [e for e in index["entries"] if e["type"] in ("claim", "dns")]
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    files = []
    for k in range(0, len(ents), per):
        f = outdir / f"packet-{k // per + 1:02d}.md"
        with f.open("w", encoding="utf-8") as w:
            for e in ents[k:k + per]:
                fl = e["fields"]
                w.write(f"## {e['id']} ({'do not say' if e['type'] == 'dns' else 'claim'})\n\n{e['statement']}\n\n")
                w.write("".join(f"- {k2}: {v}\n" for k2, v in fl.items() if k2 != "from"))
                w.write("\nFrom the note:\n\n")
                bases = re.findall(r"critic: ([^)]+)\)", fl.get("conf", "") + " " + fl.get("class", ""))
                refs = re.split(r",\s*", fl.get("from", "")) + [
                    r if ":" in r else f"{next(iter(index['inputs']))}:{r}"
                    for b in bases for r in re.split(r",\s*", b.strip())]
                for ref in refs:
                    for g in expand(ref) or []:
                        x = items.get(g)
                        w.write(f"> {g} [{x['where'][:40]}] {x['text']}\n>\n" if x else f"> {g}: not in inventory\n>\n")
                w.write("\n")
        files.append(f)
    print(f"{len(ents)} entries in {len(files)} packets -> {outdir}")


def cmd_citekey(argv):
    opt = {k: argv[argv.index(f"--{k}") + 1] for k in ("author", "title", "year", "doi", "refs") if f"--{k}" in argv}
    if opt.get("doi") and opt.get("refs"):
        hit = refs_keys(opt["refs"]).get(opt["doi"].lower().strip())
        if hit:
            print(hit)
            return
    print(citekey(opt.get("author", ""), opt.get("title", ""), opt.get("year", "")))


if __name__ == "__main__":
    cmds = ("detect", "lint", "packets", "citekey")
    if len(sys.argv) < 3 or sys.argv[1] not in cmds:
        print(__doc__)
        sys.exit(2)
    if sys.argv[1] == "detect":
        sys.exit(cmd_detect(sys.argv[2:]) or 0)
    if sys.argv[1] == "citekey":
        sys.exit(cmd_citekey(sys.argv[2:]) or 0)
    if sys.argv[1] == "packets":
        sys.exit(packets(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "packets") or 0)
    sys.exit(lint(sys.argv[2]))
