#!/usr/bin/env bash
# Build or update everything the explain skill runs on, without sudo:
#   1. the `report` conda env (env/report.yml, conda-forge)
#   2. its pip layer (env/requirements.txt), never letting pip replace conda's manim
#   3. Kokoro model files into $REPORT_HOME/models
#   4. reveal.js and axe-core into $REPORT_HOME/vendor (offline copies; no CDN at render time)
# then write the settings file ~/.config/explain/config.env (paths and voice;
# nothing secret, so not ~/.env). Safe to re-run.
#
#   install-env.sh [--base ~/miniforge3] [--home ~/.local/share/explain] [--name report]
#
# Needs network. Checksums of everything downloaded are pinned in env/assets.sha256;
# a file whose sum differs is deleted and the script stops.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL="$(dirname "$HERE")"
BASE="$HOME/miniforge3"
RHOME="$HOME/.local/share/explain"
NAME="report"
while [ $# -gt 0 ]; do
  case "$1" in
    --base) BASE="$2"; shift 2 ;;
    --home) RHOME="$2"; shift 2 ;;
    --name) NAME="$2"; shift 2 ;;
    -h|--help) sed -n '2,14p' "$0"; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done

KOKORO_URL="https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0"
KOKORO_FILES="kokoro-v1.0.onnx voices-v1.0.bin"
VENDOR_PKGS="reveal.js@6.0.2 axe-core@4.14.0"
SUMS="$SKILL/env/assets.sha256"

say() { printf '\n== %s\n' "$1"; }
CONDA="$BASE/bin/mamba"; [ -x "$CONDA" ] || CONDA="$BASE/bin/conda"
[ -x "$CONDA" ] || { echo "no conda or mamba under $BASE" >&2; exit 1; }
ENV="$BASE/envs/$NAME"
PY="$ENV/bin/python"

check_sum() {  # file, key: verify against the pinned sum, or report it if none is pinned
  local f="$1" key="$2" got want
  got=$(sha256sum "$f" | cut -d' ' -f1)
  want=$(awk -v k="$key" '$2==k {print $1}' "$SUMS" 2>/dev/null || true)
  if [ -z "$want" ]; then
    echo "  no pinned sum for $key; add this line to env/assets.sha256:"
    echo "  $got  $key"
  elif [ "$got" != "$want" ]; then
    rm -f "$f"; echo "  CHECKSUM MISMATCH for $key (got $got); deleted" >&2; exit 1
  else
    echo "  sha256 ok  $key"
  fi
}

say "1. conda env '$NAME' at $ENV"
if [ -d "$ENV" ]; then
  "$CONDA" env update -n "$NAME" -f "$SKILL/env/report.yml" --prune -y
else
  "$CONDA" env create -n "$NAME" -f "$SKILL/env/report.yml" -y
fi

say "2. pip layer"
# Everything but manim-voiceover installs normally. manim-voiceover goes in
# --no-deps, then its own requirements minus manim, so conda's manim stays.
W=$(mktemp -d); trap 'rm -rf "$W"' EXIT
grep -vE '^\s*(#|$)' "$SKILL/env/requirements.txt" | sed 's/\s*#.*//' > "$W/all"
grep -v '^manim-voiceover' "$W/all" > "$W/rest"
"$PY" -m pip install -q -r "$W/rest"
"$PY" -m pip install -q --no-deps "$(grep '^manim-voiceover' "$W/all")"
"$PY" - <<'EOF' > "$W/vo"
from importlib.metadata import requires
import re
for r in requires("manim-voiceover") or []:
    if "extra ==" in r:
        continue
    name = re.split(r"[ ;<>=!~\[]", r, 1)[0]
    if name.lower() != "manim":
        print(r.split(";")[0].strip())
EOF
if [ -s "$W/vo" ]; then "$PY" -m pip install -q -r "$W/vo"; fi
"$PY" -m pip check || echo "  (pip check reported the conflicts above)"

say "3. Kokoro models into $RHOME/models"
mkdir -p "$RHOME/models"
for f in $KOKORO_FILES; do
  if [ ! -f "$RHOME/models/$f" ]; then
    curl -fsSL --retry 3 -o "$RHOME/models/$f.part" "$KOKORO_URL/$f"
    mv "$RHOME/models/$f.part" "$RHOME/models/$f"
  fi
  check_sum "$RHOME/models/$f" "$f"
done

say "4. vendor files into $RHOME/vendor"
mkdir -p "$RHOME/vendor"
for pkg in $VENDOR_PKGS; do
  dir="$RHOME/vendor/${pkg/@/-}"
  [ -d "$dir" ] && { echo "  present  $dir"; continue; }
  tmp="$W/${pkg/@/-}"; mkdir -p "$tmp/x"
  npm pack --silent --pack-destination "$tmp" "$pkg" >/dev/null
  tgz=$(ls "$tmp"/*.tgz)
  check_sum "$tgz" "$(basename "$tgz")"
  tar -xzf "$tgz" -C "$tmp/x"
  mv "$tmp/x/package" "$dir"
  echo "  unpacked $dir"
done

CONF="${EXPLAIN_CONFIG:-$HOME/.config/explain/config.env}"
say "5. settings file $CONF (not secret; edit voice and speed there)"
keep() {  # existing value of a setting the owner may have changed, else the default
  local v=""
  [ -f "$CONF" ] && v=$(sed -n "s/^$1=//p" "$CONF" | tail -1)
  printf '%s' "${v:-$2}"
}
CHROME=$(ls -d "$HOME"/.cache/ms-playwright/chromium-*/chrome-linux*/chrome 2>/dev/null | sort -V | tail -1 || true)
VOICE=$(keep REPORT_VOICE bm_george); SPEED=$(keep REPORT_TTS_SPEED 1.0); PROVIDER=$(keep REPORT_TTS_PROVIDER cpu)
FPS=$(keep REPORT_FPS 30); JOBS=$(keep REPORT_RENDER_JOBS 2)
mkdir -p "$(dirname "$CONF")"
cat > "$CONF.tmp" <<EOF
# explain skill settings. Nothing secret here.
# Paths are rewritten by scripts/install-env.sh; voice, speed, provider and render settings are kept.

# voice (any Kokoro voice id; b* voices speak British English, a* American)
REPORT_VOICE=$VOICE
REPORT_TTS_SPEED=$SPEED
REPORT_TTS_PROVIDER=$PROVIDER

# animation render: frames per second of the delivered video; scenes rendered at once (CPU cores)
REPORT_FPS=$FPS
REPORT_RENDER_JOBS=$JOBS

# paths
REPORT_PYTHON=$PY
REPORT_BIN=$ENV/bin
REPORT_HOME=$RHOME
REPORT_TTS_MODEL=$RHOME/models/kokoro-v1.0.onnx
REPORT_TTS_VOICES=$RHOME/models/voices-v1.0.bin
REPORT_CHROME=${CHROME:-}
EOF
mv "$CONF.tmp" "$CONF"
echo "  wrote $CONF (voice $VOICE, speed $SPEED, $PROVIDER)"
echo "  next: bash $HERE/check.sh"
