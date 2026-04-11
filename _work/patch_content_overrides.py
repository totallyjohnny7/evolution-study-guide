"""patch_content_overrides.py — Per-node content customization.

Adds:
1. CLADO_OVERRIDES dict: node title -> custom {taxa, group_member, group_label,
   axis_start, axis_end, character_marks} so each cladogram is SPECIFIC to its
   topic (Tiktaalik shows Fish->Tiktaalik->Amphibian->Tetrapod, Human Evolution
   shows Chimp->Australopithecus->H. erectus->H. sapiens, etc.)

2. TIMELINE_OVERRIDES dict: node title -> custom {era_labels, era_dates, axis_start_mya}
   so each timeline zooms to its specific period (Cambrian timeline shows just
   Cambrian/Ordovician/Silurian/Devonian, Mesozoic shows Triassic/Jurassic/Cretaceous/Paleogene).

3. Modifies svg_cladogram to use CLADO_OVERRIDES[node['title']]
4. Modifies svg_timeline to use TIMELINE_OVERRIDES[node['title']]
"""
import re

PATH = '_work/enrich_v3.py'

with open(PATH, 'r', encoding='utf-8') as f:
    src = f.read()

# ============================================================================
# Insert overrides dict BEFORE svg_cladogram
# ============================================================================

