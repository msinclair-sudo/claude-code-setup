"""
Read tools for the Obsidian Vault MCP Server.

General-purpose, unrestricted reads: full-text search, boolean tag search,
note reading, directory listing, wikilink graph inspection, and recency.
"""

import re
from datetime import date
from pathlib import Path
from typing import Annotated, Optional

from fastmcp import FastMCP

from config import VAULT_ROOT


# ---------------------------------------------------------------------------
# Private helpers (inlined — helpers.py has been removed)
# ---------------------------------------------------------------------------

_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
_WIKILINK_RE = re.compile(r"\[\[([^\]\n]+?)\]\]")


def _abs(rel: str) -> Path:
    """Resolve a vault-relative path to an absolute path."""
    return VAULT_ROOT / rel


def _frontmatter(content: str) -> str:
    """Return the YAML frontmatter block (between the leading --- fences), or ''."""
    m = _FM_RE.match(content)
    return m.group(1) if m else ""


def _clean_tag(s: str) -> str:
    return s.strip().strip('"').strip("'").lstrip("#").strip()


def _extract_tags(content: str) -> list[str]:
    """
    Extract tags from YAML frontmatter, scoped to the `tags:` key only.
    Handles list form (- Foo), inline form (tags: [A, B] / tags: A B), and
    a single scalar (tags: Foo). Other YAML lists (e.g. destinations:) are
    NOT treated as tags.
    """
    fm = _frontmatter(content)
    if not fm:
        return []

    lines = fm.splitlines()
    tags: list[str] = []
    for i, line in enumerate(lines):
        m = re.match(r"^tags:\s*(.*)$", line)
        if not m:
            continue
        inline = m.group(1).strip()
        if inline:
            inline = inline.strip("[]")
            parts = re.split(r"[,\s]+", inline)
            tags.extend(_clean_tag(p) for p in parts if p.strip())
        else:
            # Block list form on the following indented lines.
            for nxt in lines[i + 1:]:
                lm = re.match(r"^\s*-\s+(.*)$", nxt)
                if lm:
                    t = _clean_tag(lm.group(1))
                    if t:
                        tags.append(t)
                elif nxt.strip() == "":
                    continue
                else:
                    break  # a new top-level key — end of the tags block
        break  # only the first tags: key

    return [t for t in tags if t]


def _iter_md(path_prefix: str = ""):
    """Yield (md_file, rel_str) for every .md file, optionally scoped to a prefix."""
    for md_file in VAULT_ROOT.rglob("*.md"):
        rel = str(md_file.relative_to(VAULT_ROOT))
        if path_prefix and not rel.startswith(path_prefix):
            continue
        yield md_file, rel


def _fuzzy_resolve(path: str) -> tuple[Optional[Path], Optional[str]]:
    """
    Resolve a vault-relative path or bare stem to a concrete file.
    Returns (Path, None) on success, or (None, error_message) on failure.
    """
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
        return None, (
            f"Ambiguous: multiple files match '{path}':\n{paths_str}\n"
            "Please provide the full relative path."
        )
    return None, f"File not found: '{path}'"


def _link_target_stem(raw: str) -> str:
    """From a wikilink inner string 'folder/Name#Heading|Alias' return 'Name'."""
    target = raw.split("|", 1)[0].split("#", 1)[0].strip()
    if "/" in target:
        target = target.rsplit("/", 1)[1]
    return target.strip()


