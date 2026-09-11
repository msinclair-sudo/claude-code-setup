# Claude Code Setup

One Claude Code environment, kept the same across every machine I work on:
skills, a custom statusline, global permissions, and a shared `CLAUDE.md`.

This repo is the source of truth. Everything lands in `~/.claude/`, so edit the
files here and run `install.sh` again to update a machine. Editing anything under
`~/.claude/` directly gets overwritten on the next run.

---

## Quick start

```bash
# Install: skills + statusline + permissions + CLAUDE.md
bash install.sh

# Show all options
bash install.sh --help
```

Restart Claude Code afterwards. The `claude` CLI is the only requirement.

---

## What the installer does

**Skills.** The installer finds every directory under `skills/` and copies it
to `~/.claude/skills/`. Drop a new skill folder in and the next run picks it
up; you never edit the installer to add one.

**Statusline.** `shell/statusline.sh` goes to `~/.claude/statusline.sh`, then
gets registered in `~/.claude/settings.json`.

**Hooks.** Any `.py` in `hooks/` goes to `~/.claude/hooks/` and is registered the
same way. The repo ships none at present.

**Permissions.** If `permissions.json` exists, the installer merges its `allow`
rules into `~/.claude/settings.json`. The file is gitignored and
machine-specific; copy `permissions.example.json` to create it. Without it, the
installer skips the step and leaves your existing permissions alone.

**Global CLAUDE.md.** `global_claude.md` becomes `~/.claude/CLAUDE.md`, the
standing instructions every session on the machine loads. It carries the path
conventions and the voice I want writing in.

---

## Skills

### Writing

| Skill | What it does |
|---|---|
| `humanizer` | Rewrites AI-sounding prose so it reads like the writer, without changing what it says. Patterns are ordered strongest-first; weaker ones need corroboration before they justify an edit. |
| `write-pass` | Two-pass elevation workflow for manuscripts: `humanizer`, then `de-densify`. |
| `de-densify` | Splits overloaded sentences, unpacks buried definitions, and breaks up evidence parades. The one skill here that expands rather than cuts. |
| `schimel-science-writing` | Knowledge base from Schimel's *Writing Science* — story structure, the knowledge gap, condensing. |
| `sentence-prose` | Knowledge base from Gopen & Swan's *The Science of Scientific Writing* — topic and stress position, reader expectation. |
| `google-devdocs-style` | Google's developer documentation style guide, for technical writing and term rulings. |
| `research-brief` | Writes briefs for research agents that collect generalisable facts rather than confirming a design back to itself. |

### Obsidian

| Skill | What it does |
|---|---|
| `obsidian-cli` | Read, create, and search vault notes through Obsidian's first-party CLI. Also covers plugin and theme development. Requires Obsidian running. |
| `obsidian-markdown` | Obsidian-flavoured Markdown: wikilinks, embeds, callouts, properties. |
| `obsidian-bases` | `.base` files — database-like views, filters, formulas. |
| `json-canvas` | `.canvas` files — nodes, edges, groups. |
| `md-docx` | Markdown ⇄ Word via Pandoc, preserving callouts and matching APA citations to BibTeX keys. |

### Research and tooling

| Skill | What it does |
|---|---|
| `biblion` | Query a biblion corpus (citation graph, embeddings, concept spine) or ingest new literature. |
| `book-to-skill` | Converts books and documents into structured agent skills. |
| `defuddle` | Extracts clean markdown from web pages, dropping navigation and clutter. |

### Agent Workstream Harness

`harness`, `harness-root`, `harness-upward`, `harness-downward` handle role-tree
coordination for multi-agent work. `harness` resolves a session's position and
loads whichever of the other three applies.

---

## Retiring a skill

Installing copies files but never deletes them, so a skill you retire here
survives on every machine that already had it. To retire one properly, delete its
folder from `skills/`, then run `--prune` on each machine:

```bash
bash install.sh --prune        # reports, then asks before removing
bash install.sh --prune --yes  # no prompt
```

`--prune` only removes skills a previous install deployed, which it tracks in
`~/.claude/.install-manifest.json`. Skills that arrived another way, from an MCP
server or a plugin, stay put even though this repo does not define them. Without
the flag, the installer names what is retired and leaves it alone.

On a machine that predates the manifest, the first run records what is installed
and removes nothing. Retirements propagate from the run after that.

---

## Layout

```
install.sh               Installer
global_claude.md         Becomes ~/.claude/CLAUDE.md
permissions.example.json Template for permission rules (copy to permissions.json)
config.example.yaml      Template for machine-specific paths (copy to config.yaml)
hooks/                   Hooks, copied to ~/.claude/hooks/ if present
shell/                   statusline.sh
skills/                  Skills, auto-discovered by install.sh
```
