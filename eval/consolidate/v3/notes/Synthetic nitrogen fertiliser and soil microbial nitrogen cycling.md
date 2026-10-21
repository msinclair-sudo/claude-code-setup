---
type: knowledge
title: Synthetic nitrogen fertiliser and soil microbial nitrogen cycling
inputs:
  - NFERT: PhD/Proposal/Research/Results/N-fertiliser_microbial-cycling_review.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-21
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
| NFERT | [[N-fertiliser_microbial-cycling_review]] | no | narrative author-year | no | no | fallback |

## Concepts

### haber-bosch: ammonia synthesis by the Haber-Bosch process
needs: none
- **haber-bosch.1** Ammonia synthesis runs through the Haber-Bosch process, which fixes atmospheric N₂ with hydrogen at high temperature and pressure; most of the energy and almost all of the carbon enter upstream, when hydrogen is stripped from natural gas or coal by steam reforming.
  conf: not stated · class: not stated · holds: ammonia manufacture from natural gas or coal · src: none (the reviewer's account; no source cited) · trail: NFERT §Energy per unit · from: NFERT:B-0022, NFERT:B-0023

### manufacturing-energy: energy per unit of ammonia and nitrogen
needs: haber-bosch
- **manufacturing-energy.1** Modern natural-gas plants need roughly 28 GJ per tonne of ammonia.
  conf: not stated · class: not stated · holds: modern natural-gas plants · src: tockThermoEnvironomicEvaluation2015, demirhanSustainableAmmoniaProduction2019 · trail: NFERT §Energy per unit · from: NFERT:B-0024
- **manufacturing-energy.2** The global average sits higher, near 37 GJ per tonne of ammonia, because older and coal-fed plants remain in service; coal-based production in China runs to about 59 GJ per tonne.
  conf: not stated · class: not stated · holds: the global plant mix; coal-based production in China · src: tunaTechnoEconomicAssessment2014 · trail: NFERT §Energy per unit · from: NFERT:B-0025
- **manufacturing-energy.3** Energy requirements fell from about 55 GJ per tonne of ammonia in the 1950s to the high-20s today.
  conf: not stated · class: not stated · holds: the 1950s to the present · src: tunaTechnoEconomicAssessment2014 · trail: NFERT §Energy per unit · from: NFERT:B-0026
- **manufacturing-energy.4** Ammonia carries 82% nitrogen by mass, so one tonne of N requires about 1.21 tonnes of ammonia; manufacturing one tonne of fertiliser N therefore costs roughly 34 GJ on the best natural-gas route and roughly 45 GJ at the global average.
  conf: not stated · class: deriv (note: "The conversion is arithmetic applied to the cited per-ammonia values") · holds: the reviewer's conversion of manufacturing-energy.1 and .2; not a separately measured quantity · src: none (the reviewer's conversion) · trail: NFERT §Energy per unit · from: NFERT:B-0027, NFERT:B-0028, NFERT:B-0029

### manufacturing-co2: carbon dioxide per unit of ammonia and nitrogen
needs: haber-bosch, manufacturing-energy
- **manufacturing-co2.1** Production CO₂ tracks the feedstock: modern natural-gas plants emit close to 1.6 t CO₂ per tonne of ammonia.
  conf: not stated · class: not stated · holds: modern natural-gas plants · src: tockThermoEnvironomicEvaluation2015 · trail: NFERT §Carbon dioxide per unit · from: NFERT:B-0030, NFERT:B-0031
- **manufacturing-co2.2** The ecoinvent inventory gives 1.92 t CO₂-equivalent per tonne of liquid ammonia alongside 41 GJ of primary energy.
  conf: not stated · class: not stated · holds: the ecoinvent inventory, as used by Razon (2014) · src: razonLifeCycleAnalysis2014 · trail: NFERT §Carbon dioxide per unit · from: NFERT:B-0032
- **manufacturing-co2.3** A process-optimisation study citing a global mix that includes coal reports about 2.8 t CO₂ per tonne of ammonia.
  conf: not stated · class: not stated · holds: a global plant mix including coal · src: demirhanSustainableAmmoniaProduction2019 · trail: NFERT §Carbon dioxide per unit · from: NFERT:B-0033
