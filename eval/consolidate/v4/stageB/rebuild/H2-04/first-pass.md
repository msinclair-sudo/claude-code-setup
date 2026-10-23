# First pass: H2-04

Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted.

- **First-pass fault rate: 21/142 = 14.8%** (Wilson 9.9% to 21.6%).
- Checker A alone 14, checker B alone 20, both 13; agree (ok against fault) on 134 of 142.
- Per 100 entries: holds + absent 14.8; stronger + numbers 0.0; conf 0.0; critic 0.0; merged 0.0.
- Kinds (entries): holds 17, absent 4.

| Packet | Entries | A | B | Either | Agree |
|---|---|---|---|---|---|
| packet-01.md | 60 | 5 | 6 | 7 | 57 |
| packet-02.md | 60 | 7 | 10 | 10 | 57 |
| packet-03.md | 22 | 2 | 4 | 4 | 20 |

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checkers' reasons |
|---|---|---|
