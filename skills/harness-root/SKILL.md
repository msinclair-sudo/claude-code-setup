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
