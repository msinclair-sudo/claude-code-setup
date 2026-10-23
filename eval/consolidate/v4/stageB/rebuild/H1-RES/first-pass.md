# First pass: H1-RES

Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted.

- **First-pass fault rate: 7/177 = 4.0%** (Wilson 1.9% to 7.9%).
- Checker A alone 5, checker B alone 4, both 2; agree (ok against fault) on 172 of 177.
- Per 100 entries: holds + absent 3.4; stronger + numbers 0.6; conf 0.0; critic 0.0; merged 0.0.
- Kinds (entries): holds 5, absent 1, stronger 1.

| Packet | Entries | A | B | Either | Agree |
|---|---|---|---|---|---|
| packet-01.md | 60 | 0 | 2 | 2 | 58 |
| packet-02.md | 60 | 3 | 2 | 3 | 59 |
| packet-03.md | 57 | 2 | 0 | 2 | 55 |

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checkers' reasons |
|---|---|---|
| n-cycle-vertical.4 | stronger | stronger: the entry says Anand and Chanway "found ... that nifH was transmitted horizontally while nifD was transmitted vertically", dropping the hedge in "phylogenetic analyses suggested nifH was transmitted horizontally". / stronger: the entry says Anand and Chanway "found ... that nifH was transmitted horizontally while nifD was transmitted vertically", dropping the hedge in the text, where "phylogenetic analyses suggested" this. |
