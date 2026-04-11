"""Hawaiian Laupala cricket speciation — song + preference QTL — compare diagram."""

from .types import make_node, make_edge, validate_diagram


def laupala_qtl_compare_diagram():
    nodes = [
        # Column headers
        make_node(
            id='song_title',
            label='Male song pulse rate',
            detail=(
                'Male Laupala crickets produce mating songs by rubbing their '
                'legs together, generating a species-specific pulse rate. '
                'Each species has a discrete, characteristic pulse rate with '
                'no intermediates in the wild.'
            ),
            mnemonic='males sing',
            color='teal',
        ),
        make_node(
            id='pref_title',
            label='Female preference',
            detail=(
                'Female Laupala prefer the pulse rate characteristic of their '
                'own species. Preference and song rate co-vary perfectly '
                'across species — fast-song species have fast-preferring '
                'females.'
            ),
            mnemonic='females choose',
            color='coral',
        ),

        # Song column
        make_node(
            id='song_fast',
            label='Fast pulse rate species',
            detail=(
                'Laupala kohalensis has a fast pulse rate. Pulse rates differ '
                'discretely between sister species in the Big Island '
                'Hawaiian radiation.'
            ),
            value='L. kohalensis',
            color='teal',
        ),
        make_node(
            id='song_slow',
            label='Slow pulse rate species',
            detail=(
                'Laupala paranigra has a slow pulse rate. The species-specific '
                'pulse rates are narrow and do not overlap with their sister '
                'species.'
            ),
            value='L. paranigra',
            color='teal',
        ),
        make_node(
            id='song_mechanism',
            label='Leg-rubbing mechanism',
            detail=(
                'Robbins: "similar to frogs" — males rub their legs together '
                'to produce pulse song, and females respond based on '
                'species-specific preference. The general mechanism '
                'parallels anuran advertisement call systems.'
            ),
            mnemonic='cricket leg = frog call',
            color='teal',
        ),
        make_node(
            id='song_discrete',
            label='Discrete species differences',
            detail=(
                'No intermediate pulse rates are found in nature. The '
                'transition between species-typical rates is sharp, not a '
                'continuous gradient.'
            ),
            color='teal',
        ),
        make_node(
            id='song_qtl',
            label='Song QTL',
            detail=(
                'Quantitative trait locus mapping (Shaw lab) places pulse '
                'rate control on a specific chromosomal region in the '
                'Laupala genome. The effect sizes are concentrated rather '
                'than spread across many small loci.'
            ),
            color='teal',
        ),

        # Preference column
        make_node(
            id='pref_conspec',
            label='Prefers conspecific pulse',
            detail=(
                'Female phonotaxis assays show clear preference for the '
                'conspecific male pulse rate over non-conspecific rates. '
                'Preference is not learned.'
            ),
            color='coral',
        ),
        make_node(
            id='pref_covary',
            label='Preference co-varies with song',
            detail=(
                'Across the Hawaiian Laupala radiation, female preference '
                'values track male song values. Fast-song species have '
                'fast-preferring females; slow-song species have '
                'slow-preferring females.'
            ),
            color='coral',
        ),
        make_node(
            id='pref_qtl',
            label='Preference QTL — SAME region',
            detail=(
                'Shaw lab QTL mapping (Shaw et al.) places the female '
                'preference locus in the SAME chromosomal region as the '
                'male song locus. Song and preference are genetically '
                'linked — possibly controlled by the same gene or a tight '
                'cluster.'
            ),
            mnemonic='linkage locks isolation',
            color='coral',
        ),
        make_node(
            id='pref_single_mut',
            label='One mutation shifts BOTH',
            detail=(
                'Because song and preference map to the same locus, a single '
                'mutation can shift male song and female preference together. '
                'This bypasses the usual problem with sympatric speciation: '
                'preference and signal have to evolve simultaneously.'
            ),
            color='coral',
        ),
        make_node(
            id='pref_linked',
            label='Linkage drives rapid speciation',
            detail=(
                'Genetic linkage between signal and preference means '
                'recombination cannot break them apart — reproductive '
                'isolation can arise in one or a few generations, allowing '
                'sympatric-like speciation.'
            ),
            watchOut=(
                'When song and preference map to the SAME locus, a single '
                'mutation can establish reproductive isolation in one '
                'generation — that is why Laupala speciates so fast.'
            ),
            color='coral',
        ),

        # Context nodes
        make_node(
            id='big_island',
            label='Big Island endemism',
            value='6 spp / 430 kyr',
            detail=(
                'Six Laupala species arose on the Big Island of Hawaii '
                'alone in ~430,000 years — about 10× the average arthropod '
                'speciation rate. One of the fastest documented animal '
                'radiations.'
            ),
            mnemonic='10× arthropod rate',
            color='amber',
        ),
        make_node(
            id='robbins_quote',
            label="Robbins: 'similar to frogs'",
            detail=(
                'Robbins draws a parallel to frog call systems: male signal '
                'plus female preference at discrete species-specific values. '
                'The Laupala system is the cricket version of frog call '
                'divergence.'
            ),
            color='purple',
        ),
        make_node(
            id='two_colonizations',
            label='Two independent colonizations',
            detail=(
                'Phylogeny shows TWO independent Laupala colonizations of '
                'the Big Island. The rapid song-and-preference speciation '
                'has occurred repeatedly — not as a single lucky event.'
            ),
            color='purple',
        ),
    ]

    edges = [
        make_edge('song_title', 'song_fast', label='fast end', style='arrow'),
        make_edge('song_title', 'song_slow', label='slow end', style='arrow'),
        make_edge('song_fast', 'song_mechanism', label='how', style='arrow'),
        make_edge('song_slow', 'song_mechanism', label='how', style='arrow'),
        make_edge('song_mechanism', 'song_discrete', label='pattern', style='arrow'),
        make_edge('song_discrete', 'song_qtl', label='genetic basis', style='arrow'),
        make_edge('pref_title', 'pref_conspec', label='behavior', style='arrow'),
        make_edge('pref_conspec', 'pref_covary', label='pattern', style='arrow'),
        make_edge('pref_covary', 'pref_qtl', label='genetic basis', style='arrow'),
        make_edge('pref_qtl', 'pref_single_mut', label='consequence', style='arrow'),
        make_edge('pref_single_mut', 'pref_linked', label='consequence', style='arrow'),
        make_edge('song_qtl', 'pref_qtl', label='SAME locus', style='dashed'),
        make_edge('pref_linked', 'big_island', label='enables', style='dashed'),
        make_edge('big_island', 'two_colonizations', label='repeated', style='dashed'),
        make_edge('song_mechanism', 'robbins_quote', label='analogy', style='dashed'),
    ]

    return validate_diagram({
        'type': 'compare',
        'title': 'Laupala Cricket Speciation — Song + Preference Linked QTL',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'Song + preference at the same QTL → one mutation shifts both → rapid sympatric speciation.',
    }, node_id='laupala_qtl_compare')
