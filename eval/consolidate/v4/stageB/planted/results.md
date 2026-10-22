# B1: planted-fault test, checkpoint report (2026-10-22)

Does the v4 checker catch known faults, by kind, especially omissions? Two fresh checkers judged the claims blind.
They used `checker.md` as built in B0 (change 5's wording and the hint paragraph), with hints in the packets, and
were told it was an ordinary check. Seeds: pool 20261025, assignment 20261026, judging order 20261027.
- Tool: `../tools/planted.py`.
- Per-claim detail: `scores.md`.
- The key: `key.json`.

## What was planted

| Step | Result |
|---|---|
| Pool | 130 claims the v3 first-pass checker passed, 4 to 29 per note across all 14 notes (`pool.json`, committed before screening) |
| Screening (fresh checker, no hints, v4 wording) | 102 clean; **28 set aside as faulted** (24 `holds`, 2 `stronger`, 2 `absent`) |
| Applicability (the planter) | hedge fits 70 claims, number 51, standing 43, setting 37, counter-clause **15** |
| Assignment (seeded, to quotas 20 / 20 / 8 / 8 / 8) | 59 plants; counter-clause short by 5 (only 15 claims carry one); 43 controls |
| Validation (fresh validator) | 48 pass, 11 fail: 9 of 15 counter-clause plants (the dropped clause did not qualify what the claim still said, so leaving it out was detail, which is allowed), 1 setting (added facts, not a setting), 1 number (the new number matched the cited text). Failed plants were dropped |
| Judged | 91 claims: 48 planted and 43 controls, in seeded order; 32 carried a hint |

## Catch rates (caught = any fault; "either" = at least one of the two judges)

| Edit type | Planted | Judge 1 | Judge 2 | Either | Both | Intended kind (either) | With a hint | Either, 95% Wilson interval |
|---|---|---|---|---|---|---|---|---|
| Hedge or scope removed | 20 | 16 | 17 | 17 | 16 | 17 | 8 | 85% (64% to 95%) |
| Counter-clause dropped | 6 | 4 | 5 | 5 | 4 | 5 | 2 | 83% (44% to 97%) |
| True setting added | 7 | 6 | 6 | 7 | 5 | 7 | 5 | 100% (65% to 100%) |
| Number changed | 7 | 7 | 7 | 7 | 7 | 7 | 6 | 100% (65% to 100%) |
| Standing raised | 8 | 8 | 8 | 8 | 8 | 8 | 2 | 100% (68% to 100%) |
| **Controls (unedited): faulted** | 43 | 1 | 0 | 1 | 0 | | 9 | 2% (0% to 12%) |

Per judge, omissions (hedge plus counter-clause, 26 plants): judge 1 caught 20 (77%), judge 2 caught 22 (85%).
Additions, numbers and standing (22 plants): 21 and 21. Every catch was of the intended kind.

## What was missed

Both judges missed four plants. All are subtle scope limits, or a contrary argument from a second source:

| Claim | Type | What the edit removed |
|---|---|---|
| TSL/phrase-and-multilingual-tail.1 | hedge | "by this corpus": a search-scope qualifier, the "untested" problem |
| H2-01/direct-dimension.12 | hedge | "only as a nearest precedent" became "as a precedent" |
| 16S/abundance-distribution.25 | hedge | "reported as a distribution" |
| 16S/abundance-distribution.7 | counter | ", and Haegeman 2013 argues the tail is not identifiable from sample data at all" (and its source) |

Caught by one judge only:
- H2-04/complementarity-overlap.11: "Pairwise metabolic models predict that" removed, a modelled result recast as a
  direct finding;
- GHOST/missingness-degradation.6: "but not the catastrophic collapse of GCNMF" dropped.

The faulted control, CB3/n2o.5 (judge 1: `holds` adds "N2O", a gas the cited text does not name), may be a real fault
the screener missed rather than a false alarm.

## Reading

- **Omissions are mostly caught now:** 85% of hedges and 5 of 6 counter-clauses, against the spot-check, where the
  v3 checker missed both omissions. Change 5's wording names exactly these cases (a dropped scope, hedge, condition,
  denominator or "but not …"), and the judges used it. Additions, numbers and raised standing were all caught. False
  alarms on clean claims were rare (1 of 43).
- **What still gets through** are qualifiers that do not look like hedges: search scope ("by this corpus"), precedent
  scope ("nearest precedent"), measurement form ("reported as a distribution"), and a second source's contrary
  argument. The first is the case change 3's `search:` field now carries as a separate field. The omission hint
  (hedge, negation and contrast words in the cited text missing from the entry) would flag "only", "nearest",
  "by"-phrases and "argues … not".
- **Caveats.**
  - Planted faults may be easier to catch than natural ones: each plant is one clean edit, and the validator
    dropped the most ambiguous counter-clause plants (9 of 15).
  - The counter-clause type has only 6 plants: its interval runs from 44% to 97%.
  - Both judges read checker.md's examples, which name the planted kinds; natural faults may be less like the
    examples.
- **Side finding for B2:** the screener, a v4-worded checker, faulted 28 of 130 claims the v3 checkers had passed
  (22%), 24 of them `holds`. Stage A suggested the same. The re-scored v3 baseline will be well above v3's 12.1%.

## At the checkpoint

The owner's condition for the omission hint was poor omission catch rates. Omissions were caught at 85% (hedge) and
5 of 6 (counter-clause); all four double misses were subtle scope qualifiers. Two options:
1. **Proceed to B2 with the checker as it is** (recommended). The rates are not poor. The commonest miss (search
   scope) is now a field of its own in v4 notes.
2. **Add the omission hint first.** It would be confirmed on a freshly planted set (screener, planter, validator, two
   judges: about 5 runs) before B2.
