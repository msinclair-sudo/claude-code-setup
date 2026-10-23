#!/usr/bin/env python3
"""consolidate: read research result notes as they are, and check the knowledge note built from them.

  kn.py detect NOTE [--id ID] [--inventory OUT.md]   what the note has, which checks can run, and the
                                                     inventory of items the knowledge note must account for
  kn.py lint KNOWLEDGE.md                            check the knowledge note; write KNOWLEDGE.index.json
  kn.py packets KNOWLEDGE.md OUTDIR [--only IDS] [--hints]
                                                     each claim and do-not-say entry beside the note text it
                                                     came from, for the faithfulness checker; --only takes
                                                     comma-separated entry IDs (the fixed ones, for the re-check);
                                                     --hints adds, under each entry, the words not found in its
                                                     cited text (for the checker only, never the builder)
  kn.py spotcheck KNOWLEDGE.md OUT.md [--n 20 --seed S]
                                                     a random sample of entries, each with its from text and
                                                     trail, for a person to judge (the seed is recorded)
  kn.py view KNOWLEDGE.md [OUT.md]                   the writer's view, from the index: each question's
                                                     answer (the critic's version where there is one), the
                                                     concepts with each claim and its standing, what not to
                                                     say, the gaps; no provenance
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
REFUTED_TITLE = re.compile(r"refuted|killed in verification", re.I)      # refutations, not a second reader's critique
ANSWER_TITLE = re.compile(r"^(?:\d+\.\s*)?(?:answers?\b|verdicts?\b|provisional verdicts?\b|assessment\b|"
                          r"quantitative synthesis\b)|answers as delivered|answers in brief", re.I)
NO_CRITIC = re.compile(r"\bno\b|not run|without|was not", re.I)
# A references heading is the whole title ("References", "Sources (12)"), never the start of a longer one: a note
# titled "Sources of functional covariation" is not its own reference list.
REF_TITLE = re.compile(r"^(?:\d+\.\s*)?(?:references?|reference list|bibliography|sources|works cited)"
                       r"(?:\s*\([^)]*\))?\s*:?$", re.I)
SKIP_TITLE = re.compile(r"note role|provenance|search record|sources not obtained|references?$|reference list|"
                        r"bibliography|stage.?2|conventions|verification log", re.I)
SENT = re.compile(r"(?<=[.!?])[\"')\]]*\s+(?=[A-Z(\[\"*])")
ABBR = re.compile(r"(?:\b(?:St|Dr|Mr|Ms|Mrs|Prof|Fig|Figs|Eq|No|Vol|cf|vs|al|approx|ca|Inc|Ltd|Co|sp|spp|e\.g|i\.e|"
                  r"Supp|Suppl|Tab|Ref|Refs|Ch|Sect)\.|(?<![\w.])[A-Z]\.)$")     # "J. Smith", "Supp. Fig. 3"


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


def region_lines(secs, want, default=False, title_at=None):
    """Lines of the sections `want` picks. want(kind, title) is True, False, or None to inherit from the enclosing
    heading (default at the top), so an excluded section excludes its subsections and an included one includes
    them. A callout belongs to the heading above it unless want decides it. The note's own title (the heading at
    line `title_at`) never decides: its words describe the note, not a section."""
    out, stack = [], []          # (level, included)
    for kind, title, level, lines, at in secs:
        if kind == "heading":
            while stack and stack[-1][0] >= level:
                stack.pop()
        parent = stack[-1][1] if stack else default
        w = None if (kind == "heading" and at == title_at) else want(kind, title)
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


def is_bullet(u):
    return bool(re.match(r"([-*+]|\d+[.)])\s+", u))


def detect(path, nid=None, declared=None):
    """What a result note has, and its inventory. `declared`: answer sections the knowledge note's frontmatter names
    for this input (heading starts, '§' optional), for answers under headings detection does not know; or
    'none (reason)'."""
    full, body, _ = read(path)
    secs = sections(body)
    title = next((t for k, t, lv, _, _ in secs if k == "heading" and lv == 1), Path(path).stem)
    title_at = next((at for k, t, lv, _, at in secs if k == "heading" and lv == 1), None)
    decl = declared if isinstance(declared, list) else []
    decl_none = isinstance(declared, str) and declared.strip().lower().startswith("none")
    labels = [label_parts(m.group(1)) for m in BRACKET.finditer(body)]
    labels = [st for ok, st in labels if ok]
    with_standing = sum(1 for st in labels if st)
    labelled = len(labels) >= 10          # a few stray labels (MB-02 has 3) do not make a labelling convention
    style_counts = {k: len(p.findall(body)) for k, p in STYLES.items()}
    style = "labelled (access; class; standing)" if labelled else (
        max(style_counts, key=style_counts.get) if max(style_counts.values()) >= 5 else "none found")
    is_crit = lambda t: bool(CRITIC_TITLE.search(t)) and not re.search(r"stage.?2", t, re.I) and not NO_CRITIC.search(t)
    is_decl = lambda k, t: any(bare(k, t).lower().startswith(d.lstrip("§ ").lower()) for d in decl if d.strip("§ "))
    is_ans = lambda k, t: (bool(ANSWER_TITLE.search(bare(k, t))) or (k == "callout" and "answer" in t.lower())
                           or is_decl(k, t))
    crit = region_lines(secs, lambda k, t: True if is_crit(t) else (False if is_ans(k, t) else None),
                        title_at=title_at)
    said_none = any(CRITIC_TITLE.search(t) and NO_CRITIC.search(t) for _, t, *_ in secs)
    refuted_only = bool(crit) and all(REFUTED_TITLE.search(t) and not re.search(r"critic|critique|adversarial", t, re.I)
                                      for t, _ in crit)
    answers = region_lines(secs, lambda k, t: False if CRITIC_TITLE.search(t) else (True if is_ans(k, t) else None),
                           title_at=title_at)
    is_refs = lambda k, t: bool(REF_TITLE.search(bare(k, t).strip())) or "not obtained" in t.lower()
    refs_only = lambda k, t: False if is_refs(k, t) else None
    bib = len(re.findall(r"^@\w+\{", body, re.M))
    if not nid:
        m = re.search(r"(?:review for|brief|Brief)\s+\*{0,2}([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+)\b", full) or \
            re.search(r"\b([A-Z]{2,}[0-9]*-[0-9]{1,3}[A-Z]?)\b", full[:6000])
        nid = m.group(1) if m else re.sub(r"[^A-Za-z0-9]+", "-", Path(path).stem)[:24].strip("-")
    sidecar = Path(path).with_suffix(".run.json")

    inv = []
    occupied = set()        # (section, unit, sentence) positions that already have a required address
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
                            default=True, title_at=title_at)
        n = 0
        for where, lines in keep:
            for ui, u in enumerate(units(lines)):
                ss = sentences(u)
                lab = [bool(labels_in(s)) for s in ss]
                if is_bullet(u) and len(ss) > 1 and lab[-1] and sum(lab) == 1:
                    found = [(range(len(ss)), u)]          # one label ending a bullet covers the bullet
                else:
                    found = [([k], s) for k, s in enumerate(ss) if lab[k]]
                for ks, s in found:
                    if norm(s) in seen:                    # a repeat gets a body address below
                        continue
                    seen.add(norm(s))
                    occupied.update((id(lines), ui, k) for k in ks)
                    n += 1
                    inv.append({"id": f"I-{n:04d}", "where": where, "text": s, "labels": labels_in(s)})
    if answers:
        if not labelled:
            ver = "fallback (answers and critique; the note has no labelled citations)"
        n = 0
        for where, lines in answers:
            for ui, u in enumerate(units(lines)):
                for k, s in enumerate(sentences(u)):
                    if norm(s) in seen:      # the same answer in the callout and in the body
                        continue
                    seen.add(norm(s))
                    occupied.add((id(lines), ui, k))
                    n += 1
                    inv.append({"id": f"A-{n:03d}", "where": where, "text": s})
    elif not labelled:
        ver = ("critique only (no labelled citations and no answers section found)" if crit
               else "not run (declared: no answer sections)" if decl_none
               else "not run (no labelled citations, answers or critique found)")
    # every other sentence of the note gets an address: not required, but a claim's `from` can point to it. Each
    # occurrence gets its own, so a repeated line ("*Strength:* Moderate.") can be cited where it stands. The
    # critique has its own addresses (C-nnn); the reference list and the sources-not-obtained list theirs (R-nnnn),
    # so a finding that lives only in a reference annotation can still be cited.
    in_crit = {id(lines) for _, lines in crit}
    n = 0
    for where, lines in region_lines(secs, refs_only, default=True, title_at=title_at):
        if id(lines) in in_crit:
            continue
        for ui, u in enumerate(units(lines)):
            for k, s in enumerate(sentences(u)):
                if (id(lines), ui, k) not in occupied:
                    n += 1
                    inv.append({"id": f"B-{n:04d}", "where": where, "text": s})
    n = 0
    for where, lines in region_lines(secs, lambda k, t: True if is_refs(k, t) else None, title_at=title_at):
        if id(lines) in in_crit:
            continue
        for u in units(lines):
            for s in sentences(u):
                n += 1
                inv.append({"id": f"R-{n:04d}", "where": where, "text": s})
    # coverage: every section with text should have given at least one address; a section that gave none (or a
    # reference list that swallowed the body) is a detection miss, reported so that lint can fail loudly
    addressed = {x["where"] for x in inv}
    unaddressed = []
    for kind, t, lv, lines, at in secs:
        nsent = sum(len(sentences(u)) for u in units(lines))
        if nsent and t not in addressed and at != title_at:
            unaddressed.append(f"{bare(kind, t)[:60]} ({nsent} sentences)")
    kinds = Counter(x["id"][0] for x in inv)
    feats = {
        "id": nid, "path": str(path), "title": title,
        "critique": ("refutations only" if refuted_only else "yes") if crit else
                    ("no (the note says none ran)" if said_none else "no"),
        "citations": style,
        "standing labels": f"yes ({with_standing} of {len(labels)} labels)" if with_standing else "no",
        "answers section": "yes" if answers else "no",
        "references": f"bibtex ({bib})" if bib else ("list" if any(REF_TITLE.search(s[1]) for s in secs)
                                                     else "not found"),
        "run record": "yes" if sidecar.exists() else "no",
        "omission check": ver,
        "inventory": Counter(x["id"][0] for x in inv if x["id"][0] not in "BR"),
        "body addresses": kinds["B"],
        "reference addresses": kinds["R"],
        "unaddressed sections": unaddressed,
    }
    return feats, inv


# ---------------------------------------------------------------- questions and answers, for the writer's view

ANS_LABEL = re.compile(r"^(?:[-*+]\s+)?\*\*((?:(?:D\d+|Q(?:uestion)?\s*\d+)\b|\([a-z]\)\s)[^*]*?)[:.]?\*\*[:.]?\s*(.*)$",
                       re.S)


def ans_key(label):
    """'D1 (a) 16S copies per genome' -> 'D1 (a)'; 'D2: definitions' -> 'D2'; 'Question 1 — ...' -> 'D1';
    '(a) Single authoritative taxonomy?' -> '(a)'."""
    if re.match(r"\([a-z]\)\s", label.strip()):
        return label.strip()[:3]
    m = re.match(r"(?:D|Q(?:uestion)?\s*)(\d+)(?:,?\s*case\s*([A-Za-z](?:/[A-Za-z])*)\b|,?\s*(?:case\s*)?\(([a-z])\))?",
                 label.strip())
    if not m:
        return label.strip()
    case = m.group(2) or m.group(3)
    return f"D{m.group(1)}" + (f" ({case})" if case else "")


def plain(s):
    """Answer text without citation markers and labels ([3], [30, FT], [S1], [FT; meas; repl], [[links]])."""
    s = re.sub(r"\[\[([^\]|]+\|)?([^\]]+)\]\]", r"\2", s)
    s = re.sub(r"\s*\[(?:\d[^\[\]]{0,60}|S\d+[^\[\]]{0,40}|(?:FT|AB|SEC)\b[^\[\]]{0,60})\]", "", s)
    s = BRACKET.sub(lambda m: "" if label_parts(m.group(1))[0] else m.group(0), s)
    return re.sub(r"\s{2,}", " ", s).strip()


def labelled_blocks(lines, stop_at_blank=False):
    """[(key or None, label, text)]: a line opening with **D1...** or **Question 1...** starts an answer; other
    lines continue the one before (a blank line keeps the paragraph break). With stop_at_blank, the first blank
    line after an answer has started ends the list (the critic's reformulated answers, before its assessment)."""
    out, gap = [], False
    for ln in lines:
        s = ln.strip()
        if not s or re.fullmatch(r"-{3,}|```.*", s):
            if out and stop_at_blank:
                break
            gap = True
            continue
        m = ANS_LABEL.match(s)
        if m:
            out.append([ans_key(m.group(1)), m.group(1).strip(), m.group(2).strip()])
        elif out:
            out[-1][2] += ("\n\n" if gap else " ") + s
        else:
            out.append([None, "", s])
        gap = False
    return [tuple(x) for x in out if x[2].strip()]


def note_answers(path, declared=None):
    """The note's answers: the critic's reformulated answers or verdict where it gave them, otherwise the note's
    answers, verdict or assessment sections (and any declared ones). [{key, label, text, raw, source}]; `raw` keeps
    the citation markers, which the writer's view turns into author and year."""
    _, body, _ = read(path)
    secs = sections(body)
    decl = declared if isinstance(declared, list) else []
    crit = []
    for kind, title, _, lines, _ in secs:
        if kind == "callout" and CRITIC_TITLE.search(title) and not NO_CRITIC.search(title):
            joined = "\n".join(lines)
            if re.search(r"reformulated (?:answers?|verdicts?)", joined, re.I):
                after = re.split(r"\*\*reformulated (?:answers?|verdicts?):?\*\*:?", joined, flags=re.I)[-1].splitlines()
                blocks = labelled_blocks(after, stop_at_blank=True)
                crit = [b for b in blocks if b[0]] or blocks[:1]      # an unlabelled verdict is one answer
                break
    body_ans = []
    for kind, title, _, lines, _ in secs:      # every answers, verdict or assessment section of the body
        b = bare(kind, title)
        if kind == "heading" and not CRITIC_TITLE.search(title) and (
                ANSWER_TITLE.search(b) or "answer" in b.lower()
                or any(b.lower().startswith(d.lstrip("§ ").lower()) for d in decl if d.strip("§ "))):
            blocks = labelled_blocks(lines)
            if blocks and not any(k for k, *_ in blocks):
                blocks = [(None, b, "\n\n".join(t for _, _, t in blocks))]    # an unlabelled section: one answer
            body_ans += blocks
    if not body_ans:
        for kind, title, _, lines, _ in secs:
            if kind == "callout" and "answer" in title.lower() and not CRITIC_TITLE.search(title):
                body_ans = labelled_blocks(lines)
                break
    out = [{"key": k, "label": lb, "text": plain(t), "raw": t, "source": "critic"} for k, lb, t in crit]
    have = {k for k, *_ in crit}
    out += [{"key": k, "label": lb, "text": plain(t), "raw": t, "source": "review"} for k, lb, t in body_ans
            if not (k and (k in have or k.split(" (")[0] in {h.split(" (")[0] for h in have}))]
    return out


def find_note(root, name):
    name = name.split("|")[0].split("#")[0].strip()
    for p in root.rglob(f"{name}.md"):
        if ".trash" not in p.parts and not any(x.startswith(".") for x in p.relative_to(root).parts):
            return p
    return None


def brief_questions(path, nid, root):
    """The questions the research asked, verbatim from the AGENT BRIEF its Note Role links to (the block for this
    ID, or the only one), else the note's own question headings. ({key: question}, where they came from)."""
    full, body, _ = read(path)
    role = next(("\n".join(ln) for k, t, _, ln, _ in sections(body) if k == "callout" and "note role" in t.lower()),
                "")
    link = re.search(r"\[\[([^\]]+)\]\]", role)
    brief = find_note(root, link.group(1)) if link else None
    if brief:
        btext = brief.read_text(encoding="utf-8", errors="replace")
        blocks = re.split(r"^#### ", btext, flags=re.M)[1:]
        blocks = [b for b in blocks if "AGENT BRIEF" in b]
        named = re.search(r"(?:review|result) for (?:brief )?\*{0,2}([A-Z][A-Za-z0-9-]+)", role)
        pick = [b for b in blocks if b.split(":")[0].split()[0] in (nid, named.group(1) if named else nid)]
        block = pick[0] if pick else (blocks[0] if len(blocks) == 1 else None)
        if block:
            agent = block.split("[!note] ROUTING")[0].split("[!example] DISPATCH")[0]
            qs = {f"D{m.group(1)}": m.group(2).strip()
                  for m in re.finditer(r"^>\s*-\s*\*\*D(\d+)\.?\*\*\s*(.+)$", agent, re.M)}
            if not qs:
                m = re.search(r"^>\s*\*\*Question:\*\*\s*(.+)$", agent, re.M)
                qs = {"D1": m.group(1).strip()} if m else {}
            if qs:
                return qs, f"the AGENT BRIEF in {brief.relative_to(root).with_suffix('')}"
    qs = {f"D{m.group(1)}": m.group(2).strip() for m in
          re.finditer(r"^#{1,4}\s+Q(?:uestion)?\s*(\d+)\s*[—:\-–.]+\s*(.+)$", body, re.M)}
    return qs, ("the note's own question headings" if qs else "not stated in the note or a linked brief")


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
                if x["id"][0] not in "BR":
                    f.write(f"- {feats['id']}:{x['id']} [{x['where'][:50]}] {x['text']}\n")
            f.write("\n## Body addresses: not required; cite them in `from` for findings the list above lacks\n\n")
            for x in inv:
                if x["id"][0] == "B":
                    f.write(f"- {feats['id']}:{x['id']} [{x['where'][:50]}] {x['text']}\n")
            f.write("\n## Reference addresses: not required; the reference list and sources not obtained, for a "
                    "finding that lives only there\n\n")
            for x in inv:
                if x["id"][0] == "R":
                    f.write(f"- {feats['id']}:{x['id']} [{x['where'][:50]}] {x['text']}\n")
        print(f"inventory        {len(inv)} items -> {out}")


# ---------------------------------------------------------------- the knowledge note

CONF = re.compile(r"^(repl|single|cont|unclear|mixed|not stated)(?:\s*\((marker|critic: [^)]+|inputs: [^)]+|note: \"[^\"]+\")\))?$")
# Search status of an absence or a gap, and whether contrary evidence was looked for: never inferred.
SEARCH = re.compile(r"^(searched, not found|not searched|not stated)(?:\s*\((note: \"[^\"]+\"|critic: [^)]+|run: [^)]+)\))?$")
CONTRARY = re.compile(r"^(searched|one-sided|not stated)(?:\s*\((note: \"[^\"]+\"|critic: [^)]+|run: [^)]+)\))?$")
RATING = re.compile(r'^"([^"]+)"(?:\s*\(critic:\s*((?:[A-Za-z0-9][A-Za-z0-9-]*:)?C-\d+):\s*([^)]+)\))?$')
SECOND_READER = re.compile(r"second reader|never checked|not checked by|no critic", re.I)
KLASS = re.compile(r"^(meas|deriv|model|assert|reading|search|not stated)(?:/(meas|deriv|model|assert))?"
                   r"(?:\s*\((marker|critic: [^)]+|note: \"[^\"]+\")\))?$")
LIMIT = re.compile(r"^(access|access and evidence)\s*\((critic: [^)]+|note: \"[^\"]+\")\)$")
CRITREF = re.compile(r"critic:\s*((?:[A-Za-z0-9][A-Za-z0-9-]*:)?C-\d+(?:\.\.\d+)?"
                     r"(?:\s*,\s*(?:[A-Za-z0-9][A-Za-z0-9-]*:)?C-\d+(?:\.\.\d+)?)*)")
# The words that state a standing (format.md, "Which words count"); a quoted basis without one is suspect.
TABLE = {"repl": r"replicat|consistent|converg|independent",
         "single": r"single|\bone (?:study|dataset|data set|laboratory|lab|source|site|experiment|paper|trial)|"
                   r"\bonly (?:test|study|one|source|dataset)",
         "cont": r"contest|disput|conflict|disagree|contradict",
         "unclear": r"unclear|unsettled|poorly constrained|cannot tell|unknown|uncertain|unresolved"}
FIELDS = {
    "claim": ({"conf", "class", "holds", "src", "trail", "from"}, {"rating", "limit", "search", "contrary"}),
    "background": ({"kind", "ref", "check"}, set()),
    "dns": ({"why", "instead", "from"}, {"trail"}),
    "gap": ({"blocks", "origin", "search"}, {"from", "trail", "src", "contrary"}),
}
INPUT_COLS = ("id", "note", "critique", "citations", "standing labels", "run record", "omission check")
ENTRY = re.compile(r"^- \*\*([a-z0-9][a-z0-9._-]*)\*\*\s+(.*)$")
FIELDLINE = re.compile(r"^\s{2,}(\w+):\s")
IDREF = re.compile(r"([A-Za-z0-9][A-Za-z0-9-]*):([ABCIR])-(\d+)(?:\.\.(\d+))?")


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
    w = 4 if kind in "IBR" else 3
    return [f"{a}:{kind}-{n:0{w}d}" for n in range(lo, hi + 1)]


def critic_refs(fields, default):
    """Critique items an entry names as a basis (conf, class, limit) or as a label correction (src), each with its
    input ID (the ID may be left off when there is one input)."""
    out = []
    for fld in ("conf", "class", "limit", "src", "rating", "search", "contrary"):
        for m in CRITREF.finditer(fields.get(fld, "")):
            out += [r if re.match(r"[A-Za-z0-9][A-Za-z0-9-]*:", r) else f"{default}:{r}"
                    for r in re.split(r"\s*,\s*", m.group(1))]
    return out


def entry_refs(fields, default):
    """Every inventory reference the checker is shown for an entry: its `from`, then the critique it names."""
    refs = [r for r in re.split(r",\s*", fields.get("from", "")) if r.strip()]
    return refs + [r for r in critic_refs(fields, default) if r not in refs]


def qnorm(s):
    """For matching a quotation against note text: case, emphasis marks, curly quotes and spacing ignored."""
    s = s.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    return re.sub(r"\s+", " ", re.sub(r"[*`]", "", s)).lower().strip()


def resolve_trail(t, inputs, secs_by):
    """'MB-01 §2.2', '§critic', '§answers', or the start of a callout's title ('§Integration read');
    returns [(id, title, kind)] or raises ValueError."""
    out = []        # a comma separates trail parts only before '§' or '<ID> §': headings may contain commas
    for part in [x.strip() for x in re.split(r",\s*(?=(?:[A-Za-z0-9][A-Za-z0-9-]*\s+)?§)", t)]:
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


def declared_answers(fm):
    """{input ID: [heading starts] or 'none (reason)'}: the answer sections a knowledge note declares for inputs
    whose answers detection does not find (frontmatter `answers:`)."""
    out = {}
    for item in fm.get("answers") or []:
        nid, v = (next(iter(item.items())) if isinstance(item, dict) else
                  [x.strip() for x in str(item).split(":", 1)])
        v = str(v).strip()
        out[str(nid).strip()] = v if v.lower().startswith("none") else [x.strip() for x in v.split(",") if x.strip()]
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
    infos = []
    decls = declared_answers(fm)
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
        feats[nid], inv = detect(p, nid, decls.get(nid))
        ft = feats[nid]
        if ft["omission check"].startswith("not run (no "):
            err(f"input {nid}: detection found no answers, labelled citations or critique, so the omission check "
                "cannot run. Declare the sections that hold its answers in the frontmatter (answers: - "
                f"{nid}: §Heading, §Heading), or write '{nid}: none (reason)'")
        if not ft["body addresses"]:
            err(f"input {nid}: no body addresses: detection read the whole body as something else (a title taken "
                "for a references heading?). Nothing in the body can be cited")
        elif ft["reference addresses"] > ft["body addresses"] + sum(ft["inventory"].values()):
            err(f"input {nid}: {ft['reference addresses']} reference addresses against {ft['body addresses']} body "
                "addresses: the reference list seems to have swallowed the body")
        for s in ft["unaddressed sections"]:
            if not SKIP_TITLE.search(s):
                err(f"input {nid}: section '{s}' has text but no address: a detection miss")
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
    default = next(iter(invs)) if len(invs) == 1 else "?"
    ntexts = [qnorm(t) for t in texts.values()]

    def item(g):
        nid, iid = g.split(":")
        return invs.get(nid, {}).get(iid)

    def check_basis(eid, fld, basis, value, ptext):
        """A basis names a critique item that exists, or quotes words that sit in the entry's own text."""
        if basis.startswith("critic:"):
            for ref in re.split(r",\s*", basis[7:].strip()):
                ref = ref if ":" in ref else f"{default}:{ref}"
                got = expand(ref)
                if not got:
                    err(f"{eid}: {fld} basis '{ref}': write critic: <ID>:C-nnn (the ID may be left off when there "
                        "is one input)")
                elif not all(item(g) for g in got):
                    err(f"{eid}: {fld} basis {ref} is not in the inventory")
        elif basis.startswith("note:"):
            quote = basis[7:-1]
            msg = where_is(quote, ptext)
            if msg:
                err(f"{eid}: {fld} quotes \"{quote}\", which {msg}")
            if fld == "conf" and value in TABLE and not re.search(TABLE[value], quote, re.I):
                warn(f"{eid}: conf {value} quotes \"{quote}\", which has no word the format's table counts as "
                     f"'{value}' (references/format.md, Which words count)")

    def where_is(quote, ptext):
        if qnorm(quote) in ptext:
            return None
        if any(qnorm(quote) in t for t in ntexts):
            return ("is in the note but not in this entry's from text (the checker sees only that): cite the "
                    "sentence it is in")
        return "is not in any input note"

    for e in entries:
        f, eid, req_opt = e["fields"], e["id"], FIELDS[e["type"]]
        ptext = qnorm(" ".join(x["text"] for r in entry_refs(f, default) for g in (expand(r) or []) if (x := item(g))))
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
            q = RATING.match(f["rating"].strip())
            if not q:
                err(f"{eid}: rating is the note's own words in quotes, with the critic's ruling beside it if the "
                    "critic disputes it: rating: \"Moderate\" (critic: C-050: rests on a summary)")
            else:
                if where_is(q.group(1), ptext):
                    err(f'{eid}: rating "{q.group(1)}" {where_is(q.group(1), ptext)}')
                if q.group(2):
                    check_basis(eid, "rating", f"critic: {q.group(2)}", None, ptext)
        for fld, rx in (("search", SEARCH), ("contrary", CONTRARY)):
            if fld not in f:
                continue
            mm = rx.match(f[fld].strip())
            if not mm:
                err(f"{eid}: {fld} '{f[fld]}' (values and basis: see references/format.md, Search status)")
                continue
            basis = mm.group(2)
            if fld == "contrary" and mm.group(1) == "one-sided" and not (basis or "").startswith("critic:"):
                err(f"{eid}: contrary: one-sided rests on the critic's one-sided-handling finding: (critic: C-nnn)")
            elif mm.group(1) != "not stated" and not basis:
                err(f"{eid}: {fld} {mm.group(1)} needs its basis: (note: \"words\"), (critic: C-nnn) or (run: ...); "
                    "never inferred")
            elif basis and basis.startswith("run:") and not any(ft["run record"] == "yes" for ft in feats.values()):
                err(f"{eid}: {fld} basis (run: ...) but no input has a run record")
            elif basis and not basis.startswith("run:"):
                check_basis(eid, fld, basis, None, ptext)
        for fld in ("holds", "why", "src", "origin"):          # entry IDs are navigation; a writer can't follow them
            ids_in = [x for x in re.findall(r"(?<![\w.-])([a-z][a-z0-9-]*\.\d+)(?![\w-])", f.get(fld, "")) if x in known]
            if ids_in:
                warn(f"{eid}: {fld} cites {', '.join(ids_in)}: say what the finding is instead; entry IDs are "
                     "navigation, and the writer's view does not show them")
        if e["type"] == "claim" and f.get("class", "").startswith("search") and "search" not in f:
            err(f"{eid}: class search needs its search status: search: searched, not found (basis) | not searched "
                "(basis) | not stated")
        if "limit" in f:
            mm = LIMIT.match(f["limit"])
            if not mm:
                err(f"{eid}: limit '{f['limit']}': 'access' or 'access and evidence', with the basis that says so: "
                    "(critic: C-nnn) or (note: \"words from the note\")")
            else:
                check_basis(eid, "limit", mm.group(2), mm.group(1), ptext)
        for m in CRITREF.finditer(f.get("src", "")):        # a label the critic corrected
            for ref in re.split(r"\s*,\s*", m.group(1)):
                got = expand(ref if ":" in ref else f"{default}:{ref}")
                if not got or not all(item(g) for g in got):
                    err(f"{eid}: src names critic {ref}, which is not in the inventory")
        for was in re.findall(r'was "([^"]+)"', f.get("src", "")):
            if where_is(was, ptext):
                err(f'{eid}: src says the note\'s label was "{was}", which {where_is(was, ptext)}')
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
                if basis and basis != "marker" and not basis.startswith("inputs:"):
                    check_basis(eid, fld, basis, mm.group(1), ptext)
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
        if f.get("blocks") and f["blocks"].strip() != "none":
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
    required = {nid: [i for i in inv if i[0] not in "BR"] for nid, inv in invs.items()}
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
        ky = re.search(r"(\d{4})[a-z]?$", reuse or "")
        if ky and year and ky.group(1) != year.group(0):     # information only: the year is transcribed, never looked up
            infos.append(f"source {k}: kept the refs bibliography's key {reuse}, whose year differs from the note's "
                         f"{year.group(0)} (often online against issue year); nothing to do")

    # a note no second reader checked says so, in a gap
    if any(not ft["critique"].startswith("yes") for ft in feats.values()) and not any(
            e["type"] == "gap" and SECOND_READER.search(e["statement"] + " " + e["fields"].get("origin", ""))
            for e in entries):
        err("an input has no critique (or refutations only): add a gap saying its findings were never checked by a "
            "second reader, naming the figures its answers rest on")

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
        "answers": {},
    }
    for nid, p in inputs.items():          # the questions asked and the answers already checked, for the writer
        qs, where = brief_questions(p, nid, root)
        ans = note_answers(p, decls.get(nid))
        for a in ans:
            if a["key"] is None and len(qs) <= 1:
                a["key"] = next(iter(qs), "D1")
        index["answers"][nid] = {"questions": qs, "questions_from": where,
                                 "critique": feats[nid]["critique"], "answers": ans}
    out = path.with_suffix(".index.json")
    out.write_text(json.dumps(index, indent=1, ensure_ascii=False), encoding="utf-8")
    counts = Counter(e["type"] for e in entries)
    print(f"{path.name}: {len(concepts)} concepts ({len([g for g in groups])} groups), "
          f"{counts['claim']} claims, {counts['background']} background, {counts['dns']} do-not-say, "
          f"{counts['gap']} gaps, {len(bib)} sources")
    for nid in invs:
        print(f"  omission {nid}: {feats[nid]['omission check'].split(' (')[0]}, "
              f"{len(required[nid]) - len(omitted[nid])}/{len(required[nid])} accounted for")
    for nid, ft in feats.items():
        print(f"  coverage {nid}: {sum(ft['inventory'].values())} required, {ft['body addresses']} body, "
              f"{ft['reference addresses']} reference addresses; unaddressed sections: "
              f"{', '.join(ft['unaddressed sections']) or 'none'}")
    for i in infos:
        print("  info:", i)
    for w in warns:
        print("  warn:", w)
    for e in errs:
        print("  ERROR:", e)
    print(f"  index -> {out.name}; {len(errs)} errors, {len(warns)} warnings")
    return 1 if errs else 0