OVERRIDES_BLOCK = '''
# -- per-node content overrides (per lecture variation) --------------------

# For cladogram nodes: real taxa instead of generic "Species A/B/C/D".
# The mapping is by node title substring.
CLADO_OVERRIDES = {
    'Tree Thinking': {
        'taxa': ['Taxon 1', 'Taxon 2', 'Taxon 3', 'Taxon 4'],
        'group_members': ['A', 'B'],
        'group_label': 'Clade',
        'subtitle': 'How to read a phylogenetic tree: tips, nodes, clades, root',
        'character_marks': [],
    },
    'Cladistics': {
        'taxa': ['Mammals', 'Birds', 'Reptiles', 'Fish'],
        'group_members': ['A', 'B', 'C'],
        'group_label': 'Amniotes (monophyletic)',
        'subtitle': 'Amniotic egg = synapomorphy uniting mammals + birds + reptiles',
        'character_marks': [
            ('trunk_to_n1', 'egg', 'Amniotic egg'),
            ('tipA', 'hand', 'Hair/milk'),
            ('tipB', 'feather', 'Feathers'),
        ],
    },
    'Parsimony': {
        'taxa': ['Shark', 'Dolphin', 'Tuna', 'Seal'],
        'group_members': ['B', 'D'],
        'group_label': 'Streamlined body (homoplasy)',
        'subtitle': 'Convergence: shark + dolphin both streamlined, but not closest relatives',
        'character_marks': [
            ('tipB', 'fish', 'Fins (convergent)'),
            ('tipD', 'fish', 'Fins (convergent)'),
        ],
    },
    'Fins to Limbs': {
        'taxa': ['Fish', 'Tiktaalik', 'Amphibian', 'Tetrapod'],
        'group_members': ['B', 'C', 'D'],
        'group_label': 'Tetrapod lineage (limbed)',
        'subtitle': 'Tiktaalik (375 Mya) = transitional fish with limb-like fins',
        'character_marks': [
            ('tipB', 'bone', 'Proto-limbs'),
            ('tipC', 'leg', 'True limbs'),
            ('tipD', 'footprints', 'Walking'),
        ],
    },
    'Feathers': {
        'taxa': ['Theropod', 'Feathered Dino', 'Archaeopteryx', 'Modern Bird'],
        'group_members': ['B', 'C', 'D'],
        'group_label': 'Feathered clade',
        'subtitle': 'Feathers evolved ~160 Mya before flight; exapted for flight in birds',
        'character_marks': [
            ('tipB', 'feather', 'Proto-feathers'),
            ('tipC', 'feather', 'Flight feathers'),
            ('tipD', 'bird', 'Powered flight'),
        ],
    },
    'Human Evolution': {
        'taxa': ['Chimpanzee', 'Australopithecus', 'H. erectus', 'H. sapiens'],
        'group_members': ['B', 'C', 'D'],
        'group_label': 'Hominin lineage',
        'subtitle': 'Bipedalism first (~6 Mya), then brain expansion (~2 Mya)',
        'character_marks': [
            ('tipB', 'footprints', 'Bipedalism'),
            ('tipC', 'brain', 'Big brain'),
            ('tipD', 'atom', 'Culture'),
        ],
    },
    'Descent with Modification': {
        'taxa': ['Wolf', 'Dog', 'Coyote', 'Fox'],
        'group_members': ['A', 'B', 'C'],
        'group_label': 'Canid family',
        'subtitle': 'Common descent + modification explains observable diversity',
        'character_marks': [
            ('trunk_top', 'dna', 'Shared DNA'),
        ],
    },
}


# For timeline nodes: per-topic era labels + dates.
TIMELINE_OVERRIDES = {
    'Pre-Darwin': {
        'era_labels': ['Greeks', 'Medieval', 'Renaissance', 'Pre-Darwin'],
        'era_dates':  ['-500 BCE', '500-1500', '1500-1750', '1750-1859'],
        'axis_past':  'ANCIENT',
        'axis_now':   '1859',
        'subtitle':   'From Aristotle\\'s Scala Naturae to Lamarck — ideas before Darwin',
    },
    'Voyage of the Beagle': {
        'era_labels': ['Departure', 'S. America', 'Galápagos', 'Return'],
        'era_dates':  ['1831', '1832-1835', '1835', '1836'],
        'axis_past':  'DEC 1831',
        'axis_now':   'OCT 1836',
        'subtitle':   'Darwin\\'s 5-year voyage gathering the evidence for Origin',
    },
    'Age of the Earth': {
        'era_labels': ['PRECAMBRIAN', 'PALEOZOIC', 'MESOZOIC', 'CENOZOIC'],
        'era_dates':  ['4600-541 Mya', '541-252 Mya', '252-66 Mya', '66-0 Mya'],
        'axis_past':  '4.6 BYA',
        'axis_now':   'NOW',
        'subtitle':   'Earth = 4.568 billion years; most of that is Precambrian',
    },
    'Origin of Life': {
        'era_labels': ['Hadean', 'Early Archean', 'Late Archean', 'Proterozoic'],
        'era_dates':  ['4600-4000', '4000-3500', '3500-2500', '2500-541'],
        'axis_past':  '4.6 BYA',
        'axis_now':   '541 MYA',
        'subtitle':   'Abiogenesis: prebiotic chemistry → RNA world → LUCA',
    },
    'Early Life': {
        'era_labels': ['Stromatolites', 'GOE', 'Eukaryotes', 'Multicellular'],
        'era_dates':  ['3500 Mya', '2400 Mya', '1800 Mya', '1000 Mya'],
        'axis_past':  '3.5 BYA',
        'axis_now':   '541 MYA',
        'subtitle':   'First cells → oxygen → eukaryotes → multicellularity',
    },
    'Cambrian Explosion': {
        'era_labels': ['Cambrian', 'Ordovician', 'Silurian', 'Devonian'],
        'era_dates':  ['541-485', '485-443', '443-419', '419-359'],
        'axis_past':  '541 MYA',
        'axis_now':   '359 MYA',
        'subtitle':   'Cambrian explosion: all major animal phyla in ~25 Myr',
    },
    'Mesozoic': {
        'era_labels': ['Triassic', 'Jurassic', 'Cretaceous', 'Cenozoic'],
        'era_dates':  ['252-201', '201-145', '145-66', '66-0'],
        'axis_past':  '252 MYA',
        'axis_now':   'NOW',
        'subtitle':   'Age of dinosaurs → K-T extinction → Age of mammals',
    },
}

'''

# Insert right before 'def svg_cladogram'
insert_at = src.index('def svg_cladogram(node):')
src = src[:insert_at] + OVERRIDES_BLOCK + '\n' + src[insert_at:]
print(f'Inserted overrides block. Size: {len(src):,}')

