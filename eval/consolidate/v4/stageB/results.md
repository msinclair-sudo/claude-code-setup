# Stage B results: gate B

v4's first pass on the 14 rebuilt notes against the re-scored v3, with the same frozen checking procedure (checker.md and hints as at 7b5a0b3; 60-entry packets; two fresh checkers per packet, a fault from either counted). v4 is every entry of every note (1847 entries); v3 is the B2 baseline (300 entries, stratified, weighted to whole notes). The criteria are judged on the point estimates.

Intervals (95%): Wilson for v4's pooled rates; the baseline's bootstrap (seed 20261037) for v3; for each ratio, a bootstrap of 10,000 resamples (seed 20261038, fixed before scoring) resampling v3 within note and stratum and v4's notes as clusters.

16S was built before revision 6 (the `src`/`conf` fix and the clarified builder rule) and was not rebuilt.

## Criteria 1 to 3

| Measure (per 100 entries) | v4 | v4 95% | Re-scored v3 | v3 95% | v4/v3 | Ratio 95% | Criterion | Met |
|---|---|---|---|---|---|---|---|---|
| First-pass fault rate | 9.7 (179/1847) | 8.4 to 11.1 | 38.6 | 33.4 to 43.9 | 0.25 | 0.17 to 0.32 | at most 2/3 | yes |
| holds + absent | 7.9 (145/1847) | 6.7 to 9.2 | 36.1 | 31.1 to 41.3 | 0.22 | 0.14 to 0.29 | at most 1/2 | yes |
| stronger + numbers | 1.4 (26/1847) | 1.0 to 2.1 | 1.9 | 0.5 to 3.6 | 0.75 | 0.31 to 2.67 | not above v3 | yes |
| conf | 0.3 (6/1847) | 0.1 to 0.7 | 0.4 | 0.0 to 1.2 | 0.82 | 0.00 to unbounded | not above v3 | yes |

v3 as it reported itself (one checker, its own packets): 206/1697 = 12.1% first-pass faults, against the re-scored rate above.

Ratio intervals that reach 1 (no difference): stronger + numbers, conf. For criterion 3 that is the test's direction (not above v3); for criteria 1 and 2 it would mean the improvement is not distinguishable from none.

## Criterion 4: omission

| Note | Input | Omission check | Body addresses | Unaddressed sections outside the allow-list |
|---|---|---|---|---|
| 16S | MB-01 | exact (every labelled sentence, every answer sentence, and the critique) | 385 | none |
| 16S | MB-02 | fallback (answers and critique; the note has no labelled citations) | 309 | none |
| H2-01 | H2-01 | exact (every labelled sentence, every answer sentence, and the critique) | 171 | none |
| TSL | TSL | fallback (answers and critique; the note has no labelled citations) | 46 | none |
| CB1 | CB1-LIMING | fallback (answers and critique; the note has no labelled citations) | 147 | none |
| CB2 | CB2-RRNA | fallback (answers and critique; the note has no labelled citations) | 119 | none |
| NFERT | NFERT | fallback (answers and critique; the note has no labelled citations) | 75 | none |
| CB3 | CB3-AG-EMISSIONS | fallback (answers and critique; the note has no labelled citations) | 140 | none |
| GHOST | GHOST | fallback (answers and critique; the note has no labelled citations) | 52 | none |
| TAXRES | TAXRES | fallback (answers and critique; the note has no labelled citations) | 28 | none |
| H1-RES | H1-RES | fallback (answers and critique; the note has no labelled citations) | 170 | none |
| H2-04 | H2-04 | exact (every labelled sentence, every answer sentence, and the critique) | 76 | none |
| H1-05 | H1-05 | exact (every labelled sentence, every answer sentence, and the critique) | 151 | none |
| H1-02 | H1-02 | fallback (answers and critique; the note has no labelled citations) | 191 | none |
| H1-06 | H1-06 | fallback (answers and critique; the note has no labelled citations) | 164 | none |

Met: yes.

## Criterion 5: re-check

