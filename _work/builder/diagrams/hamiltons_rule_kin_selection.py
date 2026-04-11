"""Hamilton's rule and kin selection — flow diagram.

Source: BIOL 4230 Lec 11. Hamilton 1964 "The Genetical Evolution of Social
Behaviour" (J. Theor. Biol.) introduced inclusive fitness and rB > C. Haldane
reportedly quipped he would lay down his life for "two brothers or eight cousins."
"""

from .types import make_node, make_edge, validate_diagram


def hamiltons_rule_kin_selection_diagram():
    nodes = [
        make_node(
            id='altruism_problem',
            label='Altruism paradox',
            detail=(
                'Why would selection favor behaviors that REDUCE the actor\'s own fitness? '
                'A naive view of natural selection predicts altruism should always be lost. '
                'Yet alarm calls, helpers at the nest, and self-sacrificing workers exist '
                'throughout the animal kingdom.'
            ),
            color='red',
        ),
        make_node(
            id='direct_fitness',
            label='Direct fitness',
            detail=(
                'Own reproductive output via personal offspring. Each of your offspring '
                'carries your alleles with probability r = 0.5 (for diploid sexual reproduction). '
                'This is the component captured by classical Darwinian fitness.'
            ),
            color='blue',
        ),
        make_node(
            id='indirect_fitness',
            label='Indirect fitness',
            detail=(
                'Reproductive output of relatives that carry the same alleles by common '
                'descent. Helping a full sibling reproduce propagates your alleles at '
                'effective rate r = 0.5 per sibling offspring. This is the component Darwin missed.'
            ),
            color='purple',
        ),
        make_node(
            id='inclusive_fitness',
            label='Inclusive fitness',
            value='direct + indirect',
            detail=(
                'The sum of direct and indirect fitness — the full accounting of an allele\'s '
                'propagation through the population (Hamilton 1964). The unit selection '
                'actually "sees" when weighing cooperative vs selfish behavior.'
            ),
            mnemonic='inclusive = me + my kin',
            color='teal',
        ),
        make_node(
            id='coeff_r',
            label='Coefficient of relatedness r',
            value='offspring/full-sib 0.5, half-sib 0.25, cousin 0.125',
            detail=(
                'Probability that two individuals share an allele identical by descent. '
                'Offspring and full siblings r = 0.5. Half siblings and nieces/nephews '
                'r = 0.25. First cousins r = 0.125. Computed from the pedigree using '
                'Wright\'s path method.'
            ),
            color='amber',
        ),
        make_node(
            id='hamilton_rule',
            label='rB > C',
            detail=(
                'Altruism is favored when (relatedness × benefit to recipient) > (cost to '
                'actor). The formal inequality that packages kin selection into one line of '
                'algebra. Hamilton derived it in his 1964 paper.'
            ),
            mnemonic='rB beats C',
            watchOut=(
                'rB > C, NOT B > rC and NOT rB > rC — only the BENEFIT is discounted by '
                'relatedness. The cost to the actor is unconditional.'
            ),
            color='green',
        ),
        make_node(
            id='haldane',
            label='Haldane: 2 brothers or 8 cousins',
            detail=(
                '2 × 0.5 = 1 (break-even for a sibling). 8 × 0.125 = 1 (break-even for a '
                'cousin). Haldane\'s pub-napkin quip that captured kin selection decades '
                'before Hamilton formalized it.'
            ),
            color='amber',
        ),
        make_node(
            id='haplodiploidy',
            label='Haplodiploidy + eusociality',
            detail=(
                'In Hymenoptera (ants, bees, wasps) males are haploid and females are '
                'diploid. Full sisters share r = 0.75 (higher than r = 0.5 to their own '
                'offspring), while brothers are only r = 0.25. This asymmetry may have '
                'facilitated the repeated evolution of eusociality in this clade.'
            ),
            watchOut=(
                'Haplodiploidy FACILITATES but does NOT automatically cause eusociality — '
                'many haplodiploid species are not eusocial, and termites are eusocial '
                'without it.'
            ),
            color='purple',
        ),
        make_node(
            id='meerkat',
            label='Meerkat helpers at the den',
            detail=(
                'Non-breeding meerkats babysit, feed, and teach pups from the dominant '
                'pair — usually siblings or half-siblings. Helpers gain indirect fitness '
                'and also reduced individual predation risk from group living. Clutton-Brock '
                'long-term Kalahari study is a textbook demonstration.'
            ),
            color='teal',
        ),
        make_node(
            id='peromyscus_sperm',
            label='Peromyscus brother sperm',
            detail=(
                'Related sperm from a single male aggregate and swim faster than '
                'unrelated sperm. Kin selection operating at the gamete level — rB > C in '
                'miniature. Only observed in promiscuous species (P. maniculatus) where '
                'sperm competition exists, not in monogamous sisters (P. polionotus).'
            ),
            color='blue',
        ),
    ]
    edges = [
        make_edge('altruism_problem', 'direct_fitness', label='problem'),
        make_edge('altruism_problem', 'indirect_fitness', label='problem'),
        make_edge('direct_fitness', 'inclusive_fitness', label='component of'),
        make_edge('indirect_fitness', 'inclusive_fitness', label='component of'),
        make_edge('coeff_r', 'hamilton_rule', label='input to'),
        make_edge('inclusive_fitness', 'hamilton_rule', label='formalized as'),
        make_edge('hamilton_rule', 'haldane', label='worked example'),
        make_edge('hamilton_rule', 'haplodiploidy', label='predicts'),
        make_edge('hamilton_rule', 'meerkat', label='empirical support'),
        make_edge('hamilton_rule', 'peromyscus_sperm', label='empirical support'),
    ]
    return validate_diagram({
        'type': 'flow',
        'title': "Hamilton's Rule and Kin Selection",
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'rB > C. Relatedness × Benefit > Cost.',
    }, node_id='hamiltons_rule_kin_selection')
