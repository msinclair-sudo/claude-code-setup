---
type: knowledge
title: Stepwise denitrification and N2O output in constraint-based models
inputs:
  - C-STEPDEN: PhD/Proposal/Research/Results/Stepwise Denitrification with N2O Output in Constraint-Based Metabolic Models.md
refs: PhD/Proposal/Refs/Refs.bib
built: 2026-10-24
status: draft
tags:
  - research
  - knowledge
---

# Stepwise denitrification and N2O output in constraint-based models

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
| C-STEPDEN | [[Stepwise Denitrification with N2O Output in Constraint-Based Metabolic Models]] | no | narrative author-year | no | no | fallback (answers and critique; the note has no labelled citations) |

## Concepts

### denitrification-pathway: the four-step denitrification pathway
needs: none

- **denitrification-pathway.1** The denitrification pathway is a four-step dissimilatory reduction, NO₃⁻→NO₂⁻→NO→N₂O→N₂, catalysed by nitrate reductase (Nar/Nap), nitrite reductase (NirK/NirS), nitric oxide reductase (cNor/qNor, norBC) and nitrous oxide reductase (NosZ).
  conf: not stated · class: not stated · holds: the full canonical heterotrophic chain, as the review describes it; no organism named · src: none (the note cites no source for it) · trail: C-STEPDEN §What · from: C-STEPDEN:B-0007, C-STEPDEN:B-0020
- **denitrification-pathway.2** The four-step reduction consumes 10 electrons per two nitrate ions converted to dinitrogen.
  conf: not stated · class: not stated · holds: the full pathway from nitrate to dinitrogen · src: none (the note cites no source for it) · trail: C-STEPDEN §What · from: C-STEPDEN:B-0020

### constraint-based-model: constraint-based (FBA) models and the kinetic boundary
needs: denitrification-pathway

- **constraint-based-model.bg1** Flux balance analysis (FBA) is a mathematical approach for analysing the flow of metabolites through a metabolic network: the network's stoichiometry, as mass balances at steady state, constrains the fluxes, and linear programming finds the flux distribution that optimises a stated biological objective, such as biomass production when growth is predicted.
  kind: background · ref: orthWhatFluxBalance2010 · check: DOI 10.1038/nbt.1614 resolves on Crossref (Orth, Thiele and Palsson 2010, Nature Biotechnology 28(3):245-248); the definition is the abstract's first sentence, and the steady-state mass balance, linear programming and biomass objective are stated in the main text (read in PMC3108565)
