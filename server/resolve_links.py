"""
resolve_links.py — Markdown internal link resolver

Scans markdown files for broken relative links, attempts to resolve them
against real files in the same directory tree, and either fixes them in-place
or converts unresolvable links to comments.

Usage:
    python resolve_links.py <file_or_dir> [--dry-run] [--verbose]

    <file_or_dir>  A single .md file or a directory to scan recursively.
    --dry-run      Print proposed changes without writing anything.
    --verbose      Show all links including those that are already valid.

Output:
    - Resolved links are rewritten in-place.
    - Unresolvable links are converted to HTML comments:
        [text](broken.md)  →  <!-- UNRESOLVED LINK: [text](broken.md) -->
    - A summary report is printed to stdout.

Exit codes:
    0  All links resolved or already valid.
    1  One or more unresolvable links remain (converted to comments).
"""

import argparse
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Link extraction
# ---------------------------------------------------------------------------

# Matches [text](target) — captures text and target separately.
# Skips http/https URLs and mailto: links.
LINK_RE = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "#"))


def extract_links(content: str) -> list[tuple[str, str, int]]:
    """
    Return list of (full_match, target, line_number) for all internal links.
    Skips lines that are HTML comments to avoid re-processing previously
    unresolved links that were already converted to <!-- UNRESOLVED LINK: --> comments.
    """
    results = []
    for lineno, line in enumerate(content.splitlines(), start=1):
        if line.strip().startswith("<!--"):
            continue
        for m in LINK_RE.finditer(line):
            target = m.group(2).split("#")[0]  # strip anchors
            if target and not is_external(target):
                results.append((m.group(0), target, lineno))
    return results


# ---------------------------------------------------------------------------
# Resolution
# ---------------------------------------------------------------------------

def build_file_index(root: Path) -> dict[str, list[Path]]:
    """
    Index all .md files under root by multiple keys:
      - exact stem          (e.g. '18-gap_queries')
      - exact filename      (e.g. '18-gap_queries.md')
      - normalised stem     (underscores→hyphens, digit+letter→digit-letter)
    """
    index: dict[str, list[Path]] = {}
    for p in root.rglob("*.md"):
        keys = {p.stem, p.name, normalise_stem(p.stem)}
        for key in keys:
            index.setdefault(key, []).append(p)
    return index


def normalise_stem(stem: str) -> str:
    """
    Normalise a stem for fuzzy matching.
    Converts underscores to hyphens, and also handles the pattern
    where a numeric prefix is joined directly to a letter suffix:
      04a_phase1  →  04-a-phase1
      04b_foo     →  04-b-foo
    """
    s = stem.replace("_", "-")
    # Insert hyphen between digit(s) and an immediately following letter: 04a → 04-a
    s = re.sub(r'(\d)([a-zA-Z])', r'\1-\2', s)
    return s


def resolve_target(target: str, source_file: Path, index: dict[str, list[Path]]) -> Path | None:
    """
    Try to find the real file for a relative link target.
    Resolution order:
      1. Exact relative path from source file's directory
      2. Exact filename match in index
      3. Exact stem match in index
      4. Normalised stem (underscores → hyphens) match in index
    Returns the matched Path, or None if unresolvable.
    """
    source_dir = source_file.parent
    target_path = Path(target)
    stem = target_path.stem
    name = target_path.name

    # 1. Direct relative path
    candidate = (source_dir / target_path).resolve()
    if candidate.exists():
        return candidate

    # 2. Exact filename in index
    if name in index and len(index[name]) == 1:
        return index[name][0]

    # 3. Exact stem in index
    if stem in index and len(index[stem]) == 1:
        return index[stem][0]

    # 4. Normalised stem (underscore → hyphen)
    norm = normalise_stem(stem)
    if norm in index and len(index[norm]) == 1:
        return index[norm][0]

    # 5. Ambiguous — more than one match, can't resolve safely
    return None


# ---------------------------------------------------------------------------
# Rewriting
# ---------------------------------------------------------------------------

