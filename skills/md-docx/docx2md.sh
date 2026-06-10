#!/usr/bin/env bash
# Usage: ./docx2md.sh input.docx [output.md]
# Converts a .docx to Obsidian-flavoured markdown:
#   - pandoc docx -> gfm (pipe tables, footnotes, $math$), no line wrapping
#   - embedded images extracted to <output>.media/
#   - internal [text](note.md) links rewritten to [[note]] wikilinks
#   - APA in-text citations matched against Refs.bib -> [@citekey]
# Per-document tweaks: edit the pandoc line below.

set -euo pipefail

if [[ $# -lt 1 ]]; then
    echo "Usage: $0 input.docx [output.md]" >&2
    exit 1
fi

INPUT="$1"
OUTPUT="${2:-${INPUT%.docx}.md}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
BIB="$VAULT_ROOT/PhD/Proposal/Refs/Refs.bib"
MEDIA="${OUTPUT%.md}.media"

# 1. docx -> markdown
pandoc "$INPUT" \
    --from=docx \
    --to=markdown_strict+pipe_tables+footnotes+tex_math_dollars-raw_html \
    --wrap=none \
    --markdown-headings=atx \
    --extract-media="$MEDIA" \
    -o "$OUTPUT.tmp"

# 1b. reconstruct Obsidian callouts. Pandoc renders a callout as a plain
#     blockquote and (a) escapes the bracket -> "> \[!warning\] Title body..."
#     and (b) merges the title line into the body. Undo both: unescape the
#     marker and split the title onto its own line so Obsidian re-renders the
#     banner. Mirrors convert.sh, which sends callouts out as blockquotes.
python3 - "$OUTPUT.tmp" <<'PY'
import re, sys
p = sys.argv[1]
lines = open(p, encoding="utf-8").read().split("\n")
TYPES = r"note|abstract|info|todo|tip|success|question|warning|failure|danger|bug|example|quote|important|caution|callout"
# a blockquote line whose content starts with an (escaped) [!type] ... marker
marker = re.compile(r"^>\s*\\?\[!(" + TYPES + r")\\?\]\s*(.*)$", re.I)
# inline callout markers anywhere in prose come back bracket-escaped:
#   \[!callout: Author, year\]  ->  [!callout: Author, year]
inline = re.compile(r"\\\[(!\w+[^\]]*?)\\\]")
out = []
i = 0
while i < len(lines):
    ln = inline.sub(r"[\1]", lines[i])  # unescape inline [!...] markers first
    m = marker.match(ln)
    if not m:
        # A lone '>' that separates two adjacent callouts (Pandoc merges them
        # into one blockquote) must become a real blank line so Obsidian renders
        # two callouts, not one. Detect: lone '>' whose next quote line is a title.
        if ln.strip() == ">":
            j = i
            while j < len(lines) and lines[j].strip() == ">":
                j += 1
            nxt = inline.sub(r"[\1]", lines[j]) if j < len(lines) else ""
            if marker.match(nxt):
                out.append("")   # callout boundary -> paragraph break
                i = j
                continue
        out.append(ln)
        i += 1
        continue
    ctype, rest = m.group(1), m.group(2)
    # Pandoc may glue the title and first body sentence with a double-space;
    # treat the run up to the first '  ' (or end) as the title.
    parts = re.split(r"\s{2,}", rest, maxsplit=1)
    title = parts[0].strip()
    body = parts[1].strip() if len(parts) > 1 else ""
    out.append(f"> [!{ctype}] {title}".rstrip())
    if body:
        out.append(f"> {body}")
    i += 1
    # convert.sh inserts a blank '>' between a callout title and its body to
    # protect the split; swallow it so the reconstructed callout has no empty
    # row. (A '>' that is instead a boundary to the NEXT callout is handled at
    # the top of the loop and turned into a paragraph break.)
    if i < len(lines) and lines[i].strip() == ">":
        nxt = inline.sub(r"[\1]", lines[i + 1]) if i + 1 < len(lines) else ""
        if not marker.match(nxt):
            i += 1
open(p, "w", encoding="utf-8").write("\n".join(out))
PY

# 2. internal links [text](something.md...) -> [[note]] (skip http/https/mailto/#)
python3 - "$OUTPUT.tmp" <<'PY'
import re, sys
p = sys.argv[1]
t = open(p, encoding="utf-8").read()
def repl(m):
    text, target = m.group(1), m.group(2)
    # leave web links, mailto, and intra-doc anchors (incl. Zotero #ref-/#X
    # citation links, handled later by apa2pandoc.py) untouched
    if re.match(r'^(https?:|mailto:|#)', target):
        return m.group(0)
    note = re.sub(r'\.md($|#.*)', '', target).strip()
    note = note.split('/')[-1]
    if not note:
        return m.group(0)
    return f'[[{note}]]' if note == text else f'[[{note}|{text}]]'
t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', repl, t)
open(p, "w", encoding="utf-8").write(t)
PY

# 3. APA citations -> pandoc keys (report to stderr)
if [[ -f "$BIB" ]]; then
    python3 "$SCRIPT_DIR/apa2pandoc.py" "$BIB" < "$OUTPUT.tmp" > "$OUTPUT"
    rm -f "$OUTPUT.tmp"
else
    echo "WARNING: $BIB not found; skipping citation matching" >&2
    mv "$OUTPUT.tmp" "$OUTPUT"
fi

echo "Wrote: $OUTPUT" >&2
