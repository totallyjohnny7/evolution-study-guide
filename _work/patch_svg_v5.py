"""patch_svg_v5.py — Replace BIO_ICONS with Lucide + rewrite all generators
to presentation quality with icons, legends, subtitles, and annotations.

This is a MAJOR rewrite. It:
1) Imports LUCIDE_ICONS from _work/lucide_icons_extracted.py
2) Replaces the hand-rolled BIO_ICONS dict inside enrich_v3.py with the
   Lucide data.
3) Replaces _bio_icon() with a version that emits a <g> wrapper setting
   stroke color + width, and inlines the Lucide paths inside.
4) Replaces svg_timeline with a geological scale + fossil icons design.
5) Replaces svg_process_flow with large icon tiles + connector arrows.
6) Replaces svg_four_box with a header+icon+definition card design.
7) Replaces svg_stages with anatomical icons + progression arrows.
8) Replaces svg_cycle with icons inside circles + curved arrows.
9) Replaces svg_network with hub+satellites with icons.
10) Replaces svg_balance with weight tiles on pans + icons.
11) Replaces svg_comparison with icon-topped comparison panels.
12) Replaces svg_landscape with organism positions on curve.
"""
import re
import os

PATH = '_work/enrich_v3.py'
ICONS_PATH = '_work/lucide_icons_extracted.py'

# Load Lucide icons
with open(ICONS_PATH, 'r', encoding='utf-8') as f:
    icons_module_src = f.read()
namespace = {}
exec(icons_module_src, namespace)
LUCIDE_ICONS = namespace['LUCIDE_ICONS']
print(f'Loaded {len(LUCIDE_ICONS)} Lucide icons')

# Load current enrich_v3.py
with open(PATH, 'r', encoding='utf-8') as f:
    src = f.read()

# ============================================================================
# 1) REPLACE BIO_ICONS dict with a short reference to LUCIDE_ICONS
#    + replace _bio_icon() with the new <g> wrapper version
# ============================================================================

# Build the literal Python dict text for embedding
icons_dict_text = 'BIO_ICONS = {\n'
for key in sorted(LUCIDE_ICONS.keys()):
    val = LUCIDE_ICONS[key].replace('\\', '\\\\').replace('"', '\\"')
    icons_dict_text += f'    {key!r}: "{val}",\n'
icons_dict_text += '}\n'