| Note | Round 1: fixed, still faulted | Later rounds: still faulted of fixed |
|---|---|---|
| 16S | 68, 2 | 1 of 2; 0 of 1 |
| H2-01 | 10, 0 | none needed |
| TSL | 6, 0 | none needed |
| CB1 | 4, 0 | none needed |
| CB2 | 2, 0 | none needed |
| NFERT | 1, 0 | none needed |
| CB3 | 11, 0 | none needed |
| GHOST | 2, 0 | none needed |
| TAXRES | 6, 0 | none needed |
| H1-RES | 7, 0 | none needed |
| H2-04 | 21, 1 | 0 of 1 |
| H1-05 | 17, 2 | 0 of 2 |
| H1-02 | 14, 0 | none needed |
| H1-06 | 10, 2 | 1 of 2; 0 of 1 |

Round 1, pooled: 7 of 179 fixed entries still faulted = 3.9% (Wilson 1.9% to 7.9%), against at most 15% (v3: 11% development, 14% held-out). Met: yes.

## By note

| Note | Entries | First pass | Re-scored v3 estimate | holds + absent | stronger + numbers | conf |
|---|---|---|---|---|---|---|
| 16S | 560 | 68 (12.1%) | 35% | 53 | 10 | 3 |
| H2-01 | 143 | 10 (7.0%) | 61% | 9 | 1 | 0 |
| TSL | 31 | 6 (19.4%) | 36% | 3 | 3 | 0 |
| CB1 | 145 | 4 (2.8%) | 18% | 3 | 1 | 0 |
| CB2 | 81 | 2 (2.5%) | 32% | 1 | 1 | 0 |
| NFERT | 54 | 1 (1.9%) | 20% | 1 | 0 | 0 |
| CB3 | 92 | 11 (12.0%) | 55% | 5 | 3 | 3 |
| GHOST | 46 | 2 (4.3%) | 23% | 2 | 0 | 0 |
| TAXRES | 30 | 6 (20.0%) | 66% | 5 | 1 | 0 |
| H1-RES | 177 | 7 (4.0%) | 18% | 6 | 1 | 0 |
| H2-04 | 142 | 21 (14.8%) | 27% | 21 | 0 | 0 |
| H1-05 | 119 | 17 (14.3%) | 52% | 14 | 3 | 0 |
| H1-02 | 124 | 14 (11.3%) | 52% | 14 | 0 | 0 |
| H1-06 | 103 | 10 (9.7%) | 38% | 8 | 2 | 0 |

Kinds, v4 (entries): holds 112, absent 38, stronger 23, conf 6, numbers 3, critic 2, merged 1.

## Every `stronger` and `numbers` fault (criterion 3)

### v4

