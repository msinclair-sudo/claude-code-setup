# First pass: CB1

Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted.

- **First-pass fault rate: 4/145 = 2.8%** (Wilson 1.1% to 6.9%).
- Checker A alone 2, checker B alone 4, both 2; agree (ok against fault) on 143 of 145.
- Per 100 entries: holds + absent 2.1; stronger + numbers 0.7; conf 0.0; critic 0.0; merged 0.0.
- Kinds (entries): absent 2, holds 1, stronger 1.

| Packet | Entries | A | B | Either | Agree |
|---|---|---|---|---|---|
| packet-01.md | 60 | 0 | 1 | 1 | 59 |
| packet-02.md | 60 | 2 | 2 | 2 | 60 |
| packet-03.md | 25 | 0 | 1 | 1 | 24 |

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checkers' reasons |
|---|---|---|
| liming-effects.6 | stronger | stronger: The entry keeps "reduced N₂O emissions and nitrate leaching" but drops the contrary finding in the same sentence, "but that in CO₂-C equivalents 'the GHG emissions from liming were about four times those saved by reducing N₂O emissions'". / stronger: the entry keeps "liming to pH 6.0 as recommended reduced N₂O emissions and nitrate leaching" but drops the contrary finding the text gives in the same sentence, "but that in CO₂-C equivalents 'the GHG emissions from liming were about four times those saved by reducing N₂O emissions'". |