NEW_ICON_BLOCK = '''

# -- biological icon library (Lucide icons, ISC license) ---------------------
# https://github.com/lucide-icons/lucide
# Each value is the inner SVG content (paths, circles) for a 24x24 viewBox.
# Rendered by _bio_icon() inside a <g> wrapper that sets stroke color.

''' + icons_dict_text + '''

def _bio_icon(key, cx, cy, size, color, stroke_width=2.0, fill_mode='stroke'):
    """Render a Lucide-style biological icon centered at (cx,cy) with
    diameter = 2*size. All icons use a 24x24 viewBox."""
    inner = BIO_ICONS.get(key)
    if not inner:
        return ''
    scale = (size * 2) / 24.0
    tx = cx - size
    ty = cy - size
    if fill_mode == 'fill':
        fill_attr = f'fill="{color}"'
    else:
        fill_attr = 'fill="none"'
    return (
        f'<g transform="translate({tx:.1f},{ty:.1f}) scale({scale:.3f})" '
        f'stroke="{color}" stroke-width="{stroke_width}" '
        f'stroke-linecap="round" stroke-linejoin="round" {fill_attr}>'
        f'{inner}</g>'
    )


def _pick_bio_icon(color_key, term_text):
    """Pick a sensible Lucide icon given color role + term semantic."""
    tl = (term_text or '').lower()
    for k, hints in [
        ('feather',    ['feather', 'flight', 'plum']),
        ('wing',       ['wing']),
        ('foot',       ['foot', 'paw', 'track', 'footprint']),
        ('hand',       ['hand', 'finger', 'digit']),
        ('eye',        ['eye', 'photo', 'vision', 'sight', 'retin', 'pax6']),
        ('bone',       ['bone', 'skelet', 'vertebr', 'tetrapod', 'limb']),
        ('skull',      ['skull', 'cranium']),
        ('brain',      ['brain', 'neural', 'nervous', 'cogniti']),
        ('bird',       ['bird', 'avian']),
        ('fish',       ['fish', 'tiktaalik', 'aquat', 'marine', 'sperm', 'male gamet']),
        ('rabbit',     ['rabbit', 'mammal']),
        ('turtle',     ['turtle', 'reptil']),
        ('worm',       ['worm', 'helminth']),
        ('bug',        ['insect', 'bug', 'arthropod']),
        ('snail',      ['snail', 'mollusc']),
        ('egg',        ['egg', 'zygote', 'oocyte', 'female gamet']),
        ('baby',       ['offspring', 'juvenile', 'baby', 'embryo']),
        ('heart',      ['heart', 'love', 'mate', 'circulat']),
        ('dna',        ['dna', 'gene', 'genom', 'allele', 'chromosome', 'rna', 'sequence']),
        ('microscope', ['microscope', 'microscopy', 'observ']),
        ('leaf',       ['leaf', 'plant', 'flora']),
        ('trees',      ['tree', 'forest']),
        ('sprout',     ['sprout', 'seedling', 'germinat']),
        ('flower',     ['flower', 'blossom', 'petal']),
        ('flame',      ['heat', 'temp', 'therm', 'metabol', 'fire']),
        ('drop',       ['water', 'ocean', 'marine', 'aqua', 'droplet']),
        ('sun',        ['sun', 'solar', 'day']),
        ('moon',       ['moon', 'night', 'nocturn']),
        ('wind',       ['wind', 'air', 'breath']),
        ('snowflake',  ['cold', 'ice', 'snow', 'freeze']),
        ('mountain',   ['mountain', 'peak', 'landscape', 'fitness', 'adapt']),
        ('waves',      ['waves', 'ocean', 'current', 'tide']),
        ('atom',       ['chem', 'molec', 'protein', 'atom']),
        ('star',       ['fit', 'success', 'optim', 'star']),
        ('bolt',       ['energy', 'spark', 'lightning', 'zap', 'mutation']),
        ('check',      ['correct', 'success', 'true']),
        ('cross',      ['wrong', 'fail', 'loss', 'cost', 'false']),
        ('plus',       ['add', 'gain', 'benefit', 'increase']),
        ('minus',      ['loss', 'decrease', 'reduce']),
        ('equal',      ['equal', 'same', 'equiv']),
        ('percent',    ['percent', 'ratio', 'rate']),
        ('infinity',   ['infinite', 'continuous', 'forever']),
        ('repeat',     ['repeat', 'cycle', 'recurr']),
        ('refresh',    ['refresh', 'renew', 'regenerat']),
        ('target',     ['target', 'goal', 'aim']),
        ('compass',    ['direction', 'orient', 'navigate']),
        ('scale',      ['scale', 'balance', 'weigh', 'trade-off', 'tradeoff']),
        ('trophy',     ['winner', 'compet', 'prize']),
        ('crown',      ['king', 'dominant', 'alpha']),
        ('shield',     ['defense', 'protect', 'shield']),
        ('lock',       ['lock', 'fix', 'commit', 'isolat']),
        ('key',        ['key', 'critical', 'unlock']),
        ('scissors',   ['cut', 'sever', 'cleav']),
        ('flask',      ['experiment', 'lab', 'test', 'chem']),
        ('test_tube',  ['test', 'sample', 'vial']),
        ('beaker',     ['beaker', 'mix', 'solution']),
        ('pill',       ['drug', 'medic', 'antibiot']),
        ('clock',      ['time', 'clock', 'rate', 'generat']),
        ('hourglass',  ['hourglass', 'wait', 'age']),
        ('calendar',   ['schedule', 'year', 'date']),
        ('arrow_r',    ['next', 'follow']),
        ('arrow_up',   ['increase', 'rise', 'grow']),
        ('arrow_down', ['decrease', 'fall', 'drop']),
        ('link',       ['link', 'connect', 'bond']),
        ('globe',      ['globe', 'world', 'biogeograph', 'earth']),
        ('layers',     ['layer', 'strata', 'level']),
        ('network',    ['network', 'web', 'interact']),
        ('shuffle',    ['shuffle', 'mix', 'recomb']),
        ('merge',      ['merge', 'fuse', 'combine']),
        ('branch',     ['branch', 'split', 'fork', 'speciat']),
        ('fork',       ['fork', 'diverge']),
        ('shell',      ['shell', 'mollusc', 'cambrian']),
        ('gem',        ['gem', 'crystal', 'zircon', 'mineral']),
        ('thermometer',['thermometer', 'body temp']),
        ('fuel',       ['fuel', 'energy', 'atp']),
    ]:
        for hint in hints:
            if hint in tl:
                return k
    return {
        'teal':   'atom',
        'purple': 'dna',
        'coral':  'star',
        'pink':   'bolt',
    }.get(color_key, 'star')
'''

# Remove the old BIO_ICONS dict + old _bio_icon + _pick_bio_icon that patch_v4 inserted
# Splice: find the start of '\n\n# -- biological icon library (24x24'
# and remove through the end of _pick_bio_icon()
# Our marker: insertion started after _icon_shape() with the line
# '\n# -- biological icon library (24x24 path ...'
# The whole block ends right before '\n# -- four-box layout'
start_marker = '\n\n# -- biological icon library'
end_marker   = '\n\n# -- four-box layout'
s = src.index(start_marker)
e = src.index(end_marker)
src = src[:s] + NEW_ICON_BLOCK + src[e:]

print(f'Step 1: icon library replaced. New size: {len(src):,}')

# Write intermediate state
with open(PATH, 'w', encoding='utf-8') as f:
    f.write(src)

# Verify syntax
try:
    compile(src, PATH, 'exec')
    print('Step 1 syntax: OK')
except SyntaxError as e:
    print(f'Step 1 SyntaxError: {e}')
    import sys; sys.exit(1)