| Note | Entry | Kinds | Checkers' reasons |
|---|---|---|---|
| 16S | primers.2 | stronger | stronger: The entry says "V4 primers under-represented SAR11 and over-represented Gammaproteobacteria", widening the text's "The original 515F/806R V4 primers" to V4 primers in general. |
| 16S | ploidy.3 | stronger | stronger: the entry says this "is the only direct origin and terminus count for E. coli at two growth rates" outright, but the text says only that removing Pecoraro 2011 "would remove the only direct origin and terminus counts" from the review's evidence. |
| 16S | ploidy.18 | stronger | stronger: the entry says "but A. vinelandii rises" where the text says it "is reported to rise ... (SECONDARY, via Bruck et al. 2023 full text)", dropping the hedge and the secondary standing. |
| 16S | ploidy.22 | stronger | stronger: the text says "No source I found measured 16S copies per cell directly in environmental cells", but the entry drops "I found" and states "No source measured 16S copies per cell directly in environmental cells" as a general fact. / stronger: the entry says "No source measured 16S copies per cell directly in environmental cells" where the text says "No source I found measured", dropping the search scope. |
| 16S | community-copy-number.5 | stronger | stronger: the entry says "the EMP gives about 2.2" with no sign that the value is predicted, though its cited critique (C-024) says these copy numbers "are predictions from one source". |
| 16S | denoising-clustering.4 | stronger | stronger: "pipeline choice biased interpretations" is firmer than the critique's "Straub 2020 reports pipeline-dependent interpretations". / stronger: the entry says "pipeline choice biased interpretations", where the text (C-087) says only that Straub 2020 "reports pipeline-dependent interpretations". |
| 16S | bias-consistency.1 | stronger | stronger: the closing clause "bias behaves as a multiplicative factor per taxon that calibration controls can correct" is stated as a general property, dropping the "one dataset modelled for this question" scope the text gives (I-0002 "One reanalysis finds it consistent") and the field evidence of inconsistency in C-129. |
| 16S | scaling-normalisation.4 | stronger | stronger: the text marks the RNA-seq origin citations "(Bullard 2010; Robinson and Oshlack 2010; Anders and Huber 2010, indirect)", but the entry drops "indirect" from both its wording and its src labels. / stronger: the text marks the RNA-seq origin sources "indirect", and the entry drops that qualifier from both the claim and holds. |
| 16S | beta-diversity.5 | stronger | stronger: the text gives a contrary finding, proportions "still depth-sensitive under Schloss's null", which the entry drops while keeping conf single. |
| 16S | abundance-occupancy.8 | stronger | stronger: the entry says "detection limits and neutral or sampling models predict a positive relationship without selection" but drops the text's scope for the detection-limits evidence, "[76, a single 454-era study at one site]". |
| H2-01 | transfer-dependence.1 | stronger | stronger: The entry gives the synthesis as "transfer depends on the similarity of the training set to the target", dropping the hedge in "three dependencies recur" / "transfer appears to depend on similarity between training and target". |
| TSL | collection-df.1 | stronger | stronger: the entry states "specificity is inversely related to df (lower df = more specific)" but drops the caveat its text gives in B-0011, that "df is a *frequency proxy*, not a definition of semantic specificity" and "low df from typos/OCR/identifiers does not imply true specificity". / stronger: the entry states "specificity is inversely related to df (lower df = more specific)" with the high rating but drops the contrary caveat its text attaches to that rating, "low df from typos/OCR/identifiers does not imply true specificity". |
| TSL | information-content.1 | stronger | stronger: the entry gives the IC scheme ("root P = 1, IC = 0", "altitude maps directly onto generality") with the high rating but drops the condition its text attaches to that rating, "Caveat: needs a unified root; WordNet has none naturally". |
| TSL | class-df.1 | stronger | stronger: the entry keeps the first half of A-008 ("operationalises the same inverse-frequency principle at the cluster level") and drops its "but it is an **engineering instantiation, not an independently validated specificity measure**". / stronger: the entry keeps "operationalises the same inverse-frequency principle at the cluster level" but drops the rest of that sentence, "but it is an engineering instantiation, not an independently validated specificity measure". |
| CB1 | liming-effects.6 | stronger | stronger: The entry keeps "reduced N₂O emissions and nitrate leaching" but drops the contrary finding in the same sentence, "but that in CO₂-C equivalents 'the GHG emissions from liming were about four times those saved by reducing N₂O emissions'". / stronger: the entry keeps "liming to pH 6.0 as recommended reduced N₂O emissions and nitrate leaching" but drops the contrary finding the text gives in the same sentence, "but that in CO₂-C equivalents 'the GHG emissions from liming were about four times those saved by reducing N₂O emissions'". |
| CB2 | variation-axes.1 | stronger | stronger: the entry lists "sequencing depth" among the axes with direct evidence and drops the text's qualifier that depth "is measured, but only as simulated per-genome coverage in targeted-assembly benchmarks — not as library depth in a real assemble-and-bin pipeline". / stronger: the entry lists "sequencing depth" among the axes with direct evidence without the text's limit that depth is measured "only as simulated per-genome coverage in targeted-assembly benchmarks — not as library depth in a real assemble-and-bin pipeline". |
| CB3 | soil-n2o.4 | stronger | stronger: the cited table row gives the 795 MtCO2 eq input "*medium confidence*", but the entry and its holds drop that standing and state the ~1.5% without it. / stronger: the table row gives the 795 MtCO2 eq share "*medium confidence*", but the entry states "~1.5%" with no hedge and conf "not stated", and holds omits it. |
| CB3 | dns.1 | stronger | stronger: the why says no boundary "produces five per cent for agriculture", dropping the text's "produces exactly five per cent", which goes on to say three boundaries "land close enough that a 'roughly 5%' claim could have originated from any of them". |
| CB3 | dns.2 | stronger | stronger: the why says "No boundary produces five per cent for agricultural soils", dropping the text's "exactly", although the same quoted sentence says boundaries "land close enough that a 'roughly 5%' claim could have originated from any of them". / stronger: the why says "No boundary produces five per cent for agricultural soils", dropping "exactly" from the text's "produces exactly five per cent ... and none produces it for agricultural soils". |
| TAXRES | fungal-repositories.1 | numbers | numbers: the text gives "Fungi enter via Index Fungorum (114,301 names ...)", the names as they enter the backbone, and the entry restates this as "Index Fungorum holds 114,301 names", dropping the context that defines the figure. |
| H1-RES | n-cycle-vertical.4 | stronger | stronger: the entry says Anand and Chanway "found ... that nifH was transmitted horizontally while nifD was transmitted vertically", dropping the hedge in "phylogenetic analyses suggested nifH was transmitted horizontally". / stronger: the entry says Anand and Chanway "found ... that nifH was transmitted horizontally while nifD was transmitted vertically", dropping the hedge in the text, where "phylogenetic analyses suggested" this. |
| H1-05 | other-habitats.8 | numbers | numbers: the entry keeps "about 31 of 148 datasets reversed", while the critic's full-text check (C-033) gives "13 deviating datasets (3 faster, 10 slower)". |
| H1-05 | other-habitats.11 | stronger | stronger: the entry says marine and host-associated studies "report lower functional turnover", dropping the "mostly" in A-014's "mostly report lower functional turnover". / stronger: the entry says marine and host-associated studies "report lower functional turnover", dropping the text's "mostly report lower functional turnover". |
| H1-05 | unit-annotation-metric.16 | stronger | stronger: the entry says "no study ran both on the same soils", where the text says "I found no study that ran both", turning a search result into a fact. |
| H1-06 | perturbation-response-depth.9 | numbers | numbers: the text says perturbation responses "cluster at roughly genus depth in 16S terms [19, 20, 21]", and the entry replaces this with "tau_D about 0.016 to 0.024", pooling Isobe 2019's 0.016 to 0.020 with Isobe 2020's 0.016 to 0.024 and extending it to the litter study (amend), for which the quoted text gives no tau_D. / numbers: the text says perturbation responses "cluster at roughly genus depth" across [19, 20, 21], while the entry's "tau_D about 0.016 to 0.024" pools [19]'s 0.016 to 0.020 with [20]'s 0.016 to 0.024 and extends the range to the litter study, which has no tau_D in the quoted text. |
| H1-06 | env-preference-depth.2 | absent, stronger | stronger: C-005 says the label "only emerges when natural evidence is set beside engineered results or a preprint that measures a different quantity (CCA loadings)", but the entry drops "or a preprint" and says it emerges "only when" natural evidence is set beside engineered isolate and transplant results. / absent: C-005 says the label emerges when natural evidence is set beside "engineered results or a preprint that measures a different quantity", but the entry moves the preprint onto the natural side and says the label emerges "only when" that evidence "is set beside engineered isolate and transplant results". |

