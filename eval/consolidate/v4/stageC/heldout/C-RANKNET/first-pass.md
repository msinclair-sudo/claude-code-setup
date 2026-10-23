# First pass: C-RANKNET

Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted.

- **First-pass fault rate: 26/143 = 18.2%** (Wilson 12.7% to 25.3%).
- Checker A alone 21, checker B alone 22, both 17; agree (ok against fault) on 134 of 143.
- Per 100 entries: holds + absent 17.5; stronger + numbers 0.7; conf 0.0; critic 0.7; merged 0.0.
- Kinds (entries): holds 19, absent 7, stronger 1, critic 1.

| Packet | Entries | A | B | Either | Agree |
|---|---|---|---|---|---|
| packet-01.md | 60 | 7 | 10 | 12 | 53 |
| packet-02.md | 60 | 9 | 8 | 9 | 59 |
| packet-03.md | 23 | 5 | 4 | 5 | 22 |

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checkers' reasons |
|---|---|---|
| expression-benchmarks.14 | holds, stronger | stronger: the entry keeps "rank-family measures are ahead of Pearson on two curated truth sets" but drops the text's qualifier that "the authors themselves conclude the ordering is contingent on the biological process" (and holds adds "AraCyc", which the quoted text does not name). / holds: holds names "the AraCyc pathway task", but the quoted text says only "two curated truth sets" and does not name AraCyc. |
