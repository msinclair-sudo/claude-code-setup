"""Metabarcoding, simulated end to end: cells in the soil -> DNA -> 16S copies -> PCR -> reads at a sequencing depth.

Every number the metabarcoding exemplar shows comes from here (seed fixed). Run it to print them.
The model is deliberately simple and says so on screen ("simulated"); where a parameter rests on a
measurement, the source is named (MB-01 literature review, vault Topics/Biology/Research/Results):
  cells        lognormal abundances over N_TAXA taxa (a few common, many rare); mean abundances
               were lognormal in every dataset Grilli (2020) examined
  extraction   each taxon's cells give up their DNA with their own yield, 0.25 to 1 (illustrative:
               harder bead beating raised Gram-positive DNA by up to 400%, Albertsen et al. 2015)
  16S copies   1 to 15 copies per genome, the bacterial range in rrnDB (Stoddard et al. 2015), drawn
               so that one copy is commonest
  PCR          CYCLES cycles (35, as in the Earth Microbiome Project protocol); each taxon amplifies at
               its own rate. No absolute per-cycle efficiency for 16S templates has been measured, so
               the rates are set relative to each other: the log of each taxon's fold bias after 35
               cycles is normal with sd PCR_SD, which puts about 1 taxon in 5 more than fourfold off,
               as in lab-grown gut communities after 35 cycles (Silverman et al. 2021: 19% beyond fourfold;
               their 10-strain mock community: average bias 2.6-fold)
  sequencing   reads are a random draw (multinomial) from the amplicon pool, at a chosen depth
  rarefying    a random subsample without replacement down to a common depth; rarefaction is the
               average over many such subsamples (Schloss 2024)
Left out on purpose (the narration says so): chimeras, index misassignment, sequencing errors and
spurious ASVs, all of which add false taxa; genome copies per cell (barely measured in soil);
contamination; differences in total load between samples.
"""
import numpy as np

SEED, N_TAXA, CELLS, CYCLES = 7, 80, 100_000, 35
PCR_SD = 1.06                     # sd of ln(fold bias) after CYCLES: P(|ln b| > ln 4) = 0.19
DEPTHS = (500, 5_000, 50_000)
DEEP, SHALLOW, DRAWS = 50_000, 2_000, 200


def community():
    rng = np.random.default_rng(SEED)
    w = np.sort(rng.lognormal(0, 2.0, N_TAXA))[::-1]
    cells = np.maximum(1, np.round(w / w.sum() * CELLS)).astype(int)
    lyse = rng.uniform(0.25, 1.0, N_TAXA)                       # share of each taxon's DNA recovered
    k = np.arange(1, 16)
    copies = rng.choice(k, N_TAXA, p=0.7 ** (k - 1) / (0.7 ** (k - 1)).sum())
    bias = np.exp(rng.normal(0, PCR_SD, N_TAXA))                  # fold bias after CYCLES, relative
    return cells, lyse, copies, bias


def stages(cells, lyse, copies, bias):
    """Each taxon's share after each step: cells, extracted DNA (genomes), 16S templates, amplicons."""
    def share(a):
        return a / a.sum()
    return dict(true=share(cells), dna=share(cells * lyse), templates=share(cells * lyse * copies),
                pool=share(cells * lyse * copies * bias))


def sequence(pool, depth, rng):
    return rng.multinomial(depth, pool)


def rarefy(counts, depth, rng):
    reads = np.repeat(np.arange(len(counts)), counts)
    return np.bincount(rng.choice(reads, size=depth, replace=False), minlength=len(counts))


def observed(counts):
    return int((counts > 0).sum())


def data():
    cells, lyse, copies, bias = community()
    s = stages(cells, lyse, copies, bias)
    pool = s["pool"]
    rng = np.random.default_rng(SEED + 1)
    runs = {d: sequence(pool, d, rng) for d in DEPTHS}
    deep, shallow = sequence(pool, DEEP, rng), sequence(pool, SHALLOW, rng)
    draws = np.array([observed(rarefy(deep, SHALLOW, rng)) for _ in range(DRAWS)])
    lo, hi = np.percentile(draws, [2.5, 97.5])
    return dict(cells=cells, lyse=lyse, copies=copies, bias=bias, **s, runs=runs,
                deep=deep, shallow=shallow, obs_deep=observed(deep), obs_shallow=observed(shallow),
                rare_draws=draws, rare_mean=float(draws.mean()), rare_lo=int(round(lo)), rare_hi=int(round(hi)))


if __name__ == "__main__":
    d = data()
    t, p = d["true"], d["pool"]
    print(f"{N_TAXA} taxa, {CELLS:,} cells; most common {d['cells'][0]} cells ({t[0]:.1%}); "
          f"{(d['cells'] <= 10).sum()} taxa with 10 cells or fewer")
    print(f"extraction yield {d['lyse'].min():.2f}-{d['lyse'].max():.2f}; copies {d['copies'].min()}-{d['copies'].max()}, "
          f"mean {d['copies'].mean():.1f}; PCR fold bias {d['bias'].min():.2f}-{d['bias'].max():.2f}, "
          f"beyond fourfold: {(np.abs(np.log(d['bias'])) > np.log(4)).sum()} of {N_TAXA}")
    print("top 6 copies:", d["copies"][:6], " lyse:", np.round(d["lyse"][:6], 2), " bias:", np.round(d["bias"][:6], 2))
    for name in ("true", "dna", "templates", "pool"):
        print(f"{name:>9} top 6 %:", np.round(d[name][:6] * 100, 1))
    r = p / t
    k, j = int(np.argmax(r[:6])), int(np.argmin(r[:6]))
    print(f"among the 6 coloured taxa: biggest gain taxon {k+1} {t[k]:.1%} -> {p[k]:.1%}; "
          f"biggest loss taxon {j+1} {t[j]:.1%} -> {p[j]:.1%}")
    for dep, c in d["runs"].items():
        rel = c / c.sum()
        print(f"depth {dep:>6,}: {observed(c)} taxa seen; top taxon {rel[0]:.1%} (pool {p[0]:.1%}); "
              f"taxa in pool below 1/{dep}: {(p < 1 / dep).sum()}")
    print(f"two samples: deep {DEEP:,} reads -> {d['obs_deep']} taxa; shallow {SHALLOW:,} -> {d['obs_shallow']} taxa")
    print(f"deep rarefied to {SHALLOW:,}: mean {d['rare_mean']:.1f}, middle 95% {d['rare_lo']}-{d['rare_hi']} "
          f"(raw {np.percentile(d['rare_draws'], [2.5, 97.5])}); shallow inside: {d['rare_lo'] <= d['obs_shallow'] <= d['rare_hi']}")