### Re-scored v3 (the baseline sample)

| Note | Entry | Kinds | Checkers' reasons |
|---|---|---|---|
| 16S | ploidy.15 | stronger | stronger: the text says "No source I found measured 16S copies per cell", and the entry drops "I found" to "No source measured". / stronger: the entry says "No source measured 16S copies per cell directly", dropping the text's hedge "No source I found measured". |
| TSL | information-content.1 | stronger | stronger: the entry drops the caveat that comes with the confidence rating, "Caveat: needs a unified root; WordNet has none naturally." / stronger: the entry drops the text's condition "Caveat: needs a unified root; WordNet has none naturally." |
| CB3 | dns.2 | numbers | numbers: the why gives "published estimates range from about 1.5% to 4.1%" for agricultural soils, dropping the text's definition "estimates of N₂O from agricultural soils as a share of global GHG". |
| H1-RES | accessory-function.23 | stronger | stronger: the text says "This pattern suggests that a large fraction of accessory content represents ...", and the entry drops "suggests" to state it as fact. / stronger: the text says "This pattern suggests that a large fraction...", and the entry drops "suggests" to state it flatly. |
| H1-06 | dns.6 | absent, numbers | absent: the quoted statement's "about otu94" and "tau_D about 0.017 to 0.02" are not in the text, which gives "otu97-to-genus rise" and "tau_D ~0.017". / numbers: the quoted phrasing gives "tau_D about 0.017 to 0.02" and "otu94", while the text gives only "tau_D ~0.017" and an "otu97-to-genus rise". |
| H1-06 | metabolic-depth.12 | stronger | stronger: the entry gives absolute depths under "replicates across independent datasets" but drops the text's "the absolute depths are not" [consistent] and "inconsistent in absolute depth between datasets and trees". / stronger: the entry gives absolute depths (e.g. "sulfate reduction 0.039") as part of the replicating pattern but drops the text's "the absolute depths are not" consistent between datasets. |

