# First pass: C-DENIT

Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted.

- **First-pass fault rate: 39/191 = 20.4%** (Wilson 15.3% to 26.7%).
- Checker A alone 32, checker B alone 34, both 27; agree (ok against fault) on 179 of 191.
- Per 100 entries: holds + absent 17.3; stronger + numbers 2.1; conf 0.5; critic 1.0; merged 0.0.
- Kinds (entries): holds 22, absent 11, stronger 3, critic 2, conf 1, numbers 1.

| Packet | Entries | A | B | Either | Agree |
|---|---|---|---|---|---|
| packet-01.md | 60 | 9 | 10 | 12 | 55 |
| packet-02.md | 60 | 11 | 13 | 13 | 58 |
| packet-03.md | 60 | 7 | 7 | 8 | 58 |
| packet-04.md | 11 | 5 | 4 | 6 | 8 |

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checkers' reasons |
|---|---|---|
| reconciliation.3 | stronger | stronger: the entry drops the cited condition that "Event counts depend on fixed penalties (HGT 3, duplication 2, loss 1)" and that "the method is deep-time", keeping only the taxon-sampling caveat. |
| primer-bias.3 | numbers | numbers: the text attributes "nearly half of 227" to Heylen2006 and "70% gave no norB amplicon" to Heylen2007, but the entry joins them in one sentence so that the 70% reads as a share of the same 227 denitrifiers. |
| primer-bias.5 | holds, stronger | stronger: the text limits the claim to "Every primer-based habitat result in 3.1", but the entry drops "in 3.1" and extends it to "the primer-based habitat studies the review covers". / holds: the text limits the claim to "every primer-based habitat result in 3.1", while holds widens it to "the primer-based habitat studies the review covers". |
| dns.20 | stronger | stronger: The why says "their labels support a negative claim", but the text says the labels "are also used to support a negative claim", which is the critique's objection, not an endorsement. |
