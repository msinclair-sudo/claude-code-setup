---
type: knowledge
title: Agricultural liming rates, supply, energy and carbon dioxide
inputs:
  - CB1-LIMING: PhD/Proposal/Research/Results/Agricultural Liming - Rates, Supply, Energy Cost and Emitted Carbon Dioxide.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-21
status: draft
tags:
  - research
  - knowledge
---

# Agricultural liming rates, supply, energy and carbon dioxide

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
| CB1-LIMING | [[Agricultural Liming - Rates, Supply, Energy Cost and Emitted Carbon Dioxide]] | no (the note says none ran) | numbered | no | no | fallback |

## Concepts

### agricultural-lime: Agricultural lime as a material
needs: none
- **agricultural-lime.1** Agricultural lime is a low-specification, coarse bulk product for which purity requirements are low.
  conf: not stated · class: not stated · holds: the reviewer's characterisation; no source cited for it · src: none (the reviewer's statement; no source cited) · trail: CB1-LIMING §Consumption, §Verdict on the scarcity · from: CB1-LIMING:A-019, CB1-LIMING:B-0059
- **agricultural-lime.2** Pelletised lime is usually specified at 90% passing a 150 µm sieve, and bulk ground limestone is coarser still.
  conf: not stated · class: not stated · holds: as reported by Goulding (2016) · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0079

### lime-requirement: Lime requirement and application rates
needs: agricultural-lime
- **lime-requirement.1** Lime rates are set by a lime requirement calculation, not by a standard dose, and the spread across soil types is wide enough that any single number misleads.
  conf: not stated · class: not stated · holds: the reviewer's summary of the rate evidence (UK grid, long-term experiments, tropical incubation datasets) · src: gouldingSoilAcidificationImportance2016, aramburumerlosEstimatingLimeRequirements2023 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0017
- **lime-requirement.2** The UK recommendation table (Fertiliser Manual RB209, reproduced by Goulding) specifies, to lift an arable soil (20 cm depth) from pH 5.0 to the recommended 6.5: 10 t/ha on sands, 12 on sandy and silt loams, 14 on clay loams and clays, 14 on organic soils and 16 on peaty soils.
  conf: not stated · class: not stated · holds: UK arable soils, 20 cm depth, target pH 6.5; the clearest published grid the reviewer found · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0018, CB1-LIMING:B-0019, CB1-LIMING:B-0130 · rating: "Well established"
- **lime-requirement.3** From a starting pH of 6.0 the same arable table gives 4, 5, 6 and 4 t/ha.
  conf: not stated · class: not stated · holds: UK arable soils, target pH 6.5 (RB209 via Goulding); the note gives four values against five soil classes at pH 5.0 · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0020, CB1-LIMING:B-0130 · rating: "Well established"
- **lime-requirement.4** Grassland, with a lower target of pH 6.0, takes roughly half the arable rates: 5, 6, 7, 7 and 6 t/ha from pH 5.0, and nothing at pH 6.0.
  conf: not stated · class: not stated · holds: UK grassland, target pH 6.0 (RB209 via Goulding) · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0021, CB1-LIMING:B-0130 · rating: "Well established"
- **lime-requirement.5** The lime requirement is strongly non-linear with starting pH and buffering capacity.
  conf: not stated · class: not stated · holds: temperate soils (UK evidence via Goulding) · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Application rates, §What is well established · from: CB1-LIMING:B-0022, CB1-LIMING:B-0130 · rating: "Well established"
- **lime-requirement.6** On the Park Grass Experiment, fewer than 5 t/ha of lime raised soil pH from about 6 to 7 over five years, but nearer 20 t/ha were needed to go from 5 to 7.
  conf: not stated · class: meas (note: "Park Grass Experiment") · holds: Park Grass Experiment (UK), five years · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0023
- **lime-requirement.7** The Rothamsted and Woburn long-term liming experiments used 5, 10 and 20 t/ha and 4.6, 10.9 and 17.3 t/ha respectively, with repeat applications marked on the pH time series.
  conf: not stated · class: meas (note: "long-term liming experiments") · holds: Rothamsted and Woburn (UK) · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0024
- **lime-requirement.8** Precision variable-rate application of pelletised lime on the North Wyke Farm Platform ran at up to 1 t/ha; across four fields with starting pH 5.5–5.8 the recommendation reached the pH 6.0 target only in the field that started at 5.8, falling 0.2 units short in the other three.
  conf: not stated · class: not stated · holds: North Wyke Farm Platform (UK), four fields · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0029, CB1-LIMING:B-0030
- **lime-requirement.9** Lime recommendations do not reliably deliver the correction they promise.
  conf: not stated · class: reading (note: "Recommendations do not reliably deliver") · holds: the reviewer's inference from the four North Wyke fields · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0031
- **lime-requirement.10** About 3.6 kg CaCO₃ balances the Ca²⁺ lost with nitrate per kg of ammonium-N nitrified (roughly 180 kg CaCO₃ per 50 kg NH₄-N), while neutralising the acid actually formed by nitrifying 50 kg NH₄-N requires about 360 kg CaCO₃.
  conf: not stated · class: not stated · holds: acidity from nitrification of ammonium-N (Goulding 2016) · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0032
- **lime-requirement.11** Goulding notes the second figure (about 360 kg CaCO₃ per 50 kg NH₄-N) matches field observations of lime requirement better than the first.
  conf: not stated · class: not stated · holds: as reported by Goulding (2016) · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0033
- **lime-requirement.12** For tropical soils the target is usually acidity saturation or base saturation rather than pH, and the estimated rate depends heavily on which target the model uses: "large differences in the estimated lime rates depending on the target soil chemical property" across 303 African soil samples.
  conf: not stated · class: not stated · holds: 303 African soil samples (Aramburu Merlos et al. 2023) · src: aramburumerlosEstimatingLimeRequirements2023 (read in full, used only for its framing) · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0034
- **lime-requirement.13** The compiled incubation datasets of Aramburu Merlos et al. span lime requirements of 0.2–23.9 cmolc/kg, which at a bulk density of 1 g/cm³ and 20 cm depth converts one-for-one to t CaCO₃/ha: a two-order-of-magnitude range, which the note gives as the answer to "what is a typical rate".
  conf: not stated · class: deriv (note: "converts one-for-one") · holds: compiled tropical incubation datasets; the conversion assumes bulk density 1 g/cm³ and 20 cm depth · src: aramburumerlosEstimatingLimeRequirements2023 (read in full, used only for its framing) · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0035, CB1-LIMING:B-0036
- **lime-requirement.14** The Ethiopian value-chain study reports about 20 quintals (2 t) of lime per hectare as the average requirement.
  conf: not stated · class: not stated · holds: Ethiopia (Oumer et al. 2023) · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0027

### application-frequency: Reapplication frequency
needs: lime-requirement
- **application-frequency.1** Reapplication frequency is less well pinned down than rate, and mostly appears as a working assumption rather than a measurement.
  conf: not stated · class: not stated · holds: West and McBride (2005, US) and Oumer et al. (2023, Ethiopia) · src: westContributionAgriculturalLime2005, oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Application rates, §What is well established · from: CB1-LIMING:B-0025, CB1-LIMING:B-0135
- **application-frequency.2** West and McBride adopt "a conservative application rate of 5 Mg crushed rock per hectare every 5 years," annualised to about 1 Mg/ha/yr, for their US calculation.
  conf: not stated · class: not stated · holds: an assumption for a US calculation, not a measurement · src: westContributionAgriculturalLime2005 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0026
- **application-frequency.3** Once the full recommended rate is applied, lime "can benefit farmers for up to five years" (Ethiopian value-chain study).
  conf: not stated · class: not stated · holds: Ethiopia (Oumer et al. 2023) · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0027
- **application-frequency.4** A five-year interval is common to the two very different systems (US and Ethiopia), but the reviewer found no systematic survey establishing it.
  conf: not stated · class: search (note: "I found no systematic survey establishing it") · holds: two systems, US and Ethiopia · src: westContributionAgriculturalLime2005, oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0028

### lime-consumption: Lime consumption
needs: agricultural-lime
- **lime-consumption.1** The US EPA inventory reports minerals applied to soils of 9.9 Mt limestone and 1.0 Mt dolomite in 2020, down from 19.0 and 2.4 Mt in 1990.
  conf: not stated · class: not stated · holds: US national inventory, 1990 and 2020 · src: usLimingCRFSource2022 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0037
- **lime-consumption.2** USGS reports that about 1% of the 1.5 billion tonnes of crushed stone produced in the US in 2024 went to agricultural uses, which is arithmetically about 15 Mt; earlier editions put the share at 2%.
  conf: not stated · class: deriv (note: "which is arithmetically about 15 Mt") · holds: US crushed-stone production, 2024; the 15 Mt is the reviewer's arithmetic · src: willettStoneCrushed2025 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0038
