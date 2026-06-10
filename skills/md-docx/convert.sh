#!/usr/bin/env bash
# Usage: ./convert.sh input.md [output.docx]
# Converts a markdown file to .docx using the styles defined in reference.docx.
# Per-document overrides (reference-doc, bibliography, csl, toc...) go in the
# markdown file's YAML frontmatter.
#
# Callouts: Obsidian callouts (`> [!type] Title` + body lines) are normalised
# before pandoc so they survive a docx round-trip (see docx2md.sh, which
# reconstructs them). A blank `>` line is inserted between the title and the
# body so pandoc keeps the title on its own blockquote paragraph; the `[!type]`
# marker is left as literal text and is what docx2md.sh reads back.

set -euo pipefail

if [[ $# -lt 1 ]]; then
    echo "Usage: $0 input.md [output.docx]" >&2
    exit 1
fi

INPUT="$1"
OUTPUT="${2:-${INPUT%.md}.docx}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULTS="$SCRIPT_DIR/defaults.yaml"

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

pandoc -d "$DEFAULTS" "$PREPPED" -o "$OUTPUT"
echo "Wrote: $OUTPUT"
