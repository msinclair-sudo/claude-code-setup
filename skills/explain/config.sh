#!/usr/bin/env bash
# explain skill: where its tools live.
#
# The values live in the global ~/.env (chmod 600, outside any repo). This file
# reads ONLY the REPORT_* keys from it, parsed line by line and never sourced,
# so API keys and other entries are never read or exported. Nothing machine
# specific is committed here; a missing key stays unset and scripts/check.sh
# says which.
#
#   Keys (scripts/install-env.sh prints a filled block to append):
#   REPORT_PYTHON        python of the `report` conda env
#   REPORT_BIN           that env's bin/ (ffmpeg, dot, manim go on PATH)
#   REPORT_HOME          models/ and vendor/ live here (e.g. ~/.local/share/explain)
#   REPORT_TTS_MODEL     Kokoro .onnx model
#   REPORT_TTS_VOICES    Kokoro voices .bin
#   REPORT_VOICE         Kokoro voice id, e.g. bf_emma
#   REPORT_TTS_SPEED     speaking speed factor, e.g. 1.0
#   REPORT_TTS_PROVIDER  cpu | cuda
#   REPORT_CHROME        a Chrome/Chromium binary for kaleido and stills
#
# The env file is $EXPLAIN_GLOBAL_ENV, else $MCP_ENV (exported by install.sh),
# else ~/.env.

_EXPLAIN_ENV="${EXPLAIN_GLOBAL_ENV:-${MCP_ENV:-$HOME/.env}}"
if [ -f "$_EXPLAIN_ENV" ]; then
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
  done < "$_EXPLAIN_ENV"
  unset _line _key _val
else
  echo "warning: env file '$_EXPLAIN_ENV' not found; explain config is unset (scripts/check.sh will fail)." >&2
fi
unset _EXPLAIN_ENV