- **lime-consumption.3** West and McBride, reviewing the historical series, concluded that EPA's then-current 20 Tg figure understated the real total and that "30 Tg may better represent the annual U.S. consumption of aglime"; aglime comprises 3–5% of reported crushed limestone and dolomite usage, and an apparent 10 Tg decline between 1980 and 2000 coincided with a change in data collection and reporting.
  conf: not stated · class: not stated · holds: US, historical series to about 2001 · src: westContributionAgriculturalLime2005 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0039
- **lime-consumption.4** US consumption figures disagree with each other: the US number is somewhere between about 11 and 30 Mt/yr depending on whose accounting is taken (estimates differ by up to threefold), and the discrepancy is a reporting artefact, not a physical one.
  conf: cont (note: "Consumption figures disagree with each other") · class: not stated · holds: US; the range spans the EPA inventory, USGS and West and McBride; the note does not resolve it · src: usLimingCRFSource2022, willettStoneCrushed2025, westContributionAgriculturalLime2005 · trail: CB1-LIMING §Consumption, §What is well established · from: CB1-LIMING:B-0037, CB1-LIMING:B-0040, CB1-LIMING:B-0041, CB1-LIMING:B-0137
- **lime-consumption.5** UK annual lime applications "have declined from c 6000–7000 kt product/year to c 2500 kt product/year today," against a calculated average annual UK lime loss of 4,250,000 t CaCO₃.
  conf: not stated · class: not stated · holds: UK (Goulding 2016) · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Consumption, §Verdict on the scarcity · from: CB1-LIMING:B-0042, CB1-LIMING:A-011
- **lime-consumption.6** The UK is applying less than 60% of what its soils lose.
  conf: not stated · class: not stated · holds: UK; the reviewer's arithmetic from Goulding's two figures · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0043
- **lime-consumption.7** Goulding gives the cause of UK under-liming as economic ("although a short-term saving, reducing or omitting the application of lime to correct acidity risks significant economic loss") and attributes the decline to farm economics, not availability; nothing in Goulding attributes it to lime being unavailable.
  conf: not stated · class: not stated · holds: UK (Goulding 2016) · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Consumption, §Verdict on the scarcity · from: CB1-LIMING:B-0044, CB1-LIMING:B-0046, CB1-LIMING:A-011
- **lime-consumption.8** Of more than 200,000 UK soil analyses collated for 2013/14, about 40% of arable soils were below the recommended pH 6.5 and 57% of grassland soils below pH 6.0.
  conf: not stated · class: meas (note: "200,000 analyses") · holds: UK soil tests, 2013/14 · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0044
- **lime-consumption.9** Where liming falls short of agronomic need, the documented causes are demand, price and transport logistics, not the rock; under-liming in the UK is a demand-side and price-side phenomenon.
  conf: not stated · class: reading (note: "Under-liming in the UK is a demand-side and price-side phenomenon") · holds: the UK (Goulding) and Ethiopia (Oumer et al.) · src: gouldingSoilAcidificationImportance2016, oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Verdict, §Consumption, §Verdict on the scarcity · from: CB1-LIMING:A-003, CB1-LIMING:A-010, CB1-LIMING:B-0045
- **lime-consumption.10** There is no authoritative global consumption figure in the peer-reviewed or inventory literature the reviewer could reach, and no peer-reviewed global total that was not a counterfactual.
  conf: not stated · class: search (note: "no authoritative global consumption figure") · holds: the peer-reviewed and inventory literature reached by the review · src: none (a search result) · trail: CB1-LIMING §Consumption, §What is well established · from: CB1-LIMING:B-0047, CB1-LIMING:B-0138, CB1-LIMING:B-0139
- **lime-consumption.11** FAOSTAT's Emissions from Crops domain covers crop residues, residue burning, rice cultivation and nitrogen fertiliser application, and no FAOSTAT climate-change domain covers liming.
  conf: not stated · class: search (note: "no FAOSTAT climate-change domain covers liming") · holds: FAOSTAT climate-change domains · src: foodClimateChangeAgrifood2025 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0047, CB1-LIMING:B-0139
- **lime-consumption.12** Without a verified global total, any claim about global lime scarcity is being made without a global demand figure to test it against.
  conf: not stated · class: reading (note: "The absence of a verified global total is itself a finding") · holds: the reviewer's inference from the absent global figure · src: none (the reviewer's synthesis) · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0050
- **lime-consumption.13** The nearest thing to a global-scale quantification is a counterfactual: Wang et al., assuming all acid agricultural soils worldwide were limed periodically, estimate an additional CO₂ release of about 624–656 Tg CO₂/yr from lime mining, transport, application and dissolution combined.
  conf: not stated · class: model (note: "is a counterfactual") · holds: a fully limed world (all acid agricultural soils limed periodically); it does not describe current practice · src: wangPotentialBenefitsLiming2021 (abstract or structured summary only) · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0051, CB1-LIMING:B-0052, CB1-LIMING:B-0053

### lime-resource: The limestone resource and supply
needs: agricultural-lime
- **lime-resource.1** USGS states that "Stone resources are plentiful throughout the world" and classifies crushed-stone reserves as "Adequate, except where special types are needed or where local shortages exist."
  conf: not stated · class: not stated · holds: USGS Mineral Commodity Summaries 2025, Stone (Crushed), World Resources and reserves entries · src: willettStoneCrushed2025 · trail: CB1-LIMING §Verdict, §Consumption, §Verdict on the scarcity, §What is well established · from: CB1-LIMING:A-002, CB1-LIMING:A-007, CB1-LIMING:B-0054, CB1-LIMING:B-0055, CB1-LIMING:B-0133 · rating: "Well established"
- **lime-resource.2** No source the reviewer reviewed describes carbonate lime as a globally scarce or limited material, and the one primary source that speaks directly to the question (USGS, the agency whose job it is to make that assessment) says the opposite.
  conf: not stated · class: search (note: "No source I reviewed describes carbonate lime") · holds: the sources reviewed · src: willettStoneCrushed2025 · trail: CB1-LIMING §Verdict on the scarcity · from: CB1-LIMING:A-006, CB1-LIMING:A-008
- **lime-resource.3** The claim that carbonate lime is a globally scarce or limited material is unsupported; the evidence runs against scarcity from three further directions, none assembled to support a conclusion.
  conf: not stated · class: reading (note: "That is a direct negative") · holds: the review's verdict over USGS, Goulding (UK) and Oumer et al. (Ethiopia) · src: willettStoneCrushed2025, gouldingSoilAcidificationImportance2016, oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Verdict, §Verdict on the scarcity · from: CB1-LIMING:A-001, CB1-LIMING:A-008, CB1-LIMING:A-009, CB1-LIMING:A-028
- **lime-resource.4** About 70% of US crushed stone production in 2024 was limestone and dolomite, from roughly 3,500 quarries operated by about 1,400 companies across 50 states.
  conf: not stated · class: not stated · holds: US, 2024 · src: willettStoneCrushed2025 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0056
- **lime-resource.5** USGS states that "the supply of high-purity limestone and dolomite suitable for specialty uses is limited in many geographic areas"; the limitation is scoped to high-purity specialty grades, and nothing in the USGS text or any source the reviewer read extends it to agricultural lime.
  conf: not stated · class: not stated · holds: high-purity, specialty-use limestone and dolomite · src: willettStoneCrushed2025 · trail: CB1-LIMING §Consumption, §Verdict on the scarcity · from: CB1-LIMING:A-004, CB1-LIMING:A-016, CB1-LIMING:A-017, CB1-LIMING:A-018, CB1-LIMING:A-019, CB1-LIMING:B-0057, CB1-LIMING:B-0058, CB1-LIMING:B-0059
- **lime-resource.6** USGS flags localised shortages near urban and industrialised areas driven by zoning and land-development competition, which pushes new quarries away from population centres and raises delivered prices; USGS presents this as a price driver, not a reserve limitation.
  conf: not stated · class: not stated · holds: urban and industrialised areas (US) · src: willettStoneCrushed2025 · trail: CB1-LIMING §Consumption, §Verdict on the scarcity · from: CB1-LIMING:B-0060, CB1-LIMING:A-026
- **lime-resource.7** Oumer et al. found all surveyed Ethiopian public and private ag-lime plants running far below capacity "due to a lack of ag-lime demand": Guder at 12% of its 46,800 t/yr capacity, Dejen at 19%, Kella at 29%, Dashen at 2% of 144,000 t/yr, and Muger cement at under 1% of 400,000 t/yr (1–29% of installed capacity).
  conf: not stated · class: meas (note: "surveyed public and private ag-lime plants") · holds: Ethiopian ag-lime plants (Oumer et al. 2023) · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Consumption, §Verdict on the scarcity · from: CB1-LIMING:B-0061, CB1-LIMING:B-0062, CB1-LIMING:A-013
- **lime-resource.8** Oumer et al.'s SWOT tables list "Huge core-limestone deposits in all production areas" as an opportunity for both public and private producers, and the authors state that "producing a large quantity of ag-lime should not be an issue in Ethiopia."
  conf: not stated · class: not stated · holds: Ethiopia · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Consumption, §Verdict on the scarcity · from: CB1-LIMING:B-0063, CB1-LIMING:B-0064, CB1-LIMING:A-013
