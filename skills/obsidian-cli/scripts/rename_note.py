"""
rename_note.py — Obsidian note renamer and mover with wikilink update

Three modes of operation:

  1. RENAME — rename a file, update stem-based wikilinks:
         python rename_note.py "Old Name" "New Name"

  2. MOVE — move a file to a new directory, update any path-based wikilinks:
         python rename_note.py "File Name" --dest "path/to/new/dir"

  3. DIR — rename a directory, update path-based wikilinks containing old dir name:
         python rename_note.py --dir "old/dir/path" "new/dir/path"

All modes accept:
    --vault /path/to/vault   (default: current directory)
    --dry-run                preview changes without writing anything

Wikilink formats handled (rename mode):
    [[Old Name]]                 ->  [[New Name]]
    [[Old Name|Display Text]]    ->  [[New Name|Display Text]]
    [[Old Name#Header]]          ->  [[New Name#Header]]
    [[Old Name#Header|Display]]  ->  [[New Name#Header|Display]]

Path-based wikilinks handled (move / dir modes):
    [[some/path/Old Dir/file]]   ->  [[some/path/New Dir/file]]
    [[Old Dir/file|alias]]       ->  [[New Dir/file|alias]]
"""

import argparse
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Shared helpers
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
        print("Aborted — resolve ambiguity first.")
        sys.exit(1)
    return None


def scan_and_update(vault: Path, pattern: re.Pattern, replace_fn, dry_run: bool) -> tuple[list, int]:
    """
    Walk every .md file in the vault, apply replace_fn to matches of pattern.
    Returns (list of (path, count) for modified files, total replacement count).
    """
    modified = []
    total = 0
    for md_file in sorted(vault.rglob("*.md")):
        try:
            content = md_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            print(f"  WARN: Could not read {md_file.relative_to(vault)}: {e}")
            continue
        updated, count = _replace_all(content, pattern, replace_fn)
        if count > 0:
            modified.append((md_file, count))
            total += count
            if not dry_run:
                md_file.write_text(updated, encoding="utf-8")
    return modified, total


def _replace_all(content: str, pattern: re.Pattern, replace_fn) -> tuple[str, int]:
    count = 0
    def counter_replace(m):
        nonlocal count
        count += 1
        return replace_fn(m)
    updated = pattern.sub(counter_replace, content)
    return updated, count


def report(modified: list, total: int, vault: Path, dry_run: bool) -> None:
    if modified:
        print(f"\nWikilinks updated in {len(modified)} file(s):")
        for path, count in modified:
            print(f"  [{count}]  {path.relative_to(vault)}")
        print(f"\nTotal replacements: {total}")
    else:
        print("\nNo wikilinks referencing this were found.")
    if dry_run:
        print("\nDry run complete — no changes written.")
    else:
        print("\nDone.")


# ---------------------------------------------------------------------------
# Mode 1: RENAME  (stem → stem, update [[stem]] wikilinks)
# ---------------------------------------------------------------------------

def build_stem_pattern(old_stem: str) -> re.Pattern:
    """
    Match [[old_stem]], [[old_stem|alias]], [[old_stem#header]], etc.
    Does NOT match if old_stem appears as a path segment (has / before it).
    """
    escaped = re.escape(old_stem)
    pattern = (
        r"(\[\[)"
        r"(" + escaped + r")"
        r"((?:#[^\]|]*)?"
        r"(?:\|[^\]]*)?)"
        r"(\]\])"
    )
    return re.compile(pattern)


def do_rename(vault: Path, old_stem: str, new_stem: str, dry_run: bool) -> None:
    source = find_note(vault, old_stem)
    if source is None:
        print(f"ERROR: No file named '{old_stem}.md' found in vault at {vault}")
        sys.exit(1)

    new_path = source.with_name(f"{new_stem}.md")
    if new_path.exists():
        print(f"ERROR: '{new_stem}.md' already exists at {new_path.relative_to(vault)}")
        sys.exit(1)

    print(f"Renaming:  {source.relative_to(vault)}")
    print(f"       ->  {new_path.relative_to(vault)}")
    if dry_run:
        print("(dry run — no files will be modified)\n")

    pattern = build_stem_pattern(old_stem)

    def replace_fn(m: re.Match) -> str:
        return f"{m.group(1)}{new_stem}{m.group(3)}{m.group(4)}"

    modified, total = scan_and_update(vault, pattern, replace_fn, dry_run)

    if not dry_run:
        source.rename(new_path)

    report(modified, total, vault, dry_run)


