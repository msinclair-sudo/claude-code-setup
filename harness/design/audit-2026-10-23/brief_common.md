# Harness audit: common brief (read this whole file first)

## What this is

The Agent Workstream Harness is a CLI that runs a tree of Claude Code sessions on one git project:
rank 0 ("main"), leads, and lanes. Its source is in the nested git repo `setup/`. All paths
below are relative to the working directory `/mnt/a/OneDrive - Charles Sturt University/PhD/apps/mcp`.
- `setup/harness/bin/harness`: the CLI, one Python file, 27,353 lines, 859 functions, about 65
  subcommands. The argparse setup is near the end (from about line 26640).
- `setup/harness/bin/harness-gui` (4,505 lines) and `setup/harness/bin/harness-mail` (268 lines).
- `setup/harness/tests/test_harness.py` (10,877 lines, 592 tests). It loads the CLI in-process
  as module `hz`.
- Skills: `setup/skills/harness*/SKILL.md`, and the spec at `setup/skills/harness/ref/spec.md`
  (241 KB) with `ref/why.md`. Templates are in `setup/harness/templates/`.
- The fault log is `~/.claude/harness/OBSERVATIONS.md` (2,961 lines, 367 KB). Don't read it
  whole: grep for the entry numbers you need.
- The live project is biblion2. Its state is in
  `~/.claude/harness/-mnt-a-OneDrive---Charles-Sturt-University-PhD-apps-biblion2/`, and its
  transcripts are in `~/.claude/projects/*biblion2*/`.

The harness grew one observation-log fix at a time. It works. The owner wants to know where it
has become a mess, so they can keep it working and maintainable: redundant code, superseded
mechanisms, and too much prompt or context text for sessions. **This is stage 1: a ranked
report. Nothing is changed.** The cuts come later, on small branches, each passing the suite.

## Rules

- **Read-only.** Don't edit any file in the repo or under `~/.claude/`. Don't run any `harness`
  command against biblion2's live state, and don't write into it. The only place you may write
  is your findings file (below).
- **Use relative paths** for files under the working directory. Don't `cd`.
- You may run single tests:
  `python3 -m unittest discover -s setup/harness/tests -k <name>`.
  Don't run the full suite. Two failures are already known; don't report them:
  `Log191to194.test_a_wait_on_a_harness_fix_is_owed_by_nobody` depends on the CLI file's mtime,
  and `TestQueue.test_priority_goes_first_and_a_lead_promotes_a_lane_job` is flaky under load.
- Before you start, read `setup/harness/skills/ponytail-audit/SKILL.md` and
  `setup/harness/skills/ponytail/SKILL.md`, and audit in their spirit. One counterweight
  matters here: most of this code exists because something went wrong in a live run. Code that
  looks odd may be a fix. Look up its log entry before calling it a cut. If a test pins the
  behaviour, the cut needs the owner's call, not yours.

## Data prepared for you (in `/home/rabbit/.claude/jobs/23c30c1a/tmp/`)

- `cov_A.txt`, `cov_B.txt`, `cov_C.txt`, `cov_D.txt`, `cov_gui.txt`, `cov_mail.txt`: never-run
  lines by function, from coverage over the full suite. "NOT RUN" means the suite never
  executes the function at all. Overall, the suite reaches 71% of `harness`, 34% of the GUI
  and 84% of mail.
- `static.txt`:
  - functions referenced nowhere but their own def, with counts of references from the tests
    and the GUI;
  - functions with exactly one caller in the CLI.

  Every flag's value is read somewhere, so there are no dead flags in that sense.
- `usage.txt`: how often live biblion2 sessions ran each subcommand, and each subcommand+flag,
  from Bash tool calls in 1,023 transcripts. Caveats:
  - Hooks and daemons run some commands, not Bash calls: `hook-*`, `testd`, `researchd`,
    `ringer`, `doorbell` run by `harness-mail`.
  - The owner runs some from their own shell: `halt`, `resume`, `unenrol`, `archive`, `enrol`,
    `scaffold`.
  - `answer`, `gate`, `lock`, `pause` are nested sub-subcommands.

  So a zero is evidence, not proof.
- `logmap.txt`: every `log N` citation in the CLI, by line, with that entry's heading. Use it
  to spot a mechanism a later entry replaced, or two entries patching the same rule in two
  places.

## What to look for

1. **Dead:** code nothing calls, or that only tests reach and no live path does.
2. **Duplicate:** the same rule written in more than one place. For example, the same skip
   condition copied into three owed/nag functions, or two helpers computing the same thing. You
   may name helpers outside your slice by name and line.
3. **Superseded:** an older mechanism a later log entry replaced, which still runs or still
   exists.
4. **Overgrown:** a function far longer than its job, special cases stacked up, a branch per
   log entry where one general rule would do.
5. **Unused surface:** subcommands or flags nobody uses, per the usage data and the skills.
6. **Text:** messages the CLI prints or rings to sessions that are long, repeated, or say
   internals (each one costs a session tokens).
7. **Bug:** a correctness or safety bug you meet along the way. Report it, but don't go
   hunting for them.

## Shape of every finding

```
### <n>. <one-line claim>
- where: <file:line[-line]>
- category: dead | duplicate | superseded | overgrown | unused-surface | text | bug
- cut: <what to delete, merge or rewrite, concretely>
- saves: <about N lines> and/or <about N tokens per session/turn/ring>
- guarded by: <test names that pin this behaviour, or "no test">
- log: <entry numbers behind this code, or none>
- risk: safe (the suite would catch a mistake; no test needs changing) | owner's call (a test or documented behaviour would change) | unsure
- evidence: <one or two lines: coverage, usage count, the two places that duplicate, etc.>
```

Rank by value: biggest saving at lowest risk first. At most about 40 findings. Quality beats
count. Put every claim to the check of the code itself, not just the data files: a "NOT RUN"
function may be reached through `getattr` or a string dispatch, and a grep miss may be a
dynamic name.

## Output

Write your findings to `/home/rabbit/.claude/jobs/23c30c1a/tmp/findings_<YOUR LETTER>.md`. It
starts with:
- a three-line headline: the biggest wins in your slice;
- the findings;
- a short "not read / not sure" section.

Then return the same content as your final message. No file dumps: quote at most a few lines of
code when a claim needs it.