- **lime-resource.9** Beerling et al. (2020) state that logistical infrastructure to spread rock dust on croplands "already exists due to the common need to apply crushed limestone to reverse soil acidification from intensive cropping"; their argument for enhanced weathering at gigatonne scale rests in part on the existing scale and maturity of the crushed-rock industry, which the reviewer reads as implying a mature, large-scale extractive industry.
  conf: not stated · class: not stated · holds: croplands; the enhanced-weathering feasibility argument · src: beerlingPotentialLargescaleCO22020 · trail: CB1-LIMING §Consumption, §Verdict on the scarcity · from: CB1-LIMING:B-0066, CB1-LIMING:B-0067, CB1-LIMING:A-027
- **lime-resource.10** Two observations could be read as consistent with scarcity but do not evidence it: USGS's urban shortages (planning and land-use pressure) and Beerling et al.'s reliance on existing crushed-limestone infrastructure, which cuts against scarcity rather than for it.
  conf: not stated · class: reading (note: "Two observations could be read") · holds: the reviewer's reading of USGS and Beerling et al. (2020) · src: willettStoneCrushed2025, beerlingPotentialLargescaleCO22020 · trail: CB1-LIMING §Verdict on the scarcity · from: CB1-LIMING:A-025, CB1-LIMING:A-026, CB1-LIMING:A-027

### lime-access: Access to lime and value-chain constraints
needs: lime-resource
- **lime-access.1** Lime is genuinely hard to obtain in parts of sub-Saharan Africa: Silva et al. state that "lime is not widely available in the region," with crop yield loss to soil acidity on 32.7 Mha, 23% of sub-Saharan Africa's cropland, and a burden of US$6.0 billion.
  conf: not stated · class: not stated · holds: sub-Saharan Africa (Silva et al. 2025) · src: silvaSoilAcidityRemediation2025 (abstract or structured summary only) · trail: CB1-LIMING §Verdict on the scarcity · from: CB1-LIMING:A-022
- **lime-access.2** The binding constraints Oumer et al. identify in Ethiopia are demand creation, warehousing, power interruptions, procurement processes, transport, and the absence of a quality standard beyond calcium carbonate equivalence: the Ethiopian case locates the failure in the value chain, not the deposits.
  conf: not stated · class: not stated · holds: Ethiopia (Oumer et al. 2023) · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Consumption, §Verdict on the scarcity · from: CB1-LIMING:B-0065, CB1-LIMING:A-023
- **lime-access.3** Farmers named "the bulky nature of lime, the difficulty of transportation to farm plots (lack of simple machines), labor-intensive nature of the lime application, untimely (late) supply" as the adoption barriers; none of these is the rock running out.
  conf: not stated · class: not stated · holds: Ethiopian farmers (Oumer et al. 2023) · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0087, CB1-LIMING:B-0088
- **lime-access.4** In the region most often described as lime-constrained the constraint is not the rock: the sub-Saharan access constraint is a matter of access, not resource, a distribution problem on a locally abundant mineral rather than a resource one.
  conf: not stated · class: reading (note: "the review characterises as a distribution problem") · holds: the reviewer's reading of Silva et al. (2025) and Oumer et al. (2023) · src: silvaSoilAcidityRemediation2025, oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Verdict, §Verdict on the scarcity · from: CB1-LIMING:A-004, CB1-LIMING:A-012, CB1-LIMING:A-021, CB1-LIMING:A-024
- **lime-access.5** The literature supports that carbonate lime is bulky and that its supply chains fail badly in some regions.
  conf: not stated · class: not stated · holds: the review's summary of what the literature supports · src: oumerAgriculturalLimeValue2023, silvaSoilAcidityRemediation2025 · trail: CB1-LIMING §Verdict, §Verdict on the scarcity · from: CB1-LIMING:A-005, CB1-LIMING:A-029

### emission-factor: The IPCC Tier 1 emission factor for liming
needs: agricultural-lime
- **emission-factor.1** IPCC (2006) Volume 4 Chapter 11 §11.3 gives Equation 11.12: CO₂–C emission = (M_limestone × EF_limestone) + (M_dolomite × EF_dolomite), with M in tonnes per year and EF in tonnes of C per tonne of material.
  conf: not stated · class: not stated · holds: IPCC 2006 Guidelines, Tier 1 · src: dekleinChapter11N2O2006 · trail: CB1-LIMING §Carbon dioxide emitted · from: CB1-LIMING:B-0091, CB1-LIMING:B-0131 · rating: "Well established"
- **emission-factor.2** The Tier 1 default emission factors are 0.12 for limestone and 0.13 for dolomite, equivalent to the carbonate carbon contents of the materials (12% for CaCO₃, 13% for CaMg(CO₃)₂).
  conf: not stated · class: not stated · holds: IPCC 2006 Guidelines, Tier 1 · src: dekleinChapter11N2O2006 · trail: CB1-LIMING §Carbon dioxide emitted · from: CB1-LIMING:B-0092, CB1-LIMING:B-0093, CB1-LIMING:B-0131 · rating: "Well established"
- **emission-factor.3** Multiplying by 44/12 gives 0.44 t CO₂ per tonne of limestone and about 0.477 per tonne of dolomite.
  conf: not stated · class: deriv (note: "Multiplying by 44/12") · holds: the reviewer's conversion of the IPCC defaults · src: dekleinChapter11N2O2006 · trail: CB1-LIMING §Carbon dioxide emitted · from: CB1-LIMING:B-0094
- **emission-factor.4** Oxides and hydroxides of lime are excluded from the method, since they contain no inorganic carbon; their CO₂ is produced during manufacture, not after soil application.
  conf: not stated · class: not stated · holds: IPCC 2006 Guidelines · src: dekleinChapter11N2O2006 · trail: CB1-LIMING §Carbon dioxide emitted · from: CB1-LIMING:B-0095
- **emission-factor.5** The stated uncertainty is one-sided: "-50% based on approximations suggesting emissions may be less than half of the maximum value, which is the current factor value"; the default is a ceiling, representing "the absolute maximum emissions associated with liming."
  conf: not stated · class: not stated · holds: IPCC 2006 Guidelines, Tier 1 · src: dekleinChapter11N2O2006 · trail: CB1-LIMING §Carbon dioxide emitted, §What is well established · from: CB1-LIMING:B-0096, CB1-LIMING:B-0097, CB1-LIMING:B-0131 · rating: "Well established"
- **emission-factor.6** The Tier 2 text states that "emissions are likely to be less than assumed using the Tier 1 approach because the amount of CO₂ emitted after liming will depend on site-specific influences and transport of dissolved inorganic C through rivers and lakes to the ocean."
  conf: not stated · class: not stated · holds: IPCC 2006 Guidelines, Tier 2 · src: dekleinChapter11N2O2006 · trail: CB1-LIMING §Carbon dioxide emitted · from: CB1-LIMING:B-0098
- **emission-factor.7** Under the IPCC Tier 3 text, increases in soil or dissolved inorganic C from liming do not constitute a net removal of CO₂ from the atmosphere; carbonate-C from liming that is not returned to the atmosphere is considered a net reduction in the emissions associated with the practice.
  conf: not stated · class: not stated · holds: IPCC 2006 Guidelines, Tier 3 accounting · src: dekleinChapter11N2O2006 · trail: CB1-LIMING §Carbon dioxide emitted · from: CB1-LIMING:B-0099, CB1-LIMING:B-0100
- **emission-factor.8** The defaults have not been revised: in the 2019 Refinement, section 11.3 CO₂ Emissions from Liming reads, in its entirety, "No refinement", so the 2006 factors and their −50% uncertainty stand as of the most recent IPCC methodological update.
  conf: not stated · class: not stated · holds: IPCC 2019 Refinement · src: hergoualchChapter11N2O2019 · trail: CB1-LIMING §Carbon dioxide emitted, §What is well established · from: CB1-LIMING:B-0101, CB1-LIMING:B-0102, CB1-LIMING:B-0131 · rating: "Well established"

### inventory-factor: Country-specific factors and the US inventory
needs: emission-factor
- **inventory-factor.1** West and McBride concluded that "net CO₂ emissions from the application of aglime is 0.059 Mg C per Mg limestone and 0.064 Mg C per Mg dolomite," on the reasoning that the primary dissolution pathway is reaction with carbonic acid, which takes up CO₂, and that a significant fraction of dissolved constituents leach and are transported to the ocean, where much precipitates as CaCO₃.
  conf: not stated · class: not stated · holds: US analysis (West and McBride 2005) · src: westContributionAgriculturalLime2005 · trail: CB1-LIMING §Carbon dioxide emitted · from: CB1-LIMING:B-0103
- **inventory-factor.2** West and McBride estimated 4.4–6.6 Tg CO₂ for the US in 2001 from 20–30 Tg of aglime.
  conf: not stated · class: not stated · holds: US, 2001 · src: westContributionAgriculturalLime2005 · trail: CB1-LIMING §Carbon dioxide emitted · from: CB1-LIMING:B-0104
