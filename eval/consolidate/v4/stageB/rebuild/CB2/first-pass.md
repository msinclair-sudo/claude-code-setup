# First pass: CB2

Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted.

- **First-pass fault rate: 2/81 = 2.5%** (Wilson 0.7% to 8.6%).
- Checker A alone 2, checker B alone 2, both 2; agree (ok against fault) on 81 of 81.
- Per 100 entries: holds + absent 1.2; stronger + numbers 1.2; conf 0.0; critic 0.0; merged 0.0.
- Kinds (entries): holds 1, stronger 1.

| Packet | Entries | A | B | Either | Agree |
|---|---|---|---|---|---|
| packet-01.md | 60 | 0 | 0 | 0 | 60 |
| packet-02.md | 21 | 2 | 2 | 2 | 21 |

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checkers' reasons |
|---|---|---|
| variation-axes.1 | stronger | stronger: the entry lists "sequencing depth" among the axes with direct evidence and drops the text's qualifier that depth "is measured, but only as simulated per-genome coverage in targeted-assembly benchmarks — not as library depth in a real assemble-and-bin pipeline". / stronger: the entry lists "sequencing depth" among the axes with direct evidence without the text's limit that depth is measured "only as simulated per-genome coverage in targeted-assembly benchmarks — not as library depth in a real assemble-and-bin pipeline". |
