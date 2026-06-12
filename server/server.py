# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "fastmcp>=0.4.0",
#   "pydantic>=2.0.0",
# ]
# ///
"""
Obsidian Vault MCP Server
A lightweight, general-purpose bridge to an Obsidian vault: unrestricted reads
plus unguarded writes (create/overwrite, append, rename). No naming, tagging, or
placement enforcement — tags are suggested via tool descriptions, never required.
"""

from fastmcp import FastMCP

from tools import read, write

mcp = FastMCP(
    "obsidian-vault",
    instructions=(
        "Use these tools to read from and write to the Obsidian vault. All tools "
        "operate relative to VAULT_ROOT — you never need the absolute vault path.\n\n"
        "Read tools are unrestricted. Write tools (vault_write, vault_append, "
        "vault_rename) can write anywhere in the vault. When creating a new note, "
        "include YAML frontmatter with at least one tag so it is discoverable:\n\n"
        "    ---\n"
        "    tags:\n"
        "      - MyTag\n"
        "    ---\n\n"
        "Use vault_search_tags for boolean tag filtering, vault_wikilinks to inspect "
        "a note's link graph, and vault_rename to rename/move a note and propagate "
        "all wikilinks across the vault."
    ),
)

read.register(mcp)
write.register(mcp)

if __name__ == "__main__":
    mcp.run()
