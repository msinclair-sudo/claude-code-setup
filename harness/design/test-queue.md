# Test queue — scope and decisions

Status: built 2026-10-06; cut back the same day (entries 82–86).

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

## The harness has no tests (owner, 2026-10-06)

The first version built test knowledge in: it reused a finished report by commit (83: a stale green,
since biblion2's tests read live databases git doesn't hold), ran a `test_setup` for every job (85: it
failed on main's documents-only commits), and claimed to remove "everything it built" (86: only
`/tmp`; the 27 GB came from the project's own scratch paths). The owner: the harness shouldn't have
built-in tests. It manages git trees and task ordering, and provides the method for the codebase to
run its tests when there are multiple worktrees.

So the harness schedules runs, isolates them and delivers the results. The project owns what runs,
its setup, where its scratch goes, which arms a change needs, and whether an old result still holds.

## Decisions (owner, 2026-10-06)

1. One run at a time per project, from two queues: priority for integration (a lead's or rank 0's
   check), normal for lanes and `harness test` jobs. Each is first in, first out; priority goes
   first; a running job is never pre-empted.
2. Lanes may still run a single test file directly while developing; modules, the suite and sweeps
   go through the queue.
3. Copies live on the Linux disk: `~/.cache/harness/runs/<project>/<job>/`.
4. The manifest's checks list stays as the project's declaration: named commands with a timeout and
   a blind spot, run as given (the owner was unsure; kept so `mark --done` and `review` keep their
   per-arm reports).

## How it works

- `harness check` refuses a dirty worktree, then queues a job for HEAD in the priority queue (lead,
  rank 0) or the normal one (lane), or joins an identical job (same commit and arms) still queued or
  running. A finished report is never reused. Submit prints the expected wait from finished jobs'
  durations. It returns at once and the requester's doorbell rings with the result; `--wait` blocks;
  `--arms a,b` runs only the named arms (the report says partial); `--priority`/`--normal` override
  the queue; `--report <sha>` reprints one.
- `harness test -- <command>` queues any command (a sweep, a probe) in the normal queue. `harness
  test` lists the queue in run order with estimates; `--cancel <id|all>`, `--log <id>`.
- The runner, `harness testd`, is a plain detached process, one per project (`testq/runner.lock`,
  flock), started by submit, gone after two quiet minutes. Each job: check 5 GB free, `git worktree
  add --detach` at the commit, the arms with `HARNESS_TEST_ORIGIN`, `HARNESS_TEST_SHA`,
  `HARNESS_TEST_JOB`, `HARNESS_TEST_SCRATCH` and `TMPDIR` set (the last two inside the run folder),
  the report to the commit and every requester, doorbells rung, then the worktree removed and the run
  folder deleted.
- Each job holds `testq/slot.lock`; `harness slot -- <cmd>` takes the same slot.
- `kill_tree` reads the process tree from `/proc` before anything dies and kills every group and pid.
  Timeouts, `test --cancel` (SIGUSR1: that job ends, the runner goes on), the runner's SIGTERM and
  `harness stop` use it.
- A check's `reads_from` command widens its `reads` for holds (79).
- The GUI's tests card shows the running job and the queue in run order, priority marked, with
  estimates.

## Left to the project

biblion2's: drop `test_setup` from its manifest and build the surface client in that arm's own
command; put scratch copies under `HARNESS_TEST_SCRATCH`; find the old build from the `.pth` file or
`HARNESS_TEST_ORIGIN` rather than `..`; remove the stray worktrees under `scratch/test-modules/dag/`.
