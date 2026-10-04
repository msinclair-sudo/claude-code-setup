# Timed tasks — scope

Agreed with the owner 2026-10-05. Not built. This file is not installed. It grew out of entry 70: a
live job had to start no earlier than an external provider's 00:05 UTC reset, and the harness had
nothing that could start it then.

## What it is

A lead writes a task with a start time:

```bash
harness brief enrich-live-runs --for dev --at 00:05Z [--window 2h] [--worktree] --write "..."
```

At that time the harness creates a **temporary node** under the lead, starts a session on it, and
that session works this one task. What the lead's other lanes are doing doesn't matter: the timed
task has a node of its own. It presents to the lead like any lane. When the lead signs it off, the
node is retired.

`--not-before` (shipped in `6cf7524`) covers "may not start before". `--at` covers "starts then, on
its own node".

## Two kinds, declared by the lead

| | job (default) | code (`--worktree`) |
| --- | --- | --- |
| for | running or watching something: a live import, a measurement, a nightly check | changing files that get integrated |
| where | a scratch directory, with read access to the lead's worktree | its own branch and worktree, cut from the lead's branch at spawn |
| leaves | its report, notes and facts on the task | commits the lead integrates by fast-forward |
| retiring | session stopped; scratch swept | as a job, plus the worktree and branch removed after integration |

The harness does not guess the kind. From a brief's text it can't tell whether the work will need to
commit, and either wrong guess costs something.

## Who

- **May create one:** leads and rank 0. A lane may *ask* for one, through the existing route
  (`harness finding <name> --to <lead> …`, or its report). The lead decides and writes the brief.
- **The node:** named after its lead and task, e.g. `dev.job-enrich-live-runs`. It is recorded in
  the harness state, not in `tree.json`, because a lead can't edit the tree and the node lives for
  hours. It claims a lock like any node, so I1 (one session per node) holds. `status`, `queue` and
  the GUI show it as temporary.
- **If the lead isn't running at the time,** the node spawns anyway. The task is on the lead's
  record, and whoever occupies the lead next signs it off.

## Firing

Nothing in the harness runs between turns (R4), so there are two paths:

1. Writing the brief starts a detached process that sleeps until the time, then spawns the node.
2. If that process is lost (a reboot, WSL shutting down), the next harness command anywhere in the
   tree notices the overdue task and spawns it.

**`--window` (optional).** If the spawn would happen after `at + window`, it does not. The task is
marked **missed**, and the lead's orientation says so: `missed enrich-live-runs: window closed
02:05Z — re-brief with a new --at`. Without `--window`, a late task fires whenever it's noticed.

`status` shows each timed task as `scheduled 00:05Z`, then `launched 00:05`, `late (launched
07:40)` or `missed`.

## Access

A live job usually needs reach beyond a worktree (a live database, a data directory). Today grants
attach to a node, and a temporary node doesn't exist until spawn. So this folds in entry 61:

```bash
harness grant --for-task enrich-live-runs <path> --reason "..."
```

The grant attaches to the task. It applies to whichever node runs that task, at spawn or recycle,
and lapses when the task closes. That also fixes 61's original problem: a task boundary stripping a
lane's access, because the grant was attached to the node and its reason said "for task X" only in
prose.

## No runtime cap

Tasks are short and sessions already stop reliably at the end of one, so there is no `--for`
limit. Revisit if a timed session is ever seen running on.

## Still to settle in planning

- **How a job session gets its orientation outside the repo.** Its scratch directory needs the
  harness hooks, or the session starts blind. Option: write a `.claude/settings.json` there with the
  same hooks and `--add-dir` the lead's worktree.
- **The sleeper** writes its pid to the timed-task record, so `status` can tell scheduled-and-alive
  from lost.
- **Retiring** reuses `trim` for the code kind, and `sweep` collects the transcript and scratch
  space.
