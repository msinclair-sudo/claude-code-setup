---
type: knowledge
title: Agriculture's share of global greenhouse gas emissions
inputs:
  - "CB3-AG-EMISSIONS: PhD/Proposal/Research/Results/Agriculture's Share of Global Greenhouse Gas Emissions by Accounting Boundary.md"
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-22
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

### accounting-boundary: Accounting boundaries for agriculture's emissions share
needs: none
- **accounting-boundary.1** The question "what share of global emissions is agriculture?" has no single answer because four different accounting boundaries are in routine use, each defensible, each producing a number between roughly 2% and 42%.
  conf: not stated · class: not stated · holds: published headline figures, each fixed by the review to its boundary, year, gases, metric and denominator · src: none (the reviewer's synthesis) · trail: CB3-AG-EMISSIONS §What this review does · from: CB3-AG-EMISSIONS:B-0011, CB3-AG-EMISSIONS:B-0012
- **accounting-boundary.2** Gas coverage differs between sources: SRCCL's 23% AFOLU figure covers only CO2, CH4 and N2O, while EDGAR-FOOD and FAOSTAT include F-gases.
  conf: not stated · class: not stated · holds: SRCCL footnote 21; EDGAR-FOOD (Crippa et al. 2021) and FAOSTAT (Tubiello et al. 2022) · src: ipccSummaryPolicymakers2019, crippaFoodSystemsResponsible2021, tubielloPrePostproductionProcesses2022 · trail: CB3-AG-EMISSIONS §Where the major sources differ · from: CB3-AG-EMISSIONS:B-0088

### gwp-metric: GWP100 and CO2-equivalent aggregation
needs: none
- **gwp-metric.bg1** The Global Warming Potential (GWP) of a gas is the time-integrated radiative forcing due to a pulse emission of it, relative to a pulse emission of an equal mass of CO2; an emission multiplied by this metric is its CO2-equivalent emission, and GWP100 is the metric integrated over a 100-year time horizon.
  kind: background · ref: myhreAnthropogenicNaturalRadiative2013 · check: DOI 10.1017/CBO9781107415324.018 resolves on Crossref (Anthropogenic and Natural Radiative Forcing, Climate Change 2013, pp. 659-740); definition stated in §8.7.1.2, CO2-equivalent emissions in §8.7.1.1 and §8.7.1.2 (integration over 20, 100 or 500 years)
- **gwp-metric.1** EDGAR-FOOD and FAOSTAT aggregate with AR5 GWP100 (CH4 = 28, N2O = 265); AR6 uses AR6 GWP100 with climate–carbon feedbacks (CH4 = 27, N2O = 273).
  conf: not stated · class: not stated · holds: EDGAR-FOOD (Crippa et al. 2021), FAOSTAT (Tubiello et al. 2022), IPCC AR6 WGIII Ch. 7 Table 7.1 footnote g · src: crippaFoodSystemsResponsible2021, tubielloPrePostproductionProcesses2022, nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §Where the major sources differ, §Boundary B · from: CB3-AG-EMISSIONS:B-0086, CB3-AG-EMISSIONS:B-0021, CB3-AG-EMISSIONS:B-0037
- **gwp-metric.2** AR6 warns that "The choice of metric depends on the purpose of the analysis and all GHG emission metrics have limitations and uncertainties".
  conf: not stated · class: not stated · holds: IPCC AR6 WGIII Summary for Policymakers · src: ipccSummaryPolicymakers2022 · trail: CB3-AG-EMISSIONS §Where the major sources differ · from: CB3-AG-EMISSIONS:B-0087
- **gwp-metric.3** Lynch et al. argue that GWP100 CO2-equivalent reporting misrepresents agriculture's warming contribution, because agriculture is dominated by CH4 and N2O rather than CO2: "conventional reporting of aggregated CO2-equivalent emission rates is highly ambiguous and does not straightforwardly reflect historical or anticipated contributions to global temperature change".
  conf: not stated · class: not stated · holds: an argument about the aggregation metric, not a measured share · src: lynchAgricultureSContribution2021 (full HTML text, targeted) · trail: CB3-AG-EMISSIONS §Bounding and negative facts · from: CB3-AG-EMISSIONS:B-0095
- **gwp-metric.4** Lynch et al. do not offer a replacement share; the criticism attacks the aggregation, not the inventory.
  conf: not stated · class: not stated · holds: Lynch et al. 2021 as the review read it · src: lynchAgricultureSContribution2021 · trail: CB3-AG-EMISSIONS §Bounding and negative facts · from: CB3-AG-EMISSIONS:B-0096
- **gwp-metric.5** The direction of the effect Lynch et al. describe is not uniformly downward: they state that "the impact of increasing methane emissions at rates above ~1% per year will be understated by reporting using GWP100 CO2e".
  conf: not stated · class: not stated · holds: methane emissions increasing at rates above ~1% per year · src: lynchAgricultureSContribution2021 · trail: CB3-AG-EMISSIONS §Bounding and negative facts · from: CB3-AG-EMISSIONS:B-0097

### denominator: Global total emissions used as the denominator
needs: none
- **denominator.1** FAOSTAT uses a global total of 53.5 Gt CO2eq for 2022; AR6 uses 59 ± 6.6 Gt for 2019 and 55.9 ± 6.1 Gt for the 2010–2019 mean.
  conf: not stated · class: not stated · holds: FAOSTAT Analytical Brief 94 (2022); IPCC AR6 WGIII SPM (2019); AR6 WGIII Ch. 7 (2010–2019 mean) · src: faoGreenhouseGasEmissions2024, ipccSummaryPolicymakers2022, nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §Where the major sources differ · from: CB3-AG-EMISSIONS:B-0083
- **denominator.2** The same numerator over these denominators shifts a share by several points.
  conf: not stated · class: not stated · holds: the denominators 53.5, 55.9 and 59 Gt · src: none (the reviewer's synthesis) · trail: CB3-AG-EMISSIONS §Where the major sources differ · from: CB3-AG-EMISSIONS:B-0084
- **denominator.3** Neither FAO brief the review read explains the gap between FAO's and AR6's global totals.
  conf: not stated · class: search (note: "Neither FAO brief I read explains the gap") · holds: the FAO briefs read (Analytical Brief 94; the 2025 release as web summary and COP30 takeaways) · src: faoGreenhouseGasEmissions2024, faoGreenhouseGasEmissions2025a, faoGreenhouseGasEmissions2025b · trail: CB3-AG-EMISSIONS §Where the major sources differ · from: CB3-AG-EMISSIONS:B-0085

### co2-accounting: CO2 accounting method for land use
needs: none
- **co2-accounting.bg1** A bookkeeping model estimates the net carbon flux from land use and land-cover change by applying prescribed changes in the carbon density of vegetation and soils to documented changes in the areas of land uses.
  kind: background · ref: houghtonGlobalRegionalFluxes2017 · check: DOI 10.1002/2016GB005546 resolves on Crossref (Global Biogeochemical Cycles 31(3), 456-472); stated in the abstract ("We used a bookkeeping model that prescribed changes in carbon density of vegetation and soils for 20 types of ecosystems and five land uses", with areas of croplands, pastures and forests from FAO data)
- **co2-accounting.1** The CO2 accounting method (bookkeeping models versus national inventories/FAOSTAT) moves AFOLU between 13% and 21% of global emissions; AR6 states this directly.
  conf: not stated · class: not stated · holds: AFOLU, 2010–2019, IPCC AR6 WGIII Ch. 7 · src: nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §Where the major sources differ · from: CB3-AG-EMISSIONS:B-0080, CB3-AG-EMISSIONS:B-0081
- **co2-accounting.2** The AR6 Figure 7.3 caption warns that AFOLU CO2 from bookkeeping models "is not directly comparable to LULUCF in NGHGIs".
  conf: not stated · class: not stated · holds: AFOLU CO2 versus NGHGI LULUCF, AR6 WGIII Ch. 7 Figure 7.3 caption · src: nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §Where the major sources differ, §Bounding and negative facts · from: CB3-AG-EMISSIONS:B-0082, CB3-AG-EMISSIONS:B-0094

### food-system: Boundary A, the whole food system or agrifood system
needs: accounting-boundary, gwp-metric, denominator
- **food-system.1** The food-system boundary is the broadest: farm-gate production, plus land-use change attributed to agriculture, plus everything up- and downstream (fertiliser manufacture, processing, packaging, transport, retail, household cooking, food waste disposal).
  conf: not stated · class: not stated · holds: the review's definition of Boundary A · src: none (the reviewer's definition) · trail: CB3-AG-EMISSIONS §Boundary A · from: CB3-AG-EMISSIONS:B-0017
- **food-system.2** IPCC SRCCL (2019) gave 21–37% of total net anthropogenic GHG emissions for the food system, 2007–2016, medium confidence.
  conf: not stated · class: not stated · holds: 2007–2016; CO2, CH4 and N2O · src: ipccSummaryPolicymakers2019 (section A.3 and its footnotes) · trail: CB3-AG-EMISSIONS §Boundary A, §Table of candidate shares · from: CB3-AG-EMISSIONS:B-0018, CB3-AG-EMISSIONS:B-0107 · rating: "medium confidence"
- **food-system.3** SRCCL: "Emissions within farm gate and from agricultural land expansion contributing to the global food system represent 16–27% of total anthropogenic emissions (medium confidence)."
  conf: not stated · class: not stated · holds: 2007–2016; CO2, CH4 and N2O; SRCCL A.3.6 · src: ipccSummaryPolicymakers2019 · trail: CB3-AG-EMISSIONS §Boundary A · from: CB3-AG-EMISSIONS:B-0018, CB3-AG-EMISSIONS:B-0114 · rating: "medium confidence"
- **food-system.4** SRCCL: "Emissions outside the farm gate represent 5–10% of total anthropogenic emissions (medium confidence)."
  conf: not stated · class: not stated · holds: 2007–2016; CO2, CH4 and N2O; SRCCL A.3.6 · src: ipccSummaryPolicymakers2019 · trail: CB3-AG-EMISSIONS §Boundary A · from: CB3-AG-EMISSIONS:B-0019, CB3-AG-EMISSIONS:B-0115 · rating: "medium confidence"
- **food-system.5** Crippa et al. 2021 (EDGAR-FOOD): food systems emitted 18 Gt CO2e in 2015, 34% of total GHG, with a stated 95% confidence interval of 14–22 Gt CO2e; CO2, CH4, N2O and F-gases, aggregated with AR5 GWP100.
  conf: not stated · class: not stated · holds: 2015; EDGAR-FOOD database; four gases; AR5 GWP100 (CH4 = 28, N2O = 265) · src: crippaFoodSystemsResponsible2021 (abstract, methods, metric statements) · trail: CB3-AG-EMISSIONS §Boundary A · from: CB3-AG-EMISSIONS:B-0020, CB3-AG-EMISSIONS:B-0021, CB3-AG-EMISSIONS:B-0108
- **food-system.6** Tubiello et al. 2022 (FAOSTAT): agrifood systems emitted 16.5 Gt CO2eq in 2019, 31% (range 19–43%), from an assigned uncertainty of 30% on farm gate and pre/post-production and 50% on land-use change; the review's table gives its 95% CI as 11–22 Gt.
  conf: not stated · class: not stated · holds: 2019; FAOSTAT; four gases; AR5 GWP100 · src: tubielloPrePostproductionProcesses2022 (abstract, Table 1, metric and uncertainty sections) · trail: CB3-AG-EMISSIONS §Boundary A, §Table of candidate shares · from: CB3-AG-EMISSIONS:B-0022, CB3-AG-EMISSIONS:B-0109
- **food-system.7** Uncertainty in the food-system figures is large and mostly not statistical: EDGAR-FOOD's 95% CI is 14–22 Gt on an 18 Gt central estimate, and FAOSTAT's 19–43% range on a 31% central estimate comes from assigned, not estimated, uncertainties; Tubiello et al.: "The above uncertainties are meant only as first rough estimates".
  conf: not stated · class: not stated · holds: EDGAR-FOOD 2015; FAOSTAT 2019 · src: crippaFoodSystemsResponsible2021, tubielloPrePostproductionProcesses2022 · trail: CB3-AG-EMISSIONS §Bounding and negative facts · from: CB3-AG-EMISSIONS:B-0104
- **food-system.8** Tubiello et al. 2021 gave 33% for 2018 and reconciled it with Crippa: "Our estimate of 16 Gt CO2 eq yr−1 in 2018 is consistent with their findings, also considering their stated uncertainty range of 14–22 Gt CO2 eq yr−1".
  conf: not stated · class: not stated · holds: 2018; FAOSTAT team · src: tubielloGreenhouseGasEmissions2021 (§2.4 limitations, §4 discussion) · trail: CB3-AG-EMISSIONS §Boundary A · from: CB3-AG-EMISSIONS:B-0023
- **food-system.9** IPCC AR6 WGIII Chapter 12: "Some 23–42% of global GHG emissions are associated with food systems", with absolute emissions rising "from 14 to 17 GtCO2-eq yr-1 in the period 1990–2018".
  conf: not stated · class: not stated · holds: 1990–2018; AR6 GWP100; a range only · src: babikerCrosssectoralPerspectives2022 (targeted text extraction of the food-system statements only) · trail: CB3-AG-EMISSIONS §Boundary A, §What this review does · from: CB3-AG-EMISSIONS:B-0024, CB3-AG-EMISSIONS:B-0106, CB3-AG-EMISSIONS:B-0014, CB3-AG-EMISSIONS:B-0010 · limit: access (note: "note where the review itself says it read only an abstract")
- **food-system.10** FAOSTAT's own share is falling and has been revised: Analytical Brief 94 reports 16.2 Gt CO2eq for 2022 against a global total of 53.5 Gt, i.e. 29.7%, "below 30 percent for the first time on record", down from 38% in 2000.
  conf: not stated · class: not stated · holds: 2022; FAOSTAT; global total 53.5 Gt · src: faoGreenhouseGasEmissions2024 · trail: CB3-AG-EMISSIONS §Boundary A · from: CB3-AG-EMISSIONS:B-0025
- **food-system.11** FAO's 2025 release gives 16.5 Gt for 2023, and its share as 32% in the FAO web summary ("fell from 38 to 32 percent in 2023") but 30% in FAO's own COP30 takeaways for the same report ("decreased from 40 percent to 30 percent"); two FAO communications about one release disagree by two percentage points, against 29.7% for 2022 in Brief 94.
  conf: cont (note: "disagree") · class: not stated · holds: 2023; FAO 2025 agrifood release, as web summary and COP30 takeaways · src: faoGreenhouseGasEmissions2025a (FAO web summary; brief's own text not obtained), faoGreenhouseGasEmissions2025b, faoGreenhouseGasEmissions2024 · trail: CB3-AG-EMISSIONS §Boundary A, §Bounding and negative facts · from: CB3-AG-EMISSIONS:B-0026, CB3-AG-EMISSIONS:B-0027, CB3-AG-EMISSIONS:B-0100 · limit: access (note: "I could not obtain the brief's own text to adjudicate")
- **food-system.12** Poore & Nemecek 2018 sit lower because the boundary is narrower: "Today's food supply chain creates ~13.7 billion metric tons of carbon dioxide equivalents (CO2eq), 26% of anthropogenic GHG emissions"; their accounting stops at retail and excludes consumer cooking and waste.
  conf: not stated · class: not stated · holds: food supply chain to retail, food only; ~2010 baseline; CO2, CH4, N2O · src: pooreReducingFoodS2018 (accepted manuscript, headline results) · trail: CB3-AG-EMISSIONS §Boundary A · from: CB3-AG-EMISSIONS:B-0028, CB3-AG-EMISSIONS:B-0030, CB3-AG-EMISSIONS:B-0112
- **food-system.13** Poore & Nemecek 2018: "A further 2.8 billion metric tons of CO2eq (5%) are caused by nonfood agriculture and other drivers of deforestation".
  conf: not stated · class: not stated · holds: non-food agriculture and other deforestation drivers; ~2010 baseline · src: pooreReducingFoodS2018 · trail: CB3-AG-EMISSIONS §Boundary A · from: CB3-AG-EMISSIONS:B-0029, CB3-AG-EMISSIONS:B-0113
- **food-system.14** Poore & Nemecek stop at retail and count only food, while Crippa and FAOSTAT include consumption and waste; OWID identifies exactly three causes of the 26% versus 34% gap: consumer cooking and waste, disagreement over how much deforestation to attribute to agriculture, and whether non-food agricultural products are counted.
  conf: not stated · class: not stated · holds: Poore & Nemecek 2018 versus EDGAR-FOOD, as Our World in Data compares them · src: ritchieSectorSectorWhere2020, pooreReducingFoodS2018, crippaFoodSystemsResponsible2021 · trail: CB3-AG-EMISSIONS §Where the major sources differ · from: CB3-AG-EMISSIONS:B-0089, CB3-AG-EMISSIONS:B-0090
- **food-system.15** Tubiello et al. concede their own land-use-change component is probably too high: "recent studies have estimated that only 80% of deforestation may be linked to agriculture globally ... We are thus likely overestimating the food-related land use change component".
  conf: not stated · class: not stated · holds: the FAOSTAT food-system estimate's land-use-change component · src: tubielloGreenhouseGasEmissions2021 · trail: CB3-AG-EMISSIONS §Where the major sources differ · from: CB3-AG-EMISSIONS:B-0091, CB3-AG-EMISSIONS:B-0092
- **food-system.16** A search for published criticism or formal comment disputing the EDGAR-FOOD "one third" figure or its land-use attribution found none; the qualifications on that figure come from its own authors and from boundary comparisons (Tubiello, OWID), not from an adversarial literature.
  conf: not stated · class: search (note: "found none") · holds: the review's search by web search, direct page fetch, and where available the biblion corpus and Scholar Gateway semantic search · src: none (a search result) · trail: CB3-AG-EMISSIONS §Bounding and negative facts · from: CB3-AG-EMISSIONS:B-0101, CB3-AG-EMISSIONS:B-0102, CB3-AG-EMISSIONS:B-0007
- **food-system.17** SRCCL footnote 22: food-system "emissions data are not directly comparable to the national inventories prepared according to the 2006 IPCC Guidelines for National Greenhouse Gas Inventories".
  conf: not stated · class: not stated · holds: SRCCL food-system emissions versus national inventories · src: ipccSummaryPolicymakers2019 · trail: CB3-AG-EMISSIONS §Bounding and negative facts · from: CB3-AG-EMISSIONS:B-0093
- **food-system.18** The review names as authoritative for this boundary: for a range with an assessed confidence level, IPCC AR6 WGIII Ch. 12 (23–42%) and SRCCL (21–37%); for an annually updated inventory-consistent number, FAOSTAT; for an independent database, EDGAR-FOOD.
  conf: not stated · class: not stated · holds: the food-system boundary · src: babikerCrosssectoralPerspectives2022, ipccSummaryPolicymakers2019, tubielloPrePostproductionProcesses2022, faoGreenhouseGasEmissions2024, faoGreenhouseGasEmissions2025a, crippaFoodSystemsResponsible2021 · trail: CB3-AG-EMISSIONS §Boundary A · from: CB3-AG-EMISSIONS:B-0031..0033
- **food-system.19** FAO's 2025 release table entry: agrifood systems 16.5 Gt CO2eq in 2023, 32% (FAO web) or 30% (FAO COP30 document), with no uncertainty stated and the sources in conflict.
  conf: not stated · class: not stated · holds: 2023; FAO 2025 · src: faoGreenhouseGasEmissions2025a, faoGreenhouseGasEmissions2025b · trail: CB3-AG-EMISSIONS §Table of candidate shares · from: CB3-AG-EMISSIONS:B-0110, CB3-AG-EMISSIONS:B-0111

### afolu: Boundary B, agriculture, forestry and other land use (AFOLU)
needs: accounting-boundary, co2-accounting, gwp-metric, denominator
- **afolu.1** IPCC AR6 WGIII Chapter 7: "The AFOLU (managed land) sector, on average, accounted for 13–21% of global total anthropogenic greenhouse gas (GHG) emissions in the period 2010–2019 (medium confidence)".
  conf: not stated · class: not stated · holds: 2010–2019 mean; CO2, CH4, N2O; AR6 GWP100 with climate–carbon feedbacks · src: nabuursAgricultureForestryOther2022 (executive summary, §7.2.1, §7.2.3, Table 7.1) · trail: CB3-AG-EMISSIONS §Boundary B · from: CB3-AG-EMISSIONS:B-0034, CB3-AG-EMISSIONS:B-0036 · rating: "medium confidence"
- **afolu.2** The 13–21% spread is two different CO2 accounting methods, not statistical noise: 11.9 ± 4.4 GtCO2eq of a total 55.9 ± 6.1 GtCO2eq gives 21% using bookkeeping models for the CO2 component, and "When using FAOSTAT/NGHGIs CO2 flux data, then the contribution of AFOLU to total emissions amounts to 13% of global emissions".
  conf: not stated · class: not stated · holds: 2010–2019 mean; AR6 WGIII Ch. 7 §7.2.1 · src: nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §Boundary B · from: CB3-AG-EMISSIONS:B-0035, CB3-AG-EMISSIONS:B-0116, CB3-AG-EMISSIONS:B-0117
- **afolu.3** AR6's AFOLU figures cover CO2, CH4 and N2O and use AR6 GWP100 with climate–carbon feedbacks (CH4 = 27, N2O = 273).
  conf: not stated · class: not stated · holds: AR6 WGIII Ch. 7, Table 7.1 footnote g · src: nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §Boundary B · from: CB3-AG-EMISSIONS:B-0036, CB3-AG-EMISSIONS:B-0037
- **afolu.4** The AR6 WGIII Summary for Policymakers gives "In 2019, approximately ... 22% [13 GtCO2-eq] from agriculture, forestry and other land use (AFOLU)", against global net anthropogenic emissions of 59 ± 6.6 GtCO2-eq in 2019; it is a single year rather than a decadal mean, which is why it exceeds the chapter's 21%.
  conf: not stated · class: not stated · holds: 2019 only; total 59 ± 6.6 Gt · src: ipccSummaryPolicymakers2022 · trail: CB3-AG-EMISSIONS §Boundary B · from: CB3-AG-EMISSIONS:B-0038, CB3-AG-EMISSIONS:B-0039, CB3-AG-EMISSIONS:B-0118
- **afolu.5** AR6's "22%" and "13–21%" are the same assessment on different periods and CO2 conventions.
  conf: not stated · class: not stated · holds: AR6 WGIII SPM (2019) and Ch. 7 (2010–2019 mean) · src: ipccSummaryPolicymakers2022, nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §Boundary B · from: CB3-AG-EMISSIONS:B-0040
- **afolu.6** SRCCL reported AFOLU as "23% (12.0 ± 2.9 GtCO2eq yr-1) of total net anthropogenic emissions of GHGs (medium confidence)" for 2007–2016, covering only CO2, CH4 and N2O; AR6 supersedes it with 13–21% for 2010–2019.
  conf: not stated · class: not stated · holds: 2007–2016; CO2, CH4, N2O (SRCCL A.3 and footnote 21) · src: ipccSummaryPolicymakers2019, nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §Boundary B, §Bounding and negative facts · from: CB3-AG-EMISSIONS:B-0041, CB3-AG-EMISSIONS:B-0042, CB3-AG-EMISSIONS:B-0099, CB3-AG-EMISSIONS:B-0119 · rating: "medium confidence"
- **afolu.7** In the Climate Watch/WRI breakdown for 2016 as presented by Our World in Data, Agriculture, Forestry and Land Use totals 18.4%, with livestock and manure 5.8%, rice 1.3%, crop burning 3.5% and deforestation 2.2%.
  conf: not stated · class: not stated · holds: 2016; GWP100; no uncertainty given · src: ritchieSectorSectorWhere2020 (secondary presentation of Climate Watch/WRI) · trail: CB3-AG-EMISSIONS §Boundary D, §Table of candidate shares · from: CB3-AG-EMISSIONS:B-0061, CB3-AG-EMISSIONS:B-0120

### farm-gate: Boundary C, agricultural production alone (farm gate)
needs: accounting-boundary, gwp-metric, denominator
- **farm-gate.1** AR6 WGIII Ch. 7: "Average non-CO2 emission (aggregated using GWP100 IPCC AR6 values) from agriculture have risen from 5.2 ± 1.4 GtCO2-eq yr−1 for the period 1990 to 1999, to 6.0 ± 1.7 GtCO2-eq yr−1 for the period 2010 to 2019 (Crippa et al. 2021)".
  conf: not stated · class: not stated · holds: agricultural non-CO2 (CH4 + N2O); AR6 GWP100; §7.2.1 · src: nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §Boundary C · from: CB3-AG-EMISSIONS:B-0043
- **farm-gate.2** 6.0 / 55.9 = 10.7% of total net anthropogenic GHG, 2010–2019 (the review's arithmetic).
  conf: not stated · class: deriv (note: "My arithmetic") · holds: agricultural production, non-CO2 only; 2010–2019; AR6 total 55.9 Gt · src: nabuursAgricultureForestryOther2022 (the review's arithmetic on its figures) · trail: CB3-AG-EMISSIONS §Boundary C · from: CB3-AG-EMISSIONS:B-0044, CB3-AG-EMISSIONS:B-0121
- **farm-gate.3** The AR6 chapter's component figures are agricultural CH4 157.0 ± 47.1 MtCH4 yr−1 (4.2 ± 1.3 GtCO2-eq) and N2O 6.6 ± 4.0 MtN2O yr−1 (1.8 ± 1.1 GtCO2-eq), with assessed uncertainties of 30% and 60% respectively.
  conf: not stated · class: not stated · holds: AR6 WGIII Ch. 7 Table 7.1; 2010–2019 · src: nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §Boundary C · from: CB3-AG-EMISSIONS:B-0045
- **farm-gate.4** FAOSTAT's farm gate is a slightly wider boundary (it includes on-farm energy CO2): 7.8 Gt CO2eq in 2022, 48% of agrifood systems emissions, and 8.1 Gt in 2023.
  conf: not stated · class: not stated · holds: FAOSTAT; 2022 and 2023; four gases; AR5 GWP100 · src: faoGreenhouseGasEmissions2024, faoGreenhouseGasEmissions2025a · trail: CB3-AG-EMISSIONS §Boundary C · from: CB3-AG-EMISSIONS:B-0046
- **farm-gate.5** 7.8 / 53.5 = 14.6% of FAO's global total for 2022 (the review's arithmetic).
  conf: not stated · class: deriv (note: "My arithmetic") · holds: FAOSTAT farm gate including on-farm energy; 2022; FAO total 53.5 Gt · src: faoGreenhouseGasEmissions2024 (the review's arithmetic on its figures) · trail: CB3-AG-EMISSIONS §Boundary C · from: CB3-AG-EMISSIONS:B-0047, CB3-AG-EMISSIONS:B-0122
- **farm-gate.6** The difference between FAOSTAT's 14.6% and the IPCC's 10.7% is partly gases (FAO adds on-farm CO2), partly database, partly the denominator (53.5 versus 55.9–59 Gt).
  conf: not stated · class: not stated · holds: the two farm-gate figures above · src: none (the reviewer's synthesis) · trail: CB3-AG-EMISSIONS §Boundary C · from: CB3-AG-EMISSIONS:B-0048

### livestock: Livestock as a sub-boundary
needs: farm-gate, gwp-metric
- **livestock.1** Livestock's Long Shadow (2006) put livestock at 18% of total GHG; Gerber et al. 2013 revised this to "7.1 gigatonnes CO2-eq per annum, representing 14.5 percent of all human-induced emissions", and its Annex gives the reasons: a GIS-based model (GLEAM) instead of statistical tables, a different reference period, IPCC 2006 rather than 2001 guidelines, different GWP values (296/298 for N2O and 23/25 for CH4 across the two reports), a narrower feed boundary, exclusion of soil organic matter losses under constant land use, and land-use-change emissions of 0.65 Gt rather than 2.4 Gt.
  conf: not stated · class: not stated · holds: livestock supply chain; ~2005; CO2, CH4, N2O · src: gerberTacklingClimateChange2013 (headline sections and the Annex comparing it with Livestock's Long Shadow) · trail: CB3-AG-EMISSIONS §Boundary C · from: CB3-AG-EMISSIONS:B-0049, CB3-AG-EMISSIONS:B-0050, CB3-AG-EMISSIONS:B-0123
- **livestock.2** FAO's 2023 assessment lowered the livestock figure again, to about 6.2 Gt CO2eq for 2015, ~12% of anthropogenic emissions.
  conf: not stated · class: not stated · holds: livestock agrifood systems; 2015; GLEAM · src: faoPathwaysTowardsLower2023 (retrieved via FAO's own press summary and repository listing; reported as secondary) · trail: CB3-AG-EMISSIONS §Boundary C · from: CB3-AG-EMISSIONS:B-0051, CB3-AG-EMISSIONS:B-0124
- **livestock.3** The livestock figure has a documented revision history, 18% → 14.5% → ~12%, and the 18% figure is superseded.
  conf: not stated · class: not stated · holds: Livestock's Long Shadow (2006), Gerber et al. 2013, FAO 2023 · src: gerberTacklingClimateChange2013, faoPathwaysTowardsLower2023 · trail: CB3-AG-EMISSIONS §Boundary C, §Bounding and negative facts · from: CB3-AG-EMISSIONS:B-0049, CB3-AG-EMISSIONS:B-0052, CB3-AG-EMISSIONS:B-0098

### n2o: Nitrous oxide emissions
needs: gwp-metric, denominator
- **n2o.1** AR6 Table 7.1: total net anthropogenic N2O is 9.4 ± 5.6 MtN2O yr−1, or 2.6 ± 1.5 GtCO2-eq yr−1, of which AFOLU is 69%.
  conf: not stated · class: not stated · holds: 2010–2019; AR6 GWP100 · src: nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §Boundary D · from: CB3-AG-EMISSIONS:B-0063
- **n2o.2** All anthropogenic N2O, every sector, is 2.6 / 55.9 = ~4.7% of all anthropogenic GHG in 2010–2019 (the review's arithmetic from Table 7.1); it includes fossil fuel, industry, waste and biomass burning N2O, not just agriculture.
  conf: not stated · class: deriv (note: "My arithmetic") · holds: all sectors; 2010–2019; AR6 GWP100; ±1.5 Gt and 60% uncertainty on N2O · src: nabuursAgricultureForestryOther2022 (the review's arithmetic on its figures) · trail: CB3-AG-EMISSIONS §Boundary D, §Verdict: which boundary · from: CB3-AG-EMISSIONS:B-0064, CB3-AG-EMISSIONS:A-010, CB3-AG-EMISSIONS:A-011, CB3-AG-EMISSIONS:B-0125
- **n2o.3** AFOLU N2O alone is 1.8 / 55.9 = 3.2% of all anthropogenic GHG (the review's arithmetic).
  conf: not stated · class: deriv (note: "My arithmetic") · holds: 2010–2019; AR6 GWP100; ±1.1 Gt · src: nabuursAgricultureForestryOther2022 (the review's arithmetic on its figures) · trail: CB3-AG-EMISSIONS §Boundary D · from: CB3-AG-EMISSIONS:B-0064, CB3-AG-EMISSIONS:B-0065, CB3-AG-EMISSIONS:B-0128
- **n2o.4** Tian et al. 2024: anthropogenic N2O rose from 4.8 (3.1–7.3) to 6.7 (3.3–10.9) Tg N yr−1 between 1980 and 2020; direct agricultural emissions reached 3.9 (2.9–5.1) Tg N yr−1 in 2020, of which direct soil emissions from synthetic fertilisers and manure application were 2.1 (1.7–2.6) Tg N yr−1 and manure left on pasture 1.4 (0.9–1.9) Tg N yr−1; indirect agricultural emissions were 1.3 (0.9–1.6) Tg N yr−1.
  conf: not stated · class: not stated · holds: global N2O budget, 1980–2020, in mass terms · src: tianGlobalNitrousOxide2024 (abstract, executive summary, Table 3, regional attribution) · trail: CB3-AG-EMISSIONS §Boundary D · from: CB3-AG-EMISSIONS:B-0066
- **n2o.5** Tian et al. 2024: "Agricultural emissions contributed 74% of total anthropogenic emissions in the 2010s, with 56% from direct agricultural emissions and 18% from indirect emissions".
  conf: not stated · class: not stated · holds: anthropogenic N2O, 2010s · src: tianGlobalNitrousOxide2024 · trail: CB3-AG-EMISSIONS §Boundary D · from: CB3-AG-EMISSIONS:B-0067
- **n2o.6** Tian et al. 2020 gave agriculture 3.8 (2.5–5.8) Tg N yr−1 for 2007–2016 out of 7.3 (4.2–11.4) Tg N anthropogenic.
  conf: not stated · class: not stated · holds: 2007–2016 · src: tianComprehensiveQuantificationGlobal2020 (abstract, Table 1, methods) · trail: CB3-AG-EMISSIONS §Boundary D · from: CB3-AG-EMISSIONS:B-0068
- **n2o.7** Agricultural N2O of 4.8 Tg N yr−1 (direct 3.6 + indirect 1.2, 2010s) converts to 7.54 Tg N2O, and at AR6 GWP100 = 273 to ~2.06 Gt CO2eq, about 3.5% of 59 Gt (the review's arithmetic, flagged as its own).
  conf: not stated · class: deriv (note: "My arithmetic, flagged as mine") · holds: agricultural N2O, direct + indirect, 2010s, from the Global N2O Budget; AR6 GWP100; 59 Gt total; budget ranges wide · src: tianGlobalNitrousOxide2024 (the review's arithmetic on its figures) · trail: CB3-AG-EMISSIONS §Boundary D · from: CB3-AG-EMISSIONS:B-0069, CB3-AG-EMISSIONS:B-0127

### soils: Boundary D, agricultural soils
needs: n2o, afolu, accounting-boundary
- **soils.1** The soils and N2O boundary is where numbers are smallest and where cross-source disagreement is proportionally largest.
  conf: not stated · class: not stated · holds: the soils and N2O figures the review compares · src: none (the reviewer's synthesis) · trail: CB3-AG-EMISSIONS §Boundary D · from: CB3-AG-EMISSIONS:B-0053
- **soils.2** AR6 Figure 7.3 subdivides 2019 AFOLU emissions (13 Gt) by activity: LULUCF (CO2) 51%, enteric fermentation (CH4) 23%, managed soils and pasture (CO2, N2O) 11%, rice cultivation (CH4) 8%, manure management (N2O, CH4) 3%, synthetic fertilizer application (N2O) 3%, biomass burning (CH4, N2O) 1%; CH4 and N2O data from EDGAR.
  conf: not stated · class: not stated · holds: 2019 AFOLU; shares read off the rendered figure, not the text · src: nabuursAgricultureForestryOther2022 (Figure 7.3 read from a rendered page image) · trail: CB3-AG-EMISSIONS §Boundary D · from: CB3-AG-EMISSIONS:B-0054, CB3-AG-EMISSIONS:B-0055
- **soils.3** Managed soils and pasture, 11% of 13 Gt, is ~1.4 Gt CO2eq, which against 59 Gt in 2019 is ~2.4% of global emissions (the review's arithmetic).
  conf: not stated · class: deriv (note: "My arithmetic") · holds: 2019; CO2 + N2O; AR6 GWP100; figure read from image · src: nabuursAgricultureForestryOther2022 (the review's arithmetic on its figures) · trail: CB3-AG-EMISSIONS §Boundary D · from: CB3-AG-EMISSIONS:B-0056, CB3-AG-EMISSIONS:B-0129
- **soils.4** SRCCL: "Cropland soils emitted around 3 MtN2O yr-1 (around 795 MtCO2 eq yr-1) during the period 2007–2016 (medium confidence)".
  conf: not stated · class: not stated · holds: cropland soils; 2007–2016; SRCCL A.3.5 · src: ipccSummaryPolicymakers2019 · trail: CB3-AG-EMISSIONS §Boundary D · from: CB3-AG-EMISSIONS:B-0057 · rating: "medium confidence"
- **soils.5** Against SRCCL's implied total of ~52 Gt, cropland soils N2O is ~1.5% (the review's arithmetic).
  conf: not stated · class: deriv (note: "My arithmetic") · holds: cropland soils N2O; 2007–2016; AR5 GWP100 · src: ipccSummaryPolicymakers2019 (the review's arithmetic on its figures) · trail: CB3-AG-EMISSIONS §Boundary D · from: CB3-AG-EMISSIONS:B-0058, CB3-AG-EMISSIONS:B-0131
- **soils.6** Climate Watch/WRI, as presented by Our World in Data for 2016, gives "Agricultural soils (4.1%)": nitrous oxide produced when synthetic nitrogen fertilizers are applied to soils, including emissions from agricultural soils for all agricultural products (food for direct human consumption, animal feed, biofuels, and other non-food crops).
  conf: single (note: "single-source") · class: not stated · holds: inventory category (3.D-equivalent); 2016; GWP100; no uncertainty statement; one secondary presentation, not verified against the primary dataset · src: ritchieSectorSectorWhere2020 (secondary presentation, unverified against the underlying dataset) · trail: CB3-AG-EMISSIONS §Boundary D, §What this review does, §Verdict: which boundary · from: CB3-AG-EMISSIONS:B-0059, CB3-AG-EMISSIONS:B-0060, CB3-AG-EMISSIONS:B-0062, CB3-AG-EMISSIONS:B-0015, CB3-AG-EMISSIONS:B-0016, CB3-AG-EMISSIONS:A-006, CB3-AG-EMISSIONS:A-008, CB3-AG-EMISSIONS:A-017, CB3-AG-EMISSIONS:B-0126 · rating: "the weakest-supported number in this review" · limit: access (note: "which I could verify only as presented by Our World in Data")
- **soils.7** Independent reconstructions of the same quantity come in lower than 4.1%: ~3.5% from the Global N2O Budget (the review's arithmetic), ~2.4% for "managed soils and pasture" from EDGAR via AR6, ~1.5% for cropland soils from SRCCL.
  conf: not stated · class: not stated · holds: Tian et al. 2024, AR6 WGIII Ch. 7 Figure 7.3, SRCCL A.3.5 · src: tianGlobalNitrousOxide2024, nabuursAgricultureForestryOther2022, ipccSummaryPolicymakers2019 · trail: CB3-AG-EMISSIONS §Verdict: which boundary · from: CB3-AG-EMISSIONS:A-009
- **soils.8** Published estimates of N2O from agricultural soils as a share of global GHG emissions range from about 1.5% to 4.1%, depending on whether the category is cropland soils only, managed soils and pasture, or the full inventory "agricultural soils" line, and on the database and metric used; the 4.1% end rests on a single unverified source.
  conf: not stated · class: not stated · holds: the note's own range, spanning SRCCL cropland soils (~1.5%), AR6 Figure 7.3 managed soils and pasture (~2.4%) and Climate Watch/WRI agricultural soils (4.1%) · src: ipccSummaryPolicymakers2019, nabuursAgricultureForestryOther2022, ritchieSectorSectorWhere2020 · trail: CB3-AG-EMISSIONS §Verdict, §Verdict: which boundary · from: CB3-AG-EMISSIONS:A-004, CB3-AG-EMISSIONS:A-016, CB3-AG-EMISSIONS:A-017

### synthetic-fertiliser: Synthetic nitrogen fertiliser
needs: soils, food-system
- **synthetic-fertiliser.1** Field N2O from synthetic fertiliser application, EDGAR via AR6: ~3% of AFOLU, ~0.4 Gt CO2eq, 2019, which is ~0.7% of global emissions (the review's arithmetic).
  conf: not stated · class: deriv (note: "My arithmetic") · holds: 2019; N2O; AR6 GWP100; Figure 7.3 read from image · src: nabuursAgricultureForestryOther2022 (the review's arithmetic on its figures) · trail: CB3-AG-EMISSIONS §Boundary D · from: CB3-AG-EMISSIONS:B-0070, CB3-AG-EMISSIONS:B-0071, CB3-AG-EMISSIONS:B-0056, CB3-AG-EMISSIONS:B-0133
- **synthetic-fertiliser.2** FAOSTAT: field N2O from synthetic fertiliser was 601 Mt CO2eq in 2019 (up 42% since 1990); fertiliser manufacturing, counted separately under pre- and post-production, was 408 Mt CO2eq.
  conf: not stated · class: not stated · holds: 2019; FAOSTAT; AR5 GWP100; Tubiello et al. 2022 Table 1 · src: tubielloPrePostproductionProcesses2022 · trail: CB3-AG-EMISSIONS §Boundary D · from: CB3-AG-EMISSIONS:B-0072
- **synthetic-fertiliser.3** 601 Mt against FAO's ~53 Gt total is ~1.1% (the review's arithmetic).
  conf: not stated · class: deriv (note: "My arithmetic") · holds: 2019; FAOSTAT; 30% assigned uncertainty · src: tubielloPrePostproductionProcesses2022 (the review's arithmetic on its figures) · trail: CB3-AG-EMISSIONS §Boundary D · from: CB3-AG-EMISSIONS:B-0073, CB3-AG-EMISSIONS:B-0132
- **synthetic-fertiliser.4** Menegat et al. 2022: "the synthetic N fertiliser supply chain was responsible for estimated emissions of 1.13 GtCO2e in 2018, representing 10.6% of agricultural emissions and 2.1% of global GHG emissions", with production 38.8%, field emissions 58.6% and transportation 2.6%.
  conf: not stated · class: not stated · holds: whole synthetic N supply chain; 2018; CO2 + N2O · src: menegatGreenhouseGasEmissions2022 (Abstract read only) · trail: CB3-AG-EMISSIONS §Boundary D, §No adversarial pass · from: CB3-AG-EMISSIONS:B-0074, CB3-AG-EMISSIONS:B-0075, CB3-AG-EMISSIONS:B-0076, CB3-AG-EMISSIONS:B-0130, CB3-AG-EMISSIONS:B-0010 · limit: access (note: "note where the review itself says it read only an abstract")
- **synthetic-fertiliser.5** An author correction to Menegat et al. 2022 exists but concerns figure axis labels and a supplementary table, not the headline.
  conf: not stated · class: not stated · holds: the correction's abstract or publisher metadata · src: menegatAuthorCorrectionGreenhouse2022 (abstract or publisher metadata) · trail: CB3-AG-EMISSIONS §Boundary D · from: CB3-AG-EMISSIONS:B-0076
- **synthetic-fertiliser.6** EDGAR's 0.4 Gt and FAOSTAT's 0.601 Gt for the same quantity, field N2O from synthetic fertiliser, differ by roughly 50%; neither source the review read states a reason for this gap, and AR6 notes only that FAOSTAT, EDGAR and USEPA global means "are within the uncertainty bounds of EDGAR" given assessed uncertainties of 30% (CH4) and 60% (N2O).
  conf: not stated · class: not stated · holds: 2019; EDGAR via AR6 Figure 7.3 and FAOSTAT Table 1; AR6 Table 7.1 footnote c · src: nabuursAgricultureForestryOther2022, tubielloPrePostproductionProcesses2022 · trail: CB3-AG-EMISSIONS §Boundary D · from: CB3-AG-EMISSIONS:B-0077, CB3-AG-EMISSIONS:B-0078

### five-percent: Which boundary produces a figure near five per cent
needs: soils, n2o, food-system, afolu, farm-gate
- **five-percent.1** No boundary in the current authoritative literature produces (exactly) five per cent for agriculture, and none produces it for agricultural soils.
  conf: not stated · class: not stated · holds: the boundaries and sources the review read · src: none (the reviewer's verdict) · trail: CB3-AG-EMISSIONS §Verdict, §Verdict: which boundary · from: CB3-AG-EMISSIONS:A-001, CB3-AG-EMISSIONS:A-005
- **five-percent.2** Three boundaries land close enough that a "roughly 5%" claim could have originated from any of them, and they are not interchangeable: N2O from agricultural soils at 4.1% (Climate Watch/WRI 2016 via Our World in Data, which the review calls its own weakest-supported number, one unverified secondary presentation); all anthropogenic N2O across every sector at ~4.7%; and emissions outside the farm gate at 5–10%.
  conf: not stated · class: not stated · holds: Climate Watch/WRI via OWID (2016), AR6 WGIII Ch. 7 Table 7.1 (2010–2019), SRCCL A.3.6 (2007–2016) · src: ritchieSectorSectorWhere2020, nabuursAgricultureForestryOther2022, ipccSummaryPolicymakers2019 · trail: CB3-AG-EMISSIONS §Verdict, §Verdict: which boundary · from: CB3-AG-EMISSIONS:A-002, CB3-AG-EMISSIONS:A-005
- **five-percent.3** The 4.1% agricultural soils figure is the closest match to a soils-specific claim, and the only widely circulated breakdown in which a soils category sits near 5%.
  conf: not stated · class: not stated · holds: Climate Watch/WRI for 2016, as presented by Our World in Data · src: ritchieSectorSectorWhere2020 · trail: CB3-AG-EMISSIONS §Verdict: which boundary · from: CB3-AG-EMISSIONS:A-006, CB3-AG-EMISSIONS:A-007
- **five-percent.4** If a "5%" claim is really about N2O rather than about soils, all anthropogenic N2O (~4.7%) is what it matches, but that figure includes fossil fuel, industry, waste and biomass burning N2O, not just agriculture.
  conf: not stated · class: not stated · holds: 2010–2019; AR6 Table 7.1 · src: nabuursAgricultureForestryOther2022 · trail: CB3-AG-EMISSIONS §Verdict: which boundary · from: CB3-AG-EMISSIONS:A-010, CB3-AG-EMISSIONS:A-011
- **five-percent.5** Emissions outside the farm gate (5–10%, SRCCL) and non-food agriculture plus other deforestation drivers (5%, Poore & Nemecek) are both exactly 5% at one end, and both are about something else entirely: supply chains and non-food crops.
  conf: not stated · class: not stated · holds: SRCCL A.3.6 (2007–2016); Poore & Nemecek 2018 · src: ipccSummaryPolicymakers2019, pooreReducingFoodS2018 · trail: CB3-AG-EMISSIONS §Verdict: which boundary · from: CB3-AG-EMISSIONS:A-012, CB3-AG-EMISSIONS:A-013
- **five-percent.6** A figure near 5% is not agricultural production (10.7–14.6%), not AFOLU (13–22%), not agriculture with land-use change for food (16–27%), and not the food system (21–42%).
  conf: not stated · class: not stated · holds: the note's own ranges, spanning AR6 Ch. 7 non-CO2 and FAOSTAT farm gate (10.7–14.6%), AR6 Ch. 7 and SPM (13–22%), SRCCL A.3.6 (16–27%), SRCCL and AR6 Ch. 12 (21–42%) · src: nabuursAgricultureForestryOther2022, faoGreenhouseGasEmissions2024, ipccSummaryPolicymakers2022, ipccSummaryPolicymakers2019, babikerCrosssectoralPerspectives2022 · trail: CB3-AG-EMISSIONS §Verdict, §Verdict: which boundary · from: CB3-AG-EMISSIONS:A-003, CB3-AG-EMISSIONS:A-014
- **five-percent.7** A figure near 5% is three to eight times smaller than any of those, and can only belong to a soils- or N2O-specific boundary.
  conf: not stated · class: not stated · holds: the ranges in five-percent.6 · src: none (the reviewer's synthesis) · trail: CB3-AG-EMISSIONS §Verdict: which boundary · from: CB3-AG-EMISSIONS:A-015

## Do not say

- **dns.1** "Agriculture accounts for about 5% of global greenhouse gas emissions."
  why: the note's verdict: no boundary in the current authoritative literature produces five per cent for agriculture; agricultural production is 10.7–14.6%, AFOLU 13–22%, the food system 21–42% · instead: five-percent.1, five-percent.6 · trail: CB3-AG-EMISSIONS §Verdict: which boundary · from: CB3-AG-EMISSIONS:A-001, CB3-AG-EMISSIONS:A-014
- **dns.2** "Agricultural soils produce 5% of global greenhouse gas emissions."
  why: the note's verdict: no boundary produces five per cent for agricultural soils; published estimates range from about 1.5% to 4.1% · instead: soils.8, five-percent.3 · trail: CB3-AG-EMISSIONS §Verdict · from: CB3-AG-EMISSIONS:A-001, CB3-AG-EMISSIONS:A-004
- **dns.3** "About 5% of global emissions, whether counted as soil N2O, all N2O or emissions outside the farm gate."
  why: the note says the three near-5% boundaries "are not interchangeable" · instead: five-percent.2 · trail: CB3-AG-EMISSIONS §Verdict: which boundary · from: CB3-AG-EMISSIONS:A-005
- **dns.4** "Agriculture's N2O is about 4.7% of global greenhouse gas emissions."
  why: the ~4.7% is all anthropogenic N2O and includes fossil fuel, industry, waste and biomass burning N2O, not just agriculture · instead: n2o.2, n2o.3, n2o.7 · trail: CB3-AG-EMISSIONS §Verdict: which boundary · from: CB3-AG-EMISSIONS:A-011
- **dns.5** "AR6 gives two rival estimates of AFOLU's share: 22% and 13–21%."
  why: the note: quoting them as though they were rival estimates would be an error; they are the same assessment on different periods and CO2 conventions · instead: afolu.4, afolu.5 · trail: CB3-AG-EMISSIONS §Boundary B · from: CB3-AG-EMISSIONS:B-0040
- **dns.6** "The 13–21% range for AFOLU reflects statistical uncertainty."
  why: the note: the spread is not statistical noise but two different CO2 accounting methods · instead: afolu.2, co2-accounting.1 · trail: CB3-AG-EMISSIONS §Boundary B · from: CB3-AG-EMISSIONS:B-0035
- **dns.7** "Livestock produces 18% of global greenhouse gas emissions."
  why: the note: the 18% figure is superseded and should not be treated as current · instead: livestock.1, livestock.2, livestock.3 · trail: CB3-AG-EMISSIONS §Boundary C · from: CB3-AG-EMISSIONS:B-0052
- **dns.8** "AFOLU accounts for 23% of total net anthropogenic emissions" (SRCCL, 2007–2016) as the current figure.
  why: the note: SRCCL's AFOLU figure has been superseded by AR6's 13–21% for 2010–2019 · instead: afolu.1, afolu.6 · trail: CB3-AG-EMISSIONS §Boundary B · from: CB3-AG-EMISSIONS:B-0041, CB3-AG-EMISSIONS:B-0042
- **dns.9** "EDGAR and FAOSTAT agree on field N2O from synthetic fertiliser."
  why: the two differ by roughly 50% for the same quantity; the note says to report this as unexplained divergence, not as agreement · instead: synthetic-fertiliser.6 · trail: CB3-AG-EMISSIONS §Boundary D · from: CB3-AG-EMISSIONS:B-0077, CB3-AG-EMISSIONS:B-0079
- **dns.10** "EDGAR-FOOD's one-third figure is accepted, since no one has disputed it."
  why: the note: finding no published criticism is absence of published criticism, not endorsement · instead: food-system.16 · trail: CB3-AG-EMISSIONS §Bounding and negative facts · from: CB3-AG-EMISSIONS:B-0101, CB3-AG-EMISSIONS:B-0103

## Gaps

- **gap.1** The figures the answers rest on were never checked by a second reader: the 4.1% Climate Watch/WRI agricultural soils figure, the ~4.7% all-N2O share, SRCCL's 5–10% outside the farm gate, Poore & Nemecek's 5%, the ~3.5%, ~2.4% and ~1.5% soil reconstructions, and the excluded ranges 10.7–14.6%, 13–22%, 16–27% and 21–42%. The note ran no critic and no second agent re-deriving the load-bearing figures; references were verified mechanically, with no claim-level verification.
  blocks: five-percent, soils, n2o, food-system, afolu, farm-gate · origin: no critique; the note's own warning and verification log · trail: CB3-AG-EMISSIONS §No adversarial pass, §Verification log · from: CB3-AG-EMISSIONS:B-0008, CB3-AG-EMISSIONS:B-0009, CB3-AG-EMISSIONS:B-0010, CB3-AG-EMISSIONS:B-0139, CB3-AG-EMISSIONS:B-0140
- **gap.2** The 4.1% agricultural soils figure checked against the Climate Watch dataset itself; the review could verify it only as presented by Our World in Data.
  blocks: soils.6, five-percent.3 · origin: source not obtained that matters · src: ritchieSectorSectorWhere2020 · trail: CB3-AG-EMISSIONS §What this review does · from: CB3-AG-EMISSIONS:B-0015, CB3-AG-EMISSIONS:A-008
- **gap.3** FAO's agrifood share for 2023 from the text of Analytical Brief 115 itself, to settle 32% (web summary) against 30% (COP30 takeaways); the review could not obtain the brief's own text.
  blocks: food-system.11, food-system.19 · origin: source not obtained that matters; two FAO communications disagree · src: faoGreenhouseGasEmissions2025a, faoGreenhouseGasEmissions2025b · trail: CB3-AG-EMISSIONS §Boundary A · from: CB3-AG-EMISSIONS:B-0027
- **gap.4** The reason EDGAR (0.4 Gt) and FAOSTAT (0.601 Gt) differ by roughly 50% for field N2O from synthetic fertiliser; no source the review read states one.
  blocks: synthetic-fertiliser.6 · origin: not found · trail: CB3-AG-EMISSIONS §Boundary D · from: CB3-AG-EMISSIONS:B-0078
- **gap.5** The reason FAO's global total (53.5 Gt for 2022) differs from AR6's (55.9–59 Gt); neither FAO brief the review read explains it.
  blocks: denominator.1, denominator.3 · origin: not found · trail: CB3-AG-EMISSIONS §Where the major sources differ · from: CB3-AG-EMISSIONS:B-0085
- **gap.6** Sources read only as abstract, metadata or a targeted extract, whose figures enter the review: Menegat et al. 2022 (2.1%) and its author correction, IPCC AR6 WGIII Chapter 12 (23–42%), FAO's 2025 agrifood release; and FAO 2023 (~12% for livestock), retrieved via a press summary and repository listing only.
  blocks: synthetic-fertiliser.4, food-system.9, food-system.11, livestock.2 · origin: sources not obtained in full · src: menegatGreenhouseGasEmissions2022, babikerCrosssectoralPerspectives2022, faoGreenhouseGasEmissions2025a, faoPathwaysTowardsLower2023 · trail: CB3-AG-EMISSIONS §What this review does · from: CB3-AG-EMISSIONS:B-0014
- **gap.7** The AR6 Figure 7.3 activity shares (managed soils and pasture 11%, synthetic fertiliser application 3%) confirmed from the chapter's text or data; the review read them off the rendered figure.
  blocks: soils.2, soils.3, synthetic-fertiliser.1 · origin: figure read from a rendered image, not the text · trail: CB3-AG-EMISSIONS §Boundary D · from: CB3-AG-EMISSIONS:B-0055

## Out of scope

- CB3-AG-EMISSIONS:B-0001..0003: the note's role (scope of the result note)
- CB3-AG-EMISSIONS:B-0004..0006: provenance of the run (brief given verbatim, routing withheld, blind parallel agents, search routes)
- CB3-AG-EMISSIONS:B-0013: access record of the sources read (applied in Sources)
- CB3-AG-EMISSIONS:B-0105: table header
- CB3-AG-EMISSIONS:B-0134..0138: post-hoc DOI verification and the reference [15] DOI correction (applied in Sources)

## Sources

```bibtex
@incollection{nabuursAgricultureForestryOther2022,
  author = {Nabuurs, G-J. and Mrabet, R. and Abu Hatab, A. and Bustamante, M. and Clark, H. and Havlík, P. and House, J. and Mbow, C. and Ninan, K.N. and Popp, A. and Roe, S. and Sohngen, B. and Towprayoon, S.},
  title = {Agriculture, Forestry and Other Land Uses (AFOLU)},
  booktitle = {Climate Change 2022: Mitigation of Climate Change. Contribution of Working Group III to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change},
  editor = {Shukla, P.R. and Skea, J. and Slade, R. and Al Khourdajie, A. and van Diemen, R. and McCollum, D. and Pathak, M. and Some, S. and Vyas, P. and Fradera, R. and Belkacemi, M. and Hasija, A. and Lisboa, G. and Luz, S. and Malley, J.},
  pages = {747--860},
  publisher = {Cambridge University Press},
  address = {Cambridge, UK and New York, NY, USA},
  year = {2022},
  doi = {10.1017/9781009157926.009},
  url = {https://www.ipcc.ch/report/ar6/wg3/downloads/report/IPCC_AR6_WGIII_Chapter07.pdf},
  note = {access: full_text (read in full or in substantial part: executive summary, §7.2.1, §7.2.3, Table 7.1, and Figure 7.3 read from a rendered page image); cited as: CB3-AG-EMISSIONS [1]}
}
@incollection{ipccSummaryPolicymakers2019,
  author = {{IPCC}},
  title = {Summary for Policymakers},
  booktitle = {Climate Change and Land: an IPCC Special Report on climate change, desertification, land degradation, sustainable land management, food security, and greenhouse gas fluxes in terrestrial ecosystems},
  editor = {Shukla, P.R. and Skea, J. and Calvo Buendia, E. and Masson-Delmotte, V. and Pörtner, H.-O. and Roberts, D.C. and Zhai, P. and Slade, R. and Connors, S. and van Diemen, R. and Ferrat, M. and Haughey, E. and Luz, S. and Neogi, S. and Pathak, M. and Petzold, J. and Portugal Pereira, J. and Vyas, P. and Huntley, E. and Kissick, K. and Belkacemi, M. and Malley, J.},
  pages = {3--36},
  publisher = {IPCC},
  address = {Geneva},
  year = {2019},
  url = {https://www.ipcc.ch/site/assets/uploads/sites/4/2022/11/SRCCL_SPM.pdf},
  note = {access: full_text (section A.3 and its footnotes); cited as: CB3-AG-EMISSIONS [2]; incomplete: doi}
}
@article{crippaFoodSystemsResponsible2021,
  author = {Crippa, M. and Solazzo, E. and Guizzardi, D. and Monforti-Ferrario, F. and Tubiello, F.N. and Leip, A.},
  title = {Food systems are responsible for a third of global anthropogenic GHG emissions},
  journal = {Nature Food},
  volume = {2},
  number = {3},
  pages = {198--209},
  year = {2021},
  doi = {10.1038/s43016-021-00225-9},
  note = {access: full_text (abstract, methods, metric statements); cited as: CB3-AG-EMISSIONS [3]}
}
@article{tubielloPrePostproductionProcesses2022,
  author = {Tubiello, F.N. and Karl, K. and Flammini, A. and Gütschow, J. and Obli-Laryea, G. and Conchedda, G. and Pan, X. and Qi, S.Y. and Halldórudóttir Heiðarsdóttir, H. and Wanner, N. and Quadrelli, R. and Rocha Souza, L. and Benoit, P. and Hayek, M. and Sandalow, D. and Mencos Contreras, E. and Rosenzweig, C. and Rosero Moncayo, J. and Conforti, P. and Torero, M.},
  title = {Pre- and post-production processes increasingly dominate greenhouse gas emissions from agri-food systems},
  journal = {Earth System Science Data},
  volume = {14},
  number = {4},
  pages = {1795--1809},
  year = {2022},
  doi = {10.5194/essd-14-1795-2022},
  note = {access: full_text (abstract, Table 1, metric and uncertainty sections); cited as: CB3-AG-EMISSIONS [4]}
}
@article{tubielloGreenhouseGasEmissions2021,
  author = {Tubiello, F.N. and Rosenzweig, C. and Conchedda, G. and Karl, K. and Gütschow, J. and Xueyao, P. and Obli-Laryea, G. and Wanner, N. and Qiu, S.Y. and De Barros, J. and Flammini, A. and Mencos-Contreras, E. and Souza, L. and Quadrelli, R. and Heiðarsdóttir, H.H. and Benoit, P. and Hayek, M. and Sandalow, D.},
  title = {Greenhouse gas emissions from food systems: building the evidence base},
  journal = {Environmental Research Letters},
  volume = {16},
  number = {6},
  pages = {065007},
  year = {2021},
  doi = {10.1088/1748-9326/ac018e},
  note = {access: full_text (§2.4 limitations, §4 discussion); cited as: CB3-AG-EMISSIONS [5]}
}
@report{faoGreenhouseGasEmissions2024,
  author = {{FAO}},
  title = {Greenhouse gas emissions from agrifood systems. Global, regional and country trends, 2000–2022},
  series = {FAOSTAT Analytical Brief 94},
  institution = {FAO},
  address = {Rome},
  year = {2024},
  issn = {2709-0078},
  url = {https://openknowledge.fao.org/server/api/core/bitstreams/111b7ee8-282b-42ff-ad95-cccecd90f8ea/content},
  note = {access: full_text; cited as: CB3-AG-EMISSIONS [6]; incomplete: doi}
}
@article{tianComprehensiveQuantificationGlobal2020,
  author = {Tian, H. and Xu, R. and Canadell, J.G. and Thompson, R.L. and Winiwarter, W. and Suntharalingam, P. and Davidson, E.A. and Ciais, P. and Jackson, R.B. and Janssens-Maenhout, G. and Prather, M.J. and Regnier, P. and Pan, N. and Pan, S. and Peters, G.P. and Shi, H. and Tubiello, F.N. and Zaehle, S. and Zhou, F. and Arneth, A. and Battaglia, G. and Berthet, S. and Bopp, L. and Bouwman, A.F. and Buitenhuis, E.T. and Chang, J. and Chipperfield, M.P. and Dangal, S.R.S. and Dlugokencky, E. and Elkins, J.W. and Eyre, B.D. and Fu, B. and Hall, B. and Ito, A. and Joos, F. and Krummel, P.B. and Landolfi, A. and Laruelle, G.G. and Lauerwald, R. and Li, W. and Lienert, S. and Maavara, T. and MacLeod, M. and Millet, D.B. and Olin, S. and Patra, P.K. and Prinn, R.G. and Raymond, P.A. and Ruiz, D.J. and van der Werf, G.R. and Vuichard, N. and Wang, J. and Weiss, R.F. and Wells, K.C. and Wilson, C. and Yang, J. and Yao, Y.},
  title = {A comprehensive quantification of global nitrous oxide sources and sinks},
  journal = {Nature},
  volume = {586},
  number = {7828},
  pages = {248--256},
  year = {2020},
  doi = {10.1038/s41586-020-2780-0},
  note = {access: full_text (abstract, Table 1, methods); cited as: CB3-AG-EMISSIONS [7]}
}
@article{tianGlobalNitrousOxide2024,
  author = {Tian, H. and Pan, N. and Thompson, R.L. and Canadell, J.G. and Suntharalingam, P. and Regnier, P. and Davidson, E.A. and Prather, M. and Ciais, P. and Muntean, M. and Pan, S. and Winiwarter, W. and Zaehle, S. and Zhou, F. and Jackson, R.B. and Bange, H.W. and Berthet, S. and Bian, Z. and Bianchi, D. and Bouwman, A.F. and Buitenhuis, E.T. and Dutton, G. and Hu, M. and Ito, A. and Jain, A.K. and Jeltsch-Thömmes, A. and Joos, F. and Kou-Giesbrecht, S. and Krummel, P.B. and Lan, X. and Landolfi, A. and Lauerwald, R. and Li, Y. and Lu, C. and Maavara, T. and Manizza, M. and Millet, D.B. and Mühle, J. and Patra, P.K. and Peters, G.P. and Qin, X. and Raymond, P. and Resplandy, L. and Rosentreter, J.A. and Shi, H. and Sun, Q. and Tonina, D. and Tubiello, F.N. and van der Werf, G.R. and Vuichard, N. and Wang, J. and Wells, K.C. and Western, L.M. and Wilson, C. and Yang, J. and Yao, Y. and You, Y. and Zhu, Q.},
  title = {Global nitrous oxide budget (1980–2020)},
  journal = {Earth System Science Data},
  volume = {16},
  number = {6},
  pages = {2543--2604},
  year = {2024},
  doi = {10.5194/essd-16-2543-2024},
  note = {access: full_text (abstract, executive summary, Table 3, regional attribution); cited as: CB3-AG-EMISSIONS [8]}
}
@report{faoGreenhouseGasEmissions2025a,
  author = {{FAO}},
  title = {Greenhouse gas emissions from agrifood systems. Global, regional and country trends, 2001–2023},
  series = {FAOSTAT Analytical Brief 115},
  institution = {FAO},
  address = {Rome},
  year = {2025},
  doi = {10.4060/cd7300en},
  url = {https://www.fao.org/statistics/highlights-archive/highlights-detail/greenhouse-gas-emissions-from-agrifood-systems.-global--regional-and-country-trends--2001-2023/en},
  note = {access: abstract_only (the FAO web summary; not the brief's own text); cited as: CB3-AG-EMISSIONS [9]}
}
@report{faoGreenhouseGasEmissions2025b,
  author = {{FAO}},
  title = {Greenhouse gas emissions from agrifood systems 2001–2023: Takeaways},
  institution = {FAO},
  address = {Rome},
  year = {2025},
  url = {https://porelclima.org/images/2025/Belem_documentos/COP30_emisiones_agroalimentarias_FAO.pdf},
  note = {access: abstract_only (listed with [9] as read only as abstract or publisher metadata; the FAO COP30 takeaways PDF was retrieved); cited as: CB3-AG-EMISSIONS [9a]; incomplete: doi}
}
@article{pooreReducingFoodS2018,
  author = {Poore, J. and Nemecek, T.},
  title = {Reducing food's environmental impacts through producers and consumers},
  journal = {Science},
  volume = {360},
  number = {6392},
  pages = {987--992},
  year = {2018},
  doi = {10.1126/science.aaq0216},
  note = {access: full_text (accepted manuscript, headline results); cited as: CB3-AG-EMISSIONS [10]}
}
@online{ritchieSectorSectorWhere2020,
  author = {Ritchie, H.},
  title = {Sector by sector: where do global greenhouse gas emissions come from?},
  organization = {Our World in Data},
  year = {2020},
  url = {https://ourworldindata.org/ghg-emissions-by-sector},
  note = {access: full_text (Our World in Data sector page, full text; sector breakdown for 2016 sourced to Climate Watch and the World Resources Institute, which was not checked in the dataset itself); cited as: CB3-AG-EMISSIONS [11]; incomplete: doi}
}
@book{gerberTacklingClimateChange2013,
  author = {Gerber, P.J. and Steinfeld, H. and Henderson, B. and Mottet, A. and Opio, C. and Dijkman, J. and Falcucci, A. and Tempio, G.},
  title = {Tackling climate change through livestock – A global assessment of emissions and mitigation opportunities},
  publisher = {Food and Agriculture Organization of the United Nations},
  address = {Rome},
  year = {2013},
  isbn = {978-92-5-107920-1},
  url = {https://www.fao.org/3/i3437e/i3437e.pdf},
  note = {access: full_text (headline sections and the Annex comparing it with Livestock's Long Shadow); cited as: CB3-AG-EMISSIONS [12]; incomplete: doi}
}
@article{menegatGreenhouseGasEmissions2022,
  author = {Menegat, S. and Ledo, A. and Tirado, R.},
  title = {Greenhouse gas emissions from global production and use of nitrogen synthetic fertilisers in agriculture},
  journal = {Scientific Reports},
  volume = {12},
  pages = {14490},
  year = {2022},
  doi = {10.1038/s41598-022-18773-w},
  note = {access: abstract_only (abstract read only); cited as: CB3-AG-EMISSIONS [13]}
}
@article{menegatAuthorCorrectionGreenhouse2022,
  author = {Menegat, S. and Ledo, A. and Tirado, R.},
  title = {Author Correction: Greenhouse gas emissions from global production and use of nitrogen synthetic fertilisers in agriculture},
  journal = {Scientific Reports},
  volume = {12},
  pages = {19777},
  year = {2022},
  doi = {10.1038/s41598-022-24242-1},
  note = {access: abstract_only (abstract or publisher metadata); cited as: CB3-AG-EMISSIONS [13a]}
}
@article{lynchAgricultureSContribution2021,
  author = {Lynch, J. and Cain, M. and Frame, D. and Pierrehumbert, R.},
  title = {Agriculture's contribution to climate change and role in mitigation is distinct from predominantly fossil CO2-emitting sectors},
  journal = {Frontiers in Sustainable Food Systems},
  volume = {4},
  pages = {518039},
  year = {2021},
  doi = {10.3389/fsufs.2020.518039},
  note = {access: full_text (full HTML text, targeted); cited as: CB3-AG-EMISSIONS [14]}
}
@incollection{babikerCrosssectoralPerspectives2022,
  author = {Babiker, M. and Berndes, G. and Blok, K. and Cohen, B. and Cowie, A. and Geden, O. and Ginzburg, V. and Leip, A. and Smith, P. and Sugiyama, M. and Yamba, F.},
  title = {Cross-sectoral perspectives},
  booktitle = {Climate Change 2022: Mitigation of Climate Change. Contribution of Working Group III to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change},
  editor = {Shukla, P.R. and others},
  pages = {1245--1354},
  publisher = {Cambridge University Press},
  address = {Cambridge, UK and New York, NY, USA},
  year = {2022},
  doi = {10.1017/9781009157926.014},
  url = {https://www.ipcc.ch/report/ar6/wg3/downloads/report/IPCC_AR6_WGIII_Chapter12.pdf},
  note = {access: abstract_only (targeted text extraction of the food-system statements only); cited as: CB3-AG-EMISSIONS [15]; DOI as corrected in the note's verification log (the agent gave 10.1017/9781009157926.005, which resolves to AR6 WGIII Chapter 3); incomplete: editor (the note gives Shukla, P.R. et al.)}
}
@incollection{ipccSummaryPolicymakers2022,
  author = {{IPCC}},
  title = {Summary for Policymakers},
  booktitle = {Climate Change 2022: Mitigation of Climate Change. Contribution of Working Group III to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change},
  editor = {Shukla, P.R. and Skea, J. and Slade, R. and Al Khourdajie, A. and van Diemen, R. and McCollum, D. and Pathak, M. and Some, S. and Vyas, P. and Fradera, R. and Belkacemi, M. and Hasija, A. and Lisboa, G. and Luz, S. and Malley, J.},
  pages = {3--48},
  publisher = {Cambridge University Press},
  address = {Cambridge, UK and New York, NY, USA},
  year = {2022},
  doi = {10.1017/9781009157926.001},
  url = {https://www.ipcc.ch/report/ar6/wg3/downloads/report/IPCC_AR6_WGIII_SPM.pdf},
  note = {access: not stated; cited as: CB3-AG-EMISSIONS [16]}
}
@report{faoPathwaysTowardsLower2023,
  author = {{FAO}},
  title = {Pathways towards lower emissions – A global assessment of the greenhouse gas emissions and mitigation options from livestock agrifood systems},
  institution = {FAO},
  address = {Rome},
  year = {2023},
  doi = {10.4060/cc9029en},
  url = {https://openknowledge.fao.org/server/api/core/bitstreams/a06a30d3-6e9d-4e9c-b4b7-29a6cc307208/content},
  note = {access: secondary (retrieved via FAO's own press summary and repository listing; full text not read, its 6.2 Gt / ~12 per cent figure reported as secondary); cited as: CB3-AG-EMISSIONS [17]}
}
@incollection{myhreAnthropogenicNaturalRadiative2013,
  author = {Myhre, G. and Shindell, D. and Bréon, F.-M. and Collins, W. and Fuglestvedt, J. and Huang, J. and Koch, D. and Lamarque, J.-F. and Lee, D. and Mendoza, B. and Nakajima, T. and Robock, A. and Stephens, G. and Takemura, T. and Zhang, H.},
  title = {Anthropogenic and Natural Radiative Forcing},
  booktitle = {Climate Change 2013: The Physical Science Basis. Contribution of Working Group I to the Fifth Assessment Report of the Intergovernmental Panel on Climate Change},
  editor = {Stocker, T.F. and Qin, D. and Plattner, G.-K. and Tignor, M. and Allen, S.K. and Boschung, J. and Nauels, A. and Xia, Y. and Bex, V. and Midgley, P.M.},
  pages = {659--740},
  publisher = {Cambridge University Press},
  address = {Cambridge, United Kingdom and New York, NY, USA},
  year = {2013},
  doi = {10.1017/CBO9781107415324.018},
  note = {background; access: full_text (§8.7.1.1 and §8.7.1.2 checked)}
}
@article{houghtonGlobalRegionalFluxes2017,
  author = {Houghton, R. A. and Nassikas, A. A.},
  title = {Global and regional fluxes of carbon from land use and land cover change 1850–2015},
  journal = {Global Biogeochemical Cycles},
  volume = {31},
  number = {3},
  pages = {456--472},
  year = {2017},
  doi = {10.1002/2016GB005546},
  note = {background; access: abstract_only (abstract checked on Crossref)}
}
```