## Information (not gate criteria)

### Settings kept and near-copies (`tools/notestats.py`)

| Note | v3 claims | v3 with a setting | v4 claims | v4 with a setting | v4/v3 share | v3 near-copies | v4 near-copies |
|---|---|---|---|---|---|---|---|
| 16S | 410 | 341 (83%) | 505 | 411 (81%) | 0.98 | 148 (36%) | 205 (41%) |
| H2-01 | 168 | 152 (90%) | 131 | 108 (82%) | 0.91 | 86 (51%) | 57 (44%) |
| TSL | 29 | 28 (97%) | 25 | 21 (84%) | 0.87 | 13 (45%) | 6 (24%) |
| CB1 | 100 | 93 (93%) | 133 | 124 (93%) | 1.00 | 59 (59%) | 79 (59%) |
| CB2 | 57 | 48 (84%) | 71 | 65 (92%) | 1.09 | 35 (61%) | 34 (48%) |
| NFERT | 41 | 36 (88%) | 50 | 44 (88%) | 1.00 | 26 (63%) | 29 (58%) |
| CB3 | 75 | 73 (97%) | 80 | 75 (94%) | 0.96 | 42 (56%) | 38 (48%) |
| GHOST | 31 | 27 (87%) | 41 | 35 (85%) | 0.98 | 12 (39%) | 16 (39%) |
| TAXRES | 26 | 22 (85%) | 28 | 26 (93%) | 1.10 | 13 (50%) | 17 (61%) |
| H1-RES | 116 | 96 (83%) | 171 | 133 (78%) | 0.94 | 62 (53%) | 108 (63%) |
| H2-04 | 99 | 87 (88%) | 115 | 101 (88%) | 1.00 | 39 (39%) | 52 (45%) |
| H1-05 | 129 | 124 (96%) | 97 | 92 (95%) | 0.99 | 26 (20%) | 18 (19%) |
| H1-02 | 112 | 101 (90%) | 109 | 107 (98%) | 1.09 | 60 (54%) | 48 (44%) |
| H1-06 | 123 | 109 (89%) | 92 | 87 (95%) | 1.07 | 59 (48%) | 46 (50%) |

### The 16S removals

From the 16S builder's own edit scripts (`rebuild/16S/removed-settings.md`), before the revision 6 clarification: 76 removals in 72 entries, all dropped and none kept with an added address. By the builder's account, 42 of the removed details are stated elsewhere in the inputs, 6 partly, 8 not at all and 20 unchecked. Its 16 other fixes added an address. The later builders, given the clarified rule, kept details with addresses; their removals (own wording, or details no addressable sentence gives) are listed per batch in `state.md`.

### Do-not-say readability

One fresh reader, given only the Do not say sections of the 14 writer's views, marked each entry usable by a writer as it stands, or a fragment, with a reason.

