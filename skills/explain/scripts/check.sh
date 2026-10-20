#!/usr/bin/env bash
# Is this machine ready to make explanations? Prints PASS/FAIL per item and
# exits non-zero if anything a tier needs is missing.
#
#   check.sh            every tier
#   check.sh --tier N   only what tiers 0..N need
#   check.sh --smoke    run the smoke renders too (scripts/smoke.sh)
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=/dev/null
source "$HERE/../config.sh"
TIER=4; SMOKE=0
while [ $# -gt 0 ]; do
  case "$1" in
    --tier) TIER="$2"; shift 2 ;;
    --smoke) SMOKE=1; shift ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done

fail=0
ok()  { printf '  PASS  %s\n' "$1"; }
bad() { printf '  FAIL  %s\n' "$1"; fail=1; }
need() { [ "$TIER" -ge "$1" ]; }
key() { [ -n "${!1:-}" ] && ok "$1 set" || bad "$1 missing from ~/.env (scripts/install-env.sh prints it)"; }
py() { "$REPORT_PYTHON" -c "import $1" >/dev/null 2>&1 && ok "python: $1" || bad "python: $1 not importable from REPORT_PYTHON"; }
bin() { local b="$REPORT_BIN/$1"; [ -x "$b" ] || b=$(command -v "$1" 2>/dev/null || true)
        [ -n "$b" ] && [ -x "$b" ] && ok "bin: $1 ($b)" || bad "bin: $1 not found in REPORT_BIN or PATH"; }

echo "explain: environment check (tiers 0..$TIER)"
for k in REPORT_PYTHON REPORT_BIN REPORT_HOME; do key "$k"; done
[ -x "${REPORT_PYTHON:-/nonexistent}" ] || { bad "REPORT_PYTHON not executable"; echo "explain: not ready"; exit 1; }

# tier 0-1: page, figures, maths
bin pandoc
for m in yaml numpy matplotlib graphviz playwright; do py "$m"; done
bin dot
bin latex; bin dvisvgm
key REPORT_CHROME
[ -x "${REPORT_CHROME:-/nonexistent}" ] && ok "chrome executable" || bad "REPORT_CHROME not executable"
[ -f "${REPORT_HOME:-}/vendor/axe-core-4.14.0/axe.min.js" ] && ok "vendor: axe-core" || bad "vendor: axe-core missing (install-env.sh)"

if need 2; then  # slides, narration
  [ -f "$REPORT_HOME/vendor/reveal.js-6.0.2/dist/reveal.js" ] && ok "vendor: reveal.js" || bad "vendor: reveal.js missing (install-env.sh)"
  for k in REPORT_TTS_MODEL REPORT_TTS_VOICES REPORT_VOICE; do key "$k"; done
  [ -f "${REPORT_TTS_MODEL:-/nonexistent}" ] && ok "kokoro model file" || bad "kokoro model file missing"
  [ -f "${REPORT_TTS_VOICES:-/nonexistent}" ] && ok "kokoro voices file" || bad "kokoro voices file missing"
  py kokoro_onnx; py soundfile
  bin ffmpeg
  f="$REPORT_BIN/ffmpeg"; [ -x "$f" ] || f=ffmpeg
  enc=$("$f" -hide_banner -encoders 2>/dev/null || true)   # captured: grep -q on a pipe trips pipefail
  if grep -q libx264 <<<"$enc" && grep -qE ' aac ' <<<"$enc"; then
    ok "ffmpeg encoders: libx264, aac"; else bad "ffmpeg lacks libx264 or aac (need the gpl build)"; fi
fi
if need 3; then py plotly; py kaleido; fi
if need 4; then py manim; py manim_voiceover; bin manim; fi

if [ "$SMOKE" = 1 ]; then
  if [ "$fail" = 0 ]; then bash "$HERE/smoke.sh" || fail=1; else echo "  (smoke skipped: fix the FAILs first)"; fi
fi
[ "$fail" = 0 ] && echo "explain: ready" || echo "explain: not ready"
exit "$fail"
