# First pass: C-COVDIST

Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted.

- **First-pass fault rate: 1/69 = 1.4%** (Wilson 0.3% to 7.8%).
- Checker A alone 1, checker B alone 0, both 0; agree (ok against fault) on 68 of 69.
- Per 100 entries: holds + absent 1.4; stronger + numbers 0.0; conf 0.0; critic 0.0; merged 0.0.
- Kinds (entries): holds 1.

| Packet | Entries | A | B | Either | Agree |
|---|---|---|---|---|---|
| packet-01.md | 60 | 1 | 0 | 1 | 59 |
| packet-02.md | 9 | 0 | 0 | 0 | 9 |

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checkers' reasons |
|---|---|---|
