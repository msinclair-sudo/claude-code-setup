# Accuracy: the claims ledger and the blind fact-check

A polished explanation makes a wrong one look right: viewers of a flawed explanation were as confident as viewers of a correct one, and a model judging accuracy agreed with people at r = 0.14. So accuracy is checked against the sources, before anything is rendered, by a reader that never sees the render.

## claims.yaml
One entry per number or factual statement the reader sees or hears:
- `id`, `text` (exactly as shown or spoken), `source` (file:line, DOI, or the query that produced it), `kind`, `value`, `unit`.
- `kind`: **quoted** (the source says it), **derived** (computed from the source; say how in `source`), **illustrative** (made up to show the idea; the page labels it so).

## The blind fact-check (step 3)
Start a fresh subagent with the Agent tool. Give it only `claims.yaml` and read access to the sources; never the storyboard, the build or the stills. Prompt:

> For each claim in claims.yaml, open its source and judge it: **supported** (the source says this, at this strength and scope), **overstated** (the source says something narrower, more hedged, or about a different population or setting), or **unsupported** (the source does not say it, or the number differs). Check every number and unit. Flag any claim where a hedge was dropped ("may" became "does"), a scope widened (one dataset became "in general"), a correlation became a cause, or a range became a point. Derived claims: redo the derivation. Return one line per claim id: verdict, and the source's own words when it is not supported.

Fix every overstated or unsupported claim in `claims.yaml` and wherever it is used, then rebuild. Record the verdicts in `checks/factcheck.md`.

## Depictions
- A figure drawn from the real data or system carries `<span class="x-label">data</span>`; one made up to show the idea carries `illustrative`. In animation, say it in the narration or a corner label.
- A truncated axis gets a visible note on the figure; a scale bar beats a stated size.
- Wording of uncertainty: give the range or the count, not only a word ("likely").
