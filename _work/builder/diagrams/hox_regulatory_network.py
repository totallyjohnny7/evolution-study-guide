"""Hox regulatory network — tree diagram (evo-devo toolkit and regulatory change)."""

from .types import make_node, make_edge, validate_diagram


def hox_regulatory_network_diagram():
    nodes = [
        make_node(
            id='hox_ancestor',
            label='Ancestral Hox cluster',
            detail=(
                'The single Hox cluster present in the last common bilaterian ancestor. Encodes '
                'transcription factors that pattern the anterior-posterior body axis. Everything '
                'downstream — flies, mice, humans — descended from this one toolkit.'
            ),
            mnemonic='One toolkit to build them all.',
            color='gray',
        ),
        make_node(
            id='fly_hox',
            label='Drosophila Hox',
            detail=(
                'Fruit flies carry one Hox cluster split into two complexes (Antennapedia and '
                'Bithorax) containing 8 homeotic genes. Classic mutants like Antennapedia '
                '(legs where antennae should be) and Ultrabithorax (four wings) first revealed '
                'Hox function.'
            ),
            value='8 genes',
            mnemonic='Fly Hox made the field.',
            color='coral',
        ),
        make_node(
            id='mouse_hox',
            label='Mouse Hox',
            detail=(
                'Vertebrate Hox was duplicated TWICE during early vertebrate evolution, producing '
                'four clusters (HoxA, HoxB, HoxC, HoxD) with roughly 10 genes each. Redundancy '
                'among paralogs allowed evolutionary flexibility without losing essential functions.'
            ),
            value='4 clusters x ~10 genes',
            mnemonic='Two whole-genome duplications = 4 Hox clusters.',
            color='blue',
        ),
        make_node(
            id='conserved_order',
            label='Colinear arrangement',
            detail=(
                'Hox genes are arranged on the chromosome in the same order in which they are '
                'expressed along the anterior-posterior body axis. 3-prime genes pattern the head, '
                '5-prime genes pattern the tail. This spatial colinearity is conserved from flies '
                'to humans and is unique to Hox clusters.'
            ),
            mnemonic='Chromosome order = body order.',
            color='purple',
        ),
        make_node(
            id='pitx1_stickleback',
            label='Pitx1 regulatory change',
            detail=(
                'Freshwater threespine sticklebacks (Gasterosteus aculeatus) lost their pelvic '
                'spines repeatedly in different lakes. David Kingsley\'s lab showed this was driven '
                'by deletion of a pelvic ENHANCER of the Pitx1 gene, not a change in the coding '
                'sequence. The protein is fine — only its deployment changed.'
            ),
            mnemonic='Same gene, different switch = dropped pelvis.',
            watchOut='Regulatory vs coding evolution are NOT mutually exclusive — both contribute to morphology.',
            color='teal',
        ),
        make_node(
            id='bmp4_finch',
            label='Bmp4 + calmodulin expression',
            detail=(
                'Abzhanov, Tabin, and Grant showed that Galapagos finch beak diversity is produced '
                'by changes in the expression LEVELS of just two proteins: Bmp4 (beak depth and '
                'width) and calmodulin (beak length). Small regulatory tweaks produced the adaptive '
                'radiation Darwin famously documented.'
            ),
            mnemonic='Two knobs, 14 beaks.',
            color='amber',
        ),
        make_node(
            id='distalless',
            label='Distalless (Dll)',
            detail=(
                'Distalless is an appendage-identity gene deployed to build limbs across phyla: '
                'insect legs, crustacean antennae, sea urchin tube feet, vertebrate limbs, '
                'annelid parapodia. A shared developmental logic used wherever the body needs '
                'to grow a projecting structure.'
            ),
            mnemonic='Dll = "build an outgrowth here".',
            color='green',
        ),
    ]
    edges = [
        make_edge('hox_ancestor', 'fly_hox', label='Drosophila lineage', style='arrow'),
        make_edge('hox_ancestor', 'mouse_hox', label='vertebrate lineage (2x WGD)', style='arrow'),
        make_edge('fly_hox', 'conserved_order', label='colinear', style='dashed'),
        make_edge('mouse_hox', 'conserved_order', label='colinear', style='dashed'),
        make_edge('mouse_hox', 'pitx1_stickleback', label='enhancer loss example', style='arrow'),
        make_edge('mouse_hox', 'bmp4_finch', label='expression-level tuning example', style='arrow'),
        make_edge('hox_ancestor', 'distalless', label='appendage toolkit sibling', style='dashed'),
    ]
    return validate_diagram({
        'type': 'tree',
        'title': 'Hox and the Regulatory Toolkit of Evo-Devo',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'Small regulatory changes produce big morphological differences. Same toolkit, different deployment.',
    }, node_id='hox_regulatory_network')