def relative_link(from_file: Path, to_file: Path) -> str:
    """Compute the relative path from from_file's directory to to_file."""
    try:
        return str(to_file.relative_to(from_file.parent))
    except ValueError:
        # Files not under a common parent — use a longer relative path
        parts_from = from_file.parent.parts
        parts_to = to_file.parts
        # Find common prefix length
        common = 0
        for a, b in zip(parts_from, parts_to):
            if a == b:
                common += 1
            else:
                break
        ups = len(parts_from) - common
        rel = "../" * ups + "/".join(parts_to[common:])
        return rel


def process_file(
    md_file: Path,
    index: dict[str, list[Path]],
    dry_run: bool,
    verbose: bool,
) -> tuple[int, int, int]:
    """
    Process a single markdown file.
    Returns (resolved_count, unresolved_count, already_valid_count).
    """
    content = md_file.read_text(encoding="utf-8", errors="replace")
    links = extract_links(content)

    if not links:
        return 0, 0, 0

    resolved = 0
    unresolved = 0
    already_valid = 0
    new_content = content

    for full_match, target, lineno in links:
        # Check if already valid
        candidate = (md_file.parent / Path(target)).resolve()
        if candidate.exists():
            if verbose:
                print(f"  OK       line {lineno:4d}: {target}")
            already_valid += 1
            continue

        real_path = resolve_target(target, md_file, index)

        if real_path is not None:
            new_target = relative_link(md_file, real_path)
            # Preserve anchor if present
            if "#" in full_match.split("](")[1]:
                anchor = "#" + full_match.split("#", 1)[1].rstrip(")")
                new_target += anchor
            # Rebuild the link with the same display text
            text = re.match(r'\[([^\]]*)\]', full_match).group(1)
            new_link = f"[{text}]({new_target})"
            new_content = new_content.replace(full_match, new_link, 1)
            print(f"  RESOLVED line {lineno:4d}: {target!r} → {new_target!r}  ({md_file.name})")
            resolved += 1
        else:
            # Convert to comment
            comment = f"<!-- UNRESOLVED LINK: {full_match} -->"
            new_content = new_content.replace(full_match, comment, 1)
            print(f"  BROKEN   line {lineno:4d}: {target!r} — could not resolve  ({md_file.name})")
            unresolved += 1

    if not dry_run and new_content != content:
        md_file.write_text(new_content, encoding="utf-8")

    return resolved, unresolved, already_valid


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Resolve broken internal markdown links."
    )
    parser.add_argument("target", help="A .md file or directory to scan recursively.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing.")
    parser.add_argument("--verbose", action="store_true", help="Show already-valid links too.")
    args = parser.parse_args()

    target = Path(args.target).resolve()

    if target.is_file():
        root = target.parent
        files = [target]
    elif target.is_dir():
        root = target
        files = list(target.rglob("*.md"))
    else:
        print(f"ERROR: '{args.target}' is not a file or directory.", file=sys.stderr)
        sys.exit(2)

    if not files:
        print("No markdown files found.")
        return

    print(f"Scanning {len(files)} file(s) under '{root}'")
    if args.dry_run:
        print("(dry run — no files will be modified)\n")
    else:
        print()

    index = build_file_index(root)

    total_resolved = 0
    total_unresolved = 0
    total_valid = 0

    for md_file in sorted(files):
        r, u, v = process_file(md_file, index, args.dry_run, args.verbose)
        total_resolved += r
        total_unresolved += u
        total_valid += v

    print(f"\n── Summary ──────────────────────────────")
    print(f"  Already valid : {total_valid}")
    print(f"  Resolved      : {total_resolved}")
    print(f"  Unresolved    : {total_unresolved}")
    if args.dry_run:
        print("  (no files written — dry run)")

    if total_unresolved > 0:
        print("\nUnresolved links have been converted to HTML comments.")
        print("Search for '<!-- UNRESOLVED LINK:' to find them.")
        sys.exit(1)


if __name__ == "__main__":
    main()
