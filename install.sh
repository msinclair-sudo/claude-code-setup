#!/usr/bin/env bash
# Claude Code environment installer
# Sets up: skills, statusline, global permissions, CLAUDE.md
# Optionally sets up the Obsidian vault MCP server and vault-specific skills.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
CONFIG_FILE="$SCRIPT_DIR/config.yaml"
PERMISSIONS_FILE="$SCRIPT_DIR/permissions.json"
INSTALL_DIR="$HOME/.claude/mcp/obsidian_vault"
SETTINGS_FILE="$HOME/.claude/settings.json"

# ~/.env — THE single source of truth for host-specific paths/values (vault
# roots, biblion locations, etc.) plus the user's API keys. Per machine; not in
# the repo. Copy/append the keys from .env.example. We read ONLY our own
# allowlisted keys (VAULT_*/OBSIDIAN_*; biblion's config.sh reads BIBLION_*
# itself) — parsed, not sourced, so unrelated entries like API keys are never
# pulled into this process. MCP_ENV is exported so the installed skill copies
# (e.g. ~/.claude/skills/biblion/config.sh) resolve back to this same file.
ENV_FILE="$HOME/.env"
if [[ -f "$ENV_FILE" ]]; then
    while IFS= read -r _line || [[ -n "$_line" ]]; do
        case "$_line" in
            VAULT_ROOT=*|VAULT_ROOT[0-9]=*|OBSIDIAN_BIN=*) ;;
            *) continue ;;
        esac
        _key=${_line%%=*}; _val=${_line#*=}
        case "$_val" in
            \"*\") _val=${_val#\"}; _val=${_val%\"} ;;
            \'*\') _val=${_val#\'}; _val=${_val%\'} ;;
        esac
        export "$_key=$_val"
    done < "$ENV_FILE"
    unset _line _key _val
    export MCP_ENV="$ENV_FILE"
fi

# Skills are split into two groups:
#   - VAULT_SKILLS: depend on the obsidian-vault MCP server; installed only
#     when --vault_root is supplied.
#   - GENERAL_SKILLS: every other skill dir under skills/, auto-discovered and
#     installed on every machine. Drop a new skill folder into skills/ and it
#     is picked up automatically — no need to edit this list.
VAULT_SKILLS=(vault)

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

Installs Claude Code configuration: general skills, statusline,
global permissions, and CLAUDE.md. The Obsidian vault MCP server and its
related skills are installed only when --vault_root is supplied.

Options:
  --vault_root [PATH]   Install the Obsidian vault MCP server and vault-specific
                        skills (make-note, process-notes, explore-vault,
                        tracker, request-task).
                          - With PATH: use the given vault path directly
                            (must exist).
                          - Without PATH: read vault_root* from config.yaml
                            and pick the first existing path.
                        A valid vault root is REQUIRED to install the MCP: if
                        config.yaml specifies none that exists on this machine,
                        PATH must be given here or the install aborts.
                        Omit this flag entirely to skip vault installation
                        (useful on machines without Obsidian).

  --biblion             Register the biblion MCP server after installing skills.
                        The biblion skill itself is always installed (it is a
                        general skill); this flag additionally runs the skill's
                        own scripts/check.sh and, if checks pass, scripts/
                        register.sh to register the biblion MCP at user scope.
                        Machine-specific paths come from the skill's config.sh.
                        If checks fail (e.g. biblion absent on this machine) the
                        MCP is skipped without aborting the install.

  -h, --help            Show this help message and exit.

Examples:
  bash michaels_setup/install.sh
      Install general skills + statusline. No vault MCP.

  bash michaels_setup/install.sh --vault_root
      Full install. Resolves vault path from config.yaml.

  bash michaels_setup/install.sh --vault_root "/mnt/c/Users/Me/Vault"
      Full install using the explicit vault path.

  bash michaels_setup/install.sh --biblion
      Install skills, then register the biblion MCP server (user scope).

Requirements:
  - claude CLI (always)
  - uv         (only when installing the vault MCP server)
EOF
}

# ── Parse arguments ──────────────────────────────────────────────────────────

INSTALL_VAULT=false
VAULT_ROOT_ARG=""
INSTALL_BIBLION=false

while [[ $# -gt 0 ]]; do
    case "$1" in
        -h|--help)
            show_help
            exit 0
            ;;
        --biblion)
            INSTALL_BIBLION=true
            shift
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

# ── Resolve vault root (required when installing the MCP) ────────────────────
#
# A valid vault root is REQUIRED to install the MCP. It is satisfied by, in order:
#   1. an explicit --vault_root PATH on the command line (must exist on disk), or
#   2. an internally specified path in config.yaml (first vault_root* that exists).
# If neither yields an existing directory, the vault root is required and the
# install aborts — the MCP is never registered without one.

