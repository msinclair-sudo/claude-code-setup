#!/usr/bin/env python3
"""Rewrite APA in-text citations to Pandoc citation keys, matched against a .bib.

Reads markdown on stdin, writes rewritten markdown on stdout, prints a match
report to stderr. Matching is by first-author surname + year (which is unique
for ~all entries in this project's Refs.bib). Ambiguous or unmatched cites are
left as-is, wrapped in an <!-- UNMATCHED: ... --> comment, and listed on stderr.

Usage:
    apa2pandoc.py REFS.bib < input.md > output.md
"""
import re
import sys
import unicodedata
from collections import defaultdict


def fold(s):
    """Lowercase and strip accents for robust surname matching."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.lower().strip()


def first_author_surname(author_field):
    """Extract first author's surname, handling 'Last, First' and 'First Last',
    compound/prefixed names (van, de, von) and brace-protected names."""
    first = author_field.split(" and ")[0].strip()
    first = first.replace("{", "").replace("}", "")
    if "," in first:
        return first.split(",")[0].strip()
    tokens = first.split()
    if not tokens:
        return first
    prefixes = {"van", "von", "de", "der", "den", "del", "la", "le", "di", "da"}
    i = len(tokens) - 1
    while i > 0 and tokens[i - 1].lower() in prefixes:
        i -= 1
    return " ".join(tokens[i:])


def load_bib(path):
    text = open(path, encoding="utf-8").read()
    entries = re.findall(r"@\w+\{([^,]+),(.*?)(?=\n@|\Z)", text, re.S)
    index = defaultdict(list)  # (folded_surname, year) -> [citekey, ...]
    for key, body in entries:
        am = re.search(r"author\s*=\s*\{(.*?)\}", body, re.S)
        ym = re.search(r"(?:date|year)\s*=\s*\{?(\d{4})", body)
        if not am or not ym:
            continue
        surname = first_author_surname(am.group(1))
        index[(fold(surname), ym.group(1))].append(key.strip())
    return index


YEAR = r"\d{4}[a-z]?"
UNIT = re.compile(
    r"(?P<names>[A-ZÀ-Þ][^,();]*?)"
    r",\s*(?P<year>" + YEAR + r")"
)
PAREN = re.compile(r"\(([^()]*?" + YEAR + r"[^()]*?)\)")
NARR = re.compile(
    r"(?P<names>[A-ZÀ-Þ][\w’'\-]*(?:\s+(?:et al\.?|&|and)\s+[A-ZÀ-Þ][\w’'\-]*)*?)"
    r"\s*\((?P<year>" + YEAR + r")\)"
)


def lead_surname(names):
    """First surname token from an APA author phrase like 'Averill et al.'
    Strips a trailing 'et al.' and any second author after &/and, then takes
    the surname (last whitespace token, keeping van/de prefixes is not needed
    here since APA in-text uses bare surnames)."""
    names = names.strip()
    # cut at the first co-author / et al. boundary. '&' has no word boundary,
    # so match it separately from the word-y 'et al.'/'and'.
    names = re.split(r"\s*&\s*|\s+(?:et\s+al\.?|and)\b", names)[0]
    names = names.strip().rstrip(",")
    return names.split()[-1] if names else ""


report = {"matched": [], "ambiguous": [], "unmatched": []}

# Zotero/Word cites survive docx->md as hyperlinks into the reference list:
#   [`Chen et al. ``(``2022`](#ref-chenFunctionalRedundancySoil2022)   <- key in anchor
#   [`Wu et al., 2019`](#X0c8123a9...)                                  <- opaque anchor
# Match the whole [visible](#anchor) span. #ref- carries the citekey verbatim;
# #X... falls back to surname+year from the (backtick-mangled) visible text.
HYPERLINK = re.compile(r"\[`?([^\]]*?)`?\]\(#(ref-[A-Za-z0-9]+|X[a-f0-9]+)\)")


def rewrite_hyperlink(m, index):
    visible, anchor = m.group(1), m.group(2)
    if anchor.startswith("ref-"):
        key = anchor[4:]  # citekey is embedded directly
        report["matched"].append(("(#ref anchor)", "", key))
        return "[@" + key + "]"
    # opaque #X anchor: strip backtick noise from visible text, parse surname+year
    clean = visible.replace("`", "").replace("(", " ").strip()
    ym = re.search(r"(\d{4}[a-z]?)", clean)
    surname = lead_surname(clean)
    if ym:
        key, err = resolve(surname, ym.group(1), index)
        if key:
            report["matched"].append((surname, ym.group(1), key))
            return "[@" + key + "]"
        report[err].append((surname, ym.group(1) if ym else "?", visible))
    return m.group(0) + " <!-- UNMATCHED: " + visible.replace("`", "") + " -->"


def resolve(surname, year, index):
    yr = year.rstrip("abcdefghijklmnop")
    fs = fold(surname)
    hits = index.get((fs, yr), [])
    if not hits:
        # APA in-text often drops a name prefix the bib keeps (e.g. visible
        # "Tatenhove-Pel" vs bib "van Tatenhove-Pel"). Match on prefix-stripped
        # surname when it's unambiguous in that year.
        cand = [v for (s, y), v in index.items()
                if y == yr and (s.endswith(" " + fs) or s.split()[-1] == fs)]
        flat = [k for ks in cand for k in ks]
        if len(flat) == 1:
            return flat[0], None
        if len(flat) > 1:
            return None, "ambiguous"
    if len(hits) == 1:
        return hits[0], None
    if len(hits) > 1:
        return None, "ambiguous"
    return None, "unmatched"


def rewrite_parenthetical(m, index):
    inner = m.group(1)
    # already-converted cites (from the hyperlink pass) live as [@key] inside
    # the parens — leave the whole group alone, unwrapping the bare ()-wrapper.
    if "[@" in inner:
        keys = re.findall(r"@[A-Za-z0-9]+", inner)
        return "[" + "; ".join(keys) + "]" if keys else m.group(0)
    out_keys = []
    flagged = []
    for unit in re.split(r";", inner):
        um = UNIT.search(unit)
        if not um:
            flagged.append(unit.strip())
            continue
        surname = lead_surname(um.group("names"))
        key, err = resolve(surname, um.group("year"), index)
        if key:
            out_keys.append("@" + key)
            report["matched"].append((surname, um.group("year"), key))
        else:
            report[err].append((surname, um.group("year"), unit.strip()))
            flagged.append(unit.strip())
    if flagged and not out_keys:
        return "(" + inner + ") <!-- UNMATCHED: " + " | ".join(flagged) + " -->"
    rebuilt = "[" + "; ".join(out_keys) + "]"
    if flagged:
        rebuilt += " <!-- UNMATCHED: " + " | ".join(flagged) + " -->"
    return rebuilt


def rewrite_narrative(m, index):
    surname = lead_surname(m.group("names"))
    key, err = resolve(surname, m.group("year"), index)
    if key:
        report["matched"].append((surname, m.group("year"), key))
        return m.group("names") + " [@" + key + "]"
    report[err].append((surname, m.group("year"), m.group(0)))
    return m.group(0) + " <!-- UNMATCHED: " + surname + " " + m.group("year") + " -->"


def strip_reference_list(text):
    """Remove the docx's rendered reference list, since the Pandoc render plugin
    regenerates it from [@keys]. Keep the heading, and keep any reference entry
    whose in-text citation is still UNMATCHED (so it can be resolved by hand)."""
    m = re.search(r"^#+\s*References?\b.*$", text, re.M | re.I)
    if not m:
        return text  # no reference list to strip
    head, reflist = text[: m.end()], text[m.end():]

    # surnames+years still unresolved in the BODY (carry an UNMATCHED flag there)
    body = text[: m.start()]
    keep_surnames = set()
    for um in re.finditer(r"<!-- UNMATCHED: ([^>]*?) -->", body):
        frag = um.group(1)
        sm = re.search(r"([A-ZÀ-Þ][A-Za-zÀ-ÿ’'-]+)\s+(?:et al|&|and|,)", frag)
        if sm:
            keep_surnames.add(fold(sm.group(1)))

    kept = []
    # reference entries are separated by blank lines; each starts "Surname, I."
    for entry in re.split(r"\n\s*\n", reflist):
        s = entry.strip()
        if not s:
            continue
        sm = re.match(r"([A-ZÀ-Þ][A-Za-zÀ-ÿ’'-]+),", s)
        if sm and fold(sm.group(1)) in keep_surnames:
            # drop the false UNMATCHED noise on the kept entry's year/DOI
            s = re.sub(r"\s*<!-- UNMATCHED: [^>]*? -->", "", s)
            kept.append(s)

    if kept:
        return head + "\n\n" + "\n\n".join(kept) + "\n"
    return head.rstrip() + "\n"


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: apa2pandoc.py REFS.bib < in.md > out.md")
    index = load_bib(sys.argv[1])
    text = sys.stdin.read()
    # 1. Zotero hyperlink cites first (they carry exact keys / clean visible text)
    text = HYPERLINK.sub(lambda m: rewrite_hyperlink(m, index), text)
    # 2. plain-text APA cites: narrative before parenthetical
    text = NARR.sub(lambda m: rewrite_narrative(m, index), text)
    text = PAREN.sub(lambda m: rewrite_parenthetical(m, index), text)
    # 3. drop the rendered reference list (regenerated from keys by the plugin),
    #    but KEEP any entry whose in-text cite stayed UNMATCHED so it's fixable.
    text = strip_reference_list(text)
    sys.stdout.write(text)

    def emit(title, rows):
        print(f"\n{title}: {len(rows)}", file=sys.stderr)
        for r in rows:
            print("  " + " | ".join(str(x) for x in r), file=sys.stderr)

    print("=== citation match report ===", file=sys.stderr)
    print(f"matched: {len(report['matched'])}", file=sys.stderr)
    if report["ambiguous"]:
        emit("AMBIGUOUS (left as-is, pick a key manually)", report["ambiguous"])
    if report["unmatched"]:
        emit("UNMATCHED (no surname+year in bib)", report["unmatched"])


if __name__ == "__main__":
    main()
