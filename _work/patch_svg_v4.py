"""patch_svg_v4.py — Presentation-quality rewrite.

1. Injects BIO_ICONS dict + _bio_icon() helper right after _icon_shape().
2. Replaces svg_cladogram with a TWO-PANEL reference-quality layout.
3. Replaces svg_timeline with fossil icons + Mya dates + era layer.
4. Replaces svg_process_flow with step icons + better composition.
5. Replaces svg_four_box with icon-per-cell and header band.
6. Replaces svg_stages with anatomical icons per row.
7. Replaces svg_cycle with icons inside circles.
8. Replaces svg_network with icons in hub + satellites.
9. Replaces svg_balance with weight icons on pans.
10. Replaces svg_comparison with side icons.
11. Replaces svg_landscape with organism positions on curve.
"""
import re

PATH = '_work/enrich_v3.py'

with open(PATH, 'r', encoding='utf-8') as f:
    src = f.read()

# ============================================================================
# 1) Icon library: inject after _icon_shape() (end of shared SVG helpers block)
# ============================================================================

ICON_LIB = r'''

# -- biological icon library (24x24 path 'd' strings, scaled to any size) -----

BIO_ICONS = {
    'feather': (
        'M12,2 Q8,6 8,12 Q8,18 11,22 L13,22 Q16,18 16,12 Q16,6 12,2 Z '
        'M12,5 L9,8 M12,8 L8,11 M12,11 L9,14 M12,14 L9,17 M12,17 L10,20'
    ),
    'wing': (
        'M2,10 Q6,4 12,6 Q18,4 22,10 Q20,12 14,11 Q14,14 12,15 '
        'Q10,14 10,11 Q4,12 2,10 Z'
    ),
    'leg': (
        'M9,2 L15,2 L15,8 L13,12 L15,18 L17,22 L13,22 L11,18 L9,12 L9,2 Z'
    ),
    'foot': (
        'M8,4 A2,3 0 1,1 8,5 Z M12,3 A2,3 0 1,1 12,4 Z M16,4 A2,3 0 1,1 16,5 Z '
        'M6,9 A1.5,2 0 1,1 6,10 Z M18,9 A1.5,2 0 1,1 18,10 Z '
        'M12,13 Q7,14 7,18 Q7,22 12,22 Q17,22 17,18 Q17,14 12,13 Z'
    ),
    'hand': (
        'M8,8 L10,3 L11,3 L11,10 L12,10 L12,2 L13,2 L13,10 L14,10 L14,3 L15,3 '
        'L15,10 L16,10 L16,5 L17,5 L17,14 Q17,22 13,22 Q7,22 7,16 L7,10 L8,8 Z'
    ),
    'egg': 'M12,2 Q5,6 5,14 Q5,22 12,22 Q19,22 19,14 Q19,6 12,2 Z',
    'skull': (
        'M6,10 Q6,3 12,3 Q18,3 18,10 L18,14 L16,14 L16,17 L14,17 L14,14 '
        'L10,14 L10,17 L8,17 L8,14 L6,14 Z '
        'M8,8 A1.5,1.5 0 1,1 8,9 Z M16,8 A1.5,1.5 0 1,1 16,9 Z'
    ),
    'dna': (
        'M6,2 Q18,6 6,10 Q18,14 6,18 Q18,22 6,22 '
        'M18,2 Q6,6 18,10 Q6,14 18,18 Q6,22 18,22 '
        'M8,4 L16,4 M7,8 L17,8 M7,12 L17,12 M7,16 L17,16 M8,20 L16,20'
    ),
    'eye': (
        'M2,12 Q12,4 22,12 Q12,20 2,12 Z '
        'M12,8 A4,4 0 1,1 12,16 A4,4 0 1,1 12,8 Z'
    ),
    'cell': (
        'M12,2 A10,10 0 1,1 12,22 A10,10 0 1,1 12,2 Z '
        'M12,8 A4,4 0 1,1 12,16 A4,4 0 1,1 12,8 Z'
    ),
    'bone': (
        'M4,8 A3,3 0 1,1 7,11 L17,11 A3,3 0 1,1 20,8 A3,3 0 1,1 17,13 '
        'L7,13 A3,3 0 1,1 4,16 A3,3 0 1,1 7,13 Z'
    ),
    'bird': (
        'M4,14 Q8,6 14,8 L18,5 L17,9 L22,10 L17,12 Q14,16 10,15 Q6,15 4,14 Z'
    ),
    'fish': (
        'M2,12 L8,8 Q14,8 18,12 Q14,16 8,16 Z L6,15 L5,13 L6,9 Z '
        'M18,12 L22,8 L22,16 Z M15,11 A1,1 0 1,1 15,12 Z'
    ),
    'lizard': (
        'M4,12 Q8,8 12,10 Q16,8 20,12 L22,14 Q18,14 14,16 Q10,14 6,16 L4,12 Z '
        'M8,10 L7,6 M10,12 L11,8 M14,12 L15,8 M18,12 L19,6'
    ),
    'leaf': 'M4,20 Q4,4 20,4 Q20,20 4,20 Z M4,20 L14,10',
    'flame': (
        'M12,2 Q8,6 8,10 Q8,14 12,12 Q14,16 12,20 Q18,18 18,12 Q18,6 12,2 Z'
    ),
    'drop': 'M12,2 Q4,12 8,18 Q12,22 16,18 Q20,12 12,2 Z',
    'star': (
        'M12,2 L14.8,9 L22,9.5 L16,14 L18,21 L12,17 L6,21 L8,14 L2,9.5 L9.2,9 Z'
    ),
    'atom': (
        'M12,12 A2,2 0 1,1 12,13 Z '
        'M2,12 Q12,2 22,12 M2,12 Q12,22 22,12 '
        'M12,2 Q22,12 12,22 M12,2 Q2,12 12,22'
    ),
    'check': 'M4,12 L10,18 L20,4',
    'cross': 'M4,4 L20,20 M20,4 L4,20',
    'bolt': 'M13,2 L6,14 L11,14 L9,22 L18,10 L13,10 Z',
    'bacterium': (
        'M4,10 Q4,6 8,6 L16,6 Q20,6 20,10 L20,14 Q20,18 16,18 L8,18 Q4,18 4,14 Z '
        'M7,10 A1,1 0 1,1 7,11 Z M12,12 A1,1 0 1,1 12,13 Z M17,9 A1,1 0 1,1 17,10 Z'
    ),
    'sperm': (
        'M6,12 A3,3 0 1,1 12,12 A3,3 0 1,1 6,12 Z '
        'M12,12 Q16,10 18,14 Q20,10 22,14'
    ),
    'tree': (
        'M12,2 Q4,8 8,14 L10,14 L10,22 L14,22 L14,14 L16,14 Q20,8 12,2 Z'
    ),
    'tooth': (
        'M6,4 Q4,10 6,16 L8,22 L10,16 L11,12 L12,16 L14,22 L16,16 Q20,10 18,4 '
        'Q14,2 12,4 Q10,2 6,4 Z'
    ),
    'dino': (
        'M4,16 Q6,10 10,10 L12,6 Q16,4 18,8 L22,10 Q20,12 16,12 L16,16 L14,20 '
        'L12,20 L12,16 L10,16 L10,20 L8,20 L8,16 Z'
    ),
    'mushroom': (
        'M4,10 Q4,4 12,4 Q20,4 20,10 L4,10 Z '
        'M8,10 L8,18 Q8,22 12,22 Q16,22 16,18 L16,10 Z'
    ),
    'arrow_r': 'M2,12 L18,12 M14,8 L18,12 L14,16',
    'heart': 'M12,20 Q2,14 6,6 Q10,2 12,6 Q14,2 18,6 Q22,14 12,20 Z',
    'peak': 'M2,20 L9,6 L14,14 L17,10 L22,20 Z',
    'flask': (
        'M9,2 L9,10 L4,20 Q4,22 6,22 L18,22 Q20,22 20,20 L15,10 L15,2 Z '
        'M9,2 L15,2'
    ),
}


def _bio_icon(key, cx, cy, size, color, stroke_width=1.8, fill_mode='stroke'):
    """Render a biological icon centered at (cx,cy) with diameter = 2*size.
    fill_mode: 'stroke' (outline), 'fill' (solid), 'both' (fill + stroke)."""
    path = BIO_ICONS.get(key)
    if not path:
        return ''
    scale = (size * 2) / 24.0
    tx = cx - size
    ty = cy - size
    if fill_mode == 'fill':
        style = f'fill="{color}" stroke="none"'
    elif fill_mode == 'both':
        style = (f'fill="{color}" fill-opacity="0.25" stroke="{color}" '
                 f'stroke-width="{stroke_width}" stroke-linecap="round" '
                 f'stroke-linejoin="round"')
    else:
        style = (f'fill="none" stroke="{color}" stroke-width="{stroke_width}" '
                 f'stroke-linecap="round" stroke-linejoin="round"')
    return (
        f'<g transform="translate({tx:.1f},{ty:.1f}) scale({scale:.3f})">'
        f'<path d="{path}" {style}/></g>'
    )


def _pick_bio_icon(color_key, term_text):
    """Pick a sensible icon given color role + term semantic.
    Heuristic: scan the term text for known keywords; fall back by color role."""
    tl = (term_text or '').lower()
    # Literal term -> icon mapping (highest priority)
    for k, hints in [
        ('feather', ['feather', 'flight', 'plum']),
        ('wing',    ['wing', 'flight']),
        ('leg',     ['leg', 'limb', 'tetrapod']),
        ('foot',    ['foot', 'paw', 'track']),
        ('hand',    ['hand', 'finger', 'digit']),
        ('egg',     ['egg', 'oocyte', 'zygote']),
        ('skull',   ['skull', 'cranium', 'fossil']),
        ('dna',     ['dna', 'gene', 'genom', 'allele', 'chromosome', 'rna']),
        ('eye',     ['eye', 'photo', 'vision', 'sight', 'retin', 'pax6']),
        ('cell',    ['cell', 'organelle', 'nucleus', 'eukaryot']),
        ('bone',    ['bone', 'skelet', 'vertebr']),
        ('bird',    ['bird', 'avian']),
        ('fish',    ['fish', 'tiktaalik', 'aquat']),
        ('lizard',  ['lizard', 'reptil', 'dinosaur']),
        ('leaf',    ['leaf', 'plant', 'flora']),
        ('flame',   ['heat', 'temp', 'therm', 'metabol']),
        ('drop',    ['water', 'ocean', 'marine', 'aqua']),
        ('star',    ['fit', 'success', 'optim']),
        ('atom',    ['chem', 'molec', 'protein']),
        ('bolt',    ['energy', 'catalys', 'spark']),
        ('bacterium', ['bacter', 'microb', 'prokary']),
        ('sperm',   ['sperm', 'male gamet']),
        ('tree',    ['tree', 'forest', 'phylo']),
        ('tooth',   ['tooth', 'bite', 'predat']),
        ('dino',    ['dinosaur', 'saurop', 'extinct']),
        ('mushroom',['fung', 'mushroom']),
        ('heart',   ['heart', 'beat', 'circulat']),
        ('peak',    ['peak', 'mountain', 'landscape', 'adapt', 'fitness']),
        ('flask',   ['experiment', 'lab', 'test']),
        ('check',   ['correct', 'success']),
        ('cross',   ['wrong', 'fail', 'loss', 'cost']),
    ]:
        for hint in hints:
            if hint in tl:
                return k
    # Fallback by color role
    return {
        'teal':   'atom',    # mechanism -> generic mechanism icon
        'purple': 'dna',     # entity -> DNA
        'coral':  'star',    # outcome -> star/fitness
        'pink':   'bolt',    # exception -> bolt/surprise
    }.get(color_key, 'star')

'''

