"""patch_tree_parsimony_special.py — dedicated diagrams for Tree Thinking and Parsimony.

Adds:
1. svg_tree_thinking_special — anatomical-style labeling with arrows pointing at
   each tree structure (Tip, Node, Clade, Root) with big callout labels.

2. svg_parsimony_special — shows convergence by marking the SAME trait on two
   unrelated branches (Shark + Dolphin), demonstrating homoplasy.

Routes both from pick_svg.
"""
import re

PATH = '_work/enrich_v3.py'
with open(PATH, 'r', encoding='utf-8') as f:
    src = f.read()

NEW_FUNCS = '''
def svg_tree_thinking_special(node):
    """Anatomical-style diagram: a single big cladogram with Tip / Node / Clade / Root
    explicitly labeled with callout arrows pointing at each structure."""
    v2 = node['v2']

    W, H = 960, 660
    TITLE_H = 80
    PAD = 30

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:960px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
    ]

    # Title + subtitle
    parts.append(
        f'<text x="{W//2}" y="38" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="26" font-weight="700" '
        f'fill="{PAL["text"]}">Anatomy of a Phylogenetic Tree</text>'
    )
    parts.append(
        f'<text x="{W//2}" y="62" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="13" font-style="italic" '
        f'fill="{PAL["gold"]}" opacity="0.85">'
        f'The 4 parts every cladogram has — learn to read the shape, not the labels</text>'
    )

    # Tree geometry: one big centered cladogram
    tree_left = 250
    tree_right = 680
    tree_top = TITLE_H + 50
    tree_bot = H - 80

    root_x   = tree_left + 30
    split1_x = tree_left + int((tree_right - tree_left) * 0.35)
    split2_x = tree_left + int((tree_right - tree_left) * 0.62)
    tip_x    = tree_right

    cH = tree_bot - tree_top
    tip_ys = [tree_top + cH * f for f in [0.10, 0.35, 0.62, 0.88]]
    node1_y = (tip_ys[0] + tip_ys[1]) / 2
    node2_y = (tip_ys[2] + tip_ys[3]) / 2
    root_y  = (node1_y + node2_y) / 2

    # Colors per concept (distinct so each label visually stands out)
    C_TIP   = PAL['purple']
    C_NODE  = PAL['teal']
    C_CLADE = PAL['coral']
    C_ROOT  = PAL['emerald']

    # ---- Clade highlight rectangle (BEHIND tree) around top clade ----
    clade_x0 = split2_x - 8
    clade_y0 = tip_ys[0] - 26
    clade_x1 = tip_x + 80
    clade_y1 = tip_ys[1] + 26
    parts.append(
        f'<rect x="{clade_x0}" y="{clade_y0}" width="{clade_x1 - clade_x0}" '
        f'height="{clade_y1 - clade_y0}" '
        f'fill="{C_CLADE}" opacity="0.10" rx="14"/>'
        f'<rect x="{clade_x0}" y="{clade_y0}" width="{clade_x1 - clade_x0}" '
        f'height="{clade_y1 - clade_y0}" '
        f'fill="none" stroke="{C_CLADE}" stroke-width="2.5" stroke-dasharray="6 4" rx="14"/>'
    )

    # ---- Tree branches ----
    branches = [
        (root_x, root_y, split1_x, root_y),              # trunk
        (split1_x, node1_y, split1_x, node2_y),          # main vert
        (split1_x, node1_y, split2_x, node1_y),          # up clade
        (split1_x, node2_y, split2_x, node2_y),          # down clade
        (split2_x, tip_ys[0], split2_x, tip_ys[1]),
        (split2_x, tip_ys[2], split2_x, tip_ys[3]),
        (split2_x, tip_ys[0], tip_x, tip_ys[0]),
        (split2_x, tip_ys[1], tip_x, tip_ys[1]),
        (split2_x, tip_ys[2], tip_x, tip_ys[2]),
        (split2_x, tip_ys[3], tip_x, tip_ys[3]),
    ]
    for (x1, y1, x2, y2) in branches:
        parts.append(
            f'<line x1="{x1}" y1="{y1:.1f}" x2="{x2}" y2="{y2:.1f}" '
            f'stroke="{PAL["muted"]}" stroke-width="3"/>'
        )

    # ---- Tip circles + species labels ----
    species = ['Species A', 'Species B', 'Species C', 'Species D']
    for i, ty in enumerate(tip_ys):
        parts.append(
            f'<circle cx="{tip_x}" cy="{ty:.1f}" r="7" '
            f'fill="{PAL["bg"]}" stroke="{C_TIP}" stroke-width="2.5"/>'
        )
        parts.append(
            f'<text x="{tip_x + 14}" y="{ty + 4:.1f}" '
            f'font-family="Georgia,serif" font-size="13" font-weight="600" '
            f'fill="{PAL["text"]}">{species[i]}</text>'
        )

    # ---- Internal node dots ----
    for nx, ny in [(split1_x, root_y), (split2_x, node1_y), (split2_x, node2_y)]:
        parts.append(
            f'<circle cx="{nx}" cy="{ny:.1f}" r="6" '
            f'fill="{PAL["bg"]}" stroke="{C_NODE}" stroke-width="2.5"/>'
        )

    # ---- Root dot (highlighted) ----
    parts.append(
        f'<circle cx="{root_x}" cy="{root_y:.1f}" r="9" '
        f'fill="{C_ROOT}" stroke="{PAL["bg"]}" stroke-width="2.5"/>'
    )

    # ================================================================
    # 4 BIG CALLOUT LABELS with arrows pointing at each feature
    # ================================================================

    def callout(label_x, label_y, target_x, target_y, color, number, title, definition,
                anchor='start'):
        out = []
        # Curved arrow from label to target
        mid_x = (label_x + target_x) / 2
        mid_y = (label_y + target_y) / 2
        out.append(
            f'<path d="M {label_x},{label_y} Q {mid_x},{label_y} {target_x},{target_y}" '
            f'fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" '
            f'marker-end="url(#tree-arrow-{number})" opacity="0.85"/>'
        )
        # Label badge with number + big name + def
        out.append(
            f'<circle cx="{label_x}" cy="{label_y}" r="18" '
            f'fill="{color}" fill-opacity="0.2" stroke="{color}" stroke-width="2.5"/>'
            f'<text x="{label_x}" y="{label_y + 6}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="18" font-weight="700" '
            f'fill="{color}">{number}</text>'
        )
        if anchor == 'end':
            text_x = label_x - 26
            ta = 'end'
        else:
            text_x = label_x + 26
            ta = 'start'
        out.append(
            f'<text x="{text_x}" y="{label_y - 6}" text-anchor="{ta}" '
            f'font-family="Georgia,serif" font-size="17" font-weight="700" '
            f'fill="{PAL["text"]}">{escape_xml(title)}</text>'
        )
        out.append(
            f'<text x="{text_x}" y="{label_y + 14}" text-anchor="{ta}" '
            f'font-family="Georgia,serif" font-size="12" font-style="italic" '
            f'fill="{color}" opacity="0.9">{escape_xml(definition)}</text>'
        )
        return out

    # Arrow markers for each callout color
    parts.append(
        f'<defs>'
        f'<marker id="tree-arrow-1" markerWidth="9" markerHeight="7" refX="8" refY="3.5" '
        f'orient="auto"><polygon points="0 0, 9 3.5, 0 7" fill="{C_TIP}"/></marker>'
        f'<marker id="tree-arrow-2" markerWidth="9" markerHeight="7" refX="8" refY="3.5" '
        f'orient="auto"><polygon points="0 0, 9 3.5, 0 7" fill="{C_NODE}"/></marker>'
        f'<marker id="tree-arrow-3" markerWidth="9" markerHeight="7" refX="8" refY="3.5" '
        f'orient="auto"><polygon points="0 0, 9 3.5, 0 7" fill="{C_CLADE}"/></marker>'
        f'<marker id="tree-arrow-4" markerWidth="9" markerHeight="7" refX="8" refY="3.5" '
        f'orient="auto"><polygon points="0 0, 9 3.5, 0 7" fill="{C_ROOT}"/></marker>'
        f'</defs>'
    )

    # 1. TIP — callout on upper left, arrow pointing at Species A circle
    parts.extend(callout(
        label_x=100, label_y=tip_ys[0] - 10,
        target_x=tip_x - 10, target_y=tip_ys[0],
        color=C_TIP, number='1',
        title='Tip',
        definition='present-day species at branch ends',
        anchor='start',
    ))

    # 2. NODE — callout on lower left, arrow to upper internal node
    parts.extend(callout(
        label_x=100, label_y=tip_ys[1] + 26,
        target_x=split2_x - 6, target_y=node1_y,
        color=C_NODE, number='2',
        title='Node',
        definition='common ancestor of descendants',
        anchor='start',
    ))

    # 3. CLADE — callout on upper right of tree, arrow to highlighted rectangle
    parts.extend(callout(
        label_x=W - 80, label_y=tree_top + 30,
        target_x=clade_x1 - 10, target_y=clade_y0 + 18,
        color=C_CLADE, number='3',
        title='Clade',
        definition='ancestor + ALL descendants',
        anchor='end',
    ))

    # 4. ROOT — callout on lower right, arrow pointing at root dot
    parts.extend(callout(
        label_x=W - 80, label_y=H - 80,
        target_x=root_x + 12, target_y=root_y,
        color=C_ROOT, number='4',
        title='Root',
        definition='deepest common ancestor',
        anchor='end',
    ))

    parts.append('</svg>')
    return ''.join(parts)


def svg_parsimony_special(node):
    """Parsimony diagram showing convergence/homoplasy: the SAME trait (streamlined body)
    appears on TWO unrelated branches (Shark + Dolphin), demonstrating that similarity
    can mislead a cladistic analysis."""
    v2 = node['v2']

    W, H = 960, 680
    TITLE_H = 80

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:960px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
    ]

    # Title + subtitle
    parts.append(
        f'<text x="{W//2}" y="38" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="26" font-weight="700" '
        f'fill="{PAL["text"]}">Parsimony &amp; Homoplasy</text>'
    )
    parts.append(
        f'<text x="{W//2}" y="62" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="13" font-style="italic" '
        f'fill="{PAL["gold"]}" opacity="0.85">'
        f'Shark &amp; dolphin look alike (streamlined body) but evolved it independently — convergence</text>'
    )

    C_CONV = PAL['amber']
    C_GOOD = PAL['emerald']

    # ---- Panel A: the WRONG tree (grouped by appearance) ----
    # Shark + Dolphin together because both streamlined, missing Tuna and Seal
    pA_x = 30
    pA_y = TITLE_H + 20
    pA_w = (W - 90) // 2
    pA_h = H - TITLE_H - 120

    def panel_header(px, py, pw, title, color, verdict, verdict_color):
        out = [
            f'<rect x="{px}" y="{py}" width="{pw}" height="{pA_h}" '
            f'fill="{PAL["bg"]}" fill-opacity="0.5" stroke="{color}" '
            f'stroke-width="2" rx="12"/>',
            f'<rect x="{px}" y="{py}" width="{pw}" height="42" '
            f'fill="{color}" opacity="0.15" rx="12"/>',
            f'<rect x="{px}" y="{py + 38}" width="{pw}" height="4" fill="{color}"/>',
            f'<text x="{px + 16}" y="{py + 27}" '
            f'font-family="Georgia,serif" font-size="15" font-weight="700" '
            f'fill="{PAL["text"]}">{escape_xml(title)}</text>',
        ]
        # Verdict pill
        vw = 110
        vx = px + pw - vw - 12
        out.append(
            f'<rect x="{vx}" y="{py + 10}" width="{vw}" height="22" rx="11" '
            f'fill="{verdict_color}" fill-opacity="0.25" stroke="{verdict_color}" '
            f'stroke-width="1.5"/>'
            f'<text x="{vx + vw/2}" y="{py + 25}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="11" font-weight="700" '
            f'letter-spacing="1" fill="{verdict_color}">{escape_xml(verdict)}</text>'
        )
        return out

    # Helper: draw a 4-tip tree inside a panel
    def draw_tree(px, py, pw, ph, ordering, marked_tips, mark_color, explanation):
        """ordering: list of 4 taxa names in top-to-bottom order.
           marked_tips: list of indices (0-3) that get the homoplasy star mark."""
        out = []
        tree_x0 = px + 20
        tree_y0 = py + 64
        tree_w  = pw - 40
        tree_h  = ph - 64 - 60
        root_x   = tree_x0 + 18
        split1_x = tree_x0 + int(tree_w * 0.32)
        split2_x = tree_x0 + int(tree_w * 0.55)
        tip_x    = tree_x0 + int(tree_w * 0.72)
        tip_text_x = tip_x + 12

        top_y = tree_y0 + 20
        bot_y = tree_y0 + tree_h - 10
        tip_ys = [top_y + (bot_y - top_y) * f for f in [0.10, 0.37, 0.63, 0.90]]
        node1_y = (tip_ys[0] + tip_ys[1]) / 2
        node2_y = (tip_ys[2] + tip_ys[3]) / 2
        root_y  = (node1_y + node2_y) / 2

        out.append(
            f'<circle cx="{root_x}" cy="{root_y:.1f}" r="4" fill="{PAL["gold"]}"/>'
            f'<text x="{root_x - 6}" y="{root_y + 14}" text-anchor="end" '
            f'font-family="Georgia,serif" font-size="9" fill="{PAL["muted"]}">Common</text>'
            f'<text x="{root_x - 6}" y="{root_y + 24}" text-anchor="end" '
            f'font-family="Georgia,serif" font-size="9" fill="{PAL["muted"]}">Ancestor</text>'
        )

        branches = [
            ('trunk', root_x, root_y, split1_x, root_y),
            ('trunk_mid', split1_x, node1_y, split1_x, node2_y),
            ('to_n1', split1_x, node1_y, split2_x, node1_y),
            ('to_n2', split1_x, node2_y, split2_x, node2_y),
            ('n1_vert', split2_x, tip_ys[0], split2_x, tip_ys[1]),
            ('n2_vert', split2_x, tip_ys[2], split2_x, tip_ys[3]),
            ('tipA', split2_x, tip_ys[0], tip_x, tip_ys[0]),
            ('tipB', split2_x, tip_ys[1], tip_x, tip_ys[1]),
            ('tipC', split2_x, tip_ys[2], tip_x, tip_ys[2]),
            ('tipD', split2_x, tip_ys[3], tip_x, tip_ys[3]),
        ]
        for bid, x1, y1, x2, y2 in branches:
            out.append(
                f'<line x1="{x1}" y1="{y1:.1f}" x2="{x2}" y2="{y2:.1f}" '
                f'stroke="{PAL["muted"]}" stroke-width="2"/>'
            )

        # Internal node dots
        for nx, ny in [(split1_x, root_y), (split2_x, node1_y), (split2_x, node2_y)]:
            out.append(
                f'<circle cx="{nx}" cy="{ny:.1f}" r="3" fill="{PAL["border"]}"/>'
            )

        # Tip circles + labels
        for i, (ty, name) in enumerate(zip(tip_ys, ordering)):
            is_marked = i in marked_tips
            tcolor = mark_color if is_marked else PAL['muted']
            out.append(
                f'<circle cx="{tip_x}" cy="{ty:.1f}" r="5" '
                f'fill="{PAL["bg"]}" stroke="{tcolor}" stroke-width="2"/>'
                f'<text x="{tip_text_x}" y="{ty + 4:.1f}" '
                f'font-family="Georgia,serif" font-size="12" font-weight="600" '
                f'fill="{PAL["text"]}">{escape_xml(name)}</text>'
            )
            # Star mark on marked tips (independent trait evolution)
            if is_marked:
                mx = (split2_x + tip_x) / 2
                my = ty - 10
                out.append(
                    f'<circle cx="{mx:.0f}" cy="{my:.0f}" r="8" '
                    f'fill="{mark_color}" stroke="{PAL["bg"]}" stroke-width="2"/>'
                    f'<text x="{mx:.0f}" y="{my + 4:.0f}" text-anchor="middle" '
                    f'font-family="Georgia,serif" font-size="11" font-weight="700" '
                    f'fill="{PAL["bg"]}">★</text>'
                )

        # Explanation
        exp_lines = wrap_text(explanation, max_chars=48)[:3]
        ey = py + ph - 46
        for li, ln in enumerate(exp_lines):
            out.append(
                f'<text x="{px + 16}" y="{ey + li * 14}" '
                f'font-family="Georgia,serif" font-size="11" '
                f'fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
            )
        return out

    # ---- PANEL A: Wrong conclusion — grouping by appearance ----
    parts.extend(panel_header(pA_x, pA_y, pA_w,
        'Naïve: group by appearance', C_CONV, '✗ MISLEADING', PAL['crimson']))
    # In this tree, Shark (0) and Dolphin (1) are grouped together — but with TWO ★ marks
    # showing the trait appears TWICE (once on each lineage)
    parts.extend(draw_tree(
        pA_x, pA_y, pA_w, pA_h,
        ordering=['Shark', 'Dolphin', 'Tuna', 'Seal'],
        marked_tips=[0, 1],
        mark_color=C_CONV,
        explanation='Shark + Dolphin LOOK alike (★ streamlined body). If we group by looks we get the wrong tree!',
    ))

    # ---- PANEL B: Correct tree — grouped by shared ancestry ----
    pB_x = pA_x + pA_w + 30
    parts.extend(panel_header(pB_x, pA_y, pA_w,
        'Parsimony: true relationships', C_GOOD, '✓ CORRECT', C_GOOD))
    # Shark/Tuna are fish (top), Dolphin/Seal are mammals (bottom). Marks on 0 and 2 (non-adjacent)
    parts.extend(draw_tree(
        pB_x, pA_y, pA_w, pA_h,
        ordering=['Shark', 'Tuna', 'Dolphin', 'Seal'],
        marked_tips=[0, 2],
        mark_color=C_GOOD,
        explanation='True tree: sharks are fish, dolphins are mammals. Streamlined body (★) evolved TWICE = homoplasy.',
    ))

    # ---- Bottom legend strip ----
    legend_y = H - 56
    parts.append(
        f'<rect x="30" y="{legend_y}" width="{W - 60}" height="40" '
        f'fill="{PAL["gold"]}" fill-opacity="0.08" stroke="{PAL["gold"]}" '
        f'stroke-width="1" stroke-opacity="0.4" rx="8"/>'
    )
    parts.append(
        f'<text x="{W//2}" y="{legend_y + 24}" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="13" font-style="italic" '
        f'fill="{PAL["gold"]}" opacity="0.9">'
        f'★ = streamlined body trait. Parsimony picks the tree with fewest changes — but two independent evolutions of the same trait (homoplasy) can fool it.</text>'
    )

    parts.append('</svg>')
    return ''.join(parts)


'''

