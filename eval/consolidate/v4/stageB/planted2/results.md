# B1b: the omission hint on a fresh planted set (2026-10-23)

Does an omission hint help the checker catch scope-type omissions, without more false alarms? The owner chose this test
at the B1 checkpoint. B1's four double misses were scope qualifiers that do not look like hedges.

**The design.**
- Four fresh checkers judged the same 86 claims, blind and in the same seeded order.
  - **W1 and W2** had the omission hint ("In the cited text, not in the entry: …") and its checker.md paragraph
    (`checker-W.md`).
  - **N1 and N2** had B1's setup (`checker-N.md`, checker.md at 7b5a0b3).
  - The packets are identical apart from the 50 omission lines (checked by diff).
- **Seeds:** pool 20261028, assignment 20261029, judging order 20261030, controls 20261031.
- **Records:**
  - the tool: `../tools/planted2.py`;
  - the hint code as tested: `../tools/omission_hint.py`;
  - per-claim detail and tables: `scores.md`;
  - the sealed key: `key.json`.

## What was planted

| Step | Result |
|---|---|
| Pool | 200 v3-passed claims outside B1's pool, 4 to 50 per note, all 14 notes (`pool.json`, committed before screening) |
| Screening (fresh checker, B1's wording, no hints) | 176 clean; 24 set aside (16 `holds`, 6 `absent`, 2 `conf`) |
| Applicability | scope 97, number 88, standing 71, setting 52, counter 32, hedge 13 (16 less three hedges inside direct quotations, removed before assignment) |
| Assignment (seeded, quotas 24 / 12 / 8 / 4 / 4 / 4) | 56 plants, all quotas filled; 45 controls |
| Validation (fresh validator) | 41 pass, 15 fail: scope 8 (the dropped word left the claim covering no more), counter 5, standing 2. Failed plants were dropped |
| Judged | 86 claims: 41 planted, 45 controls. 31 omission plants, 14 of them hint-visible (the hint lists an item for the edited claim that it did not list for the clean one) |

## Catch rates (caught = any fault; "either" = at least one of the condition's two judges)

| Edit type | n | Hint-visible | W either | N either | W1, W2 | N1, N2 |
|---|---|---|---|---|---|---|
| Scope qualifier | 16 | 4 | 13 (81%, 57% to 93%) | 12 (75%, 51% to 90%) | 13, 12 | 12, 12 |
| Counter or contrary | 7 | 5 | 5 (71%, 36% to 92%) | 5 (71%, 36% to 92%) | 5, 4 | 5, 5 |
| Hedge | 8 | 5 | 8 (100%, 68% to 100%) | 8 (100%, 68% to 100%) | 8, 8 | 8, 8 |
| **Omissions, pooled** | 31 | 14 | **26 (84%, 67% to 93%)** | **25 (81%, 64% to 91%)** | 26, 24 | 25, 25 |
| Setting, number, standing | 10 | | 10 | 10 | | |
| **Controls faulted** | 45 | | **3 (7%, 2% to 18%)** | **4 (9%, 4% to 21%)** | 2, 3 | 3, 3 |

Summed over each condition's two judges, omission catches were W 50 and N 50, out of 62. Control faults were W 5 and
N 6, out of 90.

**Paired, on the same claims (either):**
- **Omission plants:** 1 caught only with the hint, 0 only without, 25 by both, 5 by neither (exact McNemar p =
  1.00). The one W-only catch, H1-02/mobile-region-loss.5 ("simulated" removed), carried no omission line, so the
  hint did not cause it.
- **Hint-visible omission plants:** 12 caught by both conditions, 2 by neither.
- **Controls:** 0 faulted only with the hint, 1 only without, 3 by both.

**Faulted controls, read by a blind adjudicator** (no hints, information only). All four are real faults that the
screener missed, not false alarms:
- three `holds`: "global ocean", "Yuan et al.'s simulated and synthetic sets" and "Li and Yin's simulations", none
  in the cited text;
- one `conf`: `limit: access` on a full-text source.

Read that way, neither condition raised a false alarm.

## What got through

Five omission plants were missed by all four judges:

| Claim | Type | What was removed | Omission line listed it? |
|---|---|---|---|
| H1-06/perturbation-response.9 | scope | "measured by qSIP" (in one forest soil) | yes: "by qsip in one forest" |
| H2-01/other-field-transfer.1 | counter | "…compressed sensing, not a direct covariance-reproduction score" | yes: "not a direct covariance-reproduction score" |
| H1-02/sample-dependence.7 | scope | "related" (recovered genomes) | no |
| H1-RES/pangenome.11 | scope | "(12 symbionts)" and "12" in `holds` | no |
| 16S/ploidy.11 | counter | "although the open full text reports single-cell CLSM and FACS distributions" | no |

For the two hint-visible misses, the W judges saw the dropped words and judged them detail. The hint pointed them
there, and they disagreed with the plant.

## Decision (rule fixed before drawing, plan.md revision 4)

- **The rule's output: not adopted, stop.** It tripped on its absolute clause: W2 faulted 3 of 45 controls, above 5%
  (2.25). The relative clause (W exceeds N by 3 or more) did not trip, since W had 5 and N 6. N1 and N2 also faulted
  3 each, and the adjudicator found all four faulted controls to be real faults. **So the hint did not raise false
  alarms.** The absolute clause was badly drafted: it measured the checker, not the hint.
- **Under the rule's other branch it is not adopted either.** There was no gain in omissions caught: 50 against 50.
- **So the omission hint is not adopted.** The skill's checker is restored to B1's setup (checker.md, `hints()`,
  `packets --hints` as at 7b5a0b3). The tested code is kept in `../tools/omission_hint.py`.

## Reading

- **On a fresh set weighted to scope, the B1 checker already catches most omissions:** 81% pooled without the hint
  and 84% with it. That covers every hedge, 12 of 16 scope qualifiers, and 5 of 7 counter-clauses.
- **The hint does not change what the checker decides.** On the 14 plants where it listed the dropped words, both
  conditions caught the same 12 and missed the same 2. The 2 misses were seen and judged detail. What still gets through is
  qualifiers a judge can read as detail ("measured by qSIP", a sample count, "related"), and a second-source
  counter-point. A word list cannot settle that judgement.
- **The screener misses `holds` additions.** It passed 4 of 45 controls that four judges and the adjudicator later
  faulted (B1 had 1 of 43). The B2 baseline will count such faults.
- **Caveats:**
  - Planted faults may be easier to catch than natural ones.
  - The validator removed the most arguable plants (8 of 24 scope).
  - Counts per type are small, so the intervals are wide.
  - The hint was visible on only 14 of 31 omission plants, so its effect was tested on few claims.
