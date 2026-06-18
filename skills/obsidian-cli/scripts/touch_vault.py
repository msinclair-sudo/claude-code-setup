#!/usr/bin/env python3
"""
Force Obsidian to detect external edits made from WSL.

Re-touches modified files to update their mtime and optionally nudges
.obsidian/workspace.json to trigger a vault-wide re-scan.
"""

import argparse
import os
import sys
import time
from pathlib import Path

SKIP_DIRS = {".obsidian", ".git", ".claude", ".trash"}


def touch(path: Path, dry_run: bool = False) -> str:
    """Touch a file to update its mtime. Returns a status line."""
    if not path.exists():
        return f"SKIP (not found): {path}"
    if dry_run:
        return f"WOULD TOUCH: {path}"
    os.utime(path, None)
    return f"TOUCHED: {path}"


def find_recent(vault: Path, minutes: int) -> list[Path]:
    """Find .md files modified within the last N minutes, skipping dotfile dirs."""
    cutoff = time.time() - (minutes * 60)
    results = []
    for md in vault.rglob("*.md"):
        # Skip dotfile directories
        if any(part in SKIP_DIRS for part in md.relative_to(vault).parts):
            continue
        try:
            if md.stat().st_mtime >= cutoff:
                results.append(md)
        except OSError:
            continue
    return sorted(results)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Force Obsidian to detect external edits by re-touching files."
    )
    parser.add_argument(
        "files", nargs="*",
        help="Specific file paths to touch (relative to vault root or absolute).",
    )
    parser.add_argument(
        "--recent", type=int, metavar="N",
        help="Touch all .md files modified within the last N minutes.",
    )
    parser.add_argument(
        "--refresh", action="store_true",
        help="Touch .obsidian/workspace.json to trigger a vault-wide re-scan.",
    )
    parser.add_argument(
        "--vault", type=str, default=".",
        help="Vault root path (default: current working directory).",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print what would be touched without modifying anything.",
    )
    args = parser.parse_args()

    if not args.files and args.recent is None and not args.refresh:
        parser.print_help()
        return 1

    vault = Path(args.vault).resolve()
    touched = []

    # Touch specific files
    for f in args.files:
        p = Path(f)
        if not p.is_absolute():
            p = vault / p
        touched.append(touch(p, args.dry_run))

    # Touch recently modified files
    if args.recent is not None:
        recent = find_recent(vault, args.recent)
        for p in recent:
            touched.append(touch(p, args.dry_run))

    # Refresh workspace.json
    if args.refresh:
        ws = vault / ".obsidian" / "workspace.json"
        touched.append(touch(ws, args.dry_run))

    for line in touched:
        print(line)

    return 0


if __name__ == "__main__":
    sys.exit(main())