VAULT_ROOT=""

# The Obsidian vault MCP server was archived to
# skill_inspiration/archived-obsidian-vault-mcp/. Vault access is now provided
# by the obsidian-cli skill (a general skill). If the MCP source is absent,
# disable the vault-MCP install path and fall back to a general install.
if [[ "$INSTALL_VAULT" == true && ! -d "$SCRIPT_DIR/server" ]]; then
    echo "NOTE: --vault_root was requested, but the vault MCP server source is" >&2
    echo "      archived (skill_inspiration/archived-obsidian-vault-mcp/)." >&2
    echo "      The Obsidian vault MCP is no longer installed; vault access is" >&2
    echo "      now via the obsidian-cli skill. Proceeding with general install." >&2
    INSTALL_VAULT=false
fi

if [[ "$INSTALL_VAULT" == true ]]; then
    if [[ -n "$VAULT_ROOT_ARG" ]]; then
        # Explicit path provided on the command line — must exist.
        if [[ ! -d "$VAULT_ROOT_ARG" ]]; then
            echo "ERROR: --vault_root path does not exist: $VAULT_ROOT_ARG" >&2
            exit 1
        fi
        VAULT_ROOT="$VAULT_ROOT_ARG"
    elif [[ -n "$VAULT_ROOT" && -d "$VAULT_ROOT" ]]; then
        : # already resolved from .env (VAULT_ROOT set and exists)
    elif [[ -n "${VAULT_ROOT1:-}${VAULT_ROOT2:-}${VAULT_ROOT3:-}" ]]; then
        # No explicit path — pick the first VAULT_ROOT* from .env that exists.
        for cand in "${VAULT_ROOT1:-}" "${VAULT_ROOT2:-}" "${VAULT_ROOT3:-}"; do
            if [[ -n "$cand" && -d "$cand" ]]; then VAULT_ROOT="$cand"; break; fi
        done
    elif [[ -f "$CONFIG_FILE" ]]; then
        # No explicit path — fall back to the internally specified config path,
        # selecting the first vault_root* candidate that exists on this machine.
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
    fi

    # Required: if no existing vault root was resolved from flag or config, abort.
    if [[ -z "$VAULT_ROOT" ]]; then
        echo "ERROR: A vault root is required to install the MCP, but none was found." >&2
        if [[ ! -f "$CONFIG_FILE" ]]; then
            echo "  config.yaml does not exist, and no path was given to --vault_root." >&2
            echo "    cp michaels_setup/config.example.yaml michaels_setup/config.yaml  (then edit it)" >&2
        else
            echo "  config.yaml specifies no vault_root* path that exists on this machine." >&2
        fi
        echo "  Pass the path explicitly:  --vault_root /path/to/vault" >&2
        exit 1
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
if [[ "$INSTALL_BIBLION" == true ]]; then
    echo "biblion MCP : will register after skills (--biblion)"
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
    cp "$SCRIPT_DIR/server/touch_vault.py"   "$INSTALL_DIR/touch_vault.py"
    cp "$SCRIPT_DIR/server/tools/__init__.py" "$INSTALL_DIR/tools/__init__.py"
    cp "$SCRIPT_DIR/server/tools/read.py"     "$INSTALL_DIR/tools/read.py"
    cp "$SCRIPT_DIR/server/tools/write.py"    "$INSTALL_DIR/tools/write.py"
    echo "Copied server files to $INSTALL_DIR"

    # Deploy the rename_note.py script into the vault. The repo is the source of
    # truth; vault_rename invokes the deployed copy at <VAULT_ROOT>/scripts/.
    mkdir -p "$VAULT_ROOT/scripts"
    cp "$SCRIPT_DIR/server/rename_note.py" "$VAULT_ROOT/scripts/rename_note.py"
    echo "Deployed rename_note.py to $VAULT_ROOT/scripts/"

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
    # Vault skills are delivered with the vault itself, so their source may not
    # live in the repo. Skip (don't abort under set -e) when the source is absent.
    if [[ ! -d "$SCRIPT_DIR/skills/$SKILL" ]]; then
        echo "  WARNING: skill source not found, skipping: $SKILL"
        continue
    fi
    SKILL_DIR="$HOME/.claude/skills/$SKILL"
    echo "Installing $SKILL skill..."
    rm -rf "$SKILL_DIR"
    cp -r "$SCRIPT_DIR/skills/$SKILL" "$SKILL_DIR"
    echo "  Installed skill to $SKILL_DIR"
done

# ── Install harness runtime + workflows ──────────────────────────────────────
#
# The four harness skills (harness, -upward, -downward, -root) are installed
# above, auto-discovered under skills/. This block installs what those skills
# call: the `harness` CLI and the guard-hook templates it scaffolds into a repo.
#
# Nothing is enrolled by default. A session takes a role only in a project that
# has BOTH a committed .harness/tree.json and a local binding under
# ~/.claude/harness/<slug>/ — so installing this changes no existing behaviour.
# Per-project bindings and locks live beside the CLI and are never touched here.