# ============================================================================
# Modify svg_cladogram to use CLADO_OVERRIDES
# ============================================================================

# Find the cladogram's docstring and add override lookup before the t1/t2/t3/t4 assignments
OLD_SETUP = """    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W, H = 900, 580
    TITLE_H = 74
    PANEL_PAD = 16
    PANEL_W = (W - PANEL_PAD * 3) // 2  # two panels side by side
    PANEL_H = H - TITLE_H - PANEL_PAD - 30"""

NEW_SETUP = """    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    # Look up per-node content overrides by title substring match
    override = None
    for key, config in CLADO_OVERRIDES.items():
        if key.lower() in node['title'].lower():
            override = config
            break

    W, H = 900, 580
    TITLE_H = 74
    PANEL_PAD = 16
    PANEL_W = (W - PANEL_PAD * 3) // 2  # two panels side by side
    PANEL_H = H - TITLE_H - PANEL_PAD - 30"""

if OLD_SETUP not in src:
    print('WARNING: cladogram setup pattern not found; cladogram may not exist in the expected form')
else:
    src = src.replace(OLD_SETUP, NEW_SETUP)
    print('Cladogram setup patched')

# Replace the species_labels = ['A', 'B', 'C', 'D'] line so it uses override taxa
OLD_LABELS = """        # Tip labels: Species A/B/C/D
        species_labels = ['A', 'B', 'C', 'D']"""
NEW_LABELS = """        # Tip labels: use override taxa if provided, else generic Species A-D
        species_labels = ['A', 'B', 'C', 'D']
        tip_taxa = (override['taxa'] if override and 'taxa' in override
                    else ['Species A', 'Species B', 'Species C', 'Species D'])"""

if OLD_LABELS not in src:
    print('WARNING: species labels pattern not found')
else:
    src = src.replace(OLD_LABELS, NEW_LABELS)
    print('Species labels patched')

# Replace the tip label rendering to use tip_taxa
OLD_TIP_TEXT = """                f'fill="{PAL["text"]}">Species {species_labels[i]}</text>'"""
NEW_TIP_TEXT = """                f'fill="{PAL["text"]}">{escape_xml(tip_taxa[i])}</text>'"""

if OLD_TIP_TEXT not in src:
    print('WARNING: tip text pattern not found')
else:
    src = src.replace(OLD_TIP_TEXT, NEW_TIP_TEXT)
    print('Tip text patched')

# Replace the subtitle with override subtitle if available
OLD_SUBTITLE = """    subtitle_lines = wrap_text(v2['definition'], max_chars=90)[:1]
    if subtitle_lines:
        parts.append(
            f'<text x="{W//2}" y="62" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="14" font-style="italic" '
            f'fill="{PAL["gold"]}" opacity="0.85">'
            f'{escape_xml(subtitle_lines[0])}</text>'
        )"""

NEW_SUBTITLE = """    subtitle_text = (override['subtitle'] if override and 'subtitle' in override
                     else v2['definition'])
    subtitle_lines = wrap_text(subtitle_text, max_chars=90)[:1]
    if subtitle_lines:
        parts.append(
            f'<text x="{W//2}" y="62" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="14" font-style="italic" '
            f'fill="{PAL["gold"]}" opacity="0.85">'
            f'{escape_xml(subtitle_lines[0])}</text>'
        )"""

# The cladogram might have this pattern only once — use find
if OLD_SUBTITLE in src:
    src = src.replace(OLD_SUBTITLE, NEW_SUBTITLE, 1)
    print('Cladogram subtitle patched')
else:
    print('WARNING: cladogram subtitle pattern not found')

# Update the right panel's group_members to use override
OLD_GROUP_MEMBERS = """        group_color=c3,
        group_members=['A', 'B'],
    ))"""
NEW_GROUP_MEMBERS = """        group_color=c3,
        group_members=(override['group_members'] if override and 'group_members' in override
                       else ['A', 'B']),
    ))"""