- **inventory-factor.3** The US EPA adopted the West and McBride factors, roughly half the default: the 2020 US emission estimate from liming of soils is 2.4 MMT CO₂ Eq. using the country-specific factors, against 4.8 MMT CO₂ Eq. using the IPCC (2006) default emission factors.
  conf: not stated · class: not stated · holds: US national inventory, 2020 · src: usLimingCRFSource2022, westContributionAgriculturalLime2005 · trail: CB1-LIMING §Carbon dioxide emitted, §What is well established · from: CB1-LIMING:B-0105, CB1-LIMING:B-0106, CB1-LIMING:B-0132 · rating: "Well established"
- **inventory-factor.4** EPA applies ±15% to the activity data, and models the fraction of lime dissolved by nitric against carbonic acid and the leached bicarbonate fraction as triangular distributions "between ranges of zero and 100 percent of the estimates."
  conf: not stated · class: not stated · holds: US national inventory, 2020 · src: usLimingCRFSource2022 · trail: CB1-LIMING §Carbon dioxide emitted · from: CB1-LIMING:B-0107
- **inventory-factor.5** EPA's Monte Carlo result puts 2020 US liming emissions "between -0.26 and 4.73 MMT CO₂ Eq. at the 95 percent confidence level," 111% below to 97% above the point estimate; EPA notes "a small probability of a negative emissions value leading to a net uptake of CO₂ from the atmosphere," so a national inventory's own published confidence interval for this source includes net removal.
  conf: not stated · class: model (note: "Its Monte Carlo result") · holds: US national inventory, 2020, 95% confidence level · src: usLimingCRFSource2022 · trail: CB1-LIMING §Carbon dioxide emitted, §What is well established · from: CB1-LIMING:B-0108, CB1-LIMING:B-0109, CB1-LIMING:B-0110, CB1-LIMING:B-0132 · rating: "Well established"

### field-co2: Measured CO₂ from limed soils
needs: emission-factor
- **field-co2.1** Cho et al. applied ¹³C-labelled CaCO₃ to a temperate Korean upland soil at 0–2 Mg/ha/yr and measured CO₂ fluxes by closed chamber over two years, finding "approximately 0.026 Mg C per Mg of CaCO₃ was emitted as CO₂," about a fifth of the IPCC default, and proposing 0.039 Mg C/Mg once an ocean term is added.
  conf: not stated · class: meas (note: "measured CO") · holds: one temperate Korean upland soil, 0–2 Mg/ha/yr, two years · src: choEvaluationCarbonDioxide2019 (abstract or structured summary only) · trail: CB1-LIMING §Where the numbers · from: CB1-LIMING:B-0111
- **field-co2.2** Cho et al. state that the IPCC assumption that all carbonate C is released "appears unlikely based on current knowledge of the very low solubility of CaCO₃ and carbonate transport through soil."
  conf: not stated · class: not stated · holds: the authors' framing · src: choEvaluationCarbonDioxide2019 (abstract or structured summary only) · trail: CB1-LIMING §Where the numbers · from: CB1-LIMING:B-0112
- **field-co2.3** Rousset et al., applying two carbonate liming products to an acidic sandy loam under winter rye, found soil pH rose from 5.7 to about 7.0, yield rose from 320 to over 400 g/m², and soil CO₂ emissions fell by approximately 40% for both materials; they conclude that "the IPCC principles, predicting increased CO₂ emissions from lime-derived C, may need to be re-examined in the future."
  conf: not stated · class: meas (note: "at least one field study") · holds: one acidic sandy loam under winter rye, two carbonate products · src: roussetSurprisingMinimisationCO22024 (abstract or structured summary only) · trail: CB1-LIMING §Where the numbers · from: CB1-LIMING:B-0113, CB1-LIMING:B-0134
- **field-co2.4** The actual emission factor is poorly constrained: measured values put it anywhere from 0.026 to 0.12 Mg C/Mg, with at least one field study finding a net reduction in soil CO₂ after liming; field measurements come in well below the default.
  conf: unclear (note: "Poorly constrained") · class: not stated · holds: the note's own range across IPCC (2006), West and McBride (2005) and Cho et al. (2019), with Rousset et al. (2024) · src: dekleinChapter11N2O2006, westContributionAgriculturalLime2005, choEvaluationCarbonDioxide2019, roussetSurprisingMinimisationCO22024 · trail: CB1-LIMING §Where the numbers, §What is well established · from: CB1-LIMING:B-0111, CB1-LIMING:B-0134
- **field-co2.5** Hamilton et al. compared Ca²⁺ + Mg²⁺ against carbonate alkalinity in soil solutions, tile drainage and streams, mainly in southern Michigan: soil solutions sampled under tension showed lime acting as either source or sink, but infiltrating waters, tile drainage and streams draining agricultural watersheds "tended to indicate net CO₂ uptake."
  conf: not stated · class: meas (note: "Their own paired measurements") · holds: mainly southern Michigan; soil solutions, tile drainage and streams · src: hamiltonEvidenceCarbonSequestration2007 · trail: CB1-LIMING §Where the numbers · from: CB1-LIMING:B-0114, CB1-LIMING:B-0115, CB1-LIMING:B-0120
- **field-co2.6** Hamilton et al. state that "dissolution of lime may sequester CO₂ equal to roughly 25–50% of its C content, in contrast to the prevailing assumption that all of the carbon in lime becomes CO₂," and that the 30 Tg/yr of US aglime "could thus sequester up to 1.9 Tg C/yr."
  conf: not stated · class: not stated · holds: extrapolated from mainly southern Michigan to 30 Tg/yr of US aglime; the strongest case the note finds for net carbon-negative liming · src: hamiltonEvidenceCarbonSequestration2007 · trail: CB1-LIMING §Where the numbers · from: CB1-LIMING:B-0114, CB1-LIMING:B-0116
- **field-co2.7** "As nitrate concentrations increased in infiltrating waters, lime switched from a net CO₂ sink to a source, implying nitrification as a major acidifying process."
  conf: not stated · class: not stated · holds: infiltrating waters, mainly southern Michigan (Hamilton et al. 2007) · src: hamiltonEvidenceCarbonSequestration2007 · trail: CB1-LIMING §Where the numbers · from: CB1-LIMING:B-0117
- **field-co2.8** Liming is carbon negative where dissolution is driven by carbonic acid and the bicarbonate is exported to groundwater and rivers, and carbon positive where strong acids, chiefly nitric acid from nitrification of fertiliser N, do the dissolving; the sign of the flux is a function of nitrogen management and hydrology, not a property of the lime.
  conf: not stated · class: reading (note: "That makes the sign of the flux a function of nitrogen management") · holds: the reviewer's reading of Hamilton et al. (2007) · src: hamiltonEvidenceCarbonSequestration2007 · trail: CB1-LIMING §Where the numbers · from: CB1-LIMING:B-0118, CB1-LIMING:B-0119
- **field-co2.9** Hamilton et al.'s own paired measurements were not one-sided: under their no-till treatment sink strength tended positive, while "on average, liming is neither a consistent source nor a sink for CO₂."
  conf: not stated · class: meas (note: "Their own paired measurements") · holds: Hamilton et al.'s paired treatments, including no-till · src: hamiltonEvidenceCarbonSequestration2007 · trail: CB1-LIMING §Where the numbers · from: CB1-LIMING:B-0120
- **field-co2.10** Biasi et al. (2008) published a paper titled "Direct experimental evidence for the contribution of lime to CO₂ release from managed peat soil", cited only as a pointer to a contrary result in an organic soil, with no claim about its magnitude.
  conf: not stated · class: not stated · holds: managed peat soil; title only · src: biasiDirectExperimentalEvidence2008 (title only) · trail: CB1-LIMING §Where the numbers · from: CB1-LIMING:B-0121, CB1-LIMING:B-0122
- **field-co2.11** Carbonate lime is itself a carbon dioxide source of contested magnitude.
  conf: cont (note: "contested magnitude") · class: not stated · holds: the review's summary of the CO₂ evidence · src: dekleinChapter11N2O2006, westContributionAgriculturalLime2005, choEvaluationCarbonDioxide2019, roussetSurprisingMinimisationCO22024, hamiltonEvidenceCarbonSequestration2007 · trail: CB1-LIMING §Verdict, §Verdict on the scarcity · from: CB1-LIMING:A-005, CB1-LIMING:A-029

### ghg-balance: The whole-system greenhouse gas balance of liming
needs: field-co2
- **ghg-balance.1** Wang et al., meta-analysing 1,570 observations from 121 field studies, find liming raises crop yield by 36.3%, increases SOC stocks by 4.51% annually, cuts soil N₂O by 21.3% and paddy CH₄ by 19.0%, giving a global GHG benefit of 633–749 Tg CO₂-eq/yr, offset by 624–656 Tg CO₂/yr from mining, transport, application and dissolution, so that "the overall GHG balance is likely neutral."
  conf: not stated · class: not stated · holds: global, 1,570 observations from 121 field studies; the offset is the counterfactual of all acid agricultural soils limed periodically · src: wangPotentialBenefitsLiming2021 (abstract or structured summary only) · trail: CB1-LIMING §Where the numbers · from: CB1-LIMING:B-0123
