# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "fastmcp>=0.4.0",
#   "pydantic>=2.0.0",
# ]
# ///
"""
Obsidian Vault MCP Server
Provides guarded read/write access to the Obsidian vault with enforced naming,
tagging, and placement conventions.
"""

from fastmcp import FastMCP

from tools import read, write

mcp = FastMCP(
    "obsidian-vault",
    instructions=(
        "Use these tools to read from and write to the Obsidian vault. "
        "Read tools (vault_search, vault_read, vault_list, vault_tags) are unrestricted. "
        "Write tools (vault_create_note, vault_append, vault_rename) are guarded — all writes "
        "go to claude_doc_dump/ directories only and require at least one primary tag and at "
        "least one destination wikilink. Use vault_rename to rename a note and propagate the "
        "change to all wikilinks across the vault. "
        "Every new note body should include a > [!abstract] Note Role callout with four fields "
        "in this order: Contains, Cannot contain, Points to, Pointed to by. "
        "The callout title must be 'Note Role' — never 'Summary'."
    ),
)

read.register(mcp)
write.register(mcp)

if __name__ == "__main__":
    mcp.run()
