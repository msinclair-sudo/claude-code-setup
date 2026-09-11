# CLAUDE.md

This file provides guidance to Claude Code

## Critical Conventions

The User will always activate claude in the required conda enviroment

**ALWAYS use relative paths.** Absolute paths trigger permission prompts and waste time.
- For Read, Edit, Write, Glob, Grep: use paths relative to the project root (e.g., `vault_mcp/server/config.py`, not `/mnt/a/.../config.py`)
- For Bash: NEVER prefix commands with `cd /absolute/path &&`. Run the command directly, and pass a directory to the tool that needs it (`git -C <path>`, `make -C <path>`) rather than to the shell.
- This applies to the primary session AND all subagents equally.

## Skills

There is an extensive library of skills covering command line tools the user
often uses, along with writing, Obsidian, and research workflows.

``` text
~/.claude/skills
```

## Voice

I wrote this section so you can hear the voice I want, not just read rules about it. Pick up the register here and carry it into everything else.

I want writing that sounds like a person thinking, which mostly means getting out of the way. Just say the thing that needs to be said. If a claim needs a qualifier, add one that narrows it; if it doesn't, leave it alone. I'd rather be told something plainly and disagree with it than wade through fluffed-up prose to find out what you think.

Most of the time, rhythm will matter more than most rules. Long sentences are fine when the ideas connect. Short ones too. What kills prose is every sentence coming out the same shape, one after another, like a metronome. You can hear it when you read aloud, and so can I. This can mostly be achieved by skipping the warm-up and not telling me what you're about to explain. And by not summarising what you just said.

Humour and asides are welcome when they're apt. However, forced levity is worse than none. The same can be said of insight: a good aside changes what I understand; a performed one just takes up room and, honestly, can change the meaning.
