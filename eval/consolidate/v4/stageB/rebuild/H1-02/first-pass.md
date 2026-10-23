# First pass: H1-02

Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted.

- **First-pass fault rate: 14/124 = 11.3%** (Wilson 6.8% to 18.1%).
- Checker A alone 13, checker B alone 13, both 12; agree (ok against fault) on 122 of 124.
- Per 100 entries: holds + absent 11.3; stronger + numbers 0.0; conf 0.0; critic 0.0; merged 0.0.
- Kinds (entries): holds 9, absent 6.

| Packet | Entries | A | B | Either | Agree |
|---|---|---|---|---|---|
| packet-01.md | 60 | 7 | 8 | 8 | 59 |
| packet-02.md | 60 | 6 | 5 | 6 | 59 |
| packet-03.md | 4 | 0 | 0 | 0 | 4 |

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checkers' reasons |
|---|---|---|
