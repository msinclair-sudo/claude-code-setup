# Agent Workstream Harness — runtime

Machinery for running several Claude Code sessions against one repository as a
rank tree: each session holds one git worktree, code integrates upward by
fast-forward, documents climb as reviewed requests, and only rank 0 writes them.

The rules live in `../skills/harness/ref/spec.md` — transactions `T1`–`T12`,
invariants `I1`–`I10`, runtime `R1`–`R11`. `tree.canvas` beside it is the diagram.

There is **one** copy of that spec. The role skills (`-upward`, `-downward`,
`-root`) carry none and point back to it. They used to bundle their own, for
portability — but a role skill is never installed without `harness` and cannot
work without it, since `whoami` is what names it. The copies bought no
portability. They cost four files to keep in step, and a mid-lead loading two
roles could read the same 30 KB twice without being able to tell it had.

`sync-spec.sh` now guards that singularity rather than performing a fan-out:

```bash
harness/sync-spec.sh --check      # exit 1 if a role re-grew a spec, or a pointer went stale
harness/sync-spec.sh --from "/path/to/Agent Workstream Harness.md"
```

Nothing runs `--check` automatically, so a re-duplication stays silent until
someone looks. Run it before releasing a spec change, or wire it into this repo's
own pre-commit.

## What installs where

| repo | installed to | what it is |
| --- | --- | --- |
| `../skills/harness*/` | `~/.claude/skills/` | how an agent behaves. Auto-discovered by `install.sh`. |
| `bin/harness` | `~/.claude/harness/bin/` | position, occupancy, enrolment. Stdlib Python. |
| `templates/` | `~/.claude/harness/templates/` | guard hooks + tree/manifest starters |
| `../workflows/*.js` | `~/.claude/workflows/` | a lead's integration pass |

Per-project state (`binding.json`, `locks/`) is created at enrolment under
`~/.claude/harness/<slug>/` and is never touched by the installer.

## Opting a project in — two keys, both deliberate

```bash
harness scaffold /path/to/repo     # writes .harness/ + sets core.hooksPath
# edit .harness/tree.json, fill in .harness/manifest.json, commit both
harness enrol /path/to/repo        # this machine joins
harness whoami                     # exit 3 until both keys exist
```

Opting out is `harness unenrol` — local, immediate, touches nothing shared.

## Two things that are easy to get wrong

**Never set `core.hooksPath` to a relative path.** A relative path that is
missing on a branch runs no hook, exits 0, and warns nobody — the branch is
silently unguarded. `scaffold` sets it absolute so every worktree resolves to the
same guards.

**`reference-transaction` is the primary guard, not a backstop.** Every upward
integration is a fast-forward by design, so `pre-merge-commit` never fires on the
path a document would take. That hook must be POSIX `sh` with an explicit
`exit 0`: a non-zero exit gives `fatal: ref updates aborted by hook` and the
repository stops accepting *any* ref update. Test changes against a scratch clone.

## Naming: no node branch may be a path prefix of another

Git refs are files, so `refs/heads/dev` blocks `refs/heads/dev/ui` from existing —
in either order. Use `dev`, `dev_ui`, `w_m1`; never `dev/ui`. `harness whoami`
refuses a tree that breaks this rather than letting it fail at the first
`git worktree add`.

## Statusline integration

`statusline-snippet.py` is paste-ready and self-contained. Its contract is silence:
it returns `""` for any reason it cannot produce a segment — not a repo, not
enrolled, no index, branch is not a node — and it never raises. A statusline runs
in every session regardless of enrolment, so absence must cost nothing.

```python
seg = harness_segment(cdir)
if seg: print(seg)          # ↑dev·  [ui]  ⇄ api!6 m1◦  ↓ ui1· ui2·
```

`•` busy · `◦` idle · `·` nobody · `!N` N sessions sharing one worktree.

Cost is one `git rev-parse` (common-dir and branch in a single call) plus two file
reads. Prefer it over shelling out to `harness position`, which pays Python startup
again. `harness position --quiet` exists for the same contract when a shell is
easier: silent, exit 0, nothing on stderr.

Occupancy comes from `~/.claude/sessions/<pid>.json`, which carries `cwd`, `kind`
and `status`. Most entries are dead sessions, so every pid is checked.

## Orientation hook

`harness scaffold` writes a `SessionStart` hook into the **target repo's** own
`.claude/settings.json` — not into `~/.claude/settings.json`. It runs
`harness whoami --quiet --no-check` on `startup|resume|compact`, so a session in
an enrolled worktree wakes up knowing its node.

Scoping it to the repo means it does not exist in any other project: the command
is never spawned there, rather than being spawned and staying silent. Commit the
file and it travels with the tree.

`resume` is the matcher that matters — a resumed session gets a new session id and
would otherwise orphan its own lock.

Remove it by deleting the `SessionStart` entry from the repo's
`.claude/settings.json`. Nothing else depends on it.

## `harness doctor` — proving the guard, not reading its settings

Run it in each worktree after scaffolding, and after anything touches the hooks.
Exit 0 prints *refusal demonstrated, not inferred*; any failure means the worktree
is not guarded as configured.

It checks ten things in two groups. **Wiring**: `core.hooksPath` set and absolute;
`_guard` and the three hooks present and executable; and their mode **as git
records it**, because where `core.fileMode` is false a `chmod` succeeds on disk
while git stores `100644` and the hooks arrive inert in every fresh clone.

**Behaviour**, which is the half that matters:

- it synthesises content the document node has never held, stages it in a
  **throwaway index** so your real one is untouched, and requires a refusal
- it requires the guard to *allow* a document that arrived from the document node,
  so a guard that refuses everything fails too
- it requires **novel** content on a code path to pass, drawn from **this**
  worktree rather than the document node's tree

That last one had to be rebuilt. The first version drew its code sample from the
document node, which in a real project tracks *no code at all* — so the arm could
never fail. It also reimplemented the guard's matcher instead of asking it, drifted
to the older semantics, and consequently selected a *document* as its code sample.
Found by `biblion2-dev`. `_guard --classify` now exists so there is one matcher and
nothing has to copy it.

That second arm is not decoration. The first version of the authorship fix built
its blob set **empty** — `git diff-tree --stdin` silently ignores input with no
trailing newline — so the guard refused every document including legitimate
merges. Config inspection would have called that healthy. `doctor` caught it on
its first run.

A check that compares `core.hooksPath` to an expected string does the opposite: it
goes red *because* the harness is correctly installed, and whatever remedy it
prints disarms it.

## Not yet verified

The full cycle across two real terminals — `T1 → T2 → T11 → work → T2 → T4 → T10`
with a forced conflict — has not been run. The token bands in `I10` are estimates
and carry a warning callout until measured.