if OLD_GROUP_MEMBERS in src:
    src = src.replace(OLD_GROUP_MEMBERS, NEW_GROUP_MEMBERS)
    print('Cladogram group_members patched')

# ============================================================================
# Modify svg_timeline to use TIMELINE_OVERRIDES
# ============================================================================

OLD_TL_LABELS = """    event_xs = [110, 280, 500, 740]
    era_colors = ['#1a0d0d', '#0d1a0d', '#1a160d', '#0d0d1a']
    era_labels = ['PRECAMBRIAN', 'PALEOZOIC', 'MESOZOIC', 'CENOZOIC']
    era_dates  = ['4600-541 Mya', '541-252 Mya', '252-66 Mya', '66-0 Mya']
    era_bounds = [60, 220, 430, 660, 880]"""

NEW_TL_LABELS = """    event_xs = [110, 280, 500, 740]
    era_colors = ['#1a0d0d', '#0d1a0d', '#1a160d', '#0d0d1a']
    era_bounds = [60, 220, 430, 660, 880]

    # Look up per-node timeline config
    tl_override = None
    for key, config in TIMELINE_OVERRIDES.items():
        if key.lower() in node['title'].lower():
            tl_override = config
            break
    if tl_override:
        era_labels = [s.upper() for s in tl_override['era_labels']]
        era_dates  = tl_override['era_dates']
        axis_past  = tl_override['axis_past']
        axis_now   = tl_override['axis_now']
    else:
        era_labels = ['PRECAMBRIAN', 'PALEOZOIC', 'MESOZOIC', 'CENOZOIC']
        era_dates  = ['4600-541 Mya', '541-252 Mya', '252-66 Mya', '66-0 Mya']
        axis_past  = 'PAST'
        axis_now   = 'NOW'"""

if OLD_TL_LABELS not in src:
    print('WARNING: timeline labels pattern not found')
else:
    src = src.replace(OLD_TL_LABELS, NEW_TL_LABELS)
    print('Timeline labels patched')

# Replace PAST/NOW with per-node axis labels
OLD_TL_AXIS = """        f'<text x="50" y="{axis_y + 5}" text-anchor="end" '
        f'font-family="Georgia,serif" font-size="10" letter-spacing="1" '
        f'fill="{PAL["muted"]}">PAST</text>'
        f'<text x="886" y="{axis_y + 5}" '
        f'font-family="Georgia,serif" font-size="10" letter-spacing="1" '
        f'fill="{PAL["muted"]}">NOW</text>'"""

NEW_TL_AXIS = """        f'<text x="50" y="{axis_y + 5}" text-anchor="end" '
        f'font-family="Georgia,serif" font-size="10" letter-spacing="1" '
        f'fill="{PAL["muted"]}">{escape_xml(axis_past)}</text>'
        f'<text x="886" y="{axis_y + 5}" '
        f'font-family="Georgia,serif" font-size="10" letter-spacing="1" '
        f'fill="{PAL["muted"]}">{escape_xml(axis_now)}</text>'"""

if OLD_TL_AXIS in src:
    src = src.replace(OLD_TL_AXIS, NEW_TL_AXIS)
    print('Timeline axis patched')

# Update timeline subtitle too
OLD_TL_SUBTITLE = """    subtitle_lines = wrap_text(v2['definition'], max_chars=100)[:1]
    if subtitle_lines:
        parts.append(
            f'<text x="{W//2}" y="62" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="13" font-style="italic" '
            f'fill="{PAL["gold"]}" opacity="0.85">'
            f'{escape_xml(subtitle_lines[0])}</text>'
        )"""

# This pattern appears multiple times — we need to find the timeline's specific occurrence
# Just use a count
count = src.count(OLD_TL_SUBTITLE)
print(f'Subtitle pattern count: {count} (may need per-generator fix)')

# ============================================================================
# Write out + syntax check
# ============================================================================

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(src)

print(f'\nFinal size: {len(src):,} bytes')
try:
    compile(src, PATH, 'exec')
    print('Syntax: OK')
except SyntaxError as e:
    print(f'SyntaxError line {e.lineno}: {e}')
