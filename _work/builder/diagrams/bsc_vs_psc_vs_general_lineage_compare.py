"""Species concepts — BSC vs PSC vs General Lineage Concept — compare diagram."""

from .types import make_node, make_edge, validate_diagram


def bsc_vs_psc_vs_general_lineage_compare_diagram():
    nodes = [
        # Column headers
        make_node(
            id='bsc_title',
            label='Biological Species Concept (BSC)',
            detail=(
                'The textbook definition for animals. Defines a species by '
                'reproductive isolation — can the populations actually or '
                'potentially interbreed to produce viable, fertile offspring?'
            ),
            mnemonic='BSC = Breeding test',
            color='blue',
        ),
        make_node(
            id='psc_title',
            label='Phylogenetic Species Concept (PSC)',
            detail=(
                'Defines a species as the smallest monophyletic group '
                'diagnosable by shared derived characters. Applies to any '
                'lineage, including asexuals and fossils.'
            ),
            mnemonic='PSC = Phylogeny test',
            color='teal',
        ),
        make_node(
            id='glc_title',
            label='General Lineage Concept (GLC)',
            detail=(
                'Pluralistic — a species is a separately evolving metapopulation '
                'lineage. Integrates BSC, PSC, and ecological criteria. '
                'Recognizes that speciation is a process, not a single moment.'
            ),
            mnemonic='GLC = Lineage test',
            color='purple',
        ),

        # Row: Definition
        make_node(
            id='bsc_def',
            label='Definition: reproductive isolation',
            detail=(
                '"Groups of actually or potentially interbreeding natural '
                'populations which are reproductively isolated from other '
                'such groups." (Mayr 1942)'
            ),
            color='blue',
        ),
        make_node(
            id='psc_def',
            label='Definition: smallest monophyletic group',
            detail=(
                'The smallest diagnosable cluster of individuals with a '
                'parental pattern of ancestry and descent, defined by one or '
                'more shared DERIVED characters (synapomorphies).'
            ),
            color='teal',
        ),
        make_node(
            id='glc_def',
            label='Definition: evolving lineage',
            detail=(
                'Separately evolving metapopulation lineage. A species is '
                'recognized whenever enough evidence (reproductive, '
                'phylogenetic, ecological) points to independent evolution.'
            ),
            color='purple',
        ),

        # Row: Key figure
        make_node(
            id='bsc_author',
            label='Key figure: Ernst Mayr 1942',
            detail=(
                'Formalized in "Systematics and the Origin of Species" (1942). '
                'Became the dominant animal textbook definition for half a '
                'century.'
            ),
            color='blue',
        ),
        make_node(
            id='psc_author',
            label='Key figures: Hennig / Cracraft',
            detail=(
                'Willi Hennig (1966) established cladistic methods; Joel '
                'Cracraft and others applied them to define species as the '
                'smallest diagnosable monophyletic groups.'
            ),
            color='teal',
        ),
        make_node(
            id='glc_author',
            label='Key figure: de Queiroz 1998',
            detail=(
                'Kevin de Queiroz proposed the General Lineage Concept as a '
                'unifying framework showing that all species concepts agree '
                'on the core idea of lineage, disagreeing only on secondary '
                'criteria.'
            ),
            color='purple',
        ),

        # Row: Works for
        make_node(
            id='bsc_works',
            label='Works for: sexual sympatric organisms',
            detail=(
                'Ideal for sexually reproducing species that co-occur — you '
                'can test whether hybrids are viable and fertile in the wild.'
            ),
            color='blue',
        ),
        make_node(
            id='psc_works',
            label='Works for: all life forms',
            detail=(
                'Applies to sexuals, asexuals, fossils, prokaryotes — any '
                'lineage with diagnosable derived characters.'
            ),
            color='teal',
        ),
        make_node(
            id='glc_works',
            label='Works for: all life forms',
            detail=(
                'Applies to any lineage. Different criteria (reproductive, '
                'phylogenetic, ecological) may disagree on borderline cases, '
                'which are flagged rather than forced into a category.'
            ),
            color='purple',
        ),

        # Row: Fails for
        make_node(
            id='bsc_fails',
            label='Fails for: asexuals, fossils, allopatric pops',
            detail=(
                'Asexuals like bdelloid rotifers have no breeding to test. '
                'Fossils (trilobites) cannot be interbred. Allopatric '
                'populations cannot be tested. Hybridizing species (elk × '
                'red deer) break the rule.'
            ),
            color='blue',
        ),
        make_node(
            id='psc_fails',
            label='Fails for: over-splits with many characters',
            detail=(
                'Character choice changes species counts — different '
                'character sets can yield wildly different numbers of '
                'species for the same group. Tends to oversplit when many '
                'characters are examined.'
            ),
            color='teal',
        ),
        make_node(
            id='glc_fails',
            label='Fails for: borderline cases need judgment',
            detail=(
                'When different criteria disagree (e.g., phylogenetically '
                'distinct but reproductively compatible), the concept does '
                'not give a crisp answer — the case must be flagged.'
            ),
            color='purple',
        ),

        # Row: Strength
        make_node(
            id='bsc_strength',
            label='Strength: captures evolutionary independence',
            detail=(
                'Gene flow halts between species, so each lineage evolves '
                'independently. The BSC directly captures this causal '
                'mechanism.'
            ),
            color='blue',
        ),
        make_node(
            id='psc_strength',
            label='Strength: universally applicable',
            detail=(
                'Can be applied to any organism with any reproductive mode '
                'and to fossils. Operational — just needs character data.'
            ),
            color='teal',
        ),
        make_node(
            id='glc_strength',
            label='Strength: pluralistic + process-based',
            detail=(
                'Recognizes speciation as a gradual process and integrates '
                'all available evidence. No forced binary decisions.'
            ),
            color='purple',
        ),

        # Row: Weakness
        make_node(
            id='bsc_weakness',
            label='Weakness: untestable on fossils/asexuals',
            detail=(
                'Cannot be applied to ~half of all biodiversity — prokaryotes, '
                'asexual eukaryotes, and extinct taxa. Reproductive isolation '
                'in allopatry is potential, not observable.'
            ),
            color='blue',
        ),
        make_node(
            id='psc_weakness',
            label='Weakness: "garbage in, garbage out"',
            detail=(
                "Robbins: 'garbage in, garbage out' — different character "
                'sets produce different species counts on the same geckos. '
                'Arbitrariness of character selection undermines objectivity.'
            ),
            color='teal',
        ),
        make_node(
            id='glc_weakness',
            label='Weakness: criteria can conflict',
            detail=(
                'When reproductive, phylogenetic, and ecological criteria '
                'disagree, judgment is required. Not as crisp as BSC or PSC.'
            ),
            color='purple',
        ),

        # Row: Example
        make_node(
            id='bsc_example',
            label='Example: mules (horse × donkey)',
            detail=(
                'Horse (64 chromosomes) × donkey (62) produces mule (63). '
                'Mules are nearly always sterile because unpaired '
                'chromosomes cannot segregate at meiosis. Proves horses '
                'and donkeys are distinct species by the BSC.'
            ),
            color='blue',
        ),
        make_node(
            id='psc_example',
            label='Example: Anopheles gambiae complex',
            detail=(
                'Cryptic mosquito species — morphologically identical, but '
                'distinguishable only by molecular characters. PSC identifies '
                'them as separate species; BSC struggles because they can '
                'occasionally hybridize.'
            ),
            color='teal',
        ),
        make_node(
            id='glc_example',
            label='Example: elk vs red deer',
            detail=(
                'Elk (Cervus canadensis) and red deer (Cervus elaphus) '
                'interbreed freely in captivity but rarely in the wild due '
                'to behavioral and ecological differences. BSC borderline; '
                'GLC recognizes them as separately evolving lineages.'
            ),
            watchOut=(
                'No single species concept works for all organisms. BSC is '
                'standard in animal textbooks but fails for about half of '
                'life (asexuals, prokaryotes, fossils).'
            ),
            color='purple',
        ),
    ]

    edges = [
        make_edge('bsc_title', 'bsc_def', label='row 1', style='arrow'),
        make_edge('psc_title', 'psc_def', label='row 1', style='arrow'),
        make_edge('glc_title', 'glc_def', label='row 1', style='arrow'),
        make_edge('bsc_def', 'bsc_author', label='row 2', style='arrow'),
        make_edge('psc_def', 'psc_author', label='row 2', style='arrow'),
        make_edge('glc_def', 'glc_author', label='row 2', style='arrow'),
        make_edge('bsc_author', 'bsc_works', label='row 3', style='arrow'),
        make_edge('psc_author', 'psc_works', label='row 3', style='arrow'),
        make_edge('glc_author', 'glc_works', label='row 3', style='arrow'),
        make_edge('bsc_works', 'bsc_fails', label='row 4', style='arrow'),
        make_edge('psc_works', 'psc_fails', label='row 4', style='arrow'),
        make_edge('glc_works', 'glc_fails', label='row 4', style='arrow'),
        make_edge('bsc_fails', 'bsc_strength', label='row 5', style='arrow'),
        make_edge('psc_fails', 'psc_strength', label='row 5', style='arrow'),
        make_edge('glc_fails', 'glc_strength', label='row 5', style='arrow'),
        make_edge('bsc_strength', 'bsc_weakness', label='row 6', style='arrow'),
        make_edge('psc_strength', 'psc_weakness', label='row 6', style='arrow'),
        make_edge('glc_strength', 'glc_weakness', label='row 6', style='arrow'),
        make_edge('bsc_weakness', 'bsc_example', label='row 7', style='arrow'),
        make_edge('psc_weakness', 'psc_example', label='row 7', style='arrow'),
        make_edge('glc_weakness', 'glc_example', label='row 7', style='arrow'),
    ]

    return validate_diagram({
        'type': 'compare',
        'title': 'Species Concepts: BSC vs PSC vs General Lineage Concept',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'BSC = Breeding test. PSC = Phylogeny test. GLC = Lineage test. No winner universally.',
    }, node_id='bsc_vs_psc_vs_general_lineage_compare')
