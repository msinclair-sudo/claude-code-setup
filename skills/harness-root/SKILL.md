---
name: harness-root
description: Rank-0 duties in an Agent Workstream Harness — apply T5 document requests, write T9 rulings, own the charter, manifest, guards, grants and scope registry. Load only when the harness skill's whoami reports harness-root for this session.
---

# Root — rank 0 only

You are the only writer of documents in the tree, and you are also a lead: `harness-downward` applies to you in full. This covers what is yours alone.

## The charter

```bash
harness charter                                  # read it
harness charter --write "..."                    # what this project is for
harness charter --feature "<name>" --write "..." # one feature, in scope
harness charter --feature "<name>" --move up     # order is yours; new ones go last
harness charter --feature "<name>" --demote      # file under the one above; --promote lifts it out
harness charter --feature "<name>" --delete      # gone, with any sub-features
```

Prose: what the project is for, who its output is for, what each feature is. It says what and why; a brief says how and done. Check there is a charter before you write briefs. Every brief must trace to a feature; work that doesn't is either a missing feature (take it to the operator) or not this project's (don't brief it).

Draft it from what the operator told you, mark what you inferred or guessed, and let them correct it in `harness gui`. Never draft it from the state of the repository. A feature that leaves scope is deleted outright. Order features in the order someone should meet them, two levels at most.

## Focus

When the operator names a priority, set it: `harness focus <task>... --why "…"` (several tasks, or a quoted glob such as `'enrich*'`; split parts follow their segment). `--add`/`--remove` edit it, `harness focus` shows it, `--clear` ends it. Nags about other work fold into one line; queues are labelled, never filtered, so there is no need to list a lane's out-of-focus tasks in it. Setting it prints the queued work it leaves out.

## Briefs (`T1`)

You write your own briefs and your children's, never a grandchild's (tell the lead instead).

```bash
harness brief <task> --write "..."              # your own
harness brief <task> --for dev --write "..."    # your child's
```

A brief is rewritten in place; `harness note` is the append-only half. Write a segment for the rank below, not a task list, and write everything you know in one go. A finding you have ruled on in a document closes with `harness finding <name> --ruled "<commit>"`; one that should become work goes down with `--to <lead>`, and the lead's brief from it is born approved.

## Approving briefs

`harness brief <task> --approve`, or `--decline "why"` (the why is required). Orientation lists pending approvals; they are yours. Decide sparingly; declining costs one line. Approving a brief you asked for records `self_approved`. When one matters, put it to the owner instead.

## Priority

`harness queue dev_1 --order doi-index,ingest-2024 --why "…"`. You may order any node's queue. Every reorder needs `--why`. A lead may override you with a reason; read the queue after reordering.

Make a condition structural, not a note: a note does not stop a close or a check. `harness brief <segment> --close-after <task>` refuses `mark --close` until that task is signed off; `--not-before <UTC>` holds a start on a clock and starts the lane when it passes; no session cron is needed. `harness hold <path> --why "..." [--until <task>]` makes every `check` arm that reads a shared resource print `NOT RUN (held: …)` while a job holds it.

## Asking the owner

Use `harness ask` (see `harness-downward`), as leads do. When the owner is in your session, asking them directly is fine; record the answer where it is used (a brief, a fact or the charter). Do not use a block for a question: a block means "I cannot reach X".

**Commands the owner must run** (a login, an install, a permission rule, anything outside your reach) go out as one action ask on your standing task `owner`, never as chat text the owner has to find:

```bash
harness ask owner --kind action --question "Install the pinned x before the import runs?" \
  --run "pip install x==1.2" --run "harness grant ..."
```

Each open item gets its own intermediary session, and the commands show in the owner's Issues tab at once. Carry on, or end your turn: when the owner clicks **Done** your doorbell rings with their note. If the intermediary needs something from you it rings your doorbell too (orientation also says so): answer with `harness ask <id> --msg "..."`, never `SendMessage`, because the item's session may be asleep. The same `--msg` adds anything to an open item later.

## Blocks: comments and closing them

Operator comments on any block come to you, not the lane. `whoami` reports unread ones.

```bash
harness blocked --list                      # every open block, with its thread
harness blocked <need> --comment "..."      # reply into the thread
harness blocked --decided                   # answered: unlinked, and in hand with task state
harness brief <task> --for dev --from-block "<need>" --write "..."
harness blocked "<need>" --task <task>      # link an existing task; repeatable; closes it
harness blocked "<need>" --resolve --task <task>
harness blocked "<need>" --no-task "why it produced none"
```

Convert the discussion into a grant, a `T9` ruling or a brief; never relay the thread. An answered block is yours to close, anywhere in the tree. `--resolve` refuses an operator-answered block that names neither `--task` nor `--no-task`. If the task exists, link it rather than writing it twice. Brief the whole of what the answer unblocked to your lead and let it split. Comments on a brief go to the lead who writes it.

## Applying a document request (`T5`)

The documenter (`T18`) keeps the markdown, and you review every batch it submits: `harness pairs <task>` shows the diff and marks it read, then `harness pairs apply <task>`, or `harness pairs <task> --decline "why"`. Orientation and your Stop hook name a batch that has waited five minutes; a chain of runs waits on your decision. `CLAUDE.md` has a word budget (`claude_md_words` in the manifest) that `pairs apply` enforces on every pairs batch; your own direct edits are not checked, so keep to it.

`harness pairs <task>` shows a submitted batch; `harness pairs apply <task>` re-checks every pair, applies all or none, prints the context around each change (read it for a now-stale neighbouring sentence), and makes one commit with a `Task:` trailer. A refusal names the decayed pair: return it with `harness note`.

## Rulings (`T9`) and the scope registry (`I3`)

One rulings file; leads submit, you write, through the same channel as `T5`. Only missing intent and repeat scope defects should reach you; routine rulings mean the filter below `T7` is failing. One scope registry for the whole tree: no two open tasks anywhere may claim the same path.

## The manifest and the guards

You own `.harness/manifest.json`: document and code globs, and checks. Checks run from a queue in a fresh copy of the commit, not where the worktree was. The harness has no tests and no setup step of its own: anything git doesn't track and a check needs (a built client, say) is built by the check's own command. A test that needs a neighbouring checkout finds it from `$HARNESS_TEST_ORIGIN`, and copies it makes belong under `$HARNESS_TEST_SCRATCH`, which is deleted after the run. A check may declare `"reads_from": "<command>"`, printing one path per line, so holds use the project's own list of what it reads rather than a typed copy (obs 79). A check cannot be registered without stating what it cannot see. A check may carry `"timeout": <seconds>`; a timeout reports `NOT RUN (timed out)`.

The three hooks are POSIX `sh` with an explicit `exit 0`:

| hook | coverage |
| --- | --- |
| `pre-commit` | a document edit as authored; blind to merges |
| `pre-merge-commit` | real merges; silent on every fast-forward |
| `reference-transaction` | every ref move; the primary guard |

A non-zero exit from `reference-transaction` gives `fatal: ref updates aborted by hook` and the repository stops accepting ref updates. `core.hooksPath` is absolute into your worktree, so there is one copy and every edit takes effect everywhere on save: test every hook or manifest change against a scratch clone first. Never set `core.hooksPath` to a relative path, and never add a check comparing it to an expected value.

Run `harness doctor` after any hook or manifest change; on your node it also runs doctor in each child's worktree. It proves the document guard refuses and allows; for other hooks it only proves they match the installed template. The integration gate has no watched refusal.

Drift repair is yours alone; `harness scaffold` refuses below rank 0. Read the diff first, check what it did to `.claude/settings.json`, then commit the hooks.

## Grants (`I11`)

A member writes only inside its worktree. Clearing a reach request is yours or the operator's, never a lead's, and never by doing the write for it.

```bash
harness blocked --list                      # this project only
harness grant <node> <path> --reason "..."  # append-only, records who and why
harness grant --list                        # live and revoked
harness grant <node> <path> --revoke        # stays on the record
```

Grants live in `~/.claude/harness/<slug>/grants.json`, never in `tree.json`. They apply at the next spawn or recycle. Grant the path, record the reason, revoke it when the task closes. A grant does not clear Claude Code's permission classifier: when the owner authorises a class of live write, the route is a project permission rule the owner adds, named in the grant's reason.

## Cleaning up

When a split segment closes or the focus completes, orientation says `N complete unit(s) await a cleanup decision`. Read `harness sweep <unit> --dry-run` (or `--all --dry-run`), then decide: `harness sweep <unit> --why "..."` gzips the unit's lane transcripts into the archive, deletes their job `tmp/`, folds the unit's briefs, marks and notes into one archive file and prunes dead caches; `--keep --why` declines. Before a deletion list goes to the owner, run it through `harness cited <path>...` (`--deletable` prints only what no open record needs): `sweep` protects only what the harness deletes. Only paths protect: a file a record names (a jobs path, or `$CLAUDE_JOB_DIR/tmp/<file>` resolved through its author) is kept, file by file. `harness sweep --sessions --dry-run` lists ended sessions still on Claude Code's list; with `--why` it `claude rm`s them (transcripts stay), except those whose job folder a record cites. `harness sweep --stale --dry-run` offers closed findings and uncited facts older than 14 days; folded, they stay readable by name. Every decision goes to the ledger; `harness archive [<unit> [task]]` reads it back, and archived tasks still read as closed.

## Shrinking the tree (`R3`)

```bash
harness trim <node>... --dry-run   # the plan, and every refusal
harness trim <node>...             # worktree, branch, tree, index, claims
harness trim                       # no names: reconcile the stores only
```

It collects every refusal before deleting anything: occupied node, dirty worktree, unnamed child, a commit the parent lacks, unreadable roster. `--force` overrides dirty and containment (it prints the sha it orphans); nothing overrides occupancy. The `tree.json` edit is staged, not committed: commit it yourself. Worktrees or branches belonging to no node are reported, not touched. When `whoami` reports open task records naming no node in the tree, `harness trim` closes those naming a trimmed node; close ones naming no node with `harness mark <task> --close --force`. Don't guess an owner.

## Recycling the lead

You are never recycled; everything under you starts cold. You compact at `--autocompact 500k`; add `~/.claude/harness/templates/compact-instructions.md` to the project `CLAUDE.md` once, so a compaction keeps what lives only in context. Recycle `dev` when it is waiting with nothing in flight (`harness recycle --idle`; `--cold` for sessions past the cache lifetime). If recycling would lose something, the lead was holding state that belongs in a record: write it there.

## Seeing it all

```bash
harness gui                    # 127.0.0.1:8791, walks upward if busy
harness gui --port 9000        # exact, or refused
harness gui --once             # the JSON it would serve
harness note <task-id>         # brief, opener, comments
harness note <task-id> --add "…"
```

The viewer never writes. After it is updated, restart it (a red banner says so). Loopback only. Use a comment, not a message, for anything the next occupant of a node needs.

On demand only: the spec, `~/.claude/skills/harness/ref/spec.md`, and why each rule exists, `ref/why.md`.
