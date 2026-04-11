"""Life-history schedule across species — r/K timeline diagram.

Source: BIOL 4230 Lec 12. r-selected species (left) mature fast and live short
lives; K-selected species (right) mature slowly and live long lives. Real
species with measured ages at first reproduction and lifespan.
"""

from .types import make_node, make_edge, validate_diagram


def life_history_r_k_timeline_diagram():
    nodes = [
        make_node(
            id='adactylidium',
            label='Adactylidium mite',
            value='mature at hatching, dies ~4 days',
            detail=(
                'The most extreme r-strategist known. Offspring are inseminated by their '
                'brothers while still inside the mother, then eat their way out of her body '
                'at ~4 days old. The entire life cycle is compressed into days.'
            ),
            x=0.0,
            color='coral',
        ),
        make_node(
            id='mayfly',
            label='Mayfly',
            value='hours, thousands of eggs',
            detail=(
                'Adult mayflies live only hours to a few days. They do not feed — adults '
                'have no functional mouthparts. Entire adult existence is mating and egg-laying. '
                'Females lay thousands of eggs in a single event (semelparity).'
            ),
            x=0.08,
            color='coral',
        ),
        make_node(
            id='mouse',
            label='House mouse',
            value='1st repro ~6 weeks',
            detail=(
                'Mus musculus reaches sexual maturity at ~6 weeks and can produce a litter '
                'every 3 weeks thereafter. A single female can theoretically produce 60+ '
                'offspring per year. High extrinsic mortality from predators selects for '
                'early and fast reproduction.'
            ),
            x=0.15,
            color='coral',
        ),
        make_node(
            id='rabbit',
            label='Rabbit',
            value='~6 months',
            detail=(
                'Rabbits reach sexual maturity at ~6 months and produce multiple litters '
                'per year. The classic r-selected mammal — large litters, little parental '
                'investment post-weaning, short lifespan in the wild (~1–2 years).'
            ),
            mnemonic='r = rabbit',
            x=0.22,
            color='coral',
        ),
        make_node(
            id='guppy_hi',
            label='Guppy (high predation)',
            value='11 years to evolve earlier maturation',
            detail=(
                'David Reznick transplanted guppies from high-predation streams (Crenicichla '
                'predator) to low-predation streams (Rivulus predator). In just 11 years the '
                'transplanted populations evolved LATER maturation and LARGER body size. '
                'Confirms r/K shifts evolve in real time under measurable selection.'
            ),
            x=0.3,
            color='amber',
        ),
        make_node(
            id='opossum_main',
            label='Mainland opossum',
            value='high predation, fast aging',
            detail=(
                'Steve Austad studied Virginia opossums in Georgia. Mainland populations '
                'face heavy predation from coyotes and vehicles — senescence is fast, '
                'lifespan is short. Classic high-extrinsic-mortality phenotype.'
            ),
            x=0.38,
            color='amber',
        ),
        make_node(
            id='opossum_island',
            label='Sepelo Island opossum',
            value='~5000 yr low predation, slow aging',
            detail=(
                'Austad\'s key comparison: opossums isolated on Sepelo Island (Georgia) '
                'for ~5000 years in the absence of mammalian predators. They evolved '
                'SLOWER aging and longer lifespans than mainland populations. Real-time '
                'evolution of the rate of senescence.'
            ),
            x=0.5,
            color='amber',
        ),
        make_node(
            id='elephant',
            label='Elephant',
            value='1st repro ~10-12 yr, 1 calf / ~5 yr',
            detail=(
                'African elephants reach first reproduction at 10–12 years and produce '
                'one calf every ~5 years. Long gestation (22 months). Heavy maternal and '
                'matriarchal investment in each offspring. Lifespan 60–70 years in the wild.'
            ),
            x=0.7,
            color='teal',
        ),
        make_node(
            id='kiwi',
            label='Kiwi bird',
            value='1 huge egg / season',
            detail=(
                'Kiwi lay a single enormous egg (up to 20% of the female body mass — '
                'the largest egg:body ratio of any bird). Extreme parental investment in '
                'one offspring at a time. Classic K strategy in birds.'
            ),
            mnemonic='Extreme K strategy',
            x=0.78,
            color='teal',
        ),
        make_node(
            id='human',
            label='Human',
            value='~18 yr childhood',
            detail=(
                'Humans have the longest childhood of any primate — ~18 years of '
                'dependence. First reproduction usually 15–25 years. Extreme parental '
                'investment per offspring, including grandparental care (grandmother '
                'hypothesis). Lifespan 70+ years.'
            ),
            x=0.85,
            color='teal',
        ),
        make_node(
            id='bristlecone',
            label='Bristlecone pine',
            value='>4000 yr lifespan',
            detail=(
                'Pinus longaeva — the oldest non-clonal organisms on Earth. Methuselah is '
                '~4855 years old. Slow growth, dense wood, extreme longevity. Reproduce '
                'iteroparously over millennia. The extreme K endpoint.'
            ),
            mnemonic='K = K-apes... and K-trees',
            watchOut=(
                'r/K is a CONTINUUM, not a binary. Most species fall somewhere between '
                'the extremes.'
            ),
            x=1.0,
            color='teal',
        ),
    ]
    return validate_diagram({
        'type': 'timeline',
        'title': 'Life-History Schedule — r/K Continuum Across Species',
        'nodes': nodes,
        'edges': [],
        'mnemonic': 'Live fast die young (r) OR slow steady reproduce forever (K). Energy is finite either way.',
    }, node_id='life_history_r_k_timeline')
