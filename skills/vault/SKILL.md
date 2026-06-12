---
name: vault
description: Read from and write to the Obsidian vault via the obsidian-vault MCP. Use for /vault or any vault operation — searching notes, reading/listing, creating or overwriting, appending, editing, importing a local file, renaming/moving with wikilink propagation, staging dumps for later integration, and reading or updating project trackers.
---

# vault

Thin bridge to the Obsidian vault. Reads are unrestricted; writes are **unguarded** — `vault_write` creates or overwrites any `.md` anywhere, verbatim. The tags and conventions below are guidance, not enforced by the tools.

## Tools
Read: `vault_search(query, tag, path_prefix)` · `vault_search_tags(must_have, any_of, exclude, path_prefix)` · `vault_read(path)` · `vault_list(directory, all_files)` · `vault_wikilinks(path)` · `vault_recent(n, tag)`
Write: `vault_write(path, content)` · `vault_append(path, content)` · `vault_rename(name_a, name_b, dest, is_dir, dry_run)`
Bare stems fuzzy-resolve (read/append/wikilinks); pass a full vault-relative path when ambiguous.

## Everyday operations
- **Search** — text via `vault_search`; boolean tags via `vault_search_tags`; recent work via `vault_recent`. Scope either search with `path_prefix`.
- **Read / browse** — `vault_read`, `vault_list`; `vault_wikilinks` shows a note's outward + inbound links.
- **Create / overwrite** — build the full file (frontmatter + body) and `vault_write`. Put tags in frontmatter so the note is findable. A substantive new note opens with a `> [!abstract] Note Role` callout — fields in order: **Contains, Cannot contain, Points to, Pointed to by** (title always exactly `Note Role`).
- **Edit** — no string-replace tool: `vault_read`, change the text, `vault_write` the whole file back, preserving everything you aren't changing (frontmatter included). For large/mostly-intact notes the host `Edit` tool on `<VAULT_ROOT>/<path>` is a safer surgical option.
- **Append** — `vault_append`.
- **Import a local file** — copy with the host shell (`cp "/abs/src.md" "<VAULT_ROOT>/<dest>.md"`); add frontmatter afterward with `vault_write` if needed. `cp -r` a directory to keep relative links intact.
- **Rename / move** — `vault_rename`: rename (`name_a`,`name_b`), move (`name_a`,`dest`), or directory (`name_a`,`name_b`,`is_dir=True`). Always `dry_run=True` first, show the preview, then commit.

## Dumps — stage now, integrate later
Stage content that spans several notes or isn't ready to place: `vault_write` to `PhD/<project>/claude_doc_dump/<name>.md` with frontmatter tags including **`doc_dump`**, a `destinations:` list of target `[[wikilinks]]`, and `updated:`. Verify target stems first with `vault_search`/`vault_wikilinks` — don't infer them.

**Integrate** (find → understand → weave): `vault_search_tags(must_have=["doc_dump"])` lists dumps; process oldest `**Created:**` first (later wins on conflict). For each — read it, read its destinations plus their linked/related notes, weave content in by topic (not blind append), update or remove superseded content, set `updated:` on every touched note, then delete the dump file (`rm`). Substantive changes to notes beyond the declared destinations: confirm first.

## Trackers
Notes tagged `Tracker` at `PhD/<project>/*_Tracker.md`, holding typed callouts (`> [!data-pull|task|decision|blocker]` with `> **status**:`, `> **detail**:`, optional `source`/`target`/`blocks`) under `## Data Pulls / Tasks / Decisions / Blockers` and `## Completed`.
- **Read** — `vault_search_tags(must_have=["Tracker"])` to locate (project = parent dir); `vault_read` and parse the callouts; present grouped by type, filtered by status.
- **Add item** — read → confirm the title is unique → insert a formatted callout under the right section header → `vault_write`.
- **Update status** — read → change that item's `> **status**:` line (match by exact title); on `complete`, move it to `## Completed` as `- [x] <title> (<date>)` → `vault_write`.

## Notes
- For manuscript prose, use `/write-science` (full paragraphs, IMRAD, journal citation style).
- `vault_write` overwrites the whole file — when editing notes or trackers, preserve all content you aren't deliberately changing.
