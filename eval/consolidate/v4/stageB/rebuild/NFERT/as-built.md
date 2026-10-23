---
type: knowledge
title: Synthetic nitrogen fertiliser and soil microbial nitrogen cycling
inputs:
  - NFERT: PhD/Proposal/Research/Results/N-fertiliser_microbial-cycling_review.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-23
status: draft
tags:
  - research
  - knowledge
---

# Synthetic nitrogen fertiliser and soil microbial nitrogen cycling

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
| NFERT | [[N-fertiliser_microbial-cycling_review]] | no | narrative author-year | no | no | fallback (answers and critique; the note has no labelled citations) |

## Concepts

### haber-bosch: Haber-Bosch ammonia synthesis
needs: none
- **haber-bosch.1** Ammonia synthesis runs through the Haber-Bosch process, which fixes atmospheric N₂ with hydrogen at high temperature and pressure.
  conf: not stated · class: not stated · holds: ammonia synthesis, as the review describes the process · src: none (the review cites no source for this sentence) · trail: NFERT §Energy per unit · from: NFERT:B-0022
- **haber-bosch.2** Most of the energy and almost all of the carbon in ammonia synthesis enter upstream, when hydrogen is stripped from natural gas or coal by steam reforming.
  conf: not stated · class: not stated · holds: ammonia synthesis with hydrogen from natural gas or coal by steam reforming · src: none (the review cites no source for this sentence) · trail: NFERT §Energy per unit · from: NFERT:B-0022, NFERT:B-0023

### ammonia-nitrogen: ammonia as the carrier of fertiliser nitrogen
needs: none
- **ammonia-nitrogen.1** Ammonia carries 82% nitrogen by mass, so one tonne of N requires about 1.21 tonnes of ammonia.
  conf: not stated · class: not stated · holds: the mass ratio the review uses to convert per-ammonia figures into per-tonne-N values · src: none (the review cites no source for this sentence) · trail: NFERT §Energy per unit · from: NFERT:B-0027, NFERT:B-0028, NFERT:R-0013

### manufacturing-energy: energy to manufacture ammonia and fertiliser nitrogen
needs: haber-bosch, ammonia-nitrogen
- **manufacturing-energy.1** Modern natural-gas plants need roughly 28 GJ per tonne of ammonia.
  conf: not stated · class: not stated · holds: modern natural-gas ammonia plants; per tonne of ammonia · src: tockThermoEnvironomicEvaluation2015, demirhanSustainableAmmoniaProduction2019 · trail: NFERT §Energy per unit · from: NFERT:B-0024
- **manufacturing-energy.2** The global average energy requirement for ammonia sits near 37 GJ per tonne, higher than modern natural-gas plants because older and coal-fed plants remain in service.
  conf: not stated · class: not stated · holds: global average of ammonia production, per tonne of ammonia; against modern natural-gas plants at roughly 28 GJ · src: tunaTechnoEconomicAssessment2014 · trail: NFERT §Energy per unit · from: NFERT:B-0024, NFERT:B-0025
- **manufacturing-energy.3** Coal-based ammonia production in China runs to about 59 GJ per tonne of ammonia.
  conf: not stated · class: not stated · holds: coal-based production in China; per tonne of ammonia · src: tunaTechnoEconomicAssessment2014 · trail: NFERT §Energy per unit · from: NFERT:B-0024, NFERT:B-0025
- **manufacturing-energy.4** The energy requirement of ammonia production fell from about 55 GJ per tonne in the 1950s to the high-20s today.
  conf: not stated · class: not stated · holds: the historical trajectory from the 1950s to today; per tonne of ammonia · src: tunaTechnoEconomicAssessment2014 · trail: NFERT §Energy per unit · from: NFERT:B-0024, NFERT:B-0026
