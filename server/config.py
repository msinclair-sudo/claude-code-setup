"""
Configuration constants for the Obsidian Vault MCP Server.
"""

import os
from pathlib import Path

VAULT_ROOT = Path(os.environ.get("VAULT_ROOT", "/path/to/your/Obsidian Vault"))

ALLOWED_PRIMARY_TAGS = [
    "Writing", "Code", "Tracker", "Methods", "Todo",
    "Scripts", "Theory", "Issues", "PhD", "Life",
]

ALLOWED_PLACEMENT_DIRS: dict[str, list[str]] = {
    "Literature Review": ["PhD/Literature Review/claude_doc_dump"],
    "mtDNA":             ["PhD/mtDNA/claude_doc_dump"],
    "Evolution theory":  ["PhD/Evolution theory/claude_doc_dump"],
    "Hazelnut Project":  ["PhD/Hazelnut Project/claude_doc_dump"],
    "scripts":           ["scripts/claude_doc_dump"],
    "Notes to process":  ["Notes to process/claude_doc_dump"],
}

# Flat set of all valid placement paths for fast lookup
ALL_VALID_PLACEMENTS: set[str] = {
    p for paths in ALLOWED_PLACEMENT_DIRS.values() for p in paths
}
