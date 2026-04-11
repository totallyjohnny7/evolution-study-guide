"""Cladistics character-state matrix — matrix diagram.

Source: BIOL 4230 Lec 15. Five taxa plus an outgroup scored for four binary
morphological characters. Synapomorphies (shared DERIVED states) are the
evidence that groups taxa into clades. Symplesiomorphies (shared ANCESTRAL
states) are uninformative.
"""

from .types import make_node, make_edge, validate_diagram


def cladistics_character_matrix_diagram():
    nodes = [
        # Row headers — taxa
        make_node(
            id='row_out',
            label='Outgroup',
            detail=(
                'A taxon known from other evidence to have branched off before the '
                'ingroup. By definition carries the ancestral (0) state for all characters '
                'in this matrix. Polarizes character evolution.'
            ),
            color='gray',
        ),
        make_node(
            id='row_A',
            label='Taxon A',
            detail='Ingroup taxon A — scored 1,1,0,1 across the four characters.',
            color='amber',
        ),
        make_node(
            id='row_B',
            label='Taxon B',
            detail='Ingroup taxon B — scored 1,0,0,1 across the four characters.',
            color='amber',
        ),
        make_node(
            id='row_C',
            label='Taxon C',
            detail='Ingroup taxon C — scored 0,1,1,0 across the four characters.',
            color='amber',
        ),
        make_node(
            id='row_D',
            label='Taxon D',
            detail='Ingroup taxon D — scored 0,0,1,0 across the four characters.',
            color='amber',
        ),
        make_node(
            id='row_E',
            label='Taxon E',
            detail='Ingroup taxon E — scored 1,1,0,1 across the four characters (same profile as A).',
            color='amber',
        ),
        # Column headers — characters
        make_node(
            id='col_wings',
            label='Wings',
            detail='Character 1: presence (1) or absence (0) of wings.',
            color='blue',
        ),
        make_node(
            id='col_antennae',
            label='Club antennae',
            detail='Character 2: clubbed (1) vs filiform (0) antennae.',
            color='blue',
        ),
        make_node(
            id='col_elytra',
            label='Elytra',
            detail='Character 3: hardened forewing elytra present (1) or absent (0).',
            color='blue',
        ),
        make_node(
            id='col_mandibles',
            label='Mandibles',
            detail='Character 4: large chewing mandibles present (1) or absent (0).',
            color='blue',
        ),
        # Cells — taxon A row
        make_node(id='A_wings',     label='1', detail='Taxon A has wings (derived).', color='teal'),
        make_node(id='A_antennae',  label='1', detail='Taxon A has club antennae (derived).', color='teal'),
        make_node(id='A_elytra',    label='0', detail='Taxon A lacks elytra (ancestral).', color='gray'),
        make_node(id='A_mandibles', label='1', detail='Taxon A has large mandibles (derived).', color='teal'),
        # Cells — taxon B row
        make_node(id='B_wings',     label='1', detail='Taxon B has wings (derived).', color='teal'),
        make_node(id='B_antennae',  label='0', detail='Taxon B lacks club antennae (ancestral).', color='gray'),
        make_node(id='B_elytra',    label='0', detail='Taxon B lacks elytra (ancestral).', color='gray'),
        make_node(id='B_mandibles', label='1', detail='Taxon B has large mandibles (derived).', color='teal'),
        # Cells — taxon C row
        make_node(id='C_wings',     label='0', detail='Taxon C lacks wings (ancestral).', color='gray'),
        make_node(id='C_antennae',  label='1', detail='Taxon C has club antennae (derived).', color='teal'),
        make_node(id='C_elytra',    label='1', detail='Taxon C has elytra (derived).', color='teal'),
        make_node(id='C_mandibles', label='0', detail='Taxon C lacks large mandibles (ancestral).', color='gray'),
        # Cells — taxon D row
        make_node(id='D_wings',     label='0', detail='Taxon D lacks wings (ancestral).', color='gray'),
        make_node(id='D_antennae',  label='0', detail='Taxon D lacks club antennae (ancestral).', color='gray'),
        make_node(id='D_elytra',    label='1', detail='Taxon D has elytra (derived).', color='teal'),
        make_node(id='D_mandibles', label='0', detail='Taxon D lacks large mandibles (ancestral).', color='gray'),
        # Cells — taxon E row
        make_node(id='E_wings',     label='1', detail='Taxon E has wings (derived).', color='teal'),
        make_node(id='E_antennae',  label='1', detail='Taxon E has club antennae (derived).', color='teal'),
        make_node(id='E_elytra',    label='0', detail='Taxon E lacks elytra (ancestral).', color='gray'),
        make_node(id='E_mandibles', label='1', detail='Taxon E has large mandibles (derived).', color='teal'),
        # Cells — outgroup row
        make_node(id='O_wings',     label='0', detail='Outgroup lacks wings — defines the ancestral state.', color='gray'),
        make_node(id='O_antennae',  label='0', detail='Outgroup lacks club antennae — defines the ancestral state.', color='gray'),
        make_node(id='O_elytra',    label='0', detail='Outgroup lacks elytra — defines the ancestral state.', color='gray'),
        make_node(id='O_mandibles', label='0', detail='Outgroup lacks large mandibles — defines the ancestral state.', color='gray'),
        # Standalone concept nodes
        make_node(
            id='synapomorphy',
            label='Synapomorphy',
            detail=(
                'A shared DERIVED character state — evidence of common ancestry within a '
                'clade. In this matrix, "wings present (1)" is a synapomorphy grouping '
                'A, B, and E together to the exclusion of C and D.'
            ),
            mnemonic='Synapomorphy = Shared + Derived',
            color='green',
        ),
        make_node(
            id='symplesiomorphy',
            label='Symplesiomorphy',
            detail=(
                'A shared ANCESTRAL character state — uninformative for grouping within a '
                'clade, because it was present in the common ancestor and has been retained. '
                '"Lacking elytra (0)" is shared between A, B, E and the outgroup — but tells '
                'us nothing about ingroup relationships.'
            ),
            color='red',
        ),
        make_node(
            id='monophyletic',
            label='Monophyletic group',
            detail=(
                'Ancestor plus ALL of its descendants. The only valid type of taxon in '
                'modern systematics. Defined by at least one synapomorphy.'
            ),
            color='purple',
        ),
        make_node(
            id='tree_count',
            label='Tree topology count',
            value='5 taxa → 105 trees, 9 taxa → 2 million',
            detail=(
                'The number of possible rooted binary trees grows super-exponentially with '
                'taxon count. 3 taxa → 3 trees. 5 taxa → 105 trees. 9 taxa → ~2 million '
                'trees. The search space is astronomical.'
            ),
            watchOut=(
                'Computer algorithms (parsimony, likelihood, Bayesian) are required for '
                'more than ~6 taxa — brute-force enumeration breaks down quickly.'
            ),
            color='coral',
        ),
    ]
    edges = [
        make_edge('col_wings', 'synapomorphy', label='informative', style='dashed'),
        make_edge('col_antennae', 'synapomorphy', label='informative', style='dashed'),
        make_edge('col_elytra', 'symplesiomorphy', label='retained by some', style='dashed'),
        make_edge('synapomorphy', 'monophyletic', label='defines'),
        make_edge('symplesiomorphy', 'monophyletic', label='cannot define', style='dashed'),
        make_edge('monophyletic', 'tree_count', label='best tree search'),
    ]
    return validate_diagram({
        'type': 'matrix',
        'title': 'Cladistics Character-State Matrix',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': "Synapomorphies define clades; symplesiomorphies don't.",
    }, node_id='cladistics_character_matrix')
