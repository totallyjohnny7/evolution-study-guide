"""patch_svg_v2.py — Add three science-illustration SVG generators +
update pick_svg() routing so 18 nodes get biology-style figures instead
of generic concept maps.

New generators:
  svg_cladogram     — Right-angle phylogenetic tree (4 taxa, 2 sister pairs)
  svg_timeline      — Geological timeline with era bands + event markers
  svg_process_flow  — Horizontal 4-step process with large flow arrows

Updated pick_svg() routes:
  CLADOGRAM  — tree, phylo, cladistic, parsimony, tiktaalik, feather, exaptation…
  TIMELINE   — deep time, age of earth, origin of life, cambrian, mesozoic…
  PROCESS    — four ingredients, mechanism, drift, bottleneck, hardy-weinberg…
  CYCLE      — (unchanged) coevolution, arms race, reproduction, game theory…
  HIERARCHY  — (unchanged) species concept, reproductive isolation…
  FOUR_BOX   — (default fallback)
"""
import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

NEW_CHUNK = r'''
# -- cladogram (right-angle phylogenetic tree) ---------------------------

def svg_cladogram(node):
    """4-taxon right-angle cladogram with 2 sister pairs, time axis,
    and colored tip circles. Labels show term name + short definition."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W, H    = 760, 440
    TITLE_H = 44
    root_x  = 65
    split1_x = 200
    split2_x = 350
    tip_x    = 475

    # 4 evenly-spaced tip Y positions within the content area
    cH = H - TITLE_H - 32
    tip_ys = [
        TITLE_H + cH * 0.12,
        TITLE_H + cH * 0.37,
        TITLE_H + cH * 0.62,
        TITLE_H + cH * 0.87,
    ]
    node1_y = (tip_ys[0] + tip_ys[1]) / 2
    node2_y = (tip_ys[2] + tip_ys[3]) / 2
    root_y  = (node1_y + node2_y) / 2

    color_map = {t.get('color','gray'): nc.get(t.get('color','gray'), PAL['muted'])
                 for t in kt[:4]}
    defs_str, _mids = _arrow_defs(color_map)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:760px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
        # Subtle background gradient bands (ancestral → derived)
        f'<defs><linearGradient id="clado-bg" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0%" stop-color="#0d1520" stop-opacity="0.7"/>'
        f'<stop offset="100%" stop-color="#0d1117" stop-opacity="0"/>'
        f'</linearGradient></defs>',
        f'<rect x="{root_x}" y="{TITLE_H}" width="{tip_x - root_x}" '
        f'height="{H - TITLE_H - 24}" fill="url(#clado-bg)" rx="4"/>',
        # Title
        f'<text x="{W//2}" y="30" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="19" font-weight="700" '
        f'fill="{PAL["gold"]}">{escape_xml(node["title"].split(":")[0].strip())}</text>',
        # Root dot + label
        f'<circle cx="{root_x}" cy="{root_y:.1f}" r="5" fill="{PAL["gold"]}"/>',
        f'<text x="{root_x - 6}" y="{root_y + 4:.1f}" text-anchor="end" '
        f'font-family="Georgia,serif" font-size="9" fill="{PAL["muted"]}">Common</text>',
        f'<text x="{root_x - 6}" y="{root_y + 14:.1f}" text-anchor="end" '
        f'font-family="Georgia,serif" font-size="9" fill="{PAL["muted"]}">Ancestor</text>',
    ]

    # === Tree branches (all right-angle L-shapes) ===
    # Trunk: root → vertical bar at split1
    parts.append(
        f'<line x1="{root_x}" y1="{root_y:.1f}" x2="{split1_x}" y2="{root_y:.1f}" '
        f'stroke="{PAL["muted"]}" stroke-width="2.5"/>'
        f'<line x1="{split1_x}" y1="{node1_y:.1f}" x2="{split1_x}" y2="{node2_y:.1f}" '
        f'stroke="{PAL["muted"]}" stroke-width="2.5"/>'
        # Top clade: split1 → node1 horizontal + split2 vertical
        f'<line x1="{split1_x}" y1="{node1_y:.1f}" x2="{split2_x}" y2="{node1_y:.1f}" '
        f'stroke="{PAL["muted"]}" stroke-width="2"/>'
        f'<line x1="{split2_x}" y1="{tip_ys[0]:.1f}" x2="{split2_x}" y2="{tip_ys[1]:.1f}" '
        f'stroke="{PAL["muted"]}" stroke-width="2"/>'
        # Bottom clade: split1 → node2 horizontal + split2 vertical
        f'<line x1="{split1_x}" y1="{node2_y:.1f}" x2="{split2_x}" y2="{node2_y:.1f}" '
        f'stroke="{PAL["muted"]}" stroke-width="2"/>'
        f'<line x1="{split2_x}" y1="{tip_ys[2]:.1f}" x2="{split2_x}" y2="{tip_ys[3]:.1f}" '
        f'stroke="{PAL["muted"]}" stroke-width="2"/>'
        # Internal node dots
        f'<circle cx="{split1_x}" cy="{node1_y:.1f}" r="4" fill="{PAL["border"]}"/>'
        f'<circle cx="{split1_x}" cy="{node2_y:.1f}" r="4" fill="{PAL["border"]}"/>'
        f'<circle cx="{split2_x}" cy="{node1_y:.1f}" r="3" fill="{PAL["border"]}"/>'
        f'<circle cx="{split2_x}" cy="{node2_y:.1f}" r="3" fill="{PAL["border"]}"/>'
    )

    # Tip branches + labels
    for i, t in enumerate(kt[:4]):
        ty    = tip_ys[i]
        color = nc.get(t.get('color','gray'), PAL['muted'])
        # Branch from split2 to tip
        parts.append(
            f'<line x1="{split2_x}" y1="{ty:.1f}" x2="{tip_x}" y2="{ty:.1f}" '
            f'stroke="{color}" stroke-width="2.5"/>'
            f'<circle cx="{tip_x}" cy="{ty:.1f}" r="7" '
            f'fill="{PAL["bg"]}" stroke="{color}" stroke-width="2.5"/>'
        )
        # Tip labels: term bold + def small, to the right
        tx = tip_x + 16
        term_lines = wrap_text(t['term'], max_chars=24)[:2]
        def_lines  = wrap_text(t['def'],  max_chars=32)[:2]
        term_base  = ty - (len(term_lines) * 14 + len(def_lines) * 12) / 2 + 12
        for li, ln in enumerate(term_lines):
            parts.append(
                f'<text x="{tx}" y="{term_base + li * 14:.1f}" '
                f'font-family="Georgia,serif" font-size="13" font-weight="700" '
                f'fill="{PAL["text"]}">{escape_xml(ln)}</text>'
            )
        def_y0 = term_base + len(term_lines) * 14
        for li, ln in enumerate(def_lines):
            parts.append(
                f'<text x="{tx}" y="{def_y0 + li * 12:.1f}" '
                f'font-family="Georgia,serif" font-size="10" '
                f'fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
            )

    # Time axis
    axis_y = H - 14
    parts.append(
        f'<line x1="{root_x}" y1="{axis_y}" x2="{tip_x + 8}" y2="{axis_y}" '
        f'stroke="{PAL["border"]}" stroke-width="1"/>'
        f'<polygon points="{tip_x+10},{axis_y} {tip_x+4},{axis_y-3} {tip_x+4},{axis_y+3}" '
        f'fill="{PAL["muted"]}"/>'
        f'<text x="{root_x}" y="{axis_y + 10}" font-family="Georgia,serif" '
        f'font-size="9" fill="{PAL["muted"]}">Ancestral</text>'
        f'<text x="{tip_x}" y="{axis_y + 10}" text-anchor="end" '
        f'font-family="Georgia,serif" font-size="9" fill="{PAL["muted"]}">Derived ▶</text>'
    )

    # Definition in top-right corner
    def_lines = wrap_text(v2['definition'], max_chars=40)[:2]
    for li, ln in enumerate(def_lines):
        parts.append(
            f'<text x="{W - 14}" y="{TITLE_H + 16 + li * 14}" text-anchor="end" '
            f'font-family="Georgia,serif" font-size="11" fill="{PAL["gold"]}" '
            f'opacity="0.6">{escape_xml(ln)}</text>'
        )

    parts.append('</svg>')
    return ''.join(parts)


# -- geological timeline --------------------------------------------------

def svg_timeline(node):
    """Horizontal timeline with 4 key events, geological era background
    bands, and alternating above/below labels."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W, H    = 760, 400
    TITLE_H = 44
    axis_y  = H // 2 + 14   # timeline axis Y

    # 4 event X positions (asymmetric — events space out like real geo time)
    event_xs = [90, 220, 380, 560]

    # Geological era bands (4 sections, left to right = ancient to recent)
    era_colors  = ['#1e0d0d', '#0d1e0d', '#1e160d', '#0d0d1e']
    era_labels  = ['Precambrian', 'Paleozoic', 'Mesozoic', 'Cenozoic']
    era_bounds  = [50, 170, 310, 470, 700]

    color_map = {t.get('color','gray'): nc.get(t.get('color','gray'), PAL['muted'])
                 for t in kt[:4]}
    defs_str, _mids = _arrow_defs(color_map)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:760px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
    ]

    # Era background bands
    for i in range(4):
        x0, x1 = era_bounds[i], era_bounds[i+1]
        parts.append(
            f'<rect x="{x0}" y="{TITLE_H}" width="{x1-x0}" height="{H-TITLE_H-16}" '
            f'fill="{era_colors[i]}" rx="4" opacity="0.8"/>'
            f'<text x="{(x0+x1)//2}" y="{TITLE_H + 14}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="9" fill="{PAL["muted"]}" '
            f'opacity="0.7" letter-spacing="1">{era_labels[i].upper()}</text>'
        )

    # Title
    parts.append(
        f'<text x="{W//2}" y="30" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="19" font-weight="700" '
        f'fill="{PAL["gold"]}">{escape_xml(node["title"].split(":")[0].strip())}</text>'
    )

    # Main timeline axis
    parts.append(
        f'<line x1="50" y1="{axis_y}" x2="710" y2="{axis_y}" '
        f'stroke="{PAL["muted"]}" stroke-width="3"/>'
        # Left arrow (past)
        f'<polygon points="50,{axis_y} 60,{axis_y-4} 60,{axis_y+4}" fill="{PAL["muted"]}"/>'
        # Right arrow (present)
        f'<polygon points="710,{axis_y} 700,{axis_y-4} 700,{axis_y+4}" fill="{PAL["muted"]}"/>'
        f'<text x="40" y="{axis_y - 8}" text-anchor="middle" font-family="Georgia,serif" '
        f'font-size="9" fill="{PAL["muted"]}">PAST</text>'
        f'<text x="720" y="{axis_y - 8}" text-anchor="middle" font-family="Georgia,serif" '
        f'font-size="9" fill="{PAL["muted"]}">NOW</text>'
    )

    # Event markers + labels (alternating above/below)
    for i, t in enumerate(kt[:4]):
        ex    = event_xs[i]
        color = nc.get(t.get('color','gray'), PAL['muted'])
        above = (i % 2 == 0)   # even = above, odd = below

        # Tick mark on axis
        parts.append(
            f'<line x1="{ex}" y1="{axis_y - 10}" x2="{ex}" y2="{axis_y + 10}" '
            f'stroke="{color}" stroke-width="2"/>'
        )

        # Event circle on axis
        parts.append(
            f'<circle cx="{ex}" cy="{axis_y}" r="8" '
            f'fill="{PAL["bg"]}" stroke="{color}" stroke-width="2.5"/>'
            f'<circle cx="{ex}" cy="{axis_y}" r="3" fill="{color}"/>'
        )

        # Vertical connector line
        connector_h = 60
        if above:
            lx1, ly1 = ex, axis_y - 10
            lx2, ly2 = ex, axis_y - connector_h
        else:
            lx1, ly1 = ex, axis_y + 10
            lx2, ly2 = ex, axis_y + connector_h

        parts.append(
            f'<line x1="{lx1}" y1="{ly1}" x2="{lx2}" y2="{ly2}" '
            f'stroke="{color}" stroke-width="1.5" stroke-dasharray="3 3" opacity="0.6"/>'
        )

        # Label box
        term_lines = wrap_text(t['term'], max_chars=18)[:2]
        def_lines  = wrap_text(t['def'],  max_chars=22)[:3]

        total_text_h = len(term_lines) * 15 + len(def_lines) * 13 + 8
        if above:
            box_y = ly2 - total_text_h - 6
        else:
            box_y = ly2 + 6

        # Subtle box background
        box_w_est = 140
        parts.append(
            f'<rect x="{ex - box_w_est//2}" y="{box_y - 4}" '
            f'width="{box_w_est}" height="{total_text_h + 8}" '
            f'fill="{PAL["bg"]}" stroke="{color}" stroke-width="1" '
            f'rx="5" opacity="0.8"/>'
        )

        # Term name
        for li, ln in enumerate(term_lines):
            parts.append(
                f'<text x="{ex}" y="{box_y + (li + 1) * 15}" '
                f'text-anchor="middle" font-family="Georgia,serif" '
                f'font-size="13" font-weight="700" '
                f'fill="{PAL["text"]}">{escape_xml(ln)}</text>'
            )

        # Def text
        def_y0 = box_y + len(term_lines) * 15 + 8
        for li, ln in enumerate(def_lines):
            parts.append(
                f'<text x="{ex}" y="{def_y0 + li * 13}" '
                f'text-anchor="middle" font-family="Georgia,serif" '
                f'font-size="10" fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
            )

    parts.append('</svg>')
    return ''.join(parts)


# -- horizontal process flow (4 steps with arrows) -----------------------

def svg_process_flow(node):
    """Horizontal 4-step process diagram: each keyTerm is one stage,
    connected by large colored arrows showing mechanistic sequence."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W       = 760
    BOX_W   = 155
    BOX_H   = 155
    ARROW_W = 22
    GAP     = 14   # gap between box and arrow
    TITLE_H = 46

    # Total width = 4 boxes + 3 arrows + gaps
    total_w = 4 * BOX_W + 3 * (ARROW_W + 2 * GAP)
    start_x = (W - total_w) // 2   # ≈ 20

    H = TITLE_H + 20 + BOX_H + 50  # title + margin + box + footer
    box_y = TITLE_H + 20

    color_map = {t.get('color','gray'): nc.get(t.get('color','gray'), PAL['muted'])
                 for t in kt[:4]}
    defs_str, _mids = _arrow_defs(color_map)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:760px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
        f'<text x="{W//2}" y="30" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="19" font-weight="700" '
        f'fill="{PAL["gold"]}">{escape_xml(node["title"].split(":")[0].strip())}</text>',
    ]

    step_stride = BOX_W + ARROW_W + 2 * GAP

    for i, t in enumerate(kt[:4]):
        bx    = start_x + i * step_stride
        color = nc.get(t.get('color','gray'), PAL['muted'])
        ckey  = t.get('color','gray')

        # Box
        parts.append(
            f'<rect x="{bx}" y="{box_y}" width="{BOX_W}" height="{BOX_H}" '
            f'fill="{PAL["bg"]}" stroke="{color}" stroke-width="2" rx="8"/>'
        )
        # Top color band
        parts.append(
            f'<rect x="{bx}" y="{box_y}" width="{BOX_W}" height="8" '
            f'fill="{color}" rx="7"/>'
            f'<rect x="{bx}" y="{box_y+4}" width="{BOX_W}" height="4" fill="{color}"/>'
        )
        # Step number badge (top-right corner)
        parts.append(
            f'<circle cx="{bx + BOX_W - 14}" cy="{box_y + 20}" r="11" '
            f'fill="{color}" opacity="0.25"/>'
            f'<text x="{bx + BOX_W - 14}" y="{box_y + 25}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="13" font-weight="700" '
            f'fill="{color}">{i+1}</text>'
        )
        # Type icon
        parts.append(_icon_shape(ckey, bx + 16, box_y + 22, 6, color))

        # Term name
        term_lines = wrap_text(t['term'], max_chars=18)[:2]
        term_cx = bx + BOX_W // 2
        for li, ln in enumerate(term_lines):
            parts.append(
                f'<text x="{term_cx}" y="{box_y + 46 + li * 16}" '
                f'text-anchor="middle" font-family="Georgia,serif" '
                f'font-size="13" font-weight="700" '
                f'fill="{PAL["text"]}">{escape_xml(ln)}</text>'
            )
        # Separator
        sep_y = box_y + 46 + len(term_lines) * 16 + 4
        parts.append(
            f'<line x1="{bx+10}" y1="{sep_y}" x2="{bx+BOX_W-10}" y2="{sep_y}" '
            f'stroke="{color}" stroke-width="0.75" opacity="0.4"/>'
        )
        # Def text
        def_y = sep_y + 12
        def_lines = wrap_text(t['def'], max_chars=20)[:4]
        for li, ln in enumerate(def_lines):
            parts.append(
                f'<text x="{term_cx}" y="{def_y + li * 13}" '
                f'text-anchor="middle" font-family="Georgia,serif" '
                f'font-size="11" fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
            )

        # Arrow to next box (not after last)
        if i < 3:
            ax = bx + BOX_W + GAP
            ay = box_y + BOX_H // 2
            next_color = nc.get(kt[i+1].get('color','gray'), PAL['muted'])
            # Large filled chevron arrow
            parts.append(
                f'<polygon points="'
                f'{ax},{ay-8} {ax+ARROW_W-8},{ay-8} {ax+ARROW_W},{ay} '
                f'{ax+ARROW_W-8},{ay+8} {ax},{ay+8}" '
                f'fill="{color}" opacity="0.55"/>'
            )

    # Bottom definition strip
    def_lines = wrap_text(v2['definition'], max_chars=88)[:2]
    footer_y = box_y + BOX_H + 18
    for li, ln in enumerate(def_lines):
        parts.append(
            f'<text x="{W//2}" y="{footer_y + li * 15}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="11" '
            f'fill="{PAL["gold"]}" opacity="0.65">{escape_xml(ln)}</text>'
        )

    parts.append('</svg>')
    return ''.join(parts)

'''

