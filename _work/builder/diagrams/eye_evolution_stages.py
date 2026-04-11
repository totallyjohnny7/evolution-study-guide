"""Eye evolution stages — flow diagram (mollusk lineage + Nilsson-Pelger model)."""

from .types import make_node, make_edge, validate_diagram


def eye_evolution_stages_diagram():
    nodes = [
        make_node(
            id='photoreceptor_patch',
            label='Flat photoreceptor patch',
            detail=(
                'Earliest "eye": a flat layer of opsin-expressing cells on the body surface '
                'that detects the presence or absence of light but gives no directional '
                'information. Modern limpets (Patella) retain this grade.'
            ),
            value='Limpets',
            mnemonic='Light on / light off — nothing more.',
            color='gray',
        ),
        make_node(
            id='pit_eye',
            label='Pit eye',
            detail=(
                'The photoreceptor patch sinks into a cup-shaped depression. The walls of the cup '
                'shadow the receptors differentially, giving crude directional information about '
                'where light is coming from. Seen today in abalone (Haliotis).'
            ),
            value='Abalone',
            mnemonic='Cup walls = directionality.',
            color='teal',
        ),
        make_node(
            id='pinhole_eye',
            label='Pinhole eye',
            detail=(
                'The cup closes further, leaving only a narrow aperture. This pinhole acts like '
                'a camera obscura and forms a crude image on the receptor layer without needing '
                'a lens. The living nautilus (Nautilus pompilius) still uses this design.'
            ),
            value='Nautilus',
            mnemonic='Pinhole camera obscura — no lens required.',
            color='blue',
        ),
        make_node(
            id='lens_eye',
            label='Camera eye with lens',
            detail=(
                'A transparent cover forms over the aperture and differentiates into a lens that '
                'focuses light onto the retina. The octopus lens is built from crystallin proteins '
                'recruited from ancestral heat-shock chaperones — a textbook exaptation.'
            ),
            value='Octopus/Squid',
            mnemonic='Lens = exapted heat-shock protein.',
            color='purple',
        ),
        make_node(
            id='vert_camera_eye',
            label='Vertebrate camera eye',
            detail=(
                'Independently evolved in vertebrates. Identical gross anatomy to the cephalopod '
                'eye but the retina is INVERTED — light passes through the neural layer before '
                'reaching photoreceptors, and the optic nerve exits through the retina creating '
                'a blind spot. Octopuses have no blind spot.'
            ),
            value='Humans',
            mnemonic='Same body plan, opposite wiring.',
            watchOut='CONVERGENT with cephalopod camera eye, NOT homologous — vertebrates have a blind spot, octopuses do not.',
            color='coral',
        ),
        make_node(
            id='pax6_master',
            label='Pax6 master control gene',
            detail=(
                'Pax6 is a transcription factor that sits atop the eye-development gene regulatory '
                'network. It is so conserved that a MOUSE Pax6 gene inserted into a fruit fly '
                'produces an ectopic FLY eye — the downstream wiring is lineage-specific but the '
                'master switch is shared from a common bilaterian ancestor.'
            ),
            mnemonic='Pax6 = eye-building ignition key shared since bilaterians.',
            color='amber',
        ),
        make_node(
            id='nilsson_pelger',
            label='Nilsson & Pelger 1994',
            detail=(
                'Dan Nilsson and Susanne Pelger modeled the gradual reshaping of a flat '
                'photoreceptor patch into a focused camera eye under weak selection (1% fitness '
                'improvement per generation, 0.005% change per step). Result: about 350,000 '
                'generations — geologically almost instantaneous. Directly refutes Darwin\'s '
                'worry that "half an eye" would be useless.'
            ),
            value='~350k gens',
            mnemonic='Half an eye IS useful — and camera eyes evolve in a blink of geologic time.',
            color='green',
        ),
    ]
    edges = [
        make_edge('photoreceptor_patch', 'pit_eye', label='cup forms', style='arrow'),
        make_edge('pit_eye', 'pinhole_eye', label='aperture narrows', style='arrow'),
        make_edge('pinhole_eye', 'lens_eye', label='lens exapted', style='arrow'),
        make_edge('lens_eye', 'vert_camera_eye', label='convergent (independent)', style='dashed'),
        make_edge('pax6_master', 'photoreceptor_patch', label='master switch shared', style='dashed'),
        make_edge('nilsson_pelger', 'lens_eye', label='models timing of this sequence', style='dashed'),
    ]
    return validate_diagram({
        'type': 'flow',
        'title': 'Eye Evolution — From Photoreceptor Patch to Camera Eye',
        'nodes': nodes,
        'edges': edges,
        'mnemonic': 'From patch to camera: each stage provides its own fitness advantage. No "half an eye" problem.',
    }, node_id='eye_evolution_stages')
