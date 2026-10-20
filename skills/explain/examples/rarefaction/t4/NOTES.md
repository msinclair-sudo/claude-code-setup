# Tier 4 narrated animation: what the loop did

Rebuilt 2026-10-20 after the owner's review ("no introduction ... we just dive straight into it"): the story now starts from a droplet of soil and follows the counts through the 16S gene, PCR, sequencing depth and rarefaction (pipeline.py, 12 segments, 4 chapters, 2 min 21 s). The skill gained a setting-first arc (`role` per segment; lint warns when tier 2+ does not open with `setting`).

- **Blind fact-check** (../factcheck.md): Suzuki and Giovannoni (1996) had been cited for the wrong PCR mechanism; "every bacterium carries" the 16S gene was in neither source; a truncated percentile (58.975 shown as 58). All fixed before rendering the final.
- **Round 1 reader**, blocking: blue and orange meant taxa, then samples; "commonest first" on a chart kept in cell-count order; one draw per depth cannot show precision; the barcode never labelled; "sequencing depth" never on screen. Fixed: samples are white and told apart by labels; 30 repeat sequencings per depth; the barcode cut visibly from the 16S gene; the term on screen; reads matched to taxa in the narration.
- **Round 2 reader:** nothing blocking; round 3 took the minors (neutral gene colour, "genome" and "PCR" on screen, richness defined, average marked, summary tag).
- Skill changes from this round: `self.tag()` corner labels (schematic, simulated, summary), "a colour keeps one meaning" and "show the spread" rules, `track()` for axis-placed objects.
