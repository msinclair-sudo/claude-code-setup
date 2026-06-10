#!/usr/bin/env python3
"""PreToolUse hook: clean up unnecessary absolute paths in Bash commands.

Two rewrites:
1. Strip redundant `cd "/cwd" &&` prefixes
2. Replace absolute paths to cwd (or subdirs of cwd) with relative equivalents
"""
import json, sys, os, re

def main():
    data = json.load(sys.stdin)
    tool_input = data.get("tool_input", {})
    command = tool_input.get("command", "")
    original = command
    cwd = os.getcwd()

    # 1. Strip redundant cd to cwd
    m = re.match(r'^cd\s+["\']?([^"\'&]+?)["\']?\s*&&\s*', command)
    if m and os.path.normpath(m.group(1).strip()) == os.path.normpath(cwd):
        command = command[m.end():]

    # 2. Replace absolute cwd paths with relative equivalents
    # Match quoted paths: "/mnt/a/long path/..." or '/mnt/a/long path/...'
    # and escaped paths: /mnt/a/long\ path/...
    norm_cwd = os.path.normpath(cwd)

    # Handle quoted absolute paths (double or single quotes)
    def replace_quoted(m):
        quote = m.group(1)
        path = m.group(2)
        norm = os.path.normpath(path)
        if norm == norm_cwd:
            return quote + "." + quote
        if norm.startswith(norm_cwd + "/"):
            return quote + os.path.relpath(norm, cwd) + quote
        return m.group(0)

    command = re.sub(r'(["\'])(' + re.escape(cwd) + r'[^"\']*)\1', replace_quoted, command)

    # Handle backslash-escaped spaces in unquoted paths
    escaped_cwd = cwd.replace(" ", r"\ ")
    if escaped_cwd in command:
        def replace_escaped(m):
            path = m.group(0).replace(r"\ ", " ")
            norm = os.path.normpath(path)
            if norm == norm_cwd:
                return "."
            if norm.startswith(norm_cwd + "/"):
                rel = os.path.relpath(norm, cwd)
                return rel.replace(" ", r"\ ")
            return m.group(0)

        # Build pattern matching the escaped cwd and any path continuation
        pat = re.escape(escaped_cwd).replace(r"\\\ ", r"\\ ") + r'[^\s|;&)]*'
        command = re.sub(pat, replace_escaped, command)

    if command != original:
        result = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "updatedInput": {"command": command}
            }
        }
        json.dump(result, sys.stdout)

if __name__ == "__main__":
    main()
