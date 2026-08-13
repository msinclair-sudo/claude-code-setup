#!/usr/bin/env bash
# Register the biblion MCP server with Claude Code at USER scope, using the
# `claude mcp add` CLI (version-safe; writes to whatever store Claude Code uses).
# Idempotent: removes any existing registration of the same name first.
#
# stdio (default): Claude launches `$BIBLION_PYTHON $BIBLION_HOME/biblion/mcp_server.py`
#   per session — running the server file directly by PATH (not `-m`), so the CODE
#   always comes from $BIBLION_HOME regardless of any pip/editable install in the
#   interpreter. DBs are read from $BIBLION_DATA_DIR. http: registers $BIBLION_HTTP_URL.
#
# After running, restart Claude Code (or use /mcp to reconnect) so the new
# server is picked up.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=/dev/null
source "$HERE/../config.sh"

if ! command -v claude >/dev/null; then
  echo "error: the 'claude' CLI is not on PATH; cannot register." >&2
  exit 1
fi

NAME="$BIBLION_MCP_NAME"
echo "Registering MCP '$NAME' (user scope, transport=$BIBLION_TRANSPORT)…"

# Remove any prior registration so this is a clean overwrite (ignore if absent).
claude mcp remove "$NAME" -s user  >/dev/null 2>&1 || true
claude mcp remove "$NAME"          >/dev/null 2>&1 || true

if [ "$BIBLION_TRANSPORT" = "http" ]; then
  claude mcp add "$NAME" --scope user --transport http "$BIBLION_HTTP_URL"
else
  # stdio: run the server FILE directly from BIBLION_HOME (so the code location is
  # truly switchable), with deps supplied by BIBLION_PYTHON.
  SERVER="$BIBLION_HOME/biblion/mcp_server.py"
  if [ ! -f "$SERVER" ]; then
    echo "error: server file not found: $SERVER (check BIBLION_HOME in config.sh)" >&2
    exit 1
  fi
  claude mcp add "$NAME" --scope user \
    -e "BIBLION_DATA_DIR=$BIBLION_DATA_DIR" \
    -e "BIBLION_MCP_TRANSPORT=stdio" \
    -- "$BIBLION_PYTHON" "$SERVER"
fi

echo
echo "Registered. Current MCP servers:"
claude mcp list 2>/dev/null | sed 's/^/  /' || true
echo
echo "Restart Claude Code (or run /mcp) to load the '$NAME' tools."
