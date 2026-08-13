#!/usr/bin/env bash
# Remove the biblion MCP registration (user scope). Run before re-registering
# after a relocation, or to fully unhook the skill.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=/dev/null
source "$HERE/../config.sh"

NAME="$BIBLION_MCP_NAME"
if ! command -v claude >/dev/null; then
  echo "error: the 'claude' CLI is not on PATH." >&2
  exit 1
fi
claude mcp remove "$NAME" -s user >/dev/null 2>&1 || true
claude mcp remove "$NAME"         >/dev/null 2>&1 || true
echo "Removed MCP '$NAME' (if it was registered). Restart Claude Code to drop the tools."
