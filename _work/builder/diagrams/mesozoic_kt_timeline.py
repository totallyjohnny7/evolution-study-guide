"""Mesozoic era + K-Pg boundary + Cenozoic recovery — timeline diagram."""

from .types import make_node, make_edge, validate_diagram


def mesozoic_kt_timeline_diagram():
    # x mapping: 0 = 252 Mya (start Triassic), 1 = present (0 Mya)
    # x = (252 - mya) / 252

    nodes = [
        make_node(
            id='triassic',
            label='Triassic 250-202 Mya',
            value='First dinosaurs 230 Mya',
            detail=(
                'First true DINOSAURS appear ~230 Mya. Marine environments '
                'dominated by plesiosaurs and ichthyosaurs. The synapsid '
                'lineage continues as small cynodonts — mammal ancestors '
                'that were small, likely nocturnal, and coexisted with '
                'dinosaurs for ~150 Myr.'
            ),
            mnemonic='HARD — Triassic',
            x=0.08,
            color='amber',
        ),
        make_node(
            id='tr_jr_ext',
            label='End-Triassic extinction',
            value='~201 Mya',
            detail=(
                'Mass extinction at the Triassic-Jurassic boundary. Clears out '
                'competing archosaur groups (phytosaurs, rauisuchians) and '
                'allows dinosaurs to dominate terrestrial ecosystems in the '
                'Jurassic.'
            ),
            x=0.20,
            color='red',
        ),
        make_node(
            id='jurassic',
            label='Jurassic 202-145 Mya',
            value='Age of Dinosaurs',
            detail=(
                'Massive diversification of dinosaurs — sauropods, stegosaurs, '
                'theropods. Birds arose WITHIN Dinosauria from small coelurosaurian '
                'theropods ~150 Mya. Archaeopteryx is the classic transitional '
                'fossil showing feathers, teeth, and a long bony tail.'
            ),
            mnemonic='CASH — (Jurassic, then Cretaceous); birds ARE dinosaurs',
            x=0.30,
            color='green',
        ),
        make_node(
            id='archaeopteryx',
            label='Archaeopteryx ~150 Mya',
            value='first bird',
            detail=(
                'Feathers + teeth + claws on wings + long bony tail. Found in '
                'Solnhofen limestone, Germany. Mosaic transitional fossil '
                'linking non-avian dinosaurs to modern birds.'
            ),
            x=0.38,
            color='teal',
        ),
        make_node(
            id='cretaceous',
            label='Cretaceous 145-65 Mya',
            value='Angiosperms 132 Mya',
            detail=(
                'Flowering plants (angiosperms) appear ~132 Mya and rapidly '
                'diversify, driving massive insect coevolution. Primate '
                'trichromatic color vision later evolves to detect ripe fruit '
                'against green foliage. Dinosaurs reach peak diversity just '
                'before the K-Pg boundary.'
            ),
            x=0.52,
            color='pink',
        ),
        make_node(
            id='kt',
            label='K-Pg boundary 66 Mya',
            value='Chicxulub asteroid',
            detail=(
                '~10 mile (15 km) asteroid strike at Chicxulub, Yucatán '
                'Peninsula. Global iridium anomaly layer worldwide confirms '
                'extraterrestrial origin. ~2/3 of species went extinct. All '
                'non-avian dinosaurs wiped out; only the avian dinosaur lineage '
                '(birds) survived.'
            ),
            mnemonic="'K' from German Kreide (chalk)",
            watchOut=(
                'Birds ARE dinosaurs — the only surviving dinosaur lineage. '
                '"Dinosaurs went extinct" only applies to non-avian dinosaurs.'
            ),
            x=0.76,
            color='red',
        ),
        make_node(
            id='cenozoic',
            label='Cenozoic 66 Mya - now',
            value='Age of Mammals',
            detail=(
                'Mammalian adaptive radiation into ecological niches vacated '
                'by non-avian dinosaurs. ~50 Mya: first primates. ~20 Mya: '
                'first apes. ~7 Mya: first hominins. ~195 kya: anatomically '
                'modern Homo sapiens.'
            ),
            x=0.86,
            color='purple',
        ),
        make_node(
            id='hominins',
            label='Hominins ~7 Mya',
            value='bipedal lineage',
            detail=(
                'First bipedal primate lineage separates from the chimpanzee '
                'lineage ~7 Mya (Sahelanthropus, Orrorin). Leads eventually '
                'to Australopithecus, Homo, and modern humans.'
            ),
            x=0.96,
            color='green',
        ),
    ]

    edges = [
        make_edge('triassic', 'tr_jr_ext', label='extinction', style='arrow'),
        make_edge('tr_jr_ext', 'jurassic', label='dinosaur rise', style='arrow'),
        make_edge('jurassic', 'archaeopteryx', label='birds evolve', style='dashed'),
        make_edge('archaeopteryx', 'cretaceous', label='→ 145 Mya', style='arrow'),
        make_edge('cretaceous', 'kt', label='asteroid impact', style='arrow'),
        make_edge('kt', 'cenozoic', label='mammal radiation', style='arrow'),
        make_edge('cenozoic', 'hominins', label='bipedal split', style='arrow'),
    ]

    return validate_diagram({
        'type': 'timeline',
        'title': 'Mesozoic Era + K-Pg Boundary + Cenozoic — 252 Mya to Present',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'Mesozoic → K-Pg asteroid → mammals radiate → us.',
    }, node_id='mesozoic_kt_timeline')
