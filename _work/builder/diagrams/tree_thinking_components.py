"""Components of a phylogenetic tree — tree diagram.

Source: BIOL 4230 Lec 15. Darwin 1837 sketched the first phylogenetic tree in
his B Notebook with the famous "I think" annotation. A modern cladogram has a
small fixed vocabulary: tip, branch, internal node, root, clade, sister taxa.
"""

from .types import make_node, make_edge, validate_diagram


def tree_thinking_components_diagram():
    nodes = [
        make_node(
            id='root',
            label='Root / outgroup',
            detail=(
                'The base of the tree, chosen to polarize character states. The outgroup '
                'is a taxon known (from other evidence) to have diverged before the rest '
                'of the ingroup — it defines which states are ancestral and which are derived.'
            ),
            color='gray',
        ),
        make_node(
            id='internal_node',
            label='Internal node (speciation event)',
            detail=(
                'Represents an inferred common ancestor — NOT a direct fossil, just a '
                'logical split point where one lineage became two. Supported by shared '
                'derived characters (synapomorphies) in the descendants.'
            ),
            color='purple',
        ),
        make_node(
            id='branch',
            label='Branch',
            detail=(
                'A lineage persisting through time between splits. Length may represent '
                'time or amount of character change. A branch does NOT imply "primitive" '
                'or "advanced" — it just traces ancestry.'
            ),
            color='teal',
        ),
        make_node(
            id='tip',
            label='Tip (terminal taxon)',
            detail=(
                'A present-day species, population, or molecular sequence at the end of a '
                'branch. Tips are what we actually observe; internal nodes and roots are '
                'inferred.'
            ),
            color='amber',
        ),
        make_node(
            id='clade',
            label='Clade / monophyletic group',
            detail=(
                'An ancestor plus ALL of its descendants. The only valid type of taxonomic '
                'group in modern phylogenetic systematics. A clade can be cut from a tree '
                'with a single scissor snip.'
            ),
            mnemonic='clade = complete family tree branch',
            color='green',
        ),
        make_node(
            id='sister_taxa',
            label='Sister taxa',
            detail=(
                'Two lineages sharing an immediate common ancestor — i.e., separated by '
                'exactly one internal node. Humans and chimps are sister taxa. Sisters '
                'share a more recent ancestor with each other than with any other taxon.'
            ),
            color='blue',
        ),
        make_node(
            id='snail_islands',
            label='Robbins snail island example',
            detail=(
                'Population 1 colonizes island 2 (pink form), which then seeds island 3 '
                '(high-spire form), which in turn seeds island 4. On a phylogeny, the '
                'populations on islands 3 and 4 are sister taxa — more closely related to '
                'each other than either is to the population on island 1.'
            ),
            watchOut=(
                'Current island-1 snails are NOT the ancestors of islands 3 and 4 — modern '
                'tips are cousins, not ancestors. Every living taxon is at a tip, never at '
                'a node.'
            ),
            color='coral',
        ),
        make_node(
            id='rotation_free',
            label='Node rotations are free',
            detail=(
                'Rotating any internal node around its pivot does not change the phylogeny. '
                'Only the TOPOLOGY (who shares an ancestor with whom) matters — not the '
                'left-right arrangement of tips on the page. Two trees that look different '
                'may be identical phylogenies.'
            ),
            watchOut=(
                'NEVER read trees left-to-right as "progress." There is no "highest" or '
                '"most evolved" tip. Every tip has had exactly the same amount of evolution '
                'since the root.'
            ),
            color='red',
        ),
    ]
    edges = [
        make_edge('root', 'internal_node', label='base of tree', style='arrow'),
        make_edge('internal_node', 'branch', label='connects via', style='arrow'),
        make_edge('branch', 'tip', label='ends at', style='arrow'),
        make_edge('internal_node', 'clade', label='defines'),
        make_edge('internal_node', 'sister_taxa', label='separates'),
        make_edge('clade', 'snail_islands', label='illustrated by'),
        make_edge('sister_taxa', 'snail_islands', label='islands 3 & 4 are'),
        make_edge('internal_node', 'rotation_free', label='topology rule', style='dashed'),
    ]
    return validate_diagram({
        'type': 'tree',
        'title': 'Tree-Thinking — Components of a Phylogeny',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'Tip, Branch, Node, Root, Clade — the five words that describe any phylogeny.',
    }, node_id='tree_thinking_components')