- **manufacturing-co2.4** Carbon capture on a natural-gas plant can bring the gate figure down to about 0.79 t CO₂ per tonne of ammonia.
  conf: not stated · class: not stated · holds: a natural-gas plant with carbon capture · src: tockThermoEnvironomicEvaluation2015 · trail: NFERT §Carbon dioxide per unit · from: NFERT:B-0034
- **manufacturing-co2.5** Per unit nitrogen, the manufacturing footprint is about 1.9 to 3.4 t CO₂-equivalent per tonne of N, the lower bound for efficient gas plants and the upper bound for coal-heavy mixes.
  conf: not stated · class: deriv (note: "Expressed per unit nitrogen") · holds: the reviewer's conversion of the per-ammonia figures · src: none (the reviewer's conversion of manufacturing-co2.1 to .3) · trail: NFERT §Carbon dioxide per unit · from: NFERT:B-0035
- **manufacturing-co2.6** Manufacture costs about 28 to 37 GJ and emits about 1.6 to 2.8 t CO₂ per tonne of ammonia, equivalently about 1.9 to 3.4 t CO₂-equivalent per tonne of N.
  conf: repl (note: "Independent industrial-ecology and biogeochemistry sources converge") · class: not stated · holds: the range spans Tock et al., Demirhan et al., Razon and Tunå et al. · src: tockThermoEnvironomicEvaluation2015, demirhanSustainableAmmoniaProduction2019, razonLifeCycleAnalysis2014, tunaTechnoEconomicAssessment2014 · trail: NFERT §Verdicts · from: NFERT:A-001, NFERT:A-002 · rating: "WELL-ESTABLISHED WITH QUANTIFIED FIGURES"
- **manufacturing-co2.7** These are cradle-to-gate manufacturing figures: they exclude the field N₂O released after application, which is the larger life-cycle term and belongs to use, not manufacture.
  conf: not stated · class: not stated · holds: cradle-to-gate system boundary · src: menegatGreenhouseGasEmissions2022, gaoGreenhouseGasEmissions2023 · trail: NFERT §Carbon dioxide per unit · from: NFERT:B-0036, NFERT:B-0037

