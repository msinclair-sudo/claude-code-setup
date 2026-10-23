# First pass: GHOST

Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted.

- **First-pass fault rate: 2/46 = 4.3%** (Wilson 1.2% to 14.5%).
- Checker A alone 2, checker B alone 1, both 1; agree (ok against fault) on 45 of 46.
- Per 100 entries: holds + absent 4.3; stronger + numbers 0.0; conf 0.0; critic 0.0; merged 0.0.
- Kinds (entries): absent 2, holds 1.

| Packet | Entries | A | B | Either | Agree |
|---|---|---|---|---|---|
| packet-01.md | 46 | 2 | 1 | 2 | 45 |

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checkers' reasons |
|---|---|---|