- **Usable: 184/199 = 92.5%** (Wilson 87.9% to 95.4%), against the target of at least 90%.

| Note | Entries | Usable |
|---|---|---|
| 16S | 55 | 51 |
| H2-01 | 12 | 11 |
| TSL | 6 | 4 |
| CB1 | 12 | 12 |
| CB2 | 10 | 10 |
| NFERT | 4 | 3 |
| CB3 | 12 | 12 |
| GHOST | 5 | 5 |
| TAXRES | 2 | 1 |
| H1-RES | 6 | 6 |
| H2-04 | 27 | 25 |
| H1-05 | 22 | 20 |
| H1-02 | 15 | 14 |
| H1-06 | 11 | 10 |

Fragments, with the reader's reason:

- 16S/26: there is no "Say instead", and the entry does not say plainly that no replacement exists or how to handle the framing.
- 16S/29: the "Do not write" sentence describes the review's own summary table rather than anything a writer would put in a paper, and the reason leans on "the brief", which the writer cannot see.
- 16S/34: the "Do not write" sentence is about the review's reading process rather than something a writer would plausibly write, and there is no "Say instead".
- 16S/46: there is no "Say instead", and the entry does not say why none is offered.
- H2-01/6: the only "Say instead" is a narration of the review's synthesis and a bare "the critic"'s objection, cited to "the reviewer's synthesis", which gives the writer no wording to use.
- TSL/2: the reason is only a verification vote tally with no statement of what is wrong, and there is no "Say instead".
- TSL/4: there is no "Say instead", and the reason gives only a verification vote tally.
- NFERT/4: the "Say instead" is an unfinished "Whether..." clause that poses an open question rather than a wording the writer can use.
- TAXRES/1: the replacement is about the research process and leans on "the scout" and "harness verification", which the writer cannot see; nothing in it belongs in a paper.
- H2-04/18: the "Do not write" sentence is about the review's reading process, the reason leans on "FT-s", "the protocol's access categories" and "the review's own legend", and there is no "Say instead".
- H2-04/23: there is no "Say instead", and the entry does not say plainly that no replacement exists.
- H1-05/13: the "Do not write" sentence is about the review's reading process rather than something a writer would put in a paper, and there is no "Say instead".
- H1-05/14: the "Do not write" sentence is about the review's reading process, and the "Say instead" is a verbless phrase that does not address the access problem.
- H1-02/10: the "Do not write" sentence is about the review's sensitivity check rather than something a writer would plausibly write, and the reason leans on the "verdict" and a bare "the critic".
- H1-06/11: the "Say instead" asserts the same untested natural-to-engineered correspondence that the reason says the sources do not test.

**Borderline passes, as the reader reported them.** The reader marked 14 entries usable that would be fragments under a strict reading of "references the writer cannot see":
- 7 have reasons that cite section numbers, item codes or a bare "the critic" but still make sense without them: 16S/2, H2-01/4, H2-04/4, H1-02/9, H1-06/1, H1-06/4 and H1-06/8.
- 4 have reasons that lead with a verification vote but also say what holds: TSL/1, TSL/3, GHOST/1 and GHOST/2.
- 3 have one usable "Say instead" beside an unusable one: H2-01/1, H1-02/7 and H1-RES/5.

Counting these as fragments gives 170 of 199 usable (85.4%), below the 90% target.

The fragments fall into five kinds:
- no "Say instead" and no reason why none is given (4);
- a "Do not write" sentence about the review's own process, which a writer would not put in a paper (6);
- a reason that is only a vote tally (1);
- a "Say instead" that leans on items the writer cannot see or is unfinished (3);
- a "Say instead" that contradicts the reason (1).

## Gate B

- Criterion 1 (first-pass rate): met.
- Criterion 2 (holds + absent): met.
- Criterion 3 (stronger + numbers; conf): met (stronger + numbers met, conf met).
- Criterion 4 (omission): met.
- Criterion 5 (re-check): met.

**All five criteria are met.** The development notes informed this plan, so passing here is necessary, not sufficient; stage C is the real test. The owner decides.
