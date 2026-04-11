"""TSD Charnov-Bull model — flow diagram (Warner & Shine 2008 jacky dragon)."""

from .types import make_node, make_edge, validate_diagram


def tsd_charnov_bull_diagram():
    nodes = [
        make_node(
            id='egg_temp',
            label='Egg incubation temperature',
            detail=(
                'In TSD species the temperature experienced by the egg during a critical '
                'developmental window sets the phenotypic sex of the hatchling. Warner & Shine '
                'used three treatments: 23 degC, 27 degC, and 33 degC across six outdoor enclosures.'
            ),
            value='23/27/33 degC',
            mnemonic='Nest thermometer decides sex.',
            watchOut='The "pivotal temperature" differs by species and even by population.',
            color='amber',
        ),
        make_node(
            id='sex_determined',
            label='Sex determined at pivotal temp',
            detail=(
                'Crossing the pivotal temperature during the thermosensitive window flips the '
                'developmental switch that produces ovaries vs testes. No sex chromosomes '
                'required — the gonad path is chosen by thermal input to aromatase expression.'
            ),
            mnemonic='Pivotal temp = the tipping point.',
            color='amber',
        ),
        make_node(
            id='tsd_vs_gsd',
            label='TSD vs GSD',
            detail=(
                'TSD = temperature-dependent sex determination (reptiles, some fish). '
                'GSD = genotypic sex determination (mammals XY, birds ZW). Both produce sexed '
                'offspring but GSD is insensitive to nest temperature while TSD is entirely driven by it.'
            ),
            mnemonic='TSD thermometer vs GSD genome.',
            watchOut='Some species have BOTH — genotype can be overridden by extreme temperatures.',
            color='gray',
        ),
        make_node(
            id='charnov_bull',
            label='Charnov-Bull model',
            detail=(
                'Charnov & Bull (1977) predicted that TSD is adaptive when egg environment '
                'differentially affects MALE vs FEMALE fitness. If warm nests produce fitter males '
                'and cool nests produce fitter females (or vice versa), matching sex to temperature '
                'beats random assignment.'
            ),
            mnemonic='Temperature matters DIFFERENTLY for sons vs daughters.',
            color='purple',
        ),
        make_node(
            id='jacky_exp',
            label='Jacky dragon experiment',
            detail=(
                'Warner & Shine 2008 Nature tracked reproductive success of jacky dragons '
                '(Amphibolurus muricatus) hatched at 23, 27, and 33 degC. High-temperature males '
                'and low-temperature females had the highest lifetime reproductive success — '
                'the first direct test confirming the Charnov-Bull prediction.'
            ),
            value='Warner & Shine 2008',
            mnemonic='Jacky dragon = Charnov-Bull vindicated.',
            color='teal',
        ),
        make_node(
            id='aromatase_inhibitor',
            label='Aromatase inhibitor override',
            detail=(
                'Warner & Shine dosed eggs with an aromatase inhibitor (fadrozole) that blocks '
                'the temperature-driven conversion of androgens to estrogens. This decoupled sex '
                'from temperature, allowing the team to produce "wrong-temperature males" and '
                '"wrong-temperature females" and measure their fitness directly.'
            ),
            mnemonic='Drug breaks the temp-sex link so we can test it.',
            watchOut='Without the aromatase trick, temperature and sex are perfectly correlated — cannot separate their effects.',
            color='coral',
        ),
        make_node(
            id='climate_threat',
            label='Climate change sex-ratio skew',
            detail=(
                'In TSD species like green sea turtles (Chelonia mydas), rising sand temperatures '
                'have already pushed northern Great Barrier Reef nests above 99% female. Similar '
                'feminization threatens crocodilians, tuatara, and many lizards — climate-driven '
                'sex ratios can collapse populations faster than any other effect.'
            ),
            watchOut='Rising temperatures in TSD species like sea turtles can produce all-female nests and cause population collapse.',
            color='red',
        ),
    ]
    edges = [
        make_edge('egg_temp', 'sex_determined', label='thermosensitive window', style='arrow'),
        make_edge('sex_determined', 'tsd_vs_gsd', label='contrasts with', style='solid'),
        make_edge('sex_determined', 'charnov_bull', label='requires adaptive explanation', style='arrow'),
        make_edge('charnov_bull', 'jacky_exp', label='predicted and confirmed by', style='arrow'),
        make_edge('jacky_exp', 'aromatase_inhibitor', label='experimental tool used', style='arrow'),
        make_edge('charnov_bull', 'climate_threat', label='breaks down under climate change', style='dashed'),
    ]
    return validate_diagram({
        'type': 'flow',
        'title': 'Temperature-Dependent Sex Determination — Charnov-Bull Model',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'Charnov-Bull: TSD is adaptive when temperature x sex-specific fitness interaction differs. TSD is a DERIVED trait — evolved independently multiple times.',
    }, node_id='tsd_charnov_bull')