# ---------------------------------------------------------------------------
# Mode 2: MOVE  (file → new directory, update path-based wikilinks)
# ---------------------------------------------------------------------------

def do_move(vault: Path, stem: str, dest_dir: Path, dry_run: bool) -> None:
    source = find_note(vault, stem)
    if source is None:
        print(f"ERROR: No file named '{stem}.md' found in vault at {vault}")
        sys.exit(1)

    if not dest_dir.is_absolute():
        dest_dir = vault / dest_dir

    dest_dir.mkdir(parents=True, exist_ok=True)
    new_path = dest_dir / source.name

    if new_path.resolve() == source.resolve():
        print("Source and destination are the same — nothing to do.")
        sys.exit(0)

    if new_path.exists():
        print(f"ERROR: '{source.name}' already exists at {new_path.relative_to(vault)}")
        sys.exit(1)

    # Build the old vault-relative path fragment for wikilink matching
    old_rel = source.relative_to(vault)          # e.g. PhD/Literature Review/Methodology_Notes/Pipeline_Overview.md
    old_dir_fragment = str(old_rel.parent)        # e.g. PhD/Literature Review/Methodology_Notes
    new_rel_dir = str(dest_dir.relative_to(vault))  # e.g. PhD/Literature Review

    print(f"Moving:  {old_rel}")
    print(f"     ->  {new_path.relative_to(vault)}")
    if dry_run:
        print("(dry run — no files will be modified)\n")

    # Scan for path-based wikilinks containing the old directory path + stem
    old_wikilink_path = f"{old_dir_fragment}/{stem}".replace("\\", "/")
    new_wikilink_path = f"{new_rel_dir}/{stem}".replace("\\", "/")

    # Also handle just old_dir_name/stem in case relative paths are used
    old_dir_name = Path(old_dir_fragment).name   # e.g. Methodology_Notes
    old_short = f"{old_dir_name}/{stem}"
    new_dir_name = dest_dir.name if dest_dir != vault else ""
    new_short = f"{new_dir_name}/{stem}" if new_dir_name else stem

    modified = []
    total = 0

    for md_file in sorted(vault.rglob("*.md")):
        try:
            content = md_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            print(f"  WARN: Could not read {md_file.relative_to(vault)}: {e}")
            continue

        updated = content
        count = 0

        # Replace full path variant
        full_pat = re.compile(
            r"(\[\[)" + re.escape(old_wikilink_path) + r"((?:#[^\]|]*)?(?:\|[^\]]*)?)(\]\])"
        )
        updated, n = _replace_all(updated, full_pat,
            lambda m: f"{m.group(1)}{new_wikilink_path}{m.group(2)}{m.group(3)}")
        count += n

        # Replace short path variant (dir_name/stem)
        if old_short != new_short:
            short_pat = re.compile(
                r"(\[\[)" + re.escape(old_short) + r"((?:#[^\]|]*)?(?:\|[^\]]*)?)(\]\])"
            )
            updated, n = _replace_all(updated, short_pat,
                lambda m: f"{m.group(1)}{new_short}{m.group(2)}{m.group(3)}")
            count += n

        if count > 0:
            modified.append((md_file, count))
            total += count
            if not dry_run:
                md_file.write_text(updated, encoding="utf-8")

    if not dry_run:
        source.rename(new_path)

    # Stem-based links ([[Pipeline_Overview]]) are unaffected — Obsidian resolves by stem
    print("Note: stem-based wikilinks ([[Pipeline_Overview]]) resolve by filename search — no update needed.")
    report(modified, total, vault, dry_run)


# ---------------------------------------------------------------------------
# Mode 3: DIR  (rename a directory, update path-based wikilinks)
# ---------------------------------------------------------------------------

