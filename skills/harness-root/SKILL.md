---
name: harness-root
description: Rank-0 duties in an Agent Workstream Harness — apply document change requests as old-to-new pairs, write the single rulings file, own the manifest, guards and the global scope registry. Load only when the harness skill's whoami reports harness-root for this session. Covers applying T5 requests, T9 rulings, and ownership of the guard and scope machinery.
---

# Root — rank 0 only

Spec: `~/.claude/skills/harness/ref/spec.md` — one copy, shared by all four
harness skills. Every rule below has a heading there. If you already read it
this session under another role, do not read it again: it is the same file.

You are the only writer of documents in the tree, and you also act as a lead:
`harness-downward` applies to you in full. This skill covers only what is yours
alone.

## Applying a document request (`T5`)

A request arrives as an exact old→new pair with a rationale and a pinned base.

- Apply it literally. If `old` no longer matches, **refuse and return it.** That
  refusal is the feature — the alternative is a three-way merge of a document
  nobody read.
- The pair has been reviewed once per rank on the way up. You are the last
  reviewer, not the first.

## Rulings (`T9`)

One rulings file. Leads submit; you write. A ruling *is* a document change and
uses the same channel — there is no second mechanism.

Most conflicts must not produce a ruling. Only two things should reach you:
missing intent, and a repeat scope defect. If rulings are arriving routinely, the
filter below `T7` is not working.

## The manifest and the guards

You own `.harness/manifest.json` — the document and code globs, and the check
definitions. **A check cannot be registered without stating what it cannot see.**
That required field is what makes "report all three" enforceable rather than
aspirational.

You own the three hooks. They must be POSIX `sh` with an explicit `exit 0`:

| hook | coverage |
| --- | --- |
| `pre-commit` | catches a document edit as it is authored. Blind to merges. |
| `pre-merge-commit` | fires on a real merge. **Silent on every fast-forward.** |
| `reference-transaction` | fires on every ref move. The one that has to survive. |

Because every upward integration is a fast-forward by design, the second hook is
silent on the path documents would actually take. Treat the third as primary.

**A non-zero exit from `reference-transaction` gives `fatal: ref updates aborted
by hook` and the repository stops accepting any ref update.** A crashing guard is
worse than no guard. Test every change to it against a scratch clone first.

Never set `core.hooksPath` to a relative path. A relative path that is missing on
a branch runs no hook, exits 0, and warns nobody.

## Verifying the guards you own

`harness doctor`, in each worktree, after any change to the hooks or the manifest.
It is the only instrument that proves a guard fires; everything else infers it.

Do not replace it with a check comparing `core.hooksPath` to an expected value.
Such a check goes red **because** the harness is correctly installed, and the
remedy it prints disarms every worktree at once while reporting success.

## The scope registry (`I3`)

One registry for the whole tree, not per lead. No two open tasks anywhere may
claim the same path. This is what makes textual conflicts rare rather than
routine, and it is cheaper than any resolution protocol.

What remains after it is semantic conflict — a changed signature a caller
elsewhere depends on. That produces no merge conflict at all and is caught by
checks at integration, not by git.

## Guards do not travel — there is one copy

`core.hooksPath` is absolute and points at `.harness/hooks` in **your** worktree.
Every worktree in the tree resolves to that same copy, and the guard reads the
tree and manifest from there too. Nothing rides down, so no branch is ever
running unguarded while it waits for a merge.

The cost is that you cannot test a guard change on one node first: an edit here
takes effect everywhere the moment you save it, and a broken manifest stops every
worktree at once. **Test every change against a scratch clone before saving it.**

## Shrinking the tree (`R3`)

A node is recorded in three places: `.harness/tree.json`, which travels;
`index.json`, which is derived and can be thrown away; and `locks/*.lock`, the
claims, which are closed rather than deleted. Adding a node touches the first.
Removing one touches all three, and only the first announces itself.

