#!/usr/bin/env bash
# Sanity-check the biblion skill config BEFORE registering. Prints PASS/FAIL per
# item and exits non-zero if anything would stop the MCP server from working.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=/dev/null
source "$HERE/../config.sh"

fail=0
ok()   { printf '  PASS  %s\n' "$1"; }
bad()  { printf '  FAIL  %s\n' "$1"; fail=1; }

echo "biblion skill — config check (transport=$BIBLION_TRANSPORT)"

# 1. The server FILE exists at BIBLION_HOME (this exact file is what runs), the
#    interpreter is usable, and the MCP deps are importable from it. The server is
#    launched by path (not `-m`), so we validate the file + deps, not package import.
SERVER="$BIBLION_HOME/biblion/mcp_server.py"
if [ -f "$SERVER" ]; then
  ok "server file present  ($SERVER)"
else
  bad "server file missing  ($SERVER) — check BIBLION_HOME"
fi
if [ -x "$BIBLION_PYTHON" ]; then
  ok "BIBLION_PYTHON is executable  ($BIBLION_PYTHON)"
else
  bad "BIBLION_PYTHON not executable  ($BIBLION_PYTHON)"
fi
if [ -f "$SERVER" ] && "$BIBLION_PYTHON" -m py_compile "$SERVER" 2>/dev/null; then
  ok "server file compiles under BIBLION_PYTHON"
else
  bad "server file does not compile under BIBLION_PYTHON"
fi
if "$BIBLION_PYTHON" -c "import mcp.server.fastmcp, pydantic" 2>/dev/null; then
  ok "MCP deps importable from BIBLION_PYTHON (mcp, pydantic)"
else
  bad "MCP deps missing — run: $BIBLION_PYTHON -m pip install 'biblion[mcp]'"
fi

# 2. Data dir + at least one project DB.
if [ -d "$BIBLION_DATA_DIR" ]; then
  projects=$(find "$BIBLION_DATA_DIR" -maxdepth 2 -name '*.db' ! -name '*_snapshot.db' ! -name '*_claims.db' 2>/dev/null | head -5)
  if [ -n "$projects" ]; then
    ok "BIBLION_DATA_DIR has project DB(s):"; echo "$projects" | sed 's/^/          /'
  else
    bad "BIBLION_DATA_DIR has no <name>/<name>.db projects  ($BIBLION_DATA_DIR)"
  fi
else
  bad "BIBLION_DATA_DIR does not exist  ($BIBLION_DATA_DIR)"
fi

# 3. http only: is the URL reachable?
if [ "$BIBLION_TRANSPORT" = "http" ]; then
  if command -v curl >/dev/null && curl -s -o /dev/null --max-time 3 "$BIBLION_HTTP_URL"; then
    ok "http endpoint reachable  ($BIBLION_HTTP_URL)"
  else
    bad "http endpoint not reachable ($BIBLION_HTTP_URL) — is the container up? (docker compose up -d mcp)"
  fi
fi

echo
if [ "$fail" -eq 0 ]; then echo "All checks passed. Next: scripts/register.sh"; else echo "Fix the FAIL items, then re-run."; fi
exit "$fail"
