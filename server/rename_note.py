"""
rename_note.py — Obsidian note renamer with wikilink update

Renames a markdown file and updates all wikilinks that reference it across the vault.

Usage:
    python rename_note.py "Old File Name" "New File Name"
    python rename_note.py "Old File Name" "New File Name" --vault /path/to/vault
    python rename_note.py "Old File Name" "New File Name" --dry-run

Wikilink formats handled:
    [[Old File Name]]                  -> [[New File Name]]
    [[Old File Name|Display Text]]     -> [[New File Name|Display Text]]
    [[Old File Name#Header]]           -> [[New File Name#Header]]
    [[Old File Name#Header|Display]]   -> [[New File Name#Header|Display]]

The file name must match exactly (case-sensitive). The .md extension is optional
in both the argument and the wikilink — both forms are handled.
"""

import argparse
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def strip_md(name: str) -> str:
    """Remove .md extension if present."""
    return name[:-3] if name.lower().endswith(".md") else name


def find_note(vault: Path, stem: str) -> Path | None:
    """Return the Path of the note whose stem matches exactly, or None."""
    matches = [p for p in vault.rglob("*.md") if p.stem == stem]
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        print(f"ERROR: Multiple files named '{stem}.md' found:")
        for m in matches:
            print(f"  {m.relative_to(vault)}")
        print("Rename aborted — resolve ambiguity first.")
        sys.exit(1)
    return None


def build_pattern(old_stem: str) -> re.Pattern:
    """
    Build a regex that matches the old stem inside [[ ]] wikilinks.

    Captures:
        group 1 — everything before the stem inside [[
        group 2 — the stem itself (exact match)
        group 3 — everything after the stem up to ]] (optional #header, |alias)
    """
    escaped = re.escape(old_stem)
    # The stem must be preceded by [[ or [[ ... | (for embedded aliases) —
    # actually Obsidian wikilinks always put the file name first, so the stem
    # sits immediately after [[ with optional path prefix (not used here).
    # Pattern: [[ <stem> <optional #header> <optional |alias> ]]
    pattern = (
        r"(\[\[)"           # opening [[
        r"(" + escaped + r")"  # exact stem
        r"((?:#[^\]|]*)?"   # optional #header (no ] or | chars)
        r"(?:\|[^\]]*)?)"   # optional |alias
        r"(\]\])"           # closing ]]
    )
    return re.compile(pattern)


def replace_in_content(content: str, old_stem: str, new_stem: str) -> tuple[str, int]:
    """
    Replace all wikilink references to old_stem with new_stem.
    Returns (updated_content, replacement_count).
    """
    pattern = build_pattern(old_stem)

    count = 0

    def replacer(m: re.Match) -> str:
        nonlocal count
        count += 1
        opening = m.group(1)   # [[
        after   = m.group(3)   # #header and/or |alias (may be empty)
        closing = m.group(4)   # ]]
        return f"{opening}{new_stem}{after}{closing}"

    updated = pattern.sub(replacer, content)
    return updated, count


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rename an Obsidian note and update all wikilinks referencing it."
    )
    parser.add_argument("old_name", help="Current file name (with or without .md)")
    parser.add_argument("new_name", help="New file name (with or without .md)")
    parser.add_argument(
        "--vault",
        default=".",
        help="Path to vault root (default: current directory)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing anything",
    )
    args = parser.parse_args()

    vault = Path(args.vault).resolve()
    old_stem = strip_md(args.old_name)
    new_stem = strip_md(args.new_name)

    if old_stem == new_stem:
        print("Old and new names are identical — nothing to do.")
        sys.exit(0)

    # ------------------------------------------------------------------
    # 1. Locate the source file
    # ------------------------------------------------------------------
    source = find_note(vault, old_stem)
    if source is None:
        print(f"ERROR: No file named '{old_stem}.md' found in vault at {vault}")
        sys.exit(1)

    # Guard: new name must not already exist
    new_path = source.with_name(f"{new_stem}.md")
    if new_path.exists():
        print(f"ERROR: A file named '{new_stem}.md' already exists at:")
        print(f"  {new_path.relative_to(vault)}")
        print("Rename aborted.")
        sys.exit(1)

    print(f"Renaming:  {source.relative_to(vault)}")
    print(f"       ->  {new_path.relative_to(vault)}")
    if args.dry_run:
        print("(dry run — no files will be modified)\n")

    # ------------------------------------------------------------------
    # 2. Scan all markdown files and update wikilinks
    # ------------------------------------------------------------------
    md_files = list(vault.rglob("*.md"))
    total_replacements = 0
    modified_files: list[tuple[Path, int]] = []

    for md_file in md_files:
        try:
            content = md_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            print(f"  WARN: Could not read {md_file.relative_to(vault)}: {e}")
            continue

        updated, count = replace_in_content(content, old_stem, new_stem)

        if count > 0:
            modified_files.append((md_file, count))
            total_replacements += count
            if not args.dry_run:
                md_file.write_text(updated, encoding="utf-8")

    # ------------------------------------------------------------------
    # 3. Rename the file itself
    # ------------------------------------------------------------------
    if not args.dry_run:
        source.rename(new_path)

    # ------------------------------------------------------------------
    # 4. Report
    # ------------------------------------------------------------------
    if modified_files:
        print(f"\nWikilinks updated in {len(modified_files)} file(s):")
        for path, count in sorted(modified_files, key=lambda x: x[0]):
            label = "  (the renamed file)" if path == source else ""
            print(f"  [{count}]  {path.relative_to(vault)}{label}")
        print(f"\nTotal replacements: {total_replacements}")
    else:
        print("\nNo wikilinks referencing this file were found.")

    if args.dry_run:
        print("\nDry run complete — no changes written.")
    else:
        print("\nDone.")


if __name__ == "__main__":
    main()
