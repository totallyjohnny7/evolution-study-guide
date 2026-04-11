"""Feathers evolved before flight — exaptation flow diagram.

Source: BIOL 4230 Lec 16. Feathers first appeared on small non-flying theropod
dinosaurs as insulation, display, and brooding structures. Flight was a later
exaptation — an old structure co-opted for a new function. Archaeopteryx (1860)
is the classic transitional fossil; Oviraptor (1993 brooding posture) and
Velociraptor (quill nodes on the ulna) provide direct fossil evidence of
feathers on non-flying dinosaurs.
"""

from .types import make_node, make_edge, validate_diagram


def feathers_before_flight_exaptation_diagram():
    nodes = [
        make_node(
            id='simple_filaments',
            label='Proto-feather filaments',
            detail=(
                'The first feathers were hair-like down filaments on small theropod '
                'dinosaurs. Arms were far too short to support flight. Preserved in '
                'Liaoning fossils (e.g. Sinosauropteryx) with clear filamentous integument.'
            ),
            color='gray',
        ),
        make_node(
            id='insulation',
            label='Insulation function',
            detail=(
                'Filaments retained body heat — crucial for small endothermic theropods '
                'with high surface-area-to-volume ratios. This is considered the ORIGINAL '
                'function of feathers: thermoregulation, not flight.'
            ),
            color='blue',
        ),
        make_node(
            id='display',
            label='Display / species recognition',
            detail=(
                'Melanosome analysis of fossil feathers reveals bright colors and patterns '
                'in non-flying dinosaurs. Feathers evolved for sexual signaling and species '
                'recognition — analogous to the modern peacock train, which is also far '
                'too heavy for flight.'
            ),
            color='coral',
        ),
        make_node(
            id='brooding',
            label='Egg brooding',
            detail=(
                'An Oviraptor specimen discovered in 1993 was preserved in a brooding '
                'posture directly over a clutch of eggs, arms extended to shield them. '
                'Feathered forelimbs functioned as incubation coverings long before any '
                'flight function.'
            ),
            color='amber',
        ),
        make_node(
            id='velociraptor_quills',
            label='Velociraptor quill nodes',
            detail=(
                'The ulna of Velociraptor preserves regularly spaced quill-attachment '
                'bumps identical to those on the wing bones of modern birds. Direct '
                'fossil evidence of feathers on a non-flying dinosaur — the bone itself '
                'records where the feathers anchored.'
            ),
            color='purple',
        ),
        make_node(
            id='archaeopteryx',
            label='Archaeopteryx 1860',
            value='~145 Mya',
            detail=(
                'The classic transitional fossil, described in 1860 just one year after '
                'Darwin\'s Origin. Shows feathers integrated with an otherwise dinosaurian '
                'skeleton: teeth, claws on the wing, and a long bony tail. First fossil to '
                'demonstrate the intermediate body plan between dinosaurs and modern birds.'
            ),
            color='teal',
        ),
        make_node(
            id='wair_hypothesis',
            label='WAIR: Wing-Assisted Incline Running',
            detail=(
                'Hypothesis proposed by Ken Dial: juvenile ground birds flap their '
                'proto-wings while running up steep surfaces to gain traction. Observed '
                'in modern chukar partridges. Provides a selective pathway for stronger '
                'flight strokes via a function that is useful at every intermediate stage.'
            ),
            color='green',
        ),
        make_node(
            id='flight_exapted',
            label='Flight = exaptation',
            detail=(
                'Feathers evolved FOR insulation, display, and brooding, then were '
                'CO-OPTED for flight. This is the classic definition of exaptation '
                '(Gould & Vrba 1982): an existing structure repurposed for a new function '
                'that did not drive its original evolution.'
            ),
            mnemonic='exaptation = "ex-adaptation" — old structure, new function',
            watchOut=(
                'Exaptation does NOT require gene duplication — it is the same structure, '
                'repurposed. It is also not Lamarckism — the process is still driven by '
                'natural selection on existing variation.'
            ),
            color='red',
        ),
        make_node(
            id='swim_bladder',
            label='Swim bladders ← primitive lungs',
            detail=(
                'A parallel exaptation: early fish had primitive lungs for gulping air in '
                'low-O₂ swamp water. Many fish later modified these into swim bladders for '
                'buoyancy control. Swim bladders are HOMOLOGOUS with tetrapod lungs — same '
                'structure, different function.'
            ),
            color='pink',
        ),
    ]
    edges = [
        make_edge('simple_filaments', 'insulation', label='original function', style='arrow'),
        make_edge('simple_filaments', 'display', label='secondary function', style='arrow'),
        make_edge('simple_filaments', 'brooding', label='secondary function', style='arrow'),
        make_edge('brooding', 'velociraptor_quills', label='fossil evidence'),
        make_edge('velociraptor_quills', 'archaeopteryx', label='next along the lineage'),
        make_edge('archaeopteryx', 'wair_hypothesis', label='possible flight origin'),
        make_edge('wair_hypothesis', 'flight_exapted', label='structure co-opted'),
        make_edge('insulation', 'flight_exapted', label='pre-flight function', style='dashed'),
        make_edge('flight_exapted', 'swim_bladder', label='parallel case', style='dashed'),
    ]
    return validate_diagram({
        'type': 'flow',
        'title': 'Feathers Before Flight — Exaptation in Action',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'Birds ARE dinosaurs. Feathers came first for insulation; flight came later as exaptation.',
    }, node_id='feathers_before_flight_exaptation')
