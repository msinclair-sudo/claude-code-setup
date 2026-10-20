# Compare richness at a depth both samples reach

<p class="x-message">The deep sample's count rises steeply, then slowly, with depth; at a depth both samples reach, they agree.</p>

<span class="x-label">simulated</span> Two samples from one simulated community of 300 taxa. Sequenced to 20,000 reads, the deep sample shows 288 taxa; the shallow sample, at 2,000 reads, shows 221. Each curve shows how many taxa a sample reveals as more of its reads are used. Marked at 2,000 reads, the deepest point the shallow sample reaches, the deep sample shows 218 on average.

{{plot:f1}}

Move the slider to compare at a smaller depth: the two still agree. Only past 2,000 reads, where the shallow sample has no reads left, does the deep sample pull ahead.

A rarefied count is one subsample's worth, so it varies. Each frame below is one subsample; across 200 subsamples, the middle 95% span 208 to 228 (the shaded band), and the shallow sample's 221 sits inside it.

{{plot:f2}}

Rarefaction estimates the number of taxa expected in a random subsample of a smaller, common size, so samples of unequal size can be compared (Hurlbert 1971; Gotelli and Colwell 2001). The cost: rarefying throws reads away. McMurdie and Holmes (2014) showed in simulations that it loses statistical power when testing which taxa differ in abundance.

<div class="x-sources">Sources: Hurlbert (1971) Ecology 52: 577–586, doi:10.2307/1934145. Gotelli and Colwell (2001) Ecology Letters 4: 379–391, doi:10.1046/j.1461-0248.2001.00230.x. McMurdie and Holmes (2014) PLoS Computational Biology 10: e1003531, doi:10.1371/journal.pcbi.1003531. Simulation: sim.py, seed 7.</div>