- **manufacturing-energy.5** Manufacturing one tonne of fertiliser N costs roughly 34 GJ on the best natural-gas route and roughly 45 GJ at the global average; these per-N figures are arithmetic applied to the cited per-ammonia values, not separately measured quantities.
  conf: not stated · class: deriv (note: "The conversion is arithmetic applied to the cited per-ammonia values, not a separately measured quantity") · holds: per tonne of N, converted from the per-ammonia figures (roughly 28 GJ for modern natural-gas plants, near 37 GJ at the global average) at about 1.21 tonnes of ammonia per tonne of N · src: none (the reviewer's conversion of the cited per-ammonia figures) · trail: NFERT §Energy per unit · from: NFERT:B-0024, NFERT:B-0025, NFERT:B-0027, NFERT:B-0028, NFERT:B-0029
- **manufacturing-energy.6** Manufacturing ammonia costs about 28 to 37 GJ per tonne.
  conf: repl (note: "Independent industrial-ecology and biogeochemistry sources converge") · class: not stated · holds: manufacture, per tonne of ammonia; the range runs from modern natural-gas plants (roughly 28 GJ) to the global average (near 37 GJ) · src: tockThermoEnvironomicEvaluation2015, demirhanSustainableAmmoniaProduction2019, razonLifeCycleAnalysis2014, tunaTechnoEconomicAssessment2014 · trail: NFERT §Verdicts, §Energy per unit · from: NFERT:A-001, NFERT:A-002, NFERT:B-0024, NFERT:B-0025 · rating: "WELL-ESTABLISHED WITH QUANTIFIED FIGURES"

### manufacturing-co2: carbon dioxide from manufacturing ammonia and fertiliser nitrogen
needs: haber-bosch, ammonia-nitrogen
- **manufacturing-co2.1** Production CO₂ from ammonia manufacture tracks the feedstock.
  conf: not stated · class: not stated · holds: ammonia production · src: none (the review cites no source for this sentence) · trail: NFERT §Carbon dioxide · from: NFERT:B-0030
- **manufacturing-co2.2** Modern natural-gas plants emit close to 1.6 t CO₂ per tonne of ammonia.
  conf: not stated · class: not stated · holds: modern natural-gas ammonia plants; per tonne of ammonia · src: tockThermoEnvironomicEvaluation2015 · trail: NFERT §Carbon dioxide · from: NFERT:B-0031
- **manufacturing-co2.3** The ecoinvent inventory gives 1.92 t CO₂-equivalent per tonne of liquid ammonia, alongside 41 GJ of primary energy.
  conf: not stated · class: not stated · holds: the ecoinvent inventory, which the review calls widely used, as given in Razon 2014; per tonne of liquid ammonia · src: razonLifeCycleAnalysis2014 · trail: NFERT §Carbon dioxide · from: NFERT:B-0032
- **manufacturing-co2.4** A process-optimisation study citing a global production mix that includes coal reports about 2.8 t CO₂ per tonne of ammonia.
  conf: not stated · class: not stated · holds: a global mix that includes coal, as cited by a process-optimisation study (Demirhan et al. 2019); per tonne of ammonia · src: demirhanSustainableAmmoniaProduction2019 · trail: NFERT §Carbon dioxide · from: NFERT:B-0031, NFERT:B-0033
- **manufacturing-co2.5** Carbon capture on a natural-gas plant can bring the gate figure down to about 0.79 t CO₂ per tonne of ammonia.
  conf: not stated · class: not stated · holds: a natural-gas plant with carbon capture; gate figure per tonne of ammonia · src: tockThermoEnvironomicEvaluation2015 · trail: NFERT §Carbon dioxide · from: NFERT:B-0031, NFERT:B-0034
- **manufacturing-co2.6** Expressed per unit nitrogen, the manufacturing footprint is about 1.9 to 3.4 t CO₂-equivalent per tonne of N, the lower bound for efficient gas plants and the upper bound for coal-heavy mixes.
  conf: not stated · class: deriv (note: "per-tonne-N values flagged where they derive from stoichiometric conversion of per-ammonia figures") · holds: cradle-to-gate manufacturing; per tonne of N, from stoichiometric conversion of per-ammonia figures; lower bound efficient gas plants, upper bound coal-heavy mixes · src: none (the reviewer's conversion of the cited per-ammonia figures) · trail: NFERT §Carbon dioxide · from: NFERT:B-0035, NFERT:B-0036, NFERT:R-0013
- **manufacturing-co2.7** Manufacture emits about 1.6 to 2.8 t CO₂ per tonne of ammonia, equivalently about 1.9 to 3.4 t CO₂-equivalent per tonne of N.
  conf: repl (note: "Independent industrial-ecology and biogeochemistry sources converge") · class: not stated · holds: manufacture; per tonne of ammonia, and per tonne of N · src: tockThermoEnvironomicEvaluation2015, demirhanSustainableAmmoniaProduction2019, razonLifeCycleAnalysis2014, tunaTechnoEconomicAssessment2014 · trail: NFERT §Verdicts, §Integration read · from: NFERT:A-001, NFERT:A-002, NFERT:B-0012 · rating: "WELL-ESTABLISHED WITH QUANTIFIED FIGURES"
- **manufacturing-co2.8** These manufacturing figures are cradle-to-gate: they exclude the field N₂O released after application, which is the larger life-cycle term and belongs to use, not manufacture.
  conf: not stated · class: not stated · holds: cradle-to-gate manufacturing figures against the field N₂O of the use phase · src: menegatGreenhouseGasEmissions2022, gaoGreenhouseGasEmissions2023 · trail: NFERT §Carbon dioxide · from: NFERT:B-0036, NFERT:B-0037

### emission-share: nitrogen fertiliser's share of greenhouse-gas emissions
needs: manufacturing-co2
- **emission-share.1** The share of emissions attributed to nitrogen fertiliser depends entirely on where the system boundary is drawn, and the three commonly cited figures answer three different questions.
  conf: not stated · class: not stated · holds: manufacturing alone, the synthetic-N supply chain, and the full nitrogen-fertiliser life cycle including manure · src: none (the reviewer's synthesis) · trail: NFERT §Share of emissions · from: NFERT:B-0038, NFERT:B-0049
- **emission-share.2** Manufacturing alone is the smallest of the three slices.
  conf: not stated · class: not stated · holds: manufacturing alone, against the synthetic-N supply chain and the full life cycle including manure · src: none (the reviewer's synthesis) · trail: NFERT §Share of emissions · from: NFERT:B-0039, NFERT:B-0049
- **emission-share.3** The International Fertilizer Association attributed 0.47 Gt CO₂-equivalent, about 0.93% of total anthropogenic emissions, to N fertiliser production in 2007.
  conf: not stated · class: not stated · holds: N fertiliser production (manufacturing alone), 2007; the International Fertilizer Association's figure as reported in Menegat et al. 2022 · src: menegatGreenhouseGasEmissions2022 · trail: NFERT §Share of emissions · from: NFERT:B-0039, NFERT:B-0040
- **emission-share.4** Independent process studies place ammonia manufacture at roughly 1% to 1.8% of global greenhouse-gas emissions.
  conf: not stated · class: not stated · holds: ammonia manufacture; process studies · src: tunaTechnoEconomicAssessment2014, demirhanSustainableAmmoniaProduction2019, tockThermoEnvironomicEvaluation2015 · trail: NFERT §Share of emissions · from: NFERT:B-0041
- **emission-share.5** Manufacture is about 0.9% to 1.8% of global emissions.
  conf: repl (note: "Independent industrial-ecology and biogeochemistry sources converge") · class: not stated · holds: manufacturing alone; the range spans the International Fertilizer Association's 0.93% for 2007 (reported in Menegat et al. 2022) and the process studies' 1% to 1.8% · src: menegatGreenhouseGasEmissions2022, tunaTechnoEconomicAssessment2014, demirhanSustainableAmmoniaProduction2019, tockThermoEnvironomicEvaluation2015 · trail: NFERT §Verdicts, §Share of emissions, §Integration read · from: NFERT:A-001, NFERT:A-003, NFERT:B-0012, NFERT:B-0040, NFERT:B-0041, NFERT:B-0049 · rating: "WELL-ESTABLISHED WITH QUANTIFIED FIGURES"
- **emission-share.6** The full synthetic-N supply chain, which adds field and transport emissions to manufacture, came to 1.13 Gt CO₂-equivalent in 2018, equal to 10.6% of agricultural emissions and 2.1% of global emissions.
  conf: not stated · class: not stated · holds: the full synthetic-N supply chain (manufacture, field and transport), 2018; Menegat et al. (2022)'s estimate · src: menegatGreenhouseGasEmissions2022 · trail: NFERT §Share of emissions, §Verdicts, §Integration read · from: NFERT:A-001, NFERT:A-003, NFERT:B-0012, NFERT:B-0042, NFERT:B-0043, NFERT:B-0049 · rating: "WELL-ESTABLISHED WITH QUANTIFIED FIGURES"
- **emission-share.7** Within the synthetic-N supply-chain total, manufacture accounts for 38.8%, field emissions for 58.6% and transport for 2.6%.
  conf: not stated · class: not stated · holds: Menegat et al. (2022)'s 2018 supply-chain total of 1.13 Gt CO₂-equivalent · src: menegatGreenhouseGasEmissions2022 · trail: NFERT §Share of emissions · from: NFERT:B-0043, NFERT:B-0044
- **emission-share.8** In the synthetic-N supply chain, the use phase, not the factory, dominates emissions.
  conf: not stated · class: not stated · holds: the synthetic-N supply chain, where field emissions are 58.6% and manufacture 38.8% of the total · src: menegatGreenhouseGasEmissions2022 · trail: NFERT §Share of emissions · from: NFERT:B-0043, NFERT:B-0044, NFERT:B-0045
- **emission-share.9** Production and use of nitrogen fertiliser, manure included, come to about 5% of global greenhouse-gas emissions, roughly two-thirds occurring after deployment and one-third during production.
  conf: not stated · class: not stated · holds: the full nitrogen-fertiliser life cycle including manure; Gao and Cabrera Serrenho (2023)'s estimate · src: gaoGreenhouseGasEmissions2023 · trail: NFERT §Share of emissions, §Verdicts, §Integration read · from: NFERT:A-001, NFERT:A-003, NFERT:B-0012, NFERT:B-0046, NFERT:B-0047, NFERT:B-0049 · rating: "WELL-ESTABLISHED WITH QUANTIFIED FIGURES"
- **emission-share.10** Manure emits about 23 t CO₂-equivalent per tonne of N, some 1.9 times an average synthetic fertiliser, because much of its nitrogen is lost.
  conf: not stated · class: not stated · holds: per tonne of N, manure against an average synthetic fertiliser; reported by Gao and Cabrera Serrenho (2023) · src: gaoGreenhouseGasEmissions2023 · trail: NFERT §Share of emissions · from: NFERT:B-0047, NFERT:B-0048
- **emission-share.11** Quoting one of these figures as if it were another is the most common error in this literature.
  conf: not stated · class: not stated · holds: the three boundary figures (manufacturing about 0.9% to 1.8%, the synthetic-N supply chain about 2.1%, the full life cycle including manure about 5% of global emissions) · src: none (the reviewer's statement) · trail: NFERT §Share of emissions · from: NFERT:B-0049, NFERT:B-0050

### nitrogen-use-efficiency: nitrogen-use efficiency
needs: emission-share
- **nitrogen-use-efficiency.1** Nitrogen-use efficiency is the single most effective mitigation lever for the emissions of the nitrogen-fertiliser life cycle.
  conf: not stated · class: not stated · holds: the full nitrogen-fertiliser life cycle including manure (production and use); Gao and Cabrera Serrenho (2023) identify it · src: gaoGreenhouseGasEmissions2023 · trail: NFERT §Share of emissions · from: NFERT:B-0046, NFERT:B-0047, NFERT:B-0048

### symbiotic-fixation: symbiotic biological nitrogen fixation by legumes and rhizobia
needs: none
- **symbiotic-fixation.1** Legumes in symbiosis with rhizobia are the largest biological nitrogen input to cropping systems, and their effect on fertiliser demand is documented.
  conf: not stated · class: not stated · holds: cropping systems · src: ladhaBiologicalNitrogenFixation2022 · trail: NFERT §The strong, direct channel · from: NFERT:B-0054
- **symbiotic-fixation.2** In an organic legume-based rotation in Europe, 87% of total nitrogen inputs came from fixation, and the rotation matched conventional productivity at a surplus of only 21 kg N per hectare per year, against 40 to 100 for fertilised systems.
  conf: not stated · class: not stated · holds: an organic legume-based rotation in Europe, against fertilised systems; N surplus in kg N per hectare per year · src: angladeRelationshipsEstimatingN22015 · trail: NFERT §The strong, direct channel · from: NFERT:B-0055
- **symbiotic-fixation.3** The mechanism is direct: fixed nitrogen substitutes for applied nitrogen in the legume and partially enriches the following crop.
  conf: not stated · class: not stated · holds: legume symbiotic fixation and the following crop · src: none (the review cites no source for this sentence) · trail: NFERT §The strong, direct channel · from: NFERT:B-0056
- **symbiotic-fixation.4** The fraction of legume nitrogen derived from fixation varies enormously, from a few percent to nearly all, depending on species, soil mineral nitrogen and competition.
  conf: not stated · class: not stated · holds: legumes; one of two qualifications the review says bound the symbiotic channel · src: angladeRelationshipsEstimatingN22015, ladhaBiologicalNitrogenFixation2022 · trail: NFERT §The strong, direct channel · from: NFERT:B-0057, NFERT:B-0058
- **symbiotic-fixation.5** Fixation is suppressed by the fertiliser it might replace: applying 125 to 250 kg fertiliser N per hectare cut fixation rates by 81% to 86% in one system reviewed by Ladha et al. (2022).
  conf: not stated · class: not stated · holds: one system reviewed by Ladha et al. (2022); 125 to 250 kg fertiliser N per hectare · src: ladhaBiologicalNitrogenFixation2022 · trail: NFERT §The strong, direct channel, §Where the evidence sits · from: NFERT:B-0059, NFERT:B-0074
- **symbiotic-fixation.6** Symbiotic fixation and fertiliser are partly substitutive, not additive, which caps the achievable saving.
  conf: not stated · class: reading (note: "Symbiotic fixation and fertiliser are therefore partly substitutive, not additive") · holds: the reviewer's inference from fertiliser suppression of fixation (125 to 250 kg N per hectare cutting fixation by 81% to 86% in one system) · src: none (the reviewer's inference from the suppression finding) · trail: NFERT §The strong, direct channel, §Where the evidence sits · from: NFERT:B-0059, NFERT:B-0060, NFERT:B-0074
- **symbiotic-fixation.7** Where legume-based biological fixation is deliberately added, the reduction in synthetic input is real and direct, with strong direct evidence bounded by wide variability in fixation fraction and by fertiliser suppression of fixation.
  conf: not stated · class: not stated · holds: deliberate legume-based biological fixation (humans deliberately adding a nitrogen-fixing symbiosis) · src: angladeRelationshipsEstimatingN22015, ladhaBiologicalNitrogenFixation2022 · trail: NFERT §Verdicts, §Question 2 · from: NFERT:A-004, NFERT:B-0052 · rating: "ESTABLISHED BUT QUALIFIED" · contrary: not stated

### free-living-fixation: free-living and associative diazotrophs
needs: none
- **free-living-fixation.bg1** Diazotrophs are the nitrogen-fixing organisms; most biological nitrogen fixation results from the activity of the molybdenum nitrogenase, an oxygen-sensitive metalloenzyme complex found in all known diazotrophs.
  kind: background · ref: musExploringAlternativesBiological2018 · check: DOI 10.1039/c8mt00038g resolves on Crossref (Metallomics 10(4):523-538, 2018); stated in the abstract (Europe PMC record), first sentences
- **free-living-fixation.1** Free-living and associative diazotrophs are ubiquitous and do fix nitrogen, but their measured contribution in cereal systems is modest.
  conf: not stated · class: meas (note: "their measured contribution in cereal systems is modest") · holds: cereal systems · src: ladhaBiologicalNitrogenFixation2022 · trail: NFERT §The weak channel · from: NFERT:B-0063, NFERT:A-006
- **free-living-fixation.2** Engineering cereals to fix their own nitrogen remains unrealised.
  conf: not stated · class: not stated · holds: cereals · src: ladhaBiologicalNitrogenFixation2022 · trail: NFERT §The weak channel · from: NFERT:B-0063
- **free-living-fixation.3** Free-living fixation gives only INDIRECT support for a reduced fertiliser requirement: the fixed quantities are rarely large enough to displace a defined fertiliser rate at constant yield.
  conf: not stated · class: not stated · holds: free-living and associative diazotrophs in cereal systems; displacement of a defined fertiliser rate at constant yield · src: ladhaBiologicalNitrogenFixation2022 (INDIRECT) · trail: NFERT §The weak channel, §Verdicts · from: NFERT:B-0063, NFERT:B-0064, NFERT:A-006

### microbial-inoculants: microbial inoculants (biofertilisers)
needs: none
- **microbial-inoculants.1** Microbial inoculants raise yield inconsistently: the largest meta-analysis, spanning 171 field studies, found yield responses of +8.5% in continental climates, +10.0% in oceanic, +14.9% in tropical and +20.0% in dry climates, with effects described as often inconsistent and dependent on soil phosphorus and climate.
  conf: not stated · class: not stated · holds: a meta-analysis of 171 field studies; yield response by climate (continental, oceanic, tropical, dry); dependent on soil phosphorus and climate · src: schutzImprovingCropYield2018 · trail: NFERT §The weak channel · from: NFERT:B-0065, NFERT:B-0066
- **microbial-inoculants.2** The inoculant evidence is INDIRECT for the question of reduced synthetic input, because it measures yield gain at a given input rather than input reduction at a held yield.
  conf: not stated · class: not stated · holds: inoculant field evidence; yield gain at a given input, not input reduction at a held yield · src: schutzImprovingCropYield2018 (INDIRECT) · trail: NFERT §The weak channel, §Verdicts · from: NFERT:B-0067, NFERT:A-006

### n-mineralisation: nitrogen mineralisation by the resident community
needs: none
- **n-mineralisation.1** Only about 1% to 4% of soil organic nitrogen is mineralised in a season.
  conf: not stated · class: not stated · holds: soil organic nitrogen; per season · src: stluceNitrogenDynamicsIndices2011 · trail: NFERT §The weak channel · from: NFERT:B-0069
- **n-mineralisation.2** Mineralisation by the resident community supplies nitrogen, but alone it is seldom sufficient to reach the maximum yield of modern cultivars, so additional fertiliser or organic nitrogen is needed.
  conf: not stated · class: not stated · holds: maximum yield of modern cultivars · src: stluceNitrogenDynamicsIndices2011 · trail: NFERT §The weak channel, §Verdicts · from: NFERT:B-0068, NFERT:B-0069, NFERT:A-006
- **n-mineralisation.3** Quantifying soil nitrogen supply can improve fertiliser-use efficiency and trim rates, but the lever is the measured soil supply, not a demonstrated property of microbial-community efficiency.
  conf: not stated · class: not stated · holds: measured soil nitrogen supply used to set fertiliser rates · src: none (the review cites no source for this sentence) · trail: NFERT §The weak channel · from: NFERT:B-0070

### fertiliser-substitution: whether microbial nitrogen cycling reduces synthetic nitrogen input
needs: symbiotic-fixation, free-living-fixation, microbial-inoculants, n-mineralisation
- **fertiliser-substitution.1** Whether microbial nitrogen cycling reduces synthetic input splits along a clear line: where humans deliberately add a nitrogen-fixing symbiosis, the reduction is real and direct; where the claim rests on the resident free-living community cycling nitrogen more efficiently, the support is mostly indirect.
  conf: not stated · class: not stated · holds: the question of whether efficient microbial nitrogen cycling in soil lowers the synthetic input a crop needs at constant yield · src: none (the reviewer's synthesis) · trail: NFERT §Question 2 · from: NFERT:B-0003, NFERT:B-0051, NFERT:B-0052, NFERT:B-0053
- **fertiliser-substitution.2** The strongest evidence for reduced synthetic input is agronomic and concerns legume inclusion, a deliberate management choice, not the spontaneous efficiency of a resident community.
  conf: not stated · class: not stated · holds: agronomic evidence on legume inclusion · src: none (the reviewer's synthesis) · trail: NFERT §Where the evidence sits · from: NFERT:B-0071
- **fertiliser-substitution.3** Reduced fertiliser need co-varies with soil organic matter, water (moisture), rotation and management, so the microbial contribution is hard to separate.
  conf: not stated · class: not stated · holds: attribution, the first of the three failure modes the review names · src: none (the reviewer's synthesis) · trail: NFERT §Where the evidence sits · from: NFERT:B-0008, NFERT:B-0072, NFERT:B-0073
- **fertiliser-substitution.4** Free-living fixation and mineralisation seldom meet high-yield demand, so the resident community supplements rather than replaces synthetic nitrogen.
  conf: not stated · class: not stated · holds: magnitude, one of the three failure modes the review names; high-yield demand · src: none (the reviewer's synthesis) · trail: NFERT §Where the evidence sits · from: NFERT:B-0072, NFERT:B-0075
- **fertiliser-substitution.5** For the resident microbial community cycling nutrients more efficiently, as the question is literally posed, the link to a reduced synthetic input is weakly or only indirectly supported: three lines of evidence (inoculants, free-living fixation, mineralisation) bound the claim, and none isolates the microbial term cleanly.
  conf: not stated · class: not stated · holds: a soil whose existing microbial community cycles nutrients efficiently; the inoculant evidence measures yield gain rather than input reduction at constant yield, free-living fixation is modest, and mineralisation rarely meets high-yield demand · src: schutzImprovingCropYield2018 (INDIRECT), ladhaBiologicalNitrogenFixation2022 (INDIRECT), stluceNitrogenDynamicsIndices2011 · trail: NFERT §Verdicts, §The weak channel · from: NFERT:A-005, NFERT:A-006, NFERT:B-0061, NFERT:B-0062 · rating: "WEAKLY / ONLY INDIRECTLY SUPPORTED" · contrary: not stated
- **fertiliser-substitution.6** No reviewed source isolates microbial-community efficiency from confounding soil and management variables as the cause of a reduced synthetic requirement at held yield.
  conf: not stated · class: search (note: "No reviewed source isolates") · holds: the sources this review gathered; its agronomy and soil-science evidence was retrieved by general web search · src: none (a statement about the reviewed sources) · trail: NFERT §Verdicts · from: NFERT:A-007, NFERT:B-0011 · search: searched, not found (note: "No reviewed source isolates microbial-community efficiency from confounding soil and management variables")

## Do not say
- **dns.1** "Manufacturing nitrogen fertiliser accounts for about 5% of global greenhouse-gas emissions."
  why: About 5% is the figure for the full life cycle including manure, while manufacturing is about 0.9% to 1.8% of global emissions, and the review calls quoting one figure as if it were another the most common error in this literature. · instead: emission-share.5, emission-share.9 · trail: NFERT §Share of emissions · from: NFERT:B-0049, NFERT:B-0050
- **dns.2** "Manufacturing nitrogen fertiliser accounts for about 2.1% of global greenhouse-gas emissions."
  why: About 2.1% is the figure for the synthetic-N supply chain, which adds field and transport emissions, while manufacturing is about 0.9% to 1.8%, and the review calls quoting one figure as if it were another the most common error in this literature. · instead: emission-share.5, emission-share.6 · trail: NFERT §Share of emissions · from: NFERT:B-0042, NFERT:B-0049, NFERT:B-0050
- **dns.3** "Efficient microbial nitrogen cycling in soil lowers the synthetic fertiliser a crop needs."
  why: The review names the hazard of attributing a reduced fertiliser requirement to microbial efficiency when the reduction co-varies with soil organic matter, moisture and management, and no reviewed source isolates microbial-community efficiency from these confounders as the cause of a reduced requirement at held yield. · instead: fertiliser-substitution.5, fertiliser-substitution.6, symbiotic-fixation.7 · trail: NFERT §Verdicts · from: NFERT:B-0008, NFERT:A-007
- **dns.4** "The review found that efficient microbial nitrogen cycling does not make fertiliser use more efficient."
  why: The review asked whether microbial cycling reduces synthetic input (a substitution question), not how efficiently fertiliser is used or how much is lost, and the note's integration read (2026-06-10) says its framing chased substitution and so reported a null against a claim about efficiency. · instead: gap.2 · trail: NFERT §Integration read · from: NFERT:B-0015, NFERT:B-0016, NFERT:B-0017

## Gaps
- **gap.1** No second reader checked this review. Its answers rest on the manufacturing figures (about 28 to 37 GJ and 1.6 to 2.8 t CO₂ per tonne of ammonia, about 1.9 to 3.4 t CO₂-equivalent per tonne of N), the emission shares (manufacture about 0.9% to 1.8% of global emissions, the synthetic-N supply chain about 2.1% of global and 10.6% of agricultural emissions, the full life cycle including manure about 5%), and for the second question on Anglade et al. 2015 and Ladha et al. 2022 for legume fixation, Schütz et al. 2018 for inoculants and St. Luce et al. 2011 for mineralisation.
  blocks: manufacturing-energy, manufacturing-co2, emission-share, symbiotic-fixation, fertiliser-substitution · origin: the note has no critique (it has an integration read, but no second reader's check of the figures) · search: not stated · from: NFERT:A-002, NFERT:A-003, NFERT:A-004, NFERT:A-006
- **gap.2** Whether the composition and functional state of the soil microbial community govern the fraction of applied N that is taken up versus lost (leaching, denitrification, N₂O), that is, nitrogen-use efficiency, at held input.
  blocks: nitrogen-use-efficiency · origin: the note's integration read (2026-06-10), which says the review answered a substitution question while the claim it was meant to serve is about N-use efficiency, and re-scopes the brief to the efficiency and loss question in a new brief (research_brief_BG2_biocircular_soil_efficiency) · search: not stated · trail: NFERT §Integration read · from: NFERT:B-0015, NFERT:B-0016, NFERT:B-0017, NFERT:B-0018, NFERT:B-0020
- **gap.3** A study that isolates microbial-community efficiency from confounding soil and management variables (organic matter, moisture or water, rotation, management) as the cause of a reduced synthetic requirement at held yield.
  blocks: fertiliser-substitution · origin: the review's own not-found result and the attribution hazard it names · search: searched, not found (note: "No reviewed source isolates microbial-community efficiency from confounding soil and management variables") · trail: NFERT §Verdicts · from: NFERT:A-007, NFERT:B-0008, NFERT:B-0073

## Out of scope

## Sources

```bibtex
@article{menegatGreenhouseGasEmissions2022,
  author  = {Menegat, Stefano and Ledo, Alicia and Tirado, Reyes},
  title   = {Greenhouse gas emissions from global production and use of nitrogen synthetic fertilisers in agriculture},
  journal = {Scientific Reports},
  year    = {2022},
  volume  = {12},
  number  = {1},
  pages   = {14490},
  doi     = {10.1038/s41598-022-18773-w},
  note    = {access: not stated; cited as: NFERT Menegat et al. 2022 (also as the source reporting the International Fertilizer Association's 2007 figure)}
}

@article{gaoGreenhouseGasEmissions2023,
  author  = {Gao, Yunhu and Cabrera Serrenho, Andr{\'e}},
  title   = {Greenhouse gas emissions from nitrogen fertilizers could be reduced by up to one-fifth of current levels by 2050 with combined interventions},
  journal = {Nature Food},
  year    = {2023},
  volume  = {4},
  number  = {2},
  pages   = {170--178},
  doi     = {10.1038/s43016-023-00698-w},
  note    = {access: not stated; cited as: NFERT Gao and Cabrera Serrenho 2023}
}

@article{tockThermoEnvironomicEvaluation2015,
  author  = {Tock, Laurence and Mar{\'e}chal, Fran{\c{c}}ois and Perrenoud, Marc},
  title   = {Thermo-environomic evaluation of the ammonia production},
  journal = {The Canadian Journal of Chemical Engineering},
  year    = {2015},
  volume  = {93},
  number  = {2},
  pages   = {356--362},
  doi     = {10.1002/cjce.22126},
  note    = {access: not stated; cited as: NFERT Tock et al. 2015}
}

@article{tunaTechnoEconomicAssessment2014,
  author  = {Tun{\aa}, Per and Hulteberg, Christian and Ahlgren, Serina},
  title   = {Techno-economic assessment of nonfossil ammonia production},
  journal = {Environmental Progress \& Sustainable Energy},
  year    = {2014},
  volume  = {33},
  number  = {4},
  pages   = {1290--1297},
  doi     = {10.1002/ep.11886},
  note    = {access: not stated; cited as: NFERT Tunå et al. 2014}
}

@article{demirhanSustainableAmmoniaProduction2019,
  author  = {Demirhan, C. Doga and Tso, William W. and Powell, Joseph B. and Pistikopoulos, Efstratios N.},
  title   = {Sustainable ammonia production through process synthesis and global optimization},
  journal = {AIChE Journal},
  year    = {2019},
  volume  = {65},
  number  = {7},
  pages   = {e16498},
  doi     = {10.1002/aic.16498},
  note    = {access: not stated; cited as: NFERT Demirhan et al. 2019}
}

@article{razonLifeCycleAnalysis2014,
  author  = {Razon, Luis F.},
  title   = {Life cycle analysis of an alternative to the Haber-Bosch process: Non-renewable energy usage and global warming potential of liquid ammonia from cyanobacteria},
  journal = {Environmental Progress \& Sustainable Energy},
  year    = {2014},
  volume  = {33},
  number  = {2},
  pages   = {618--624},
  doi     = {10.1002/ep.11817},
  note    = {access: not stated; cited as: NFERT Razon 2014}
}

@article{ladhaBiologicalNitrogenFixation2022,
  author  = {Ladha, Jagdish K. and Peoples, Mark B. and Reddy, Pallavolu M. and Biswas, Jatish C. and Bennett, Alan and Jat, Mangi L. and Krupnik, Timothy J.},
  title   = {Biological nitrogen fixation and prospects for ecological intensification in cereal-based cropping systems},
  journal = {Field Crops Research},
  year    = {2022},
  volume  = {283},
  pages   = {108541},
  doi     = {10.1016/j.fcr.2022.108541},
  note    = {access: not stated; cited as: NFERT Ladha et al. 2022}
}

@article{angladeRelationshipsEstimatingN22015,
  author  = {Anglade, Juliette and Billen, Gilles and Garnier, Josette},
  title   = {Relationships for estimating N2 fixation in legumes: incidence for N balance of legume-based cropping systems in Europe},
  journal = {Ecosphere},
  year    = {2015},
  volume  = {6},
  number  = {3},
  pages   = {37},
  doi     = {10.1890/ES14-00353.1},
  note    = {access: not stated; cited as: NFERT Anglade et al. 2015}
}

@article{schutzImprovingCropYield2018,
  author  = {Sch{\"u}tz, Lukas and Gattinger, Andreas and Meier, Matthias and M{\"u}ller, Adrian and Boller, Thomas and M{\"a}der, Paul and Mathimaran, Natarajan},
  title   = {Improving crop yield and nutrient use efficiency via biofertilization---A global meta-analysis},
  journal = {Frontiers in Plant Science},
  year    = {2018},
  volume  = {8},
  pages   = {2204},
  doi     = {10.3389/fpls.2017.02204},
  note    = {access: not stated; cited as: NFERT Schütz et al. 2018}
}

@incollection{stluceNitrogenDynamicsIndices2011,
  author    = {St. Luce, Mervin and Whalen, Joann K. and Ziadi, Noura and Zebarth, Bernie J.},
  title     = {Nitrogen dynamics and indices to predict soil nitrogen supply in humid temperate soils},
  booktitle = {Advances in Agronomy},
  publisher = {Academic Press},
  year      = {2011},
  volume    = {112},
  pages     = {55--102},
  doi       = {10.1016/B978-0-12-385538-1.00002-0},
  note      = {access: not stated; cited as: NFERT St. Luce et al. 2011}
}

@article{musExploringAlternativesBiological2018,
  author  = {Mus, Florence and Alleman, Alexander B. and Pence, Natasha and Seefeldt, Lance C. and Peters, John W.},
  title   = {Exploring the alternatives of biological nitrogen fixation},
  journal = {Metallomics},
  year    = {2018},
  volume  = {10},
  number  = {4},
  pages   = {523--538},
  doi     = {10.1039/c8mt00038g},
  note    = {background; not in the inputs; checked on Crossref and Europe PMC}
}
```
