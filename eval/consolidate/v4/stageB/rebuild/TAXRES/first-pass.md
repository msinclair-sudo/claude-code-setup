# First pass: TAXRES

Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted.

- **First-pass fault rate: 6/30 = 20.0%** (Wilson 9.5% to 37.3%).
- Checker A alone 2, checker B alone 6, both 2; agree (ok against fault) on 26 of 30.
- Per 100 entries: holds + absent 16.7; stronger + numbers 3.3; conf 0.0; critic 0.0; merged 0.0.
- Kinds (entries): holds 5, numbers 1.

| Packet | Entries | A | B | Either | Agree |
|---|---|---|---|---|---|
| packet-01.md | 30 | 2 | 6 | 6 | 26 |

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checkers' reasons |
|---|---|---|
| fungal-repositories.1 | numbers | numbers: the text gives "Fungi enter via Index Fungorum (114,301 names ...)", the names as they enter the backbone, and the entry restates this as "Index Fungorum holds 114,301 names", dropping the context that defines the figure. |
