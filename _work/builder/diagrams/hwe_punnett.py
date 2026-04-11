"""Hardy-Weinberg Punnett square — Drosophila ADH locus (Lec 4, p=0.7, q=0.3)."""
from .types import make_node, make_edge, validate_diagram


def hwe_punnett_diagram():
    """Return the HWE Punnett square for the Lecture 4 Drosophila ADH worked example."""
    nodes = [
        make_node(
            id='row_A',
            label='A (p=0.7)',
            detail=(
                'Row header: maternal gamete carrying allele A at frequency p = 0.7. '
                'Under random mating, 70% of eggs carry A. p is simply the count of A '
                'alleles divided by the total number of alleles (2N) in the population.'
            ),
            mnemonic='p = frequency of the A allele in the egg pool.',
            watchOut='p is an ALLELE frequency, not a genotype frequency. Do not conflate p with f(AA).',
            value='p=0.7',
            color='amber',
        ),
        make_node(
            id='row_a',
            label='a (q=0.3)',
            detail=(
                'Row header: maternal gamete carrying allele a at frequency q = 0.3. '
                'Because only two alleles segregate at this ADH locus, p + q = 1, so '
                'q = 1 − p = 0.3.'
            ),
            mnemonic='q = 1 − p, always.',
            watchOut='q drifts upward when the A allele is selected against — not when a is "good".',
            value='q=0.3',
            color='amber',
        ),
        make_node(
            id='col_A',
            label='A (p=0.7)',
            detail=(
                'Column header: paternal gamete carrying allele A at frequency p = 0.7. '
                'Random mating means egg A meets sperm A with probability p × p.'
            ),
            mnemonic='Column = sperm, row = egg. Random mating lets us multiply.',
            watchOut='Only valid if mating is random with respect to this locus.',
            value='p=0.7',
            color='amber',
        ),
        make_node(
            id='col_a',
            label='a (q=0.3)',
            detail=(
                'Column header: paternal gamete carrying allele a at frequency q = 0.3. '
                'Sperm a has the same population frequency as egg a because gametes are '
                'drawn from the same allele pool.'
            ),
            mnemonic='Sperm and egg frequencies equal if both sexes share allele frequencies.',
            watchOut='Sex-linked loci break this symmetry — X and Y pools differ.',
            value='q=0.3',
            color='amber',
        ),
        make_node(
            id='AA',
            label='AA = p² = 0.49',
            detail=(
                'Homozygous dominant cell. Expected frequency under HWE = p × p = 0.7 × 0.7 = 0.49. '
                'In the Lec 4 Drosophila ADH sample of n = 500 flies the expected count is 245, '
                'but Robbins reported observed AA = 287 — an excess of homozygotes.'
            ),
            mnemonic='p² = AA share of the population.',
            watchOut='Excess AA with deficient Aa is the signature of inbreeding or Wahlund effect.',
            value='exp 245 / obs 287',
            color='teal',
        ),
        make_node(
            id='Aa_1',
            label='Aa = pq = 0.21',
            detail=(
                'First heterozygous cell: egg A meets sperm a. Frequency = p × q = 0.7 × 0.3 = 0.21. '
                'Combined with its mirror cell (aA), the total heterozygote frequency is 2pq = 0.42.'
            ),
            mnemonic='pq is half of 2pq — don’t forget the mirror cell.',
            watchOut='Students sometimes report heterozygote frequency as pq instead of 2pq.',
            value='pq=0.21',
            color='blue',
        ),
        make_node(
            id='aA_1',
            label='aA = qp = 0.21',
            detail=(
                'Mirror heterozygous cell: egg a meets sperm A. Genotype is identical to Aa_1 '
                'but with reversed parental origin. Adding both halves gives 2pq = 0.42, the '
                'expected Aa frequency. Expected count in n=500 is 210; observed only 126.'
            ),
            mnemonic='2pq = combined heterozygote share.',
            watchOut='Heterozygote deficit (obs 126 vs exp 210) points to non-random mating or drift.',
            value='qp=0.21',
            color='blue',
        ),
        make_node(
            id='aa',
            label='aa = q² = 0.09',
            detail=(
                'Homozygous recessive cell. Expected frequency = q × q = 0.3 × 0.3 = 0.09. '
                'Expected count in n=500 is 45; Robbins reported observed aa = 87 — nearly '
                'double. Chi-square on AA=287, Aa=126, aa=87 vs expected 245/210/45 gives '
                'P = 0.02, so the ADH locus is NOT in HWE and at least one assumption is violated.'
            ),
            mnemonic='q² = the "recessive disease" fraction you can see.',
            watchOut=(
                'Chi-square P = 0.02 means we reject HWE for ADH. Excess homozygotes at both '
                'ends plus a heterozygote deficit — classic inbreeding signature, not drift alone.'
            ),
            value='exp 45 / obs 87',
            color='teal',
        ),
    ]
    edges = []
    return validate_diagram({
        'type': 'punnett',
        'title': 'Hardy-Weinberg Punnett Square — Drosophila ADH (Lec 4, n=500)',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'p² + 2pq + q² = 1. If observed ≠ expected → some force is acting.',
    }, node_id='hwe_punnett')
