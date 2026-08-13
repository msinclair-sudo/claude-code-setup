#!/usr/bin/env bash
# Usage: ./convert.sh input.md [output.docx] [--csl /path/to/style.csl]
# Converts a markdown file to .docx using the styles defined in reference.docx.
# Citations render with the bundled APA 7th-edition CSL (apa.csl in this skill)
# unless you override it with --csl /path/to/style.csl (or the CSL env var).
# Per-document overrides (reference-doc, bibliography, toc...) go in the
# markdown file's YAML frontmatter.
#
# Callouts: Obsidian callouts (`> [!type] Title` + body lines) are normalised
# before pandoc so they survive a docx round-trip (see docx2md.sh, which
# reconstructs them). A blank `>` line is inserted between the title and the
# body so pandoc keeps the title on its own blockquote paragraph; the `[!type]`
# marker is left as literal text and is what docx2md.sh reads back.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULTS="$SCRIPT_DIR/defaults.yaml"
# Citation style: bundled APA 7th edition, overridable by --csl / CSL env var.
CSL="${CSL:-$SCRIPT_DIR/apa.csl}"
POSITIONAL=()
while [[ $# -gt 0 ]]; do
    case "$1" in
        --csl)
            CSL="${2:?--csl requires a path to a .csl file}"
            shift 2
            ;;
        --csl=*)
            CSL="${1#--csl=}"
            shift
            ;;
        *)
            POSITIONAL+=("$1")
            shift
            ;;
    esac
done
set -- "${POSITIONAL[@]}"

if [[ $# -lt 1 ]]; then
    echo "Usage: $0 input.md [output.docx] [--csl /path/to/style.csl]" >&2
    exit 1
fi

INPUT="$1"
OUTPUT="${2:-${INPUT%.md}.docx}"

if [[ ! -f "$CSL" ]]; then
    echo "ERROR: CSL file not found: $CSL" >&2
    echo "       Pass --csl /path/to/style.csl or restore apa.csl in the skill." >&2
    exit 1
fi

# Preprocess callouts into a round-trip-safe blockquote shape.
PREPPED="$(mktemp).md"
trap 'rm -f "$PREPPED"' EXIT
python3 - "$INPUT" "$PREPPED" <<'PY'
import re, sys
src, dst = sys.argv[1], sys.argv[2]
TYPES = (r"note|abstract|info|todo|tip|success|question|warning|failure|"
         r"danger|bug|example|quote|important|caution|callout")
title_re = re.compile(r"^>\s*\[!(" + TYPES + r")\][+-]?\s*(.*)$", re.I)
lines = open(src, encoding="utf-8").read().split("\n")
out = []
for i, ln in enumerate(lines):
    m = title_re.match(ln)
    out.append(ln)
    if m:
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        # if a body line follows directly, insert a blank quote line so pandoc
        # keeps the callout title as its own paragraph through the conversion
        if nxt.startswith(">") and nxt.strip() not in (">", ">"):
            out.append(">")
open(dst, "w", encoding="utf-8").write("\n".join(out))
PY

# Page geometry for the section breaks emitted by sectionbreak.lua. A
# paragraph-level <w:sectPr> sets the geometry of the section it ends, so we copy
# pgSz/pgMar from the active reference.docx to keep every section identical.
geom() {  # $1 = element tag (pgSz|pgMar)
    python3 - "$SCRIPT_DIR/reference.docx" "$1" <<'PY' 2>/dev/null || true
import re, sys, zipfile
docx, tag = sys.argv[1], sys.argv[2]
with zipfile.ZipFile(docx) as z:
    xml = z.read("word/document.xml").decode("utf-8", "replace")
m = re.search(r"<w:%s\b[^>]*/>" % tag, xml)
print(m.group(0) if m else "", end="")
PY
}
export MDDOCX_PGSZ="$(geom pgSz)"
export MDDOCX_PGMAR="$(geom pgMar)"

pandoc -d "$DEFAULTS" \
    --reference-doc "$SCRIPT_DIR/reference.docx" \
    --csl "$CSL" \
    --lua-filter "$SCRIPT_DIR/sectionbreak.lua" \
    --resource-path "$SCRIPT_DIR:.:$(dirname "$INPUT")" \
    "$PREPPED" -o "$OUTPUT"
echo "Wrote: $OUTPUT"
