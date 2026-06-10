"""
Write tools for the Obsidian Vault MCP Server.
"""

import re
import sys
import subprocess
from pathlib import Path
from typing import Annotated

from fastmcp import FastMCP

from config import VAULT_ROOT
from helpers import (
    abs_path,
    validate_stem,
    validate_tags,
    validate_placement,
    build_frontmatter,
    build_destinations_header,
    discover_trackers,
    NOTE_TYPE_SKELETONS,
)


def _touch_vault(*files: Path, refresh: bool = True) -> None:
    """
    Call touch_vault.py to force Obsidian to detect external edits.
    Fires and forgets — errors are silently ignored so write tools
    never fail due to a touch issue.
    """
    script = Path(__file__).parent.parent / "touch_vault.py"
    if not script.exists():
        return
    cmd = [sys.executable, str(script), "--vault", str(VAULT_ROOT)]
    for f in files:
        cmd.append(str(f))
    if refresh:
        cmd.append("--refresh")
    try:
        subprocess.Popen(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except OSError:
        pass


def register(mcp: FastMCP) -> None:

    @mcp.tool()
    def vault_create_note(
        name: Annotated[str, "File stem without .md. Alphanumeric and underscores only (e.g. my_note, My_README), or a numeric section (e.g. 01-Introduction). No spaces or special characters."],
        placement: Annotated[str, "Vault-relative claude_doc_dump directory. Allowed values: 'PhD/Literature Review/claude_doc_dump', 'PhD/mtDNA/claude_doc_dump', 'PhD/Evolution theory/claude_doc_dump', 'PhD/Hazelnut Project/claude_doc_dump', 'scripts/claude_doc_dump', 'Notes to process/claude_doc_dump'. Subdirectories within these are also allowed."],
        tags: Annotated[list[str], "List of tags. Must include at least one primary tag: Writing, Code, Tracker, Methods, Todo, Scripts, Theory, Issues, PhD, Life. Secondary tags are unrestricted."],
        destinations: Annotated[list[str], "One or more wikilinks pointing to where this content should eventually be integrated. e.g. ['[[01-Introduction]]', '[[02-Methods-and-initial-findings]]']. At least one required."],
        content: Annotated[str, "Body text. Each logical section should open with a '**→ Destinations:** [[target]]' line so the processing Claude knows where each part belongs."] = "",
        note_type: Annotated[str, "Optional note type: Hub, Theory, Code, Method, or Writing. When provided, a skeleton Note Role callout is auto-inserted after the destinations header. Caller fills in the <placeholders>."] = "",
    ) -> str:
        """
        Create a new note in a claude_doc_dump/ directory.
        All writes are restricted to dump directories — a privileged Claude session processes
        them into the correct vault locations later.
        """
        err = validate_stem(name)
        if err:
            return f"VALIDATION ERROR - Name: {err}"

        primary_tags, secondary_tags, err = validate_tags(tags)
        if err:
            return f"VALIDATION ERROR - Tags: {err}"

        err = validate_placement(placement)
        if err:
            return f"VALIDATION ERROR - Placement: {err}"

        if not destinations:
            return (
                "VALIDATION ERROR - Destinations: At least one destination wikilink is required. "
                "Example: [\"[[01-Introduction]]\"]"
            )

        target_dir = abs_path(placement)
        target_file = target_dir / f"{name}.md"

        if target_file.exists():
            return f"ERROR: File already exists: '{placement}/{name}.md'. Use vault_append to add content."

        # Validate note_type if provided
        if note_type and note_type not in NOTE_TYPE_SKELETONS:
            valid = ", ".join(NOTE_TYPE_SKELETONS)
            return f"VALIDATION ERROR - note_type: '{note_type}' is not valid. Choose from: {valid}"

        all_tags = primary_tags + secondary_tags
        if "doc_dump" not in all_tags:
            all_tags.append("doc_dump")
        frontmatter = build_frontmatter(all_tags, destinations)
        dest_header = build_destinations_header(destinations)

        # Build body with optional Note Role skeleton
        role_block = ""
        if note_type:
            role_block = f"\n{NOTE_TYPE_SKELETONS[note_type]}\n"
        body = f"\n{dest_header}{role_block}\n{content}" if content else f"\n{dest_header}{role_block}"

        try:
            target_dir.mkdir(parents=True, exist_ok=True)
            target_file.write_text(frontmatter + body, encoding="utf-8")
        except OSError as e:
            return f"ERROR writing file: {e}"

        rel = target_file.relative_to(VAULT_ROOT)
        dest_list = ", ".join(destinations)

        _touch_vault(target_file)

        # Soft warning if content provided but no Note Role callout
        warning = ""
        if content and "[!abstract] Note Role" not in content and not note_type:
            warning = (
                "\nWARNING: No Note Role callout detected. New vault notes require a "
                "> [!abstract] Note Role callout with fields: Contains, Cannot contain, "
                "Points to, Pointed to by. Consider passing note_type to auto-generate one."
            )

        return (
            f"Created: '{rel}'\n"
            f"NEXT STEP: call vault_flag_pending on each destination file — {dest_list}"
            f"{warning}"
        )

    @mcp.tool()
    def vault_append(
        path: Annotated[str, "Vault-relative path or bare filename stem of the target dump note, e.g. 'my_literature_notes' or 'PhD/Literature Review/claude_doc_dump/my_literature_notes.md'."],
        destinations: Annotated[list[str], "Wikilinks for where this section's content should eventually go. e.g. ['[[03-Discussion]]']. At least one required."],
        content: Annotated[str, "Markdown text for this section. A destinations header is prepended automatically."],
    ) -> str:
        """
        Append a new section to an existing claude_doc_dump note.
        Does NOT overwrite existing content — frontmatter and all prior sections are preserved.
        """
        if not destinations:
            return "VALIDATION ERROR - Destinations: At least one destination wikilink is required."

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
                return f"Ambiguous: multiple files match '{path}':\n{paths_str}"
            else:
                return f"File not found: '{path}'"

        try:
            existing = target.read_text(encoding="utf-8", errors="replace")
            separator = "\n" if existing.endswith("\n") else "\n\n"
            dest_header = build_destinations_header(destinations)
            section = f"{dest_header}\n{content}"
            target.write_text(existing + separator + section + "\n", encoding="utf-8")
        except OSError as e:
            return f"ERROR: {e}"

        rel = target.relative_to(VAULT_ROOT)
        _touch_vault(target)
        return f"Appended section to '{rel}' (destinations: {destinations})."

    @mcp.tool()
    def vault_edit_dump(
        path: Annotated[str, "Vault-relative path or bare filename stem of the target dump note, e.g. 'my_literature_notes' or 'PhD/Literature Review/claude_doc_dump/my_literature_notes.md'."],
        old_string: Annotated[str, "Exact text to find in the note. Must match uniquely (appear exactly once). Include enough surrounding context to be unambiguous."],
        new_string: Annotated[str, "Replacement text. Use empty string to delete the matched text."],
    ) -> str:
        """
        Edit an existing claude_doc_dump note by replacing an exact string match.
        Only works on files inside claude_doc_dump/ directories. Does not touch
        frontmatter — to change tags or destinations, create a new dump note instead.
        The old_string must appear exactly once in the file (excluding frontmatter).
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
                return f"Ambiguous: multiple files match '{path}':\n{paths_str}"
            else:
                return f"File not found: '{path}'"

        # Guard: only allow edits to files inside claude_doc_dump/
        rel = target.relative_to(VAULT_ROOT)
        if "claude_doc_dump" not in rel.parts:
            return (
                f"WRITE GUARD: '{rel}' is not inside a claude_doc_dump/ directory. "
                "vault_edit_dump can only modify dump notes."
            )

        try:
            content = target.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            return f"ERROR reading file: {e}"

        # Split frontmatter from body to protect it
        fm_end = 0
        if content.startswith("---"):
            second_fence = content.find("---", 3)
            if second_fence != -1:
                fm_end = second_fence + 3
                # advance past the newline after closing ---
                if fm_end < len(content) and content[fm_end] == "\n":
                    fm_end += 1

        frontmatter = content[:fm_end]
        body = content[fm_end:]

        count = body.count(old_string)
        if count == 0:
            return "ERROR: old_string not found in the note body."
        if count > 1:
            return f"ERROR: old_string appears {count} times — must be unique. Include more surrounding context."

        new_body = body.replace(old_string, new_string, 1)

        try:
            target.write_text(frontmatter + new_body, encoding="utf-8")
        except OSError as e:
            return f"ERROR writing file: {e}"

        _touch_vault(target)
        return f"Edited '{rel}': replaced 1 occurrence ({len(old_string)} → {len(new_string)} chars)."

    @mcp.tool()
    def vault_rename(
        old_name: Annotated[str, "Current file stem without .md, e.g. 'old_note_name'. Must match exactly (case-sensitive)."],
        new_name: Annotated[str, "New file stem without .md. Alphanumeric and underscores only (e.g. my_note, My_README), or a numeric section (e.g. 01-Introduction). No spaces or special characters."],
        dry_run: Annotated[bool, "If True, preview all changes without writing anything. Use to verify before committing a rename."] = False,
    ) -> str:
        """
        Rename a note and update all wikilinks referencing it across the entire vault.
        Handles all wikilink formats: [[Name]], [[Name|Alias]], [[Name#Header]], [[Name#Header|Alias]].
        Delegates to the bundled rename_note.py script.
        """
        err = validate_stem(new_name)
        if err:
            return f"VALIDATION ERROR - New name: {err}"

        script = Path(__file__).parent.parent / "rename_note.py"
        if not script.exists():
            return f"ERROR: rename_note.py not found at '{script}'. Cannot rename."

        cmd = [
            sys.executable, str(script),
            old_name, new_name,
            "--vault", str(VAULT_ROOT),
        ]
        if dry_run:
            cmd.append("--dry-run")

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60,
            )
            output = result.stdout + result.stderr
            if result.returncode != 0:
                return f"ERROR (exit {result.returncode}):\n{output}"
            # Touch recently modified files since rename affects multiple files
            _touch_vault()
            return output or f"Rename completed: '{old_name}' → '{new_name}'."
        except subprocess.TimeoutExpired:
            return "ERROR: rename_note.py timed out after 60 seconds."
        except OSError as e:
            return f"ERROR running rename_note.py: {e}"

    @mcp.tool()
    def vault_import_file(
        source_path: Annotated[str, "Absolute path to the local file to import, e.g. '/home/user/Documents/example.md'."],
        name: Annotated[str, "File stem without .md for the destination note. Alphanumeric and underscores only (e.g. my_note, My_README), or a numeric section (e.g. 01-Introduction). No spaces or special characters."],
        placement: Annotated[str, "Vault-relative claude_doc_dump directory. Allowed values: 'PhD/Literature Review/claude_doc_dump', 'PhD/mtDNA/claude_doc_dump', 'PhD/Evolution theory/claude_doc_dump', 'PhD/Hazelnut Project/claude_doc_dump', 'scripts/claude_doc_dump', 'Notes to process/claude_doc_dump'. Subdirectories within these are also allowed."],
        tags: Annotated[list[str], "List of tags. Must include at least one primary tag: Writing, Code, Tracker, Methods, Todo, Scripts, Theory, Issues, PhD, Life. Secondary tags are unrestricted."],
        destinations: Annotated[list[str], "One or more wikilinks pointing to where this content should eventually be integrated. e.g. ['[[01-Introduction]]']. At least one required."],
    ) -> str:
        """
        Import a local file directly into a claude_doc_dump/ directory without passing
        its content through the context window. Prepends vault frontmatter and a
        destinations header, then copies the file content as-is. Ideal for large files.
        """
        err = validate_stem(name)
        if err:
            return f"VALIDATION ERROR - Name: {err}"

        primary_tags, secondary_tags, err = validate_tags(tags)
        if err:
            return f"VALIDATION ERROR - Tags: {err}"

        err = validate_placement(placement)
        if err:
            return f"VALIDATION ERROR - Placement: {err}"

        if not destinations:
            return "VALIDATION ERROR - Destinations: At least one destination wikilink is required."

        source = Path(source_path)
        if not source.exists():
            return f"ERROR: Source file not found: '{source_path}'"
        if not source.is_file():
            return f"ERROR: Source path is not a file: '{source_path}'"

        try:
            content = source.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            return f"ERROR reading source file: {e}"

        target_dir = abs_path(placement)
        target_file = target_dir / f"{name}.md"

        if target_file.exists():
            return f"ERROR: File already exists: '{placement}/{name}.md'. Use vault_append to add content."

        all_tags = primary_tags + secondary_tags
        if "doc_dump" not in all_tags:
            all_tags.append("doc_dump")
        frontmatter = build_frontmatter(all_tags, destinations)
        dest_header = build_destinations_header(destinations)

        try:
            target_dir.mkdir(parents=True, exist_ok=True)
            target_file.write_text(frontmatter + f"\n{dest_header}\n" + content, encoding="utf-8")
        except OSError as e:
            return f"ERROR writing file: {e}"

        rel = target_file.relative_to(VAULT_ROOT)
        size_kb = source.stat().st_size / 1024
        dest_list = ", ".join(destinations)
        _touch_vault(target_file)
        return (
            f"Imported '{source.name}' ({size_kb:.1f} KB) → '{rel}'\n"
            f"NEXT STEP: call vault_flag_pending on each destination file — {dest_list}"
        )

    @mcp.tool()
    def vault_import_directory(
        source_dir: Annotated[str, "Absolute path to the local directory to import recursively, e.g. '/home/user/Documents/pipeline_docs/'."],
        placement: Annotated[str, "Vault-relative claude_doc_dump directory to import into. The source directory structure is mirrored inside this placement, preserving all relative paths and links. Allowed roots: 'PhD/Literature Review/claude_doc_dump', 'PhD/mtDNA/claude_doc_dump', 'PhD/Evolution theory/claude_doc_dump', 'PhD/Hazelnut Project/claude_doc_dump', 'scripts/claude_doc_dump', 'Notes to process/claude_doc_dump'."],
        tags: Annotated[list[str], "List of tags applied to every imported note. Must include at least one primary tag: Writing, Code, Tracker, Methods, Todo, Scripts, Theory, Issues, PhD, Life. Secondary tags are unrestricted."],
        destinations: Annotated[list[str], "One or more wikilinks applied to every imported note. At least one required. e.g. ['[[Pipeline_Overview]]']"],
    ) -> str:
        """
        Recursively import a directory of markdown files into a claude_doc_dump/,
        mirroring the source directory structure exactly so relative links between
        files remain valid. Each file gets vault frontmatter and a destinations header
        prepended. Non-.md files are skipped.
        """
        primary_tags, secondary_tags, err = validate_tags(tags)
        if err:
            return f"VALIDATION ERROR - Tags: {err}"

        err = validate_placement(placement)
        if err:
            return f"VALIDATION ERROR - Placement: {err}"

        if not destinations:
            return "VALIDATION ERROR - Destinations: At least one destination wikilink is required."

        source = Path(source_dir)
        if not source.exists():
            return f"ERROR: Source directory not found: '{source_dir}'"
        if not source.is_dir():
            return f"ERROR: Source path is not a directory: '{source_dir}'"

        md_files = sorted(source.rglob("*.md"))
        if not md_files:
            return f"ERROR: No .md files found in '{source_dir}'"

        all_tags = primary_tags + secondary_tags
        if "doc_dump" not in all_tags:
            all_tags.append("doc_dump")
        frontmatter = build_frontmatter(all_tags, destinations)
        dest_header = build_destinations_header(destinations)

        dest_root = abs_path(placement)
        imported = []
        errors = []

        for md_file in md_files:
            # Preserve relative path from source root
            rel_from_source = md_file.relative_to(source)
            target_file = dest_root / rel_from_source

            if target_file.exists():
                errors.append(f"SKIP (exists): {rel_from_source}")
                continue

            try:
                content = md_file.read_text(encoding="utf-8", errors="replace")
                target_file.parent.mkdir(parents=True, exist_ok=True)
                target_file.write_text(frontmatter + f"\n{dest_header}\n" + content, encoding="utf-8")
                imported.append(str(rel_from_source))
            except OSError as e:
                errors.append(f"ERROR: {rel_from_source}: {e}")

        total_kb = sum(f.stat().st_size for f in md_files) / 1024
        dest_list = ", ".join(destinations)
        # Touch all imported files
        imported_paths = [dest_root / p for p in imported]
        _touch_vault(*imported_paths)
        lines = [f"Imported {len(imported)} file(s) ({total_kb:.1f} KB total) → '{placement}'"]
        if errors:
            lines.append(f"\nSkipped/errors ({len(errors)}):")
            lines.extend(f"  {e}" for e in errors)
        lines.append(f"\nNEXT STEP: call vault_resolve_links on the dump path, then vault_flag_pending on each destination file — {dest_list}")
        return "\n".join(lines)

    @mcp.tool()
    def vault_resolve_links(
        path: Annotated[str, "Vault-relative path to a claude_doc_dump directory or file, e.g. 'PhD/Literature Review/claude_doc_dump/pipeline_documentation'. Must be inside a claude_doc_dump directory."],
        dry_run: Annotated[bool, "If True, preview changes without writing anything."] = False,
    ) -> str:
        """
        Resolve broken internal markdown links in an imported vault dump directory.
        Run this after vault_import_directory to catch links that were valid at the
        source but broken after import (e.g. links pointing outside the imported tree).
        Skips lines already inside HTML comments — safe to re-run.
        Converts unresolvable links to <!-- UNRESOLVED LINK: ... --> comments.
        """
        err = validate_placement(path)
        if err:
            return f"VALIDATION ERROR: {err}"

        target = abs_path(path)
        if not target.exists():
            return f"ERROR: Path not found in vault: '{path}'"

        script = Path(__file__).parent.parent / "resolve_links.py"
        if not script.exists():
            return f"ERROR: resolve_links.py not found at '{script}'."

        cmd = [sys.executable, str(script), str(target)]
        if dry_run:
            cmd.append("--dry-run")

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return result.stdout + result.stderr or "No output."
        except subprocess.TimeoutExpired:
            return "ERROR: resolve_links.py timed out after 120 seconds."
        except OSError as e:
            return f"ERROR running resolve_links.py: {e}"

    def _resolve_destination(path: str):
        """
        Resolve a destination path or bare stem to an absolute Path.
        Returns (Path, None) on success or (None, error_string) on failure.
        Accepts: vault-relative path, bare stem, or bare filename.
        """
        target = abs_path(path)
        if target.exists() and target.suffix == ".md":
            return target, None

        # Fuzzy resolution by stem / filename — mirrors vault_append behaviour
        stem = Path(path).stem
        name = Path(path).name if Path(path).suffix else f"{path}.md"
        matches = list(VAULT_ROOT.rglob(f"{stem}.md"))
        if not matches:
            matches = list(VAULT_ROOT.rglob(name))
        if len(matches) == 1:
            return matches[0], None
        if len(matches) > 1:
            paths_str = "\n".join(str(m.relative_to(VAULT_ROOT)) for m in matches)
            return None, f"Ambiguous: multiple files match '{path}':\n{paths_str}\nProvide the full vault-relative path."
        return None, (
            f"NEW NOTE: Destination '[[{stem}]]' does not exist in the vault — this is a new note. "
            "Do NOT retry vault_flag_pending. Instead, include a '> [!note] NEW NOTE' callout in "
            "the dump body (see make-note skill for format). The process-notes integrator "
            "will create it."
        )

    @mcp.tool()
    def vault_flag_pending(
        destination: Annotated[str, "Vault-relative path or bare filename stem of the destination note, e.g. 'Phase_Pipeline' or 'PhD/Literature Review/Phase_Pipeline.md'. Resolved by fuzzy search if the exact path is not given."],
        dump_name: Annotated[str, "Wikilink of the dump note waiting to be integrated, e.g. '[[phase5b_optimisation]]'."],
    ) -> str:
        """
        Add a pending callout to a destination note signalling that a doc dump is
        waiting to be integrated into it. Appends:
            > [!todo] Pending dump: [[dump_name]]
        Accepts a bare stem (e.g. 'Phase_Pipeline') and resolves it to the actual
        file — fails loudly if the stem is ambiguous or not found.
        Does not duplicate if the callout already exists.
        """
        target, err = _resolve_destination(destination)
        if err:
            if err.startswith("NEW NOTE:"):
                return err          # already prefixed — surface directly, not as ERROR
            return f"ERROR: {err}"

        try:
            existing = target.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            return f"ERROR reading file: {e}"

        callout = f"> [!todo] Pending dump: {dump_name}"
        if callout in existing:
            rel = target.relative_to(VAULT_ROOT)
            return f"Pending callout for {dump_name} already exists in '{rel}'."

        separator = "\n" if existing.endswith("\n") else "\n\n"
        try:
            target.write_text(existing + separator + callout + "\n", encoding="utf-8")
        except OSError as e:
            return f"ERROR writing file: {e}"

        rel = target.relative_to(VAULT_ROOT)
        _touch_vault(target)
        return f"Flagged '{rel}' with pending dump: {dump_name}"

    @mcp.tool()
    def vault_clear_pending(
        destination: Annotated[str, "Vault-relative path or bare filename stem of the destination note, e.g. 'Phase_Pipeline' or 'PhD/Literature Review/Phase_Pipeline.md'."],
        dump_name: Annotated[str, "Wikilink of the dump note to clear, e.g. '[[phase5b_optimisation]]'. Pass empty string to clear ALL pending callouts from this file."] = "",
    ) -> str:
        """
        Remove pending dump callout(s) from a destination note after the dump has
        been integrated. Removes lines matching:
            > [!todo] Pending dump: [[dump_name]]
        Accepts a bare stem and resolves it by fuzzy search.
        Pass dump_name='' to clear all pending callouts from the file.
        """
        target, err = _resolve_destination(destination)
        if err:
            return f"ERROR: {err}"

        try:
            content = target.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            return f"ERROR reading file: {e}"

        if dump_name:
            pattern = rf'> \[!todo\] Pending dump: {re.escape(dump_name)}\n?'
            label = f"for {dump_name}"
        else:
            pattern = r'> \[!todo\] Pending dump: [^\n]+\n?'
            label = "(all)"

        updated = re.sub(pattern, "", content)
        if updated == content:
            rel = target.relative_to(VAULT_ROOT)
            return f"No pending callout found {label} in '{rel}'."

        # Normalise any runs of 3+ newlines left by removal to at most 2
        updated = re.sub(r'\n{3,}', '\n\n', updated)

        try:
            target.write_text(updated, encoding="utf-8")
        except OSError as e:
            return f"ERROR writing file: {e}"

        rel = target.relative_to(VAULT_ROOT)
        _touch_vault(target)
        return f"Cleared pending callout {label} from '{rel}'."

    @mcp.tool()
    def vault_update_tracker_item(
        project: Annotated[str, "Project name as returned by vault_list_projects (e.g. 'Literature Review', 'mtDNA')."],
        title: Annotated[str, "Exact title of the callout item to update (e.g. 'Figure 2b orphan overlay data')."],
        new_status: Annotated[str, "New status value: 'pending', 'in-progress', or 'complete'."],
    ) -> str:
        """
        Update the status field of a typed callout item in a project tracker.
        Finds the item by its exact title and replaces the status line.
        When status is set to 'complete', the item is moved to the ## Completed section.
        """
        valid_statuses = ("pending", "in-progress", "complete")
        if new_status not in valid_statuses:
            return f"VALIDATION ERROR: status must be one of {valid_statuses}, got '{new_status}'."

        trackers = discover_trackers()
        if project not in trackers:
            available = ", ".join(sorted(trackers.keys())) or "(none)"
            return f"Project '{project}' not found. Available: {available}"

        tracker_path = trackers[project]
        try:
            content = tracker_path.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            return f"Error reading tracker: {e}"

        # Find the callout block by title
        pattern = re.compile(
            r'(> \[!(?:data-pull|task|decision|blocker)\]\s*'
            + re.escape(title)
            + r'\n(?:> .+\n)*)',
            re.MULTILINE,
        )
        match = pattern.search(content)
        if not match:
            return f"Item '{title}' not found in {project} tracker."

        old_block = match.group(0)

        # Replace the status line within the block
        status_pattern = re.compile(r'(> \*\*status\*\*:\s*)(\S+)')
        if not status_pattern.search(old_block):
            return f"Item '{title}' has no status field to update."

        new_block = status_pattern.sub(rf'\g<1>{new_status}', old_block)

        if new_status == "complete":
            # Remove the item from its current location
            content = content.replace(old_block, "")
            # Clean up blank lines left behind
            content = re.sub(r'\n{3,}', '\n\n', content)

            # Build a completed checkbox entry
            from datetime import date
            done_line = f"- [x] {title} ({date.today().isoformat()})\n"

            # Append to ## Completed section
            completed_match = re.search(r'^## Completed\s*\n', content, re.MULTILINE)
            if completed_match:
                insert_pos = completed_match.end()
                content = content[:insert_pos] + "\n" + done_line + content[insert_pos:]
            else:
                content = content.rstrip("\n") + "\n\n## Completed\n\n" + done_line
        else:
            content = content.replace(old_block, new_block)

        try:
            tracker_path.write_text(content, encoding="utf-8")
        except OSError as e:
            return f"Error writing tracker: {e}"

        rel = tracker_path.relative_to(VAULT_ROOT)
        _touch_vault(tracker_path)
        return f"Updated '{title}' → {new_status} in '{rel}'."

    @mcp.tool()
    def vault_add_tracker_item(
        project: Annotated[str, "Project name as returned by vault_list_projects (e.g. 'Literature Review', 'mtDNA')."],
        item_type: Annotated[str, "Item type: 'data-pull', 'task', 'decision', or 'blocker'."],
        title: Annotated[str, "Short unique title for the item."],
        detail: Annotated[str, "Description of what's needed."],
        source: Annotated[str, "Path to source file/script (backtick-wrapped). Optional."] = "",
        target: Annotated[str, "Vault note(s) where the result goes — use [[wikilinks]]. Optional."] = "",
        blocks: Annotated[str, "Items or sections this blocks. Optional."] = "",
    ) -> str:
        """
        Add a new typed callout item to a project tracker. Inserts under the
        correct section header (## Data Pulls, ## Tasks, ## Decisions, ## Blockers).
        Validates title uniqueness and required fields.
        """
        valid_types = ("data-pull", "task", "decision", "blocker")
        if item_type not in valid_types:
            return f"VALIDATION ERROR: item_type must be one of {valid_types}, got '{item_type}'."

        trackers = discover_trackers()
        if project not in trackers:
            available = ", ".join(sorted(trackers.keys())) or "(none)"
            return f"Project '{project}' not found. Available: {available}"

        tracker_path = trackers[project]
        try:
            content = tracker_path.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            return f"Error reading tracker: {e}"

        # Check title uniqueness
        from helpers import parse_tracker_items
        existing = parse_tracker_items(content)
        for item in existing:
            if item["title"].lower() == title.lower():
                return f"VALIDATION ERROR: item '{title}' already exists in {project} tracker (type: {item['type']})."

        # Build the callout block
        lines = [f"> [!{item_type}] {title}"]
        lines.append("> **status**: pending")
        if source:
            lines.append(f"> **source**: {source}")
        if target:
            lines.append(f"> **target**: {target}")
        if blocks:
            lines.append(f"> **blocks**: {blocks}")
        lines.append(f"> **detail**: {detail}")
        callout = "\n".join(lines) + "\n"

        # Map item type to section header
        section_map = {
            "data-pull": "## Data Pulls",
            "task": "## Tasks",
            "decision": "## Decisions",
            "blocker": "## Blockers",
        }
        section_header = section_map[item_type]

        # Find the section and insert at the end of it
        # Look for the section header, then find the next ## header or end of file
        section_re = re.compile(
            rf'^{re.escape(section_header)}\s*\n',
            re.MULTILINE,
        )
        section_match = section_re.search(content)

        if section_match:
            # Find the next ## header after this section
            next_header = re.search(r'^## ', content[section_match.end():], re.MULTILINE)
            if next_header:
                insert_pos = section_match.end() + next_header.start()
            else:
                insert_pos = len(content)

            # Walk back past trailing whitespace to insert cleanly
            while insert_pos > 0 and content[insert_pos - 1] == "\n":
                insert_pos -= 1

            content = content[:insert_pos] + "\n\n" + callout + "\n" + content[insert_pos:]
        else:
            # Section doesn't exist — create it before ## Completed or at end
            completed_match = re.search(r'^## Completed\s*\n', content, re.MULTILINE)
            if completed_match:
                insert_pos = completed_match.start()
                content = content[:insert_pos] + f"{section_header}\n\n{callout}\n---\n\n" + content[insert_pos:]
            else:
                content = content.rstrip("\n") + f"\n\n{section_header}\n\n{callout}"

        try:
            tracker_path.write_text(content, encoding="utf-8")
        except OSError as e:
            return f"Error writing tracker: {e}"

        rel = tracker_path.relative_to(VAULT_ROOT)
        _touch_vault(tracker_path)
        return f"Added [{item_type}] '{title}' to {project} tracker ({rel})."
