# First pass: H1-05

Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted.

- **First-pass fault rate: 17/119 = 14.3%** (Wilson 9.1% to 21.7%).
- Checker A alone 15, checker B alone 16, both 14; agree (ok against fault) on 116 of 119.
- Per 100 entries: holds + absent 11.8; stronger + numbers 2.5; conf 0.0; critic 0.0; merged 0.0.
- Kinds (entries): holds 11, absent 3, stronger 2, numbers 1.

| Packet | Entries | A | B | Either | Agree |
|---|---|---|---|---|---|
| packet-01.md | 60 | 8 | 10 | 10 | 58 |
| packet-02.md | 59 | 7 | 6 | 7 | 58 |

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checkers' reasons |
|---|---|---|
| other-habitats.8 | numbers | numbers: the entry keeps "about 31 of 148 datasets reversed", while the critic's full-text check (C-033) gives "13 deviating datasets (3 faster, 10 slower)". |
| other-habitats.11 | stronger | stronger: the entry says marine and host-associated studies "report lower functional turnover", dropping the "mostly" in A-014's "mostly report lower functional turnover". / stronger: the entry says marine and host-associated studies "report lower functional turnover", dropping the text's "mostly report lower functional turnover". |
| unit-annotation-metric.16 | stronger | stronger: the entry says "no study ran both on the same soils", where the text says "I found no study that ran both", turning a search result into a fact. |
