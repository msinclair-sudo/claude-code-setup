# CLAUDE.md

This file provides guidance to Claude Code

## Critical Conventions

The User will always activate claude in the required conda enviroment

**ALWAYS use relative paths.** Absolute paths trigger permission prompts and waste time.
- For Read, Edit, Write, Glob, Grep: use paths relative to the project root (e.g., `michaels_setup/server/config.py`, not `/mnt/a/.../config.py`)
- For Bash: NEVER prefix commands with `cd /absolute/path &&`. The shell already starts in the project root. Just run the command directly.
- This applies to the primary session AND all subagents equally.

## Skills

There is an extensive library of skills to learn how to use comand line tools the user often uses

``` text
~/.claude/skills
```
