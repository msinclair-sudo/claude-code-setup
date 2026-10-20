#!/usr/bin/env bash
# Toolchain smoke renders, one per tier's tools, into a scratch folder.
#   smoke.sh [--keep]     (--keep leaves the folder and prints its path)
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
X="$HERE/x"; S="$HERE/smoke"
KEEP=0; [ "${1:-}" = --keep ] && KEEP=1
OUT=$(mktemp -d "${TMPDIR:-/tmp}/explain-smoke.XXXXXX")
fail=0
run() {  # name, expected file, command...
  local name="$1" want="$2"; shift 2
  local t0=$SECONDS
  if "$@" >"$OUT/$name.log" 2>&1 && [ -s "$want" ]; then
    printf '  PASS  smoke %-8s %3ds\n' "$name" $((SECONDS - t0))
  else
    printf '  FAIL  smoke %-8s (log: %s)\n' "$name" "$OUT/$name.log"; fail=1; KEEP=1
  fi
}
echo "explain: smoke renders in $OUT"
run static "$OUT/static/index.html" "$X" run python "$S/s_static.py" "$OUT/static"
grep -q 'publishable' "$OUT/static.log" || { echo "  FAIL  static_check rejected the smoke page"; fail=1; KEEP=1; }
run plotly "$OUT/plotly/page.html" "$X" run python "$S/s_plotly.py" "$OUT/plotly"
run deck   "$OUT/deck/handout.pdf" "$X" run python "$S/s_deck.py" "$OUT/deck"
for f in plotly deck; do
  grep -q 'non-file requests: none' "$OUT/$f.log" || { echo "  FAIL  $f made network requests"; fail=1; KEEP=1; }
done
run manim  "$OUT/media/videos/s_manim/480p15/Smoke.mp4" \
  "$X" run manim -ql --disable_caching --media_dir "$OUT/media" "$S/s_manim.py" Smoke
if [ "$KEEP" = 1 ]; then echo "  kept: $OUT"; else rm -rf "$OUT"; fi
exit "$fail"
