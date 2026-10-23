# First pass: C-GHOSTFUS

Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted.

- **First-pass fault rate: 8/81 = 9.9%** (Wilson 5.1% to 18.3%).
- Checker A alone 7, checker B alone 6, both 5; agree (ok against fault) on 78 of 81.
- Per 100 entries: holds + absent 7.4; stronger + numbers 2.5; conf 0.0; critic 0.0; merged 0.0.
- Kinds (entries): holds 4, absent 2, stronger 2.

| Packet | Entries | A | B | Either | Agree |
|---|---|---|---|---|---|
| packet-01.md | 60 | 4 | 3 | 4 | 59 |
| packet-02.md | 21 | 3 | 3 | 4 | 19 |

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checkers' reasons |
|---|---|---|
| co-citation-bridge.1 | stronger | stronger: the cited A-009 says the bridge "is encoded by construction but not validated downstream", and the entry keeps "encoded by construction" but drops the "but not validated downstream". / stronger: the cited text says the bridge "is encoded by construction but not validated downstream", and the entry keeps "encoded by construction" while dropping "but not validated downstream". |
| denoise-order.2 | stronger | stronger: the entry says the PCA-100 "and an autoencoder" a priori "preserves accuracy" but drops the contrary finding its text gives, that "one model (GraphConv) degraded badly with the autoencoder bottleneck". / stronger: the entry says PCA-100 "and an autoencoder" a priori "preserves accuracy" but drops the contrary finding its text gives, that "one model (GraphConv) degraded badly with the autoencoder bottleneck". |