### emission-share: share of agricultural and global emissions
needs: manufacturing-co2
- **emission-share.1** The share depends entirely on where the system boundary is drawn, and the three commonly cited figures answer three different questions.
  conf: not stated · class: not stated · holds: manufacture, supply chain and full life cycle · src: none (the reviewer's synthesis) · trail: NFERT §Share of emissions · from: NFERT:B-0038
- **emission-share.2** Manufacturing alone is the smallest slice: the International Fertilizer Association attributed 0.47 Gt CO₂-equivalent, about 0.93% of total anthropogenic emissions, to N fertiliser production in 2007.
  conf: not stated · class: not stated · holds: N fertiliser production, 2007 · src: menegatGreenhouseGasEmissions2022 (the IFA figure as reported in Menegat et al.) · trail: NFERT §Share of emissions · from: NFERT:B-0039, NFERT:B-0040
- **emission-share.3** Independent process studies place ammonia manufacture at roughly 1% to 1.8% of global greenhouse-gas emissions.
  conf: not stated · class: not stated · holds: ammonia manufacture · src: tunaTechnoEconomicAssessment2014, demirhanSustainableAmmoniaProduction2019, tockThermoEnvironomicEvaluation2015 · trail: NFERT §Share of emissions · from: NFERT:B-0041
- **emission-share.4** The full synthetic-N supply chain is larger because it adds field and transport emissions: Menegat et al. (2022) estimate 1.13 Gt CO₂-equivalent for 2018, equal to 10.6% of agricultural emissions and 2.1% of global emissions.
  conf: not stated · class: not stated · holds: synthetic-N supply chain, 2018 · src: menegatGreenhouseGasEmissions2022 · trail: NFERT §Share of emissions · from: NFERT:B-0042, NFERT:B-0043
- **emission-share.5** Within the supply-chain total, manufacture accounts for 38.8%, field emissions for 58.6% and transport for 2.6%: the use phase, not the factory, dominates.
  conf: not stated · class: not stated · holds: synthetic-N supply chain, 2018 · src: menegatGreenhouseGasEmissions2022 · trail: NFERT §Share of emissions · from: NFERT:B-0044, NFERT:B-0045
- **emission-share.6** The full nitrogen-fertiliser life cycle including manure is larger still: Gao and Cabrera Serrenho (2023) put production and use at about 5% of global greenhouse-gas emissions, roughly two-thirds occurring after deployment and one-third during production.
  conf: not stated · class: not stated · holds: full N-fertiliser life cycle, manure included · src: gaoGreenhouseGasEmissions2023 · trail: NFERT §Share of emissions · from: NFERT:B-0046, NFERT:B-0047
- **emission-share.7** Gao and Cabrera Serrenho report that manure emits about 23 t CO₂-equivalent per tonne of N, some 1.9 times an average synthetic fertiliser, because much of its nitrogen is lost.
  conf: not stated · class: not stated · holds: manure against an average synthetic fertiliser · src: gaoGreenhouseGasEmissions2023 · trail: NFERT §Share of emissions · from: NFERT:B-0048
- **emission-share.8** Manufacturing is about 0.9% to 1.8% of global emissions; the synthetic-N supply chain about 2.1% of global and 10.6% of agricultural emissions; the full life cycle including manure about 5% of global emissions.
  conf: repl (note: "Independent industrial-ecology and biogeochemistry sources converge") · class: not stated · holds: three system boundaries; the 0.9–1.8% range spans the IFA figure (via Menegat et al.) and the process studies · src: menegatGreenhouseGasEmissions2022, gaoGreenhouseGasEmissions2023, tunaTechnoEconomicAssessment2014, demirhanSustainableAmmoniaProduction2019, tockThermoEnvironomicEvaluation2015 · trail: NFERT §Verdicts, §Share of emissions · from: NFERT:A-001, NFERT:A-003, NFERT:B-0049 · rating: "WELL-ESTABLISHED WITH QUANTIFIED FIGURES"

### nue: nitrogen-use efficiency
needs: emission-share
- **nue.1** Gao and Cabrera Serrenho identify nitrogen-use efficiency as the single most effective mitigation lever for nitrogen-fertiliser emissions.
  conf: not stated · class: not stated · holds: the full N-fertiliser life cycle · src: gaoGreenhouseGasEmissions2023 · trail: NFERT §Share of emissions · from: NFERT:B-0048

### symbiotic-fixation: symbiotic biological nitrogen fixation (legumes and rhizobia)
needs: none
- **symbiotic-fixation.1** Legumes in symbiosis with rhizobia are the largest biological nitrogen input to cropping systems, and their effect on fertiliser demand is documented.
  conf: not stated · class: not stated · holds: cropping systems · src: ladhaBiologicalNitrogenFixation2022 · trail: NFERT §The strong, direct channel · from: NFERT:B-0054
- **symbiotic-fixation.2** In an organic legume-based rotation in Europe, 87% of total nitrogen inputs came from fixation, and the rotation matched conventional productivity at a surplus of only 21 kg N per hectare per year against 40 to 100 for fertilised systems.
  conf: not stated · class: not stated · holds: an organic legume-based rotation in Europe · src: angladeRelationshipsEstimatingN22015 · trail: NFERT §The strong, direct channel · from: NFERT:B-0055
- **symbiotic-fixation.3** Where humans deliberately add a nitrogen-fixing symbiosis, the reduction in synthetic input is real and direct: fixed nitrogen substitutes for applied nitrogen in the legume and partially enriches the following crop.
  conf: not stated · class: not stated · holds: deliberate legume inclusion · src: none (the reviewer's statement of the mechanism) · trail: NFERT §Question 2, §The strong, direct channel · from: NFERT:B-0052, NFERT:B-0056
- **symbiotic-fixation.4** The fraction of legume nitrogen derived from fixation varies enormously, from a few percent to nearly all, depending on species, soil mineral nitrogen and competition.
  conf: not stated · class: not stated · holds: legumes across species and soils · src: angladeRelationshipsEstimatingN22015, ladhaBiologicalNitrogenFixation2022 · trail: NFERT §The strong, direct channel · from: NFERT:B-0057, NFERT:B-0058
- **symbiotic-fixation.5** Fixation is suppressed by the very input it might replace: applying 125 to 250 kg fertiliser N per hectare cut fixation rates by 81% to 86%.
  conf: not stated · class: not stated · holds: one system reviewed by Ladha et al. (2022) · src: ladhaBiologicalNitrogenFixation2022 · trail: NFERT §The strong, direct channel · from: NFERT:B-0059
- **symbiotic-fixation.6** Symbiotic fixation and fertiliser are therefore partly substitutive, not additive, which caps the achievable saving.
  conf: not stated · class: not stated · holds: follows from symbiotic-fixation.5 · src: none (the reviewer's conclusion from symbiotic-fixation.5) · trail: NFERT §The strong, direct channel · from: NFERT:B-0060
- **symbiotic-fixation.7** For deliberate legume-based biological fixation, the reduction in synthetic input has strong direct evidence, bounded by wide variability in fixation fraction and by fertiliser suppression of fixation.
  conf: not stated · class: not stated · holds: deliberate legume-based fixation · src: angladeRelationshipsEstimatingN22015, ladhaBiologicalNitrogenFixation2022 · trail: NFERT §Verdicts · from: NFERT:A-004 · rating: "ESTABLISHED BUT QUALIFIED"

### free-living-fixation: free-living and associative diazotrophs
needs: none
- **free-living-fixation.1** Free-living and associative diazotrophs are ubiquitous and do fix nitrogen, but their measured contribution in cereal systems is modest, and engineering cereals to fix their own nitrogen remains unrealised.
  conf: not stated · class: not stated · holds: cereal systems · src: ladhaBiologicalNitrogenFixation2022 · trail: NFERT §The weak channel · from: NFERT:B-0063
- **free-living-fixation.2** Their support for a reduced fertiliser requirement is indirect: the fixed quantities are rarely large enough to displace a defined fertiliser rate at constant yield.
  conf: not stated · class: not stated · holds: cereal systems, constant yield · src: ladhaBiologicalNitrogenFixation2022 (INDIRECT) · trail: NFERT §The weak channel, §Verdicts · from: NFERT:B-0064, NFERT:A-006

### inoculants: microbial inoculants (biofertilisers)
needs: none
- **inoculants.1** Microbial inoculants raise yield inconsistently: the largest meta-analysis, spanning 171 field studies, found yield responses of +8.5% in continental climates, +10.0% in oceanic, +14.9% in tropical and +20.0% in dry climates, with effects described as often inconsistent and dependent on soil phosphorus and climate.
  conf: not stated · class: not stated · holds: 171 field studies, by climate · src: schutzImprovingCropYield2018 · trail: NFERT §The weak channel · from: NFERT:B-0065, NFERT:B-0066
- **inoculants.2** The inoculant evidence is indirect for the substitution question, because it measures yield gain at a given input rather than input reduction at a held yield.
  conf: not stated · class: not stated · holds: yield gain at a given input; not input reduction at held yield · src: schutzImprovingCropYield2018 (INDIRECT) · trail: NFERT §The weak channel, §Verdicts · from: NFERT:B-0067, NFERT:A-006

### mineralisation: nitrogen mineralisation by the resident community
needs: none
- **mineralisation.1** Mineralisation by the resident community supplies nitrogen, but rarely enough: only about 1% to 4% of soil organic nitrogen is mineralised in a season, and mineralisation alone is seldom sufficient to reach the maximum yield of modern cultivars, so additional fertiliser or organic nitrogen is needed.
  conf: not stated · class: not stated · holds: one season; modern cultivars · src: stluceNitrogenDynamicsIndices2011 · trail: NFERT §The weak channel, §Verdicts · from: NFERT:B-0068, NFERT:B-0069, NFERT:A-006
- **mineralisation.2** Quantifying soil nitrogen supply can improve fertiliser-use efficiency and trim rates, but the lever is the measured soil supply, not a demonstrated property of microbial-community efficiency.
  conf: not stated · class: not stated · holds: stated by the reviewer after St. Luce et al. · src: stluceNitrogenDynamicsIndices2011 · trail: NFERT §The weak channel · from: NFERT:B-0070

### substitution: whether microbial nitrogen cycling reduces synthetic input at constant yield
needs: symbiotic-fixation, free-living-fixation, inoculants, mineralisation
- **substitution.1** Whether microbial nitrogen cycling reduces synthetic input splits along a clear line: the reduction is real and direct where humans deliberately add a nitrogen-fixing symbiosis, and the support is mostly indirect where the claim rests on the resident free-living community cycling nitrogen more efficiently.
  conf: not stated · class: not stated · holds: the sources reviewed for Question 2 · src: angladeRelationshipsEstimatingN22015, ladhaBiologicalNitrogenFixation2022, schutzImprovingCropYield2018, stluceNitrogenDynamicsIndices2011 · trail: NFERT §Question 2, §Verdicts · from: NFERT:A-004, NFERT:B-0051, NFERT:B-0052, NFERT:B-0053 · rating: "SPLIT"
- **substitution.2** For the resident microbial community cycling nutrients more efficiently, as the question is literally posed, the link to reduced synthetic input is weakly or only indirectly supported: three lines of evidence (free-living fixation, inoculants, mineralisation) bound it, and none isolates the microbial term cleanly.
  conf: not stated · class: not stated · holds: a soil whose existing microbial community cycles nutrients efficiently · src: ladhaBiologicalNitrogenFixation2022 (INDIRECT), schutzImprovingCropYield2018 (INDIRECT), stluceNitrogenDynamicsIndices2011 · trail: NFERT §The weak channel, §Verdicts · from: NFERT:A-005, NFERT:B-0061, NFERT:B-0062 · rating: "WEAKLY / ONLY INDIRECTLY SUPPORTED"
- **substitution.3** No reviewed source isolates microbial-community efficiency from confounding soil and management variables as the cause of a reduced synthetic requirement at held yield.
  conf: not stated · class: search (note: "No reviewed source isolates microbial-community efficiency") · holds: the sources the review read · src: none (a statement about what the review found) · trail: NFERT §Verdicts · from: NFERT:A-007
- **substitution.4** Attribution is the first failure mode: reduced fertiliser need co-varies with organic matter, water and rotation (soil organic matter, moisture and management), so the microbial contribution is hard to separate.
  conf: not stated · class: not stated · holds: the Question 2 evidence · src: none (the reviewer's synthesis) · trail: NFERT §Where the evidence sits · from: NFERT:B-0008, NFERT:B-0072, NFERT:B-0073
- **substitution.5** Suppression is the second failure mode: adding fertiliser depresses fixation, bounding the saving.
  conf: not stated · class: not stated · holds: symbiotic fixation (symbiotic-fixation.5) · src: none (the reviewer's synthesis) · trail: NFERT §Where the evidence sits · from: NFERT:B-0074
- **substitution.6** Magnitude is the third failure mode: free-living fixation and mineralisation seldom meet high-yield demand, so the resident community supplements rather than replaces synthetic nitrogen.
  conf: not stated · class: not stated · holds: high-yield demand · src: none (the reviewer's synthesis of free-living-fixation and mineralisation) · trail: NFERT §Where the evidence sits · from: NFERT:B-0075
- **substitution.7** The strongest evidence for reduced synthetic input is agronomic and concerns legume inclusion, a deliberate management choice, not the spontaneous efficiency of a resident community.
  conf: not stated · class: not stated · holds: the Question 2 evidence · src: angladeRelationshipsEstimatingN22015, ladhaBiologicalNitrogenFixation2022 · trail: NFERT §Where the evidence sits · from: NFERT:B-0071

## Do not say

- **dns.1** One emission-share figure quoted as if it were another (the 2.1% supply-chain or 5% life-cycle figure given as the manufacturing share, or the reverse).
  why: the note: the three figures answer three different questions, and quoting one as if it were another is the most common error in this literature · instead: emission-share.8, emission-share.1 · trail: NFERT §Share of emissions · from: NFERT:B-0038, NFERT:B-0050
- **dns.2** A reduced fertiliser requirement attributed to microbial efficiency where the reduction co-varies with soil organic matter, moisture and management.
  why: the note names this as the hazard throughout Question 2: constant conjunction is not causation · instead: substitution.3, substitution.4 · trail: NFERT §Synthetic nitrogen fertiliser · from: NFERT:B-0007, NFERT:B-0008
- **dns.3** "Efficient microbial nitrogen cycling in soil reduces the synthetic nitrogen a crop needs", stated of the resident community as shown.
  why: weakly or only indirectly supported, and no reviewed source isolates the microbial term; the integration read keeps the finding as useful "to not overclaim" · instead: substitution.2, substitution.3 · trail: NFERT §Verdicts, §Integration read · from: NFERT:A-005, NFERT:A-007, NFERT:B-0018
- **dns.4** The review's weak support for substitution given as an answer on nitrogen-use efficiency (whether microbial cycling governs how much applied nitrogen is lost).
  why: the integration read: Q2 answered the substitution question, and so reported a null against a claim the proposal does not make; the efficiency/loss question was not researched · instead: none · trail: NFERT §Integration read · from: NFERT:B-0015, NFERT:B-0016, NFERT:B-0017

## Gaps

- **gap.1** The review was never checked by a second reader against its sources: no critique ran. The answers rest on 28–37 GJ and 1.6–2.8 t CO₂ per tonne of ammonia and 1.9–3.4 t CO₂-equivalent per tonne of N (Tock, Demirhan, Razon, Tunå); 0.9–1.8%, 2.1% (10.6% of agricultural) and 5% of global emissions (IFA via Menegat, process studies, Menegat, Gao); 87% of inputs from fixation and a 21 against 40–100 kg N/ha/yr surplus (Anglade); 81–86% suppression of fixation (Ladha); +8.5% to +20.0% inoculant yield responses (Schütz); 1–4% of soil organic N mineralised per season (St. Luce).
  blocks: manufacturing-co2, emission-share, symbiotic-fixation, inoculants, mineralisation, substitution · origin: no critique; the owner's integration read judged scope, not figures · src: tockThermoEnvironomicEvaluation2015, demirhanSustainableAmmoniaProduction2019, razonLifeCycleAnalysis2014, tunaTechnoEconomicAssessment2014, menegatGreenhouseGasEmissions2022, gaoGreenhouseGasEmissions2023, angladeRelationshipsEstimatingN22015, ladhaBiologicalNitrogenFixation2022, schutzImprovingCropYield2018, stluceNitrogenDynamicsIndices2011
- **gap.2** Does the composition and functional state of the soil microbial community govern the fraction of applied N that is taken up versus lost (leaching, denitrification, N₂O), i.e. nitrogen-use efficiency, at held input?
  blocks: nue · origin: the owner's integration read re-scopes Question 2 to this efficiency/loss question (new brief BG2) · from: NFERT:B-0016, NFERT:B-0018, NFERT:B-0019, NFERT:B-0020
- **gap.3** A study isolating microbial-community efficiency from confounding soil and management variables as the cause of a reduced synthetic requirement at held yield.
  blocks: substitution · origin: "not found" · from: NFERT:A-007, NFERT:B-0062
- **gap.4** Input reduction at held yield from microbial inoculants: the meta-analytic evidence measures yield gain at a given input.
  blocks: inoculants · origin: the evidence found measures a different quantity · src: schutzImprovingCropYield2018 · from: NFERT:B-0067

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
  note    = {access: not stated; cited as: NFERT, Menegat et al. 2022 (the integration read calls it menegat2022)}
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
  note    = {access: not stated; cited as: NFERT, Gao and Cabrera Serrenho 2023 (the integration read calls it gao2023)}
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
  note    = {access: not stated; cited as: NFERT, Tock et al. 2015}
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
  note    = {access: not stated; cited as: NFERT, Tunå et al. 2014}
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
  note    = {access: not stated; cited as: NFERT, Demirhan et al. 2019}
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
  note    = {access: not stated; cited as: NFERT, Razon 2014}
}

@article{ladhaBiologicalNitrogenFixation2022,
  author  = {Ladha, Jagdish K. and Peoples, Mark B. and Reddy, Pallavolu M. and Biswas, Jatish C. and Bennett, Alan and Jat, Mangi L. and Krupnik, Timothy J.},
  title   = {Biological nitrogen fixation and prospects for ecological intensification in cereal-based cropping systems},
  journal = {Field Crops Research},
  year    = {2022},
  volume  = {283},
  pages   = {108541},
  doi     = {10.1016/j.fcr.2022.108541},
  note    = {access: not stated; cited as: NFERT, Ladha et al. 2022}
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
  note    = {access: not stated; cited as: NFERT, Anglade et al. 2015}
}

@article{schutzImprovingCropYield2018,
  author  = {Sch{\"u}tz, Lukas and Gattinger, Andreas and Meier, Matthias and M{\"u}ller, Adrian and Boller, Thomas and M{\"a}der, Paul and Mathimaran, Natarajan},
  title   = {Improving crop yield and nutrient use efficiency via biofertilization---A global meta-analysis},
  journal = {Frontiers in Plant Science},
  year    = {2018},
  volume  = {8},
  pages   = {2204},
  doi     = {10.3389/fpls.2017.02204},
  note    = {access: not stated; cited as: NFERT, Schütz et al. 2018}
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
  note      = {access: not stated; cited as: NFERT, St. Luce et al. 2011}
}
```
