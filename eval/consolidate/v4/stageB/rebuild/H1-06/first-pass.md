# First pass: H1-06

Frozen procedure: checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted.

- **First-pass fault rate: 10/103 = 9.7%** (Wilson 5.4% to 17.0%).
- Checker A alone 6, checker B alone 10, both 6; agree (ok against fault) on 99 of 103.
- Per 100 entries: holds + absent 7.8; stronger + numbers 1.9; conf 0.0; critic 1.0; merged 0.0.
- Kinds (entries): holds 7, numbers 1, stronger 1, absent 1, critic 1.

| Packet | Entries | A | B | Either | Agree |
|---|---|---|---|---|---|
| packet-01.md | 60 | 4 | 7 | 7 | 57 |
| packet-02.md | 43 | 2 | 3 | 3 | 42 |

## Every `stronger` and `numbers` fault (gate B, criterion 3)

| Entry | Kinds | Checkers' reasons |
|---|---|---|
| perturbation-response-depth.9 | numbers | numbers: the text says perturbation responses "cluster at roughly genus depth in 16S terms [19, 20, 21]", and the entry replaces this with "tau_D about 0.016 to 0.024", pooling Isobe 2019's 0.016 to 0.020 with Isobe 2020's 0.016 to 0.024 and extending it to the litter study (amend), for which the quoted text gives no tau_D. / numbers: the text says perturbation responses "cluster at roughly genus depth" across [19, 20, 21], while the entry's "tau_D about 0.016 to 0.024" pools [19]'s 0.016 to 0.020 with [20]'s 0.016 to 0.024 and extends the range to the litter study, which has no tau_D in the quoted text. |
| env-preference-depth.2 | absent, stronger | stronger: C-005 says the label "only emerges when natural evidence is set beside engineered results or a preprint that measures a different quantity (CCA loadings)", but the entry drops "or a preprint" and says it emerges "only when" natural evidence is set beside engineered isolate and transplant results. / absent: C-005 says the label emerges when natural evidence is set beside "engineered results or a preprint that measures a different quantity", but the entry moves the preprint onto the natural side and says the label emerges "only when" that evidence "is set beside engineered isolate and transplant results". |
