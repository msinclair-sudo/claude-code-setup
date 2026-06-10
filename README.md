# Obsidian Vault MCP Server

Gives Claude Code read/write access to the Obsidian vault with enforced conventions.
Write access is restricted to `claude_doc_dump/` directories — a privileged Claude
session processes those dumps into the correct vault locations later.

---

## Installation

Copy this folder to the target machine (or access it via OneDrive), then run:

```bash
bash install.sh --vault-root "/path/to/your/vault"
```

Or run without arguments to be prompted:

```bash
bash install.sh
```

The script will:
1. Copy `server.py` to `~/.claude/mcp/obsidian_vault/`
2. Install Python dependencies (`fastmcp`, `pydantic`)
3. Add the `obsidian-vault` entry to `~/.claude/settings.json`

Restart Claude Code after installing.

---

## Vault path across machines

Each machine stores its own vault path in `~/.claude/settings.json`.
Run `install.sh` on each machine with the correct local path — the server
itself contains no hardcoded paths.

---

## Tools

### Read (unrestricted)

| Tool | What it does |
|------|-------------|
| `vault_search` | Full-text or tag search. Returns path, tags, excerpt |
| `vault_read` | Read a note by path or filename stem |
| `vault_list` | List files and subdirs in a vault directory |
| `vault_tags` | All tags in use, grouped primary vs secondary |

### Write (guarded)

| Tool | What it does |
|------|-------------|
| `vault_create_note` | Create a note in a `claude_doc_dump/` dir |
| `vault_append` | Append a section to an existing dump note |
| `vault_rename` | Rename a note via `scripts/rename_note.py` (updates all wikilinks) |
| `vault_import_file` | Import a local file into a dump dir (bypasses context window) |
| `vault_import_directory` | Recursively import a directory, mirroring structure |
| `vault_resolve_links` | Resolve broken markdown links in a dump dir after import |
| `vault_flag_pending` | Add a `[!todo] Pending dump` callout to a destination file |
| `vault_clear_pending` | Remove pending callout(s) from a destination file after integration |

---

## Write rules

**Placement** — writes only go to `claude_doc_dump/` inside each project:
```
PhD/Literature Review/claude_doc_dump/
PhD/mtDNA/claude_doc_dump/
PhD/Evolution theory/claude_doc_dump/
PhD/Hazelnut Project/claude_doc_dump/
scripts/claude_doc_dump/
Notes to process/claude_doc_dump/
```
Subdirectories within the dump are allowed for session organisation,
e.g. `PhD/Literature Review/claude_doc_dump/embeddings/`.

**Destinations** — every note and every appended section requires at least one
wikilink pointing to where the content should eventually be integrated:
```
destinations: ["[[01-Introduction]]", "[[02-Methods-and-initial-findings]]"]
```
These appear in the frontmatter and as a `**→ Destinations:**` line in the body.

**Naming** — file stems must be `snake_case`, a numeric section (`01-Introduction`),
or a script README (`my_script_README`). No camelCase or spaces.

**Tags** — at least one primary tag required. Secondary tags are unrestricted.

Primary tags: `Writing` `Code` `Tracker` `Methods` `Todo` `Scripts` `Theory` `Issues` `PhD` `Life`

---

## Updating

After editing `server.py` on one machine, copy the updated file to the other
machines' `~/.claude/mcp/obsidian_vault/server.py` (or re-run `install.sh`).
No restart of a daemon is needed — the server starts fresh each Claude session.