def do_dir(vault: Path, old_dir: Path, new_dir: Path, dry_run: bool) -> None:
    if not old_dir.is_absolute():
        old_dir = vault / old_dir
    if not new_dir.is_absolute():
        new_dir = vault / new_dir

    if not old_dir.exists():
        print(f"ERROR: Directory not found: {old_dir}")
        sys.exit(1)

    if not old_dir.is_dir():
        print(f"ERROR: Not a directory: {old_dir}")
        sys.exit(1)

    if new_dir.exists():
        print(f"ERROR: Destination already exists: {new_dir}")
        sys.exit(1)

    old_rel = str(old_dir.relative_to(vault)).replace("\\", "/")  # e.g. PhD/Literature Review/Sections
    new_rel = str(new_dir.relative_to(vault)).replace("\\", "/")  # e.g. PhD/Literature Review/Writing Sections

    old_name = old_dir.name   # e.g. Sections
    new_name = new_dir.name   # e.g. Writing Sections

    print(f"Renaming directory:  {old_rel}/")
    print(f"                 ->  {new_rel}/")
    if dry_run:
        print("(dry run — no files will be modified)\n")

    modified = []
    total = 0

    for md_file in sorted(vault.rglob("*.md")):
        try:
            content = md_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            print(f"  WARN: Could not read {md_file.relative_to(vault)}: {e}")
            continue

        updated = content
        count = 0

        # Match full vault-relative path fragment in wikilinks: [[.../Sections/...]]
        full_pat = re.compile(
            r"(\[\[[^\]]*?)" + re.escape(old_rel) + r"(/[^\]]*?\]\])"
        )
        updated, n = _replace_all(updated, full_pat,
            lambda m: f"{m.group(1)}{new_rel}{m.group(2)}")
        count += n

        # Match just the dir name as path segment: [[Sections/filename]] or [[Sections/filename|alias]]
        short_pat = re.compile(
            r"(\[\[)" + re.escape(old_name) + r"(/" + r"[^\]]*?" + r"\]\])"
        )
        updated, n = _replace_all(updated, short_pat,
            lambda m: f"{m.group(1)}{new_name}{m.group(2)}")
        count += n

        if count > 0:
            modified.append((md_file, count))
            total += count
            if not dry_run:
                md_file.write_text(updated, encoding="utf-8")

    if not dry_run:
        old_dir.rename(new_dir)

    report(modified, total, vault, dry_run)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rename or move Obsidian notes/directories while preserving wikilinks.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Modes:
  RENAME:  rename_note.py "Old Name" "New Name"
  MOVE:    rename_note.py "File Name" --dest "path/to/new/dir"
  DIR:     rename_note.py --dir "old/dir/path" "new/dir/path"
        """
    )
    parser.add_argument("name_a", nargs="?", help="Old file name (rename/move) or old dir path (--dir)")
    parser.add_argument("name_b", nargs="?", help="New file name (rename) or new dir path (--dir)")
    parser.add_argument("--dest", metavar="DIR", help="[MOVE mode] Destination directory for the file")
    parser.add_argument("--dir", action="store_true", help="[DIR mode] Rename a directory")
    parser.add_argument("--vault", default=".", help="Path to vault root (default: current directory)")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing anything")
    args = parser.parse_args()

    vault = Path(args.vault).resolve()

    # ---- DIR mode ----------------------------------------------------------
    if args.dir:
        if not args.name_a or not args.name_b:
            print("ERROR: --dir requires two arguments: old directory path and new directory path")
            sys.exit(1)
        do_dir(vault, Path(args.name_a), Path(args.name_b), args.dry_run)
        return

    # ---- MOVE mode ---------------------------------------------------------
    if args.dest:
        if not args.name_a:
            print("ERROR: --dest requires a file name argument")
            sys.exit(1)
        stem = strip_md(args.name_a)
        do_move(vault, stem, Path(args.dest), args.dry_run)
        return

    # ---- RENAME mode -------------------------------------------------------
    if not args.name_a or not args.name_b:
        parser.print_help()
        sys.exit(1)

    old_stem = strip_md(args.name_a)
    new_stem = strip_md(args.name_b)

    if old_stem == new_stem:
        print("Old and new names are identical — nothing to do.")
        sys.exit(0)

    do_rename(vault, old_stem, new_stem, args.dry_run)


if __name__ == "__main__":
    main()