# Insert these new functions right after svg_cladistics_special
insert_anchor = '\ndef svg_timeline(node):'
idx = src.index(insert_anchor)
src = src[:idx] + NEW_FUNCS + src[idx:]

# Update pick_svg to route these
old_picker = '''def pick_svg(node):
    title = node['title'].lower()
    # Special dedicated generators (must run before generic cladogram routing)
    if 'cladistics' in title:
        return svg_cladistics_special(node)
    # Highest-priority specific biology illustrations
    if any(k in title for k in CLADOGRAM_KEYWORDS):
        return svg_cladogram(node)'''

new_picker = '''def pick_svg(node):
    title = node['title'].lower()
    # Special dedicated generators (must run before generic cladogram routing)
    if 'cladistics' in title:
        return svg_cladistics_special(node)
    if 'tree thinking' in title:
        return svg_tree_thinking_special(node)
    if 'parsimony' in title:
        return svg_parsimony_special(node)
    # Highest-priority specific biology illustrations
    if any(k in title for k in CLADOGRAM_KEYWORDS):
        return svg_cladogram(node)'''

if old_picker in src:
    src = src.replace(old_picker, new_picker)
    print('pick_svg updated with Tree Thinking + Parsimony special routes')
else:
    print('WARNING: pick_svg pattern not found')

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(src)

print(f'Size: {len(src):,}')
try:
    compile(src, PATH, 'exec')
    print('Syntax: OK')
except SyntaxError as e:
    print(f'SyntaxError line {e.lineno}: {e}')