```bash
harness trim <node>... --dry-run   # the plan, and every refusal
harness trim <node>...             # worktree, branch, tree, index, claims
harness trim                       # no names: reconcile the stores only
```

It refuses before it deletes anything, and it collects **every** refusal first —
an occupied node, a dirty worktree, a child you did not name, a commit the
parent does not already hold, or a roster it could not read. A trim that removed
three of six nodes and then stopped would leave a state no store describes.

It is yours alone. `tree.json` is a document in your worktree, so a lead running
this would write into your checkout and the guard would refuse the commit a
moment later anyway.

Two things it deliberately leaves you. The tree edit is **staged, not
committed** — it prints the commit line, and the commit is a document change you
make on purpose. And a worktree or branch belonging to no node is reported and
not touched, because deleting one nobody declared is a guess.

`--force` overrides the dirty and containment refusals and prints the sha it is
about to orphan, which is the only route back. Nothing overrides occupancy.

## Grants (`I11`)

A member writes inside its worktree and nowhere else. When one needs a path
outside the repository it raises a record, and clearing that record is yours or
the operator's — never a lead's, and never by doing the write on the member's
behalf.

```bash
harness needs                              # every project on the machine, anywhere
harness blocked --list                     # this project only
harness grant <node> <path> --reason "..."  # append-only, records who and why
harness grant --list                        # live and revoked
harness grant <node> <path> --revoke        # stays on the record
```

Grants live in `~/.claude/harness/<slug>/grants.json`, beside the binding.
**Never in `tree.json`** — the tree is a document you edit, so permissions there
would be permissions you could widen for yourself, and they would travel by merge
to machines whose owner never agreed to them.

They take effect at the next spawn or recycle, as `--settings` and `--add-dir` on
the `claude` command line. A running session keeps what it started with, so a
grant never changes what a lane can do mid-task, and a revoke does not either.

Two things worth holding onto. The CLI cannot tell you from the operator: your
grants and a human's differ only in the `granted_by` field, which is why every
one carries it. And a grant made quickly for one task outlives that task — it
persists for everything that node does afterwards, and once nobody remembers why
it exists, nobody removes it. Grant the **path**, record the reason, and revoke
it when the task that needed it closes.

## Being told rather than looking

`harness needs` is the operator's queue, not yours to clear — but you will often
be the one who notices it is not empty. It runs from anywhere, including outside
a repository, and prints the `grant` and `recycle` lines already written out.

Nothing polls, because nothing is running to poll (`R4`). A block notifies at the
moment it is recorded or not at all, through three surfaces: the operator's own
`~/.claude/harness/notify` hook if one exists, the statusline badge in every
session they have open, and `harness needs` when they ask.

If they have no notifier, say so once and move on — the record is written either
way, and the badge shows it. The hook is theirs to write, not yours to install:
it is run with `HARNESS_SUMMARY`, `HARNESS_COUNT` and `HARNESS_JSON` in the
environment, and what it does with them depends on a machine you are not on.

## Seeing all of it at once

```bash
harness gui                    # 127.0.0.1:8791, opens a browser
harness gui --port 9000        # a port of your own: honoured exactly, or refused
harness gui --once             # the JSON it would serve
```

The default walks upward if 8791 is busy and says which port it landed on. An
**explicit** `--port` never wanders — if you named one, being quietly moved is
worse than being told. 8787 is RStudio Server's and 8888 is Jupyter's, which is
why neither is the default.

Every tree on the machine as one indented list: busy, idle, or no session; the
open task or `unassigned`; and a clickable attention panel that expands to the
exact `grant` and `recycle` lines.

**It serves the page it loaded at startup.** After the viewer is updated, a
browser reload changes nothing — stop it and start it again. It says so itself:
a red banner appears when the file on disk is newer than the running process.

It is a **viewer**. It never claims, writes or decides, so killing it changes
nothing — which is what keeps `R4` true. It is also a prototype with no
authentication, so it binds loopback only; it shows worktree paths, session
names and every open block, and none of that should leave the machine.
