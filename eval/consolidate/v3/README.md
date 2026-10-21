# consolidate v3: development run (2026-10-21)

The six development notes rebuilt from scratch with v3 (commit 4f28b9c, plus the clarifications in 66b23eb and
later), by three fresh builders who did not see the v2 notes: the v2 notes were removed from the vault before
the builds (copies in `../v2/notes/`). Compared against the v2 baseline in `../v2/`.

## Contents

- `as-built/`: each note as its builder first finished it, before the faithfulness check.
- `notes/`: the six notes as fixed and re-checked (also in the vault). 22 claims carry `limit: access` (16S 12,
  H2-01 5, CB1 5).
- `verdicts/`: first-pass checker verdicts (`<ID>.md`; 16S in two halves), and every re-check
  (`<ID>.recheck-N.md`).
- `acceptance.md`: tests A and B on the fixed 16S note, the same prompt as v2.
- `spot-check-16S.md`: 20 entries drawn at random from the 16S note as built, for the owner to judge (seed
  20261021, fixed before the build). `spot-check-16S.checker.md` holds the first-pass checker's verdicts on the
  same 20: sealed, read it after judging.

## First-pass faults: v3 against v2

| Note | v3 entries | v3 faulted | v2 faulted | stronger | conf | numbers | absent | critic | merged | holds |
|---|---|---|---|---|---|---|---|---|---|---|
| 16S | 460 | 88 (19%) | 170 of 541 (31%) | 0 (4) | 1 (23) | 1 (1) | 30 (30) | 2 (0) | 0 (1) | 54 (111) |
| H2-01 | 182 | 17 (9%) | 8 of 167 (5%) | 0 (0) | 1 (2) | 0 (0) | 9 (3) | 2 (2) | 0 (0) | 5 (1) |
| TSL | 35 | 3 (9%) | 13 of 42 (31%) | 0 | 0 (3) | 0 | 0 (10) | 0 | 0 | 3 (0) |
| CB1 | 107 | 10 (9%) | 11 of 113 (10%) | 0 | 4 (3) | 0 | 2 (6) | 0 | 0 | 4 (2) |
| CB2 | 64 | 3 (5%) | 9 of 73 (12%) | 0 | 0 (4) | 0 | 0 (4) | 0 | 0 | 3 (1) |
| NFERT | 45 | 1 (2%) | 6 of 48 (13%) | 0 | 0 (2) | 0 | 0 (3) | 0 | 0 | 1 (1) |
| **All** | **893** | **122 (14%)** | **217 of 984 (22%)** | 0 (4) | 6 (37) | 1 (1) | 41 (56) | 4 (2) | 0 (1) | 70 (116) |

v2 counts in brackets. Two of v3's faults are not faults under the skill's rules: 16S ploidy.2 ("one
laboratory", which the word list counts as `single`; the owner's ruling) and four CB1 `limit: access` calls on
"not read in the original" (settled by a clarification: second-hand reading is an access reason; a fresh
re-checker passed all four).

What changed:
- `conf` faults fell from 37 to 6: a quoted basis must now sit in the entry's own text, so it cannot be
  borrowed from a neighbouring sentence. `stronger` fell from 4 to 0, `holds` from 116 to 70.
- `absent` barely moved (56 to 41) and is now the main fault with `holds`: a setting, a name or a year carried
  in from outside the quoted text (a citekey's title or year, a source named elsewhere in the note, a critic
  sentence not cited). Lint cannot see these; only the checker can.
- H2-01 got worse (5% to 9%), mostly do-not-say entries citing the critic item that names a problem but not the
  one that words it, and "Not measured" list items cited without their heading. Its first pass also saw section
  titles cut at 40 characters (as v2 did); the cut was removed before the other notes' checks.

## Re-checks: who confirmed the fixes

From v3, a fresh agent that made none of the fixes re-checks every fixed entry, and the loop repeats until it
finds nothing (v2's fixes were graded by the builders themselves).

| Note | Fixed | Round 1 still faulted | Round 2 | Round 3 |
|---|---|---|---|---|
| H2-01 | 17 | 3 of 17 (one a key year, not a fault) | 1 of 2 (the title cut) | 0 of 1 |
| TSL, CB1, CB2, NFERT | 17 | 1 of 17 | 0 of 1 | |
| 16S | 87 | 9 of 87 | 1 of 9 | 0 of 1 |

Every fault found is now fixed and confirmed by a fresh checker; all six notes lint with 0 errors and every
required item accounted for. The fixed notes are copied into `notes/`.

In round 1, 13 of 121 fixes (11%) still had a fault, including one fix that turned a `holds` fault into a
`stronger` one (dns.33 dropped the critic's "in slow growth") and one that exposed a `critic` fault by citing
the critique (ploidy.25). Self-graded, those would have stood.

## Acceptance (16S, after fixes)

| Test | v3 | v2 |
|---|---|---|
| A: the 28 MB-01 critic corrections | 27 applied, 1 partly, 0 missing | 26, 2, 0 |
| B: the video's 29 literature claims | 23 covered, 6 absent | 25 covered, 4 absent |

Test B's six absences all rest on the four sources the video took from outside the research (Caporaso 2011,
Woese 1987, the DADA2 tutorial, the Illumina specifications); v2 counted two of the same claims as covered by
their nearest entries. Test A's remainder: abundance-distribution.7 restates Zhou 2013's best fits without the
critic's "unverified", and two `src` labels (chimeras.2, copy-number.21) still show the note's "repl" where
`conf` carries the critic's `single`.

## Candidates for v4 (from the builders and checkers; not applied)

- **Label versus claim corrections.** The line between a critic correcting a source's label (`src` shows the
  correction) and correcting the claim (`conf` only) is not defined; builders split differently (H2-01, 16S, and
  test A's two residues).
- **A label that introduces a list** ("reported the following [FT; meas; cont]:") covers nothing after it, so
  the list's bullets get `not stated`. Say whether it should cover the list.
- **Labels mid-bullet** leave a bullet's headline figure without a standing (H2-01: 19 bullets, MB-01: 23).
- **The standing-word table is literal**: "the only direct empirical test", "one simulated-LDA study", "one
  microbial measurement" warn. Either widen the lint patterns or say the table is the list.
- **Verification status has no field** ("full text per angle, not re-checked", "verified in extracted text",
  the critic as reader of record for a figure only it reports).
- **Body coverage in fallback notes is unchecked**: with 7 to 29 required items, most claims rest on body
  addresses, and nothing reports body sentences no entry cites. The 16S builder wrote its own script for this.
- **Callouts outside the inventory**: "Sources not obtained" holds findings (Lauber 2010's storage result) that
  no entry can cite; reference-list notes ("I did not verify them against the published version") likewise.
- **A Refuted-only section counts as a critique**, so a partly checked note (TSL: 25 of 91 claims verified)
  gets no "never checked by a second reader" gap.
- **Key years**: a reused Refs.bib key's year often differs from the note's (online versus issue year); the
  warning asks for a check the skill forbids. Make it informational.
- **`holds` from citekeys**: checkers repeatedly found settings and years taken from a key or title. Say so
  in format.md: the key is not text.
- **Two inputs' grades for one claim** have room for one `rating`; one input's critic against another input's
  label has no rule.
- **Inputs table** has no column for which checks ran (the 16S builder added a sentence).
