#!/usr/bin/env bash
# A LaTeX formula to a standalone SVG with glyphs as paths (no webfonts, so it
# passes the static check and renders the same everywhere).
#   tex2svg.sh 'd(a,b) = \min_p |p|' out.svg [colour-hex] [scale]
# Native size is 10pt type, small beside 18px body text; scale defaults to 1.8.
set -euo pipefail
TEX="$1"; OUT="$2"; COLOUR="${3:-1D2329}"; SCALE="${4:-1.8}"
W=$(mktemp -d); trap 'rm -rf "$W"' EXIT
cat > "$W/f.tex" <<EOF
\documentclass[border=1pt,varwidth]{standalone}
\usepackage{amsmath,amssymb}
\usepackage{xcolor}
\begin{document}
\color[HTML]{$COLOUR}\$\displaystyle $TEX\$
\end{document}
EOF
( cd "$W" && latex -interaction=nonstopmode -halt-on-error f.tex >/dev/null ) || { sed -n '/^!/,+3p' "$W/f.log" >&2; exit 1; }
dvisvgm --no-fonts --exact-bbox --scale="$SCALE" -o "$OUT" "$W/f.dvi" >/dev/null 2>&1
echo "$OUT"
