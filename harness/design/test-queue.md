# Test queue — scope and decisions

Status: built 2026-10-06.

## Why

On 2026-10-05 biblion2 stalled the machine (load 11.7 on 12 cores) and the owner had main stop
everything. Harness log entries 80 and 81:

- Nothing limited concurrent test runs: up to 5 runs and 16 test modules at once. A full
  `harness check` is about an hour (8 modules, serial).
- Every run read the same live `subset.db` and copied 650 MB subsets into `/tmp`; scratch reached
  4.7 GB, and an earlier out-of-disk crash followed (entry 78 is the clean-up).
- `harness stop` ended sessions but not their processes; kills did not pass down a layer.
- Entry 79: a check's `reads` was typed into the manifest and drifted from the project's own list.

The owner: "tests should be handled by a typical scheduler, not a session. Tests are submitted to the
scheduler, so we're not trying to run multiple tests of the same things in different places all
together. The test node doesn't need a session. It just takes the jobs, copies the worktree, runs the
tests, reports and tears down, removing everything it built. This helps keep the database usage
smaller, and stops us from having multiple tests running at once."

## Decisions (owner, 2026-10-06)

1. One run at a time, per project.
2. Lanes may still run a single test file directly while developing; modules, the suite and sweeps
   go through the queue.
3. Copies live on the Linux disk: `~/.cache/harness/runs/<project>/<job>/`.
4. Strict first in, first out.

## How it works

- `harness check` refuses a dirty worktree, then queues a `check` job for HEAD, joins a queued or
  running job for the same commit, or reuses a finished report (`checks/<sha>.json`) for the asking
  node. It returns at once; the requester's doorbell rings with the result. `--wait` blocks;
  `--again` forces a fresh run; `--report <sha>` reprints one.
- `harness test -- <command>` queues any command (a mutation sweep, a probe) the same way.
  `harness test` lists the queue, `--cancel <id|all>` and `--log <id>`.
- The runner, `harness testd`, is a plain detached process, one per project (`testq/runner.lock`,
  flock). Submit starts it; it exits after two quiet minutes. Each job: check 5 GB free, `git worktree
  add --detach` at the commit, the manifest's `test_setup` if any, the arms with `TMPDIR` inside the
  run folder, the report to the commit and to every requester, doorbells rung, then `git worktree
  remove` and the run folder deleted.
- Each job holds `testq/slot.lock`; `harness slot -- <cmd>` takes the same slot, for a project's own
  runner.
- `kill_tree` reads the process tree from `/proc` before anything dies and kills every group and
  pid, so a child that `setsid`s out of the group dies too. Timeouts, `test --cancel` (SIGUSR1 to the
  runner: that job ends, the runner goes on), the runner's SIGTERM and `harness stop` all use it.
- A check's `reads_from` command widens its `reads` for holds.
- The GUI's tests card shows the running job (requesters, commit, arm, elapsed) and the queue.

## Left to the project

biblion2's manifest is rank 0's: it adds `test_setup` (build `surface/build/`, which git does not
track) and, if `tests/run.py` grows a `--print-reads`, `reads_from` on each arm.
