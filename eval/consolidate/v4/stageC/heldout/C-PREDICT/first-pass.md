# First pass: C-PREDICT

Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted.

- **First-pass fault rate: 18/130 = 13.8%** (Wilson 8.9% to 20.8%).
- Checker A alone 17, checker B alone 14, both 13; agree (ok against fault) on 125 of 130.
- Per 100 entries: holds + absent 13.1; stronger + numbers 1.5; conf 0.0; critic 0.0; merged 0.0.
- Kinds (entries): holds 11, absent 6, stronger 2.

| Packet | Entries | A | B | Either | Agree |
|---|---|---|---|---|---|
| packet-01.md | 60 | 6 | 4 | 6 | 58 |
| packet-02.md | 60 | 9 | 8 | 10 | 57 |
| packet-03.md | 10 | 2 | 2 | 2 | 10 |

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checkers' reasons |
|---|---|---|
| hold-out-design.7 | stronger | stronger: "the median is 0 for every group except fungal functional groups" drops the critic's scope "median site-scale 1:1 R2", so a site-scale median is stated for Averill's test at all scales. |
| averill.7 | holds, stronger | holds: holds gives "best-fit R2", but the quoted text says only "site-scale supplementary R2 medians" and never names which of the two measures. / stronger: the entry keeps "fungal medians do not rise cleanly with rank" but drops the contrary finding its text gives, that "Averill et al. 2021 state fungal predictability rises with taxonomic scale" and "the authors' claim may rest on a different summary in the unread main text". |