def load_index(path):
    """The lint index of a knowledge note, and every inventory item of its inputs by 'ID:X-nnn'."""
    path = Path(path)
    idx = path.with_suffix(".index.json")
    if not idx.exists():
        lint(path)
    index = json.loads(idx.read_text(encoding="utf-8"))
    root = vault_root(path)
    decls = declared_answers(frontmatter(path.read_text(encoding="utf-8")))
    items = {}
    for nid, ft in index["inputs"].items():
        for x in detect(root / ft["path"], nid, decls.get(nid))[1]:
            items[f"{nid}:{x['id']}"] = x
    return index, items


# ---------------------------------------------------------------- hints for the checker (never for the builder)
# The words and tokens of an entry not found in its cited text. They show the checker where to look, not what is
# wrong. Rules as scored in v4 stage A (eval/consolidate/v4/stageA/rules.md): R1, every number, year, [n] marker,
# capitalised name and quoted phrase in the statement (and a do-not-say `why`), a name or year also accepted when it
# belongs to a source in `src`; and R2-setting, the setting-type words of `holds`. Neither met the thresholds for a
# lint gate, so they are hints, shown only in checker packets (`packets --hints`).
HINT_CAPS_COMMON = set("I DNA RNA rRNA mRNA tRNA PCR qPCR OTU OTUs ASV ASVs CO2 CH4 N2O NH3 GHG GHGs".split())
HINT_SETTING = set("""soil sediment marine ocean seawater sea freshwater lake river stream estuarine estuary coastal
wetland peat permafrost desert steppe grassland forest cropland agricultural arable paddy pasture rhizosphere root leaf
plant tree crop cereal legume maize wheat rice soybean gut stool faecal fecal human mouse murine animal host oral skin
vaginal wastewater sludge bioreactor reactor engineered compost arctic antarctic tropical temperate boreal alpine global
continental regional local site single-site plot field greenhouse laboratory lab mesocosm microcosm culture cultured
isolate in vitro vivo mock simulated simulation synthetic model modelled bacteria bacterial archaea archaeal fungi fungal
prokaryote prokaryotic eukaryote eukaryotic diatom protist virus phage genome metagenome metagenomic mag amplicon shotgun
transcriptome metatranscriptome proteome 16s its illumina miseq nanopore pacbio time-series longitudinal season seasonal
year decade experiment experimental survey review meta-analysis corpus dataset sample""".split())
_NUMWORDS = ("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen "
             "seventeen eighteen nineteen twenty").split()
