#!/usr/bin/env bash
# biblion skill — code + runtime locations.
#
# SECURE SOURCE: the real values live in the global ~/.env (chmod 600, outside
# any git repo), shared with the other skills and the biblion daemon. This file
# reads ONLY the BIBLION_* keys from that env — parsed line by line, never
# sourced — so unrelated entries (e.g. API keys) are NEVER read or exported into
# the server's environment. No machine paths, secrets, or fallback defaults are
# committed inside the skill; a missing value stays unset and scripts/check.sh
# fails clearly rather than registering a wrong path.
#
#   To relocate biblion or rotate keys, edit ~/.env (NOT this file), then re-run:
#     scripts/check.sh  &&  scripts/register.sh
#
# Override the global env path with BIBLION_GLOBAL_ENV if it lives elsewhere.
#
# Variables consumed (set them in ~/.env):
#   BIBLION_HOME    dir that CONTAINS the `biblion/` package (i.e. has biblion/mcp_server.py).
#                   The server is launched by running biblion/mcp_server.py DIRECTLY from here
#                   (by path, not `python -m`), so the CODE always comes from this dir — even if
#                   the interpreter also has biblion pip/editable-installed elsewhere.
#   BIBLION_PYTHON  a Python interpreter that has biblion's runtime DEPS installed
#                   (`pip install 'biblion[mcp]'`). Deps come from here; code comes from BIBLION_HOME.
#   BIBLION_DATA_DIR  dir holding the project databases as <name>/<name>.db (read-only at query time).
#   BIBLION_TRANSPORT stdio (default; Claude launches the server on demand) | http (running server).
#   BIBLION_HTTP_URL  the URL to register when BIBLION_TRANSPORT=http (the docker-compose mcp service).
#   BIBLION_MCP_NAME  the name the server is registered under (the tools appear as <name> in /mcp).

# Load ONLY the BIBLION_* keys from the global secure env — parsed, not sourced,
# so API keys and any other entries are never read or exported.
_BIBLION_GLOBAL_ENV="${BIBLION_GLOBAL_ENV:-$HOME/.env}"
if [ -f "$_BIBLION_GLOBAL_ENV" ]; then
  while IFS= read -r _line || [ -n "$_line" ]; do
    case "$_line" in
      BIBLION_*=*) ;;            # only our allowlisted keys
      *) continue ;;
    esac
    _key=${_line%%=*}; _val=${_line#*=}
    case "$_val" in
      \"*\") _val=${_val#\"}; _val=${_val%\"} ;;
      \'*\') _val=${_val#\'}; _val=${_val%\'} ;;
    esac
    export "$_key=$_val"
  done < "$_BIBLION_GLOBAL_ENV"
  unset _line _key _val
else
  echo "warning: global env '$_BIBLION_GLOBAL_ENV' not found; biblion config will be unset (check.sh will fail)." >&2
fi
