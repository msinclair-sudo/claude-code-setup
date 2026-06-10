# Claude Code Setup

A one-command installer for a Claude Code working environment: skills, a custom
statusline, hooks, global permissions, and a shared `CLAUDE.md`. An optional
Obsidian-vault MCP server can be installed on top with a single flag.

Everything is deployed into `~/.claude/`. Re-running the installer is the only
supported way to update a deployed environment — edit the source here, then run
`install.sh` again.

---

## Quick start

```bash
# General install: skills + statusline + hooks + permissions + CLAUDE.md
bash install.sh

# Full install: the above PLUS the Obsidian-vault MCP server and its skills
bash install.sh --vault_root "/path/to/your/Obsidian Vault"

# Show all options
bash install.sh --help
```

Restart Claude Code after installing.

**Requirements:** the `claude` CLI is always required. `uv` is required only when
installing the vault MCP server (i.e. when `--vault_root` is passed).

---

## What the general install does

Running `bash install.sh` (no flags) installs, on every machine:

- **Skills** — every directory under `skills/` is auto-discovered and installed to
  `~/.claude/skills/`, except the five vault skills (those need `--vault_root`).
  Drop a new skill folder into `skills/` and it is picked up automatically.
- **Statusline** — `shell/statusline.sh` copied to `~/.claude/statusline.sh` and
  registered in `~/.claude/settings.json`.
- **Hooks** — `hooks/strip_cd.py` copied to `~/.claude/hooks/` and registered as a
  `PreToolUse` hook for Bash.
- **Permissions** — if `permissions.json` exists (gitignored, machine-specific;
  copy from `permissions.example.json`), its `allow` rules are merged into the
  `allow` list in `~/.claude/settings.json`. If the file is absent, this step is
  skipped and existing permissions are left untouched.

No Obsidian MCP server, no vault skills, and no `uv` are involved in this mode.

---

## The optional Obsidian-vault MCP server

Passing `--vault_root` additionally installs an MCP server that gives Claude Code
guarded read/write access to an Obsidian vault. Writes are restricted to
`claude_doc_dump/` staging directories — a separate Claude session integrates
those dumps into the real vault locations later.

With `--vault_root`, the installer also:

- Copies the server (`server/`) to `~/.claude/mcp/obsidian_vault/`.
- Registers it: `claude mcp add obsidian-vault -s user -e VAULT_ROOT=... -- uv run server.py`.
- Installs the five vault skills: `make-note`, `process-notes`, `explore-vault`,
  `tracker`, `request-task`.

Dependencies (`fastmcp`, `pydantic`) are declared as inline script metadata in
`server.py` and installed by `uv` automatically. The server starts fresh each
Claude session — there is no daemon to restart.

### Vault path

`--vault_root` accepts an explicit path. Without one, the installer reads
`config.yaml` (gitignored, machine-specific) and picks the first `vault_root*`
path that exists:

```bash
cp config.example.yaml config.yaml   # then edit with your local vault paths
bash install.sh --vault_root         # resolves the path from config.yaml
```

The vault path is injected as the `VAULT_ROOT` environment variable — no path is
hardcoded in the server. On a multi-machine setup, run the installer on each
machine with its own local path.

### Vault tools

**Read (unrestricted):** `vault_search`, `vault_read`, `vault_list`, `vault_tags`,
`vault_recent`, `vault_list_projects`, `vault_read_tracker`.

**Write (guarded):** `vault_create_note`, `vault_append`, `vault_edit_dump`,
`vault_rename`, `vault_import_file`, `vault_import_directory`,
`vault_resolve_links`, `vault_flag_pending`, `vault_clear_pending`,
`vault_add_tracker_item`, `vault_update_tracker_item`.

### Write rules

**Placement** — writes only go to `claude_doc_dump/` directories. The allowed
roots are defined in `server/config.py` (`ALLOWED_PLACEMENT_DIRS`); edit that list
for your own vault. Subdirectories of a dump root are allowed.

**Naming** — file stems must be `snake_case`, a numeric section (`01-Introduction`),
or a README (`my_script_README`). No camelCase or spaces.

**Tags** — at least one primary tag is required; secondary tags are unrestricted.
Primary tags (in `config.py`): `Writing` `Code` `Tracker` `Methods` `Todo`
`Scripts` `Theory` `Issues` `PhD` `Life`.

**Destinations** — every created note requires at least one wikilink pointing to
where the content should eventually be integrated. These appear in the frontmatter
and as a destinations line in the body.

---

## Updating a deployed environment

Edit the source files in this repository, then re-run `install.sh` (with
`--vault_root` if you use the vault server). The installer overwrites the deployed
copies under `~/.claude/`. Never edit `~/.claude/mcp/`, `~/.claude/skills/`, or
other `~/.claude/` paths directly — `install.sh` is the only deployment mechanism.

---

## Layout

```
install.sh               Installer
permissions.example.json Template for permission rules (copy to permissions.json)
config.example.yaml      Template for machine-specific vault paths (copy to config.yaml)
hooks/                strip_cd.py PreToolUse hook
shell/                statusline.sh
skills/               General + vault skills (auto-discovered by install.sh)
server/               Obsidian-vault MCP server (installed only with --vault_root)
```
