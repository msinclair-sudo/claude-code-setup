---
name: obsidian-cli
description: Interact with Obsidian vaults using the Obsidian CLI to read, create, search, and manage notes, tasks, properties, and more. Also supports plugin and theme development with commands to reload plugins, run JavaScript, capture errors, take screenshots, and inspect the DOM. Use when the user asks to interact with their Obsidian vault, manage notes, search vault content, perform vault operations from the command line, or develop and debug Obsidian plugins and themes.
---

# Obsidian CLI

Use the `obsidian` CLI to interact with a running Obsidian instance. Requires Obsidian to be open.

## Setup (this machine: WSL → Windows Obsidian)

**Just run `obsidian …` directly — it is already on PATH and works from any
directory.** A WSL wrapper at `~/.local/bin/obsidian` (on PATH) forwards to the
Windows redirector, so every `obsidian …` example in this skill runs verbatim:

```bash
obsidian vault                 # -> name=Michael.md, path=A:\Obsidian Vault\Michael.md
obsidian read file="My Note"
```

This vault is driven by **Obsidian on Windows**; Claude Code runs in **WSL**. The
CLI talks to the app over IPC on the *same OS*, so the Linux binary is useless
here — the wrapper forwards to the **Windows** `Obsidian.com` redirector, which
reaches the running app over IPC. **The skill cannot operate while Obsidian is
closed** — fall back to direct file edits under the vault root in that case.

**Confirmed working (2026-06-20):** `obsidian vault` returns the open vault
`Michael.md` (`A:\Obsidian Vault\Michael.md`, 440 files).

### If `obsidian` is not found (fresh machine)

Prerequisites (one-time, on the Windows side):
1. Obsidian **≥ 1.12.4** installed and running on Windows.
2. In Obsidian: **Settings → General → Command line interface → Register CLI**.

Then either invoke the Windows redirector by full path:

```bash
"/mnt/c/Users/Owner/AppData/Local/Programs/Obsidian/Obsidian.com" read file="My Note"
```

…or (preferred) install the wrapper once so `obsidian …` works on PATH:

```bash
mkdir -p ~/.local/bin
printf '#!/usr/bin/env bash\nexec "/mnt/c/Users/Owner/AppData/Local/Programs/Obsidian/Obsidian.com" "$@"\n' > ~/.local/bin/obsidian
chmod +x ~/.local/bin/obsidian   # ensure ~/.local/bin is on your PATH
```

## Known quirks (this machine, verified 2026-06-15)

<!-- property:set is broken in this Obsidian/CLI build -->
- **`property:set` is broken — do not use it.** It returns exit 255 and silently
  changes nothing, for *any* property (not just `tags`). Read commands and
  `create`/`append`/`delete` work fine. To edit frontmatter, use `eval` with
  `app.fileManager.processFrontMatter`, which is Obsidian-native and reliable:
  ```bash
  # add a tag to one note (idempotent), via the Obsidian API:
  obsidian eval code='(async()=>{const f=app.vault.getAbstractFileByPath("path/to/Note.md"); await app.fileManager.processFrontMatter(f,(fm)=>{let t=fm.tags||[]; if(typeof t=="string")t=[t]; if(t.indexOf("paper-notes")<0)t.push("paper-notes"); fm.tags=t;}); return "done";})()'
  ```
  Loop the same pattern over `app.vault.getMarkdownFiles().filter(...)` to bulk-edit.

<!-- drvfs flush lag: Obsidian (Windows) write vs WSL disk view -->
- **Disk view lags Obsidian after a write (drvfs flush lag).** A CLI write updates
  Obsidian's in-memory state instantly, but the file on the `A:` drive can take a
  second or two to reflect it as seen from WSL. So immediately re-reading the file
  with a shell tool may show stale content while Obsidian's own view
  (e.g. `obsidian tag name=X total`, `obsidian read …`) is already correct.
  When verifying, trust the CLI view, or poll the filesystem until it converges.

<!-- obsidian.com no-ops when stdout is captured -->
- **`obsidian.com` silently no-ops when its stdout is captured.** Any
  `$(obsidian …)`, `obsidian … | pipe`, or `obsidian … >redirect` makes
  mutating commands (notably `rename`) return exit 0 *without doing anything*.
  Only **inherited stdout** (printed straight to the terminal) works, so batch
  loops that read `$(…)` output are unreliable. For bulk renames use
  `scripts/rename_note.py` (below) instead.

