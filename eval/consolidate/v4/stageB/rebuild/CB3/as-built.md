---
type: knowledge
title: Agriculture's share of global greenhouse gas emissions
inputs:
  - CB3-AG-EMISSIONS: PhD/Proposal/Research/Results/Agriculture's Share of Global Greenhouse Gas Emissions by Accounting Boundary.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-23
status: draft
tags:
  - research
  - knowledge
---

# Agriculture's share of global greenhouse gas emissions

> [!abstract] Note Role
> **Contains**: what the research in the inputs found, one claim per finding, organised by concept, with the
> standing, conditions and sources the notes give, and links back to where each was verified.
> **Cannot contain**: anything not in the inputs (except background entries, marked), verification (it stays
> in the result notes), or guidance on writing, story or order of telling.
> **Order**: the concepts are listed in one valid ordering of the `needs` graph. It has no narrative meaning;
> other valid orderings are equally correct.

## Inputs
| id | note | critique | citations | standing labels | run record | omission check |
|---|---|---|---|---|---|---|
| CB3-AG-EMISSIONS | [[Agriculture's Share of Global Greenhouse Gas Emissions by Accounting Boundary]] | no (the note says none ran) | numbered | no | no | fallback (answers and critique; the note has no labelled citations) |

## Concepts

### accounting-boundary: accounting boundaries for agriculture's emissions
needs: none
- **accounting-boundary.1** The question of what share of global emissions is agriculture has no single answer, because four different accounting boundaries are in routine use, each defensible, each producing a number between roughly 2% and 42%.
  conf: not stated · class: not stated · holds: the four accounting boundaries in routine use · src: none (the reviewer's synthesis) · trail: CB3-AG-EMISSIONS §1. What this review · from: CB3-AG-EMISSIONS:B-0011

### ghg-metric: emission metrics and gas coverage
needs: none
- **ghg-metric.1** EDGAR-FOOD and FAOSTAT aggregate emissions with AR5 GWP100 (CH4 = 28, N2O = 265), while AR6 uses AR6 GWP100 with climate–carbon feedbacks (CH4 = 27, N2O = 273).
  conf: not stated · class: not stated · holds: the metric, one of the reasons the major sources differ · src: crippaFoodSystemsResponsible2021, tubielloPrePostproductionProcesses2022, nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §6. Where the major, §3. Boundary B · from: CB3-AG-EMISSIONS:B-0037, CB3-AG-EMISSIONS:B-0086
- **ghg-metric.2** AR6 warns that "The choice of metric depends on the purpose of the analysis and all GHG emission metrics have limitations and uncertainties".
  conf: not stated · class: not stated · holds: GHG emission metrics in general · src: ipccSummaryPolicymakers2022 · trail: CB3-AG-EMISSIONS §6. Where the major · from: CB3-AG-EMISSIONS:B-0087
- **ghg-metric.3** On gas coverage, SRCCL's 23% covers only CO2, CH4 and N2O, while EDGAR-FOOD and FAOSTAT include F-gases.
  conf: not stated · class: not stated · holds: gas coverage, one of the reasons the major sources differ · src: ipccSummaryPolicymakers2019, crippaFoodSystemsResponsible2021, tubielloPrePostproductionProcesses2022 · trail: CB3-AG-EMISSIONS §6. Where the major · from: CB3-AG-EMISSIONS:B-0088
- **ghg-metric.4** Lynch et al. argue that GWP100 CO2-equivalent reporting misrepresents agriculture's warming contribution, because agriculture is dominated by CH4 and N2O rather than CO2: "conventional reporting of aggregated CO2-equivalent emission rates is highly ambiguous and does not straightforwardly reflect historical or anticipated contributions to global temperature change".
  conf: not stated · class: not stated · holds: GWP100 CO2-equivalent reporting of agriculture's emissions · src: lynchAgricultureSContribution2021 · trail: CB3-AG-EMISSIONS §7. Bounding · from: CB3-AG-EMISSIONS:B-0095
- **ghg-metric.5** Lynch et al. do not offer a replacement share: their criticism attacks the aggregation, not the inventory.
  conf: not stated · class: not stated · holds: the metric criticism by Lynch et al. · src: lynchAgricultureSContribution2021 · trail: CB3-AG-EMISSIONS §7. Bounding · from: CB3-AG-EMISSIONS:B-0095, CB3-AG-EMISSIONS:B-0096
- **ghg-metric.6** The direction of the effect Lynch et al. describe is not uniformly downward: they also state that "the impact of increasing methane emissions at rates above ~1% per year will be understated by reporting using GWP100 CO2e".
  conf: not stated · class: not stated · holds: methane emissions increasing at rates above ~1% per year, under GWP100 CO2e reporting · src: lynchAgricultureSContribution2021 · trail: CB3-AG-EMISSIONS §7. Bounding · from: CB3-AG-EMISSIONS:B-0095, CB3-AG-EMISSIONS:B-0097

### global-denominator: the global total that shares are taken of
needs: none
- **global-denominator.1** FAOSTAT uses a global total of 53.5 Gt CO2eq for 2022; AR6 uses 59 ± 6.6 Gt for 2019 and 55.9 ± 6.1 Gt for the 2010–2019 mean.
  conf: not stated · class: not stated · holds: the denominator, one of the reasons the major sources differ · src: faoGreenhouseGasEmissions2024, ipccSummaryPolicymakers2022, nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §6. Where the major · from: CB3-AG-EMISSIONS:B-0083
- **global-denominator.2** The same numerator over these denominators (53.5, 59 and 55.9 Gt) shifts a share by several points.
  conf: not stated · class: not stated · holds: the FAOSTAT and AR6 global totals · src: none (the reviewer's statement) · trail: CB3-AG-EMISSIONS §6. Where the major · from: CB3-AG-EMISSIONS:B-0083, CB3-AG-EMISSIONS:B-0084
- **global-denominator.3** Neither FAO brief the review read explains the gap between FAOSTAT's and AR6's global totals.
  conf: not stated · class: search (note: "Neither FAO brief I read explains the gap") · holds: the FAO briefs the review read · src: none (a statement about the sources the review read) · trail: CB3-AG-EMISSIONS §6. Where the major · from: CB3-AG-EMISSIONS:B-0083, CB3-AG-EMISSIONS:B-0085 · search: searched, not found (note: "Neither FAO brief I read explains the gap")

### co2-accounting: CO2 accounting methods for land use
needs: none
- **co2-accounting.1** The CO2 accounting method, bookkeeping models against national inventories or FAOSTAT, moves AFOLU's share between 13% and 21%, as AR6 states directly.
  conf: not stated · class: not stated · holds: AFOLU's share in AR6 · src: nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §6. Where the major · from: CB3-AG-EMISSIONS:B-0080, CB3-AG-EMISSIONS:B-0081
- **co2-accounting.2** The AR6 Figure 7.3 caption warns that AFOLU CO2 from bookkeeping models "is not directly comparable to LULUCF in NGHGIs".
  conf: not stated · class: not stated · holds: AFOLU CO2 from bookkeeping models against LULUCF in national greenhouse-gas inventories · src: nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §6. Where the major, §7. Bounding · from: CB3-AG-EMISSIONS:B-0082, CB3-AG-EMISSIONS:B-0094

### food-system: Boundary A, the whole food or agrifood system
needs: accounting-boundary, ghg-metric, global-denominator
- **food-system.1** The food-system boundary is the broadest: farm-gate production, plus land-use change attributed to agriculture, plus everything up- and downstream (fertiliser manufacture, processing, packaging, transport, retail, household cooking, food waste disposal).
  conf: not stated · class: not stated · holds: the whole food system or agrifood system boundary · src: none (the reviewer's description of the boundary) · trail: CB3-AG-EMISSIONS §2. Boundary A · from: CB3-AG-EMISSIONS:B-0017
- **food-system.2** IPCC SRCCL gave the food system 21–37% of total net anthropogenic GHG emissions for 2007–2016, with medium confidence.
  conf: not stated · class: not stated · holds: 2007–2016; CO2, CH4 and N2O; IPCC's own assessed medium confidence · src: ipccSummaryPolicymakers2019 · trail: CB3-AG-EMISSIONS §2. Boundary A, §8. Table · from: CB3-AG-EMISSIONS:B-0018, CB3-AG-EMISSIONS:B-0107
- **food-system.3** Emissions within the farm gate and from agricultural land expansion contributing to the global food system represent 16–27% of total anthropogenic emissions, with medium confidence.
  conf: not stated · class: not stated · holds: farm gate plus agricultural land expansion; 2007–2016; CO2, CH4 and N2O; IPCC SRCCL, section A.3.6, with IPCC's own assessed medium confidence · src: ipccSummaryPolicymakers2019 · trail: CB3-AG-EMISSIONS §2. Boundary A, §8. Table · from: CB3-AG-EMISSIONS:B-0018, CB3-AG-EMISSIONS:B-0019, CB3-AG-EMISSIONS:B-0114
- **food-system.4** Emissions outside the farm gate represent 5–10% of total anthropogenic emissions, with medium confidence.
  conf: not stated · class: not stated · holds: outside the farm gate only; 2007–2016; CO2, CH4 and N2O; IPCC SRCCL, section A.3.6, with IPCC's own assessed medium confidence · src: ipccSummaryPolicymakers2019 · trail: CB3-AG-EMISSIONS §2. Boundary A, §8. Table · from: CB3-AG-EMISSIONS:B-0018, CB3-AG-EMISSIONS:B-0019, CB3-AG-EMISSIONS:B-0115
- **food-system.5** Crippa et al. 2021 (EDGAR-FOOD) put food systems at 18 Gt CO2e in 2015, 34% of total GHG, with a stated 95% confidence interval of 14–22 Gt CO2e.
  conf: not stated · class: not stated · holds: the EDGAR-FOOD food system, 2015; CO2, CH4, N2O and F-gases aggregated with AR5 GWP100 (CH4 = 28, N2O = 265) · src: crippaFoodSystemsResponsible2021 · trail: CB3-AG-EMISSIONS §2. Boundary A, §7. Bounding, §8. Table · from: CB3-AG-EMISSIONS:B-0020, CB3-AG-EMISSIONS:B-0021, CB3-AG-EMISSIONS:B-0101, CB3-AG-EMISSIONS:B-0108 · contrary: searched (note: "I searched specifically for published criticism or formal comment disputing the EDGAR-FOOD")
- **food-system.6** No published criticism or formal comment disputing the EDGAR-FOOD "one third" figure or its land-use attribution was found; the qualifications on that figure come from its own authors and from boundary comparisons (Tubiello, OWID), not from an adversarial literature.
  conf: not stated · class: search (note: "I searched specifically for published criticism") · holds: the review's specific search for published criticism or formal comment; the review calls the result absence of published criticism, not endorsement · src: none (a statement about the review's own search) · trail: CB3-AG-EMISSIONS §7. Bounding · from: CB3-AG-EMISSIONS:B-0101, CB3-AG-EMISSIONS:B-0102, CB3-AG-EMISSIONS:B-0103 · search: searched, not found (note: "I searched specifically for published criticism or formal comment disputing the EDGAR-FOOD")
- **food-system.7** Tubiello et al. 2022 (FAOSTAT) put agrifood systems at 16.5 Gt CO2eq in 2019, 31% (range 19–43%), the range coming from an assigned uncertainty of 30% on farm gate and pre/post-production and 50% on land-use change.
  conf: not stated · class: not stated · holds: the FAOSTAT agrifood system, 2019; four gases; AR5 GWP100 · src: tubielloPrePostproductionProcesses2022 · trail: CB3-AG-EMISSIONS §2. Boundary A, §8. Table · from: CB3-AG-EMISSIONS:B-0022, CB3-AG-EMISSIONS:B-0109
- **food-system.8** Uncertainty in the food-system estimates is large and mostly not statistical: EDGAR-FOOD's 95% confidence interval is 14–22 Gt on an 18 Gt central estimate, and FAOSTAT's 19–43% range on a 31% central estimate comes from assigned, not estimated, uncertainties, which Tubiello et al. say "are meant only as first rough estimates".
  conf: not stated · class: not stated · holds: the EDGAR-FOOD and FAOSTAT food-system estimates · src: crippaFoodSystemsResponsible2021, tubielloPrePostproductionProcesses2022 · trail: CB3-AG-EMISSIONS §7. Bounding · from: CB3-AG-EMISSIONS:B-0104
- **food-system.9** Tubiello et al. 2021 gave 33% for 2018 and reconciled it with Crippa et al.: "Our estimate of 16 Gt CO2 eq yr−1 in 2018 is consistent with their findings, also considering their stated uncertainty range of 14–22 Gt CO2 eq yr−1".
  conf: not stated · class: not stated · holds: the FAOSTAT food system, 2018, against EDGAR-FOOD's stated uncertainty range · src: tubielloGreenhouseGasEmissions2021 · trail: CB3-AG-EMISSIONS §2. Boundary A · from: CB3-AG-EMISSIONS:B-0022, CB3-AG-EMISSIONS:B-0023
- **food-system.10** Tubiello et al. concede that their own land-use-change component is probably too high: "recent studies have estimated that only 80% of deforestation may be linked to agriculture globally ... We are thus likely overestimating the food-related land use change component".
  conf: not stated · class: not stated · holds: the land-use-change component of the FAOSTAT food-system estimate · src: tubielloGreenhouseGasEmissions2021 · trail: CB3-AG-EMISSIONS §6. Where the major · from: CB3-AG-EMISSIONS:B-0091, CB3-AG-EMISSIONS:B-0092
- **food-system.11** IPCC AR6 WGIII Chapter 12 widened the band again: "Some 23–42% of global GHG emissions are associated with food systems", with absolute emissions rising "from 14 to 17 GtCO2-eq yr-1 in the period 1990–2018".
  conf: not stated · class: not stated · holds: food systems including all of the supply chain, 1990–2018; AR6 GWP100; a range only; the chapter read only by targeted text extraction of its food-system statements · src: babikerCrosssectoralPerspectives2022 (targeted text extraction of the food-system statements only) · trail: CB3-AG-EMISSIONS §2. Boundary A, §1. What this review, §8. Table · from: CB3-AG-EMISSIONS:B-0014, CB3-AG-EMISSIONS:B-0024, CB3-AG-EMISSIONS:B-0106 · limit: access (note: "Read only as abstract or publisher metadata, not full text")
- **food-system.12** FAOSTAT's own share is falling and has been revised: Analytical Brief 94 reports 16.2 Gt CO2eq for 2022 against a global total of 53.5 Gt, 29.7%, "below 30 percent for the first time on record", down from 38% in 2000.
  conf: not stated · class: not stated · holds: the FAOSTAT agrifood system, 2022 against 2000; four gases; AR5 GWP100; no uncertainty stated in the brief · src: faoGreenhouseGasEmissions2024 · trail: CB3-AG-EMISSIONS §2. Boundary A, §8. Table · from: CB3-AG-EMISSIONS:B-0025, CB3-AG-EMISSIONS:B-0110
- **food-system.13** FAO's 2025 release for 2023 gives agrifood systems 16.5 Gt; the FAO web summary says the share "fell from 38 to 32 percent in 2023", while FAO's own COP30 takeaways document for the same report says it "decreased from 40 percent to 30 percent": two FAO communications about one release disagree by two percentage points.
  conf: cont (note: "two FAO communications about one release disagree by two percentage points") · class: not stated · holds: the FAOSTAT agrifood system, 2023; no uncertainty stated; the brief's own text was not obtained, only the FAO web summary and the COP30 takeaways PDF · src: faoGreenhouseGasEmissions2025a (FAO web summary), faoGreenhouseGasEmissions2025b (COP30 takeaways) · trail: CB3-AG-EMISSIONS §2. Boundary A, §7. Bounding, §8. Table · from: CB3-AG-EMISSIONS:B-0014, CB3-AG-EMISSIONS:B-0026, CB3-AG-EMISSIONS:B-0027, CB3-AG-EMISSIONS:B-0100, CB3-AG-EMISSIONS:B-0111 · limit: access (note: "I could not obtain the brief's own text to adjudicate")
- **food-system.14** Poore & Nemecek 2018 sit deliberately lower because their boundary is narrower: "Today's food supply chain creates ~13.7 billion metric tons of carbon dioxide equivalents (CO2eq), 26% of anthropogenic GHG emissions"; their accounting stops at retail and excludes consumer cooking and waste.
  conf: not stated · class: not stated · holds: the food supply chain to retail, food only; ~2010 baseline; CO2, CH4 and N2O; uncertainty not stated in the headline · src: pooreReducingFoodS2018 · trail: CB3-AG-EMISSIONS §2. Boundary A, §8. Table · from: CB3-AG-EMISSIONS:B-0028, CB3-AG-EMISSIONS:B-0030, CB3-AG-EMISSIONS:B-0112
- **food-system.15** A further 2.8 billion metric tons of CO2eq (5%) are caused by nonfood agriculture and other drivers of deforestation.
  conf: not stated · class: not stated · holds: non-food agriculture and other deforestation drivers, on the same baseline, gases and metric as the food supply chain figure; uncertainty not stated; Poore & Nemecek 2018 · src: pooreReducingFoodS2018 · trail: CB3-AG-EMISSIONS §2. Boundary A, §8. Table · from: CB3-AG-EMISSIONS:B-0028, CB3-AG-EMISSIONS:B-0029, CB3-AG-EMISSIONS:B-0112, CB3-AG-EMISSIONS:B-0113
- **food-system.16** Poore & Nemecek stop at retail and count only food, while Crippa and FAOSTAT include consumption and waste.
  conf: not stated · class: not stated · holds: supply-chain cut-off, one of the reasons the major sources differ · src: none (the review cites no source for this sentence) · trail: CB3-AG-EMISSIONS §6. Where the major · from: CB3-AG-EMISSIONS:B-0089
- **food-system.17** OWID identifies exactly three causes of the gap between 26% and 34%: consumer cooking and waste, disagreement over how much deforestation to attribute to agriculture, and whether non-food agricultural products are counted.
  conf: not stated · class: not stated · holds: Poore & Nemecek's 26% against Crippa's 34% · src: ritchieSectorSectorWhere2020 · trail: CB3-AG-EMISSIONS §6. Where the major · from: CB3-AG-EMISSIONS:B-0089, CB3-AG-EMISSIONS:B-0090
- **food-system.18** SRCCL footnote 22 states that food-system "emissions data are not directly comparable to the national inventories prepared according to the 2006 IPCC Guidelines for National Greenhouse Gas Inventories".
  conf: not stated · class: not stated · holds: food-system emissions data against national inventories · src: ipccSummaryPolicymakers2019 · trail: CB3-AG-EMISSIONS §7. Bounding · from: CB3-AG-EMISSIONS:B-0093
- **food-system.19** For the food-system boundary, the review names IPCC AR6 WGIII Chapter 12 (23–42%) and SRCCL (21–37%) as authoritative for a range with an assessed confidence level, FAOSTAT for an annually updated inventory-consistent number, and EDGAR-FOOD for an independent database.
  conf: not stated · class: not stated · holds: the food-system boundary · src: babikerCrosssectoralPerspectives2022, ipccSummaryPolicymakers2019, tubielloPrePostproductionProcesses2022, faoGreenhouseGasEmissions2024, faoGreenhouseGasEmissions2025a, crippaFoodSystemsResponsible2021 · trail: CB3-AG-EMISSIONS §2. Boundary A · from: CB3-AG-EMISSIONS:B-0031, CB3-AG-EMISSIONS:B-0032, CB3-AG-EMISSIONS:B-0033

### afolu: Boundary B, agriculture, forestry and other land use (AFOLU)
needs: accounting-boundary, co2-accounting, ghg-metric
- **afolu.1** The AFOLU (managed land) sector, on average, accounted for 13–21% of global total anthropogenic GHG emissions in 2010–2019, with medium confidence.
  conf: not stated · class: not stated · holds: 2010–2019; CO2, CH4 and N2O; AR6 GWP100 with climate–carbon feedbacks (CH4 = 27, N2O = 273); IPCC AR6 WGIII Chapter 7, with IPCC's own assessed medium confidence · src: nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §3. Boundary B · from: CB3-AG-EMISSIONS:B-0034, CB3-AG-EMISSIONS:B-0036, CB3-AG-EMISSIONS:B-0037
- **afolu.2** The 13–21% spread is not statistical noise but two different CO2 accounting methods: 11.9 ± 4.4 GtCO2eq of a total 55.9 ± 6.1 GtCO2eq gives 21% using bookkeeping models for the CO2 component, and FAOSTAT/NGHGI CO2 flux data give 13%.
  conf: not stated · class: not stated · holds: AFOLU, 2010–2019 mean; AR6 WGIII Chapter 7, §7.2.1; medium confidence for both · src: nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §3. Boundary B, §8. Table · from: CB3-AG-EMISSIONS:B-0035, CB3-AG-EMISSIONS:B-0116, CB3-AG-EMISSIONS:B-0117
- **afolu.3** The AR6 Summary for Policymakers gives AFOLU approximately 22% (13 GtCO2-eq) in 2019, against global net anthropogenic emissions of 59 ± 6.6 GtCO2-eq; it is a single year rather than a decadal mean, which is why it exceeds the chapter's 21%.
  conf: not stated · class: not stated · holds: 2019, a single year · src: ipccSummaryPolicymakers2022 · trail: CB3-AG-EMISSIONS §3. Boundary B, §8. Table · from: CB3-AG-EMISSIONS:B-0038, CB3-AG-EMISSIONS:B-0039, CB3-AG-EMISSIONS:B-0118
- **afolu.4** The AR6 Summary for Policymakers' 22% and the chapter's 13–21% are the same assessment on different periods and CO2 conventions, not rival estimates.
  conf: not stated · class: not stated · holds: the two AR6 AFOLU figures · src: none (the reviewer's reading of the two AR6 figures) · trail: CB3-AG-EMISSIONS §3. Boundary B · from: CB3-AG-EMISSIONS:B-0038, CB3-AG-EMISSIONS:B-0040
- **afolu.5** SRCCL reported AFOLU at "23% (12.0 ± 2.9 GtCO2eq yr-1) of total net anthropogenic emissions of GHGs (medium confidence)" for 2007–2016, an assessment that includes only CO2, CH4 and N2O; AR6 supersedes it with 13–21% for 2010–2019.
  conf: not stated · class: not stated · holds: SRCCL, 2007–2016, superseded by AR6 for 2010–2019 · src: ipccSummaryPolicymakers2019, nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §3. Boundary B, §7. Bounding, §8. Table · from: CB3-AG-EMISSIONS:B-0041, CB3-AG-EMISSIONS:B-0042, CB3-AG-EMISSIONS:B-0099, CB3-AG-EMISSIONS:B-0119
- **afolu.6** In the Climate Watch/WRI breakdown for 2016, as presented by Our World in Data, Agriculture, Forestry and Land Use totals 18.4%, with livestock and manure 5.8%, rice 1.3%, crop burning 3.5% and deforestation 2.2%.
  conf: not stated · class: not stated · holds: 2016; GWP100; no uncertainty given · src: ritchieSectorSectorWhere2020, climate (as presented by Our World in Data) · trail: CB3-AG-EMISSIONS §5. Boundary D, §8. Table · from: CB3-AG-EMISSIONS:B-0059, CB3-AG-EMISSIONS:B-0061, CB3-AG-EMISSIONS:B-0120
- **afolu.7** AR6 Figure 7.3 subdivides 2019 AFOLU emissions (13 Gt) by activity: LULUCF (CO2) 51%, enteric fermentation (CH4) 23%, managed soils and pasture (CO2, N2O) 11%, rice cultivation (CH4) 8%, manure management (N2O, CH4) 3%, synthetic fertilizer application (N2O) 3%, biomass burning (CH4, N2O) 1%.
  conf: not stated · class: not stated · holds: AFOLU, 2019; CH4 and N2O data from EDGAR; shares read off the rendered figure, not the text · src: nabuursAgricultureForestryOther2022 (shares read off the rendered figure) · trail: CB3-AG-EMISSIONS §5. Boundary D · from: CB3-AG-EMISSIONS:B-0054, CB3-AG-EMISSIONS:B-0055 · limit: access (note: "I read these shares off the rendered figure, not the text")

### farm-gate: Boundary C, agricultural production alone (farm gate)
needs: accounting-boundary, ghg-metric, global-denominator
- **farm-gate.1** Average non-CO2 emissions from agriculture, aggregated using AR6 GWP100 values, rose from 5.2 ± 1.4 GtCO2-eq yr−1 in 1990–1999 to 6.0 ± 1.7 GtCO2-eq yr−1 in 2010–2019.
  conf: not stated · class: not stated · holds: agriculture, non-CO2 only; AR6 WGIII Chapter 7, §7.2.1, which cites Crippa et al. 2021 for it · src: nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §4. Boundary C · from: CB3-AG-EMISSIONS:B-0043
- **farm-gate.2** By the reviewer's arithmetic, 6.0 / 55.9 Gt puts agricultural production at 10.7% of total net anthropogenic GHG for 2010–2019.
  conf: not stated · class: deriv (note: "My arithmetic") · holds: agricultural production, non-CO2 only (CH4 and N2O); AR6 GWP100; 2010–2019; ±1.7 Gt as stated · src: nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §4. Boundary C, §8. Table · from: CB3-AG-EMISSIONS:B-0043, CB3-AG-EMISSIONS:B-0044, CB3-AG-EMISSIONS:B-0121
- **farm-gate.3** AR6's component figures for agriculture are CH4 157.0 ± 47.1 MtCH4 yr−1 (4.2 ± 1.3 GtCO2-eq) and N2O 6.6 ± 4.0 MtN2O yr−1 (1.8 ± 1.1 GtCO2-eq), with assessed uncertainties of 30% and 60% respectively.
  conf: not stated · class: not stated · holds: agriculture; AR6 WGIII Chapter 7, Table 7.1 · src: nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §4. Boundary C · from: CB3-AG-EMISSIONS:B-0043, CB3-AG-EMISSIONS:B-0045
- **farm-gate.4** FAOSTAT's farm gate, a slightly wider boundary that includes on-farm energy CO2, was 7.8 Gt CO2eq in 2022, 48% of agrifood systems emissions.
  conf: not stated · class: not stated · holds: the FAOSTAT farm gate, including on-farm energy CO2; 2022 · src: faoGreenhouseGasEmissions2024 · trail: CB3-AG-EMISSIONS §4. Boundary C · from: CB3-AG-EMISSIONS:B-0046
- **farm-gate.5** FAOSTAT's farm gate was 8.1 Gt in 2023.
  conf: not stated · class: not stated · holds: the FAOSTAT farm gate, 2023; from FAO's 2025 release, of which only the FAO web summary and COP30 takeaways were retrieved, not the brief's own text · src: faoGreenhouseGasEmissions2025a (FAO web summary) · trail: CB3-AG-EMISSIONS §4. Boundary C, §1. What this review · from: CB3-AG-EMISSIONS:B-0014, CB3-AG-EMISSIONS:B-0046 · limit: access (note: "Read only as abstract or publisher metadata, not full text")
- **farm-gate.6** By the reviewer's arithmetic, 7.8 / 53.5 Gt puts FAOSTAT's farm gate at 14.6% of FAO's global total for 2022.
  conf: not stated · class: deriv (note: "My arithmetic") · holds: the FAOSTAT farm gate including on-farm energy CO2; 2022; four gases; AR5 GWP100; 30% assigned uncertainty · src: faoGreenhouseGasEmissions2024 · trail: CB3-AG-EMISSIONS §4. Boundary C, §8. Table · from: CB3-AG-EMISSIONS:B-0046, CB3-AG-EMISSIONS:B-0047, CB3-AG-EMISSIONS:B-0122
- **farm-gate.7** The difference between FAO's 14.6% and the IPCC's 10.7% is partly gases (FAO adds on-farm CO2), partly database, partly the denominator (53.5 against 55.9–59 Gt).
  conf: not stated · class: not stated · holds: the FAOSTAT farm-gate share against the IPCC agricultural non-CO2 share · src: none (the reviewer's reading) · trail: CB3-AG-EMISSIONS §4. Boundary C · from: CB3-AG-EMISSIONS:B-0047, CB3-AG-EMISSIONS:B-0048

### livestock: livestock as a sub-boundary
needs: farm-gate, ghg-metric
- **livestock.1** Livestock's Long Shadow (2006) put livestock at 18% of total GHG.
  conf: not stated · class: not stated · holds: livestock, a sub-boundary with a documented revision history · src: anonLivestockSLong2006 (via Gerber et al. 2013's Annex) · trail: CB3-AG-EMISSIONS §4. Boundary C · from: CB3-AG-EMISSIONS:B-0049, CB3-AG-EMISSIONS:B-0050
- **livestock.2** Gerber et al. 2013 revised the livestock figure to "7.1 gigatonnes CO2-eq per annum, representing 14.5 percent of all human-induced emissions".
  conf: not stated · class: not stated · holds: the livestock supply chain, ~2005; CO2, CH4 and N2O · src: gerberTacklingClimateChange2013 · trail: CB3-AG-EMISSIONS §4. Boundary C, §8. Table · from: CB3-AG-EMISSIONS:B-0049, CB3-AG-EMISSIONS:B-0050, CB3-AG-EMISSIONS:B-0123
- **livestock.3** Gerber et al. 2013's Annex states the reasons for revising Livestock's Long Shadow's 18%: a new GIS-based model (GLEAM) instead of statistical tables, a different reference period, IPCC 2006 rather than 2001 guidelines, different GWP values (296/298 for N2O and 23/25 for CH4 across the two reports), a narrower feed boundary, exclusion of soil organic matter losses under constant land use, and land-use-change emissions of 0.65 Gt rather than 2.4 Gt.
  conf: not stated · class: not stated · holds: the comparison between the 2006 and 2013 livestock assessments · src: gerberTacklingClimateChange2013 · trail: CB3-AG-EMISSIONS §4. Boundary C · from: CB3-AG-EMISSIONS:B-0049, CB3-AG-EMISSIONS:B-0050
- **livestock.4** FAO's 2023 assessment lowered the livestock figure again, to about 6.2 Gt CO2eq for 2015, ~12% of anthropogenic emissions.
  conf: not stated · class: not stated · holds: livestock agrifood systems, 2015; GLEAM; uncertainty not retrieved; retrieved via FAO's own press summary and repository listing, the report's full text not read · src: faoPathwaysTowardsLower2023 (secondary) · trail: CB3-AG-EMISSIONS §4. Boundary C, §8. Table, §10. References · from: CB3-AG-EMISSIONS:B-0051, CB3-AG-EMISSIONS:B-0124, CB3-AG-EMISSIONS:R-0080 · limit: access (note: "I did not read the report's full text, so its 6.2 Gt / ~12% figure is reported as secondary")
- **livestock.5** The 18% livestock figure is superseded and should not be treated as current: Livestock's Long Shadow 18%, then Gerber et al. 14.5%, then FAO 2023 ~12%.
  conf: not stated · class: not stated · holds: livestock's share of total GHG · src: anonLivestockSLong2006, gerberTacklingClimateChange2013, faoPathwaysTowardsLower2023 · trail: CB3-AG-EMISSIONS §4. Boundary C, §7. Bounding · from: CB3-AG-EMISSIONS:B-0052, CB3-AG-EMISSIONS:B-0098

### anthropogenic-n2o: anthropogenic nitrous oxide
needs: afolu, ghg-metric, global-denominator
- **anthropogenic-n2o.1** Total net anthropogenic N2O is 9.4 ± 5.6 MtN2O yr−1, or 2.6 ± 1.5 GtCO2-eq yr−1, of which AFOLU is 69%.
  conf: not stated · class: not stated · holds: all sectors; AR6 Table 7.1 · src: nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §5. Boundary D · from: CB3-AG-EMISSIONS:B-0063
- **anthropogenic-n2o.2** By the reviewer's arithmetic from AR6 Table 7.1, all anthropogenic N2O, every sector, is 2.6 / 55.9 = ~4.7% of all anthropogenic GHG in 2010–2019; it includes fossil fuel, industry, waste and biomass burning N2O, not just agriculture.
  conf: not stated · class: deriv (note: "My arithmetic") · holds: total anthropogenic N2O, all sectors; 2010–2019; AR6 GWP100; ±1.5 Gt, 60% uncertainty on N2O · src: nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §5. Boundary D, §9. Verdict, §8. Table · from: CB3-AG-EMISSIONS:B-0063, CB3-AG-EMISSIONS:B-0064, CB3-AG-EMISSIONS:B-0125, CB3-AG-EMISSIONS:A-010, CB3-AG-EMISSIONS:A-011
- **anthropogenic-n2o.3** By the reviewer's arithmetic, AFOLU N2O alone is 1.8 / 55.9 = 3.2% of all anthropogenic GHG.
  conf: not stated · class: deriv (note: "My arithmetic") · holds: AFOLU N2O; 2010–2019; AR6 GWP100; ±1.1 Gt as stated · src: nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §5. Boundary D, §8. Table · from: CB3-AG-EMISSIONS:B-0064, CB3-AG-EMISSIONS:B-0065, CB3-AG-EMISSIONS:B-0128
- **anthropogenic-n2o.4** Anthropogenic N2O rose from 4.8 (3.1–7.3) to 6.7 (3.3–10.9) Tg N yr−1 between 1980 and 2020.
  conf: not stated · class: not stated · holds: the global N2O budget in mass terms, 1980–2020; Tian et al. 2024 · src: tianGlobalNitrousOxide2024 · trail: CB3-AG-EMISSIONS §5. Boundary D · from: CB3-AG-EMISSIONS:B-0066
- **anthropogenic-n2o.5** Direct agricultural N2O emissions reached 3.9 (2.9–5.1) Tg N yr−1 in 2020, of which direct soil emissions from synthetic fertilisers and manure application were 2.1 (1.7–2.6) Tg N yr−1 and manure left on pasture 1.4 (0.9–1.9) Tg N yr−1; indirect agricultural emissions were 1.3 (0.9–1.6) Tg N yr−1.
  conf: not stated · class: not stated · holds: the global N2O budget in mass terms, 2020; Tian et al. 2024 · src: tianGlobalNitrousOxide2024 · trail: CB3-AG-EMISSIONS §5. Boundary D · from: CB3-AG-EMISSIONS:B-0066
- **anthropogenic-n2o.6** Agricultural emissions contributed 74% of total anthropogenic N2O emissions in the 2010s, 56% from direct agricultural emissions and 18% from indirect emissions.
  conf: not stated · class: not stated · holds: the global N2O budget, 2010s; Tian et al. 2024 · src: tianGlobalNitrousOxide2024 · trail: CB3-AG-EMISSIONS §5. Boundary D · from: CB3-AG-EMISSIONS:B-0066, CB3-AG-EMISSIONS:B-0067
- **anthropogenic-n2o.7** The 2020 predecessor budget gave agriculture 3.8 (2.5–5.8) Tg N yr−1 for 2007–2016, out of 7.3 (4.2–11.4) Tg N anthropogenic.
  conf: not stated · class: not stated · holds: the global N2O budget in mass terms, 2007–2016; Tian et al. 2020 · src: tianComprehensiveQuantificationGlobal2020 · trail: CB3-AG-EMISSIONS §5. Boundary D · from: CB3-AG-EMISSIONS:B-0066, CB3-AG-EMISSIONS:B-0068
- **anthropogenic-n2o.8** By the reviewer's arithmetic, flagged as its own, agricultural N2O of 4.8 Tg N yr−1 (direct 3.6 plus indirect 1.2, 2010s) converts to 7.54 Tg N2O and, at AR6 GWP100 = 273, to ~2.06 Gt CO2eq, about 3.5% of 59 Gt.
  conf: not stated · class: deriv (note: "My arithmetic, flagged as mine") · holds: agricultural N2O, direct plus indirect, 2010s, derived from Tian et al. 2024; AR6 GWP100; against the 59 Gt total; budget ranges wide · src: tianGlobalNitrousOxide2024 · trail: CB3-AG-EMISSIONS §5. Boundary D, §8. Table · from: CB3-AG-EMISSIONS:B-0069, CB3-AG-EMISSIONS:B-0127

### soil-n2o: Boundary D, nitrous oxide from agricultural soils
needs: afolu, anthropogenic-n2o, global-denominator
- **soil-n2o.1** The soils and nitrous oxide boundary is where numbers are smallest and where cross-source disagreement is proportionally largest.
  conf: not stated · class: not stated · holds: soils, and nitrous oxide specifically · src: none (the reviewer's synthesis) · trail: CB3-AG-EMISSIONS §5. Boundary D · from: CB3-AG-EMISSIONS:B-0053
- **soil-n2o.2** By the reviewer's arithmetic, managed soils and pasture at 11% of 2019 AFOLU emissions (13 Gt) is ~1.4 Gt CO2eq, which against 59 Gt in 2019 is ~2.4% of global emissions.
  conf: not stated · class: deriv (note: "My arithmetic") · holds: managed soils and pasture within AFOLU (CO2 and N2O), 2019; AR6 GWP100; EDGAR data via AR6 Figure 7.3, whose shares were read off the rendered figure, not the text · src: nabuursAgricultureForestryOther2022 (shares read off the rendered figure) · trail: CB3-AG-EMISSIONS §5. Boundary D, §8. Table · from: CB3-AG-EMISSIONS:B-0054, CB3-AG-EMISSIONS:B-0055, CB3-AG-EMISSIONS:B-0056, CB3-AG-EMISSIONS:B-0129 · limit: access (note: "I read these shares off the rendered figure, not the text")
- **soil-n2o.3** Cropland soils emitted around 3 MtN2O yr-1 (around 795 MtCO2 eq yr-1) during 2007–2016, with medium confidence.
  conf: not stated · class: not stated · holds: cropland soils, N2O, 2007–2016; IPCC SRCCL, section A.3.5, with IPCC's own assessed medium confidence · src: ipccSummaryPolicymakers2019 · trail: CB3-AG-EMISSIONS §5. Boundary D · from: CB3-AG-EMISSIONS:B-0057
- **soil-n2o.4** By the reviewer's arithmetic, cropland soils' 795 MtCO2 eq is ~1.5% of SRCCL's implied total of ~52 Gt.
  conf: not stated · class: deriv (note: "My arithmetic") · holds: cropland soils N2O, 2007–2016; AR5 GWP100; against SRCCL's implied total · src: ipccSummaryPolicymakers2019 · trail: CB3-AG-EMISSIONS §5. Boundary D, §8. Table · from: CB3-AG-EMISSIONS:B-0057, CB3-AG-EMISSIONS:B-0058, CB3-AG-EMISSIONS:B-0131
- **soil-n2o.5** Climate Watch/WRI, as presented by Our World in Data for 2016, gives agricultural soils 4.1%: nitrous oxide produced when synthetic nitrogen fertilizers are applied to soils, including emissions from agricultural soils for all agricultural products (food for direct human consumption, animal feed, biofuels and other non-food crops).
  conf: single (note: "Single source, secondary presentation, unverified against the underlying dataset") · class: not stated · holds: the agricultural soils inventory category (3.D-equivalent), 2016; GWP100; no uncertainty statement; verified only as presented by Our World in Data, not in the Climate Watch dataset itself · src: ritchieSectorSectorWhere2020, climate (secondary presentation; unverified against the underlying dataset) · trail: CB3-AG-EMISSIONS §5. Boundary D, §9. Verdict, §1. What this review, §8. Table · from: CB3-AG-EMISSIONS:B-0015, CB3-AG-EMISSIONS:B-0016, CB3-AG-EMISSIONS:B-0059, CB3-AG-EMISSIONS:B-0060, CB3-AG-EMISSIONS:B-0062, CB3-AG-EMISSIONS:B-0126, CB3-AG-EMISSIONS:A-006, CB3-AG-EMISSIONS:A-008, CB3-AG-EMISSIONS:A-017 · rating: "the weakest-supported number in this review" · limit: access and evidence (note: "one secondary presentation, no uncertainty statement, not verified against the primary dataset")
- **soil-n2o.6** Independent reconstructions of the same quantity come in lower than 4.1%: ~3.5% from the Global N2O Budget (by the reviewer's arithmetic), ~2.4% for managed soils and pasture from EDGAR via AR6, and ~1.5% for cropland soils from SRCCL.
  conf: not stated · class: not stated · holds: N2O from agricultural soils as a share of global emissions, against Climate Watch/WRI's 4.1% · src: tianGlobalNitrousOxide2024, nabuursAgricultureForestryOther2022, ipccSummaryPolicymakers2019 · trail: CB3-AG-EMISSIONS §9. Verdict · from: CB3-AG-EMISSIONS:A-006, CB3-AG-EMISSIONS:A-009
- **soil-n2o.7** Published estimates of N2O from agricultural soils as a share of global GHG emissions range from about 1.5% to 4.1%, depending on whether the category is cropland soils only, managed soils and pasture, or the full inventory "agricultural soils" line, and on the database and metric used; the 4.1% end rests on a single unverified source.
  conf: not stated · class: not stated · holds: the range spans SRCCL's cropland soils (~1.5%), EDGAR via AR6's managed soils and pasture (~2.4%), and Climate Watch/WRI's agricultural soils line via Our World in Data (4.1%) · src: ipccSummaryPolicymakers2019, nabuursAgricultureForestryOther2022, ritchieSectorSectorWhere2020, climate · trail: CB3-AG-EMISSIONS §9. Verdict, §Verdict · from: CB3-AG-EMISSIONS:A-004, CB3-AG-EMISSIONS:A-009, CB3-AG-EMISSIONS:A-016, CB3-AG-EMISSIONS:A-017

### synthetic-fertiliser: emissions from synthetic nitrogen fertiliser
needs: afolu, soil-n2o, global-denominator
- **synthetic-fertiliser.1** Field N2O from synthetic fertiliser application, from EDGAR via AR6, is ~3% of AFOLU, ~0.4 Gt CO2eq, in 2019.
  conf: not stated · class: not stated · holds: field N2O from synthetic fertiliser application, 2019, one of three numbers on three boundaries; the AFOLU shares read off the rendered AR6 Figure 7.3, not the text · src: nabuursAgricultureForestryOther2022 (shares read off the rendered figure) · trail: CB3-AG-EMISSIONS §5. Boundary D · from: CB3-AG-EMISSIONS:B-0055, CB3-AG-EMISSIONS:B-0070, CB3-AG-EMISSIONS:B-0071 · limit: access (note: "I read these shares off the rendered figure, not the text")
- **synthetic-fertiliser.2** By the reviewer's arithmetic, synthetic fertiliser application at 3% of 13 Gt is ~0.4 Gt, ~0.7% of global emissions.
  conf: not stated · class: deriv (note: "My arithmetic") · holds: synthetic fertiliser application (N2O), 2019; EDGAR via AR6 Figure 7.3, read off the rendered figure; AR6 GWP100; 60% uncertainty on N2O · src: nabuursAgricultureForestryOther2022 (shares read off the rendered figure) · trail: CB3-AG-EMISSIONS §5. Boundary D, §8. Table · from: CB3-AG-EMISSIONS:B-0054, CB3-AG-EMISSIONS:B-0055, CB3-AG-EMISSIONS:B-0056, CB3-AG-EMISSIONS:B-0133 · limit: access (note: "I read these shares off the rendered figure, not the text")
- **synthetic-fertiliser.3** FAOSTAT gives field N2O from synthetic fertiliser as 601 Mt CO2eq in 2019, up 42% since 1990.
  conf: not stated · class: not stated · holds: field N2O from synthetic fertiliser, FAOSTAT, 2019 · src: tubielloPrePostproductionProcesses2022 · trail: CB3-AG-EMISSIONS §5. Boundary D · from: CB3-AG-EMISSIONS:B-0072
- **synthetic-fertiliser.4** FAOSTAT counts fertiliser manufacturing separately, under pre- and post-production, at 408 Mt CO2eq.
  conf: not stated · class: not stated · holds: fertiliser manufacturing, FAOSTAT, counted under pre- and post-production · src: tubielloPrePostproductionProcesses2022 · trail: CB3-AG-EMISSIONS §5. Boundary D · from: CB3-AG-EMISSIONS:B-0072
- **synthetic-fertiliser.5** By the reviewer's arithmetic, FAOSTAT's 601 Mt against FAO's ~53 Gt total is ~1.1%.
  conf: not stated · class: deriv (note: "My arithmetic") · holds: field N2O from synthetic fertiliser, FAOSTAT, 2019; AR5 GWP100; 30% assigned uncertainty · src: tubielloPrePostproductionProcesses2022 · trail: CB3-AG-EMISSIONS §5. Boundary D, §8. Table · from: CB3-AG-EMISSIONS:B-0072, CB3-AG-EMISSIONS:B-0073, CB3-AG-EMISSIONS:B-0132
- **synthetic-fertiliser.6** The synthetic N fertiliser supply chain was responsible for estimated emissions of 1.13 GtCO2e in 2018, 10.6% of agricultural emissions and 2.1% of global GHG emissions.
  conf: not stated · class: not stated · holds: the whole synthetic N supply chain, 2018; CO2 and N2O; Menegat et al. 2022, read as abstract only · src: menegatGreenhouseGasEmissions2022 (abstract only) · trail: CB3-AG-EMISSIONS §5. Boundary D, §8. Table · from: CB3-AG-EMISSIONS:B-0074, CB3-AG-EMISSIONS:B-0076, CB3-AG-EMISSIONS:B-0130 · limit: access (note: "Abstract read only")
- **synthetic-fertiliser.7** Within the synthetic N fertiliser supply chain, production accounted for 38.8%, field emissions 58.6% and transportation 2.6%.
  conf: not stated · class: not stated · holds: the whole synthetic N supply chain, 2018; Menegat et al. 2022, read as abstract only · src: menegatGreenhouseGasEmissions2022 (abstract only) · trail: CB3-AG-EMISSIONS §5. Boundary D · from: CB3-AG-EMISSIONS:B-0074, CB3-AG-EMISSIONS:B-0075, CB3-AG-EMISSIONS:B-0076 · limit: access (note: "Abstract read only")
- **synthetic-fertiliser.8** An author correction to Menegat et al. 2022 exists, but it concerns figure axis labels and a supplementary table, not the headline.
  conf: not stated · class: not stated · holds: the author correction, read only as abstract or publisher metadata · src: menegatAuthorCorrectionGreenhouse2022 (abstract only) · trail: CB3-AG-EMISSIONS §5. Boundary D, §1. What this review · from: CB3-AG-EMISSIONS:B-0014, CB3-AG-EMISSIONS:B-0076 · limit: access (note: "Read only as abstract or publisher metadata, not full text")
- **synthetic-fertiliser.9** EDGAR's 0.4 Gt and FAOSTAT's 0.601 Gt for the same quantity, field N2O from synthetic fertiliser, differ by roughly 50%; neither source the review read states a reason, and AR6 notes only that FAOSTAT, EDGAR and USEPA global means "are within the uncertainty bounds of EDGAR", given assessed uncertainties of 30% (CH4) and 60% (N2O). The review reports this as unexplained divergence, not as agreement.
  conf: not stated · class: not stated · holds: field N2O from synthetic fertiliser, 2019; EDGAR via AR6 against FAOSTAT; AR6, Table 7.1 footnote c · src: nabuursAgricultureForestryOther2022, tubielloPrePostproductionProcesses2022 · trail: CB3-AG-EMISSIONS §5. Boundary D · from: CB3-AG-EMISSIONS:B-0071, CB3-AG-EMISSIONS:B-0072, CB3-AG-EMISSIONS:B-0077, CB3-AG-EMISSIONS:B-0078, CB3-AG-EMISSIONS:B-0079

### five-per-cent: which boundary produces a figure near five per cent
needs: food-system, afolu, farm-gate, anthropogenic-n2o, soil-n2o
- **five-per-cent.1** No boundary in the current authoritative literature produces exactly five per cent for agriculture, and none produces it for agricultural soils.
  conf: not stated · class: not stated · holds: the boundaries in the current authoritative literature · src: none (the review's verdict across its sources) · trail: CB3-AG-EMISSIONS §9. Verdict, §Verdict · from: CB3-AG-EMISSIONS:A-001, CB3-AG-EMISSIONS:A-005 · contrary: not stated
- **five-per-cent.2** Three boundaries land close enough that a "roughly 5%" claim could have originated from any of them, and they are not interchangeable: N2O from agricultural soils at 4.1% (Climate Watch/WRI 2016 via Our World in Data), all anthropogenic N2O across every sector at ~4.7%, and emissions outside the farm gate at 5–10%.
  conf: not stated · class: not stated · holds: the 4.1% is the review's own weakest-supported number, one unverified secondary presentation · src: ritchieSectorSectorWhere2020, climate (one unverified secondary presentation), nabuursAgricultureForestryOther2022, ipccSummaryPolicymakers2019 · trail: CB3-AG-EMISSIONS §9. Verdict, §Verdict · from: CB3-AG-EMISSIONS:A-002, CB3-AG-EMISSIONS:A-005
- **five-per-cent.3** The 4.1% agricultural soils figure is the closest match to a soils-specific claim, and the only widely circulated breakdown in which a soils category sits near 5%.
  conf: not stated · class: not stated · holds: nitrous oxide from agricultural soils (inventory category 3.D-equivalent), Climate Watch/WRI for 2016, as presented by Our World in Data · src: ritchieSectorSectorWhere2020, climate (as presented by Our World in Data) · trail: CB3-AG-EMISSIONS §9. Verdict · from: CB3-AG-EMISSIONS:A-006, CB3-AG-EMISSIONS:A-007
- **five-per-cent.4** If a "5%" claim is really about N2O rather than about soils, all anthropogenic N2O at ~4.7% of 2010–2019 global GHG is what it matches, but that figure includes fossil fuel, industry, waste and biomass burning N2O, not just agriculture.
  conf: not stated · class: deriv (note: "my arithmetic from Table 7.1") · holds: all anthropogenic nitrous oxide, every sector, 2010–2019 · src: nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §9. Verdict · from: CB3-AG-EMISSIONS:A-010, CB3-AG-EMISSIONS:A-011
- **five-per-cent.5** Emissions outside the farm gate (5–10%, SRCCL) and non-food agriculture plus other deforestation drivers (5%, Poore & Nemecek) are both exactly 5% at one end, and both are about something else entirely: supply chains and non-food crops.
  conf: not stated · class: not stated · holds: outside the farm gate; non-food agriculture plus other deforestation drivers · src: ipccSummaryPolicymakers2019, pooreReducingFoodS2018 · trail: CB3-AG-EMISSIONS §9. Verdict · from: CB3-AG-EMISSIONS:A-012, CB3-AG-EMISSIONS:A-013
- **five-per-cent.6** A figure near 5% is definitively not agricultural production (10.7–14.6%), not AFOLU (13–22%), not agriculture with land-use change for food (16–27%), and not the food system (21–42%); it is three to eight times smaller than any of those, and can only belong to a soils- or N2O-specific boundary.
  conf: not stated · class: not stated · holds: the review's ranges for agricultural production, AFOLU, agriculture with land-use change for food, and the food system · src: none (the review's verdict across its sources) · trail: CB3-AG-EMISSIONS §9. Verdict, §Verdict · from: CB3-AG-EMISSIONS:A-003, CB3-AG-EMISSIONS:A-014, CB3-AG-EMISSIONS:A-015 · contrary: not stated

## Do not say
- **dns.1** "Agriculture accounts for about 5% of global greenhouse-gas emissions."
  why: No boundary in the current authoritative literature produces five per cent for agriculture: agricultural production is 10.7–14.6%, AFOLU 13–22%, agriculture with land-use change for food 16–27%, and the food system 21–42%. · instead: five-per-cent.6, farm-gate.2, farm-gate.6, afolu.1 · trail: CB3-AG-EMISSIONS §9. Verdict · from: CB3-AG-EMISSIONS:A-005, CB3-AG-EMISSIONS:A-014
- **dns.2** "Agricultural soils account for about 5% of global greenhouse-gas emissions."
  why: No boundary produces five per cent for agricultural soils; published estimates of N2O from agricultural soils range from about 1.5% to 4.1% of global emissions, and the 4.1% end rests on a single unverified source. · instead: soil-n2o.7, soil-n2o.5 · trail: CB3-AG-EMISSIONS §9. Verdict · from: CB3-AG-EMISSIONS:A-005, CB3-AG-EMISSIONS:A-016, CB3-AG-EMISSIONS:A-017
- **dns.3** "Agricultural nitrous oxide makes up about 4.7% of global greenhouse-gas emissions."
  why: About 4.7% is all anthropogenic nitrous oxide, every sector, which includes fossil fuel, industry, waste and biomass burning N2O, not just agriculture. · instead: anthropogenic-n2o.2, anthropogenic-n2o.3, anthropogenic-n2o.8 · trail: CB3-AG-EMISSIONS §9. Verdict · from: CB3-AG-EMISSIONS:A-010, CB3-AG-EMISSIONS:A-011
- **dns.4** "About 5% of global emissions come from agriculture, as SRCCL's figure for emissions outside the farm gate and Poore and Nemecek's figure for non-food agriculture show."
  why: Both figures are exactly 5% at one end, but both are about something else entirely: supply chains and non-food crops. · instead: food-system.4, food-system.15, five-per-cent.5 · trail: CB3-AG-EMISSIONS §9. Verdict · from: CB3-AG-EMISSIONS:A-012, CB3-AG-EMISSIONS:A-013
- **dns.5** "IPCC AR6 gives two rival estimates of AFOLU's share of global emissions, 22% and 13–21%."
  why: Quoting 22% and 13–21% as though they were rival estimates is an error: the 22% is a single year (2019) and the 13–21% a decadal mean, the same assessment on different periods and CO2 conventions. · instead: afolu.3, afolu.4 · trail: CB3-AG-EMISSIONS §3. Boundary B · from: CB3-AG-EMISSIONS:B-0039, CB3-AG-EMISSIONS:B-0040
- **dns.6** "The 13–21% range for AFOLU's share reflects statistical uncertainty."
  why: The spread is not statistical noise: it is two different CO2 accounting methods, bookkeeping models giving 21% and FAOSTAT/NGHGI CO2 flux data giving 13%. · instead: afolu.2, co2-accounting.1 · trail: CB3-AG-EMISSIONS §3. Boundary B · from: CB3-AG-EMISSIONS:B-0035
- **dns.7** "AFOLU accounts for 23% of global greenhouse-gas emissions."
  why: The 23% is SRCCL's AFOLU figure for 2007–2016, which has been superseded: AR6 gives 13–21% for 2010–2019. · instead: afolu.1, afolu.5 · trail: CB3-AG-EMISSIONS §3. Boundary B · from: CB3-AG-EMISSIONS:B-0041, CB3-AG-EMISSIONS:B-0042
- **dns.8** "Livestock accounts for 18% of global greenhouse-gas emissions."
  why: The 18% figure, from Livestock's Long Shadow (2006), is superseded and should not be treated as current: Gerber et al. revised it to 14.5%, and FAO 2023 to about 12%. · instead: livestock.2, livestock.4, livestock.5 · trail: CB3-AG-EMISSIONS §4. Boundary C · from: CB3-AG-EMISSIONS:B-0049, CB3-AG-EMISSIONS:B-0052, CB3-AG-EMISSIONS:B-0098
- **dns.9** "EDGAR and FAOSTAT agree on field nitrous oxide from synthetic fertiliser."
  why: EDGAR's 0.4 Gt and FAOSTAT's 0.601 Gt for the same quantity differ by roughly 50%, and the review says to report this as unexplained divergence, not as agreement. · instead: synthetic-fertiliser.9 · trail: CB3-AG-EMISSIONS §5. Boundary D · from: CB3-AG-EMISSIONS:B-0077, CB3-AG-EMISSIONS:B-0079
- **dns.10** "No published criticism disputes the EDGAR-FOOD one-third figure, so the literature endorses it."
  why: The review searched for published criticism and found none, but says that is absence of published criticism, not endorsement; the qualifications on the figure come from its own authors and from boundary comparisons. · instead: food-system.6 · trail: CB3-AG-EMISSIONS §7. Bounding · from: CB3-AG-EMISSIONS:B-0101, CB3-AG-EMISSIONS:B-0102, CB3-AG-EMISSIONS:B-0103
- **dns.11** "Lynch et al. show that GWP100 reporting overstates agriculture's contribution to warming."
  why: The direction of their effect is not uniformly downward: they also state that the impact of increasing methane emissions at rates above ~1% per year will be understated by reporting using GWP100 CO2e. · instead: ghg-metric.4, ghg-metric.6 · trail: CB3-AG-EMISSIONS §7. Bounding · from: CB3-AG-EMISSIONS:B-0095, CB3-AG-EMISSIONS:B-0097
- **dns.12** "FAO reports that agrifood systems made up 32% of global emissions in 2023."
  why: FAO's web summary says 32% while FAO's own COP30 takeaways document for the same report says 30%; the two FAO communications about one release disagree, and the review could not obtain the brief's own text to adjudicate. · instead: food-system.13 · trail: CB3-AG-EMISSIONS §2. Boundary A · from: CB3-AG-EMISSIONS:B-0026, CB3-AG-EMISSIONS:B-0027

## Gaps
- **gap.1** No second reader checked this review: no adversarial pass, independent critic or second agent re-deriving the load-bearing figures, and no claim-level verification (the verification log checked only that the DOIs resolve). Its answers rest on agricultural soils at 4.1% (Climate Watch/WRI via Our World in Data), all anthropogenic N2O at ~4.7% (the reviewer's arithmetic from AR6 Table 7.1), emissions outside the farm gate at 5–10% (SRCCL), the reconstructions of ~3.5%, ~2.4% and ~1.5%, and the boundary ranges of 10.7–14.6%, 13–22%, 16–27% and 21–42%.
  blocks: five-per-cent, soil-n2o, anthropogenic-n2o, food-system, afolu, farm-gate · origin: no critic: the note's own warning that no adversarial pass was run, and its verification log · search: not stated · trail: CB3-AG-EMISSIONS §No adversarial pass, §Verification log · from: CB3-AG-EMISSIONS:B-0008, CB3-AG-EMISSIONS:B-0009, CB3-AG-EMISSIONS:B-0010, CB3-AG-EMISSIONS:B-0139, CB3-AG-EMISSIONS:B-0140, CB3-AG-EMISSIONS:A-002, CB3-AG-EMISSIONS:A-009, CB3-AG-EMISSIONS:A-014
- **gap.2** The Climate Watch/WRI agricultural soils figure of 4.1% checked against the Climate Watch dataset itself, with an uncertainty statement: the review could verify it only as presented by Our World in Data.
  blocks: soil-n2o.5, five-per-cent · origin: the review's caution that the figure's support is thin and single-source · search: not stated · src: climate, ritchieSectorSectorWhere2020 · trail: CB3-AG-EMISSIONS §1. What this review · from: CB3-AG-EMISSIONS:B-0015, CB3-AG-EMISSIONS:B-0016, CB3-AG-EMISSIONS:A-008
- **gap.3** FAO's 2025 agrifood brief's own text, to settle whether the 2023 agrifood share is 32% or 30%: two FAO communications about the release disagree, and the review could not obtain the brief.
  blocks: food-system.13 · origin: a source not obtained that matters · search: not stated · src: faoGreenhouseGasEmissions2025a, faoGreenhouseGasEmissions2025b · trail: CB3-AG-EMISSIONS §2. Boundary A · from: CB3-AG-EMISSIONS:B-0014, CB3-AG-EMISSIONS:B-0026, CB3-AG-EMISSIONS:B-0027
- **gap.4** The reason EDGAR (0.4 Gt) and FAOSTAT (0.601 Gt) differ by roughly 50% for field N2O from synthetic fertiliser.
  blocks: synthetic-fertiliser.9 · origin: the review's not-found result · search: searched, not found (note: "Neither source I read states a reason for this specific gap") · trail: CB3-AG-EMISSIONS §5. Boundary D · from: CB3-AG-EMISSIONS:B-0077, CB3-AG-EMISSIONS:B-0078
- **gap.5** The reason FAOSTAT's global total (53.5 Gt for 2022) differs from AR6's (59 Gt for 2019, 55.9 Gt for 2010–2019).
  blocks: global-denominator · origin: the review's not-found result · search: searched, not found (note: "Neither FAO brief I read explains the gap") · trail: CB3-AG-EMISSIONS §6. Where the major · from: CB3-AG-EMISSIONS:B-0083, CB3-AG-EMISSIONS:B-0085
- **gap.6** The note contradicts itself on FAOSTAT's uncertainty: the bounding section says the 19–43% range "comes from assigned, not estimated, uncertainties" ("first rough estimates"), while the table of candidate shares gives Tubiello et al. 2022's uncertainty as "95% CI 11–22 Gt; 19–43%", a confidence interval the text gives nowhere else.
  blocks: food-system.7, food-system.8 · origin: the note contradicts itself · search: not stated · src: tubielloPrePostproductionProcesses2022 · trail: CB3-AG-EMISSIONS §7. Bounding, §8. Table · from: CB3-AG-EMISSIONS:B-0022, CB3-AG-EMISSIONS:B-0104, CB3-AG-EMISSIONS:B-0109
- **gap.7** The verdict callout and the verdict section word the main finding differently: the callout says no boundary "produces five per cent for agriculture", the verdict section that none "produces exactly five per cent", and the same section says that emissions outside the farm gate and non-food agriculture plus other deforestation drivers "are exactly 5% at one end".
  blocks: five-per-cent.1 · origin: the note's verdict callout and its verdict section differ · search: not stated · trail: CB3-AG-EMISSIONS §Verdict, §9. Verdict · from: CB3-AG-EMISSIONS:A-001, CB3-AG-EMISSIONS:A-005, CB3-AG-EMISSIONS:A-013
- **gap.8** Full texts of sources read only as abstract, metadata or summary whose figures the review uses: Menegat et al. 2022 (abstract only: the 2.1% supply-chain figure), IPCC AR6 WGIII Chapter 12 (targeted extraction of the food-system statements: 23–42%), and FAO 2023 (press summary and repository listing: livestock at ~12%).
  blocks: synthetic-fertiliser.6, food-system.11, livestock.4 · origin: sources not obtained in full that matter; the note asks that numbers be treated as unconfirmed until spot-checked against the primary text · search: not stated · src: menegatGreenhouseGasEmissions2022, babikerCrosssectoralPerspectives2022, faoPathwaysTowardsLower2023 · trail: CB3-AG-EMISSIONS §1. What this review · from: CB3-AG-EMISSIONS:B-0010, CB3-AG-EMISSIONS:B-0014, CB3-AG-EMISSIONS:B-0076, CB3-AG-EMISSIONS:R-0080

## Out of scope

## Sources

```bibtex
@incollection{nabuursAgricultureForestryOther2022,
  author    = {Nabuurs, G-J. and Mrabet, R. and {Abu Hatab}, A. and Bustamante, M. and Clark, H. and Havl{\'i}k, P. and House, J. and Mbow, C. and Ninan, K.N. and Popp, A. and Roe, S. and Sohngen, B. and Towprayoon, S.},
  title     = {Agriculture, Forestry and Other Land Uses (AFOLU)},
  booktitle = {Climate Change 2022: Mitigation of Climate Change. Contribution of Working Group III to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change},
  editor    = {Shukla, P.R. and Skea, J. and Slade, R. and {Al Khourdajie}, A. and {van Diemen}, R. and McCollum, D. and Pathak, M. and Some, S. and Vyas, P. and Fradera, R. and Belkacemi, M. and Hasija, A. and Lisboa, G. and Luz, S. and Malley, J.},
  year      = {2022},
  pages     = {747--860},
  publisher = {Cambridge University Press},
  address   = {Cambridge, UK and New York, NY, USA},
  doi       = {10.1017/9781009157926.009},
  url       = {https://www.ipcc.ch/report/ar6/wg3/downloads/report/IPCC_AR6_WGIII_Chapter07.pdf},
  note      = {access: full_text (executive summary, §7.2.1, §7.2.3, Table 7.1, and Figure 7.3 read from a rendered page image); cited as: CB3-AG-EMISSIONS [1]; the verification log reports a Crossref 2023 registration year as an artefact, the cited year being correct}
}

@incollection{ipccSummaryPolicymakers2019,
  author    = {{IPCC}},
  title     = {Summary for Policymakers},
  booktitle = {Climate Change and Land: an IPCC Special Report on climate change, desertification, land degradation, sustainable land management, food security, and greenhouse gas fluxes in terrestrial ecosystems},
  editor    = {Shukla, P.R. and Skea, J. and {Calvo Buendia}, E. and Masson-Delmotte, V. and P{\"o}rtner, H.-O. and Roberts, D.C. and Zhai, P. and Slade, R. and Connors, S. and {van Diemen}, R. and Ferrat, M. and Haughey, E. and Luz, S. and Neogi, S. and Pathak, M. and Petzold, J. and {Portugal Pereira}, J. and Vyas, P. and Huntley, E. and Kissick, K. and Belkacemi, M. and Malley, J.},
  year      = {2019},
  pages     = {3--36},
  publisher = {IPCC},
  address   = {Geneva},
  url       = {https://www.ipcc.ch/site/assets/uploads/sites/4/2022/11/SRCCL_SPM.pdf},
  note      = {access: full_text (Summary for Policymakers, section A.3 and its footnotes); cited as: CB3-AG-EMISSIONS [2]; incomplete: doi}
}

@article{crippaFoodSystemsResponsible2021,
  author  = {Crippa, M. and Solazzo, E. and Guizzardi, D. and Monforti-Ferrario, F. and Tubiello, F.N. and Leip, A.},
  title   = {Food systems are responsible for a third of global anthropogenic GHG emissions},
  journal = {Nature Food},
  year    = {2021},
  volume  = {2},
  number  = {3},
  pages   = {198--209},
  doi     = {10.1038/s43016-021-00225-9},
  note    = {access: full_text (abstract, methods, metric statements); cited as: CB3-AG-EMISSIONS [3]}
}

@article{tubielloPrePostproductionProcesses2022,
  author  = {Tubiello, F.N. and Karl, K. and Flammini, A. and G{\"u}tschow, J. and Obli-Laryea, G. and Conchedda, G. and Pan, X. and Qi, S.Y. and {Halld{\'o}rud{\'o}ttir Hei{\dh}arsd{\'o}ttir}, H. and Wanner, N. and Quadrelli, R. and {Rocha Souza}, L. and Benoit, P. and Hayek, M. and Sandalow, D. and {Mencos Contreras}, E. and Rosenzweig, C. and {Rosero Moncayo}, J. and Conforti, P. and Torero, M.},
  title   = {Pre- and post-production processes increasingly dominate greenhouse gas emissions from agri-food systems},
  journal = {Earth System Science Data},
  year    = {2022},
  volume  = {14},
  number  = {4},
  pages   = {1795--1809},
  doi     = {10.5194/essd-14-1795-2022},
  note    = {access: full_text (abstract, Table 1, metric and uncertainty sections); cited as: CB3-AG-EMISSIONS [4]}
}

@article{tubielloGreenhouseGasEmissions2021,
  author  = {Tubiello, F.N. and Rosenzweig, C. and Conchedda, G. and Karl, K. and G{\"u}tschow, J. and Xueyao, P. and Obli-Laryea, G. and Wanner, N. and Qiu, S.Y. and {De Barros}, J. and Flammini, A. and Mencos-Contreras, E. and Souza, L. and Quadrelli, R. and Hei{\dh}arsd{\'o}ttir, H.H. and Benoit, P. and Hayek, M. and Sandalow, D.},
  title   = {Greenhouse gas emissions from food systems: building the evidence base},
  journal = {Environmental Research Letters},
  year    = {2021},
  volume  = {16},
  number  = {6},
  pages   = {065007},
  doi     = {10.1088/1748-9326/ac018e},
  note    = {access: full_text (§2.4 limitations, §4 discussion); cited as: CB3-AG-EMISSIONS [5]}
}

@techreport{faoGreenhouseGasEmissions2024,
  author      = {{FAO}},
  title       = {Greenhouse gas emissions from agrifood systems. Global, regional and country trends, 2000--2022},
  institution = {FAO},
  address     = {Rome},
  type        = {FAOSTAT Analytical Brief},
  number      = {94},
  year        = {2024},
  issn        = {2709-0078},
  url         = {https://openknowledge.fao.org/server/api/core/bitstreams/111b7ee8-282b-42ff-ad95-cccecd90f8ea/content},
  note        = {access: full_text; cited as: CB3-AG-EMISSIONS [6]}
}

@article{tianComprehensiveQuantificationGlobal2020,
  author  = {Tian, H. and Xu, R. and Canadell, J.G. and Thompson, R.L. and Winiwarter, W. and Suntharalingam, P. and Davidson, E.A. and Ciais, P. and Jackson, R.B. and Janssens-Maenhout, G. and Prather, M.J. and Regnier, P. and Pan, N. and Pan, S. and Peters, G.P. and Shi, H. and Tubiello, F.N. and Zaehle, S. and Zhou, F. and Arneth, A. and Battaglia, G. and Berthet, S. and Bopp, L. and Bouwman, A.F. and Buitenhuis, E.T. and Chang, J. and Chipperfield, M.P. and Dangal, S.R.S. and Dlugokencky, E. and Elkins, J.W. and Eyre, B.D. and Fu, B. and Hall, B. and Ito, A. and Joos, F. and Krummel, P.B. and Landolfi, A. and Laruelle, G.G. and Lauerwald, R. and Li, W. and Lienert, S. and Maavara, T. and MacLeod, M. and Millet, D.B. and Olin, S. and Patra, P.K. and Prinn, R.G. and Raymond, P.A. and Ruiz, D.J. and {van der Werf}, G.R. and Vuichard, N. and Wang, J. and Weiss, R.F. and Wells, K.C. and Wilson, C. and Yang, J. and Yao, Y.},
  title   = {A comprehensive quantification of global nitrous oxide sources and sinks},
  journal = {Nature},
  year    = {2020},
  volume  = {586},
  number  = {7828},
  pages   = {248--256},
  doi     = {10.1038/s41586-020-2780-0},
  note    = {access: full_text (abstract, Table 1, methods); cited as: CB3-AG-EMISSIONS [7]}
}

@article{tianGlobalNitrousOxide2024,
  author  = {Tian, H. and Pan, N. and Thompson, R.L. and Canadell, J.G. and Suntharalingam, P. and Regnier, P. and Davidson, E.A. and Prather, M. and Ciais, P. and Muntean, M. and Pan, S. and Winiwarter, W. and Zaehle, S. and Zhou, F. and Jackson, R.B. and Bange, H.W. and Berthet, S. and Bian, Z. and Bianchi, D. and Bouwman, A.F. and Buitenhuis, E.T. and Dutton, G. and Hu, M. and Ito, A. and Jain, A.K. and Jeltsch-Th{\"o}mmes, A. and Joos, F. and Kou-Giesbrecht, S. and Krummel, P.B. and Lan, X. and Landolfi, A. and Lauerwald, R. and Li, Y. and Lu, C. and Maavara, T. and Manizza, M. and Millet, D.B. and M{\"u}hle, J. and Patra, P.K. and Peters, G.P. and Qin, X. and Raymond, P. and Resplandy, L. and Rosentreter, J.A. and Shi, H. and Sun, Q. and Tonina, D. and Tubiello, F.N. and {van der Werf}, G.R. and Vuichard, N. and Wang, J. and Wells, K.C. and Western, L.M. and Wilson, C. and Yang, J. and Yao, Y. and You, Y. and Zhu, Q.},
  title   = {Global nitrous oxide budget (1980--2020)},
  journal = {Earth System Science Data},
  year    = {2024},
  volume  = {16},
  number  = {6},
  pages   = {2543--2604},
  doi     = {10.5194/essd-16-2543-2024},
  note    = {access: full_text (abstract, executive summary, Table 3, regional attribution); cited as: CB3-AG-EMISSIONS [8]}
}

@techreport{faoGreenhouseGasEmissions2025a,
  author      = {{FAO}},
  title       = {Greenhouse gas emissions from agrifood systems. Global, regional and country trends, 2001--2023},
  institution = {FAO},
  address     = {Rome},
  type        = {FAOSTAT Analytical Brief},
  number      = {115},
  year        = {2025},
  doi         = {10.4060/cd7300en},
  url         = {https://www.fao.org/statistics/highlights-archive/highlights-detail/greenhouse-gas-emissions-from-agrifood-systems.-global--regional-and-country-trends--2001-2023/en},
  note        = {access: abstract_only (the FAO web summary was retrieved, not the brief's own text); cited as: CB3-AG-EMISSIONS [9]}
}

@techreport{faoGreenhouseGasEmissions2025b,
  author      = {{FAO}},
  title       = {Greenhouse gas emissions from agrifood systems 2001--2023: Takeaways},
  institution = {FAO},
  address     = {Rome},
  year        = {2025},
  url         = {https://porelclima.org/images/2025/Belem_documentos/COP30_emisiones_agroalimentarias_FAO.pdf},
  note        = {access: abstract_only (listed with [9] among the sources read only as abstract or publisher metadata; the note says it retrieved this COP30 takeaways PDF); cited as: CB3-AG-EMISSIONS [9a]}
}

@article{pooreReducingFoodS2018,
  author  = {Poore, J. and Nemecek, T.},
  title   = {Reducing food's environmental impacts through producers and consumers},
  journal = {Science},
  year    = {2018},
  volume  = {360},
  number  = {6392},
  pages   = {987--992},
  doi     = {10.1126/science.aaq0216},
  note    = {access: full_text (accepted manuscript, headline results); cited as: CB3-AG-EMISSIONS [10]}
}

@misc{ritchieSectorSectorWhere2020,
  author = {Ritchie, H.},
  title  = {Sector by sector: where do global greenhouse gas emissions come from?},
  howpublished = {Our World in Data},
  year   = {2020},
  url    = {https://ourworldindata.org/ghg-emissions-by-sector},
  note   = {access: full_text (full text); cited as: CB3-AG-EMISSIONS [11]; sector breakdown for 2016 sourced to Climate Watch and the World Resources Institute}
}

@misc{climate,
  author = {{Climate Watch} and {World Resources Institute}},
  note   = {access: secondary (verified only as presented by Our World in Data [11], not in the Climate Watch dataset itself); named in the annotation of CB3-AG-EMISSIONS [11] as the source of its 2016 sector breakdown; not in the reference list; incomplete: title, year, url}
}

@book{gerberTacklingClimateChange2013,
  author    = {Gerber, P.J. and Steinfeld, H. and Henderson, B. and Mottet, A. and Opio, C. and Dijkman, J. and Falcucci, A. and Tempio, G.},
  title     = {Tackling climate change through livestock -- A global assessment of emissions and mitigation opportunities},
  publisher = {Food and Agriculture Organization of the United Nations},
  address   = {Rome},
  year      = {2013},
  isbn      = {978-92-5-107920-1},
  url       = {https://www.fao.org/3/i3437e/i3437e.pdf},
  note      = {access: full_text (headline sections and the Annex comparing it with Livestock's Long Shadow); cited as: CB3-AG-EMISSIONS [12]}
}

@misc{anonLivestockSLong2006,
  title = {Livestock's Long Shadow},
  year  = {2006},
  note  = {access: secondary (known through the Annex of Gerber et al. 2013, which compares the two); named in the body of CB3-AG-EMISSIONS, not in its reference list; incomplete: author, publisher, url}
}

@article{menegatGreenhouseGasEmissions2022,
  author  = {Menegat, S. and Ledo, A. and Tirado, R.},
  title   = {Greenhouse gas emissions from global production and use of nitrogen synthetic fertilisers in agriculture},
  journal = {Scientific Reports},
  year    = {2022},
  volume  = {12},
  pages   = {14490},
  doi     = {10.1038/s41598-022-18773-w},
  note    = {access: abstract_only (abstract or publisher metadata, not full text); cited as: CB3-AG-EMISSIONS [13]}
}

@article{menegatAuthorCorrectionGreenhouse2022,
  author  = {Menegat, S. and Ledo, A. and Tirado, R.},
  title   = {Author Correction: Greenhouse gas emissions from global production and use of nitrogen synthetic fertilisers in agriculture},
  journal = {Scientific Reports},
  year    = {2022},
  volume  = {12},
  pages   = {19777},
  doi     = {10.1038/s41598-022-24242-1},
  note    = {access: abstract_only (abstract or publisher metadata, not full text); cited as: CB3-AG-EMISSIONS [13a]}
}

@article{lynchAgricultureSContribution2021,
  author  = {Lynch, J. and Cain, M. and Frame, D. and Pierrehumbert, R.},
  title   = {Agriculture's contribution to climate change and role in mitigation is distinct from predominantly fossil CO2-emitting sectors},
  journal = {Frontiers in Sustainable Food Systems},
  year    = {2021},
  volume  = {4},
  pages   = {518039},
  doi     = {10.3389/fsufs.2020.518039},
  note    = {access: full_text (full HTML text, targeted); cited as: CB3-AG-EMISSIONS [14]}
}

@incollection{babikerCrosssectoralPerspectives2022,
  author    = {Babiker, M. and Berndes, G. and Blok, K. and Cohen, B. and Cowie, A. and Geden, O. and Ginzburg, V. and Leip, A. and Smith, P. and Sugiyama, M. and Yamba, F.},
  title     = {Cross-sectoral perspectives},
  booktitle = {Climate Change 2022: Mitigation of Climate Change. Contribution of Working Group III to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change},
  editor    = {Shukla, P.R. and others},
  year      = {2022},
  pages     = {1245--1354},
  publisher = {Cambridge University Press},
  address   = {Cambridge, UK and New York, NY, USA},
  doi       = {10.1017/9781009157926.014},
  url       = {https://www.ipcc.ch/report/ar6/wg3/downloads/report/IPCC_AR6_WGIII_Chapter12.pdf},
  note      = {access: abstract_only (targeted text extraction of the food-system statements only); cited as: CB3-AG-EMISSIONS [15]; DOI as corrected by the note's verification log (the review carried 10.1017/9781009157926.005, which resolves to AR6 WGIII Chapter 3)}
}

@incollection{ipccSummaryPolicymakers2022,
  author    = {{IPCC}},
  title     = {Summary for Policymakers},
  booktitle = {Climate Change 2022: Mitigation of Climate Change. Contribution of Working Group III to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change},
  editor    = {Shukla, P.R. and Skea, J. and Slade, R. and {Al Khourdajie}, A. and {van Diemen}, R. and McCollum, D. and Pathak, M. and Some, S. and Vyas, P. and Fradera, R. and Belkacemi, M. and Hasija, A. and Lisboa, G. and Luz, S. and Malley, J.},
  year      = {2022},
  pages     = {3--48},
  publisher = {Cambridge University Press},
  address   = {Cambridge, UK and New York, NY, USA},
  doi       = {10.1017/9781009157926.001},
  url       = {https://www.ipcc.ch/report/ar6/wg3/downloads/report/IPCC_AR6_WGIII_SPM.pdf},
  note      = {access: not stated; cited as: CB3-AG-EMISSIONS [16]}
}

@techreport{faoPathwaysTowardsLower2023,
  author      = {{FAO}},
  title       = {Pathways towards lower emissions -- A global assessment of the greenhouse gas emissions and mitigation options from livestock agrifood systems},
  institution = {FAO},
  address     = {Rome},
  year        = {2023},
  doi         = {10.4060/cc9029en},
  url         = {https://openknowledge.fao.org/server/api/core/bitstreams/a06a30d3-6e9d-4e9c-b4b7-29a6cc307208/content},
  note        = {access: secondary (retrieved via FAO's own press summary and repository listing; the report's full text not read); cited as: CB3-AG-EMISSIONS [17]}
}
```
