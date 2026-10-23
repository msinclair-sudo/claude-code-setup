---
type: knowledge
title: Agricultural liming rates, supply, energy and carbon dioxide
inputs:
  - CB1-LIMING: PhD/Proposal/Research/Results/Agricultural Liming - Rates, Supply, Energy Cost and Emitted Carbon Dioxide.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-23
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
| CB1-LIMING | [[Agricultural Liming - Rates, Supply, Energy Cost and Emitted Carbon Dioxide]] | no (the note says none ran) | numbered | no | no | fallback (answers and critique; the note has no labelled citations) |

## Concepts

### liming: Agricultural liming
needs: none

- **liming.bg1** Lime application neutralises soil acidity and raises soil pH; the most common source of lime for agricultural use is ground limestone.
  kind: background · ref: rasnakeLimingAcidSoils1993 · check: the URL resolves (University of Kentucky publication AGR-19, issued 1961, revised 1993); both statements are in its text ("Lime application neutralizes soil acidity, raises soil pH and adds calcium and magnesium to the soil"; "The most common source of lime for agricultural use is ground limestone")

### enhanced-weathering: Enhanced rock weathering
needs: none

- **enhanced-weathering.bg1** Enhanced weathering is the application of finely ground minerals over the land surface to remove CO₂ from the atmosphere.
  kind: background · ref: hartmannEnhancedChemicalWeathering2013 · check: DOI 10.1002/rog.20004 resolves on Crossref; stated in the abstract

### application-rate: Lime requirement and application rates
needs: liming

- **application-rate.1** Lime rates are set by a lime requirement calculation, not by a standard dose, and the spread across soil types is wide enough that any single number misleads.
  conf: not stated · class: not stated · holds: the review's general statement on rates across soil types · src: none (the reviewer's synthesis) · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0017
- **application-rate.2** To lift an arable soil (20 cm depth) from pH 5.0 to the recommended 6.5, the UK recommendation table (the Fertiliser Manual, RB209, as reproduced by Goulding) specifies 10 t/ha on sands, 12 on sandy and silt loams, 14 on clay loams and clays, 14 on organic soils and 16 on peaty soils.
  conf: not stated · class: not stated · holds: UK arable soils, 20 cm depth, from pH 5.0 to the recommended 6.5; the review calls the table the clearest published grid it found · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0018..0019
- **application-rate.3** From pH 6.0 the same UK table gives 4, 5, 6 and 4 t/ha for arable soils.
  conf: not stated · class: not stated · holds: UK arable soils (20 cm depth) starting at pH 6.0, target 6.5, in the RB209 table as reproduced by Goulding; the values are given as listed, without soil types · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0018..0020
- **application-rate.4** Grassland, with a lower target of pH 6.0, takes roughly half the arable rates: 5, 6, 7, 7 and 6 t/ha from pH 5.0, and nothing at pH 6.0.
  conf: not stated · class: not stated · holds: UK grassland, target pH 6.0, in the RB209 table as reproduced by Goulding · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0018, CB1-LIMING:B-0021
- **application-rate.5** The lime requirement is non-linear: on the Park Grass Experiment fewer than 5 t/ha of lime raised soil pH from about 6 to 7 over five years, but nearer 20 t/ha were needed to go from 5 to 7.
  conf: not stated · class: not stated · holds: the Park Grass Experiment, as reported by Goulding · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0022..0023
- **application-rate.6** The Rothamsted and Woburn long-term liming experiments used 5, 10 and 20 t/ha and 4.6, 10.9 and 17.3 t/ha respectively, with repeat applications marked on the pH time series.
  conf: not stated · class: not stated · holds: the Rothamsted and Woburn long-term liming experiments, as reported by Goulding · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0024
- **application-rate.7** The lime requirement grid for temperate soils, and its strong non-linearity with starting pH and buffering capacity, are well established.
  conf: not stated · class: not stated · rating: "Well established" · holds: temperate soils; the review's assessment, citing Goulding · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §What is well established · from: CB1-LIMING:B-0130
- **application-rate.8** Precision variable-rate application of pelletised lime on the North Wyke Farm Platform ran at up to 1 t/ha; across four fields with starting pH 5.5–5.8, the recommendation reached the pH 6.0 target only in the field that started at 5.8, and fell 0.2 units short in the other three.
  conf: not stated · class: not stated · holds: North Wyke Farm Platform, four fields, starting pH 5.5–5.8, target pH 6.0, as reported by Goulding · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0030
- **application-rate.9** Recommendations do not reliably deliver the correction they promise.
  conf: not stated · class: not stated · holds: drawn by the review from the North Wyke Farm Platform result (four fields, pelletised lime at up to 1 t/ha, target pH 6.0) · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0030..0031
- **application-rate.10** For tropical soils the target of liming is usually acidity saturation or base saturation rather than pH.
  conf: not stated · class: not stated · holds: tropical soils · src: aramburumerlosEstimatingLimeRequirements2023 (read the full text but used only its framing) · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0034, CB1-LIMING:B-0014
- **application-rate.11** Aramburu Merlos et al. show that the estimated lime rate depends heavily on which target the model uses: "large differences in the estimated lime rates depending on the target soil chemical property" across 303 African soil samples.
  conf: not stated · class: not stated · holds: tropical soils; model comparison across 303 African soil samples · src: aramburumerlosEstimatingLimeRequirements2023 (read the full text but used only its framing) · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0034, CB1-LIMING:B-0014
- **application-rate.12** Aramburu Merlos et al.'s compiled incubation datasets span lime requirements of 0.2–23.9 cmolc/kg, which at a bulk density of 1 g/cm³ and 20 cm depth converts one-for-one to t CaCO₃/ha: a two-order-of-magnitude range, which the review calls the honest answer to "what is a typical rate".
  conf: not stated · class: deriv (note: "converts one-for-one to t CaCO₃/ha") · holds: compiled incubation datasets for tropical soils; the conversion to t CaCO₃/ha assumes a bulk density of 1 g/cm³ and 20 cm depth · src: aramburumerlosEstimatingLimeRequirements2023 (read the full text but used only its framing) · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0034..0036, CB1-LIMING:B-0014
- **application-rate.13** The Ethiopian value-chain study reports that about 20 quintals (2 t) of lime per hectare is the average requirement.
  conf: not stated · class: not stated · holds: Ethiopia · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0027

### n-acidification: Acidity from nitrogen and the lime that balances it
needs: liming

- **n-acidification.1** About 3.6 kg CaCO₃ balances the Ca²⁺ lost with nitrate per kg of ammonium-N nitrified: roughly 180 kg CaCO₃ per 50 kg NH₄-N.
  conf: not stated · class: not stated · holds: as reported by Goulding · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0032
- **n-acidification.2** Neutralising the acid actually formed by nitrifying 50 kg NH₄-N requires about 360 kg CaCO₃, and Goulding notes that this figure matches field observations of lime requirement better than the figure for balancing the Ca²⁺ lost with nitrate.
  conf: not stated · class: not stated · holds: as reported by Goulding · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0032..0033

### application-frequency: How often lime is reapplied
needs: application-rate

- **application-frequency.1** West and McBride adopt "a conservative application rate of 5 Mg crushed rock per hectare every 5 years," annualised to about 1 Mg/ha/yr, for their US calculation.
  conf: not stated · class: not stated · holds: an assumption adopted for their US calculation · src: westContributionAgriculturalLime2005 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0026
- **application-frequency.2** The Ethiopian value-chain study reports that once the full recommended rate of lime is applied "it can benefit farmers for up to five years".
  conf: not stated · class: not stated · holds: Ethiopia · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0027
- **application-frequency.3** Reapplication frequency is poorly constrained: it is less well pinned down than rate, and appears mostly as a five-year working assumption rather than a measured or surveyed quantity.
  conf: unclear (note: "Poorly constrained") · class: not stated · holds: the review's assessment of the sources it read · src: westContributionAgriculturalLime2005, oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Application rates, §What is well established · from: CB1-LIMING:B-0025, CB1-LIMING:B-0134..0135
- **application-frequency.4** A five-year interval is common across two very different systems: West and McBride's US calculation and the Ethiopian value-chain study.
  conf: not stated · class: not stated · holds: the two sources the review found; not a survey · src: westContributionAgriculturalLime2005, oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0026..0028
- **application-frequency.5** The review found no systematic survey establishing a five-year reapplication interval.
  conf: not stated · class: search (note: "I found no systematic survey establishing it") · search: searched, not found (note: "I found no systematic survey establishing it") · holds: the literature the review reached · src: none (a search result of the review) · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0028

### consumption: How much agricultural lime is used
needs: liming

- **consumption.1** The US EPA inventory reports minerals applied to soils of 9.9 Mt limestone and 1.0 Mt dolomite in 2020, down from 19.0 and 2.4 Mt in 1990.
  conf: not stated · class: not stated · holds: US, 1990 and 2020, EPA inventory · src: usLimingCRFSource2022 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0037
- **consumption.2** USGS reports that about 1% of the 1.5 billion tonnes of crushed stone produced in the US in 2024 went to agricultural uses; earlier editions put the share at 2%.
  conf: not stated · class: not stated · holds: US crushed stone production, 2024 · src: willettStoneCrushed2025 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0038
- **consumption.3** About 1% of the 1.5 billion tonnes of US crushed stone is arithmetically about 15 Mt of agricultural use.
  conf: not stated · class: deriv (note: "arithmetically about 15 Mt") · holds: the review's arithmetic on the USGS share for 2024 · src: willettStoneCrushed2025 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0038
- **consumption.4** West and McBride, reviewing the historical series, concluded that EPA's then-current 20 Tg figure understated the real total and that "30 Tg may better represent the annual U.S. consumption of aglime".
  conf: not stated · class: not stated · holds: US · src: westContributionAgriculturalLime2005 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0039
- **consumption.5** West and McBride note that aglime comprises 3–5% of reported crushed limestone and dolomite usage.
  conf: not stated · class: not stated · holds: US reported usage, as reviewed by West and McBride · src: westContributionAgriculturalLime2005 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0039
- **consumption.6** West and McBride note that an apparent 10 Tg decline in the historical series between 1980 and 2000 coincided with a change in data collection and reporting.
  conf: not stated · class: not stated · holds: US, 1980–2000 · src: westContributionAgriculturalLime2005 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0039
- **consumption.7** US consumption figures disagree: the US number is somewhere between about 11 and 30 Mt/yr, depending on whose accounting is taken, and estimates differ by up to threefold; the review calls this a genuine unresolved disagreement and does not resolve it.
  conf: cont (note: "Consumption figures disagree with each other inside a single country") · class: not stated · holds: US; the range spans the EPA inventory, the USGS share and West and McBride's estimate · src: usLimingCRFSource2022, willettStoneCrushed2025, westContributionAgriculturalLime2005 · trail: CB1-LIMING §Consumption, §What is well established · from: CB1-LIMING:B-0037..0041, CB1-LIMING:B-0137
