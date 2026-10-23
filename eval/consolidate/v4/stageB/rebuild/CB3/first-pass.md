# First pass: CB3

Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted.

- **First-pass fault rate: 11/92 = 12.0%** (Wilson 6.8% to 20.2%).
- Checker A alone 7, checker B alone 11, both 7; agree (ok against fault) on 88 of 92.
- Per 100 entries: holds + absent 5.4; stronger + numbers 3.3; conf 3.3; critic 0.0; merged 0.0.
- Kinds (entries): holds 3, conf 3, absent 3, stronger 3.

| Packet | Entries | A | B | Either | Agree |
|---|---|---|---|---|---|
| packet-01.md | 60 | 1 | 4 | 4 | 57 |
| packet-02.md | 32 | 6 | 7 | 7 | 31 |

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checkers' reasons |
|---|---|---|
| soil-n2o.4 | stronger | stronger: the cited table row gives the 795 MtCO2 eq input "*medium confidence*", but the entry and its holds drop that standing and state the ~1.5% without it. / stronger: the table row gives the 795 MtCO2 eq share "*medium confidence*", but the entry states "~1.5%" with no hedge and conf "not stated", and holds omits it. |
| dns.1 | stronger | stronger: the why says no boundary "produces five per cent for agriculture", dropping the text's "produces exactly five per cent", which goes on to say three boundaries "land close enough that a 'roughly 5%' claim could have originated from any of them". |
| dns.2 | stronger | stronger: the why says "No boundary produces five per cent for agricultural soils", dropping the text's "exactly", although the same quoted sentence says boundaries "land close enough that a 'roughly 5%' claim could have originated from any of them". / stronger: the why says "No boundary produces five per cent for agricultural soils", dropping "exactly" from the text's "produces exactly five per cent ... and none produces it for agricultural soils". |
