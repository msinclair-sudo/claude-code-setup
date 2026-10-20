#!/usr/bin/env bash
# explain skill: where its tools live, and the voice settings.
#
# Nothing here is secret, so it lives in a plain, visible file rather than the
# sensitive ~/.env:
#
#     ~/.config/explain/config.env        (override the path with EXPLAIN_CONFIG)
#
# scripts/install-env.sh writes it: the paths are rewritten on every run, the
# voice settings are kept once you have changed them. Edit it by hand to change
# voice or speed. Only REPORT_* lines are read, parsed line by line, never sourced.
#
#   REPORT_PYTHON        python of the `report` conda env
#   REPORT_BIN           that env's bin/ (ffmpeg, dot, manim go on PATH)
#   REPORT_HOME          models/ and vendor/ live here (e.g. ~/.local/share/explain)
#   REPORT_TTS_MODEL     Kokoro .onnx model
#   REPORT_TTS_VOICES    Kokoro voices .bin
#   REPORT_VOICE         Kokoro voice id, e.g. bm_george
#   REPORT_TTS_SPEED     speaking speed factor, e.g. 1.0
#   REPORT_TTS_PROVIDER  cpu | cuda
#   REPORT_CHROME        a Chrome/Chromium binary for kaleido and stills

_EXPLAIN_CONF="${EXPLAIN_CONFIG:-$HOME/.config/explain/config.env}"
if [ -f "$_EXPLAIN_CONF" ]; then
  while IFS= read -r _line || [ -n "$_line" ]; do
    case "$_line" in
      REPORT_*=*) ;;
      *) continue ;;
    esac
    _key=${_line%%=*}; _val=${_line#*=}
    case "$_val" in
      \"*\") _val=${_val#\"}; _val=${_val%\"} ;;
      \'*\') _val=${_val#\'}; _val=${_val%\'} ;;
    esac
    case "$_val" in "~/"*) _val="$HOME/${_val#\~/}" ;; esac
    export "$_key=$_val"
  done < "$_EXPLAIN_CONF"
  unset _line _key _val
else
  echo "warning: '$_EXPLAIN_CONF' not found; run scripts/install-env.sh (scripts/check.sh will fail until then)." >&2
fi
unset _EXPLAIN_CONF