- **ghg-balance.2** Gibbons et al., on UK livestock farms, reported that liming to pH 6.0 as recommended reduced N₂O emissions and nitrate leaching, but that in CO₂-C equivalents "the GHG emissions from liming were about four times those saved by reducing N₂O emissions."
  conf: not stated · class: not stated · holds: UK livestock farms · src: gibbonsSustainableNutrientManagement2014 (described to me by Goulding at 7) · trail: CB1-LIMING §Where the numbers · from: CB1-LIMING:B-0124
- **ghg-balance.3** The whole-system balance is disputed, and the disagreement is large: neutral-to-beneficial at global scale (Wang et al.) and four-to-one adverse at UK farm scale (Gibbons et al.); the scopes, baselines and emission factors differ, and the note does not adjudicate.
  conf: cont (note: "The whole-system balance is disputed") · class: not stated · holds: global meta-analysis against UK livestock farms · src: wangPotentialBenefitsLiming2021, gibbonsSustainableNutrientManagement2014 · trail: CB1-LIMING §Where the numbers · from: CB1-LIMING:B-0123, CB1-LIMING:B-0125, CB1-LIMING:B-0126
- **ghg-balance.4** The soil-carbon term, which drives much of the difference, is itself unsettled: Holland et al., in a UK review, state that "the impacts of liming on soil carbon storage are variable and strongly relate to soil type, land use, climate and multiple management factors."
  conf: unclear (note: "is itself unsettled") · class: not stated · holds: UK review (Holland et al. 2018) · src: hollandLimingImpactsSoils2018 (abstract or structured summary only) · trail: CB1-LIMING §Where the numbers · from: CB1-LIMING:B-0127, CB1-LIMING:B-0128
- **ghg-balance.5** Paradelo et al. reviewed the literature and found that on balance liming increased soil C content, mostly because it increased yields and therefore residue returns.
  conf: not stated · class: not stated · holds: a literature review (Paradelo et al. 2015) · src: paradeloNetEffectLiming2015 (described by Goulding at 7) · trail: CB1-LIMING §Where the numbers · from: CB1-LIMING:B-0129

### delivery-emissions: Emissions from producing, transporting and spreading lime
needs: emission-factor
- **delivery-emissions.1** West and McBride quote West and Marland (2002) that "production of crushed limestone and transport to the delivery site results in CO₂ emissions of about 36 kg C per Mg of limestone," with fossil fuel combustion during spreading adding about 12 kg C/ha.
  conf: single (note: "a single 2002 estimate") · class: not stated · holds: a 2002 US estimate; the most-cited figure for energy and transport per tonne of agricultural lime · src: westSynthesisCarbonSequestration2002 (cited second-hand via West and McBride 2005), westContributionAgriculturalLime2005 · trail: CB1-LIMING §Energy and transport, §What is well established · from: CB1-LIMING:B-0068, CB1-LIMING:B-0069, CB1-LIMING:B-0136
- **delivery-emissions.2** Converting at 44/12, 36 kg C/t is about 132 kg CO₂ per tonne delivered.
  conf: not stated · class: deriv (note: "Converting at 44/12") · holds: the reviewer's conversion of the West and Marland (2002) figure · src: westSynthesisCarbonSequestration2002 (cited second-hand via West and McBride 2005) · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0070
- **delivery-emissions.3** Applying their 5 Mg/ha-every-5-years assumption, West and McBride get about 38 kg C/ha/yr from production, transport and application combined, against 120 kg C/ha/yr from the in-soil dissolution reaction at the IPCC default factor, for a total of 158.
  conf: single (note: "rests on one paper's arithmetic") · class: deriv (note: "rests on one paper's arithmetic") · holds: US; the 5 Mg/ha every 5 years assumption; dissolution at the IPCC default factor · src: westContributionAgriculturalLime2005 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0071, CB1-LIMING:B-0072, CB1-LIMING:B-0074
- **delivery-emissions.4** On that decomposition the supply chain does not dominate: the energy and transport of getting lime to the field is roughly a quarter of the carbon footprint of liming, and three quarters is the carbonate itself.
  conf: single (note: "rests on one paper's arithmetic") · class: deriv (note: "rests on one paper's arithmetic") · holds: West and McBride's US decomposition at the IPCC default factor; the 36 kg C/t figure is a 2002 US estimate read second-hand · src: westContributionAgriculturalLime2005, westSynthesisCarbonSequestration2002 (cited second-hand via West and McBride 2005) · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0072, CB1-LIMING:B-0073, CB1-LIMING:B-0074

### grinding-energy: Energy to grind rock
needs: agricultural-lime
- **grinding-energy.bg1** Enhanced weathering is the application of finely ground minerals over the land surface, which could be used to remove CO₂ from the atmosphere: the cations released as silicate minerals dissolve convert dissolved CO₂ to bicarbonate.
  kind: background · ref: hartmannEnhancedChemicalWeathering2013 · check: DOI 10.1002/rog.20004 resolves on Crossref (Reviews of Geophysics 51(2), 113–149); stated in the abstract
- **grinding-energy.1** Energy figures from the enhanced-weathering literature come from grinding rock far finer than agricultural lime, and so give an upper bound for agricultural lime rather than a like-for-like figure.
  conf: not stated · class: reading (note: "upper bound rather than a like-for-like figure") · holds: enhanced-weathering work on finer-ground basalt · src: liGeospatialAssessmentCost2024, beerlingPotentialLargescaleCO22020, beerlingTransformingUS2023 · trail: CB1-LIMING §Energy and transport, §What is well established · from: CB1-LIMING:B-0075, CB1-LIMING:B-0136
- **grinding-energy.2** Li et al., fitting Bond's law from a 300 µm feed, report grinding energy of roughly 9.7 kWh/t to a P80 of 100 µm, 19.4 kWh/t to 50 µm and about 128 kWh/t to 10 µm, with corresponding US grid-electricity costs of about $0.95, $1.88 and $5.81 per tonne at national average prices, and grinding CO₂ of roughly 5–35 kg CO₂/t.
  conf: not stated · class: model (note: "fitting Bond's law") · holds: enhanced-weathering feedstock, coterminous US, 300 µm feed, national average electricity prices · src: liGeospatialAssessmentCost2024 (numbers from an automated extraction of the full article rather than a line-by-line read) · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0076
- **grinding-energy.3** Li et al. conclude that "feedstock grinding is potentially the most energy- and emissions-intensive component" of the enhanced-weathering life cycle.
  conf: not stated · class: not stated · holds: enhanced-weathering life cycle · src: liGeospatialAssessmentCost2024 (numbers from an automated extraction of the full article rather than a line-by-line read) · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0077
- **grinding-energy.4** Beerling et al. (2020) state that "rock grinding to reduce particle size and maximise CDR is the primary energy consuming operation," and note that industrialised nations already spend up to about 2% of total energy production on rock comminution.
  conf: not stated · class: not stated · holds: enhanced weathering on croplands · src: beerlingPotentialLargescaleCO22020 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0078
- **grinding-energy.5** Because agricultural lime is specified far coarser, the low end of the enhanced-weathering grinding range is the relevant one, and grinding energy for agricultural lime should sit at or below about 10 kWh/t.
  conf: not stated · class: reading (note: "should sit at or below about 10 kWh/t") · holds: the reviewer's inference from Li et al. (2024) and Goulding (2016) · src: liGeospatialAssessmentCost2024, gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0079

### transport-cost: Transport, spreading and delivered cost
needs: agricultural-lime
- **transport-cost.1** The Beerling et al. preprint gives 2020 US values: transport cost of $0.07/t-km by road and $0.028/t-km by rail; road emissions around 50 g CO₂/t-km and rail around 15 g CO₂/t-km; spreading energy of 21 kWh/t rock, giving about 0.005 t CO₂/t spread; and a spreading cost of $5.5 per ton "based on the 2020 values for lime spreading in the United States."
  conf: not stated · class: not stated · holds: US, 2020 values; enhanced-weathering preprint Methods, not verified against the published version · src: beerlingTransformingUS2023 (preprint Methods) · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0080
- **transport-cost.2** In the Beerling et al. preprint the modelled truck share falls from 0.96 at 50 km to 0.31 at 1,750 km as rail takes over.
  conf: not stated · class: model (note: "Their modelled truck share") · holds: US enhanced-weathering model, distances from network analysis for basalt sources · src: beerlingTransformingUS2023 (preprint Methods) · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0081
- **transport-cost.3** The reviewer found no published measured distribution of haul distances for agricultural lime specifically; the enhanced-weathering papers compute distances from network analysis for basalt sources, a different geography.
  conf: not stated · class: search (note: "I did not find a published") · holds: the literature reached by the review · src: beerlingTransformingUS2023 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0082
- **transport-cost.4** Oumer et al. report that a private supplier won a bid to supply core limestone at 47 ETB per cubic metre, equivalent to 5.5 ETB per quintal.
  conf: not stated · class: not stated · holds: Ethiopia · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0083