- **constraint-based-model.1** In constraint-based modelling, the four denitrification reactions can in principle be encoded as separate fluxes balanced against an electron donor pool (NADH/quinone) with proton translocation.
  conf: not stated · class: not stated · holds: stated as possible in principle, for the pathway NO₃⁻→NO₂⁻→NO→N₂O→N₂ · src: none (the reviewer's synthesis) · trail: C-STEPDEN §What · from: C-STEPDEN:B-0020..0021
- **constraint-based-model.2** The boundary between "constraint-based" and "kinetic" models is occasionally blurred in the literature (for example dynamic FBA and cybernetic models); the review classified each model by whether its core engine is stoichiometric LP optimization (FBA family) or rate-equation integration (kinetic/ODE family).
  conf: not stated · class: not stated · holds: the classification used throughout the review · src: none (the reviewer's method statement) · trail: C-STEPDEN §Caveats · from: C-STEPDEN:B-0073
- **constraint-based-model.3** Standard FBA biomass-maximization does not naturally predict byproduct (N-oxide) overflow without additional constraints, a general limitation noted across the byproduct-secretion modelling literature.
  conf: not stated · class: not stated · holds: standard FBA with a biomass-maximization objective; the note names no specific study · src: none (the note names the byproduct-secretion modelling literature without a reference) · trail: C-STEPDEN §How stepwise · from: C-STEPDEN:B-0044

### kinetic-trait-models: kinetic/ODE, cybernetic and trait-based models of denitrification
needs: denitrification-pathway, constraint-based-model

- **kinetic-trait-models.1** Stepwise denitrification with N₂O as an explicit intermediate or terminal product is resolved in the kinetic/ODE and trait-based modelling families (the Activated Sludge Model for Nitrogen, electron-competition models, the cybernetic models of Song & Liu, the Kampschreur Agrobacterium model, and the PNAS/bioRxiv OMZ modular-denitrification ecosystem model); these are not constraint-based FBA models.
  conf: not stated · class: not stated · holds: kinetic/ODE, cybernetic and trait-based families, not FBA · src: hiattUpdatedProcessModel2008, pan, songDynamicMetabolicModeling2015, songRegulationStructuredDynamicMetabolic2017, kampschreurMetabolicModelingDenitrification2012, zakemEcologicalDynamicsModular2024, zakemEcologicalDynamicsExplain2024 · trail: C-STEPDEN §TL;DR, §Key Findings · rating: "well established" · from: C-STEPDEN:B-0009, C-STEPDEN:B-0018..0019
- **kinetic-trait-models.2** The Activated Sludge Model for Nitrogen (ASMN; Hiatt & Grady, 2008) "incorporates four-step denitrification (sequential reduction of nitrate to nitrogen gas via nitrite, nitric oxide, and nitrous oxide) using individual, reaction-specific parameters."
  conf: not stated · class: not stated · holds: an activated sludge process model (Water Environment Research 80(11):2145–2156), outside the FBA/constraint-based family · src: hiattUpdatedProcessModel2008 · trail: C-STEPDEN §Bounding · from: C-STEPDEN:B-0018, C-STEPDEN:B-0047
- **kinetic-trait-models.3** Electron-competition models (Pan et al., ES&T) explicitly model competition among the four denitrification steps for electrons to predict N₂O accumulation.
  conf: not stated · class: not stated · holds: kinetic models, outside the FBA/constraint-based family · src: pan · trail: C-STEPDEN §Bounding · from: C-STEPDEN:B-0047..0048, C-STEPDEN:B-0065
- **kinetic-trait-models.4** The cybernetic models of Song & Liu (2015, Ind. Eng. Chem. Res.) and Song et al. (2017, Frontiers in Microbiology) resolve sequential N-oxide intermediates with dynamic regulation.
  conf: not stated · class: not stated · holds: cybernetic dynamic metabolic models of denitrifying bacterial growth, outside the FBA/constraint-based family · src: songDynamicMetabolicModeling2015, songRegulationStructuredDynamicMetabolic2017 · trail: C-STEPDEN §Bounding · from: C-STEPDEN:B-0047, C-STEPDEN:B-0049..0050, C-STEPDEN:B-0105
- **kinetic-trait-models.5** The Kampschreur et al. (2012) Agrobacterium tumefaciens model resolves Nap/NirK/NorB with transcriptional/kinetic regulation and reproduces NO/N₂O emission from incomplete pathway expression; it is a kinetic ODE network, not FBA.
  conf: not stated · class: model (note: "reproduces NO/N₂O emission") · holds: Agrobacterium tumefaciens; a kinetic ODE metabolic network · src: kampschreurMetabolicModelingDenitrification2012 · trail: C-STEPDEN §Bounding · from: C-STEPDEN:B-0051
- **kinetic-trait-models.6** The review's model index gives the Agrobacterium tumefaciens model's N₂O mechanism as "incomplete/unbalanced enzyme expression during oxic-anoxic transition", and lists its sub-steps (Nap, NirK, NorB; regulation) as resolved.
  conf: not stated · class: not stated · holds: Agrobacterium tumefaciens; framework given as KINETIC/ODE metabolic network (not FBA) · src: kampschreurMetabolicModelingDenitrification2012 · trail: C-STEPDEN §Compact JSON · from: C-STEPDEN:B-0074
- **kinetic-trait-models.7** The Domingo-Félez & Smets NDHA model and ASM3-based extensions are pseudo-mechanistic ODE models.
  conf: not stated · class: not stated · holds: outside the FBA/constraint-based family · src: domingofelez · trail: C-STEPDEN §Bounding · from: C-STEPDEN:B-0047, C-STEPDEN:B-0052
- **kinetic-trait-models.8** Zakem and colleagues (PNAS 2024, "Ecological dynamics explain modular denitrification in the ocean"; bioRxiv 2024.09.25.615058) model the modular pathway NO₃⁻→NO₂⁻→N₂O→N₂, neglecting NO, using redox thermodynamics, biomass-yield traits and resource-competition theory; trait-based/thermodynamic ecosystem models like this resolve denitrification modules and N₂O ecologically, not via FBA.
  conf: not stated · class: not stated · holds: ocean (OMZ) denitrifier functional types; NO not represented · src: zakemEcologicalDynamicsModular2024, zakemEcologicalDynamicsExplain2024 · trail: C-STEPDEN §Bounding · from: C-STEPDEN:B-0053, C-STEPDEN:B-0074
- **kinetic-trait-models.9** Zakem and colleagues note that ocean biogeochemical models traditionally collapse denitrification into a single step, and that microbes carry only subsets ("modules") of the full pathway.
  conf: not stated · class: not stated · holds: ocean biogeochemical models; denitrifying microbes in the ocean · src: zakemEcologicalDynamicsModular2024, zakemEcologicalDynamicsExplain2024 · trail: C-STEPDEN §Bounding · from: C-STEPDEN:B-0053
- **kinetic-trait-models.10** In the Zakem modular-denitrification model, N₂O cycling emerges from community-level niche partitioning: one functional type does NO₃⁻→NO₂⁻, another N₂O→N₂.
  conf: not stated · class: not stated · holds: a trait-based ocean ecosystem model of denitrifier functional types · src: zakemEcologicalDynamicsModular2024, zakemEcologicalDynamicsExplain2024 · trail: C-STEPDEN §Bounding · from: C-STEPDEN:B-0053..0054
- **kinetic-trait-models.11** The Zakem model is the conceptual realization of the user's "community-level pathway gaps" mechanism, but implemented as a trait-based ecosystem model, not a stoichiometric/constraint-based GEM.
  conf: not stated · class: not stated · holds: the review's comparison with the user's mechanism · src: zakemEcologicalDynamicsModular2024, zakemEcologicalDynamicsExplain2024 · trail: C-STEPDEN §Bounding · from: C-STEPDEN:B-0053, C-STEPDEN:B-0055
- **kinetic-trait-models.12** The body of work that resolves all four steps with N₂O as an accumulating or terminal product, driven by missing or inhibited NosZ, electron competition, or community pathway gaps, lives in kinetic/ODE, cybernetic and trait-based ecosystem modelling, not in the FBA/constraint-based stoichiometric family; these families already deliver stepwise N₂O (ASMN, electron-competition models, Song & Liu, Kampschreur, Zakem et al. 2024).
  conf: not stated · class: not stated · holds: the review's grouping of the cases it located · src: hiattUpdatedProcessModel2008, pan, songDynamicMetabolicModeling2015, kampschreurMetabolicModelingDenitrification2012, zakemEcologicalDynamicsModular2024 · trail: C-STEPDEN §How the cases, §Recommendations · contrary: not stated · from: C-STEPDEN:B-0056, C-STEPDEN:B-0059, C-STEPDEN:B-0065..0066

### nitrifier-denitrification-models: constraint-based models of nitrifier denitrification
needs: constraint-based-model

- **nitrifier-denitrification-models.1** Perez-Garcia et al. (2014) built a stoichiometric metabolic network (SMN) of Nitrosomonas europaea energy metabolism (51 reactions, 44 metabolites) and used FBA to quantify NO and N₂O production through two distinct routes, the hydroxylamine-oxidation pathway and nitrifier denitrification (NO₂⁻→NO→N₂O via NirK and NorB).
  conf: not stated · class: model (note: "used FBA to quantify NO and N₂O production") · holds: N. europaea energy metabolism, an ammonia-oxidizing bacterium · src: perezgarciaClarifyingRegulationNO2014 (full-text Methods/reaction tables partially inaccessible; reaction counts and mechanisms corroborated from abstracts, verbatim snippets and the companion 2016 paper) · trail: C-STEPDEN §Key Findings, §What · from: C-STEPDEN:B-0006, C-STEPDEN:B-0010, C-STEPDEN:B-0023, C-STEPDEN:B-0069..0070
- **nitrifier-denitrification-models.2** In the Perez-Garcia SMN, N₂O is an explicit output and, because N. europaea lacks nosZ, necessarily a terminal product.
  conf: not stated · class: not stated · holds: N. europaea, which has no nosZ · src: perezgarciaClarifyingRegulationNO2014 · trail: C-STEPDEN §Key Findings, §What · from: C-STEPDEN:B-0010..0011, C-STEPDEN:B-0023..0024
- **nitrifier-denitrification-models.3** The Perez-Garcia SMN is the clearest case where FBA quantifies NO and N₂O as distinct products through resolved enzymatic reactions (NirK, NorB, cytochrome P460, cytochrome aa3, HAO).
  conf: not stated · class: not stated · holds: N. europaea SMN (51 reactions, 44 metabolites) · src: perezgarciaClarifyingRegulationNO2014 · trail: C-STEPDEN §What · from: C-STEPDEN:B-0023
- **nitrifier-denitrification-models.4** The Perez-Garcia SMN was validated against measured yield ratios: "These estimates matched well, deviating on average by 15% from values for 17 M yield ratios reported for non-limiting oxygen and ammonium concentrations."
  conf: not stated · class: model/meas (note: "validated against measured yield ratios") · holds: 17 M yield ratios under non-limiting oxygen and ammonium concentrations; N. europaea · src: perezgarciaClarifyingRegulationNO2014 · trail: C-STEPDEN §What · from: C-STEPDEN:B-0023, C-STEPDEN:B-0026
- **nitrifier-denitrification-models.5** Perez-Garcia et al. (2016, Biotechnology and Bioengineering) extended this lineage to a multispecies metabolic network that "captures the nitrogen respiratory pathways inferred from genomes of eight AOB and NOB species," resolving specific NO redox reactions (NirK, CytP460, cytochrome c554, flavohemoglobins, cNor).
  conf: not stated · class: not stated · holds: eight AOB and NOB species, pathways inferred from genomes · src: perezgarciaAssessmentNitricOxide2016 · trail: C-STEPDEN §What · from: C-STEPDEN:B-0027
- **nitrifier-denitrification-models.6** In the 2016 multispecies network, "Simulations showed that NO oxidation to NO2(-) decreased N2O formation by 60% without changing culture's NO2(-) production rate."
  conf: not stated · class: model (note: "Simulations showed") · holds: simulations of the eight-species AOB/NOB metabolic network during nitrification · src: perezgarciaAssessmentNitricOxide2016 · trail: C-STEPDEN §What · from: C-STEPDEN:B-0027, C-STEPDEN:B-0084
- **nitrifier-denitrification-models.7** The review's model index gives the 2016 multispecies network's N₂O mechanism as "NO redox balance; CytP460 reduces N2O by 60%", with N₂O explicit and sub-steps partly resolved (NO redox reactions, NirK, CytP460, cNor).
  conf: not stated · class: not stated · holds: eight AOB/NOB species; stoichiometric network with FBA · src: perezgarciaAssessmentNitricOxide2016 · trail: C-STEPDEN §Compact JSON · from: C-STEPDEN:B-0074
- **nitrifier-denitrification-models.8** The Mellbye et al. (2018) coculture model tracks NO, NO₂ and N₂O as separate N-oxide species, and is the closest community-level and strongest community-scale constraint-based demonstration of explicit N₂O output.
  conf: not stated · class: not stated · holds: a coculture of N. europaea and N. winogradskyi · src: mellbyeGenomeScaleConstraintBased2018 (full-text Methods/reaction tables partially inaccessible; facts corroborated from abstracts, verbatim snippets and the Methods text recovered) · trail: C-STEPDEN §Key Findings, §What · from: C-STEPDEN:B-0013, C-STEPDEN:B-0028..0029, C-STEPDEN:B-0061, C-STEPDEN:B-0069..0070
- **nitrifier-denitrification-models.9** The Mellbye coculture model integrates two genome-scale reconstructions, iFC578 for N. europaea and iFC579 for N. winogradskyi, with abiotic NO-oxidation reactions in gas and aqueous phases.
  conf: not stated · class: not stated · holds: N. europaea and N. winogradskyi coculture · src: mellbyeGenomeScaleConstraintBased2018 · trail: C-STEPDEN §Key Findings, §What · from: C-STEPDEN:B-0013, C-STEPDEN:B-0029
- **nitrifier-denitrification-models.10** In the Mellbye model N₂O production is tied to the presence of a NOR-encoding gene: "The genome-scale model also does not consider the minute N2O production observed by N. winogradskyi, since its genome does not contain any known NOR-encoding gene," an explicit gene-content rationale for emission.
  conf: not stated · class: not stated · holds: N. winogradskyi, whose genome has no known NOR-encoding gene · src: mellbyeGenomeScaleConstraintBased2018 · trail: C-STEPDEN §Key Findings, §What · from: C-STEPDEN:B-0014, C-STEPDEN:B-0030
- **nitrifier-denitrification-models.11** The Mellbye model attributes elevated coculture N-oxide emission to a microaerobic environment created by coupled metabolism, when the O₂ demand of ammonia oxidation is exacerbated by NOB activity.
  conf: not stated · class: not stated · holds: the N. europaea and N. winogradskyi coculture · src: mellbyeGenomeScaleConstraintBased2018 · trail: C-STEPDEN §Key Findings, §What · from: C-STEPDEN:B-0015, C-STEPDEN:B-0031
- **nitrifier-denitrification-models.12** The iFC578 and iFC579 reconstructions were "based upon the Department of Energy (DOE) Joint Genome Institute (JGI) sequences… with automatic annotation and model building through the SEED… followed by hand annotation using the Kyoto Encyclopedia of Genes and Genomes (KEGG) database," and were "calibrated either to maximize biomass production or energy substrate uptake."
  conf: not stated · class: not stated · holds: the Methods of the Mellbye coculture model · src: mellbyeGenomeScaleConstraintBased2018 (Methods text recovered) · trail: C-STEPDEN §What · from: C-STEPDEN:B-0032, C-STEPDEN:B-0070
- **nitrifier-denitrification-models.13** The integrated Mellbye coculture model is posted at github.com/chaplenf/microBiome-v2.1.
  conf: not stated · class: not stated · holds: microBiome-v2.1, the integrated iFC578 and iFC579 model · src: mellbyeGenomeScaleConstraintBased2018 · trail: C-STEPDEN §What, §Recommendations · from: C-STEPDEN:B-0033, C-STEPDEN:B-0061
- **nitrifier-denitrification-models.14** The review's model index classes the iFC578 + iFC579 coculture model (microBiome-v2.1) as genome-scale dynamic FBA with abiotic reactions (SEED/KEGG), its N₂O mechanism as microaerobic conditions and NOR gene presence.
  conf: not stated · class: not stated · holds: N. europaea and Nitrobacter winogradskyi coculture · src: mellbyeGenomeScaleConstraintBased2018 · trail: C-STEPDEN §Compact JSON · from: C-STEPDEN:B-0074
- **nitrifier-denitrification-models.15** Perez-Garcia et al. (2014) and Mellbye et al. (2018) are the only published FBA/stoichiometric models the review located that emit N₂O as a distinct flux, and the Mellbye model is the only community-scale one.
  conf: not stated · class: search (note: "the only published FBA/stoichiometric models located") · search: searched, not found (note: "the only published FBA/stoichiometric models located") · holds: published FBA/stoichiometric models located by the review's search · src: perezgarciaClarifyingRegulationNO2014, mellbyeGenomeScaleConstraintBased2018 · trail: C-STEPDEN §Recommendations · from: C-STEPDEN:B-0060..0061
- **nitrifier-denitrification-models.16** The 2022 iGC535 reconstruction of N. europaea (Canto-Encalada et al., PLoS Computational Biology), a substantially re-curated successor in this lineage, reached over 90% prediction accuracy, predicting growth and oxygen uptake rates with 90.52% accuracy under chemolithotrophic and chemolithoorganotrophic conditions.
  conf: not stated · class: not stated · holds: N. europaea under chemolithotrophic and chemolithoorganotrophic conditions; growth and oxygen uptake rates · src: cantoencaladaFluxBalanceAnalysis2022 · trail: C-STEPDEN §What · from: C-STEPDEN:B-0035
- **nitrifier-denitrification-models.17** The review's model index records iGC535 (N. europaea ATCC19718, genome-scale FBA in COBRA) as not resolving the N-oxide sub-steps, its focus being pollutant oxidation and growth, and as having no explicit N₂O output.
  conf: not stated · class: not stated · holds: N. europaea ATCC19718 · src: cantoencaladaFluxBalanceAnalysis2022 · trail: C-STEPDEN §Compact JSON · from: C-STEPDEN:B-0074

### electron-overflow: N2O emission as electron overflow
needs: nitrifier-denitrification-models

- **electron-overflow.1** Perez-Garcia et al. (2014) found that "NO and N2O are emitted when the sum of their production rates is greater than half the rate of NO oxidation by cytochrome P460."
  conf: not stated · class: model (note: "in these models") · holds: the N. europaea SMN · src: perezgarciaClarifyingRegulationNO2014 · trail: C-STEPDEN §Key Findings · from: C-STEPDEN:B-0010, C-STEPDEN:B-0012
- **electron-overflow.2** Perez-Garcia et al. (2014) found that "N2O is produced due to electron flow imbalances in the cell."
  conf: not stated · class: model (note: "in these models") · holds: the N. europaea SMN · src: perezgarciaClarifyingRegulationNO2014 · trail: C-STEPDEN §Key Findings · from: C-STEPDEN:B-0010, C-STEPDEN:B-0012
- **electron-overflow.3** Perez-Garcia et al. (2014) found that "Cytochromes play a key role in N2O production by directing electron flow."
  conf: not stated · class: model (note: "in these models") · holds: the N. europaea SMN · src: perezgarciaClarifyingRegulationNO2014 · trail: C-STEPDEN §Key Findings · from: C-STEPDEN:B-0010, C-STEPDEN:B-0012
- **electron-overflow.4** Perez-Garcia et al. (2014) found that "The cytochrome P460 reaction can potentially mitigate N2O emissions."
  conf: not stated · class: model (note: "in these models") · holds: the N. europaea SMN · src: perezgarciaClarifyingRegulationNO2014 · trail: C-STEPDEN §Key Findings · from: C-STEPDEN:B-0010, C-STEPDEN:B-0012
- **electron-overflow.5** The Perez-Garcia (2014) model's central, validated finding is that NO/N₂O emission is an electron-overflow phenomenon: nitrifier denitrification is "activated when the availability of electron donors exceeds that of electron sinks," dissipating excess reducing equivalents when O₂ is limiting.
  conf: not stated · class: not stated · holds: N. europaea under O₂ limitation · src: perezgarciaClarifyingRegulationNO2014 · trail: C-STEPDEN §What · from: C-STEPDEN:B-0023, C-STEPDEN:B-0025
- **electron-overflow.6** Both Perez-Garcia et al. (2014) and Mellbye et al. (2018) attribute N₂O emission to an intracellular electron-equivalent imbalance under O₂ limitation, not to a missing nosZ or a pathway gap in a four-step chain.
  conf: not stated · class: not stated · holds: the two stoichiometric/FBA models of nitrifier denitrification · src: perezgarciaClarifyingRegulationNO2014, mellbyeGenomeScaleConstraintBased2018 · trail: C-STEPDEN §TL;DR, §Key Findings · from: C-STEPDEN:B-0008, C-STEPDEN:B-0012, C-STEPDEN:B-0057
- **electron-overflow.7** In the demonstrated nitrifier-denitrification models, each transformation is encoded as a distinct reaction tied to its enzyme (NO₂⁻→NO by NirK; NO→N₂O by NorB), with N-oxides as intracellular species that can be drained by exchange reactions.
  conf: not stated · class: not stated · holds: the nitrifier-denitrification cases the review calls demonstrated · src: none (the reviewer's synthesis of the nitrifier-denitrification models) · trail: C-STEPDEN §How stepwise · from: C-STEPDEN:B-0041
- **electron-overflow.8** In these models the electron-balance logic is what forces emission: N₂O/NO appear when reducing-equivalent production outruns the available electron sink (O₂).
  conf: not stated · class: not stated · holds: the nitrifier-denitrification models · src: none (the reviewer's synthesis of the nitrifier-denitrification models) · trail: C-STEPDEN §How stepwise · from: C-STEPDEN:B-0041..0042
- **electron-overflow.9** The constraint-based representation works for nitrifier denitrification because the model treats N-oxide release as an electron-overflow valve rather than as the controlled, regulated sequential respiration of a canonical denitrifier.
  conf: not stated · class: not stated · holds: nitrifier denitrification, contrasted with canonical denitrifiers · src: none (the reviewer's synthesis) · trail: C-STEPDEN §How stepwise · from: C-STEPDEN:B-0043
- **electron-overflow.10** Constraint-based/FBA models that explicitly output N₂O do so only where N₂O is a forced electron-overflow terminus in an organism lacking nosZ (nitrifier denitrification in N. europaea); their N₂O is nitrifier-denitrification-derived and electron-overflow-driven, not a four-step heterotrophic truncation.
  conf: not stated · class: not stated · holds: Perez-Garcia et al. (2014) and Mellbye et al. (2018); N. europaea · src: perezgarciaClarifyingRegulationNO2014, mellbyeGenomeScaleConstraintBased2018 · trail: C-STEPDEN §How the cases, §Recommendations · from: C-STEPDEN:B-0057, C-STEPDEN:B-0060, C-STEPDEN:B-0062

### n-oxide-balancing: balancing the N-oxide reactions
needs: nitrifier-denitrification-models

- **n-oxide-balancing.1** The detailed mass- and charge-balancing of the N-oxide reactions in iFC578/iFC579 (electron donors, quinone/cytochrome/NADH coupling) could not be confirmed from the text the review could access.
  conf: not stated · class: not stated · holds: the Mellbye coculture reconstructions iFC578 and iFC579 · src: mellbyeGenomeScaleConstraintBased2018 · limit: access (note: "could not be confirmed from accessible text") · trail: C-STEPDEN §What · from: C-STEPDEN:B-0034
- **n-oxide-balancing.2** For Perez-Garcia et al. (2014) and Mellbye et al. (2018), the detailed electron-coupling stoichiometry of the N-oxide reactions could not be confirmed verbatim, because their full-text Methods and reaction tables were partially inaccessible (publisher bot detection).
  conf: not stated · class: not stated · holds: the two nitrifier-denitrification models · src: perezgarciaClarifyingRegulationNO2014, mellbyeGenomeScaleConstraintBased2018 · limit: access (note: "partially inaccessible (publisher bot detection)") · trail: C-STEPDEN §Caveats · from: C-STEPDEN:A-001, C-STEPDEN:B-0069
- **n-oxide-balancing.3** That iGC535 (2022) was a substantially re-curated successor of the N. europaea reconstruction indicates, in the review's reading, that N-oxide reaction balancing in this lineage required considerable manual curation effort.
  conf: not stated · class: reading (note: "indicating that N-oxide reaction balancing in this lineage required considerable manual curation effort") · holds: the N. europaea reconstruction lineage · src: cantoencaladaFluxBalanceAnalysis2022 · trail: C-STEPDEN §What · from: C-STEPDEN:B-0035
- **n-oxide-balancing.4** The documented difficulty specific to N₂O is "indirect but real": balancing the cytochrome/N-oxide reactions for mass and charge is error-prone.
  conf: not stated · class: not stated · holds: models balancing cytochrome/N-oxide reactions · src: none (the note cites no source for it) · trail: C-STEPDEN §How stepwise · from: C-STEPDEN:B-0044

### denitrifier-gems: genome-scale models of canonical denitrifiers
needs: constraint-based-model

- **denitrifier-gems.1** Single-strain denitrifier genome-scale models (GEMs) exist for Paracoccus denitrificans Pd1222, Thauera sp. MZ1T (iThauera861), Pseudomonas stutzeri A1501 (iPB890, iQY1018) and Pseudomonas aeruginosa (iMO1056, iSD1509); they represent denitrification but were built and validated for biomass yield, substrate utilization and polymer production, not for resolving N₂O as a distinct truncation output, so they collapse or do not feature N₂O as a resolved terminal readout.
  conf: not stated · class: not stated · holds: single-strain GEMs of canonical denitrifiers · src: bordelGenomescaleMetabolicModel2024, teccamposGenomescaleMetabolicModel2025, babaeiGenomescaleReconstructionMetabolic2015, yuanReconstructionMetabolicProfiling2023, oberhardt2008, dahalGenomescaleModelPseudomonas2023 · trail: C-STEPDEN §Key Findings · from: C-STEPDEN:B-0016..0017
- **denitrifier-gems.2** The Paracoccus denitrificans Pd1222 GEM (Bordel et al., 2024, mSystems; 972 genes, 1,371 reactions, 1,388 metabolites; reconstructed in RAST/SEED, simulated in COBRA-style FBA) was built and validated for biomass yields on carbon sources, including with NO₃⁻ as electron acceptor.
  conf: not stated · class: not stated · holds: P. denitrificans Pd1222; carbon-source biomass yields · src: bordelGenomescaleMetabolicModel2024 · trail: C-STEPDEN §What · from: C-STEPDEN:B-0036
- **denitrifier-gems.3** P. denitrificans is the textbook complete denitrifier (Nap, NirS, cNor, NosZ), yet the Pd1222 GEM publication's validated outputs concern carbon-source yields, not stepwise N-oxide fluxes or N₂O emission.
  conf: not stated · class: not stated · holds: P. denitrificans Pd1222 · src: bordelGenomescaleMetabolicModel2024 · trail: C-STEPDEN §What · from: C-STEPDEN:B-0036..0037
- **denitrifier-gems.4** The Thauera sp. MZ1T model iThauera861 (Tec-Campos et al., 2025, PLoS Computational Biology; 861 genes, 2,384 reactions, 1,744 metabolites) explicitly notes that the organism makes denitrification intermediates including nitrous and nitric oxide, but the model was deployed for PHB/EPS polymer production and pollutant degradation, not N₂O resolution.
  conf: not stated · class: not stated · holds: Thauera sp. MZ1T · src: teccamposGenomescaleMetabolicModel2025 · trail: C-STEPDEN §What · from: C-STEPDEN:B-0038
- **denitrifier-gems.5** The Pseudomonas stutzeri A1501 models (iPB890, Babaei et al., 2015; iQY1018, Yuan et al., 2023) and P. aeruginosa models (iMO1056, Oberhardt et al., 2008; iSD1509, Dahal et al., 2023) include denitrification for anaerobic growth but treat it as a route to N₂ and energy, not as a resolved N₂O-emitting sub-step chain.
  conf: not stated · class: not stated · holds: P. stutzeri A1501 and P. aeruginosa · src: babaeiGenomescaleReconstructionMetabolic2015, yuanReconstructionMetabolicProfiling2023, oberhardt2008, dahalGenomescaleModelPseudomonas2023 · trail: C-STEPDEN §What · from: C-STEPDEN:B-0039
- **denitrifier-gems.6** The review's model index records iSD1509 as a Pseudomonas aeruginosa PA14 genome-scale FBA model (BiGG), and iQY1018 as carrying the denitrification chain for N2 without resolving N2O.
  conf: not stated · class: not stated · holds: P. aeruginosa PA14; P. stutzeri A1501 · src: dahalGenomescaleModelPseudomonas2023, yuanReconstructionMetabolicProfiling2023 · trail: C-STEPDEN §Compact JSON · from: C-STEPDEN:B-0074
- **denitrifier-gems.7** Automated CarveMe drafts of P. stutzeri were noted to lack a functional anaerobic nitrate-respiration chain entirely.
  conf: not stated · class: not stated · holds: automated CarveMe draft reconstructions of P. stutzeri · src: none (the note names CarveMe drafts without a reference) · trail: C-STEPDEN §What · from: C-STEPDEN:B-0040
- **denitrifier-gems.8** Canonical complete-denitrifier GEMs carry the genes for all four steps but were neither built nor validated to emit N₂O as a resolved truncation product.
  conf: not stated · class: not stated · holds: complete-denitrifier GEMs the review located · src: bordelGenomescaleMetabolicModel2024, teccamposGenomescaleMetabolicModel2025 · trail: C-STEPDEN §How the cases · from: C-STEPDEN:B-0058
- **denitrifier-gems.9** The Pd1222 GEM (github.com/SergioBordel/ModelParacoccus) and iThauera861 both contain the full denitrification gene complement (nar/nap, nir, nor, nos); the review calls them the best-curated starting points for a complete-denitrifier GEM to extend.
  conf: not stated · class: not stated · holds: P. denitrificans Pd1222 and Thauera sp. MZ1T · src: bordelGenomescaleMetabolicModel2024, teccamposGenomescaleMetabolicModel2025 · trail: C-STEPDEN §Recommendations · from: C-STEPDEN:B-0063

### community-models: community constraint-based models
needs: constraint-based-model, denitrification-pathway

- **community-models.1** Community constraint-based models report aggregate process capability, not resolved denitrification sub-steps: reviews of community metabolic modelling (for example the "More is Different" review in mSystems, 2023) describe FBA/constraint-based community methods as inferring flux distributions and exchange/cross-feeding fluxes.
  conf: not stated · class: not stated · holds: community metabolic modelling as described by reviews · src: anonMoreDifferentReview2023 · trail: C-STEPDEN §Bounding · from: C-STEPDEN:B-0045
- **community-models.2** The review located no instance of a community constraint-based model resolving the four denitrification sub-steps with N₂O as a community-level truncation output.
  conf: not stated · class: search (note: "no instance located") · search: searched, not found (note: "no instance located") · holds: community metabolic modelling literature the review searched · src: anonMoreDifferentReview2023 · trail: C-STEPDEN §Bounding · from: C-STEPDEN:B-0045
- **community-models.3** AGORA/AGORA2 gut reconstructions and gut community constraint-based models (CBM) include nitrate/nitrite reductase reactions but do not resolve a stepwise denitrification-to-N₂O readout.
  conf: not stated · class: not stated · holds: gut reconstructions and gut community models · src: none (the note names AGORA/AGORA2 without a reference) · trail: C-STEPDEN §Bounding · from: C-STEPDEN:B-0046

### four-step-truncation: a constraint-based model of four-step denitrification with N2O truncation
needs: nitrifier-denitrification-models, electron-overflow, n-oxide-balancing, denitrifier-gems, community-models, kinetic-trait-models

- **four-step-truncation.1** Constraint-based/FBA models have represented N-oxide reduction as discrete enzymatic reactions (separate fluxes) with N₂O as an explicit, distinct modelled output, but only in the nitrifier-denitrification branch of ammonia-oxidizing bacteria (Nitrosomonas europaea; Perez-Garcia et al. 2014, 2016; Mellbye et al. 2018), where N₂O is terminal because the organism lacks nosZ and emission is mechanistically framed as electron-equivalent overflow under O₂ limitation.
  conf: not stated · class: not stated · holds: the nitrifier-denitrification branch of ammonia-oxidizing bacteria · src: perezgarciaClarifyingRegulationNO2014, perezgarciaAssessmentNitricOxide2016, mellbyeGenomeScaleConstraintBased2018 · trail: C-STEPDEN §Verdict, §TL;DR · rating: "PARTIALLY DEMONSTRATED" · contrary: not stated · from: C-STEPDEN:A-001, C-STEPDEN:B-0006
- **four-step-truncation.2** A genome-scale or community FBA model resolving NO₃⁻→NO₂⁻→NO→N₂O→N₂ as four separate fluxes (nar/nap, nirK/nirS, norBC, nosZ) with N₂O emerging as a truncation/accumulation product, due to a missing or regulated nosZ or a community pathway gap, was not found in the constraint-based literature; that capability currently resides exclusively in the kinetic/ODE, cybernetic and trait-based ecosystem modelling families.
  conf: not stated · class: search (note: "was NOT found in the constraint-based literature") · search: searched, not found (note: "absence of evidence in a thorough but finite search") · holds: published, locatable constraint-based literature as of June 2026; the review says an unpublished or very recent model could exist · src: none (the review's search) · trail: C-STEPDEN §Verdict, §TL;DR, §Caveats, §Recommendations · contrary: not stated · from: C-STEPDEN:A-002, C-STEPDEN:B-0007, C-STEPDEN:B-0068, C-STEPDEN:B-0071..0072
- **four-step-truncation.3** The literature has encoded denitrification reactions in constraint-based models in two clearly distinguishable ways: nitrifier-denitrification models that explicitly emit N₂O, and single-strain canonical denitrifier GEMs whose genome content carries the sub-steps but in which N₂O is not a resolved readout.
  conf: not stated · class: not stated · holds: constraint-based models the review located · src: none (the reviewer's synthesis) · trail: C-STEPDEN §What · from: C-STEPDEN:B-0022..0023, C-STEPDEN:B-0036
- **four-step-truncation.4** Resolving N₂O as an explicit output in a complete-denitrifier GEM would require adding per-step exchange reactions, explicit electron-donor/quinone coupling for each reductase, and constraints (for example capping nosZ flux to mimic Cu limitation or regulatory lag), an extension not yet published.
  conf: not stated · class: not stated · holds: complete-denitrifier GEMs such as the P. denitrificans Pd1222 GEM and iThauera861 · src: none (the reviewer's synthesis) · trail: C-STEPDEN §Recommendations · from: C-STEPDEN:B-0063..0064
- **four-step-truncation.5** The review sets the benchmark that would change its verdict to DEMONSTRATED: a published, mass- and charge-balanced genome-scale or community constraint-based model in which (a) nar/nap, nir, nor and nos are each separate reactions, (b) N₂O appears as a terminal exchange or accumulating product, and (c) the stated cause is a pathway gap (absent or capped nosZ, or cross-organism division of labour) rather than electron overflow alone; as of June 2026 no such publication was located.
  conf: not stated · class: search (note: "no such publication was located") · search: searched, not found (note: "no such publication was located") · holds: published literature as of June 2026 · src: none (the reviewer's criteria) · trail: C-STEPDEN §Recommendations · from: C-STEPDEN:B-0067..0068

## Do not say

- **dns.1** "No genome-scale or community FBA model of four-step denitrification with N₂O as a truncation output has been published."
  why: The note says its NOT FOUND reflects the absence of evidence in a thorough but finite search, that an unpublished or very recent model could exist, and that the negative claim is bounded to published, locatable constraint-based literature as of June 2026. · instead: four-step-truncation.2 · trail: C-STEPDEN §Caveats · from: C-STEPDEN:B-0007, C-STEPDEN:B-0071..0072
- **dns.2** "Perez-Garcia et al. (2014) and Mellbye et al. (2018) model N₂O as the truncation product of four-step heterotrophic denitrification."
  why: The note says their N₂O is nitrifier-denitrification-derived and electron-overflow-driven, not a four-step heterotrophic truncation. · instead: electron-overflow.10, four-step-truncation.1 · trail: C-STEPDEN §Recommendations · from: C-STEPDEN:B-0060, C-STEPDEN:B-0062

## Gaps

- **gap.1** The findings were never checked by a second reader: the note has no critique. The answers rest on the Perez-Garcia et al. (2014) N. europaea network (51 reactions, 44 metabolites; an average 15% deviation from 17 M yield ratios), the Perez-Garcia et al. (2016) eight-species network (a 60% decrease in N₂O formation), the Mellbye et al. (2018) iFC578/iFC579 coculture model, and a search that did not find a four-step constraint-based truncation model.
  blocks: four-step-truncation, nitrifier-denitrification-models, electron-overflow · origin: no critique in the input, so no second reader checked it · search: not stated · from: C-STEPDEN:A-001..002, C-STEPDEN:B-0023, C-STEPDEN:B-0026..0027, C-STEPDEN:B-0029
- **gap.2** Whether a genome-scale or community constraint-based model resolving all four denitrification steps, with N₂O as a truncation or accumulation output caused by a pathway gap, exists: the review did not find one, and says an unpublished or very recent model could exist.
  blocks: four-step-truncation · origin: the note's not-found result and its caveat · search: searched, not found (note: "absence of evidence in a thorough but finite search") · from: C-STEPDEN:A-002, C-STEPDEN:B-0071..0072
- **gap.3** The detailed electron-coupling stoichiometry (mass and charge balancing; quinone/cytochrome/NADH coupling) of the N-oxide reactions in Perez-Garcia et al. (2014) and in Mellbye et al. (2018, iFC578/iFC579) was not confirmed, because the full-text Methods and reaction tables were partially inaccessible.
  blocks: n-oxide-balancing · origin: the note's caveat on access · search: not stated · src: perezgarciaClarifyingRegulationNO2014, mellbyeGenomeScaleConstraintBased2018 · from: C-STEPDEN:B-0034, C-STEPDEN:B-0069
- **gap.4** The note is inconsistent about which constraint-based models emit N₂O as a distinct output: its Recommendations say Perez-Garcia et al. (2014) and Mellbye et al. (2018) "are the only published FBA/stoichiometric models located that emit N₂O as a distinct flux", while its Verdict names "Perez-Garcia et al. 2014, 2016; Mellbye et al. 2018" and its model index marks the 2016 multispecies network as N₂O-explicit.
  blocks: nitrifier-denitrification-models · origin: the note contradicts itself (Recommendations against Verdict and model index) · search: not stated · src: perezgarciaAssessmentNitricOxide2016 · from: C-STEPDEN:B-0060..0061, C-STEPDEN:A-001, C-STEPDEN:B-0074
- **gap.5** The note attributes the 60% decrease in N₂O formation in the 2016 multispecies network differently in two places: the body quotes "NO oxidation to NO2(-) decreased N2O formation by 60%", while the model index says "CytP460 reduces N2O by 60%".
  blocks: nitrifier-denitrification-models · origin: the note's body and its model index disagree · search: not stated · src: perezgarciaAssessmentNitricOxide2016 · from: C-STEPDEN:B-0027, C-STEPDEN:B-0074
- **gap.6** Several works the text relies on have no entry in the note's reference list: the electron-competition models (Pan et al., ES&T), the Domingo-Félez & Smets NDHA model, iMO1056 (Oberhardt et al., 2008), AGORA/AGORA2, the CarveMe drafts of P. stutzeri, and the byproduct-secretion modelling literature; three listed references (Zakem et al., Yuan et al., Dahal et al.) have abbreviated author lists.
  blocks: kinetic-trait-models, denitrifier-gems, community-models, constraint-based-model · origin: references missing or incomplete in the note · search: not stated · src: pan, domingofelez, oberhardt2008 · from: C-STEPDEN:B-0039..0040, C-STEPDEN:B-0044, C-STEPDEN:B-0046, C-STEPDEN:B-0048, C-STEPDEN:B-0052, C-STEPDEN:B-0118, C-STEPDEN:B-0128, C-STEPDEN:B-0131, C-STEPDEN:B-0137

## Out of scope

## Sources

```bibtex
@article{perezgarciaClarifyingRegulationNO2014,
  author = {Perez-Garcia, O. and Villas-Boas, S. G. and Swift, S. and Chandran, K. and Singhal, N.},
  title = {Clarifying the regulation of NO/N2O production in Nitrosomonas europaea during anoxic-oxic transition via flux balance analysis of a metabolic network model},
  journal = {Water Research},
  year = {2014},
  volume = {60},
  pages = {267--277},
  doi = {10.1016/j.watres.2014.04.049},
  pmid = {24862955},
  note = {access: not stated (full-text Methods/reaction tables partially inaccessible, publisher bot detection; facts corroborated from abstracts and verbatim snippets); cited as: C-STEPDEN [1]}
}
@article{mellbyeGenomeScaleConstraintBased2018,
  author = {Mellbye, B. L. and Giguere, A. T. and Murthy, G. S. and Bottomley, P. J. and Sayavedra-Soto, L. A. and Chaplen, F. W. R.},
  title = {Genome-Scale, Constraint-Based Modeling of Nitrogen Oxide Fluxes during Coculture of Nitrosomonas europaea and Nitrobacter winogradskyi},
  journal = {mSystems},
  year = {2018},
  volume = {3},
  number = {3},
  pages = {e00170-17},
  doi = {10.1128/mSystems.00170-17},
  pmid = {29577088},
  note = {access: not stated (full-text Methods/reaction tables partially inaccessible, publisher bot detection; facts corroborated from abstracts, verbatim snippets and the Methods text recovered); cited as: C-STEPDEN [2]}
}
@article{perezgarciaAssessmentNitricOxide2016,
  author = {Perez-Garcia, O. and Chandran, K. and Villas-Boas, S. G. and Singhal, N.},
  title = {Assessment of nitric oxide (NO) redox reactions contribution to nitrous oxide (N2O) formation during nitrification using a multispecies metabolic network model},
  journal = {Biotechnology and Bioengineering},
  year = {2016},
  volume = {113},
  number = {5},
  pages = {1124--1136},
  doi = {10.1002/bit.25880},
  pmid = {26551878},
  note = {access: not stated; cited as: C-STEPDEN [3]}
}
@article{cantoencaladaFluxBalanceAnalysis2022,
  author = {Canto-Encalada, G. and Tec-Campos, D. and Tibocha-Bonilla, J. D. and Zengler, K. and Zepeda, A. and Zu{\~n}iga, C.},
  title = {Flux balance analysis of the ammonia-oxidizing bacterium Nitrosomonas europaea ATCC19718 unravels specific metabolic activities while degrading toxic compounds},
  journal = {PLoS Computational Biology},
  year = {2022},
  volume = {18},
  number = {2},
  pages = {e1009828},
  doi = {10.1371/journal.pcbi.1009828},
  pmid = {35108266},
  note = {access: not stated; cited as: C-STEPDEN [4]}
}
@article{bordelGenomescaleMetabolicModel2024,
  author = {Bordel, S. and Mart{\'i}n-Gonz{\'a}lez, D. and B{\"o}rner, T. and Mu{\~n}oz, R. and Santos-Beneit, F.},
  title = {Genome-scale metabolic model of the versatile bacterium Paracoccus denitrificans Pd1222},
  journal = {mSystems},
  year = {2024},
  volume = {9},
  number = {2},
  pages = {e0107723},
  doi = {10.1128/msystems.01077-23},
  pmid = {38180324},
  note = {access: not stated; cited as: C-STEPDEN [5]}
}
@article{teccamposGenomescaleMetabolicModel2025,
  author = {Tec-Campos, D. and Tibocha-Bonilla, J. D. and Jiang, C. and Passi, A. and Thiruppathy, D. and Zu{\~n}iga, C. and Posadas, C. and Zepeda, A. and Zengler, K.},
  title = {A genome-scale metabolic model for the denitrifying bacterium Thauera sp. MZ1T accurately predicts degradation of pollutants and production of polymers},
  journal = {PLoS Computational Biology},
  year = {2025},
  volume = {21},
  number = {1},
  pages = {e1012736},
  doi = {10.1371/journal.pcbi.1012736},
  pmid = {39774301},
  note = {access: not stated; cited as: C-STEPDEN [6]}
}
@article{kampschreurMetabolicModelingDenitrification2012,
  author = {Kampschreur, M. J. and Kleerebezem, R. and Picioreanu, C. and Bakken, L. and Bergaust, L. and de Vries, S. and Jetten, M. S. M. and van Loosdrecht, M. C. M.},
  title = {Metabolic modeling of denitrification in Agrobacterium tumefaciens: a tool to study inhibiting and activating compounds for the denitrification pathway},
  journal = {Frontiers in Microbiology},
  year = {2012},
  volume = {3},
  pages = {370},
  doi = {10.3389/fmicb.2012.00370},
  pmid = {23091471},
  note = {access: not stated; cited as: C-STEPDEN [7]}
}
@article{songDynamicMetabolicModeling2015,
  author = {Song, H. S. and Liu, C.},
  title = {Dynamic metabolic modeling of denitrifying bacterial growth: the cybernetic approach},
  journal = {Industrial \& Engineering Chemistry Research},
  year = {2015},
  volume = {54},
  number = {42},
  pages = {10221--10227},
  doi = {10.1021/acs.iecr.5b01615},
  note = {access: not stated; cited as: C-STEPDEN [8]}
}
@article{songRegulationStructuredDynamicMetabolic2017,
  author = {Song, H. S. and Thomas, D. G. and Stegen, J. C. and Li, M. and Liu, C. and Song, X. and Chen, X. and Fredrickson, J. K. and Zachara, J. M. and Scheibe, T. D.},
  title = {Regulation-structured dynamic metabolic model provides a potential mechanism for delayed enzyme response in denitrification process},
  journal = {Frontiers in Microbiology},
  year = {2017},
  volume = {8},
  pages = {1866},
  doi = {10.3389/fmicb.2017.01866},
  pmid = {29021784},
  note = {access: not stated; cited as: C-STEPDEN [9]}
}
@article{hiattUpdatedProcessModel2008,
  author = {Hiatt, W. C. and Grady, C. P., Jr.},
  title = {An updated process model for carbon oxidation, nitrification, and denitrification},
  journal = {Water Environment Research},
  year = {2008},
  volume = {80},
  number = {11},
  pages = {2145--2156},
  doi = {10.2175/106143008X304776},
  pmid = {19024730},
  note = {access: not stated; cited as: C-STEPDEN [10]}
}
@article{zakemEcologicalDynamicsModular2024,
  author = {Zakem, E. J. and Mahadevan, R. and others},
  title = {Ecological dynamics explain modular denitrification in the ocean},
  journal = {Proceedings of the National Academy of Sciences USA},
  year = {2024},
  volume = {121},
  number = {52},
  pages = {e2417421121},
  doi = {10.1073/pnas.2417421121},
  pmid = {39693347},
  note = {access: not stated; cited as: C-STEPDEN [11]; incomplete: author (the note gives "Zakem EJ, Mahadevan R, et al." and says the full author list was not recoverable)}
}
@misc{zakemEcologicalDynamicsExplain2024,
  author = {Zakem, E. J. and Mahadevan, R. and others},
  title = {Ecological dynamics explain modular denitrification in the ocean},
  howpublished = {bioRxiv preprint 2024.09.25.615058},
  year = {2024},
  doi = {10.1101/2024.09.25.615058},
  note = {access: not stated; type: preprint; cited as: C-STEPDEN [11] (the preprint named in the same reference); incomplete: author}
}
@article{babaeiGenomescaleReconstructionMetabolic2015,
  author = {Babaei, P. and Marashi, S. A. and Asad, S.},
  title = {Genome-scale reconstruction of the metabolic network in Pseudomonas stutzeri A1501},
  journal = {Molecular BioSystems},
  year = {2015},
  volume = {11},
  number = {11},
  pages = {3022--3032},
  doi = {10.1039/c5mb00086f},
  pmid = {26302703},
  note = {access: not stated; cited as: C-STEPDEN [12]}
}
@article{yuanReconstructionMetabolicProfiling2023,
  author = {Yuan, Q. and others},
  title = {Reconstruction and metabolic profiling of the genome-scale metabolic network model of Pseudomonas stutzeri A1501},
  journal = {Synthetic and Systems Biotechnology},
  year = {2023},
  volume = {8},
  number = {4},
  pages = {688--696},
  doi = {10.1016/j.synbio.2023.10.001},
  note = {access: not stated; cited as: C-STEPDEN [13]; incomplete: author (the note gives "Yuan Q, et al.")}
}
@article{dahalGenomescaleModelPseudomonas2023,
  author = {Dahal, S. and others},
  title = {Genome-scale model of Pseudomonas aeruginosa metabolism unveils virulence and drug potentiation},
  journal = {Communications Biology},
  year = {2023},
  volume = {6},
  pages = {165},
  doi = {10.1038/s42003-023-04540-8},
  note = {access: not stated; cited as: C-STEPDEN [14]; incomplete: author (the note gives "Dahal S, et al.")}
}
@article{anonMoreDifferentReview2023,
  title = {The "More is Different" review of microbial community metabolic modeling},
  journal = {mSystems},
  year = {2023},
  volume = {8},
  number = {2},
  pages = {e01270-22},
  doi = {10.1128/msystems.01270-22},
  note = {access: not stated; type: review; cited as: C-STEPDEN [15]; incomplete: author, title (the note names the review, not its full title)}
}
@article{oberhardt2008,
  author = {Oberhardt and others},
  title = {},
  year = {2008},
  note = {access: not stated; cited in the text only (iMO1056, Oberhardt et al., 2008), not in the reference list; incomplete: author, title, journal, doi}
}
@article{pan,
  author = {Pan and others},
  title = {},
  journal = {Environmental Science \& Technology},
  note = {access: not stated; cited in the text only (electron-competition models, Pan et al., ES&T), not in the reference list; incomplete: author, title, year, volume, pages, doi}
}
@article{domingofelez,
  author = {Domingo-F{\'e}lez and Smets},
  title = {},
  note = {access: not stated; cited in the text only (the Domingo-Felez & Smets NDHA model), not in the reference list; incomplete: title, journal, year, doi}
}
@article{orthWhatFluxBalance2010,
  author = {Orth, Jeffrey D. and Thiele, Ines and Palsson, Bernhard {\O}.},
  title = {What is flux balance analysis?},
  journal = {Nature Biotechnology},
  year = {2010},
  volume = {28},
  number = {3},
  pages = {245--248},
  doi = {10.1038/nbt.1614},
  note = {background; access: full_text (PMC3108565)}
}
```