_HDASH = re.compile(r"[‐-―−]")
_HWORD = re.compile(r"[^\W_]+(?:[.\-'][^\W_]+)*")
_HNUM = re.compile(r"(?<![A-Za-z0-9.])\d+(?:\.\d+)?(?![A-Za-z0-9])")
_HBRACKET = re.compile(r"\[(\s*\d+(?:\s*[-,]\s*\d+)*\s*)\]")
_HCAP = re.compile(r"(?<![\w'\-])[A-Z][\wÀ-ɏ'\-]*")
_HQUOTE = re.compile(r'"([^"]{3,}?)"')


def _hnorm(s):
    s = s.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    s = re.sub(r"[*`]", "", _HDASH.sub("-", s))
    s = re.sub(r"(?<=\d),(?=\d{3}(?!\d))", "", s)
    return re.sub(r"'s\b", "", s)


def _hstem(w):
    for suf in ("ing", "ed", "es", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            return w[:-len(suf)]
    return w


def _hcanon(x):
    try:
        return format(float(x), ".10g")
    except ValueError:
        return x


def _hmarkers(text):
    out = set()
    for m in _HBRACKET.finditer(text):
        for part in re.split(r"\s*,\s*", m.group(1).strip()):
            a, _, b = part.partition("-")
            a, b = a.strip(), (b.strip() or a.strip())
            if a.isdigit() and b.isdigit() and int(b) - int(a) < 200:
                out.update(str(n) for n in range(int(a), int(b) + 1))
    return out


def hints(e, cited_texts, bib):
    """The words and tokens of an entry (statement, a do-not-say `why`, the setting words of `holds`) that are not in
    its cited text, for the checker. A list of short strings; empty when everything is found."""
    n = _hnorm("\n".join(cited_texts))
    low = re.sub(r"\s+", " ", n.lower())
    words = set()
    for w in _HWORD.findall(low):
        words |= {w, _hstem(w)} | ({_hstem(p) for p in w.split("-") if p} if "-" in w else set())
    nums = {_hcanon(x) for x in _HNUM.findall(n)}
    marks = _hmarkers(n)

    def has_word(w):
        w = w.strip(".'-")
        return (not w or w in words or _hstem(w) in words or
                ("-" in w and all(_hstem(p) in words for p in w.split("-") if p)))

    def has_num(x):
        c = _hcanon(x)
        return c in nums or (c.isdigit() and int(c) <= 20 and bool(re.search(rf"\b{_NUMWORDS[int(c)]}\b", low)))

    f = e["fields"]
    names, years = set(), set()
    for k, src in bib.items():
        if re.search(rf"(?<![\w]){re.escape(k)}(?![\w])", f.get("src", "")):
            for a in re.split(r"\s+and\s+", src.get("author", "")):
                s = fold(surname(a)).lower().strip("{} ")
                names |= {re.sub(r"[^a-z]", "", s)} | {re.sub(r"[^a-z]", "", w) for w in re.split(r"[\s\-]+", s)}
            if src.get("year"):
                years.add(_hcanon(re.sub(r"\D", "", src["year"])[:4]))
    names.discard("")
    out = []
    for t in [e["statement"]] + ([f.get("why", "")] if e["type"] == "dns" else []):
        tn = _hnorm(t)
        for x in sorted(_hmarkers(tn), key=int):
            if x not in marks:
                out.append(f"[{x}]")
        for x in _HNUM.findall(_HBRACKET.sub(" ", tn)):
            yr = x.isdigit() and 1800 <= int(x) <= 2099
            if not has_num(x) and not (yr and _hcanon(x) in years):
                out.append(x)
        for m in _HCAP.finditer(tn):
            w = m.group(0).rstrip("'-")
            pre = tn[:m.start()].rstrip(" \"'([")
            if len(w) < 2 or w in HINT_CAPS_COMMON or w.rstrip("s") in HINT_CAPS_COMMON:
                continue
            if pre == "" or re.search(r"[.!?][\"')\]]*$", pre):
                continue
            key = re.sub(r"[^a-z]", "", fold(w.lower()))
            parts = [re.sub(r"[^a-z]", "", fold(p)) for p in w.lower().split("-")]
            if not has_word(w.lower()) and key not in names and not (len(parts) > 1 and all(p in names for p in parts if p)):
                out.append(w)
        for m in _HQUOTE.finditer(tn):
            parts = [x.strip(" .,;:") for x in re.split(r"\.\.\.|…", re.sub(r"\s+", " ", m.group(1).lower()))]
            if not all(x in low for x in parts if x):
                out.append(f'"{m.group(1)}"')
    holds = f.get("holds", "") if e["type"] == "claim" else ""
    if holds:
        hn = _hnorm(holds)
        caps = {m.group(0).lower().rstrip("'-") for m in _HCAP.finditer(hn) if len(m.group(0)) >= 2}
        for w in _HWORD.findall(hn.lower()):
            w = w.strip(".'-")
            numeric = bool(re.fullmatch(r"\d+(?:\.\d+)?", w))
            setting = w in caps or numeric or bool(re.search(r"\d", w)) or "-" in w or w in HINT_SETTING or \
                _hstem(w) in {_hstem(x) for x in HINT_SETTING}
            if w and setting and not (has_num(w) if numeric else has_word(w)):
                out.append(f"holds: {w}")
    return list(dict.fromkeys(out))


HINT_LINE = "Not found in the cited text (where to look, not what is wrong)"

# The omission hint (v4 B1b): hedge, negation, contrast and scope words of the cited text that the entry does not
# carry. A word counts as carried only with the next content word after it, so "by this corpus" is listed even
# when the entry uses "by" elsewhere. Claims only. Fixed list, not tuned on results.
OMIT_WORDS = set("""may might could suggest likely unlikely possibly perhaps probably appear seem apparently tentative
putative preliminary uncertain unclear predict
not no never none neither nor without cannot lack fail
but however although though whereas yet except unless despite rather contrary argue dispute contradict
only nearest closest by one single some few several most mostly often sometimes partly partial within among per under
when if""".split())
_OMIT_STEMS = {_hstem(w) for w in OMIT_WORDS}
_OMIT_STOP = set("""the a an this that these those its their it of to as at in on for and or is are was were be been
being has have had with from than""".split())
_OMIT_SKIP = {"from", "src", "trail", "conf", "class", "search", "contrary"}   # controlled values, not the entry's words
OMIT_LINE = "In the cited text, not in the entry (where to look, not what is wrong)"


def _is_omit(w):
    s = _hstem(w)
    return w in OMIT_WORDS or s in _OMIT_STEMS or s + "e" in OMIT_WORDS or (w.endswith("n't") and w != "n't")


def omission_hints(e, cited_texts, cap=8):
    """Hedge, negation, contrast and scope words in an entry's cited text that the entry leaves out, each with up to
    four following words, for the checker. Claims only; a list of short strings, empty when none."""
    if e["type"] != "claim":
        return []
    f = e["fields"]
    own = [e["statement"]] + [v for k, v in f.items() if k not in _OMIT_SKIP]
    toks = [[_hstem(w.strip(".'-")) for w in _HWORD.findall(_hnorm(t).lower())] for t in own]

    def carried(w, nxt):
        # the word, followed within four words by the next content word after it, in the entry's own wording
        w, nxt = _hstem(w), (_hstem(nxt) if nxt else None)
        for ts in toks:
            for j, t in enumerate(ts):
                if t == w and (nxt is None or nxt in ts[j + 1:j + 5]):
                    return True
        return False

    out = []
    for t in cited_texts:
        for clause in re.split(r"[.;:!?()\[\],\"]+|\s[-–—]\s", _hnorm(t)):
            ws = [w.strip(".'-") for w in _HWORD.findall(clause.lower())]
            ws = [w for w in ws if w]
            start = end = -1                     # the current window; overlapping windows merge into one phrase
            for i, w in enumerate(ws):
                if not _is_omit(w):
                    continue
                nxt = next((x for x in ws[i + 1:] if x not in _OMIT_STOP), None)
                if carried(w, nxt):
                    continue
                if i < end:
                    end = i + 5
                    out[-1] = " ".join(ws[start:end])
                else:
                    start, end = i, i + 5
                    out.append(" ".join(ws[start:end]))
    return list(dict.fromkeys(out))[:cap]


def entry_block(e, items, default, trail=False, bib=None):
    """One entry as the checker sees it: statement, fields, and the note text of its `from` and named critique.
    With `bib`, the hints line (checker packets only)."""
    fl = e["fields"]
    out = [f"{e['statement']}\n\n", "".join(f"- {k}: {v}\n" for k, v in fl.items() if k != "from")]
    if trail and e.get("trail_links"):
        out.append(f"- trail links: {', '.join(e['trail_links'])}\n")
    texts = []
    out.append("\nFrom the note:\n\n")
    for ref in entry_refs(fl, default):
        for g in expand(ref) or []:
            x = items.get(g)
            out.append(f"> {g} [{x['where']}] {x['text']}\n>\n" if x else f"> {g}: not in inventory\n>\n")
            if x:
                texts.append(x["text"])
    if bib is not None:
        h = hints(e, texts, bib)
        if h:
            out.append(f"\n{HINT_LINE}: {'; '.join(h)}\n")
        o = omission_hints(e, texts)
        if o:
            out.append(f"\n{OMIT_LINE}: {'; '.join(o)}\n")
    return "".join(out)


def packets(path, outdir, per=60, only=None, with_hints=False):
    """For the faithfulness check: each entry beside the exact note text it says it came from."""
    index, items = load_index(path)
    default = next(iter(index["inputs"])) if len(index["inputs"]) == 1 else "?"
    ents = [e for e in index["entries"] if e["type"] in ("claim", "dns") and (not only or e["id"] in only)]
    if only and len(ents) != len(only):
        print("not entries:", ", ".join(sorted(set(only) - {e["id"] for e in ents})))
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    files = []
    for k in range(0, len(ents), per):
        f = outdir / f"packet-{k // per + 1:02d}.md"
        with f.open("w", encoding="utf-8") as w:
            for e in ents[k:k + per]:
                w.write(f"## {e['id']} ({'do not say' if e['type'] == 'dns' else 'claim'})\n\n")
                w.write(entry_block(e, items, default, bib=index["sources"] if with_hints else None) + "\n")
        files.append(f)
    print(f"{len(ents)} entries in {len(files)} packets -> {outdir}")


def spotcheck(path, out, n=20, seed=None):
    """A random sample of the entries the checker judges, for a person to judge blind to the checker's verdicts."""
    import random
    index, items = load_index(path)
    default = next(iter(index["inputs"])) if len(index["inputs"]) == 1 else "?"
    ents = [e for e in index["entries"] if e["type"] in ("claim", "dns")]
    if seed is None:
        seed = random.SystemRandom().randrange(10 ** 8)
    pick = sorted(random.Random(seed).sample(range(len(ents)), min(n, len(ents))))
    kinds = re.findall(r"^- `(\w+)`: (.+?)(?=\n- `|\n\nBe strict)", (Path(__file__).parents[1] / "references" /
                                                                       "checker.md").read_text(), re.S | re.M)
    with Path(out).open("w", encoding="utf-8") as w:
        w.write(f"# Spot-check: {Path(path).stem}\n\n"
                f"- Knowledge note: `{index['note']}`\n- Drawn: {len(pick)} of the {len(ents)} claims and do-not-say "
                f"entries, `random.Random({seed}).sample` over them in file order (`kn.py spotcheck --seed {seed}`)\n"
                f"- Entries: {', '.join(ents[k]['id'] for k in pick)}\n\n"
                "Judge each entry only against the note text quoted under it, as the checker does: does the entry "
                "say what that text says? Not whether the research is right. The trail is there if you want the "
                "context; the checker never sees it. Mark `ok`, or one or more faults:\n\n")
        w.write("".join(f"- `{k}`: {' '.join(v.split())}\n" for k, v in kinds) + "\n")
        for i, k in enumerate(pick, 1):
            e = ents[k]
            w.write(f"## {i}. {e['id']} ({'do not say' if e['type'] == 'dns' else 'claim'})\n\n")
            w.write(entry_block(e, items, default, trail=True))
            w.write("\n**Verdict:** \n\n**Why:** \n\n")
    print(f"seed {seed}: {', '.join(ents[k]['id'] for k in pick)} -> {out}")


CLASS_WORDS = {"meas": "measured", "deriv": "derived", "model": "modelled", "assert": "asserted",
               "reading": "the reviewer's reading", "search": "a search result"}
CONF_WORDS = {"repl": "replicated", "single": "a single source", "cont": "contested", "unclear": "unclear",
              "mixed": "the sources differ"}
SEARCH_WORDS = {"searched, not found": "searched for and not found", "not searched": "not searched for",
                "not stated": "the research does not say whether this was searched for"}
CONTRARY_WORDS = {"searched": "contrary evidence was searched for",
                  "one-sided": "a second reader found the search for contrary evidence one-sided",
                  "not stated": "the research does not say whether contrary evidence was searched for"}


def _value(v):
    """A field's value without its basis: 'single (critic: C-012)' -> 'single'."""
    return re.sub(r"\s*\((?:marker|critic:|note:|inputs:|run:)[^)]*\)\s*$", "", v or "").strip()


def _authors_year(src):
    """'Smith 2020', 'Smith and Lee 2020', 'Smith et al. 2020' from a BibTeX entry."""
    au = [re.sub(r"[{}]", "", fold(surname(a))).strip() for a in re.split(r"\s+and\s+", src.get("author", "")) if a.strip()]
    who = (au[0] if len(au) == 1 else f"{au[0]} and {au[1]}" if len(au) == 2 else f"{au[0]} et al." if au else
           re.sub(r"[{}]", "", src.get("title", "Anonymous"))[:40])
    year = re.search(r"\d{4}", src.get("year", "") or src.get("date", ""))
    return f"{who} {year.group(0) if year else 'n.d.'}"


def _keys_in(text, bib):
    return [k for k in bib if re.search(rf"(?<![\w]){re.escape(k)}(?![\w])", text or "")]


def _reference(src):
    """One reference-list line from a BibTeX entry, with only the fields it has."""
    clean = lambda s: re.sub(r"\s+", " ", re.sub(r"[{}]", "", fold(s or ""))).strip()
    year = re.search(r"\d{4}", src.get("year", "") or src.get("date", "") or "")
    authors = clean(src.get("author", "")).replace(" and ", "; ") or "Anonymous"
    parts = [f"{authors} ({year.group(0) if year else 'n.d.'})."]
    if src.get("title"):
        parts.append(clean(src["title"]).rstrip(".") + ".")
    venue = clean(src.get("journal") or src.get("booktitle") or src.get("publisher") or src.get("howpublished") or "")
    if venue:
        vol = clean(src.get("volume", "")) + (f"({clean(src['number'])})" if src.get("number") else "")
        parts.append(venue + (f" {vol}" if vol else "") + (f": {clean(src['pages'])}" if src.get("pages") else "") + ".")
    if src.get("doi"):
        parts.append(f"https://doi.org/{clean(src['doi'])}")
    elif src.get("url"):
        parts.append(clean(src["url"]))
    return " ".join(parts)


def view(path, out):
    """The writer's view, from the index. Everything that carries epistemic weight is content the writer needs;
    only navigation is stripped. For each claim: the statement, who found it (author and year), the setting it
    holds for, the kind of evidence in words, its standing with the note's own rating (and a second reader's
    ruling beside it), and for an absence whether it was searched for. The answers to the questions the research
    asked come first (a second reader's correction where there is one), then the concepts in dependency order,
    then what not to say (full sentences), the gaps with their search status, and a reference list. No trails,
    sentence addresses or citation keys; the knowledge note stays the audit version."""
    path = Path(path)
    idx = path.with_suffix(".index.json")
    if (not idx.exists() or idx.stat().st_mtime < path.stat().st_mtime
            or "answers" not in json.loads(idx.read_text(encoding="utf-8"))):
        lint(path)
    index = json.loads(idx.read_text(encoding="utf-8"))
    fm = frontmatter(path.read_text(encoding="utf-8"))
    ents, bib = index["entries"], index.get("sources", {})
    by_id = {e["id"]: e for e in ents}
    names = {c["id"]: c["name"] for c in index["concepts"]}
    cited = []                                       # sources the view cites, for the reference list
    concept_of = {e["id"]: names.get(e["concept"], "") for e in ents if e.get("concept")}

    def deid(text):
        """An entry ID in builder text is navigation: 'from symbiotic-fixation.5' -> 'from the finding on ...'."""
        return re.sub(r"(?<![\w.-])([a-z][a-z0-9-]*\.(?:\d+|bg\d+))(?![\w-])",
                      lambda m: (f"the finding on {concept_of[m.group(1)]}" if concept_of.get(m.group(1)) else
                                 "a do-not-say entry" if m.group(1).startswith("dns.") else
                                 "a gap" if m.group(1).startswith("gap.") else m.group(1)), text or "")

    def who(f):
        src = f.get("src", "") or f.get("ref", "")
        if src.startswith("none"):
            m = re.match(r"none \((.+)\)$", src.strip())
            return deid(m.group(1)) if m else ""
        keys = _keys_in(src, bib)
        cited.extend(keys)
        return "; ".join(_authors_year(bib[k]) for k in keys)

    # "[3]" in an answer -> the source the note's reference list numbers 3 (the BibTeX note's "cited as: MB-02 [3]")
    marker = {}
    for k, src in bib.items():
        for nid, nums in re.findall(r"([A-Za-z0-9][A-Za-z0-9-]*)\s*\[([\d,\s–-]+)\]", src.get("note", "")):
            for n in re.findall(r"\d+", nums):
                marker[(nid, n)] = k

    def answer_text(nid, raw):
        def sub(m):
            keys = [marker.get((nid, n)) for n in re.findall(r"\d+", m.group(1))]
            keys = [k for k in keys if k]
            cited.extend(keys)
            return f" ({'; '.join(_authors_year(bib[k]) for k in keys)})" if keys else ""
        return plain(re.sub(r"\s*\[(\d+(?:\s*[,–-]\s*\d+)*)(?:,\s*(?:FT|AB|SEC)[^\]]*)?\]", sub, raw))

    def evidence(f):
        parts = []
        k = _value(f.get("class", ""))
        if k and k != "not stated":
            parts.append(" and ".join(CLASS_WORDS.get(x, x) for x in k.split("/")))
        c = _value(f.get("conf", ""))
        if c in CONF_WORDS:
            parts.append(CONF_WORDS[c])
        r = RATING.match(f.get("rating", "").strip()) if f.get("rating") else None
        if r:
            parts.append(f"rated \"{r.group(1)}\" by the research" +
                         (f"; a second reader disputes this: {r.group(3).strip()}" if r.group(3) else ""))
        if f.get("limit"):
            parts.append("limited by access (a source was not read in full; not the same as weak evidence)"
                         if f["limit"].startswith("access (") else "limited by access and by the evidence")
        return "; ".join(parts)

    def search_line(f):
        s = []
        if f.get("search"):
            s.append(SEARCH_WORDS.get(_value(f["search"]), _value(f["search"])).capitalize())
        if f.get("contrary"):
            s.append(CONTRARY_WORDS.get(_value(f["contrary"]), _value(f["contrary"])).capitalize())
        return ". ".join(s)

    def claim_lines(e, bullet="- "):
        f = e["fields"]
        src = who(f)
        lines = [f"{bullet}{e['statement']}" + (f" ({src})" if src else "")]
        if e["type"] == "background":
            lines.append("  Background, not from the research.")
        if f.get("holds"):
            lines.append(f"  Holds for: {deid(f['holds']).rstrip('.')}.")
        ev = evidence(f)
        if ev:
            lines.append(f"  Evidence: {ev}.")
        sl = search_line(f)
        if sl:
            lines.append(f"  {sl}.")
        return "\n".join(lines) + "\n"

    w = [f"# {fm.get('title') or path.stem}: writer's view\n\n",
         "> [!abstract] About this view\n"
         "> What the research found, for writing from. Each claim gives who found it, the setting it holds for, "
         "the kind of evidence, its standing where the research stated one, and for an absence whether it was "
         "searched for. A claim with no standing given has none stated in the research; \"limited by access\" means "
         "a source was not read in full, which is not the same as weak evidence. Sources are listed at the end. "
         f"The view is generated from the knowledge note `{path.name}`, where every claim is checked against the "
         "research.\n\n",
         "## What the research found, by question\n\n"]
    for nid, a in index.get("answers", {}).items():
        qs, ans = a["questions"], a["answers"]
        checked = a["critique"].startswith("yes")
        w.append(f"### {nid}\n\n")
        if not qs:
            w.append(f"The questions are {a['questions_from']}.\n\n")
        keys = list(qs) + [k for k in dict.fromkeys(x["key"] for x in ans) if k and k.split(" (")[0] not in qs]

        def put(x):
            how = ("as corrected by a second reader" if x["source"] == "critic" else
                   "as the research gave it; a second reader reviewed it and left it as given" if checked else
                   "as the research gave it; not checked by a second reader")
            head = x["label"] if x["label"] and not re.fullmatch(r"D\d+|Q(?:uestion)?\s*\d+", x["label"]) else ""
            w.append(f"*Answer, {how}.*" + (f" **{head}**" if head else "") + "\n\n")
            w.append(answer_text(nid, x.get("raw", x["text"])) + "\n\n")
        for q in keys:
            base = q.split(" (")[0]
            if q in qs:
                w.append(f"**{base}. {qs[q]}**\n\n")
            mine = [x for x in ans if x["key"] and x["key"].split(" (")[0] == base]
            if not mine:
                w.append("*No answer to this question in the research.*\n\n")
            for x in mine:
                put(x)
        loose = [x for x in ans if not x["key"]]
        if loose:
            w.append("**Answers and verdicts not tied to a listed question**\n\n")
            for x in loose:
                put(x)
    w.append("## Concepts\n\nIn an order where each concept comes after the ones it builds on; the order means "
             "nothing more.\n\n")
    for c in sorted(index["concepts"], key=lambda c: c["order"]):
        w.append(f"### {c['name']}\n\n")
        if c.get("needs"):
            w.append(f"Builds on: {', '.join(names.get(n, n) for n in c['needs'])}.\n\n")
        for e in ents:
            if e["concept"] == c["id"] and e["type"] in ("claim", "background"):
                w.append(claim_lines(e))
        w.append("\n")
    w.append("## Do not say\n\nWordings the research itself says are wrong or overstated, each with the reason and "
             "what to say instead.\n\n")
    for e in ents:
        if e["type"] == "dns":
            f = e["fields"]
            inst = [x for x in re.split(r",\s*", f.get("instead", "")) if x in by_id]
            w.append(f"- Do not write: {e['statement']}\n  Why: {deid(f.get('why', ''))}\n")
            for x in inst:
                w.append(claim_lines(by_id[x], bullet="  Say instead: "))
    w.append("\n## Gaps\n\nWhat the research did not establish.\n\n")
    for e in ents:
        if e["type"] == "gap":
            f = e["fields"]
            src = who(f) if f.get("src") else ""
            sl = search_line(f)
            w.append(f"- {e['statement']}" + (f" ({src})" if src else "") + (f"\n  {sl}." if sl else "") + "\n")
    keys = sorted(dict.fromkeys(cited), key=lambda k: _reference(bib[k]).lower())
    if keys:
        w.append("\n## References\n\n" + "".join(f"- {_reference(bib[k])}\n" for k in keys))
    Path(out).write_text("".join(w), encoding="utf-8")
    print(f"writer's view -> {out} ({sum(1 for e in ents if e['type'] == 'claim')} claims, {len(keys)} references)")


def cmd_citekey(argv):
    opt = {k: argv[argv.index(f"--{k}") + 1] for k in ("author", "title", "year", "doi", "refs") if f"--{k}" in argv}
    if opt.get("doi") and opt.get("refs"):
        hit = refs_keys(opt["refs"]).get(opt["doi"].lower().strip())
        if hit:
            print(hit)
            return
    print(citekey(opt.get("author", ""), opt.get("title", ""), opt.get("year", "")))


if __name__ == "__main__":
    cmds = ("detect", "lint", "packets", "spotcheck", "view", "citekey")
    if {"-h", "--help"} & set(sys.argv):
        print(__doc__)
        sys.exit(0)
    if len(sys.argv) < 3 or sys.argv[1] not in cmds:
        print(__doc__)
        sys.exit(2)
    a = sys.argv[2:]
    with_hints = "--hints" in a
    a = [x for x in a if x != "--hints"]
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    pos = [x for i, x in enumerate(a) if not x.startswith("--") and (i == 0 or not a[i - 1].startswith("--"))]
    if sys.argv[1] == "detect":
        sys.exit(cmd_detect(a) or 0)
    if sys.argv[1] == "citekey":
        sys.exit(cmd_citekey(a) or 0)
    if sys.argv[1] == "packets":
        only = opt("--only")
        only = set(re.split(r"[,\s]+", only.strip())) if only else None
        sys.exit(packets(pos[0], pos[1] if len(pos) > 1 else "packets", only=only, with_hints=with_hints) or 0)
    if sys.argv[1] == "view":
        sys.exit(view(pos[0], pos[1] if len(pos) > 1 else Path(pos[0]).with_suffix(".writer.md")) or 0)
    if sys.argv[1] == "spotcheck":
        seed = opt("--seed")
        sys.exit(spotcheck(pos[0], pos[1] if len(pos) > 1 else "spotcheck.md", int(opt("--n", 20)),
                           int(seed) if seed is not None else None) or 0)
    sys.exit(lint(a[0]))