- **transport-cost.5** Average transport cost of finished ag-lime to kebeles was 163 ETB/Qt in Oromia, SNNP and Sidama, and 60 ETB/Qt in east Gojjam, with unloading at 10 ETB/Qt and transporter margins of 27–57 ETB/Qt; distance-based rates ran 0.30–0.75 ETB/Qt/km.
  conf: not stated · class: not stated · holds: Ethiopian regions named · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0084
- **transport-cost.6** In Ethiopia the delivered cost is dominated by moving the material, not obtaining it: roughly 5.5 ETB/Qt at the quarry against 60–163 ETB/Qt to transport it to a rural distribution point, so the rock at the quarry costs roughly an order of magnitude less than moving it; this is the clearest published cost breakdown showing transport dominance the reviewer found.
  conf: not stated · class: not stated · holds: Ethiopia (Oumer et al. 2023) · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Energy and transport, §Verdict on the scarcity · from: CB1-LIMING:B-0083, CB1-LIMING:B-0085, CB1-LIMING:A-014
- **transport-cost.7** A scarce mineral does not have that cost structure.
  conf: not stated · class: reading (note: "A scarce mineral does not have that cost structure") · holds: the reviewer's inference from the Ethiopian cost breakdown · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Verdict on the scarcity · from: CB1-LIMING:A-015
- **transport-cost.8** At the Ethiopian processing plants, labour dominated internal costs: 55% for Dejen, with packaging and labelling at 16%.
  conf: not stated · class: not stated · holds: Dejen plant, Ethiopia · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0086
- **transport-cost.9** The literature supports that transport dominates lime's delivered cost.
  conf: not stated · class: not stated · holds: the review's summary; the only cost breakdown is Ethiopian · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Verdict · from: CB1-LIMING:A-005, CB1-LIMING:A-029
- **transport-cost.10** A search for a comparable delivered-cost breakdown for the US or Europe found only trade-press and forum material with no verifiable method, which the note does not report.
  conf: not stated · class: search (note: "found only trade-press and forum material") · holds: US and Europe · src: none (a search result) · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0089, CB1-LIMING:B-0090

## Do not say

- **dns.1** "Carbonate lime is a globally scarce or limited material."
  why: the review's verdict is UNSUPPORTED; USGS states stone resources are plentiful throughout the world · instead: lime-resource.1, lime-resource.3 · trail: CB1-LIMING §Verdict, §Verdict on the scarcity · from: CB1-LIMING:A-001, CB1-LIMING:A-028
- **dns.2** "Liming is a crude fix using a globally limited material."
  why: the note: the "globally limited" half fails · instead: lime-resource.3 · trail: CB1-LIMING §Verdict on the scarcity · from: CB1-LIMING:A-028
- **dns.3** The USGS sentence on high-purity specialty limestone cited as evidence of agricultural-lime scarcity.
  why: the note: treating that sentence as evidence for ag-lime scarcity would be a misreading; the limitation is scoped to high-purity specialty grades · instead: lime-resource.5 · trail: CB1-LIMING §Verdict on the scarcity · from: CB1-LIMING:A-020
- **dns.4** The sub-Saharan access constraint presented as lime scarcity.
  why: the note: a regional access constraint on a locally abundant mineral is a distribution problem, and the two should not be conflated · instead: lime-access.4 · trail: CB1-LIMING §Verdict on the scarcity · from: CB1-LIMING:A-024
- **dns.5** USGS's urban shortages, or the reliance of enhanced weathering on existing crushed-limestone infrastructure, cited as evidence of scarcity.
  why: the note: two observations could be read as consistent with scarcity but do not evidence it · instead: lime-resource.6, lime-resource.10 · trail: CB1-LIMING §Verdict on the scarcity · from: CB1-LIMING:A-025
- **dns.6** "Global agricultural lime consumption is 395–450 Mt/yr."
  why: the note: these come from commercial market-research vendors whose method and underlying data cannot be verified; dropped per the brief's instruction · instead: lime-consumption.10 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0048, CB1-LIMING:B-0049
- **dns.7** "US lime consumption is more than 45 million tons."
  why: the note: a market-research vendor's figure that contradicts both USGS and EPA · instead: lime-consumption.4 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0048
- **dns.8** Wang et al.'s 624–656 Tg CO₂/yr given as the emissions of current liming.
  why: the note: it bounds the scale of a fully limed world; it does not describe current practice · instead: lime-consumption.13 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0053
- **dns.9** A single typical lime application rate.
  why: the note: the spread across soil types is wide enough that any single number misleads · instead: lime-requirement.1, lime-requirement.13 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0017, CB1-LIMING:B-0036
- **dns.10** Lime reapplication every five years given as a measured or surveyed interval.
  why: the note: frequency mostly appears as a working assumption rather than a measurement; no systematic survey establishes it · instead: application-frequency.1, application-frequency.4 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0025, CB1-LIMING:B-0028
- **dns.11** "The energy and transport of delivering lime dominate its carbon footprint."
  why: the note: that number answers which part dominates, and the answer is not the supply chain · instead: delivery-emissions.4 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0072
- **dns.12** Enhanced-weathering grinding energies given as like-for-like figures for agricultural lime.
  why: the note: they give an upper bound rather than a like-for-like figure · instead: grinding-energy.1, grinding-energy.5 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0075
- **dns.13** Enhanced-weathering haul distances given as agricultural-lime haul distances.
  why: the note: those distances come from network analysis for basalt sources, a different geography · instead: transport-cost.3 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0082
- **dns.14** The IPCC default emission factor given as the expected CO₂ from liming.
  why: the guidelines state the factor is the absolute maximum, with a one-sided −50% uncertainty; the note: the default is a ceiling · instead: emission-factor.5 · trail: CB1-LIMING §Carbon dioxide emitted · from: CB1-LIMING:B-0096, CB1-LIMING:B-0097
- **dns.15** Lime-derived increases in soil or dissolved inorganic carbon counted as a net removal of CO₂ in IPCC accounting.
  why: the IPCC Tier 3 text, quoted by the note: it "does not constitute a net removal of CO₂ from the atmosphere" · instead: emission-factor.7 · trail: CB1-LIMING §Carbon dioxide emitted · from: CB1-LIMING:B-0099
- **dns.16** "Liming is a net carbon sink" or "Liming is a net carbon source", stated as a property of the lime.
  why: the note: the sign of the flux is a function of nitrogen management and hydrology, not a property of the lime; on average liming is neither a consistent source nor a sink · instead: field-co2.8, field-co2.9 · trail: CB1-LIMING §Where the numbers · from: CB1-LIMING:B-0119, CB1-LIMING:B-0120
- **dns.17** The whole-system greenhouse gas balance of liming stated one way (neutral, beneficial or adverse) without its scale.
  why: the note: the whole-system balance is disputed and it does not adjudicate; scopes, baselines and emission factors differ · instead: ghg-balance.3 · trail: CB1-LIMING §Where the numbers · from: CB1-LIMING:B-0125, CB1-LIMING:B-0126

## Gaps

- **gap.1** No figure in this note was checked by a second reader. The answers rest on: USGS's "plentiful" and "Adequate" statements and the specialty-grade limitation; the UK decline from 6,000–7,000 to about 2,500 kt/yr against a loss of 4,250 kt CaCO₃; Ethiopian plants at 1–29% of capacity; 5.5 ETB/Qt at the quarry against 60–163 ETB/Qt transport; Silva et al.'s 32.7 Mha, 23% of cropland and US$6.0 billion. The note says to treat the numbers as unconfirmed until spot-checked against the primary text, and no claim-level verification was performed.
  blocks: lime-resource, lime-consumption, lime-access, transport-cost · origin: no critique; the note's own warning and verification log · trail: CB1-LIMING §No adversarial, §Verification log · from: CB1-LIMING:B-0008, CB1-LIMING:B-0009, CB1-LIMING:B-0010, CB1-LIMING:B-0146, CB1-LIMING:B-0147
- **gap.2** A verified global agricultural lime consumption figure.
  blocks: lime-consumption.10, lime-consumption.12 · origin: "Absent" in the note's assessment; FAOSTAT has no liming domain · trail: CB1-LIMING §What is well established · from: CB1-LIMING:B-0138, CB1-LIMING:B-0139
- **gap.3** The US consumption disagreement (about 11 to 30 Mt/yr) left unresolved.
  blocks: lime-consumption.4 · origin: the note: "a genuine unresolved disagreement and I am not resolving it" · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0041
- **gap.4** A surveyed reapplication frequency for agricultural lime.
  blocks: application-frequency · origin: "Poorly constrained" in the note's assessment; no systematic survey found · trail: CB1-LIMING §What is well established · from: CB1-LIMING:B-0135
