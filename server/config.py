"""
Configuration constants for the Obsidian Vault MCP Server.
"""

import os
from pathlib import Path

VAULT_ROOT = Path(os.environ.get("VAULT_ROOT", "/path/to/your/Obsidian Vault"))
