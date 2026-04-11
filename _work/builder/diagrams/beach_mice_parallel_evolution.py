"""Peromyscus polionotus beach mice — parallel evolution on Gulf and Atlantic coasts."""
from .types import make_node, make_edge, validate_diagram


def beach_mice_parallel_evolution_diagram():
    """Dark mainland ancestor → two independent light-coat beach populations via different genes."""
    nodes = [
        make_node(
            id='ancestral',
            label='Dark mainland ancestor',
            detail=(
                'The ancestral Peromyscus polionotus is a dark brown oldfield mouse that lives '
                'in the dark-soil interior of the southeastern United States. Its pelage '
                'matches the dark organic soil of pine-oak habitat and hides it from owls, '
                'hawks, and snakes against that background.'
            ),
            mnemonic='Dark soil → dark mouse is the ancestral state.',
            watchOut='Do not assume "primitive" — the dark phenotype is itself adaptive on dark soil.',
            color='gray',
        ),
        make_node(
            id='selection_pressure',
            label='Visual predation on light sand',
            detail=(
                'Beach populations colonized bright white sand dunes on both the Gulf of Mexico '
                'and Atlantic coasts during the Pleistocene (<10,000 years ago). Vignieri, '
                'Larson & Hoekstra (2010, Evolution 64:2153–2158) placed painted clay mouse '
                'models in both habitats and showed attack rates by avian predators on '
                'non-matching models were ~2x higher than on matching models. Visual '
                'background-matching is the selective agent.'
            ),
            mnemonic='Vignieri et al. 2010: clay-model experiments prove predator visual selection.',
            watchOut='Predator-mediated selection is empirically demonstrated, not inferred.',
            value='2× attack',
            color='red',
        ),
        make_node(
            id='gulf',
            label='Gulf Coast population',
            detail=(
                'Gulf Coast beach mice (P. polionotus leucocephalus and P. p. trissyllepsis) '
                'evolved light coats via a point mutation in the Mc1r gene (Arg→Cys at amino '
                'acid 65) that reduces receptor activity, plus a regulatory change in the '
                'Agouti signaling protein expression domain (Steiner, Römpler, Boettger, '
                'Schöneberg & Hoekstra 2009, Molecular Biology and Evolution 26:35–45). Both '
                'changes lighten pelage.'
            ),
            mnemonic='Gulf Coast = Mc1r R65C + Agouti up-regulation.',
            watchOut='Both Mc1r and Agouti contribute — single-locus explanations oversimplify.',
            value='Mc1r R65C',
            color='amber',
        ),
        make_node(
            id='atlantic',
            label='Atlantic Coast population',
            detail=(
                'Atlantic Coast beach mice (P. polionotus phasma, P. p. niveiventris, '
                'P. p. decoloratus) ALSO evolved light coats — but the light phenotype is NOT '
                'caused by the Mc1r R65C mutation. Hoekstra lab crosses and sequencing show '
                'the Atlantic light phenotype segregates with different, as-yet-unresolved '
                'loci, implicating a distinct genetic route to the same phenotype '
                '(Steiner et al. 2009 MBE).'
            ),
            mnemonic='Atlantic mice: same light coat, DIFFERENT genes from Gulf mice.',
            watchOut='Similar phenotype from different genetic routes — genetic evidence matters.',
            value='not Mc1r',
            color='coral',
        ),
        make_node(
            id='phenotype_match',
            label='Both: light coat matches sand',
            detail=(
                'In both coasts the derived pelage is cryptic against white-quartz beach sand. '
                'Vignieri et al. (2010) showed that mice transplanted onto non-matching '
                'substrate suffer substantially higher predation. Convergence on the same '
                'phenotype from two independent populations with different genetic architectures '
                'is the hallmark of parallel evolution.'
            ),
            mnemonic='Same phenotype, different genetic routes — repeatability of selection.',
            watchOut='Parallelism at the phenotypic level does not guarantee parallelism at the genetic level.',
            color='green',
        ),
        make_node(
            id='conclusion',
            label='Parallel evolution',
            detail=(
                'Definition: parallel evolution = independent populations (usually closely '
                'related) evolving the same derived phenotype in response to similar selection. '
                'Beach mice are a textbook example because the derived trait (light pelage), '
                'the selective agent (visual predation on light sand), and the genetic basis '
                '(partly different loci) are all documented by the Hoekstra lab.'
            ),
            mnemonic='Parallel = independent populations + same phenotype + same selective pressure.',
            watchOut=(
                'Parallel = same gene in related lineages. Convergent = different lineages '
                'arriving at similar phenotypes. Beach mice sit on the boundary — same species, '
                'partially different genes.'
            ),
            color='teal',
        ),
    ]
    edges = [
        make_edge('ancestral', 'selection_pressure', label='encounters new habitat', style='arrow'),
        make_edge('selection_pressure', 'gulf', label='selects for light coat (pathway 1)', style='arrow'),
        make_edge('selection_pressure', 'atlantic', label='selects for light coat (pathway 2)', style='arrow'),
        make_edge('gulf', 'phenotype_match', label='via Mc1r + Agouti', style='arrow'),
        make_edge('atlantic', 'phenotype_match', label='via different loci', style='arrow'),
        make_edge('phenotype_match', 'conclusion', label='defines', style='arrow'),
    ]
    return validate_diagram({
        'type': 'flow',
        'title': 'Beach Mice Parallel Evolution — Peromyscus polionotus (Hoekstra lab)',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'MMMP: Mc1r mutation → Melanin loss → Match sand → Predation protection.',
    }, node_id='beach_mice_parallel_evolution')
