# Stage C: state

v4 is frozen as built through stage C (plan.md revision 7): skill content as at b59851f, checker as at 7b5a0b3.
Each session reads this file first, and appends what finished and what is next.

## C0: done (2026-10-24)

- **Revision 7 and the v5 rulings** (4 to 9) are recorded in `../plan.md`.
- **`heldout/criteria.md`** was committed before the frame (a6a752b). Its seeds: draw 20261040, topics 20261041,
  letters 20261042.
- **Frame** (`heldout/frame.tsv`, from `tools/frame.py`, metadata only): 75 notes, 29 excluded.
  - 15 from v3's frame (development or read);
  - 8 v3 held-out;
  - 6 writing set-aside.

  That leaves 46 eligible notes.
- **The draw** (`heldout/draw.md`, `tools/draw.py`): one unit from each of the seven categories. Category 5 is
  dropped, with no members.

| ID | Cat. | Input (vault-relative) | Words |
|---|---|---|---|
| C-DENIT | 1 | `PhD/Proposal/Research/Results/Denitrification and N2O-reduction genes against organism phylogeny and habitat congruence, habitat association and within-genus variation (literature review).md` | 14,080 |
| C-ANALOG | 2 | `PhD/Proposal/Research/Results/Do changed conditions at a location fall within the range present elsewhere Evidence on present-day analogues for changed climate and changed soil conditions.md` | 12,664 |
| C-RANKNET | 3 | `PhD/Proposal/Research/Results/Rank-based association networks what exists, what has been benchmarked against known truth, and where the comparison has not been made.md` | 15,193 |
| C-PREDICT | 4 | `PhD/Proposal/Research/Results/Held-out prediction of taxonomic versus gene or trait community profiles from environment a literature review.md` | 12,203 |
| C-STEPDEN | 6 | `PhD/Proposal/Research/Results/Stepwise Denitrification with N2O Output in Constraint-Based Metabolic Models.md` | 3,200 |
| C-GHOSTFUS | 7 | `PhD/biblion/research/results/Featureless Ghost Nodes in Anchored Graph-Diffusion Fusion_ A Ve.md` | 3,929 |
| C-COVDIST | 8 | `PhD/Proposal/Research/Results/Quantifying Distance from Training Data to Test Points in Continuous Covariate Space.md` | 3,420 |

**Sessions, re-sized from the drawn notes.** Notes 1 to 4 are large deep runs of 12,000 to 15,000 words, about
three packets each by B6 and B7's sizes. Four in one session would be about 3M tokens, against the per-session
sizing of 1M. So the build becomes:
- **C1a:** C-DENIT and C-ANALOG, one builder;
- **C1b:** C-RANKNET and C-PREDICT, one builder;
- **C2:** C-STEPDEN, C-GHOSTFUS and C-COVDIST, one builder.

C3 to C6 are as planned. There are 15 minutes between sessions.

**Next: C1a**, after a 15-minute wait.

## C1a: started (2026-10-24, 03:03)

One builder for C-DENIT then C-ANALOG, with the B4 prompt. The notes are new, so the builder picks titles and reports the paths.
