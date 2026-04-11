"""Hardy-Weinberg assumptions paired with the force that violates each one."""
from .types import make_node, make_edge, validate_diagram


def hardy_weinberg_assumptions_diagram():
    """Five HWE assumptions on the left, their matching violation mechanisms on the right."""
    nodes = [
        # LEFT COLUMN — HWE assumptions
        make_node(
            id='inf_pop',
            label='Infinite population size',
            detail=(
                'Assumption 1: N is effectively infinite, so sampling variance in allele '
                'frequencies across generations is zero. Real populations are finite and '
                'allele counts sample from a multinomial distribution each generation.'
            ),
            mnemonic='Infinite N = no sampling error in the gamete draw.',
            watchOut='Even N = 10,000 shows measurable drift over hundreds of generations.',
            color='blue',
        ),
        make_node(
            id='no_selection',
            label='No selection',
            detail=(
                'Assumption 2: every genotype has equal fitness (w_AA = w_Aa = w_aa = 1). '
                'Any fitness differential changes the gamete pool before the next generation '
                'is sampled.'
            ),
            mnemonic='No selection = survival is a fair coin across genotypes.',
            watchOut='Selection is the ONLY force that consistently produces adaptation.',
            color='blue',
        ),
        make_node(
            id='no_mutation',
            label='No mutation',
            detail=(
                'Assumption 3: alleles do not change identity. Real mutation rates are small '
                'but nonzero: ~3×10⁻⁸ per site per generation in yeast and ~7×10⁻⁹ in '
                'Arabidopsis thaliana. Mutation is the ultimate source of new variation.'
            ),
            mnemonic='μ ≈ 10⁻⁸ — small but the only source of new alleles.',
            watchOut='Mutation is directionally weak but creates variance that other forces act on.',
            color='blue',
        ),
        make_node(
            id='no_migration',
            label='No migration (gene flow)',
            detail=(
                'Assumption 4: the population is closed — no immigrants (m = 0). Any inflow '
                'of alleles from a source with different frequencies shifts p and q toward the '
                'source population at rate proportional to m.'
            ),
            mnemonic='Closed population = no new alleles arriving.',
            watchOut='Gene flow homogenizes populations and opposes local adaptation.',
            color='blue',
        ),
        make_node(
            id='random_mating',
            label='Random mating',
            detail=(
                'Assumption 5: mating partners are chosen independently of genotype at the '
                'locus of interest. Inbreeding, assortative mating, and spatial clustering all '
                'violate this — but interestingly, non-random mating changes genotype '
                'frequencies without changing allele frequencies at all.'
            ),
            mnemonic='Random mating = panmixia; any structure breaks it.',
            watchOut='Non-random mating is the odd one out — it violates HWE without changing p or q.',
            color='blue',
        ),
        # RIGHT COLUMN — violation mechanisms
        make_node(
            id='drift',
            label='Genetic drift',
            detail=(
                'Violates "infinite N". Allele frequencies change randomly due to finite '
                'sampling. Buri 1956 ran 107 Drosophila populations (8 M + 8 F per generation) '
                'for 19 generations at the brown-eye bw locus starting at p = 0.5 and showed '
                '28 populations fixed for bw and 30 lost it by generation 19 — pure drift.'
            ),
            mnemonic='Buri 107 pops, 19 gens → drift goes to fixation or loss randomly.',
            watchOut='Drift is strongest in small populations and acts on all alleles, neutral or not.',
            value='Buri 1956',
            color='coral',
        ),
        make_node(
            id='selection_violation',
            label='Natural selection',
            detail=(
                'Violates "no selection". Differential survival/reproduction shifts allele '
                'frequencies. Classic examples: Kettlewell’s peppered moth (Biston betularia) '
                'industrial melanism and the Drosophila ADH locus where allozyme frequencies '
                'track environmental alcohol tolerance.'
            ),
            mnemonic='Selection is the only force that builds adaptation.',
            watchOut='Selection coefficients as small as s = 0.01 can still drive fixation in ~700 generations.',
            value='s ≠ 0',
            color='coral',
        ),
        make_node(
            id='mutation_violation',
            label='Mutation',
            detail=(
                'Violates "no mutation". Creates new alleles via base substitution, indel, or '
                'larger structural change. Yeast germline mutation rate ≈ 3×10⁻⁸ per site per '
                'generation; Arabidopsis thaliana ≈ 7×10⁻⁹. Slow but the only generator of '
                'truly new variation.'
            ),
            mnemonic='Yeast 3×10⁻⁸, Arabidopsis 7×10⁻⁹ per site per generation.',
            watchOut='Mutation alone produces negligible frequency change; it feeds other forces.',
            value='μ ≈ 10⁻⁸',
            color='coral',
        ),
        make_node(
            id='gene_flow',
            label='Gene flow (migration)',
            detail=(
                'Violates "no migration". Movement of individuals (or gametes) between '
                'populations with different allele frequencies redistributes existing alleles. '
                'A migrant rate m = 0.1 per generation fully homogenizes two populations within '
                '~20 generations.'
            ),
            mnemonic='Gene flow = allele frequency laundering between populations.',
            watchOut='Gene flow only redistributes alleles; it doesn’t create new ones.',
            value='m ≠ 0',
            color='coral',
        ),
        make_node(
            id='non_random',
            label='Non-random mating',
            detail=(
                'Violates "random mating". Inbreeding increases homozygosity by a factor F '
                '(the inbreeding coefficient). Assortative mating by phenotype similarly '
                'concentrates genotypes. Crucially, non-random mating changes GENOTYPE '
                'frequencies (more homozygotes) but NOT allele frequencies.'
            ),
            mnemonic='Inbreeding boosts homozygotes without changing p or q.',
            watchOut=(
                'Changes GENOTYPE frequencies but NOT allele frequencies by itself — violates '
                'HWE but is not an allele frequency change mechanism.'
            ),
            value='F > 0',
            color='coral',
        ),
    ]
    edges = [
        make_edge('inf_pop', 'drift', label='violated by', style='arrow'),
        make_edge('no_selection', 'selection_violation', label='violated by', style='arrow'),
        make_edge('no_mutation', 'mutation_violation', label='violated by', style='arrow'),
        make_edge('no_migration', 'gene_flow', label='violated by', style='arrow'),
        make_edge('random_mating', 'non_random', label='violated by', style='arrow'),
    ]
    return validate_diagram({
        'type': 'compare',
        'title': 'Hardy-Weinberg — Five Assumptions and Their Violators',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'MUD-GAS: Mutation / Drift / Gene flow / Assortative mating / Selection. Only mutation creates new variation; the others redistribute existing variation.',
    }, node_id='hardy_weinberg_assumptions')
