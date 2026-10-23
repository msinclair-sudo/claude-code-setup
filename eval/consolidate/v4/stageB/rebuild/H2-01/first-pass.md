# First pass: H2-01

Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted.

- **First-pass fault rate: 10/143 = 7.0%** (Wilson 3.8% to 12.4%).
- Checker A alone 10, checker B alone 9, both 9; agree (ok against fault) on 142 of 143.
- Per 100 entries: holds + absent 6.3; stronger + numbers 0.7; conf 0.0; critic 0.0; merged 0.0.
- Kinds (entries): absent 5, holds 4, stronger 1.

| Packet | Entries | A | B | Either | Agree |
|---|---|---|---|---|---|
| packet-01.md | 60 | 3 | 3 | 3 | 60 |
| packet-02.md | 60 | 2 | 1 | 2 | 59 |
| packet-03.md | 23 | 5 | 5 | 5 | 23 |

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checkers' reasons |
|---|---|---|
| transfer-dependence.1 | stronger | stronger: The entry gives the synthesis as "transfer depends on the similarity of the training set to the target", dropping the hedge in "three dependencies recur" / "transfer appears to depend on similarity between training and target". |
