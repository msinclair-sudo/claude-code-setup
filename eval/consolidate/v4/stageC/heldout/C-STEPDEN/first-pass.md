# First pass: C-STEPDEN

Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted.

- **First-pass fault rate: 4/67 = 6.0%** (Wilson 2.3% to 14.4%).
- Checker A alone 4, checker B alone 3, both 3; agree (ok against fault) on 66 of 67.
- Per 100 entries: holds + absent 6.0; stronger + numbers 0.0; conf 0.0; critic 0.0; merged 0.0.
- Kinds (entries): holds 4.

| Packet | Entries | A | B | Either | Agree |
|---|---|---|---|---|---|
| packet-01.md | 60 | 4 | 3 | 4 | 59 |
| packet-02.md | 7 | 0 | 0 | 0 | 7 |

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checkers' reasons |
|---|---|---|