- **gap.5** Energy and transport per tonne of agricultural lime specifically: the most-cited figure is a single 2002 estimate, read second-hand, and the modern detail comes from enhanced-weathering work on finer-ground basalt.
  blocks: delivery-emissions, grinding-energy · origin: "Poorly constrained" in the note's assessment; West and Marland (2002) not read in the original · trail: CB1-LIMING §What is well established, §Energy and transport · from: CB1-LIMING:B-0136, CB1-LIMING:B-0074 · src: westSynthesisCarbonSequestration2002
- **gap.6** A published measured distribution of haul distances for agricultural lime.
  blocks: transport-cost.3 · origin: not found by the review · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0082
- **gap.7** A delivered-cost breakdown for agricultural lime in the US or Europe with a verifiable method.
  blocks: transport-cost.10 · origin: not found by the review · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0089
- **gap.8** The actual emission factor of applied lime, which measured values put between 0.026 and 0.12 Mg C/Mg.
  blocks: field-co2.4 · origin: "Poorly constrained" in the note's assessment · trail: CB1-LIMING §What is well established · from: CB1-LIMING:B-0134
- **gap.9** Biasi et al. (2008), a contrary result in a managed peat soil: the abstract was not obtained, so its magnitude is unknown.
  blocks: field-co2.10 · origin: source cited by title only · trail: CB1-LIMING §Where the numbers · from: CB1-LIMING:B-0122 · src: biasiDirectExperimentalEvidence2008
- **gap.10** The whole-system GHG balance: Gibbons et al. was not read in the original, and the scopes, baselines and emission factors of the global and UK estimates differ.
  blocks: ghg-balance.3 · origin: the note does not adjudicate; source read second-hand · trail: CB1-LIMING §Where the numbers · from: CB1-LIMING:B-0126 · src: gibbonsSustainableNutrientManagement2014
- **gap.11** The effect of liming on soil carbon storage.
  blocks: ghg-balance.4, ghg-balance.5 · origin: the note: "The soil-carbon term ... is itself unsettled"; Paradelo et al. read second-hand · trail: CB1-LIMING §Where the numbers · from: CB1-LIMING:B-0127 · src: hollandLimingImpactsSoils2018, paradeloNetEffectLiming2015
- **gap.12** The second-hand and title-only attributions (West and Marland 2002; Gibbons et al. 2014; Paradelo et al. 2015; Biasi et al. 2008) are the agent's and were not independently confirmed.
  blocks: delivery-emissions.1, ghg-balance.2, ghg-balance.5, field-co2.10 · origin: the verification log · trail: CB1-LIMING §Verification log · from: CB1-LIMING:B-0145
- **gap.13** The Beerling et al. cost and energy figures are from the 2023 preprint Methods and were not verified against the published 2025 version.
  blocks: transport-cost.1, transport-cost.2 · origin: the note's reference list · trail: CB1-LIMING §References · src: beerlingTransformingUS2023, beerlingTransformingUSAgriculture2025

## Out of scope

## Sources