if [[ -d "$SCRIPT_DIR/harness" ]]; then
    echo "Installing harness runtime..."
    mkdir -p "$HOME/.claude/harness/bin"
    # Every executable in bin/, not just the CLI: harness-gui is a second one,
    # and naming them individually is how the next one gets forgotten.
    cp "$SCRIPT_DIR/harness/bin/"* "$HOME/.claude/harness/bin/"
    chmod +x "$HOME/.claude/harness/bin/"*
    rm -rf "$HOME/.claude/harness/templates"
    cp -r "$SCRIPT_DIR/harness/templates" "$HOME/.claude/harness/templates"
    chmod +x "$HOME/.claude/harness/templates/hooks/"*
    # On PATH, without editing anyone's shell profile. ~/.local/bin is on the
    # default PATH on every distro this targets and is already exported by the
    # stock .profile, so a symlink there is the whole job -- and `resolve()` in
    # both scripts follows it, so each still finds its sibling.
    if [[ -d "$HOME/.local/bin" ]] || mkdir -p "$HOME/.local/bin" 2>/dev/null; then
        ln -sf "$HOME/.claude/harness/bin/harness"     "$HOME/.local/bin/harness"
        ln -sf "$HOME/.claude/harness/bin/harness-gui" "$HOME/.local/bin/harness-gui"
        echo "  Linked harness and harness-gui into $HOME/.local/bin"
        case ":$PATH:" in
            *":$HOME/.local/bin:"*) ;;
            *) echo "  NOTE: $HOME/.local/bin is not on your PATH in this shell." ;;
        esac
    fi
    echo "  Installed harness CLI to $HOME/.claude/harness/bin/harness"
    echo "  Installed harness viewer  (harness gui)"
    echo "  Installed guard templates to $HOME/.claude/harness/templates/"
fi


# ── Register biblion MCP (opt-in, --biblion) ─────────────────────────────────
#
# The biblion skill is self-contained: it carries its own config.sh and
# scripts/{check,register,unregister}.sh that register the read-only biblion MCP
# at user scope. The skill is always installed above (general skill); this block
# only runs its registration when --biblion is passed. check.sh validates the
# machine-specific paths in the *installed* config.sh first, so an install on a
# machine without biblion skips the MCP cleanly instead of aborting under set -e.

if [[ "$INSTALL_BIBLION" == true ]]; then
    BIBLION_SKILL_DIR="$HOME/.claude/skills/biblion"
    echo "Registering biblion MCP server..."
    if [[ ! -d "$BIBLION_SKILL_DIR" ]]; then
        echo "  WARNING: biblion skill not installed; cannot register MCP."
    elif bash "$BIBLION_SKILL_DIR/scripts/check.sh"; then
        bash "$BIBLION_SKILL_DIR/scripts/register.sh"
    else
        echo "  WARNING: biblion check.sh failed — MCP not registered." >&2
        echo "           Fix the paths in skills/biblion/config.sh and re-run" >&2
        echo "           install.sh --biblion (or scripts/register.sh directly)." >&2
    fi
fi

# ── Install statusline ────────────────────────────────────────────────────────

STATUSLINE_SCRIPT="$HOME/.claude/statusline.sh"

echo "Installing statusline..."
cp "$SCRIPT_DIR/shell/statusline.sh" "$STATUSLINE_SCRIPT"
chmod +x "$STATUSLINE_SCRIPT"
echo "  Copied statusline script to $STATUSLINE_SCRIPT"

# ── Merge settings.json (statusline + permissions + additionalDirectories) ───

echo "Updating global settings..."

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

# Hooks — strip out any previously-registered strip_cd PreToolUse hook
hooks = settings.get("hooks", {})
pre_tool = hooks.get("PreToolUse", [])
cleaned_pre_tool = []
for entry in pre_tool:
    entry["hooks"] = [
        h for h in entry.get("hooks", [])
        if "strip_cd.py" not in h.get("command", "")
    ]
    if entry["hooks"]:
        cleaned_pre_tool.append(entry)
if cleaned_pre_tool:
    hooks["PreToolUse"] = cleaned_pre_tool
elif "PreToolUse" in hooks:
    del hooks["PreToolUse"]
if hooks:
    settings["hooks"] = hooks
elif "hooks" in settings:
    del settings["hooks"]

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
if [[ "$INSTALL_BIBLION" != true ]]; then
    echo "Note: biblion MCP was NOT registered."
    echo "      Re-run with --biblion to register it (the skill is installed)."
fi
echo "Restart Claude Code for changes to take effect."
