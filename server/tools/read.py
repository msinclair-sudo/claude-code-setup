"""
Read tools for the Obsidian Vault MCP Server.
"""

import re
from datetime import date
from pathlib import Path
from typing import Annotated

from fastmcp import FastMCP

from config import VAULT_ROOT, ALLOWED_PRIMARY_TAGS
from helpers import abs_path, discover_trackers, parse_tracker_items


def register(mcp: FastMCP) -> None:

    @mcp.tool()
    def vault_search(
        query: Annotated[str, "Space-separated search terms (case-insensitive). Each term is matched independently across the file — a file matches if it contains ALL terms anywhere in its content. Pass empty string to search by tag only."],
        tag: Annotated[str, "Filter results to notes containing this tag (exact match, case-sensitive). e.g. 'PhD', 'Methods'. Optional."] = "",
    ) -> str:
        """
        Search the vault for notes matching a text query and/or tag.
        Query is split into individual terms; a file matches if it contains ALL terms
        (each term may appear on any line). Returns FILE path, TAGS, and an EXCERPT
        showing the first line that contains any of the search terms.
        """
        results = []
        terms = query.lower().split() if query.strip() else []

        for md_file in VAULT_ROOT.rglob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue

            rel = md_file.relative_to(VAULT_ROOT)

            file_tags: list[str] = []
            fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if fm_match:
                for line in fm_match.group(1).splitlines():
                    t = re.match(r'\s*-\s+(\S+)', line)
                    if t:
                        file_tags.append(t.group(1))

            if tag and tag not in file_tags:
                continue

            if terms:
                content_lower = content.lower()
                if not all(term in content_lower for term in terms):
                    continue
                # Excerpt: first line containing any search term
                excerpt_line = next(
                    (ln for ln in content.splitlines() if any(term in ln.lower() for term in terms)),
                    ""
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
            return f"No results found for query='{query}' tag='{tag}'."
        return "\n\n".join(results)

    @mcp.tool()
    def vault_read(
        path: Annotated[str, "Vault-relative path (e.g. 'PhD/Literature Review/01-Introduction.md') or bare filename stem (e.g. '01-Introduction'). Searches recursively if no directory given."],
    ) -> str:
        """
        Read a note's full content including frontmatter.
        If multiple files share the same stem, the full relative path is required.
        """
        target = abs_path(path)

        if not target.exists():
            stem = Path(path).stem
            matches = list(VAULT_ROOT.rglob(f"{stem}.md"))
            if not matches:
                matches = list(VAULT_ROOT.rglob(f"{Path(path).name}"))
            if len(matches) == 1:
                target = matches[0]
            elif len(matches) > 1:
                paths_str = "\n".join(str(m.relative_to(VAULT_ROOT)) for m in matches)
                return f"Ambiguous: multiple files match '{path}':\n{paths_str}\nPlease provide the full relative path."
            else:
                return f"File not found: '{path}'"

        try:
            return target.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            return f"Error reading file: {e}"

    @mcp.tool()
    def vault_list(
        directory: Annotated[str, "Vault-relative directory path, e.g. 'PhD/Literature Review'. Defaults to vault root if omitted."] = "",
    ) -> str:
        """
        List files and subdirectories within a vault directory.
        Directories are marked with a trailing '/'. Only .md files are shown.
        """
        target = abs_path(directory) if directory else VAULT_ROOT

        if not target.is_dir():
            return f"Not a directory: '{directory}'"

        entries = []
        try:
            for item in sorted(target.iterdir()):
                rel = item.relative_to(VAULT_ROOT)
                if item.is_dir():
                    entries.append(f"  {rel}/")
                elif item.suffix == ".md":
                    entries.append(f"  {rel}")
        except OSError as e:
            return f"Error listing directory: {e}"

        if not entries:
            return f"Directory '{directory or 'vault root'}' is empty."
        return f"Contents of '{directory or 'vault root'}':\n" + "\n".join(entries)

    @mcp.tool()
    def vault_tags() -> str:
        """
        Return all tags used across the vault, grouped by primary vs secondary, with usage counts.
        Primary tags are the controlled set; secondary tags are unrestricted.
        """
        primary_counts: dict[str, int] = {}
        secondary_counts: dict[str, int] = {}

        for md_file in VAULT_ROOT.rglob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue

            fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not fm_match:
                continue

            for line in fm_match.group(1).splitlines():
                t = re.match(r'\s*-\s+(\S+)', line)
                if t:
                    tag = t.group(1)
                    if tag in ALLOWED_PRIMARY_TAGS:
                        primary_counts[tag] = primary_counts.get(tag, 0) + 1
                    else:
                        secondary_counts[tag] = secondary_counts.get(tag, 0) + 1

        def _fmt(counts: dict[str, int]) -> str:
            if not counts:
                return "  (none)"
            return "\n".join(
                f"  {tag}: {n}" for tag, n in sorted(counts.items(), key=lambda x: -x[1])
            )

        return (
            "PRIMARY TAGS:\n" + _fmt(primary_counts) +
            "\n\nSECONDARY TAGS:\n" + _fmt(secondary_counts)
        )

    @mcp.tool()
    def vault_recent(
        n: Annotated[int, "Number of recently updated notes to return (default 20)."] = 20,
        tag: Annotated[str, "Filter to notes containing this tag (exact match, case-sensitive). Optional."] = "",
    ) -> str:
        """
        Return the N most recently updated notes in the vault, ranked by the
        'updated:' field in their YAML frontmatter. Notes without an 'updated:'
        field are excluded. Returns path, updated date, and tags for each note.
        """
        _FM = re.compile(r'^---\n(.*?)\n---', re.DOTALL)
        _UPDATED = re.compile(r'^updated:\s*(\S+)', re.MULTILINE)
        _TAG_LINE = re.compile(r'^\s*-\s+(\S+)', re.MULTILINE)

        results: list[tuple[date, str, list[str]]] = []

        for md_file in VAULT_ROOT.rglob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue

            fm_match = _FM.match(content)
            if not fm_match:
                continue
            fm_body = fm_match.group(1)

            updated_match = _UPDATED.search(fm_body)
            if not updated_match:
                continue

            try:
                updated_date = date.fromisoformat(updated_match.group(1))
            except ValueError:
                continue

            file_tags = _TAG_LINE.findall(fm_body)

            if tag and tag not in file_tags:
                continue

            rel = str(md_file.relative_to(VAULT_ROOT))
            results.append((updated_date, rel, file_tags))

        results.sort(key=lambda x: x[0], reverse=True)
        results = results[:n]

        if not results:
            hint = f" with tag '{tag}'" if tag else ""
            return f"No notes with 'updated:' frontmatter found{hint}."

        lines = [f"{'DATE':<12}  FILE"]
        lines.append("-" * 72)
        for updated_date, rel, file_tags in results:
            tag_str = ", ".join(file_tags) if file_tags else "(none)"
            lines.append(f"{str(updated_date):<12}  {rel}")
            lines.append(f"{'':12}  tags: {tag_str}")
        return "\n".join(lines)

    @mcp.tool()
    def vault_list_projects() -> str:
        """
        Discover all projects in the vault by scanning for tracker files
        at PhD/<project>/*_Tracker.md. Returns project names and their
        tracker file paths.
        """
        trackers = discover_trackers()
        if not trackers:
            return "No tracker files found at PhD/<project>/*_Tracker.md."
        lines = []
        for name, path in trackers.items():
            rel = path.relative_to(VAULT_ROOT)
            lines.append(f"  {name}  ->  {rel}")
        return f"Projects ({len(trackers)}):\n" + "\n".join(lines)

    @mcp.tool()
    def vault_read_tracker(
        project: Annotated[str, "Project name as returned by vault_list_projects (e.g. 'Literature Review', 'mtDNA')."],
        item_type: Annotated[str, "Filter by callout type: 'data-pull', 'task', 'decision', 'blocker', or 'all' for everything."] = "all",
        status: Annotated[str, "Filter by status: 'pending', 'in-progress', 'complete', or 'all'."] = "pending",
    ) -> str:
        """
        Read a project's tracker file and return structured items parsed from
        typed callouts ([!data-pull], [!task], [!decision], [!blocker]).
        Supports filtering by type and status. Returns machine-readable output.
        """
        trackers = discover_trackers()
        if project not in trackers:
            available = ", ".join(sorted(trackers.keys())) or "(none)"
            return f"Project '{project}' not found. Available: {available}"

        try:
            content = trackers[project].read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            return f"Error reading tracker: {e}"

        items = parse_tracker_items(content)

        if item_type != "all":
            items = [i for i in items if i["type"] == item_type]
        if status != "all":
            items = [i for i in items if i.get("status", "") == status]

        if not items:
            return f"No items matching type='{item_type}' status='{status}' in {project} tracker."

        lines = []
        for i in items:
            parts = [f"[{i['type']}] {i['title']}"]
            for key in ("status", "source", "target", "blocks", "detail"):
                if key in i:
                    parts.append(f"  {key}: {i[key]}")
            lines.append("\n".join(parts))
        return f"{project} tracker — {len(items)} items:\n\n" + "\n\n".join(lines)
