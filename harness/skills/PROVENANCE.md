# Skills the harness gives a node by its role

`ponytail`, `ponytail-review`, `ponytail-audit` and `ponytail-debt` are copied byte for
byte from https://github.com/DietrichGebert/ponytail at commit
9b58c1ffb790c075ca32e70a89cf1d80588f4abf (MIT, Dietrich Gebert; `LICENSE` here).
They match the copies main vendored into biblion2's dev_dag_3 worktree on 2026-10-12.

Not copied, on purpose: the plugin's hooks, commands, `ponytail-gain` and
`ponytail-help`. The plugin's SessionStart and SubagentStart hooks inject
`skills/ponytail/SKILL.md` into every session; the harness does that itself,
for the nodes whose role or `skills` names it and for no other (log 172).

`install.sh` deploys this folder to `~/.claude/harness/skills/`, not
`~/.claude/skills/`, so no other session lists them. To move to a newer
ponytail, copy the four files at the new commit and change the commit above.