```bibtex
@incollection{dekleinChapter11N2O2006,
  author = {De Klein, C. and Novoa, R.S.A. and Ogle, S. and Smith, K.A. and Rochette, P. and Wirth, T.C. and McConkey, B.G. and Mosier, A. and Rypdal, K.},
  title = {Chapter 11: N₂O Emissions from Managed Soils, and CO₂ Emissions from Lime and Urea Application},
  booktitle = {2006 IPCC Guidelines for National Greenhouse Gas Inventories, Volume 4: Agriculture, Forestry and Other Land Use},
  publisher = {Institute for Global Environmental Strategies (IGES), Hayama, Japan, for the IPCC National Greenhouse Gas Inventories Programme},
  pages = {11.1--11.54},
  year = {2006},
  url = {https://www.ipcc-nggip.iges.or.jp/public/2006gl/pdf/4_Volume4/V4_11_Ch11_N2O&CO2.pdf},
  note = {access: full_text (§11.3 at pp. 11.26--11.30); type: inventory guidelines; cited as: CB1-LIMING [1]}
}
@incollection{hergoualchChapter11N2O2019,
  author = {Hergoualc'h, K. and Akiyama, H. and Bernoux, M. and Chirinda, N. and del Prado, A. and Kasimir, {\AA}. and MacDonald, J.D. and Ogle, S.M. and Regina, K. and van der Weerden, T.J.},
  title = {Chapter 11: N₂O Emissions from Managed Soils, and CO₂ Emissions from Lime and Urea Application},
  booktitle = {2019 Refinement to the 2006 IPCC Guidelines for National Greenhouse Gas Inventories, Volume 4: Agriculture, Forestry and Other Land Use},
  publisher = {IPCC, Switzerland},
  year = {2019},
  url = {https://www.ipcc-nggip.iges.or.jp/public/2019rf/pdf/4_Volume4/19R_V4_Ch11_Soils_N2O_CO2.pdf},
  note = {access: full_text (§11.3 at p. 11.27); cited as: CB1-LIMING [2]; incomplete: pages}
}
@incollection{willettStoneCrushed2025,
  author = {Willett, J.C.},
  title = {Stone (Crushed)},
  booktitle = {Mineral Commodity Summaries 2025},
  publisher = {U.S. Geological Survey, Reston, Virginia},
  pages = {166--167},
  year = {2025},
  doi = {10.3133/mcs2025},
  url = {https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-stone-crushed.pdf},
  note = {access: full_text; cited as: CB1-LIMING [3]}
}
@incollection{usLimingCRFSource2022,
  author = {{U.S. Environmental Protection Agency}},
  title = {Liming (CRF Source Category 3G)},
  booktitle = {Inventory of U.S. Greenhouse Gas Emissions and Sinks: 1990--2020, Chapter 5: Agriculture},
  publisher = {U.S. EPA, Washington, DC},
  pages = {5-46--5-48},
  year = {2022},
  url = {https://www.epa.gov/system/files/documents/2022-04/us-ghg-inventory-2022-chapter-5-agriculture.pdf},
  note = {access: full_text (Chapter 5 §5.5); type: national inventory; cited as: CB1-LIMING [4]}
}
@article{westContributionAgriculturalLime2005,
  author = {West, T.O. and McBride, A.C.},
  title = {The contribution of agricultural lime to carbon dioxide emissions in the United States: dissolution, transport, and net emissions},
  journal = {Agriculture, Ecosystems and Environment},
  volume = {108},
  number = {2},
  pages = {145--154},
  year = {2005},
  doi = {10.1016/j.agee.2005.01.002},
  note = {access: full_text; cited as: CB1-LIMING [5]}
}
@article{hamiltonEvidenceCarbonSequestration2007,
  author = {Hamilton, S.K. and Kurzman, A.L. and Arango, C. and Jin, L. and Robertson, G.P.},
  title = {Evidence for carbon sequestration by agricultural liming},
  journal = {Global Biogeochemical Cycles},
  volume = {21},
  number = {2},
  pages = {GB2021},
  year = {2007},
  doi = {10.1029/2006GB002738},
  note = {access: full_text; cited as: CB1-LIMING [6]}
}
@article{gouldingSoilAcidificationImportance2016,
  author = {Goulding, K.W.T.},
  title = {Soil acidification and the importance of liming agricultural soils with particular reference to the United Kingdom},
  journal = {Soil Use and Management},
  volume = {32},
  number = {3},
  pages = {390--399},
  year = {2016},
  doi = {10.1111/sum.12270},
  note = {access: full_text; cited as: CB1-LIMING [7]}
}
@article{oumerAgriculturalLimeValue2023,
  author = {Oumer, A.M. and Diro, S. and Taye, G. and Mamo, T. and Jaleta, M.},
  title = {Agricultural lime value chain efficiency for reducing soil acidity in Ethiopia},
  journal = {Soil Security},
  volume = {11},
  pages = {100092},
  year = {2023},
  doi = {10.1016/j.soisec.2023.100092},
  note = {access: full_text; cited as: CB1-LIMING [8]}
}
@article{beerlingPotentialLargescaleCO22020,
  author = {Beerling, D.J. and Kantzas, E.P. and Lomas, M.R. and Wade, P. and Eufrasio, R.M. and Renforth, P. and Sarkar, B. and Andrews, M.G. and James, R.H. and Pearce, C.R. and Mercure, J.-F. and Pollitt, H. and Holden, P.B. and Edwards, N.R. and Khanna, M. and Koh, L. and Quegan, S. and Pidgeon, N.F. and Janssens, I.A. and Hansen, J. and Banwart, S.A.},
  title = {Potential for large-scale CO₂ removal via enhanced rock weathering with croplands},
  journal = {Nature},
  volume = {583},
  number = {7815},
  pages = {242--248},
  year = {2020},
  doi = {10.1038/s41586-020-2448-9},
  note = {access: full_text (main text and Methods); cited as: CB1-LIMING [9]}
}
@misc{beerlingTransformingUS2023,
  author = {Beerling, D.J. and Kantzas, E.P. and Lomas, M.R. and Taylor, L.L. and Zhang, S. and Kanzaki, Y. and Eufrasio, R.M. and Renforth, P. and Mercure, J.-F. and Pollitt, H. and Holden, P.B. and Edwards, N.R. and Koh, L. and Epihov, D.Z. and Wolf, A. and Hansen, J.E. and Banwart, S.A. and Pidgeon, N.F. and Reinhard, C.T. and Planavsky, N.J. and Val Martin, M.},
  title = {Transforming U.S. agriculture with crushed rock for CO₂ sequestration and increased production},
  year = {2023},
  eprint = {2308.04302},
  url = {https://arxiv.org/abs/2308.04302},
  note = {access: full_text (arXiv preprint Methods); type: preprint; cited as: CB1-LIMING [10], first of two works}
}
@article{beerlingTransformingUSAgriculture2025,
  author = {Beerling, D.J. and others},
  title = {Transforming US agriculture for carbon removal with enhanced weathering},
  journal = {Nature},
  volume = {638},
  number = {8050},
  pages = {425--434},
  year = {2025},
  doi = {10.1038/s41586-024-08429-2},
  note = {access: not_obtained ("I did not verify them against the published version"); not cited (named as the published revised form of the preprint); cited as: CB1-LIMING [10], second of two works; incomplete: author}
}
@article{wangPotentialBenefitsLiming2021,
  author = {Wang, Y. and Yao, Z. and Zhan, Y. and Zheng, X. and Zhou, M. and Yan, G. and Wang, L. and Werner, C. and Butterbach-Bahl, K.},
  title = {Potential benefits of liming to acid soils on climate change mitigation and food security},
  journal = {Global Change Biology},
  volume = {27},
  number = {12},
  pages = {2807--2821},
  year = {2021},
  doi = {10.1111/gcb.15607},
  note = {access: abstract_only (abstract or structured summary only); cited as: CB1-LIMING [11]}
}
@article{choEvaluationCarbonDioxide2019,
  author = {Cho, S.R. and Jeong, S.T. and Kim, G.Y. and Lee, J.G. and Kim, P.J. and Kim, G.W.},
  title = {Evaluation of the carbon dioxide (CO₂) emission factor from lime applied in temperate upland soil},
  journal = {Geoderma},
  volume = {337},
  pages = {742--748},
  year = {2019},
  doi = {10.1016/j.geoderma.2018.10.007},
  note = {access: abstract_only (abstract or structured summary only); cited as: CB1-LIMING [12]}
}
@article{roussetSurprisingMinimisationCO22024,
  author = {Rousset, C. and Br{\'e}fort, H. and Frederico Fonseca, R. and Guyerdet, G. and Bizouard, F. and Arkoun, M. and H{\'e}nault, C.},
  title = {Surprising minimisation of CO₂ emissions from a sandy loam soil over a rye growing period achieved by liming (CaCO₃)},
  journal = {Science of the Total Environment},
  volume = {953},
  pages = {175973},
  year = {2024},
  doi = {10.1016/j.scitotenv.2024.175973},
  note = {access: abstract_only (abstract or structured summary only); cited as: CB1-LIMING [13]}
}
@article{silvaSoilAcidityRemediation2025,
  author = {Silva, J.V. and Aramburu-Merlos, F. and Baudron, F. and Gameda, S. and Sida, T.S. and Ruganzu, V. and Meliyo, J. and Jaleta, M. and Chamberlin, J. and Hijmans, R.J.},
  title = {Soil acidity remediation in sub-Saharan Africa requires targeted investments},
  journal = {Nature Food},
  volume = {6},
  number = {8},
  pages = {799--808},
  year = {2025},
  doi = {10.1038/s43016-025-01194-z},
  note = {access: abstract_only (abstract or structured summary only); cited as: CB1-LIMING [14]}
}
@article{hollandLimingImpactsSoils2018,
  author = {Holland, J.E. and Bennett, A.E. and Newton, A.C. and White, P.J. and McKenzie, B.M. and George, T.S. and Pakeman, R.J. and Bailey, J.S. and Fornara, D.A. and Hayes, R.C.},
  title = {Liming impacts on soils, crops and biodiversity in the UK: A review},
  journal = {Science of the Total Environment},
  volume = {610--611},
  pages = {316--332},
  year = {2018},
  doi = {10.1016/j.scitotenv.2017.08.020},
  note = {access: abstract_only (abstract or structured summary only); type: review; cited as: CB1-LIMING [15]}
}
@article{aramburumerlosEstimatingLimeRequirements2023,
  author = {Aramburu Merlos, F. and Silva, J.V. and Baudron, F. and Hijmans, R.J.},
  title = {Estimating lime requirements for tropical soils: Model comparison and development},
  journal = {Geoderma},
  volume = {432},
  pages = {116421},
  year = {2023},
  doi = {10.1016/j.geoderma.2023.116421},
  note = {access: full_text ("I read the full text but used only its framing"); conflict: listed under "Read as abstract or structured summary only"; cited as: CB1-LIMING [16]}
}
@article{liGeospatialAssessmentCost2024,
  author = {Li, Z. and Planavsky, N.J. and Reinhard, C.T.},
  title = {Geospatial assessment of the cost and energy demand of feedstock grinding for enhanced rock weathering in the coterminous United States},
  journal = {Frontiers in Climate},
  volume = {6},
  pages = {1380651},
  year = {2024},
  doi = {10.3389/fclim.2024.1380651},
  note = {access: full_text ("numbers came from an automated extraction of the full article rather than a line-by-line read"); conflict: listed under "Read as abstract or structured summary only"; cited as: CB1-LIMING [17]}
}
@article{westSynthesisCarbonSequestration2002,
  author = {West, T.O. and Marland, G.},
  title = {A synthesis of carbon sequestration, carbon emissions, and net carbon flux in agriculture: comparing tillage practices in the United States},
  journal = {Agriculture, Ecosystems and Environment},
  volume = {91},
  number = {1--3},
  pages = {217--232},
  year = {2002},
  doi = {10.1016/S0167-8809(01)00233-X},
  note = {access: secondary (via West and McBride 2005; "I did not read the original"); cited as: CB1-LIMING [18]}
}
@article{gibbonsSustainableNutrientManagement2014,
  author = {Gibbons, J.M. and Williamson, J.C. and Williams, A.P. and Withers, P.J.A. and Hockley, N. and Harris, I.M. and Hughes, J.W. and Taylor, R.L. and Jones, D.L. and Healey, J.R.},
  title = {Sustainable nutrient management at field, farm and regional level: soil testing, nutrient budgets and the trade-off between lime application and greenhouse gas emissions},
  journal = {Agriculture, Ecosystems and Environment},
  volume = {188},
  pages = {48--56},
  year = {2014},
  doi = {10.1016/j.agee.2014.02.016},
  note = {access: secondary (via Goulding 2016; "I did not read the original"); cited as: CB1-LIMING [19]}
}
@article{paradeloNetEffectLiming2015,
  author = {Paradelo, R. and Virto, I. and Chenu, C.},
  title = {Net effect of liming on soil organic carbon stocks: A review},
  journal = {Agriculture, Ecosystems and Environment},
  volume = {202},
  pages = {98--107},
  year = {2015},
  doi = {10.1016/j.agee.2015.01.005},
  note = {access: secondary (via Goulding 2016; "I did not read the original"); type: review; cited as: CB1-LIMING [20]}
}
@article{biasiDirectExperimentalEvidence2008,
  author = {Biasi, C. and Lind, S.E. and Pekkarinen, N.M. and Huttunen, J.T. and Shurpali, N.J. and Hyv{\"o}nen, N.P. and Repo, M.E. and Martikainen, P.J.},
  title = {Direct experimental evidence for the contribution of lime to CO₂ release from managed peat soil},
  journal = {Soil Biology and Biochemistry},
  volume = {40},
  number = {10},
  pages = {2660--2669},
  year = {2008},
  doi = {10.1016/j.soilbio.2008.07.011},
  note = {access: not_obtained (title only: "I read only the title"; abstract withheld by the publisher); cited as: CB1-LIMING [21]}
}
@misc{foodClimateChangeAgrifood2025,
  author = {{Food and Agriculture Organization of the United Nations}},
  title = {Climate Change: Agrifood systems emissions — Emissions from Crops},
  howpublished = {FAOSTAT, FAO, Rome (domain description and dataset inventory)},
  year = {2025},
  url = {https://bulks-faostat.fao.org/production/datasets_E.json},
  note = {access: full_text (consulted 18 September 2026 to confirm that no FAOSTAT climate-change domain covers liming); type: database; cited as: CB1-LIMING [22]}
}
@article{hartmannEnhancedChemicalWeathering2013,
  author = {Hartmann, Jens and West, A. Joshua and Renforth, Phil and K{\"o}hler, Peter and De La Rocha, Christina L. and Wolf-Gladrow, Dieter A. and D{\"u}rr, Hans H. and Scheffran, J{\"u}rgen},
  title = {Enhanced chemical weathering as a geoengineering strategy to reduce atmospheric carbon dioxide, supply nutrients, and mitigate ocean acidification},
  journal = {Reviews of Geophysics},
  volume = {51},
  number = {2},
  pages = {113--149},
  year = {2013},
  doi = {10.1002/rog.20004},
  note = {background; checked on Crossref 2026-10-21}
}
```