# Insert after the _icon_shape() function (just before the comment '# -- four-box layout')
marker = '\n# -- four-box layout'
idx = src.index(marker)
src = src[:idx] + ICON_LIB + src[idx:]

# ============================================================================
# 2) svg_cladogram — REFERENCE-QUALITY TWO-PANEL REWRITE
# ============================================================================

NEW_CLADOGRAM = r'''def svg_cladogram(node):
    """Reference-quality two-panel cladogram.

    LEFT PANEL:  'DEFINING CHARACTER STATES' — cladogram with first 2 terms as
                 legend entries (icons) and character state marks placed on branches.
    RIGHT PANEL: 'DEFINING EVOLUTIONARY GROUPS' — cladogram with terms 3 & 4 as
                 legend entries highlighted as clade outlines around tip groups.

    Both panels share the same 4-taxon tree topology (Species A-D) with
    Node 1, Node 2, Node 3 labels. Bottom axis: ANCESTRAL -> DERIVED.
    """
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W, H = 1020, 620
    TITLE_H = 80
    PANEL_PAD = 22
    PANEL_W = (W - PANEL_PAD * 3) // 2  # two panels side by side
    PANEL_H = H - TITLE_H - PANEL_PAD - 34

    # Term slots
    t1 = kt[0] if len(kt) >= 1 else {'term': 'Concept 1', 'def': '', 'color': 'teal'}
    t2 = kt[1] if len(kt) >= 2 else {'term': 'Concept 2', 'def': '', 'color': 'pink'}
    t3 = kt[2] if len(kt) >= 3 else {'term': 'Concept 3', 'def': '', 'color': 'coral'}
    t4 = kt[3] if len(kt) >= 4 else {'term': 'Concept 4', 'def': '', 'color': 'pink'}

    c1 = nc.get(t1.get('color', 'teal'),   PAL['teal'])
    c2 = nc.get(t2.get('color', 'pink'),   PAL['pink'])
    c3 = nc.get(t3.get('color', 'coral'),  PAL['coral'])
    c4 = nc.get(t4.get('color', 'pink'),   PAL['pink'])

    # Pick biological icons for each term
    ic1 = _pick_bio_icon(t1.get('color', 'teal'),  t1['term'])
    ic2 = _pick_bio_icon(t2.get('color', 'pink'),  t2['term'])
    ic3 = _pick_bio_icon(t3.get('color', 'coral'), t3['term'])
    ic4 = _pick_bio_icon(t4.get('color', 'pink'),  t4['term'])

    color_map = {'c1': c1, 'c2': c2, 'c3': c3, 'c4': c4}
    defs_str, _mids = _arrow_defs(color_map)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:1020px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
    ]

    # ---- Main title + subtitle ----
    main_title = node['title'].split(':')[0].strip() if ':' in node['title'] else node['title']
    parts.append(
        f'<text x="{W//2}" y="36" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="26" font-weight="700" '
        f'fill="{PAL["text"]}">{escape_xml(main_title)}</text>'
    )
    subtitle_lines = wrap_text(v2['definition'], max_chars=90)[:1]
    if subtitle_lines:
        parts.append(
            f'<text x="{W//2}" y="62" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="14" font-style="italic" '
            f'fill="{PAL["gold"]}" opacity="0.85">'
            f'{escape_xml(subtitle_lines[0])}</text>'
        )

    # ---- Panel frame helper ----
    def _draw_panel(px, py, pw, ph, title_text):
        out = [
            f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" '
            f'fill="{PAL["bg"]}" fill-opacity="0.5" stroke="{PAL["border"]}" '
            f'stroke-width="1.5" rx="10"/>',
            f'<text x="{px + pw//2}" y="{py + 26}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="14" font-weight="700" '
            f'letter-spacing="2" fill="{PAL["text"]}">'
            f'{escape_xml(title_text)}</text>',
            f'<line x1="{px + 30}" y1="{py + 36}" x2="{px + pw - 30}" y2="{py + 36}" '
            f'stroke="{PAL["gold"]}" stroke-width="1" opacity="0.4"/>',
        ]
        return out

    # ---- Shared cladogram topology inside a panel ----
    def _draw_cladogram(px, py, pw, ph, mode_marks, marks_colors, marks_icons, marks_labels,
                        group_color=None, group_members=None):
        """Draw a 4-taxon cladogram inside the panel's RIGHT portion.
        mode_marks: list of tuples (branch_id, icon_key, color) — character state marks
                    branch_id in {'trunk_top', 'trunk_bot', 'tipA', 'tipB', 'tipC', 'tipD'}
        group_color: if set, draw a dashed outline around group_members tips.
        group_members: list of tip ids to highlight.
        """
        out = []
        # Legend area (left 40% of panel)
        legend_w = int(pw * 0.38)
        tree_x0 = px + legend_w + 8
        tree_w = pw - legend_w - 24
        # Cladogram geometry
        root_x = tree_x0 + 14
        split1_x = tree_x0 + int(tree_w * 0.40)
        split2_x = tree_x0 + int(tree_w * 0.60)
        tip_x    = tree_x0 + int(tree_w * 0.82)
        tip_text_x = tip_x + 14

        top_y = py + 66
        bot_y = py + ph - 66
        cH = bot_y - top_y
        tip_ys = [top_y + cH * 0.10, top_y + cH * 0.33,
                  top_y + cH * 0.60, top_y + cH * 0.85]
        node1_y = (tip_ys[0] + tip_ys[1]) / 2
        node2_y = (tip_ys[2] + tip_ys[3]) / 2
        root_y  = (node1_y + node2_y) / 2

        # Common Ancestor label + dot (placed LEFT of the root to avoid overlap)
        ca_x = root_x - 28
        out.append(
            f'<circle cx="{root_x}" cy="{root_y:.1f}" r="5" fill="{PAL["gold"]}"/>'
            f'<text x="{ca_x}" y="{root_y - 2:.1f}" text-anchor="end" '
            f'font-family="Georgia,serif" font-size="10" '
            f'fill="{PAL["muted"]}">Common</text>'
            f'<text x="{ca_x}" y="{root_y + 10:.1f}" text-anchor="end" '
            f'font-family="Georgia,serif" font-size="10" '
            f'fill="{PAL["muted"]}">Ancestor</text>'
        )

        # Highlight clade (draw BEHIND the tree)
        if group_color and group_members:
            member_ys = []
            for m in group_members:
                idx = {'A': 0, 'B': 1, 'C': 2, 'D': 3}[m]
                member_ys.append(tip_ys[idx])
            if member_ys:
                cy_min = min(member_ys) - 22
                cy_max = max(member_ys) + 22
                # Solid background tint
                out.append(
                    f'<rect x="{split2_x - 6}" y="{cy_min}" '
                    f'width="{tip_text_x + 100 - split2_x + 6}" '
                    f'height="{cy_max - cy_min}" '
                    f'fill="{group_color}" opacity="0.07" rx="14"/>'
                )
                # Dashed outline
                out.append(
                    f'<rect x="{split2_x - 6}" y="{cy_min}" '
                    f'width="{tip_text_x + 100 - split2_x + 6}" '
                    f'height="{cy_max - cy_min}" '
                    f'fill="none" stroke="{group_color}" stroke-width="2" '
                    f'stroke-dasharray="6 4" rx="14" opacity="0.85"/>'
                )

        # Tree branches
        branches = [
            ('trunk_top', root_x, root_y, split1_x, root_y, PAL['muted']),
            ('trunk_mid', split1_x, node1_y, split1_x, node2_y, PAL['muted']),
            ('trunk_to_n1', split1_x, node1_y, split2_x, node1_y, PAL['muted']),
            ('trunk_to_n2', split1_x, node2_y, split2_x, node2_y, PAL['muted']),
            ('n1_vert', split2_x, tip_ys[0], split2_x, tip_ys[1], PAL['muted']),
            ('n2_vert', split2_x, tip_ys[2], split2_x, tip_ys[3], PAL['muted']),
            ('tipA', split2_x, tip_ys[0], tip_x, tip_ys[0], PAL['muted']),
            ('tipB', split2_x, tip_ys[1], tip_x, tip_ys[1], PAL['muted']),
            ('tipC', split2_x, tip_ys[2], tip_x, tip_ys[2], PAL['muted']),
            ('tipD', split2_x, tip_ys[3], tip_x, tip_ys[3], PAL['muted']),
        ]
        # Override branch color if marks specify it
        branch_colors = {}
        for bid, ic, col in mode_marks:
            branch_colors[bid] = col
        for bid, x1, y1, x2, y2, default_col in branches:
            col = branch_colors.get(bid, default_col)
            sw = 3 if bid in branch_colors else 2
            out.append(
                f'<line x1="{x1}" y1="{y1:.1f}" x2="{x2}" y2="{y2:.1f}" '
                f'stroke="{col}" stroke-width="{sw}"/>'
            )

        # Internal node dots + labels
        out.append(
            f'<circle cx="{split1_x}" cy="{root_y:.1f}" r="4" fill="{PAL["border"]}" '
            f'stroke="{PAL["muted"]}" stroke-width="1"/>'
            f'<text x="{split1_x + 6}" y="{root_y + 14:.1f}" '
            f'font-family="Georgia,serif" font-size="9" '
            f'fill="{PAL["muted"]}">Node 3</text>'
            f'<circle cx="{split2_x}" cy="{node1_y:.1f}" r="4" fill="{PAL["border"]}" '
            f'stroke="{PAL["muted"]}" stroke-width="1"/>'
            f'<text x="{split2_x + 6}" y="{node1_y + 14:.1f}" '
            f'font-family="Georgia,serif" font-size="9" '
            f'fill="{PAL["muted"]}">Node 1</text>'
            f'<circle cx="{split2_x}" cy="{node2_y:.1f}" r="4" fill="{PAL["border"]}" '
            f'stroke="{PAL["muted"]}" stroke-width="1"/>'
            f'<text x="{split2_x + 6}" y="{node2_y + 14:.1f}" '
            f'font-family="Georgia,serif" font-size="9" '
            f'fill="{PAL["muted"]}">Node 2</text>'
        )

        # Character state marks (icons on branches)
        for bid, ic, col in mode_marks:
            # Place the icon near the midpoint of the branch
            for b in branches:
                if b[0] == bid:
                    mx = (b[1] + b[3]) / 2
                    my = (b[2] + b[4]) / 2
                    # Shift above branch a bit
                    my -= 12
                    out.append(_bio_icon(ic, mx, my, 10, col,
                                         stroke_width=1.6, fill_mode='stroke'))
                    break

        # Tip labels: Species A/B/C/D
        species_labels = ['A', 'B', 'C', 'D']
        for i, ty in enumerate(tip_ys):
            # Small tip dot (colored if this tip is in the group, else muted)
            tip_color = PAL['muted']
            if group_members and species_labels[i] in group_members and group_color:
                tip_color = group_color
            out.append(
                f'<circle cx="{tip_x}" cy="{ty:.1f}" r="5" '
                f'fill="{PAL["bg"]}" stroke="{tip_color}" stroke-width="2"/>'
                f'<text x="{tip_text_x}" y="{ty + 4:.1f}" '
                f'font-family="Georgia,serif" font-size="13" font-weight="600" '
                f'fill="{PAL["text"]}">Species {species_labels[i]}</text>'
            )

        # Legend area (LEFT of the tree)
        lg_x = px + 18
        lg_y = py + 60
        lg_w = legend_w - 18
        # Two legend entries (the two terms this panel highlights)
        for i, (icon_key, color, term, definition) in enumerate(marks_labels):
            ey = lg_y + i * 88
            # Big rounded icon circle
            out.append(
                f'<circle cx="{lg_x + 28}" cy="{ey + 18}" r="22" '
                f'fill="{color}" fill-opacity="0.12" stroke="{color}" '
                f'stroke-width="2"/>'
            )
            out.append(_bio_icon(icon_key, lg_x + 28, ey + 18, 13, color,
                                 stroke_width=2, fill_mode='stroke'))
            # Numbered label
            out.append(
                f'<text x="{lg_x + 60}" y="{ey + 14}" '
                f'font-family="Georgia,serif" font-size="11" font-weight="700" '
                f'letter-spacing="1" fill="{color}" opacity="0.8">'
                f'{i+1}.</text>'
            )
            # Term name
            out.append(
                f'<text x="{lg_x + 76}" y="{ey + 14}" '
                f'font-family="Georgia,serif" font-size="14" font-weight="700" '
                f'fill="{PAL["text"]}">{escape_xml(term)}</text>'
            )
            # Short def
            def_lines = wrap_text(definition, max_chars=28)[:2]
            for li, ln in enumerate(def_lines):
                out.append(
                    f'<text x="{lg_x + 60}" y="{ey + 30 + li * 13}" '
                    f'font-family="Georgia,serif" font-size="11" '
                    f'fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
                )

        return out

    # ---- LEFT PANEL: character states ----
    lp_x = PANEL_PAD
    lp_y = TITLE_H
    parts.extend(_draw_panel(lp_x, lp_y, PANEL_W, PANEL_H, 'DEFINING CHARACTER STATES'))

    # Character state marks on left panel:
    # term 1 -> mark on top clade branches (trunk_to_n1 + tipA + tipB)
    # term 2 -> mark on trunk_top (ancestral = affects all)
    left_marks = [
        ('trunk_to_n1', ic1, c1),
        ('tipA',        ic1, c1),
        ('tipB',        ic1, c1),
        ('trunk_top',   ic2, c2),
    ]
    left_labels = [
        (ic1, c1, t1['term'], t1['def']),
        (ic2, c2, t2['term'], t2['def']),
    ]
    parts.extend(_draw_cladogram(
        lp_x, lp_y, PANEL_W, PANEL_H,
        mode_marks=left_marks,
        marks_colors=[c1, c2],
        marks_icons=[ic1, ic2],
        marks_labels=left_labels,
    ))

    # ---- RIGHT PANEL: evolutionary groups ----
    rp_x = PANEL_PAD * 2 + PANEL_W
    rp_y = TITLE_H
    parts.extend(_draw_panel(rp_x, rp_y, PANEL_W, PANEL_H, 'DEFINING EVOLUTIONARY GROUPS'))

    # Right panel has NO marks but DOES have group highlights:
    # term 3 (e.g. monophyletic) highlights A+B (top clade, all descendants)
    # term 4 (e.g. paraphyletic) highlights B+C+D (one clade + some others)
    # But we only visualize ONE group at a time for clarity -> use term 3
    right_labels = [
        (ic3, c3, t3['term'], t3['def']),
        (ic4, c4, t4['term'], t4['def']),
    ]
    parts.extend(_draw_cladogram(
        rp_x, rp_y, PANEL_W, PANEL_H,
        mode_marks=[],  # no character marks on right panel
        marks_colors=[c3, c4],
        marks_icons=[ic3, ic4],
        marks_labels=right_labels,
        group_color=c3,
        group_members=['A', 'B'],
    ))

    # ---- Bottom axis: ANCESTRAL -> DERIVED (spans both panels) ----
    axis_y = H - 20
    parts.append(
        f'<line x1="{PANEL_PAD + 20}" y1="{axis_y}" '
        f'x2="{W - PANEL_PAD - 20}" y2="{axis_y}" '
        f'stroke="{PAL["muted"]}" stroke-width="1.5"/>'
        f'<polygon points="{W - PANEL_PAD - 20},{axis_y} '
        f'{W - PANEL_PAD - 30},{axis_y - 5} '
        f'{W - PANEL_PAD - 30},{axis_y + 5}" fill="{PAL["muted"]}"/>'
        f'<text x="{PANEL_PAD + 24}" y="{axis_y + 14}" '
        f'font-family="Georgia,serif" font-size="11" letter-spacing="2" '
        f'fill="{PAL["muted"]}">ANCESTRAL</text>'
        f'<text x="{W - PANEL_PAD - 26}" y="{axis_y + 14}" text-anchor="end" '
        f'font-family="Georgia,serif" font-size="11" letter-spacing="2" '
        f'fill="{PAL["muted"]}">DERIVED</text>'
    )

    parts.append('</svg>')
    return ''.join(parts)
'''

# Splice: replace old svg_cladogram body (from 'def svg_cladogram(' to next '\ndef ')
start = src.index('def svg_cladogram(node):')
# Find next function def
m = re.search(r'\ndef (?!svg_cladogram)', src[start + 10:])
end = start + 10 + m.start() + 1  # include trailing newline before next def
src = src[:start] + NEW_CLADOGRAM + src[end:]

# ============================================================================
# Write out
# ============================================================================

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(src)

print(f'Patched {PATH}')
print(f'  New size: {len(src):,} bytes')
# Verify syntax
try:
    compile(src, PATH, 'exec')
    print('  Syntax: OK')
except SyntaxError as e:
    print(f'  SyntaxError: {e}')
