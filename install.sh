#!/usr/bin/env bash
# Claude Code environment installer
# Sets up: skills, statusline, global permissions, CLAUDE.md, hooks
# Optionally sets up the Obsidian vault MCP server and vault-specific skills.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="$SCRIPT_DIR/config.yaml"
PERMISSIONS_FILE="$SCRIPT_DIR/permissions.json"
INSTALL_DIR="$HOME/.claude/mcp/obsidian_vault"
SETTINGS_FILE="$HOME/.claude/settings.json"

# Skills are split into two groups:
#   - VAULT_SKILLS: depend on the obsidian-vault MCP server; installed only
#     when --vault_root is supplied.
#   - GENERAL_SKILLS: every other skill dir under skills/, auto-discovered and
#     installed on every machine. Drop a new skill folder into skills/ and it
#     is picked up automatically — no need to edit this list.
VAULT_SKILLS=(make-note process-notes explore-vault tracker request-task)

GENERAL_SKILLS=()
for SKILL_PATH in "$SCRIPT_DIR/skills"/*/; do
    [[ -d "$SKILL_PATH" ]] || continue
    SKILL_NAME="$(basename "$SKILL_PATH")"
    # Skip vault skills — they belong to the --vault_root group
    is_vault=false
    for VS in "${VAULT_SKILLS[@]}"; do
        [[ "$SKILL_NAME" == "$VS" ]] && { is_vault=true; break; }
    done
    [[ "$is_vault" == true ]] || GENERAL_SKILLS+=("$SKILL_NAME")
done

# ── Help menu ────────────────────────────────────────────────────────────────

show_help() {
    cat <<'EOF'
Usage: bash michaels_setup/install.sh [OPTIONS]

Installs Claude Code configuration: general skills, statusline, hooks,
global permissions, and CLAUDE.md. The Obsidian vault MCP server and its
related skills are installed only when --vault_root is supplied.

Options:
  --vault_root [PATH]   Install the Obsidian vault MCP server and vault-specific
                        skills (make-note, process-notes, explore-vault,
                        tracker, request-task).
                          - With PATH: use the given vault path directly.
                          - Without PATH: read vault_root* from config.yaml
                            and pick the first existing path.
                        Omit this flag entirely to skip vault installation
                        (useful on machines without Obsidian).

  -h, --help            Show this help message and exit.

Examples:
  bash michaels_setup/install.sh
      Install general skills + statusline + hooks. No vault MCP.

  bash michaels_setup/install.sh --vault_root
      Full install. Resolves vault path from config.yaml.

  bash michaels_setup/install.sh --vault_root "/mnt/c/Users/Me/Vault"
      Full install using the explicit vault path.

Requirements:
  - claude CLI (always)
  - uv         (only when installing the vault MCP server)
EOF
}

# ── Parse arguments ──────────────────────────────────────────────────────────

INSTALL_VAULT=false
VAULT_ROOT_ARG=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        -h|--help)
            show_help
            exit 0
            ;;
        --vault_root)
            INSTALL_VAULT=true
            # Optional value: only consume next arg if it doesn't look like a flag
            if [[ -n "${2:-}" && "$2" != -* ]]; then
                VAULT_ROOT_ARG="$2"
                shift 2
            else
                shift
            fi
            ;;
        --vault_root=*)
            INSTALL_VAULT=true
            VAULT_ROOT_ARG="${1#--vault_root=}"
            shift
            ;;
        *)
            echo "ERROR: Unknown option: $1" >&2
            echo "Run 'bash michaels_setup/install.sh --help' for usage." >&2
            exit 1
            ;;
    esac
done

# ── Resolve vault root (only if --vault_root was supplied) ───────────────────

VAULT_ROOT=""

if [[ "$INSTALL_VAULT" == true ]]; then
    if [[ -n "$VAULT_ROOT_ARG" ]]; then
        # Explicit path provided on the command line
        if [[ ! -d "$VAULT_ROOT_ARG" ]]; then
            echo "ERROR: --vault_root path does not exist: $VAULT_ROOT_ARG" >&2
            exit 1
        fi
        VAULT_ROOT="$VAULT_ROOT_ARG"
    else
        # Fall back to config.yaml lookup
        if [[ ! -f "$CONFIG_FILE" ]]; then
            echo "ERROR: config.yaml not found and no path given to --vault_root." >&2
            echo "  cp michaels_setup/config.example.yaml michaels_setup/config.yaml" >&2
            echo "  Then edit config.yaml with your local paths," >&2
            echo "  or pass the path directly: --vault_root /path/to/vault" >&2
            exit 1
        fi

        VAULT_ROOT=$(python3 -c "
import os
candidates = []
for line in open('$CONFIG_FILE'):
    line = line.strip()
    if line.startswith('vault_root'):
        path = line.split(':', 1)[1].strip().strip('\"').strip(\"'\")
        candidates.append(path)
for path in candidates:
    if os.path.isdir(path):
        print(path)
        break
")

        if [[ -z "$VAULT_ROOT" ]]; then
            echo "ERROR: No valid vault_root path found in config.yaml" >&2
            echo "  None of the vault_root* paths exist on this machine." >&2
            exit 1
        fi
    fi
fi

# ── Banner ───────────────────────────────────────────────────────────────────

echo ""
if [[ "$INSTALL_VAULT" == true ]]; then
    echo "Mode       : Full install (general + Obsidian vault MCP)"
    echo "Config     : $CONFIG_FILE"
    echo "Vault root : $VAULT_ROOT"
    echo "Install dir: $INSTALL_DIR"
else
    echo "Mode       : General install only (no Obsidian vault MCP)"
    echo "             Pass --vault_root to also install vault tools."
fi
echo ""

# ── Check for uv (vault install only) ────────────────────────────────────────

if [[ "$INSTALL_VAULT" == true ]]; then
    if ! command -v uv &>/dev/null; then
        echo "ERROR: 'uv' is not installed. Install it from https://docs.astral.sh/uv/" >&2
        exit 1
    fi
    echo "Found uv: $(uv --version)"
fi

# ── Copy server files + register MCP (vault install only) ────────────────────

if [[ "$INSTALL_VAULT" == true ]]; then
    mkdir -p "$INSTALL_DIR/tools"
    cp "$SCRIPT_DIR/server/server.py"        "$INSTALL_DIR/server.py"
    cp "$SCRIPT_DIR/server/config.py"        "$INSTALL_DIR/config.py"
    cp "$SCRIPT_DIR/server/helpers.py"       "$INSTALL_DIR/helpers.py"
    cp "$SCRIPT_DIR/server/rename_note.py"   "$INSTALL_DIR/rename_note.py"
    cp "$SCRIPT_DIR/server/resolve_links.py" "$INSTALL_DIR/resolve_links.py"
    cp "$SCRIPT_DIR/server/touch_vault.py"   "$INSTALL_DIR/touch_vault.py"
    cp "$SCRIPT_DIR/server/tools/__init__.py" "$INSTALL_DIR/tools/__init__.py"
    cp "$SCRIPT_DIR/server/tools/read.py"     "$INSTALL_DIR/tools/read.py"
    cp "$SCRIPT_DIR/server/tools/write.py"    "$INSTALL_DIR/tools/write.py"
    echo "Copied server files to $INSTALL_DIR"

    echo "Registering MCP server with Claude Code..."
    claude mcp remove obsidian-vault --scope user 2>/dev/null || true

    claude mcp add obsidian-vault \
        -s user \
        -e "VAULT_ROOT=$VAULT_ROOT" \
        -- uv run "$INSTALL_DIR/server.py"

    echo "  Registered obsidian-vault (user scope)"
    echo "  Server : $INSTALL_DIR/server.py"
    echo "  Vault  : $VAULT_ROOT"
fi

# ── Install skills ────────────────────────────────────────────────────────────

mkdir -p "$HOME/.claude/skills"

SKILLS_TO_INSTALL=("${GENERAL_SKILLS[@]}")
if [[ "$INSTALL_VAULT" == true ]]; then
    SKILLS_TO_INSTALL+=("${VAULT_SKILLS[@]}")
fi

for SKILL in "${SKILLS_TO_INSTALL[@]}"; do
    SKILL_DIR="$HOME/.claude/skills/$SKILL"
    echo "Installing $SKILL skill..."
    rm -rf "$SKILL_DIR"
    cp -r "$SCRIPT_DIR/skills/$SKILL" "$SKILL_DIR"
    echo "  Installed skill to $SKILL_DIR"
done

# ── Install hooks ─────────────────────────────────────────────────────────────

HOOKS_DIR="$HOME/.claude/hooks"
mkdir -p "$HOOKS_DIR"

echo "Installing hooks..."
cp "$SCRIPT_DIR/hooks/strip_cd.py" "$HOOKS_DIR/strip_cd.py"
chmod +x "$HOOKS_DIR/strip_cd.py"
echo "  Copied strip_cd.py to $HOOKS_DIR"

# ── Install statusline ────────────────────────────────────────────────────────

STATUSLINE_SCRIPT="$HOME/.claude/statusline.sh"

echo "Installing statusline..."
cp "$SCRIPT_DIR/shell/statusline.sh" "$STATUSLINE_SCRIPT"
chmod +x "$STATUSLINE_SCRIPT"
echo "  Copied statusline script to $STATUSLINE_SCRIPT"

# ── Install global CLAUDE.md ─────────────────────────────────────────────────

echo "Installing global CLAUDE.md..."
cp "$SCRIPT_DIR/global_claude.md" "$HOME/.claude/CLAUDE.md"
echo "  Copied to $HOME/.claude/CLAUDE.md"

# ── Merge settings.json (statusline + permissions + additionalDirectories) ───

echo "Updating global settings..."

REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

python3 - "$SETTINGS_FILE" "$PERMISSIONS_FILE" "$REPO_DIR" <<'PYEOF'
import json, sys, os

settings_file = sys.argv[1]
permissions_file = sys.argv[2]
repo_dir = sys.argv[3]

# Load existing settings
settings = {}
if os.path.exists(settings_file):
    with open(settings_file) as f:
        settings = json.load(f)

# Statusline
settings["statusLine"] = {
    "type": "command",
    "command": "~/.claude/statusline.sh"
}

# Permissions — merge from permissions.json if present (gitignored,
# machine-specific). When absent, leave existing permissions untouched.
existing_allow = settings.get("permissions", {}).get("allow", [])
new_rules = []
if os.path.exists(permissions_file):
    with open(permissions_file) as f:
        perms = json.load(f)
    new_rules = [r for r in perms.get("allow", []) if r not in existing_allow]
merged_allow = existing_allow + new_rules

if "permissions" not in settings:
    settings["permissions"] = {}
settings["permissions"]["allow"] = merged_allow

# additionalDirectories — add repo dir if not already present
dirs = settings.get("additionalDirectories", [])
if repo_dir not in dirs:
    dirs.append(repo_dir)
settings["additionalDirectories"] = dirs

# Hooks — register strip_cd as PreToolUse hook for Bash
hooks = settings.get("hooks", {})
pre_tool = hooks.get("PreToolUse", [])

# Check if strip_cd hook already registered
strip_cd_exists = any(
    any("strip_cd.py" in h.get("command", "") for h in entry.get("hooks", []))
    for entry in pre_tool
    if entry.get("matcher") == "Bash"
)

if not strip_cd_exists:
    pre_tool.append({
        "matcher": "Bash",
        "hooks": [{
            "type": "command",
            "command": "python3 ~/.claude/hooks/strip_cd.py"
        }]
    })
    hooks["PreToolUse"] = pre_tool
    settings["hooks"] = hooks

hooks_count = sum(len(entries) for entries in settings.get("hooks", {}).values())

# Write back
with open(settings_file, "w") as f:
    json.dump(settings, f, indent=2)
    f.write("\n")

print(f"  Updated {settings_file}")
print(f"    Permissions: {len(merged_allow)} rules ({len(new_rules)} new)")
print(f"    Additional dirs: {len(dirs)}")
print(f"    Hooks: {hooks_count} registered")
PYEOF

echo ""
echo "Installation complete."
if [[ "$INSTALL_VAULT" != true ]]; then
    echo "Note: Obsidian vault MCP was NOT installed."
    echo "      Re-run with --vault_root to enable vault tools."
fi
echo "Restart Claude Code for changes to take effect."