def register(mcp: FastMCP) -> None:

    @mcp.tool()
    def vault_search(
        query: Annotated[str, "Space-separated search terms (case-insensitive). A file matches if it contains ALL terms anywhere in its content. Pass empty string to search by tag only."],
        tag: Annotated[str, "Filter results to notes carrying this frontmatter tag (exact match, case-sensitive). Optional."] = "",
        path_prefix: Annotated[str, "Restrict the search to notes whose vault-relative path starts with this prefix, e.g. 'PhD/mtDNA'. Optional."] = "",
    ) -> str:
        """
        Full-text AND search across the vault.
        Query is split into terms; a file matches if it contains every term.
        Returns FILE path, TAGS, and an EXCERPT (first line containing a term).
        """
        results = []
        terms = query.lower().split() if query.strip() else []

        for md_file, rel in _iter_md(path_prefix):
            try:
                content = md_file.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue

            file_tags = _extract_tags(content)
            if tag and tag not in file_tags:
                continue

            if terms:
                content_lower = content.lower()
                if not all(term in content_lower for term in terms):
                    continue
                excerpt_line = next(
                    (ln for ln in content.splitlines() if any(t in ln.lower() for t in terms)),
                    "",
                )
                excerpt = excerpt_line.strip()[:200]
            else:
                excerpt = content[:200].replace("\n", " ")

            results.append(
                f"FILE: {rel}\n"
                f"TAGS: {', '.join(file_tags) if file_tags else '(none)'}\n"
                f"EXCERPT: {excerpt}"
            )

        if not results:
            return f"No results found for query='{query}' tag='{tag}' path_prefix='{path_prefix}'."
        return "\n\n".join(results)

    @mcp.tool()
    def vault_search_tags(
        must_have: Annotated[list[str], "AND — every tag listed must be present on the note."],
        any_of: Annotated[list[str], "OR — at least one of these tags must be present (ignored if empty)."] = [],
        exclude: Annotated[list[str], "NOT — a note is dropped if it carries any of these tags."] = [],
        path_prefix: Annotated[str, "Restrict to notes whose vault-relative path starts with this prefix. Optional."] = "",
    ) -> str:
        """
        Boolean search over YAML-frontmatter tags.
        Only the `tags:` frontmatter key is consulted (list, inline, or scalar form).
        Example: must_have=['PhD'], any_of=['Methods','Code'], exclude=['doc_dump'].
        """
        results = []
        for md_file, rel in _iter_md(path_prefix):
            try:
                content = md_file.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue

            tags = _extract_tags(content)
            if not tags:
                continue
            tagset = set(tags)

            if must_have and not all(t in tagset for t in must_have):
                continue
            if any_of and not any(t in tagset for t in any_of):
                continue
            if exclude and any(t in tagset for t in exclude):
                continue

            results.append(f"FILE: {rel}\nTAGS: {', '.join(tags)}")

        if not results:
            return (
                f"No notes match must_have={must_have} any_of={any_of} "
                f"exclude={exclude} path_prefix='{path_prefix}'."
            )
        return f"{len(results)} note(s):\n\n" + "\n\n".join(results)

    @mcp.tool()
    def vault_read(
        path: Annotated[str, "Vault-relative path (e.g. 'PhD/mtDNA/01-Introduction.md') or a bare filename stem (e.g. '01-Introduction'). Searched recursively if no directory is given."],
    ) -> str:
        """
        Read a note's full content including frontmatter.
        If multiple files share the same stem, the full relative path is required.
        """
        target, err = _fuzzy_resolve(path)
        if err:
            return err
        try:
            return target.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            return f"Error reading file: {e}"

    @mcp.tool()
    def vault_list(
        directory: Annotated[str, "Vault-relative directory path, e.g. 'PhD/mtDNA'. Defaults to vault root."] = "",
        all_files: Annotated[bool, "If True, also list non-.md files (assets, images, scripts). Default lists only .md files and subdirectories."] = False,
    ) -> str:
        """
        List files and subdirectories within a vault directory.
        Directories are marked with a trailing '/'. By default only .md files are
        shown; pass all_files=True to include every file.
        """
        target = _abs(directory) if directory else VAULT_ROOT
        if not target.is_dir():
            return f"Not a directory: '{directory}'"

        entries = []
        try:
            for item in sorted(target.iterdir()):
                rel = item.relative_to(VAULT_ROOT)
                if item.is_dir():
                    entries.append(f"  {rel}/")
                elif all_files or item.suffix == ".md":
                    entries.append(f"  {rel}")
        except OSError as e:
            return f"Error listing directory: {e}"

        if not entries:
            return f"Directory '{directory or 'vault root'}' is empty."
        return f"Contents of '{directory or 'vault root'}':\n" + "\n".join(entries)

    @mcp.tool()
    def vault_wikilinks(
        path: Annotated[str, "Vault-relative path or bare stem of the note whose link graph you want, e.g. 'Phase_Pipeline'."],
    ) -> str:
        """
        Inspect a note's wikilink graph.
        OUTWARD: every [[link]] the note itself contains.
        INBOUND: every note elsewhere in the vault that links to this note's stem
        (handles [[Name]], [[Name|Alias]], [[Name#Header]], and [[folder/Name]]).
        """
        target, err = _fuzzy_resolve(path)
        if err:
            return err

        stem = target.stem
        try:
            content = target.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            return f"Error reading file: {e}"

        outward = sorted({m.group(1).strip() for m in _WIKILINK_RE.finditer(content)})

        inbound = []
        stem_lower = stem.lower()
        for md_file, rel in _iter_md():
            if md_file == target:
                continue
            try:
                other = md_file.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            for m in _WIKILINK_RE.finditer(other):
                if _link_target_stem(m.group(1)).lower() == stem_lower:
                    inbound.append(rel)
                    break

        out_block = "\n".join(f"  [[{l}]]" for l in outward) if outward else "  (none)"
        in_block = "\n".join(f"  {r}" for r in sorted(inbound)) if inbound else "  (none)"
        return (
            f"Wikilinks for '{target.relative_to(VAULT_ROOT)}' (stem: {stem})\n\n"
            f"OUTWARD ({len(outward)}):\n{out_block}\n\n"
            f"INBOUND ({len(inbound)}):\n{in_block}"
        )

    @mcp.tool()
    def vault_recent(
        n: Annotated[int, "Number of recently updated notes to return (default 20)."] = 20,
        tag: Annotated[str, "Filter to notes carrying this frontmatter tag (exact match, case-sensitive). Optional."] = "",
    ) -> str:
        """
        Return the N most recently updated notes, ranked by the 'updated:' field in
        their YAML frontmatter. Notes without an 'updated:' field are excluded.

        Note: ranking deliberately uses frontmatter, not filesystem mtime — on this
        OneDrive/WSL setup sync and re-touch operations rewrite mtimes, so mtime is
        not a reliable signal of genuine edits.
        """
        _UPDATED = re.compile(r"^updated:\s*(\S+)", re.MULTILINE)
        results: list[tuple[date, str, list[str]]] = []

        for md_file, rel in _iter_md():
            try:
                content = md_file.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue

            fm = _frontmatter(content)
            if not fm:
                continue
            um = _UPDATED.search(fm)
            if not um:
                continue
            try:
                updated_date = date.fromisoformat(um.group(1))
            except ValueError:
                continue

            file_tags = _extract_tags(content)
            if tag and tag not in file_tags:
                continue
            results.append((updated_date, rel, file_tags))

        results.sort(key=lambda x: x[0], reverse=True)
        results = results[:n]

        if not results:
            hint = f" with tag '{tag}'" if tag else ""
            return f"No notes with 'updated:' frontmatter found{hint}."

        lines = [f"{'DATE':<12}  FILE", "-" * 72]
        for updated_date, rel, file_tags in results:
            tag_str = ", ".join(file_tags) if file_tags else "(none)"
            lines.append(f"{str(updated_date):<12}  {rel}")
            lines.append(f"{'':12}  tags: {tag_str}")
        return "\n".join(lines)
