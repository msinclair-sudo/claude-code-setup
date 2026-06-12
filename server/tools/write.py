"""
Write tools for the Obsidian Vault MCP Server.

Unrestricted writes: create/overwrite anywhere, append, and rename/move with
vault-wide wikilink propagation. No path, tag, or naming validation — tag
guidance lives in the vault_write docstring only.
"""

import sys
import subprocess
from pathlib import Path
from typing import Annotated, Optional

from fastmcp import FastMCP

from config import VAULT_ROOT


# ---------------------------------------------------------------------------
# Private helpers (inlined — helpers.py has been removed)
# ---------------------------------------------------------------------------

def _abs(rel: str) -> Path:
    """Resolve a vault-relative path to an absolute path."""
    return VAULT_ROOT / rel


def _resolve_existing(path: str) -> tuple[Optional[Path], Optional[str]]:
    """Resolve an existing note by vault-relative path or bare stem."""
    target = _abs(path)
    if target.exists():
        return target, None
    stem = Path(path).stem
    matches = list(VAULT_ROOT.rglob(f"{stem}.md"))
    if not matches:
        matches = list(VAULT_ROOT.rglob(Path(path).name))
    if len(matches) == 1:
        return matches[0], None
    if len(matches) > 1:
        paths_str = "\n".join(str(m.relative_to(VAULT_ROOT)) for m in matches)
        return None, f"Ambiguous: multiple files match '{path}':\n{paths_str}"
    return None, f"File not found: '{path}'"


def _touch(*files: Path) -> None:
    """
    Fire-and-forget call to touch_vault.py so Obsidian's Windows-side watcher
    detects edits made from WSL. Never raises — write tools must not fail here.
    """
    script = Path(__file__).parent.parent / "touch_vault.py"
    if not script.exists():
        return
    cmd = [sys.executable, str(script), "--vault", str(VAULT_ROOT)]
    cmd.extend(str(f) for f in files)
    cmd.append("--refresh")
    try:
        subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except OSError:
        pass


def register(mcp: FastMCP) -> None:

    @mcp.tool()
    def vault_write(
        path: Annotated[str, "Vault-relative path for the note, e.g. 'PhD/mtDNA/notes.md'. '.md' is appended if missing. Parent directories are created automatically. Overwrites if the file already exists."],
        content: Annotated[str, "Full file content. Strongly recommended: open with YAML frontmatter carrying at least one tag so the note is discoverable, e.g.\n---\ntags:\n  - MyTag\n---\n"],
    ) -> str:
        """
        Create or overwrite a note anywhere in the vault.
        Parent directories are created as needed. Writes content verbatim — no
        frontmatter, tags, or naming are enforced. Include a YAML `tags:` block so
        the note is findable via vault_search_tags.
        """
        if not path.endswith(".md"):
            path = f"{path}.md"
        target = _abs(path)
        existed = target.exists()

        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
        except OSError as e:
            return f"ERROR writing file: {e}"

        _touch(target)
        verb = "Overwrote" if existed else "Created"
        return f"{verb}: '{target.relative_to(VAULT_ROOT)}'"

    @mcp.tool()
    def vault_append(
        path: Annotated[str, "Vault-relative path or bare stem of an existing note, e.g. 'PhD/mtDNA/notes.md' or 'notes'."],
        content: Annotated[str, "Markdown text to append to the end of the note."],
    ) -> str:
        """
        Append text to the end of an existing note.
        Does not overwrite — all prior content (including frontmatter) is preserved.
        """
        target, err = _resolve_existing(path)
        if err:
            return f"ERROR: {err}"

        try:
            existing = target.read_text(encoding="utf-8", errors="replace")
            separator = "" if existing.endswith("\n") else "\n"
            target.write_text(existing + separator + content + "\n", encoding="utf-8")
        except OSError as e:
            return f"ERROR: {e}"

        _touch(target)
        return f"Appended to '{target.relative_to(VAULT_ROOT)}'."

    @mcp.tool()
    def vault_rename(
        name_a: Annotated[str, "RENAME/MOVE: current file stem (no .md), e.g. 'old_note'. DIR mode: the old directory path (vault-relative)."],
        name_b: Annotated[str, "RENAME: new file stem (no .md). DIR mode: the new directory path. Leave empty for MOVE mode."] = "",
        dest: Annotated[str, "MOVE mode only: destination directory (vault-relative) to move the file into, keeping its name. Leave empty otherwise."] = "",
        is_dir: Annotated[bool, "DIR mode: rename a directory (name_a = old dir path, name_b = new dir path)."] = False,
        dry_run: Annotated[bool, "Preview all changes without writing anything."] = False,
    ) -> str:
        """
        Rename or move a note (or directory) and propagate every wikilink across the
        whole vault. Delegates to the vault's own scripts/rename_note.py, which
        supports three modes:
          RENAME — name_a (old stem) + name_b (new stem)
          MOVE   — name_a (file) + dest (target directory)
          DIR    — is_dir=True, name_a (old dir) + name_b (new dir)
        Always run with dry_run=True first to preview the link edits.
        """
        script = VAULT_ROOT / "scripts" / "rename_note.py"
        if not script.exists():
            return (
                f"ERROR: vault-side rename script not found at "
                f"'{script.relative_to(VAULT_ROOT)}'. Cannot rename."
            )

        cmd = [sys.executable, str(script)]
        if is_dir:
            if not name_b:
                return "ERROR: DIR mode requires both name_a (old dir) and name_b (new dir)."
            cmd += [name_a, name_b, "--dir"]
        elif dest:
            cmd += [name_a, "--dest", dest]
        else:
            if not name_b:
                return "ERROR: RENAME mode requires name_b (new stem). For MOVE pass dest=, for DIR pass is_dir=True."
            cmd += [name_a, name_b]
        cmd += ["--vault", str(VAULT_ROOT)]
        if dry_run:
            cmd.append("--dry-run")

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        except subprocess.TimeoutExpired:
            return "ERROR: rename_note.py timed out after 60 seconds."
        except OSError as e:
            return f"ERROR running rename_note.py: {e}"

        output = result.stdout + result.stderr
        if result.returncode != 0:
            return f"ERROR (exit {result.returncode}):\n{output}"
        if not dry_run:
            _touch()
        return output or "Rename completed."
