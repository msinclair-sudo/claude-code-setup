# First pass: NFERT

Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted.

- **First-pass fault rate: 1/54 = 1.9%** (Wilson 0.3% to 9.8%).
- Checker A alone 1, checker B alone 1, both 1; agree (ok against fault) on 54 of 54.
- Per 100 entries: holds + absent 1.9; stronger + numbers 0.0; conf 0.0; critic 0.0; merged 0.0.
- Kinds (entries): holds 1.

| Packet | Entries | A | B | Either | Agree |
|---|---|---|---|---|---|
| packet-01.md | 54 | 1 | 1 | 1 | 54 |

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checkers' reasons |
|---|---|---|
