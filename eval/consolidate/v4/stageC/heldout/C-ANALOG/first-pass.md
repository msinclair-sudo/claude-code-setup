# First pass: C-ANALOG

Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted.

- **First-pass fault rate: 12/128 = 9.4%** (Wilson 5.4% to 15.7%).
- Checker A alone 11, checker B alone 9, both 8; agree (ok against fault) on 124 of 128.
- Per 100 entries: holds + absent 9.4; stronger + numbers 0.0; conf 0.0; critic 0.0; merged 0.0.
- Kinds (entries): absent 7, holds 5.

| Packet | Entries | A | B | Either | Agree |
|---|---|---|---|---|---|
| packet-01.md | 60 | 3 | 4 | 4 | 59 |
| packet-02.md | 60 | 5 | 3 | 5 | 58 |
| packet-03.md | 8 | 3 | 2 | 3 | 7 |

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checkers' reasons |
|---|---|---|