<!-- stale index after external/WSL moves -> ENOENT on rename -->
- **`obsidian rename` throws `ENOENT` on a stale index.** When files are
  moved/created from WSL (or any external tool), Obsidian's Windows watcher
  often misses it, so the live app doesn't know the file at its current path and
  `rename` fails. `obsidian reload` only re-indexes lazily. Fix the index with
  `scripts/touch_vault.py --refresh` (or `obsidian reload`), or sidestep it
  entirely with `scripts/rename_note.py`, which works on the files directly.

## Headless helpers — reliable rename + force-sync

Two bundled scripts in `scripts/` (next to this skill) do the things the live
CLI does unreliably here. They operate directly on the vault files, so they work
even when Obsidian is closed or its index is stale.

```bash
VAULT="/path/to/your/Obsidian Vault"              # this machine's vault root (see project-root .env: VAULT_ROOT)
SK="$HOME/.claude/skills/obsidian-cli/scripts"
```

### rename_note.py — rename / move with wikilink propagation
Prefer over `obsidian rename` for batch or scripted renames. It rewrites
`[[wikilinks]]` (stem, `#heading`, `|alias`, and path-based forms) across the
whole vault, then moves the file — no live app or index needed.

```bash
# RENAME a note + update [[Old]] / [[Old#h]] / [[Old|alias]] everywhere
python "$SK/rename_note.py" --vault "$VAULT" "Old Stem" "New Stem" --dry-run
# MOVE a note to another folder (updates path-based wikilinks)
python "$SK/rename_note.py" --vault "$VAULT" "Note Stem" --dest "PhD/Folder" --dry-run
# DIR rename a directory (updates path-based wikilinks)
python "$SK/rename_note.py" --vault "$VAULT" --dir "old/dir" "new/dir" --dry-run
```
Always `--dry-run` first to preview; drop it to apply. Then force-sync (below).

### touch_vault.py — make Obsidian notice WSL edits
After any filesystem write/rename, nudge Obsidian so its index doesn't go stale
(prevents the `ENOENT` quirk above). Equivalent to `obsidian reload` but doesn't
depend on the live app.

```bash
python "$SK/touch_vault.py" --vault "$VAULT" --recent 5 --refresh   # touch recent edits + re-scan
python "$SK/touch_vault.py" --vault "$VAULT" "PhD/x.md" --refresh    # touch one file + re-scan
```

## Command reference

Run `obsidian help` to see all available commands. This is always up to date. Full docs: https://help.obsidian.md/cli

## Syntax

**Parameters** take a value with `=`. Quote values with spaces:

```bash
obsidian create name="My Note" content="Hello world"
```

**Flags** are boolean switches with no value:

```bash
obsidian create name="My Note" silent overwrite
```

For multiline content use `\n` for newline and `\t` for tab.

## File targeting

Many commands accept `file` or `path` to target a file. Without either, the active file is used.

- `file=<name>` — resolves like a wikilink (name only, no path or extension needed)
- `path=<path>` — exact path from vault root, e.g. `folder/note.md`

## Vault targeting

Commands target the most recently focused vault by default. Use `vault=<name>` as the first parameter to target a specific vault:

```bash
obsidian vault="My Vault" search query="test"
```

## Common patterns

```bash
obsidian read file="My Note"
obsidian create name="New Note" content="# Hello" template="Template" silent
obsidian append file="My Note" content="New line"
obsidian search query="search term" limit=10
obsidian daily:read
obsidian daily:append content="- [ ] New task"
obsidian property:set name="status" value="done" file="My Note"
obsidian tasks daily todo
obsidian tags sort=count counts
obsidian backlinks file="My Note"
```

Use `--copy` on any command to copy output to clipboard. Use `silent` to prevent files from opening. Use `total` on list commands to get a count.

## Plugin development

### Develop/test cycle

After making code changes to a plugin or theme, follow this workflow:

1. **Reload** the plugin to pick up changes:
   ```bash
   obsidian plugin:reload id=my-plugin
   ```
2. **Check for errors** — if errors appear, fix and repeat from step 1:
   ```bash
   obsidian dev:errors
   ```
3. **Verify visually** with a screenshot or DOM inspection:
   ```bash
   obsidian dev:screenshot path=screenshot.png
   obsidian dev:dom selector=".workspace-leaf" text
   ```
4. **Check console output** for warnings or unexpected logs:
   ```bash
   obsidian dev:console level=error
   ```

### Additional developer commands

Run JavaScript in the app context:

```bash
obsidian eval code="app.vault.getFiles().length"
```

Inspect CSS values:

```bash
obsidian dev:css selector=".workspace-leaf" prop=background-color
```

Toggle mobile emulation:

```bash
obsidian dev:mobile on
```

Run `obsidian help` to see additional developer commands including CDP and debugger controls.
