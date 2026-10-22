# v4 diagnostics (analysis only; the skill did not change)

Run 2026-10-22 on the v3 usability material, to inform `../plan.md`.

## Facts only in the raw pieces: correctly excluded, or lost?

Every raw-piece statement with factual content was matched against the view piece on the same topic. Each
raw-only fact was looked up in the knowledge note, the writer's view and the raw notes. One read-only reader per
topic; per-topic tables in `raw-only-<topic>.md`.

| Topic | Raw statements | No fact | In both | A unused | B lost by the view | C correctly excluded | D lost by consolidation | E writer's own |
|---|---|---|---|---|---|---|---|---|
| 16S | 70 | 4 | 56 | 8 | 0 | 1 | 0 | 1 |
| TSL (findings) | 74 | 4 | 67 | 0 | 1 | 0 | 0 | 2 |
| TSL (with attribution) | 74 | 4 | 62 | 2 | 4 | 0 | 0 | 2 |
| NFERT | 72 | 2 | 64 | 2 | 2 | 0 | 0 | 2 |
| **All (findings)** | **216** | **10** | **187** | **10** | **3** | **1** | **0** | **5** |

The readers drew "in both" slightly differently: TSL's counted a finding without its named source as raw-only,
so TSL is given both ways. 16S's raw piece names few sources; NFERT's dropped citations are listed in its file
(four rows lose their source in the view piece, all through `src`).

- **D = 0 in all three topics.** Consolidation lost nothing the raw writers used.
- **C = 1.** The one excluded fact (16S, relative abundance robust to the pipeline) is a wording the critic
  corrected, kept out by dns.14.
- **B: every loss is a field the view drops.** Setting (`holds`: "one system", the rare tail), derivation
  (`class: deriv`) and attribution (`src`: Joho and Sanderson, Bystrov). Adding setting, class and author-year to
  the view addresses all of them.
- **A: the view writer's selection** from a large view; the 16S view writer used other entries on the same
  points.
- **E: the raw writer's own** background and arithmetic, two of which the fact-check faulted (NFERT's 12 t CO₂e
  per t N).

## TSL accuracy

`tsl-accuracy.md`. View piece 14 faults on 60 claims (23%), raw 6 on 66 (9%). Of the view's 14: absences stated
as fact 4, setting dropped 3, standing raised or one case generalised 5, the writer's own prevalence claims 2.
Seven trace directly to fields the view removed (search status, setting), and most of the standing faults to
`class` being removed.
