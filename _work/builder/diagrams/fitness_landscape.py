"""Sewall Wright's adaptive landscape — peaks, valleys, drift, and epistasis."""
from .types import make_node, make_edge, validate_diagram


def fitness_landscape_diagram():
    """Wright 1932 fitness landscape: peaks, valleys, selection, drift, gene flow, epistasis."""
    nodes = [
        make_node(
            id='low_fit',
            label='Low fitness valley',
            detail=(
                'A low point on the fitness surface: genotype combinations with poor '
                'reproductive success. In Wright’s (1932) framing, every point in genotype '
                'space has an associated mean fitness; valleys are low-fitness regions '
                'bounded by higher ground on all sides. Populations trapped in valleys '
                'cannot climb out by selection alone.'
            ),
            mnemonic='Valley = mean fitness minimum.',
            watchOut='Selection pushes populations uphill locally — valleys are barriers, not destinations.',
            value='valley',
            color='gray',
        ),
        make_node(
            id='local_peak',
            label='Local adaptive peak',
            detail=(
                'A region where any small genetic change lowers fitness — a local optimum. '
                'Populations on a local peak are stable under selection even though better '
                'peaks exist elsewhere in genotype space. Sewall Wright’s central question '
                '(1932 Sixth International Congress of Genetics talk) was how populations '
                'ever escape such local peaks.'
            ),
            mnemonic='Local peak = any step downhill.',
            watchOut='Selection cannot distinguish local from global peaks — it just climbs whatever slope it sits on.',
            value='local max',
            color='teal',
        ),
        make_node(
            id='higher_peak',
            label='Global/higher peak',
            detail=(
                'A taller region of the landscape with higher mean fitness than the local '
                'peak. To reach it, a population must CROSS the fitness valley separating '
                'the two peaks — a feat impossible for selection acting alone. Wright argued '
                'a subdivided population structure (many small demes connected by limited '
                'gene flow) is the ideal architecture for exploring multiple peaks.'
            ),
            mnemonic='Global peak = the best attainable fitness combination.',
            watchOut='"Global" is only global within the landscape you’ve modeled — real landscapes are high-dimensional.',
            value='global max',
            color='green',
        ),
        make_node(
            id='selection_climb',
            label='Selection climbs local peak',
            detail=(
                'Natural selection acts as a hill-climbing algorithm: each generation, the '
                'population shifts toward higher fitness by fixing beneficial alleles. The '
                'climb is always LOCAL — selection has no look-ahead and cannot see over the '
                'ridge into a valley.'
            ),
            mnemonic='Selection is a greedy uphill algorithm.',
            watchOut='Selection cannot see beyond adjacent genotypes — it is blind to distant peaks.',
            color='teal',
        ),
        make_node(
            id='drift_cross',
            label='Drift can cross valley',
            detail=(
                'In small populations, random genetic drift can push allele frequencies '
                'temporarily DOWNHILL, allowing the population to traverse a fitness valley '
                'and enter the basin of attraction of a higher peak. Wright’s Shifting '
                'Balance Theory (1932) proposed exactly this: drift crosses valleys, '
                'selection climbs peaks, gene flow spreads successful genotypes.'
            ),
            mnemonic='Drift crosses valleys because it ignores fitness.',
            watchOut=(
                'Selection alone cannot cross fitness valleys — drift is required in small '
                'populations. Wright’s shifting balance requires ALL three forces.'
            ),
            color='coral',
        ),
        make_node(
            id='gene_flow_spread',
            label='Gene flow spreads successful genotypes',
            detail=(
                'Once a sub-population drifts across a valley and selection fixes a higher-peak '
                'genotype, migration exports the successful allele combination to neighboring '
                'demes. The whole metapopulation can then shift toward the higher peak. This '
                'is the third leg of Wright’s Shifting Balance Theory.'
            ),
            mnemonic='Gene flow distributes peak discoveries across the metapopulation.',
            watchOut='Too much gene flow swamps local adaptation; too little prevents spread.',
            color='blue',
        ),
        make_node(
            id='epistasis_rugged',
            label='Epistasis creates rugged landscapes',
            detail=(
                'When alleles at one locus modify the fitness effects of alleles at others, '
                'single-locus optima no longer suffice — the landscape becomes rugged with '
                'many local peaks. Epistasis was Wright’s (1932) main motivation for treating '
                'fitness as a multi-locus surface rather than an additive sum of allele '
                'effects.'
            ),
            mnemonic='Epistasis turns smooth hills into jagged terrain.',
            watchOut='Epistasis is invisible if you measure single-locus effects in isolation.',
            color='amber',
        ),
        make_node(
            id='gallfly_multivariate',
            label='Gallfly: multivariate selection',
            detail=(
                'Goldenrod (Solidago altissima) gall flies (Eurosta solidaginis) face opposing '
                'selective pressures on gall size: parasitoid wasps (Eurytoma gigantea) favor '
                'large galls (can’t enter small ones) while downy woodpeckers favor small '
                'galls (can’t see small ones) → stabilizing selection at intermediate gall '
                'size (Weis & Abrahamson 1986; Weis et al. 1992). A real multivariate '
                'fitness peak documented in the field, similar to the garter snake color × '
                'antipredator behavior example from the Pacific Northwest that Wright-style '
                'landscapes predict.'
            ),
            mnemonic='Big galls die to wasps; small galls die to birds; intermediate survives.',
            watchOut='Stabilizing selection carves a single peak; it does not create multiple peaks.',
            color='pink',
        ),
    ]
    edges = [
        make_edge('low_fit', 'selection_climb', label='selection climbs', style='arrow'),
        make_edge('selection_climb', 'local_peak', label='reaches', style='arrow'),
        make_edge('local_peak', 'drift_cross', label='drift crosses valley', style='arrow'),
        make_edge('drift_cross', 'higher_peak', label='enters new basin', style='arrow'),
        make_edge('higher_peak', 'gene_flow_spread', label='gene flow distributes', style='arrow'),
        make_edge('epistasis_rugged', 'local_peak', label='creates multiple local peaks', style='dashed'),
        make_edge('gallfly_multivariate', 'local_peak', label='empirical peak example', style='dashed'),
    ]
    return validate_diagram({
        'type': 'flow',
        'title': 'Wright 1932 Adaptive Landscape — Peaks, Valleys, and Shifting Balance',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'Peaks & Valleys: Selection → local peak; Drift/flow → cross valley to higher peak.',
    }, node_id='fitness_landscape')