PICKER_OLD = r'''# -- layout picker (heuristic) -------------------------------------------


def pick_svg(node):
    title = node['title'].lower()
    if any(k in title for k in CYCLE_KEYWORDS):
        return svg_cycle(node)
    if any(k in title for k in HIERARCHY_KEYWORDS):
        return svg_hierarchy(node)
    return svg_four_box(node)'''

PICKER_NEW = r'''# -- layout picker (heuristic) -------------------------------------------

# Science-illustration layouts (highest priority)
CLADOGRAM_KEYWORDS = [
    'tree thinking', 'cladistic', 'synapomorph', 'monophyletic',
    'parsimony', 'homoplasy', 'convergence', 'tiktaalik',
    'fins to limb', 'feather', 'exaptation', 'transitional fossil',
    'phylo', 'clade',
]
TIMELINE_KEYWORDS = [
    'deep time', 'age of earth', 'origin of life', 'prebiotic',
    'stromatolite', 'cambrian', 'mesozoic', 'paleozoic', 'cenozoic',
    'history of life', 'mass extinction', 'k-t', 'early life',
]
PROCESS_KEYWORDS = [
    'four ingredients', 'mechanism', 'genetic drift', 'bottleneck',
    'founder', 'hardy-weinberg', 'breeders equation', 'heritability',
    'reaction norm', 'plasticity', 'genotype-phenotype', 'mutation',
    'sources of evolutionary',
]

# Generic conceptual layouts (lower priority fallbacks)
CYCLE_KEYWORDS = [
    'selection', 'cycle', 'reproduction', 'coevolution', 'life history',
    'game', 'mating', 'strategy', 'ingredients', 'arms race',
]
HIERARCHY_KEYWORDS = [
    'species concept', 'reproductive isolation', 'biogeograph',
    'speciation', 'taxonom', 'classification',
]


def pick_svg(node):
    title = node['title'].lower()
    if any(k in title for k in CLADOGRAM_KEYWORDS):
        return svg_cladogram(node)
    if any(k in title for k in TIMELINE_KEYWORDS):
        return svg_timeline(node)
    if any(k in title for k in PROCESS_KEYWORDS):
        return svg_process_flow(node)
    if any(k in title for k in CYCLE_KEYWORDS):
        return svg_cycle(node)
    if any(k in title for k in HIERARCHY_KEYWORDS):
        return svg_hierarchy(node)
    return svg_four_box(node)'''


path = r'C:\Users\johnn\Desktop\evolution-study-guide\_work\enrich_v3.py'
with open(path, 'r', encoding='utf-8') as f:
    src = f.read()

# 1. Insert the three new generators right before the layout picker
idx_picker = src.find('\n# -- layout picker')
assert idx_picker > 0, 'layout picker marker not found'
src = src[:idx_picker] + NEW_CHUNK + src[idx_picker:]

# 2. Replace the old CYCLE_KEYWORDS block + pick_svg with updated version
src = src.replace(PICKER_OLD, PICKER_NEW)

with open(path, 'w', encoding='utf-8') as f:
    f.write(src)

print(f'OK — enrich_v3.py updated ({len(src)} bytes)')
print('New generators: svg_cladogram, svg_timeline, svg_process_flow')
print('Updated pick_svg: CLADOGRAM > TIMELINE > PROCESS > CYCLE > HIERARCHY > FOUR_BOX')
