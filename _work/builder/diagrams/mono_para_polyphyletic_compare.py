"""Monophyletic vs paraphyletic vs polyphyletic — compare diagram.

Source: BIOL 4230 Lec 15. Three taxon-validity categories side-by-side. Only
monophyletic groups (ancestor plus ALL descendants) are valid clades in modern
systematics. "Reptiles" excluding birds is paraphyletic; "warm-blooded animals"
is polyphyletic — neither is a legitimate taxon.
"""

from .types import make_node, make_edge, validate_diagram


def mono_para_polyphyletic_compare_diagram():
    nodes = [
        # Column headers
        make_node(
            id='col_mono',
            label='Monophyletic',
            detail='The only valid type of taxon. Column 1 of the comparison.',
            color='green',
        ),
        make_node(
            id='col_para',
            label='Paraphyletic',
            detail='Invalid — excludes a descendant lineage. Column 2 of the comparison.',
            color='amber',
        ),
        make_node(
            id='col_poly',
            label='Polyphyletic',
            detail='Invalid — groups lineages from independent origins. Column 3 of the comparison.',
            color='red',
        ),
        # Row 1: Definition
        make_node(
            id='def_mono',
            label='Ancestor + ALL descendants',
            detail=(
                'A monophyletic group (clade) consists of a common ancestor and every '
                'descendant of that ancestor without exception. Can be cut from the tree '
                'of life with a single snip.'
            ),
            color='green',
        ),
        make_node(
            id='def_para',
            label='Ancestor + SOME descendants',
            detail=(
                'A paraphyletic group consists of a common ancestor and only some of its '
                'descendants — one or more descendant lineages are excluded. Requires '
                'multiple snips to define.'
            ),
            color='amber',
        ),
        make_node(
            id='def_poly',
            label='Multiple unrelated ancestors',
            detail=(
                'A polyphyletic group is assembled from taxa that do NOT share a recent '
                'common ancestor. The grouping is based on convergent traits rather than '
                'common descent.'
            ),
            color='red',
        ),
        # Row 2: Example
        make_node(
            id='ex_mono',
            label='Birds + crocs + lizards + snakes',
            detail=(
                'Sauropsida (traditional "reptiles" plus birds) is a valid monophyletic '
                'group because it contains the common reptilian ancestor AND all its '
                'descendants — including birds, which ARE dinosaurs.'
            ),
            color='green',
        ),
        make_node(
            id='ex_para',
            label='"Reptiles" excluding birds / "fish" excluding tetrapods',
            detail=(
                'Traditional "Reptilia" excludes birds, leaving turtles, lizards, snakes, '
                'and crocodiles — but crocs are more closely related to birds than to '
                'lizards. Similarly, "fish" as commonly used excludes the tetrapods that '
                'evolved from lobe-finned fish.'
            ),
            color='amber',
        ),
        make_node(
            id='ex_poly',
            label='"Warm-blooded animals" = birds + mammals',
            detail=(
                'Endothermy (warm-bloodedness) evolved independently in the bird lineage '
                '(within dinosaurs) and the mammal lineage (within synapsids). Grouping '
                'them together lumps two independent evolutionary origins.'
            ),
            color='red',
        ),
        # Row 3: Validity
        make_node(
            id='valid_mono',
            label='VALID clade',
            detail='Legitimate taxon. Named and used in modern systematics.',
            color='green',
        ),
        make_node(
            id='valid_para',
            label='INVALID — not a clade',
            detail='Rejected in modern cladistics. May persist as an informal common-usage label.',
            color='amber',
        ),
        make_node(
            id='valid_poly',
            label='INVALID — not a clade',
            detail='Rejected in modern cladistics. Reflects convergence rather than common descent.',
            color='red',
        ),
        # Row 4: Why it fails
        make_node(
            id='fail_mono',
            label='(does not fail)',
            detail='Monophyletic groups are, by definition, valid.',
            color='gray',
        ),
        make_node(
            id='fail_para',
            label='Excludes a descendant lineage',
            detail=(
                'The excluded descendants share a common ancestor with the retained '
                'descendants, so excluding them breaks the "all descendants" requirement.'
            ),
            color='amber',
        ),
        make_node(
            id='fail_poly',
            label='Two independent origins lumped',
            detail=(
                'The shared character evolved convergently in separate lineages. No '
                'recent common ancestor possessed the defining trait.'
            ),
            color='red',
        ),
        # Row 5: Shape hint
        make_node(
            id='shape_mono',
            label='Complete clade',
            detail='A whole subtree — every tip below one chosen internal node.',
            color='green',
        ),
        make_node(
            id='shape_para',
            label='Clade with pieces missing',
            detail='A subtree minus one or more sub-branches that are excluded by the grouping.',
            color='amber',
        ),
        make_node(
            id='shape_poly',
            label='Distant lineages lumped',
            detail='Two or more non-adjacent branches selected from different parts of the tree.',
            color='red',
        ),
        # Key pedagogical call-out
        make_node(
            id='birds_are_dinos',
            label='Birds ARE dinosaurs',
            detail=(
                'To make "reptiles" monophyletic you must include birds, because Aves is '
                'a lineage nested within Sauropsida. Birds are more closely related to '
                'crocodiles than crocodiles are to lizards.'
            ),
            watchOut=(
                '"Fish" as commonly used is PARAPHYLETIC — it excludes tetrapods (which '
                'descend from lobe-finned fish). A monophyletic "fish" group would include '
                'us.'
            ),
            color='blue',
        ),
    ]
    edges = [
        make_edge('col_mono', 'def_mono', label='definition'),
        make_edge('col_para', 'def_para', label='definition'),
        make_edge('col_poly', 'def_poly', label='definition'),
        make_edge('def_mono', 'ex_mono', label='example'),
        make_edge('def_para', 'ex_para', label='example'),
        make_edge('def_poly', 'ex_poly', label='example'),
        make_edge('ex_mono', 'valid_mono', label='validity'),
        make_edge('ex_para', 'valid_para', label='validity'),
        make_edge('ex_poly', 'valid_poly', label='validity'),
        make_edge('valid_mono', 'fail_mono', label='why'),
        make_edge('valid_para', 'fail_para', label='why'),
        make_edge('valid_poly', 'fail_poly', label='why'),
        make_edge('fail_mono', 'shape_mono', label='shape'),
        make_edge('fail_para', 'shape_para', label='shape'),
        make_edge('fail_poly', 'shape_poly', label='shape'),
        make_edge('ex_para', 'birds_are_dinos', label='see also', style='dashed'),
    ]
    return validate_diagram({
        'type': 'compare',
        'title': 'Monophyletic vs Paraphyletic vs Polyphyletic',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'Monophyletic = whole clade. Paraphyletic = missing bits. Polyphyletic = wrong lumping.',
    }, node_id='mono_para_polyphyletic_compare')