- **consumption.8** The discrepancy between the US consumption figures is a reporting artefact, not a physical one.
  conf: not stated · class: not stated · holds: US; West and McBride tie an apparent decline to a change in data collection and reporting · src: none (the reviewer's synthesis) · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0039..0040
- **consumption.9** In the UK, annual amounts of lime applied "have declined from c 6000–7000 kt product/year to c 2500 kt product/year today," against a calculated average annual UK lime loss of 4,250,000 t CaCO₃.
  conf: not stated · class: not stated · holds: UK; application in kt product per year, loss in t CaCO₃ per year · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Consumption, §Verdict on the scarcity claim · from: CB1-LIMING:B-0042, CB1-LIMING:A-011
- **consumption.10** The UK is applying less than 60% of what its soils lose.
  conf: not stated · class: not stated · holds: UK; the review's comparison of about 2500 kt product/year applied with a calculated loss of 4,250,000 t CaCO₃ a year · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0042..0043
- **consumption.11** There is no authoritative global consumption figure in the peer-reviewed or inventory literature the review could reach: FAOSTAT's Emissions from Crops domain covers crop residues, residue burning, rice cultivation and nitrogen fertiliser application, and no FAOSTAT climate-change domain covers liming.
  conf: not stated · class: search (note: "I checked FAOSTAT directly") · search: searched, not found (note: "I checked FAOSTAT directly") · holds: the peer-reviewed and inventory literature the review could reach, and FAOSTAT · src: foodClimateChangeAgrifood2025 · trail: CB1-LIMING §Consumption, §What is well established · from: CB1-LIMING:B-0047, CB1-LIMING:B-0138..0139
- **consumption.12** The review found no peer-reviewed global total that was not a counterfactual: the nearest thing to a global-scale quantification is Wang et al.'s estimate for a world in which all acid agricultural soils were limed periodically, which bounds the scale of a fully limed world and does not describe current practice.
  conf: not stated · class: search (note: "I found no peer-reviewed global total that was not a counterfactual") · search: searched, not found (note: "I found no peer-reviewed global total that was not a counterfactual") · holds: global; Wang et al.'s estimate assumes all acid agricultural soils worldwide were limed periodically · src: wangPotentialBenefitsLiming2021 (abstract or structured summary only) · trail: CB1-LIMING §Consumption, §What is well established · from: CB1-LIMING:B-0051..0053, CB1-LIMING:B-0139, CB1-LIMING:B-0014

### resource-base: The limestone and crushed-stone resource
needs: liming

- **resource-base.1** USGS, in the 2025 Mineral Commodity Summaries chapter on crushed stone, states under World Resources: "Stone resources are plentiful throughout the world."
  conf: not stated · class: not stated · rating: "Well established" · holds: crushed stone worldwide; USGS, 2025 · src: willettStoneCrushed2025 · trail: CB1-LIMING §Consumption, §Verdict on the scarcity claim, §What is well established · from: CB1-LIMING:B-0054, CB1-LIMING:A-002, CB1-LIMING:A-007, CB1-LIMING:B-0130, CB1-LIMING:B-0133
- **resource-base.2** The USGS reserves entry for crushed stone reads "Adequate, except where special types are needed or where local shortages exist."
  conf: not stated · class: not stated · rating: "Well established" · holds: crushed stone; USGS, 2025 · src: willettStoneCrushed2025 · trail: CB1-LIMING §Consumption, §Verdict on the scarcity claim, §What is well established · from: CB1-LIMING:B-0055, CB1-LIMING:A-002, CB1-LIMING:A-007, CB1-LIMING:B-0130, CB1-LIMING:B-0133
- **resource-base.3** USGS records that about 70% of US crushed stone production in 2024 was limestone and dolomite, from roughly 3,500 quarries operated by about 1,400 companies across 50 states.
  conf: not stated · class: not stated · holds: US, 2024 · src: willettStoneCrushed2025 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0056
- **resource-base.4** USGS states that "the supply of high-purity limestone and dolomite suitable for specialty uses is limited in many geographic areas".
  conf: not stated · class: not stated · holds: high-purity limestone and dolomite for specialty uses · src: willettStoneCrushed2025 · trail: CB1-LIMING §Consumption, §Verdict on the scarcity claim · from: CB1-LIMING:B-0057, CB1-LIMING:A-017
- **resource-base.5** The USGS limitation is scoped to high-purity specialty grades and does not extend to coarse agricultural lime, a low-specification bulk product for which purity requirements are low.
  conf: not stated · class: not stated · holds: agricultural lime as against high-purity specialty grades · src: willettStoneCrushed2025 · trail: CB1-LIMING §Consumption, §Verdict on the scarcity claim · from: CB1-LIMING:A-004, CB1-LIMING:A-018..019, CB1-LIMING:B-0058..0059
- **resource-base.6** Nothing in the USGS text, and no source the review read, extends the specialty-grade limitation to agricultural lime.
  conf: not stated · class: search (note: "no source I read extends the specialty-grade limitation to it") · search: searched, not found (note: "no source I read extends the specialty-grade limitation to it") · holds: the USGS chapter and the sources the review read · src: willettStoneCrushed2025 · trail: CB1-LIMING §Consumption, §Verdict on the scarcity claim · from: CB1-LIMING:A-019, CB1-LIMING:B-0059
- **resource-base.7** USGS flags localised shortages near urban and industrialised areas, driven by zoning and land-development competition, which push new quarries away from population centres and raise delivered prices.
  conf: not stated · class: not stated · holds: urban and industrialised areas · src: willettStoneCrushed2025 · trail: CB1-LIMING §Consumption, §Verdict on the scarcity claim · from: CB1-LIMING:B-0060, CB1-LIMING:A-026
- **resource-base.8** USGS presents the urban shortages as a price driver, not a reserve limitation: they are planning and land-use pressure, a siting and logistics problem, not a depletion problem.
  conf: not stated · class: not stated · holds: urban and industrialised areas · src: willettStoneCrushed2025 · trail: CB1-LIMING §Consumption, §Verdict on the scarcity claim · from: CB1-LIMING:B-0060, CB1-LIMING:A-026
- **resource-base.9** Oumer et al.'s SWOT tables list "Huge core-limestone deposits in all production areas" as an opportunity for both public and private ag-lime producers.
  conf: not stated · class: not stated · holds: Ethiopian ag-lime production areas · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Consumption, §Verdict on the scarcity claim · from: CB1-LIMING:B-0063, CB1-LIMING:A-013
- **resource-base.10** Oumer et al. state that "producing a large quantity of ag-lime should not be an issue in Ethiopia".
  conf: not stated · class: not stated · holds: Ethiopia · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Consumption, §Verdict on the scarcity claim · from: CB1-LIMING:B-0064, CB1-LIMING:A-013

### lime-supply-chain: Producing and delivering lime: capacity, logistics and delivered cost
needs: liming, enhanced-weathering

- **lime-supply-chain.1** Oumer et al. surveyed public and private ag-lime plants in Ethiopia and found all of them running far below capacity: Guder at 12% of its 46,800 t/yr capacity, Dejen at 19%, Kella at 29%, Dashen at 2% of 144,000 t/yr, and Muger cement at under 1% of 400,000 t/yr, "due to a lack of ag-lime demand".
  conf: not stated · class: not stated · holds: Ethiopian public and private ag-lime plants · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0061..0062
- **lime-supply-chain.2** Ethiopian ag-lime plants ran at 1–29% of installed capacity for want of demand.
  conf: not stated · class: not stated · holds: the review's summary of the plants Oumer et al. surveyed, whose plant-by-plant figures run from under 1% (Muger cement) to 29% (Kella) · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Verdict on the scarcity claim · from: CB1-LIMING:A-013, CB1-LIMING:B-0062
- **lime-supply-chain.3** The binding constraints Oumer et al. identify for Ethiopian ag-lime are demand creation, warehousing, power interruptions, procurement processes, transport, and the absence of a quality standard beyond calcium carbonate equivalence.
  conf: not stated · class: not stated · holds: the Ethiopian ag-lime value chain · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0061, CB1-LIMING:B-0065
- **lime-supply-chain.4** In Ethiopia a private supplier won a bid to supply core limestone at 47 ETB per cubic metre, equivalent to 5.5 ETB per quintal.
  conf: not stated · class: not stated · holds: Ethiopia · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0083
- **lime-supply-chain.5** The average transport cost of finished ag-lime to kebeles was 163 ETB/Qt in Oromia, SNNP and Sidama, and 60 ETB/Qt in east Gojjam, with unloading at 10 ETB/Qt and transporter margins of 27–57 ETB/Qt; distance-based rates ran 0.30–0.75 ETB/Qt/km.
  conf: not stated · class: not stated · holds: Ethiopia: Oromia, SNNP, Sidama and east Gojjam · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0083..0084
- **lime-supply-chain.6** The delivered cost of Ethiopian ag-lime is dominated by moving the material, not by obtaining it: roughly 5.5 ETB/Qt at the quarry against 60–163 ETB/Qt to transport it to a rural distribution point, so the rock at the quarry costs roughly an order of magnitude less than moving it. The review calls this the clearest published cost breakdown showing transport dominance.
  conf: not stated · class: not stated · holds: Ethiopia · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Energy and transport, §Verdict on the scarcity claim · from: CB1-LIMING:A-014, CB1-LIMING:B-0083, CB1-LIMING:B-0085
- **lime-supply-chain.7** At the Ethiopian processing plants labour dominated internal costs: 55% for Dejen, with packaging and labelling at 16%.
  conf: not stated · class: not stated · holds: Ethiopian ag-lime processing plants (Dejen) · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0083, CB1-LIMING:B-0086
- **lime-supply-chain.8** Farmers named "the bulky nature of lime, the difficulty of transportation to farm plots (lack of simple machines), labor-intensive nature of the lime application, untimely (late) supply" as the barriers to adopting lime.
  conf: not stated · class: not stated · holds: farmers in the Ethiopian value-chain study · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0083, CB1-LIMING:B-0087
- **lime-supply-chain.9** For the US or Europe the review found no comparable delivered-cost breakdown, only trade-press and forum material with no verifiable method, and it reports no numbers from that material.
  conf: not stated · class: search (note: "I searched for a comparable delivered-cost breakdown for the US or Europe") · search: searched, not found (note: "I searched for a comparable delivered-cost breakdown for the US or Europe") · holds: US and Europe · src: none (a search result of the review) · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0089..0090
- **lime-supply-chain.10** Carbonate lime is bulky, and transport dominates its delivered cost.
  conf: not stated · class: not stated · holds: what the review says the literature supports · src: none (the review's verdict) · trail: CB1-LIMING §Verdict · from: CB1-LIMING:A-005, CB1-LIMING:A-029
- **lime-supply-chain.11** Beerling et al. state that logistical infrastructure to spread rock dust on croplands "already exists due to the common need to apply crushed limestone to reverse soil acidification from intensive cropping".
  conf: not stated · class: not stated · holds: croplands · src: beerlingPotentialLargescaleCO22020 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0066
- **lime-supply-chain.12** Beerling et al.'s argument for the feasibility of enhanced weathering at gigatonne scale rests in part on the existing scale and maturity of the crushed-rock industry.
  conf: not stated · class: not stated · holds: enhanced weathering at gigatonne scale · src: beerlingPotentialLargescaleCO22020 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0066..0067
- **lime-supply-chain.13** The Beerling et al. preprint gives 2020 US transport costs of $0.07/t-km by road and $0.028/t-km by rail.
  conf: not stated · class: not stated · holds: US, 2020 values · src: beerlingTransformingUS2023 (preprint Methods; not verified against the published version) · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0080, CB1-LIMING:R-0035
- **lime-supply-chain.14** The Beerling et al. preprint gives a spreading cost of $5.5 per ton "based on the 2020 values for lime spreading in the United States".
  conf: not stated · class: not stated · holds: US, 2020 values · src: beerlingTransformingUS2023 (preprint Methods; not verified against the published version) · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0080, CB1-LIMING:R-0035
- **lime-supply-chain.15** In the Beerling et al. preprint the modelled truck share of transport falls from 0.96 at 50 km to 0.31 at 1,750 km as rail takes over.
  conf: not stated · class: model (note: "Their modelled truck share") · holds: the preprint's model, US · src: beerlingTransformingUS2023 (preprint Methods; not verified against the published version) · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0080..0081, CB1-LIMING:R-0035
- **lime-supply-chain.16** The review did not find a published measured distribution of haul distances for agricultural lime specifically; the enhanced-weathering papers compute distances from network analysis for basalt sources, which is a different geography.
  conf: not stated · class: search (note: "I did not find a published measured distribution of haul distances") · search: searched, not found (note: "I did not find a published measured distribution of haul distances") · holds: agricultural lime; the enhanced-weathering distances are for basalt sources · src: none (a search result of the review) · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0082

### liming-shortfall: Where liming falls short of need, and why
needs: application-rate, lime-supply-chain

- **liming-shortfall.1** Where liming falls short of agronomic need, the documented causes are demand, price and transport logistics, not the rock.
  conf: not stated · class: not stated · holds: the review's verdict across the UK and Ethiopian evidence · src: none (the review's verdict) · trail: CB1-LIMING §Verdict · from: CB1-LIMING:A-003, CB1-LIMING:A-010..011, CB1-LIMING:A-013
- **liming-shortfall.2** Goulding attributes the UK decline in lime application to farm economics, not availability; the stated cause is economic: "although a short-term saving, reducing or omitting the application of lime to correct acidity risks significant economic loss".
  conf: not stated · class: not stated · holds: UK · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Consumption, §Verdict on the scarcity claim · from: CB1-LIMING:B-0044, CB1-LIMING:A-011
- **liming-shortfall.3** Of more than 200,000 UK soil analyses collated for 2013/14, about 40% of arable soils were below the recommended pH 6.5 and 57% of grassland soils below pH 6.0.
  conf: not stated · class: not stated · holds: UK soil tests, 2013/14 · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0042, CB1-LIMING:B-0044
- **liming-shortfall.4** Under-liming in the UK is a demand-side and price-side phenomenon; nothing in Goulding attributes it to lime being unavailable.
  conf: not stated · class: not stated · holds: UK · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0045..0046
- **liming-shortfall.5** Lime is genuinely hard to obtain in parts of sub-Saharan Africa: Silva et al. state that "lime is not widely available in the region".
  conf: not stated · class: not stated · limit: access (note: "note where the review itself says it read only an abstract") · holds: sub-Saharan Africa · src: silvaSoilAcidityRemediation2025 (abstract or structured summary only) · trail: CB1-LIMING §Verdict on the scarcity claim · from: CB1-LIMING:A-022, CB1-LIMING:B-0010, CB1-LIMING:B-0014
- **liming-shortfall.6** Silva et al. report crop yield loss to soil acidity on 32.7 Mha, 23% of sub-Saharan Africa's cropland, and a burden of US$6.0 billion.
  conf: not stated · class: not stated · limit: access (note: "note where the review itself says it read only an abstract") · holds: sub-Saharan Africa's cropland · src: silvaSoilAcidityRemediation2025 (abstract or structured summary only) · trail: CB1-LIMING §Verdict on the scarcity claim · from: CB1-LIMING:A-022, CB1-LIMING:B-0010, CB1-LIMING:B-0014
- **liming-shortfall.7** The Ethiopian case study of the sub-Saharan access problem locates the failure in the value chain, not in the deposits: in the region most often described as lime-constrained, the constraint is not the rock.
  conf: not stated · class: not stated · holds: Ethiopia · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Verdict on the scarcity claim · from: CB1-LIMING:A-012, CB1-LIMING:A-022..023
- **liming-shortfall.8** The access constraint in parts of sub-Saharan Africa is a distribution problem, not a resource one: a regional access constraint on a locally abundant mineral, which should not be conflated with a scarcity problem.
  conf: not stated · class: not stated · holds: parts of sub-Saharan Africa; the review's characterisation · src: none (the review's characterisation) · trail: CB1-LIMING §Verdict on the scarcity claim · from: CB1-LIMING:A-004, CB1-LIMING:A-021, CB1-LIMING:A-024
