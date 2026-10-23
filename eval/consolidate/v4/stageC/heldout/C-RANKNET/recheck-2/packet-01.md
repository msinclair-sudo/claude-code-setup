## zero-ties.3 (claim)

Connor and colleagues frame the tie correction as preventing "the spurious conclusion that two taxa are ecologically related because they are both absent from many of the same locations".

- conf: not stated
- class: not stated
- holds: microbial co-occurrence networks
- src: connorUsingNullModels2017
- trail: C-RANKNET §What sequencing count

From the note:

> C-RANKNET:B-0120 [What sequencing count properties do to rank methods] Connor, Barberán and Clauset, working on a soil 16S matrix in which "abundance values of zero comprise fully 85% of the matrix", state that "both matrix sparsity and a heavy-tailed distribution of abundances will induce a very large number of multi-way ties, which will then have identical ranks.
>
> C-RANKNET:B-0124 [What sequencing count properties do to rank methods] Their fix is Monte Carlo tie-breaking with real-valued noise that preserves the original partial ordering, followed by a permutation null; without it the null distribution of rho is disjoint rather than smooth [17].
>
> C-RANKNET:B-0125 [What sequencing count properties do to rank methods] They frame the correction as preventing "the spurious conclusion that two taxa are ecologically related because they are both absent from many of the same locations" [17].
>
> C-RANKNET:R-0066 [References] Using null models to infer microbial co-occurrence networks.
>

