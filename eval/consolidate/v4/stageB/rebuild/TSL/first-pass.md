# First pass: TSL

Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted.

- **First-pass fault rate: 6/31 = 19.4%** (Wilson 9.2% to 36.3%).
- Checker A alone 4, checker B alone 4, both 2; agree (ok against fault) on 27 of 31.
- Per 100 entries: holds + absent 9.7; stronger + numbers 9.7; conf 0.0; critic 0.0; merged 0.0.
- Kinds (entries): stronger 3, holds 2, absent 1.

| Packet | Entries | A | B | Either | Agree |
|---|---|---|---|---|---|
| packet-01.md | 31 | 4 | 4 | 6 | 27 |

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checkers' reasons |
|---|---|---|
| collection-df.1 | stronger | stronger: the entry states "specificity is inversely related to df (lower df = more specific)" but drops the caveat its text gives in B-0011, that "df is a *frequency proxy*, not a definition of semantic specificity" and "low df from typos/OCR/identifiers does not imply true specificity". / stronger: the entry states "specificity is inversely related to df (lower df = more specific)" with the high rating but drops the contrary caveat its text attaches to that rating, "low df from typos/OCR/identifiers does not imply true specificity". |
| information-content.1 | stronger | stronger: the entry gives the IC scheme ("root P = 1, IC = 0", "altitude maps directly onto generality") with the high rating but drops the condition its text attaches to that rating, "Caveat: needs a unified root; WordNet has none naturally". |
| class-df.1 | stronger | stronger: the entry keeps the first half of A-008 ("operationalises the same inverse-frequency principle at the cluster level") and drops its "but it is an **engineering instantiation, not an independently validated specificity measure**". / stronger: the entry keeps "operationalises the same inverse-frequency principle at the cluster level" but drops the rest of that sentence, "but it is an engineering instantiation, not an independently validated specificity measure". |