- **liming-shortfall.9** The supply chains of carbonate lime fail badly in some regions.
  conf: not stated · class: not stated · holds: what the review says the literature supports · src: none (the review's verdict) · trail: CB1-LIMING §Verdict on the scarcity claim · from: CB1-LIMING:A-029
- **liming-shortfall.10** None of the adoption barriers Ethiopian farmers named is the rock running out.
  conf: not stated · class: not stated · holds: farmers in the Ethiopian value-chain study · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0083, CB1-LIMING:B-0087..0088

### grinding-energy: Energy to grind rock and lime
needs: liming, enhanced-weathering

- **grinding-energy.1** Energy figures from the enhanced-weathering literature, which grinds rock far finer than agricultural lime, give an upper bound for agricultural lime rather than a like-for-like figure.
  conf: not stated · class: not stated · holds: agricultural lime against enhanced-weathering feedstock · src: none (the reviewer's synthesis) · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0075
- **grinding-energy.2** Li et al., fitting Bond's law from a 300 µm feed, report grinding energy of roughly 9.7 kWh/t to a P80 of 100 µm, 19.4 kWh/t to 50 µm and about 128 kWh/t to 10 µm.
  conf: not stated · class: model (note: "fitting Bond's law from a 300 µm feed") · holds: enhanced-weathering feedstock ground from a 300 µm feed · src: liGeospatialAssessmentCost2024 (numbers from an automated extraction of the full article rather than a line-by-line read) · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0076..0077, CB1-LIMING:B-0014
- **grinding-energy.3** Li et al. give corresponding US grid-electricity costs for grinding of about $0.95, $1.88 and $5.81 per tonne (to 100, 50 and 10 µm) at national average prices.
  conf: not stated · class: not stated · holds: US, national average electricity prices · src: liGeospatialAssessmentCost2024 (numbers from an automated extraction of the full article rather than a line-by-line read) · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0076, CB1-LIMING:B-0014
- **grinding-energy.4** Li et al. give grinding CO₂ of roughly 5–35 kg CO₂/t.
  conf: not stated · class: not stated · holds: enhanced-weathering feedstock grinding · src: liGeospatialAssessmentCost2024 (numbers from an automated extraction of the full article rather than a line-by-line read) · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0076..0077, CB1-LIMING:B-0014
- **grinding-energy.5** Li et al. conclude that "feedstock grinding is potentially the most energy- and emissions-intensive component" of the enhanced-weathering life cycle.
  conf: not stated · class: not stated · holds: the enhanced-weathering life cycle · src: liGeospatialAssessmentCost2024 (numbers from an automated extraction of the full article rather than a line-by-line read) · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0076..0077, CB1-LIMING:B-0014
- **grinding-energy.6** Beerling et al. state that "rock grinding to reduce particle size and maximise CDR is the primary energy consuming operation".
  conf: not stated · class: not stated · holds: rock grinding to maximise CDR · src: beerlingPotentialLargescaleCO22020 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0078
- **grinding-energy.7** Beerling et al. note that industrialised nations already spend up to about 2% of total energy production on rock comminution.
  conf: not stated · class: not stated · holds: industrialised nations · src: beerlingPotentialLargescaleCO22020 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0078
- **grinding-energy.8** Goulding notes that pelletised lime is usually specified at 90% passing a 150 µm sieve, and bulk ground limestone is coarser still.
  conf: not stated · class: not stated · holds: as reported by Goulding · src: gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0079
- **grinding-energy.9** Because agricultural lime is typically specified far coarser than enhanced-weathering feedstock, the low end of the enhanced-weathering grinding range is the relevant one, and grinding energy for agricultural lime should sit at or below about 10 kWh/t.
  conf: not stated · class: not stated · holds: agricultural lime, from the enhanced-weathering grinding range of Li et al. and the coarser lime specification Goulding gives · src: liGeospatialAssessmentCost2024, gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0075..0076, CB1-LIMING:B-0079

### ipcc-liming-method: The IPCC method for CO₂ from liming
needs: liming

- **ipcc-liming-method.bg1** In the IPCC inventory guidelines a tier is a level of methodological complexity: Tier 1 is the basic method, designed to use readily available statistics with the default emission factors provided, Tier 2 is intermediate, and Tier 3 is the most demanding in complexity and data requirements.
  kind: background · ref: rypdalChapter1Introduction2006 · check: the IPCC PDF URL resolves; stated in §1.1 Concepts, p. 1.6, under "Tiers" and "Default data"
- **ipcc-liming-method.1** IPCC (2006) Volume 4 Chapter 11 §11.3 gives Equation 11.12: CO₂–C emission = (M_limestone × EF_limestone) + (M_dolomite × EF_dolomite), with M in tonnes per year and EF in tonnes of C per tonne of material.
  conf: not stated · class: not stated · rating: "Well established" · holds: the IPCC (2006) Tier 1 method · src: dekleinChapter11N2O2006 · trail: CB1-LIMING §Carbon dioxide emitted, §What is well established · from: CB1-LIMING:B-0091, CB1-LIMING:B-0130..0131
- **ipcc-liming-method.2** The Tier 1 method applies an overall emission factor of 0.12 for limestone and 0.13 for dolomite, equivalent to the carbonate carbon contents of the materials (12% for CaCO₃, 13% for CaMg(CO₃)₂).
  conf: not stated · class: deriv (note: "equivalent to carbonate carbon contents of the materials") · rating: "Well established" · holds: the IPCC (2006) Tier 1 defaults · src: dekleinChapter11N2O2006 · trail: CB1-LIMING §Carbon dioxide emitted, §What is well established · from: CB1-LIMING:B-0091..0093, CB1-LIMING:B-0130..0131
- **ipcc-liming-method.3** Multiplied by 44/12, the default factors give 0.44 t CO₂ per tonne of limestone and about 0.477 per tonne of dolomite.
  conf: not stated · class: deriv (note: "Multiplying by 44/12") · holds: the review's conversion of the IPCC (2006) Tier 1 defaults · src: dekleinChapter11N2O2006 · trail: CB1-LIMING §Carbon dioxide emitted · from: CB1-LIMING:B-0092, CB1-LIMING:B-0094
- **ipcc-liming-method.4** Oxides and hydroxides of lime are explicitly excluded from the method, since they contain no inorganic carbon: their CO₂ is produced during manufacture, not after soil application.
  conf: not stated · class: not stated · holds: the IPCC (2006) method · src: dekleinChapter11N2O2006 · trail: CB1-LIMING §Carbon dioxide emitted · from: CB1-LIMING:B-0091, CB1-LIMING:B-0095
- **ipcc-liming-method.5** The IPCC states a one-sided uncertainty of −50% for the default factors, which are a ceiling: "The uncertainty is -50% based on approximations suggesting emissions may be less than half of the maximum value, which is the current factor value (West and McBride, 2005)"; uncertainties cannot exceed the emission factors because these represent the absolute maximum emissions associated with liming.
  conf: not stated · class: not stated · rating: "Well established" · holds: the IPCC (2006) Tier 1 defaults · src: dekleinChapter11N2O2006 · trail: CB1-LIMING §Carbon dioxide emitted, §What is well established · from: CB1-LIMING:B-0096..0097, CB1-LIMING:B-0130..0131
- **ipcc-liming-method.6** The IPCC Tier 2 text repeats that "emissions are likely to be less than assumed using the Tier 1 approach because the amount of CO₂ emitted after liming will depend on site-specific influences and transport of dissolved inorganic C through rivers and lakes to the ocean."
  conf: not stated · class: not stated · holds: the IPCC (2006) Tier 2 text · src: dekleinChapter11N2O2006 · trail: CB1-LIMING §Carbon dioxide emitted · from: CB1-LIMING:B-0098
- **ipcc-liming-method.7** Under the IPCC Tier 3 text, increases in soil inorganic C or dissolved inorganic C from liming do not constitute a net removal of CO₂ from the atmosphere; carbonate-C from liming that is not returned to the atmosphere is considered a net reduction in the emissions associated with liming.
  conf: not stated · class: not stated · holds: the IPCC (2006) Tier 3 accounting rule · src: dekleinChapter11N2O2006 · trail: CB1-LIMING §Carbon dioxide emitted · from: CB1-LIMING:B-0099..0100
- **ipcc-liming-method.8** The 2019 Refinement left the liming defaults unrevised: its section 11.3, CO₂ Emissions from Liming, reads in its entirety "No refinement", so as of the most recent IPCC methodological update the 2006 factors and their −50% uncertainty stand.
  conf: not stated · class: not stated · rating: "Well established" · holds: the 2019 Refinement to the 2006 IPCC Guidelines · src: hergoualchChapter11N2O2019 · trail: CB1-LIMING §Carbon dioxide emitted, §What is well established · from: CB1-LIMING:B-0101..0102, CB1-LIMING:B-0130..0131

### supply-chain-emissions: CO₂ from producing, transporting and spreading lime
needs: ipcc-liming-method, application-frequency

- **supply-chain-emissions.1** West and McBride quote West and Marland (2002) that "production of crushed limestone and transport to the delivery site results in CO₂ emissions of about 36 kg C per Mg of limestone," with fossil fuel combustion during spreading adding about 12 kg C/ha.
  conf: single (note: "the most-cited figure is a single 2002 estimate") · class: not stated · limit: access (note: "a 2002 US estimate I did not read in the original") · holds: a 2002 US estimate · src: westContributionAgriculturalLime2005, westSynthesisCarbonSequestration2002 (second-hand, taken from West and McBride's quotation of it) · trail: CB1-LIMING §Energy and transport, §What is well established · from: CB1-LIMING:B-0068..0069, CB1-LIMING:B-0074, CB1-LIMING:B-0136, CB1-LIMING:B-0015
- **supply-chain-emissions.2** Converting at 44/12, 36 kg C per tonne of limestone is about 132 kg CO₂ per tonne delivered.
  conf: not stated · class: deriv (note: "Converting at 44/12") · holds: the review's conversion of the West and Marland figure · src: westContributionAgriculturalLime2005, westSynthesisCarbonSequestration2002 (second-hand, taken from West and McBride's quotation of it) · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0069..0070, CB1-LIMING:B-0015
- **supply-chain-emissions.3** Applying their assumption of 5 Mg/ha every 5 years, West and McBride get about 38 kg C/ha/yr from production, transport and application combined.
  conf: not stated · class: deriv (note: "Applying their 5 Mg/ha-every-5-years assumption") · holds: lime applied at 5 Mg/ha every 5 years · src: westContributionAgriculturalLime2005 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0069, CB1-LIMING:B-0071
- **supply-chain-emissions.4** Against the 38 kg C/ha/yr of logistics, West and McBride put 120 kg C/ha/yr from the in-soil dissolution reaction at the IPCC default factor, for a total of 158.
  conf: not stated · class: not stated · holds: dissolution at the IPCC default factor · src: westContributionAgriculturalLime2005 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0072
- **supply-chain-emissions.5** The supply chain does not dominate the carbon footprint of liming: the energy and transport of getting lime to the field is roughly a quarter of it, and three quarters is the carbonate itself.
  conf: single (note: "this decomposition rests on one paper's arithmetic") · class: not stated · limit: access and evidence (note: "rests on one paper's arithmetic, and that the 36 kg C/t figure is a 2002 US estimate I did not read in the original") · holds: West and McBride's arithmetic, with dissolution at the IPCC default factor · src: westContributionAgriculturalLime2005, westSynthesisCarbonSequestration2002 (second-hand, taken from West and McBride's quotation of it) · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0072..0074, CB1-LIMING:B-0015
- **supply-chain-emissions.6** The Beerling et al. preprint gives 2020 US road transport emissions of around 50 g CO₂/t-km and rail around 15 g CO₂/t-km.
  conf: not stated · class: not stated · holds: US, 2020 values · src: beerlingTransformingUS2023 (preprint Methods; not verified against the published version) · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0080, CB1-LIMING:R-0035
- **supply-chain-emissions.7** The Beerling et al. preprint gives spreading energy of 21 kWh/t rock, giving about 0.005 t CO₂/t spread.
  conf: not stated · class: not stated · holds: US, 2020 values · src: beerlingTransformingUS2023 (preprint Methods; not verified against the published version) · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0080, CB1-LIMING:R-0035
- **supply-chain-emissions.8** Energy and transport per tonne of agricultural lime specifically are poorly constrained: the most-cited figure is a single 2002 estimate, and the modern detail comes from enhanced-weathering work on finer-ground basalt.
  conf: unclear (note: "Poorly constrained") · class: not stated · holds: agricultural lime specifically · src: westSynthesisCarbonSequestration2002 (second-hand, taken from West and McBride's quotation of it), beerlingPotentialLargescaleCO22020, beerlingTransformingUS2023, liGeospatialAssessmentCost2024 · trail: CB1-LIMING §What is well established · from: CB1-LIMING:B-0134, CB1-LIMING:B-0136, CB1-LIMING:B-0015

### country-specific-factor: The US country-specific factors and the EPA inventory
needs: ipcc-liming-method

- **country-specific-factor.1** West and McBride concluded that "net CO₂ emissions from the application of aglime is 0.059 Mg C per Mg limestone and 0.064 Mg C per Mg dolomite": a country-specific Tier 2 that halves the IPCC defaults.
  conf: not stated · class: not stated · holds: a country-specific Tier 2 analysis · src: westContributionAgriculturalLime2005 · trail: CB1-LIMING §Carbon dioxide emitted · from: CB1-LIMING:B-0102..0103
- **country-specific-factor.2** West and McBride's reasoning is that the primary dissolution pathway is reaction with carbonic acid, which takes up CO₂, and that a significant fraction of dissolved constituents leach and are transported to the ocean, where much precipitates as CaCO₃.
  conf: not stated · class: not stated · holds: the reasoning behind their country-specific factors · src: westContributionAgriculturalLime2005 · trail: CB1-LIMING §Carbon dioxide emitted · from: CB1-LIMING:B-0103
- **country-specific-factor.3** West and McBride estimated 4.4–6.6 Tg CO₂ for the US in 2001 from 20–30 Tg of aglime.
  conf: not stated · class: not stated · holds: US, 2001 · src: westContributionAgriculturalLime2005 · trail: CB1-LIMING §Carbon dioxide emitted · from: CB1-LIMING:B-0103..0104
- **country-specific-factor.4** The US EPA adopted West and McBride's factors: its 2020 US emission estimate from liming of soils is 2.4 MMT CO₂ Eq. using the country-specific factors, against 4.8 MMT CO₂ Eq. using the IPCC (2006) default emission factors.
  conf: not stated · class: not stated · rating: "Well established" · holds: US, 2020, EPA inventory · src: usLimingCRFSource2022 · trail: CB1-LIMING §Carbon dioxide emitted, §What is well established · from: CB1-LIMING:B-0105..0106, CB1-LIMING:B-0130, CB1-LIMING:B-0132
- **country-specific-factor.5** EPA applies ±15% to the activity data, and models the fraction of lime dissolved by nitric versus carbonic acid and the leached bicarbonate fraction as triangular distributions "between ranges of zero and 100 percent of the estimates".
  conf: not stated · class: not stated · holds: the EPA inventory's uncertainty analysis · src: usLimingCRFSource2022 · trail: CB1-LIMING §Carbon dioxide emitted · from: CB1-LIMING:B-0107
- **country-specific-factor.6** EPA's Monte Carlo result puts its 2020 liming emissions "between -0.26 and 4.73 MMT CO₂ Eq. at the 95 percent confidence level", 111% below to 97% above the point estimate, so a national inventory's own published confidence interval for this source includes net removal; EPA notes "a small probability of a negative emissions value leading to a net uptake of CO₂ from the atmosphere".
  conf: not stated · class: model (note: "Its Monte Carlo result") · rating: "Well established" · holds: the EPA inventory, 2020 · src: usLimingCRFSource2022 · trail: CB1-LIMING §Carbon dioxide emitted, §What is well established · from: CB1-LIMING:B-0107..0110, CB1-LIMING:B-0130, CB1-LIMING:B-0132

### field-emission-factor: Measured emission factors and the sign of the flux
needs: ipcc-liming-method, n-acidification

- **field-emission-factor.1** Cho et al. applied ¹³C-labelled CaCO₃ to a temperate Korean upland soil at 0–2 Mg/ha/yr and, measuring CO₂ fluxes by closed chamber over two years, found "approximately 0.026 Mg C per Mg of CaCO₃ was emitted as CO₂", about a fifth of the IPCC default.
  conf: not stated · class: meas (note: "measured CO₂ fluxes by closed chamber") · limit: access (note: "note where the review itself says it read only an abstract") · holds: a temperate Korean upland soil, 0–2 Mg/ha/yr, two years · src: choEvaluationCarbonDioxide2019 (abstract or structured summary only) · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0111, CB1-LIMING:B-0010, CB1-LIMING:B-0014
- **field-emission-factor.2** Cho et al. propose an emission factor of 0.039 Mg C/Mg once an ocean term is added.
  conf: not stated · class: not stated · limit: access (note: "note where the review itself says it read only an abstract") · holds: a temperate Korean upland soil · src: choEvaluationCarbonDioxide2019 (abstract or structured summary only) · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0111, CB1-LIMING:B-0010, CB1-LIMING:B-0014
- **field-emission-factor.3** Cho et al. state that the IPCC assumption that all carbonate C is released "appears unlikely based on current knowledge of the very low solubility of CaCO₃ and carbonate transport through soil".
  conf: not stated · class: not stated · limit: access (note: "note where the review itself says it read only an abstract") · holds: the authors' framing · src: choEvaluationCarbonDioxide2019 (abstract or structured summary only) · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0111..0112, CB1-LIMING:B-0010, CB1-LIMING:B-0014
- **field-emission-factor.4** Rousset et al., applying two carbonate liming products to an acidic sandy loam under winter rye, found that soil CO₂ emissions fell by approximately 40% for both materials.
  conf: not stated · class: meas (note: "Field measurements come in well below the default") · limit: access (note: "note where the review itself says it read only an abstract") · holds: an acidic sandy loam under winter rye, two carbonate liming products · src: roussetSurprisingMinimisationCO22024 (abstract or structured summary only) · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0111, CB1-LIMING:B-0113, CB1-LIMING:B-0010, CB1-LIMING:B-0014
- **field-emission-factor.5** Rousset et al. conclude that "the IPCC principles, predicting increased CO₂ emissions from lime-derived C, may need to be re-examined in the future".
  conf: not stated · class: not stated · limit: access (note: "note where the review itself says it read only an abstract") · holds: from an acidic sandy loam under winter rye · src: roussetSurprisingMinimisationCO22024 (abstract or structured summary only) · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0113, CB1-LIMING:B-0010, CB1-LIMING:B-0014
- **field-emission-factor.6** The actual emission factor is poorly constrained: measured values put it anywhere from 0.026 to 0.12 Mg C/Mg, and at least one field study found a net reduction in soil CO₂ after liming.
  conf: unclear (note: "Poorly constrained") · class: not stated · holds: the range the review gives across the IPCC (2006) default, West and McBride (2005) and Cho et al. (2019); the field study is Rousset et al. (2024) · src: dekleinChapter11N2O2006, westContributionAgriculturalLime2005, choEvaluationCarbonDioxide2019 (abstract or structured summary only), roussetSurprisingMinimisationCO22024 (abstract or structured summary only) · trail: CB1-LIMING §What is well established · from: CB1-LIMING:B-0134, CB1-LIMING:B-0013..0014
- **field-emission-factor.7** Hamilton et al. compared Ca²⁺ + Mg²⁺ against carbonate alkalinity in soil solutions, tile drainage and streams: soil solutions sampled under tension showed lime acting as either source or sink, but infiltrating waters, tile drainage and streams draining agricultural watersheds "tended to indicate net CO₂ uptake".
  conf: not stated · class: not stated · holds: mainly southern Michigan; soil solutions, tile drainage and streams draining agricultural watersheds · src: hamiltonEvidenceCarbonSequestration2007 · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0114..0115
- **field-emission-factor.8** Hamilton et al. conclude that "dissolution of lime may sequester CO₂ equal to roughly 25–50% of its C content, in contrast to the prevailing assumption that all of the carbon in lime becomes CO₂".
  conf: not stated · class: not stated · holds: mainly southern Michigan · src: hamiltonEvidenceCarbonSequestration2007 · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0114, CB1-LIMING:B-0116
- **field-emission-factor.9** Hamilton et al. state that the 30 Tg/yr of US aglime "could thus sequester up to 1.9 Tg C/yr".
  conf: not stated · class: not stated · holds: US aglime use of 30 Tg/yr · src: hamiltonEvidenceCarbonSequestration2007 · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0114, CB1-LIMING:B-0116
- **field-emission-factor.10** In Hamilton et al., "as nitrate concentrations increased in infiltrating waters, lime switched from a net CO₂ sink to a source, implying nitrification as a major acidifying process".
  conf: not stated · class: not stated · holds: infiltrating waters, mainly southern Michigan · src: hamiltonEvidenceCarbonSequestration2007 · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0114, CB1-LIMING:B-0117
- **field-emission-factor.11** Liming is carbon negative where dissolution is driven by carbonic acid and the bicarbonate is exported to groundwater and rivers, and carbon positive where strong acids, chiefly nitric acid from nitrification of fertiliser N, do the dissolving; the sign of the flux is a function of nitrogen management and hydrology, not a property of the lime.
  conf: not stated · class: not stated · holds: the review's reading of Hamilton et al.'s condition · src: hamiltonEvidenceCarbonSequestration2007 · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0114, CB1-LIMING:B-0117..0119
- **field-emission-factor.12** Hamilton et al.'s own paired measurements were not one-sided: under their no-till treatment sink strength tended positive, while "on average, liming is neither a consistent source nor a sink for CO₂."
  conf: not stated · class: meas (note: "Their own paired measurements") · holds: their paired measurements, including a no-till treatment · src: hamiltonEvidenceCarbonSequestration2007 · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0114, CB1-LIMING:B-0120
- **field-emission-factor.13** Biasi et al. published a paper titled "Direct experimental evidence for the contribution of lime to CO₂ release from managed peat soil"; the review cites it only as a pointer to a contrary result in an organic soil and makes no claim about its magnitude.
  conf: not stated · class: not stated · limit: access (note: "the abstract is withheld from the indexes I could reach") · holds: a managed peat soil · src: biasiDirectExperimentalEvidence2008 (cited by title only) · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0121..0122, CB1-LIMING:B-0016
- **field-emission-factor.14** Carbonate lime is itself a carbon dioxide source of contested magnitude.
  conf: cont (note: "contested magnitude") · class: not stated · holds: what the review says the literature supports · src: none (the review's verdict) · trail: CB1-LIMING §Verdict · from: CB1-LIMING:A-005, CB1-LIMING:A-029

### liming-effects: Effects of liming on soil pH, yield and other greenhouse gases
needs: liming

- **liming-effects.1** Wang et al., meta-analysing 1,570 observations from 121 field studies, find that liming raises crop yield by 36.3%.
  conf: not stated · class: meas (note: "meta-analysing 1,570 observations from 121 field studies") · limit: access (note: "note where the review itself says it read only an abstract") · holds: a meta-analysis of 1,570 observations from 121 field studies · src: wangPotentialBenefitsLiming2021 (abstract or structured summary only) · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0123, CB1-LIMING:B-0010, CB1-LIMING:B-0014
- **liming-effects.2** Wang et al.'s meta-analysis finds that liming cuts soil N₂O by 21.3%.
  conf: not stated · class: meas (note: "meta-analysing 1,570 observations from 121 field studies") · limit: access (note: "note where the review itself says it read only an abstract") · holds: a meta-analysis of 1,570 observations from 121 field studies · src: wangPotentialBenefitsLiming2021 (abstract or structured summary only) · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0123, CB1-LIMING:B-0010, CB1-LIMING:B-0014
- **liming-effects.3** Wang et al.'s meta-analysis finds that liming cuts paddy CH₄ by 19.0%.
  conf: not stated · class: meas (note: "meta-analysing 1,570 observations from 121 field studies") · limit: access (note: "note where the review itself says it read only an abstract") · holds: paddy soils, in a meta-analysis of 1,570 observations from 121 field studies · src: wangPotentialBenefitsLiming2021 (abstract or structured summary only) · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0123, CB1-LIMING:B-0010, CB1-LIMING:B-0014
- **liming-effects.4** In Rousset et al., liming an acidic sandy loam raised soil pH from 5.7 to about 7.0.
  conf: not stated · class: not stated · limit: access (note: "note where the review itself says it read only an abstract") · holds: an acidic sandy loam under winter rye, two carbonate liming products · src: roussetSurprisingMinimisationCO22024 (abstract or structured summary only) · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0113, CB1-LIMING:B-0010, CB1-LIMING:B-0014
- **liming-effects.5** In Rousset et al., yield rose from 320 to over 400 g/m² after liming.
  conf: not stated · class: not stated · limit: access (note: "note where the review itself says it read only an abstract") · holds: winter rye on an acidic sandy loam, two carbonate liming products · src: roussetSurprisingMinimisationCO22024 (abstract or structured summary only) · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0113, CB1-LIMING:B-0010, CB1-LIMING:B-0014
- **liming-effects.6** Gibbons et al., working on UK livestock farms, reported that liming to pH 6.0 as recommended reduced N₂O emissions and nitrate leaching.
  conf: not stated · class: not stated · limit: access (note: "I did not read the Gibbons paper in the original") · holds: UK livestock farms, liming to pH 6.0 · src: gibbonsSustainableNutrientManagement2014 (second-hand, described by Goulding), gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0124, CB1-LIMING:B-0126, CB1-LIMING:B-0015

### liming-soil-carbon: Liming and soil carbon
needs: liming

- **liming-soil-carbon.1** Wang et al.'s meta-analysis finds that liming increases SOC stocks by 4.51% annually.
  conf: not stated · class: meas (note: "meta-analysing 1,570 observations from 121 field studies") · limit: access (note: "note where the review itself says it read only an abstract") · holds: a meta-analysis of 1,570 observations from 121 field studies · src: wangPotentialBenefitsLiming2021 (abstract or structured summary only) · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0123, CB1-LIMING:B-0010, CB1-LIMING:B-0014
- **liming-soil-carbon.2** Holland et al., in a UK review, state that "the impacts of liming on soil carbon storage are variable and strongly relate to soil type, land use, climate and multiple management factors".
  conf: not stated · class: not stated · limit: access (note: "note where the review itself says it read only an abstract") · holds: a UK review · src: hollandLimingImpactsSoils2018 (abstract or structured summary only) · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0128, CB1-LIMING:B-0010, CB1-LIMING:B-0014
- **liming-soil-carbon.3** Paradelo et al. reviewed the literature and found that on balance liming increased soil C content, mostly because it increased yields and therefore residue returns.
  conf: not stated · class: not stated · holds: a literature review · src: paradeloNetEffectLiming2015 (second-hand, described by Goulding), gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0129, CB1-LIMING:B-0015

### ghg-balance: The whole-system greenhouse-gas balance of liming
needs: liming-effects, liming-soil-carbon, supply-chain-emissions

- **ghg-balance.1** Wang et al. give a global GHG benefit of liming of 633–749 Tg CO₂-eq/yr, offset by 624–656 Tg CO₂/yr from lime mining, transport, application and dissolution combined, so that "the overall GHG balance is likely neutral".
  conf: not stated · class: not stated · limit: access (note: "note where the review itself says it read only an abstract") · holds: global; the 624–656 Tg CO₂/yr assumes all acid agricultural soils worldwide were limed periodically · src: wangPotentialBenefitsLiming2021 (abstract or structured summary only) · trail: CB1-LIMING §Consumption, §Where the numbers are contested · from: CB1-LIMING:B-0052, CB1-LIMING:B-0123, CB1-LIMING:B-0010, CB1-LIMING:B-0014
- **ghg-balance.2** Gibbons et al. reported that, in CO₂-C equivalents, "the GHG emissions from liming were about four times those saved by reducing N₂O emissions".
  conf: not stated · class: not stated · limit: access (note: "I did not read the Gibbons paper in the original") · holds: UK livestock farms, liming to pH 6.0 as recommended · src: gibbonsSustainableNutrientManagement2014 (second-hand, described by Goulding), gouldingSoilAcidificationImportance2016 · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0124, CB1-LIMING:B-0126, CB1-LIMING:B-0015
- **ghg-balance.3** The whole-system greenhouse-gas balance of liming is disputed, and the disagreement is large: neutral to beneficial at global scale, four to one adverse at UK farm scale. The review does not adjudicate it: the scopes, baselines and emission factors differ, and it did not read the Gibbons paper in the original.
  conf: cont (note: "The whole-system balance is disputed") · class: not stated · holds: global scale (Wang et al.) against UK farm scale (Gibbons et al.) · src: wangPotentialBenefitsLiming2021 (abstract or structured summary only), gibbonsSustainableNutrientManagement2014 (second-hand, described by Goulding) · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0123..0126, CB1-LIMING:B-0014..0015
- **ghg-balance.4** The soil-carbon term, which drives much of the difference between the whole-system estimates, is itself unsettled.
  conf: unclear (note: "is itself unsettled") · class: not stated · holds: the review's assessment · src: none (the reviewer's synthesis) · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0127

### lime-scarcity: Whether carbonate lime is globally scarce
needs: resource-base, liming-shortfall, lime-supply-chain, consumption

- **lime-scarcity.1** The claim that carbonate lime is a globally scarce or limited material is unsupported: the one primary source that speaks directly to the question, USGS, says the opposite, and the evidence runs against scarcity from three further directions, none of which was assembled to support a conclusion.
  conf: not stated · class: not stated · contrary: not stated · holds: global; the brief asked the review to test, not support, the claim · src: willettStoneCrushed2025 · trail: CB1-LIMING §Verdict, §Verdict on the scarcity claim · from: CB1-LIMING:A-001, CB1-LIMING:A-006..007, CB1-LIMING:A-009, CB1-LIMING:B-0012
- **lime-scarcity.2** No source the review read describes carbonate lime as a globally scarce or limited material.
  conf: not stated · class: search (note: "No source I reviewed describes carbonate lime as a globally scarce or limited material") · search: searched, not found (note: "No source I reviewed describes carbonate lime as a globally scarce or limited material") · holds: the sources the review read · src: none (a search result of the review) · trail: CB1-LIMING §Verdict on the scarcity claim · from: CB1-LIMING:A-006
- **lime-scarcity.3** The USGS statement is a direct negative, from the agency whose job it is to make that assessment.
  conf: not stated · class: not stated · holds: the review's reading of the USGS statement · src: willettStoneCrushed2025 · trail: CB1-LIMING §Verdict on the scarcity claim · from: CB1-LIMING:A-007..008
- **lime-scarcity.4** A scarce mineral does not have the cost structure of Ethiopian ag-lime, roughly 5.5 ETB/Qt at the quarry against 60–163 ETB/Qt to transport it to a rural distribution point.
  conf: not stated · class: not stated · holds: the review's reading of the Ethiopian costs · src: oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Verdict on the scarcity claim · from: CB1-LIMING:A-014..015, CB1-LIMING:B-0083
- **lime-scarcity.5** Beerling et al.'s reliance on existing crushed-limestone infrastructure to argue that enhanced weathering is deployable implies a mature, large-scale extractive industry, which cuts against scarcity rather than for it.
  conf: not stated · class: not stated · holds: the review's reading, given as indirect evidence · src: beerlingPotentialLargescaleCO22020 · trail: CB1-LIMING §Verdict on the scarcity claim · from: CB1-LIMING:A-025, CB1-LIMING:A-027
- **lime-scarcity.6** The absence of a verified global consumption total means that any claim about global lime scarcity is currently being made without a global demand figure to test it against.
  conf: not stated · class: not stated · holds: global · src: none (the reviewer's synthesis) · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0050
- **lime-scarcity.7** The scarcity claim is regionally qualified in one narrow and one broad sense: a genuine USGS limitation for high-purity specialty grades, which does not extend to coarse agricultural lime, and a genuine access constraint in parts of sub-Saharan Africa, which the review characterises as a distribution problem, not a resource one.
  conf: not stated · class: not stated · holds: high-purity specialty grades; parts of sub-Saharan Africa · src: willettStoneCrushed2025, silvaSoilAcidityRemediation2025 (abstract or structured summary only), oumerAgriculturalLimeValue2023 · trail: CB1-LIMING §Verdict, §Verdict on the scarcity claim · from: CB1-LIMING:A-004, CB1-LIMING:A-016, CB1-LIMING:B-0014

## Do not say

- **dns.1** "Carbonate lime is a globally scarce or limited material."
  why: The review found this claim unsupported: USGS states that stone resources are plentiful throughout the world and classifies crushed-stone reserves as adequate, and no source the review read describes carbonate lime as globally scarce or limited. · instead: lime-scarcity.1, resource-base.1, resource-base.2 · trail: CB1-LIMING §Verdict · from: CB1-LIMING:A-001..002, CB1-LIMING:A-006
- **dns.2** "Liming is a crude fix using a globally limited material."
  why: The review says that if this is the wording in circulation, its "globally limited" half fails. · instead: lime-scarcity.1 · trail: CB1-LIMING §Verdict on the scarcity claim · from: CB1-LIMING:A-028
- **dns.3** "The limited supply of high-purity limestone shows that agricultural lime is scarce."
  why: The USGS limitation is scoped to high-purity limestone and dolomite for specialty uses; agricultural lime is a coarse bulk product with low purity requirements, no source the review read extends the limitation to it, and treating the USGS sentence as evidence for ag-lime scarcity would be a misreading. · instead: resource-base.4, resource-base.5 · trail: CB1-LIMING §Verdict on the scarcity claim · from: CB1-LIMING:A-017..020
- **dns.4** "The shortage of lime in sub-Saharan Africa shows that lime is a scarce resource."
  why: The constraint there is access, not resource: the Ethiopian case study locates the failure in the value chain, not in the deposits, and a regional access constraint on a locally abundant mineral is a distribution problem that should not be conflated with a scarcity problem. · instead: liming-shortfall.5, liming-shortfall.7, liming-shortfall.8 · trail: CB1-LIMING §Verdict on the scarcity claim · from: CB1-LIMING:A-021, CB1-LIMING:A-023..024
- **dns.5** "Lime shortages near cities show that lime reserves are limited."
  why: USGS attributes these localised shortages to zoning and land-development competition and presents them as a price driver, not a reserve limitation; the review lists them among observations that could be read as consistent with scarcity but do not evidence it. · instead: resource-base.7, resource-base.8 · trail: CB1-LIMING §Verdict on the scarcity claim · from: CB1-LIMING:A-025..026
- **dns.6** "Farmers apply too little lime because lime rock is running out."
  why: Where liming falls short of agronomic need, the documented causes are demand, price and transport logistics, not the rock; in the UK, Goulding attributes the decline in application to farm economics, not availability. · instead: liming-shortfall.1, liming-shortfall.2 · trail: CB1-LIMING §Verdict · from: CB1-LIMING:A-003, CB1-LIMING:A-011
- **dns.7** "Global consumption of agricultural lime is 395 to 450 Mt per year."
  why: Those tonnages come from commercial market-research vendors whose method and underlying data the review could not verify, so it dropped them; it found no authoritative global consumption figure. · instead: consumption.11 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0047..0049
- **dns.8** "US agricultural lime consumption is more than 45 million tons."
  why: A market-research vendor asserts this figure, which contradicts both USGS and EPA, and the review dropped it. · instead: consumption.7 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0048..0049
- **dns.9** "Agricultural lime is applied at a standard rate per hectare."
  why: Rates are set by a lime requirement calculation, not by a standard dose, and the spread across soil types is wide enough that any single number misleads. · instead: application-rate.1, application-rate.12 · trail: CB1-LIMING §Application rates · from: CB1-LIMING:B-0017
- **dns.10** "Grinding agricultural lime takes as much energy as grinding rock for enhanced weathering."
  why: Enhanced weathering grinds rock far finer than agricultural lime, so its energy figures are an upper bound for lime rather than a like-for-like figure. · instead: grinding-energy.1, grinding-energy.9 · trail: CB1-LIMING §Energy and transport · from: CB1-LIMING:B-0075
- **dns.11** "Liming worldwide releases 624–656 Tg CO₂ a year."
  why: That figure is Wang et al.'s estimate for a world in which all acid agricultural soils were limed periodically; it bounds the scale of a fully limed world and does not describe current practice. · instead: ghg-balance.1, consumption.12 · trail: CB1-LIMING §Consumption · from: CB1-LIMING:B-0052..0053
- **dns.12** "Agricultural liming is a net carbon sink."
  why: In Hamilton et al., lime switched from a net CO₂ sink to a source as nitrate rose, and on average liming was neither a consistent source nor a sink; the sign of the flux is a function of nitrogen management and hydrology, not a property of the lime. · instead: field-emission-factor.10, field-emission-factor.11, field-emission-factor.12 · trail: CB1-LIMING §Where the numbers are contested · from: CB1-LIMING:B-0114, CB1-LIMING:B-0117, CB1-LIMING:B-0119..0120

## Gaps

- **gap.1** The findings were never checked by a second reader: no independent critic ran, no second agent re-derived the load-bearing figures, and the post-hoc check covered the references, not the claims. The verdict rests on USGS's "plentiful" and "Adequate" statements, the UK decline from 6,000–7,000 to about 2,500 kt/yr against an annual loss of 4,250 kt CaCO₃, Ethiopian plants at 1–29% of installed capacity, about 5.5 ETB/Qt at the quarry against 60–163 ETB/Qt to transport, and Silva et al.'s 32.7 Mha, 23% of cropland and US$6.0 billion.
  blocks: lime-scarcity, resource-base, liming-shortfall, lime-supply-chain · origin: no critic: the note's own warning that no adversarial pass was run and the claims rest on a single agent's reading; it asks that the numbers be treated as unconfirmed until spot-checked against the primary text · search: not stated · trail: CB1-LIMING §No adversarial pass, §Verification log · from: CB1-LIMING:B-0008..0010, CB1-LIMING:B-0146..0147, CB1-LIMING:A-007, CB1-LIMING:A-011, CB1-LIMING:A-013..014, CB1-LIMING:A-022
- **gap.2** A verified global consumption figure for agricultural lime.
  blocks: consumption, lime-scarcity · origin: not found: FAOSTAT has no liming domain, and the market-research tonnages could not be verified · search: searched, not found (note: "I checked FAOSTAT directly") · from: CB1-LIMING:B-0047..0048, CB1-LIMING:B-0138..0139
- **gap.3** A systematic survey of how often lime is reapplied.
  blocks: application-frequency · origin: not found; frequency appears as a five-year working assumption · search: searched, not found (note: "I found no systematic survey establishing it") · from: CB1-LIMING:B-0028, CB1-LIMING:B-0135
- **gap.4** Which US consumption figure holds: the EPA inventory, USGS and West and McBride give between about 11 and 30 Mt/yr.
  blocks: consumption · origin: the review calls this a genuine unresolved disagreement and does not resolve it · search: not stated · from: CB1-LIMING:B-0040..0041
- **gap.5** A measured distribution of haul distances for agricultural lime.
  blocks: lime-supply-chain, supply-chain-emissions · origin: not found; the enhanced-weathering papers model distances for basalt sources · search: searched, not found (note: "I did not find a published measured distribution of haul distances") · from: CB1-LIMING:B-0082
- **gap.6** A delivered-cost breakdown for agricultural lime in the US or Europe with a verifiable method.
  blocks: lime-supply-chain · origin: not found; only trade-press and forum material · search: searched, not found (note: "I searched for a comparable delivered-cost breakdown for the US or Europe") · from: CB1-LIMING:B-0089..0090
- **gap.7** Energy and transport per tonne of agricultural lime, measured for lime itself: the most-cited figure is a single 2002 estimate the review read only second-hand, and the modern detail comes from enhanced-weathering work on finer-ground basalt.
  blocks: supply-chain-emissions, grinding-energy · origin: poorly constrained in the review; the 36 kg C/t figure was not read in the original · search: not stated · src: westSynthesisCarbonSequestration2002 · from: CB1-LIMING:B-0074, CB1-LIMING:B-0134, CB1-LIMING:B-0136
- **gap.8** The actual emission factor of agricultural lime, which measured values put anywhere from 0.026 to 0.12 Mg C/Mg.
  blocks: field-emission-factor · origin: poorly constrained in the review · search: not stated · from: CB1-LIMING:B-0134
- **gap.9** The content of Biasi et al. (2008), a contrary result in a managed peat soil, which the review knew only by its title.
  blocks: field-emission-factor · origin: source not obtained: the abstract is withheld from the indexes the review could reach · search: not stated · src: biasiDirectExperimentalEvidence2008 · from: CB1-LIMING:B-0016, CB1-LIMING:B-0122
- **gap.10** The original texts of West and Marland (2002), Gibbons et al. (2014) and Paradelo et al. (2015), which the review knew only second-hand.
  blocks: supply-chain-emissions, ghg-balance, liming-soil-carbon · origin: cited second-hand; the post-hoc check did not confirm these attributions · search: not stated · src: westSynthesisCarbonSequestration2002, gibbonsSustainableNutrientManagement2014, paradeloNetEffectLiming2015 · from: CB1-LIMING:B-0015, CB1-LIMING:B-0145
- **gap.11** The whole-system greenhouse-gas balance of liming: the global-scale and UK farm-scale results were not adjudicated, and the soil-carbon term that drives much of the difference is unsettled.
  blocks: ghg-balance, liming-soil-carbon · origin: the review declines to adjudicate; scopes, baselines and emission factors differ · search: not stated · from: CB1-LIMING:B-0126..0127
- **gap.12** The figures from sources read as abstract or structured summary only (Wang et al., Cho et al., Rousset et al., Silva et al., Holland et al.), and Li et al.'s numbers taken from an automated extraction, have not been checked line by line against the primary text.
  blocks: field-emission-factor, liming-effects, liming-soil-carbon, ghg-balance, grinding-energy, liming-shortfall · origin: the note's warning to treat the numbers as unconfirmed and to note where only an abstract was read · search: not stated · from: CB1-LIMING:B-0010, CB1-LIMING:B-0014
- **gap.13** The Beerling et al. cost and energy figures, taken from the 2023 preprint Methods, have not been checked against the published 2025 version.
  blocks: lime-supply-chain, supply-chain-emissions · origin: the review read the preprint and did not verify the figures against the published version · search: not stated · src: beerlingTransformingUS2023 · from: CB1-LIMING:R-0034..0035

## Out of scope

None: every required item is cited by an entry.

## Sources

```bibtex
@incollection{dekleinChapter11N2O2006,
  author = {De Klein, C. and Novoa, R. S. A. and Ogle, S. and Smith, K. A. and Rochette, P. and Wirth, T. C. and McConkey, B. G. and Mosier, A. and Rypdal, K.},
  title = {Chapter 11: {N2O} Emissions from Managed Soils, and {CO2} Emissions from Lime and Urea Application},
  booktitle = {2006 IPCC Guidelines for National Greenhouse Gas Inventories, Volume 4: Agriculture, Forestry and Other Land Use},
  publisher = {Institute for Global Environmental Strategies (IGES), for the IPCC National Greenhouse Gas Inventories Programme},
  address = {Hayama, Japan},
  year = {2006},
  pages = {11.1--11.54},
  url = {https://www.ipcc-nggip.iges.or.jp/public/2006gl/pdf/4_Volume4/V4_11_Ch11_N2O&CO2.pdf},
  note = {access: full_text (CB1-LIMING; §11.3 at pp. 11.26--11.30 read in full); cited as: CB1-LIMING [1]; incomplete: doi}
}

@incollection{hergoualchChapter11N2O2019,
  author = {Hergoualc'h, K. and Akiyama, H. and Bernoux, M. and Chirinda, N. and del Prado, A. and Kasimir, Å. and MacDonald, J. D. and Ogle, S. M. and Regina, K. and van der Weerden, T. J.},
  title = {Chapter 11: {N2O} Emissions from Managed Soils, and {CO2} Emissions from Lime and Urea Application},
  booktitle = {2019 Refinement to the 2006 IPCC Guidelines for National Greenhouse Gas Inventories, Volume 4: Agriculture, Forestry and Other Land Use},
  publisher = {IPCC},
  address = {Switzerland},
  year = {2019},
  url = {https://www.ipcc-nggip.iges.or.jp/public/2019rf/pdf/4_Volume4/19R_V4_Ch11_Soils_N2O_CO2.pdf},
  note = {access: full_text (CB1-LIMING; §11.3 at p. 11.27, "No refinement"); cited as: CB1-LIMING [2]; incomplete: pages, doi}
}

@incollection{willettStoneCrushed2025,
  author = {Willett, J. C.},
  title = {Stone (Crushed)},
  booktitle = {Mineral Commodity Summaries 2025},
  publisher = {U.S. Geological Survey},
  address = {Reston, Virginia},
  year = {2025},
  pages = {166--167},
  doi = {10.3133/mcs2025},
  url = {https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-stone-crushed.pdf},
  note = {access: full_text (CB1-LIMING); cited as: CB1-LIMING [3]}
}

@incollection{usLimingCRFSource2022,
  author = {{U.S. Environmental Protection Agency}},
  title = {Liming (CRF Source Category 3G)},
  booktitle = {Inventory of U.S. Greenhouse Gas Emissions and Sinks: 1990--2020, Chapter 5: Agriculture},
  publisher = {U.S. EPA},
  address = {Washington, DC},
  year = {2022},
  pages = {5-46--5-48},
  url = {https://www.epa.gov/system/files/documents/2022-04/us-ghg-inventory-2022-chapter-5-agriculture.pdf},
  note = {access: full_text (CB1-LIMING; §5.5); cited as: CB1-LIMING [4]; incomplete: doi}
}

@article{westContributionAgriculturalLime2005,
  author = {West, T. O. and McBride, A. C.},
  title = {The contribution of agricultural lime to carbon dioxide emissions in the United States: dissolution, transport, and net emissions},
  journal = {Agriculture, Ecosystems and Environment},
  volume = {108},
  number = {2},
  pages = {145--154},
  year = {2005},
  doi = {10.1016/j.agee.2005.01.002},
  note = {access: full_text (CB1-LIMING); cited as: CB1-LIMING [5]}
}

@article{hamiltonEvidenceCarbonSequestration2007,
  author = {Hamilton, S. K. and Kurzman, A. L. and Arango, C. and Jin, L. and Robertson, G. P.},
  title = {Evidence for carbon sequestration by agricultural liming},
  journal = {Global Biogeochemical Cycles},
  volume = {21},
  number = {2},
  pages = {GB2021},
  year = {2007},
  doi = {10.1029/2006GB002738},
  note = {access: full_text (CB1-LIMING); cited as: CB1-LIMING [6]}
}

@article{gouldingSoilAcidificationImportance2016,
  author = {Goulding, K. W. T.},
  title = {Soil acidification and the importance of liming agricultural soils with particular reference to the United Kingdom},
  journal = {Soil Use and Management},
  volume = {32},
  number = {3},
  pages = {390--399},
  year = {2016},
  doi = {10.1111/sum.12270},
  note = {access: full_text (CB1-LIMING); cited as: CB1-LIMING [7]}
}

@article{oumerAgriculturalLimeValue2023,
  author = {Oumer, A. M. and Diro, S. and Taye, G. and Mamo, T. and Jaleta, M.},
  title = {Agricultural lime value chain efficiency for reducing soil acidity in Ethiopia},
  journal = {Soil Security},
  volume = {11},
  pages = {100092},
  year = {2023},
  doi = {10.1016/j.soisec.2023.100092},
  note = {access: full_text (CB1-LIMING); cited as: CB1-LIMING [8]}
}

@article{beerlingPotentialLargescaleCO22020,
  author = {Beerling, D. J. and Kantzas, E. P. and Lomas, M. R. and Wade, P. and Eufrasio, R. M. and Renforth, P. and Sarkar, B. and Andrews, M. G. and James, R. H. and Pearce, C. R. and Mercure, J.-F. and Pollitt, H. and Holden, P. B. and Edwards, N. R. and Khanna, M. and Koh, L. and Quegan, S. and Pidgeon, N. F. and Janssens, I. A. and Hansen, J. and Banwart, S. A.},
  title = {Potential for large-scale {CO2} removal via enhanced rock weathering with croplands},
  journal = {Nature},
  volume = {583},
  number = {7815},
  pages = {242--248},
  year = {2020},
  doi = {10.1038/s41586-020-2448-9},
  note = {access: full_text (CB1-LIMING; main text and Methods); cited as: CB1-LIMING [9]}
}

@misc{beerlingTransformingUS2023,
  author = {Beerling, D. J. and Kantzas, E. P. and Lomas, M. R. and Taylor, L. L. and Zhang, S. and Kanzaki, Y. and Eufrasio, R. M. and Renforth, P. and Mercure, J.-F. and Pollitt, H. and Holden, P. B. and Edwards, N. R. and Koh, L. and Epihov, D. Z. and Wolf, A. and Hansen, J. E. and Banwart, S. A. and Pidgeon, N. F. and Reinhard, C. T. and Planavsky, N. J. and Val Martin, M.},
  title = {Transforming U.S. agriculture with crushed rock for {CO2} sequestration and increased production},
  howpublished = {arXiv preprint arXiv:2308.04302},
  year = {2023},
  url = {https://arxiv.org/abs/2308.04302},
  note = {access: full_text (CB1-LIMING; preprint Methods; the figures were not verified against the published version); type: preprint; published in revised form as Beerling et al. (2025), Transforming US agriculture for carbon removal with enhanced weathering, Nature 638(8050), 425--434, doi 10.1038/s41586-024-08429-2; cited as: CB1-LIMING [10]}
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
  note = {access: abstract_only (CB1-LIMING; abstract or structured summary only); cited as: CB1-LIMING [11]}
}

@article{choEvaluationCarbonDioxide2019,
  author = {Cho, S. R. and Jeong, S. T. and Kim, G. Y. and Lee, J. G. and Kim, P. J. and Kim, G. W.},
  title = {Evaluation of the carbon dioxide ({CO2}) emission factor from lime applied in temperate upland soil},
  journal = {Geoderma},
  volume = {337},
  pages = {742--748},
  year = {2019},
  doi = {10.1016/j.geoderma.2018.10.007},
  note = {access: abstract_only (CB1-LIMING; abstract or structured summary only); cited as: CB1-LIMING [12]}
}

@article{roussetSurprisingMinimisationCO22024,
  author = {Rousset, C. and Bréfort, H. and Frederico Fonseca, R. and Guyerdet, G. and Bizouard, F. and Arkoun, M. and Hénault, C.},
  title = {Surprising minimisation of {CO2} emissions from a sandy loam soil over a rye growing period achieved by liming ({CaCO3})},
  journal = {Science of the Total Environment},
  volume = {953},
  pages = {175973},
  year = {2024},
  doi = {10.1016/j.scitotenv.2024.175973},
  note = {access: abstract_only (CB1-LIMING; abstract or structured summary only); cited as: CB1-LIMING [13]}
}

@article{silvaSoilAcidityRemediation2025,
  author = {Silva, J. V. and Aramburu-Merlos, F. and Baudron, F. and Gameda, S. and Sida, T. S. and Ruganzu, V. and Meliyo, J. and Jaleta, M. and Chamberlin, J. and Hijmans, R. J.},
  title = {Soil acidity remediation in sub-Saharan Africa requires targeted investments},
  journal = {Nature Food},
  volume = {6},
  number = {8},
  pages = {799--808},
  year = {2025},
  doi = {10.1038/s43016-025-01194-z},
  note = {access: abstract_only (CB1-LIMING; abstract or structured summary only); cited as: CB1-LIMING [14]}
}

@article{hollandLimingImpactsSoils2018,
  author = {Holland, J. E. and Bennett, A. E. and Newton, A. C. and White, P. J. and McKenzie, B. M. and George, T. S. and Pakeman, R. J. and Bailey, J. S. and Fornara, D. A. and Hayes, R. C.},
  title = {Liming impacts on soils, crops and biodiversity in the UK: A review},
  journal = {Science of the Total Environment},
  volume = {610--611},
  pages = {316--332},
  year = {2018},
  doi = {10.1016/j.scitotenv.2017.08.020},
  note = {access: abstract_only (CB1-LIMING; abstract or structured summary only); cited as: CB1-LIMING [15]}
}

@article{aramburumerlosEstimatingLimeRequirements2023,
  author = {Aramburu Merlos, F. and Silva, J. V. and Baudron, F. and Hijmans, R. J.},
  title = {Estimating lime requirements for tropical soils: Model comparison and development},
  journal = {Geoderma},
  volume = {432},
  pages = {116421},
  year = {2023},
  doi = {10.1016/j.geoderma.2023.116421},
  note = {access: full_text (CB1-LIMING; read the full text but used only its framing; the note lists it under "Read as abstract or structured summary only"); cited as: CB1-LIMING [16]}
}

@article{liGeospatialAssessmentCost2024,
  author = {Li, Z. and Planavsky, N. J. and Reinhard, C. T.},
  title = {Geospatial assessment of the cost and energy demand of feedstock grinding for enhanced rock weathering in the coterminous United States},
  journal = {Frontiers in Climate},
  volume = {6},
  pages = {1380651},
  year = {2024},
  doi = {10.3389/fclim.2024.1380651},
  note = {access: full_text (CB1-LIMING; numbers came from an automated extraction of the full article rather than a line-by-line read; the note lists it under "Read as abstract or structured summary only"); cited as: CB1-LIMING [17]}
}

@article{westSynthesisCarbonSequestration2002,
  author = {West, T. O. and Marland, G.},
  title = {A synthesis of carbon sequestration, carbon emissions, and net carbon flux in agriculture: comparing tillage practices in the United States},
  journal = {Agriculture, Ecosystems and Environment},
  volume = {91},
  number = {1--3},
  pages = {217--232},
  year = {2002},
  doi = {10.1016/S0167-8809(01)00233-X},
  note = {access: secondary (CB1-LIMING; cited second-hand via West and McBride 2005; not read in the original); cited as: CB1-LIMING [18]}
}

@article{gibbonsSustainableNutrientManagement2014,
  author = {Gibbons, J. M. and Williamson, J. C. and Williams, A. P. and Withers, P. J. A. and Hockley, N. and Harris, I. M. and Hughes, J. W. and Taylor, R. L. and Jones, D. L. and Healey, J. R.},
  title = {Sustainable nutrient management at field, farm and regional level: soil testing, nutrient budgets and the trade-off between lime application and greenhouse gas emissions},
  journal = {Agriculture, Ecosystems and Environment},
  volume = {188},
  pages = {48--56},
  year = {2014},
  doi = {10.1016/j.agee.2014.02.016},
  note = {access: secondary (CB1-LIMING; cited second-hand via Goulding 2016; not read in the original); cited as: CB1-LIMING [19]}
}

@article{paradeloNetEffectLiming2015,
  author = {Paradelo, R. and Virto, I. and Chenu, C.},
  title = {Net effect of liming on soil organic carbon stocks: A review},
  journal = {Agriculture, Ecosystems and Environment},
  volume = {202},
  pages = {98--107},
  year = {2015},
  doi = {10.1016/j.agee.2015.01.005},
  note = {access: secondary (CB1-LIMING; cited second-hand via Goulding 2016; not read in the original); cited as: CB1-LIMING [20]}
}

@article{biasiDirectExperimentalEvidence2008,
  author = {Biasi, C. and Lind, S. E. and Pekkarinen, N. M. and Huttunen, J. T. and Shurpali, N. J. and Hyvönen, N. P. and Repo, M. E. and Martikainen, P. J.},
  title = {Direct experimental evidence for the contribution of lime to {CO2} release from managed peat soil},
  journal = {Soil Biology and Biochemistry},
  volume = {40},
  number = {10},
  pages = {2660--2669},
  year = {2008},
  doi = {10.1016/j.soilbio.2008.07.011},
  note = {access: not_obtained (CB1-LIMING; read only the title, the abstract is withheld by the publisher from the indexes the review could reach; bibliographic details verified); cited as: CB1-LIMING [21]}
}

@misc{foodClimateChangeAgrifood2025,
  author = {{Food and Agriculture Organization of the United Nations}},
  title = {Climate Change: Agrifood systems emissions - Emissions from Crops (domain description and dataset inventory)},
  howpublished = {FAOSTAT, FAO, Rome},
  year = {2025},
  url = {https://bulks-faostat.fao.org/production/datasets_E.json},
  note = {access: full_text (CB1-LIMING; consulted 18 September 2026 to confirm that no FAOSTAT climate-change domain covers liming; domain documentation https://files-faostat.fao.org/production/GT/GT_en.pdf); cited as: CB1-LIMING [22]}
}

@techreport{rasnakeLimingAcidSoils1993,
  author = {Rasnake, Monroe and Murdock, Lloyd},
  title = {Liming Acid Soils},
  institution = {University of Kentucky, College of Agriculture, Department of Agronomy},
  number = {AGR-19},
  year = {1993},
  url = {https://publications.mgcafe.uky.edu/sites/publications.ca.uky.edu/files/agr19.htm},
  note = {background; issued 1961, revised 1993}
}

@article{hartmannEnhancedChemicalWeathering2013,
  author = {Hartmann, Jens and West, A. Joshua and Renforth, Phil and Köhler, Peter and De La Rocha, Christina L. and Wolf-Gladrow, Dieter A. and Dürr, Hans H. and Scheffran, Jürgen},
  title = {Enhanced chemical weathering as a geoengineering strategy to reduce atmospheric carbon dioxide, supply nutrients, and mitigate ocean acidification},
  journal = {Reviews of Geophysics},
  volume = {51},
  number = {2},
  pages = {113--149},
  year = {2013},
  doi = {10.1002/rog.20004},
  note = {background}
}

@incollection{rypdalChapter1Introduction2006,
  author = {Rypdal, Kristin and Paciornik, Newton and Eggleston, Simon and Goodwin, Justin and Irving, William and Penman, Jim and Woodfield, Mike},
  title = {Chapter 1: Introduction to the 2006 Guidelines},
  booktitle = {2006 IPCC Guidelines for National Greenhouse Gas Inventories, Volume 1: General Guidance and Reporting},
  publisher = {Institute for Global Environmental Strategies (IGES)},
  address = {Hayama, Japan},
  year = {2006},
  url = {https://www.ipcc-nggip.iges.or.jp/public/2006gl/pdf/1_Volume1/V1_1_Ch1_Introduction.pdf},
  note = {background}
}
```
