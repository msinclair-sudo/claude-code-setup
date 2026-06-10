"""
Shared helper functions for the Obsidian Vault MCP Server.
"""

import re
from pathlib import Path
from typing import Optional

from config import VAULT_ROOT, ALLOWED_PRIMARY_TAGS, ALL_VALID_PLACEMENTS


def abs_path(rel: str) -> Path:
    """Resolve a vault-relative path to an absolute path."""
    return VAULT_ROOT / rel


def validate_stem(stem: str) -> Optional[str]:
    """
    Returns None if valid, or an error message string if invalid.
    Valid patterns:
      - snake_case:     [a-z][a-z0-9_]+
      - kebab section:  NN-Title  (digits followed by dash and word chars)
      - Script README:  <snake_case>_README
    """
    if re.match(r'^\d{2}-\w+', stem):
        return None
    if re.match(r'^[a-zA-Z][a-zA-Z0-9_]+$', stem):
        return None
    return (
        f"Invalid file name '{stem}'. "
        "Name must be alphanumeric with underscores (e.g. my_note, My_README), "
        "or a numeric section (e.g. 01-Introduction). No spaces or special characters allowed."
    )


def validate_tags(tags: list[str]) -> tuple[list[str], list[str], Optional[str]]:
    """
    Splits tags into (primary, secondary).
    Returns (primary_tags, secondary_tags, error_or_None).
    Secondary tags are unrestricted — any tag not in ALLOWED_PRIMARY_TAGS is secondary.
    """
    primary = [t for t in tags if t in ALLOWED_PRIMARY_TAGS]
    secondary = [t for t in tags if t not in ALLOWED_PRIMARY_TAGS]

    if not primary:
        return [], [], (
            f"At least one primary tag is required. "
            f"Allowed primary tags: {ALLOWED_PRIMARY_TAGS}."
        )

    return primary, secondary, None


def validate_placement(placement: str) -> Optional[str]:
    """
    Returns None if valid, or an error message string if invalid.
    Exact claude_doc_dump paths are valid, as are any subdirectories within them.
    """
    if placement in ALL_VALID_PLACEMENTS:
        return None
    for valid in ALL_VALID_PLACEMENTS:
        if placement.startswith(valid + "/"):
            return None
    allowed = "\n".join(f"  - {p}" for p in sorted(ALL_VALID_PLACEMENTS))
    return (
        f"Placement '{placement}' is not inside a claude_doc_dump directory.\n"
        f"Allowed roots (subdirs permitted):\n{allowed}"
    )


def build_frontmatter(tags: list[str], destinations: list[str]) -> str:
    tag_lines = "\n".join(f"  - {t}" for t in tags)
    dest_lines = "\n".join(f'  - "{d}"' for d in destinations)
    return f"---\ntags:\n{tag_lines}\ndestinations:\n{dest_lines}\n---\n"


def build_destinations_header(destinations: list[str]) -> str:
    """Inline destinations block written at the top of each section."""
    links = " | ".join(destinations)
    return f"**→ Destinations:** {links}\n"


# ---------------------------------------------------------------------------
# Tracker discovery and parsing
# ---------------------------------------------------------------------------

_CALLOUT_RE = re.compile(
    r'^> \[!(data-pull|task|decision|blocker)\]\s*(.+)\n'
    r'((?:> .+\n)*)',
    re.MULTILINE,
)
_FIELD_RE = re.compile(r'^> \*\*(\w+)\*\*:\s*(.+)', re.MULTILINE)


def discover_trackers() -> dict[str, Path]:
    """Return {project_name: absolute_path} for all *_Tracker.md files at PhD/<project>/."""
    trackers: dict[str, Path] = {}
    phd_dir = VAULT_ROOT / "PhD"
    if not phd_dir.is_dir():
        return trackers
    for project_dir in sorted(phd_dir.iterdir()):
        if not project_dir.is_dir():
            continue
        for f in project_dir.iterdir():
            if f.name.endswith("_Tracker.md") and f.is_file():
                trackers[project_dir.name] = f
    return trackers


def parse_tracker_items(content: str) -> list[dict]:
    """Parse typed callouts ([!data-pull], [!task], etc.) into structured dicts."""
    items: list[dict] = []
    for m in _CALLOUT_RE.finditer(content):
        item: dict = {
            "type": m.group(1),
            "title": m.group(2).strip(),
        }
        body = m.group(3)
        for fm in _FIELD_RE.finditer(body):
            item[fm.group(1)] = fm.group(2).strip()
        items.append(item)
    return items


NOTE_TYPE_SKELETONS: dict[str, str] = {
    "Hub": (
        "> [!abstract] Note Role\n"
        "> **Contains**: Navigation index — wikilinks with one-line descriptions only. No content.\n"
        "> **Cannot contain**: Any content that belongs in the typed notes it indexes.\n"
        "> **Points to**: \n"
        "> **Pointed to by**: [[<project>_TOC]]"
    ),
    "Tracker": (
        "> [!abstract] Note Role\n"
        "> **Contains**: live task list — pipeline status, decisions, blockers\n"
        "> **Cannot contain**: prose, analysis, or implementation detail (→ linked notes)\n"
        "> **Points to**: \n"
        "> **Pointed to by**: [[<project>_TOC]]"
    ),
    "Theory": (
        "> [!abstract] Note Role\n"
        "> **Contains**: <concept> — definitions, formulas, published literature (project-agnostic)\n"
        "> **Cannot contain**: project-specific results, parameters, or pipeline references\n"
        "> **Points to**: \n"
        "> **Pointed to by**: [[<method_note>]], [[Theory_TOC]], [[<project>_Theory_TOC]]"
    ),
    "Code": (
        "> [!abstract] Note Role\n"
        "> **Contains**: implementation detail — function signatures, data flow, refactor history\n"
        "> **Cannot contain**: method rationale or scientific justification (→ paired Method note)\n"
        "> **Points to**: \n"
        "> **Pointed to by**: [[<project>_Code_TOC]], [[<paired_method_note>]]"
    ),
    "Method": (
        "> [!abstract] Note Role\n"
        "> **Contains**: processing narrative — what was done, from what input, what was produced, why\n"
        "> **Cannot contain**: implementation detail (→ paired Code note)\n"
        "> **Points to**: \n"
        "> **Pointed to by**: [[<project>_Methods_TOC]], [[<paired_code_note>]], [[<project>_Theory_TOC]]"
    ),
    "Writing": (
        "> [!abstract] Note Role\n"
        "> **Contains**: manuscript prose — external-audience text with figures/tables as evidence\n"
        "> **Cannot contain**: implementation details, raw analysis, or internal notes\n"
        "> **Points to**: \n"
        "> **Pointed to by**: [[<project>_Writing_TOC]]"
    ),
    "Issues": (
        "> [!abstract] Note Role\n"
        "> **Contains**: <description of unresolved problem>\n"
        "> **Cannot contain**: Solutions that belong in Method or Code notes.\n"
        "> **Points to**: \n"
        "> **Pointed to by**: [[<project>_Tracker]]"
    ),
}
