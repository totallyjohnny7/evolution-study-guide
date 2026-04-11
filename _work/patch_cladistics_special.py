"""patch_cladistics_special.py — dedicated generator for the Cladistics node.

Shows ALL 4 concepts (Synapomorphy, Plesiomorphy, Monophyletic, Paraphyletic)
in a 2x2 layout with strong contrast colors:
  - Left column: character states (Synapomorphy = green, Plesiomorphy = amber)
  - Right column: groups (Monophyletic = green CORRECT, Paraphyletic = red WRONG)

Each panel has its own mini-cladogram showing the concept.
"""
import re

PATH = '_work/enrich_v3.py'
with open(PATH, 'r', encoding='utf-8') as f:
    src = f.read()

NEW_FUNC = '''
def svg_cladistics_special(node):
    """Dedicated Cladistics diagram showing ALL 4 concepts in 2x2 panels.

    Top row:    Character states — Synapomorphy (derived shared) vs Plesiomorphy (ancestral shared)
    Bottom row: Group types      — Monophyletic (valid) vs Paraphyletic (invalid)

    Each quadrant is a mini-cladogram with a distinct visual highlight.
    """
    v2 = node['v2']
    kt = v2['keyTerms']

    W, H = 960, 800
    TITLE_H = 80
    PAD = 16
    QUAD_W = (W - PAD * 3) // 2
    QUAD_H = (H - TITLE_H - PAD * 3) // 2

    # Strong contrasting colors for mono vs para
    C_SYN  = PAL['emerald']   # synapomorphy = derived, the KEY insight → green
    C_PLES = PAL['amber']     # plesiomorphy = ancestral, not useful → amber
    C_MONO = PAL['emerald']   # monophyletic = VALID group → green
    C_PARA = PAL['crimson']   # paraphyletic = INVALID group → red

    color_map = {'syn': C_SYN, 'ples': C_PLES, 'mono': C_MONO, 'para': C_PARA}
    defs_str, _mids = _arrow_defs(color_map)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:960px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
    ]

    # Title + subtitle
    parts.append(
        f'<text x="{W//2}" y="38" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="26" font-weight="700" '
        f'fill="{PAL["text"]}">Cladistics: Characters &amp; Groups</text>'
    )
    parts.append(
        f'<text x="{W//2}" y="62" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="13" font-style="italic" '
        f'fill="{PAL["gold"]}" opacity="0.85">'
        f'Only SHARED DERIVED characters (synapomorphies) define MONOPHYLETIC clades</text>'
    )

    # ---- Quadrant helper ----
    def quadrant(qx, qy, qw, qh, title, subtitle, color, verdict, verdict_color,
                 mark_branches, group_members, explanation, icon_key):
        out = []
        # Outer frame
        out.append(
            f'<rect x="{qx}" y="{qy}" width="{qw}" height="{qh}" '
            f'fill="{PAL["bg"]}" fill-opacity="0.5" stroke="{color}" '
            f'stroke-width="2" rx="12"/>'
        )
        # Header strip
        out.append(
            f'<rect x="{qx}" y="{qy}" width="{qw}" height="42" '
            f'fill="{color}" opacity="0.15" rx="12"/>'
            f'<rect x="{qx}" y="{qy + 38}" width="{qw}" height="4" fill="{color}"/>'
        )
        # Icon circle
        out.append(
            f'<circle cx="{qx + 28}" cy="{qy + 22}" r="15" '
            f'fill="{color}" fill-opacity="0.2" stroke="{color}" stroke-width="2"/>'
        )
        out.append(_bio_icon(icon_key, qx + 28, qy + 22, 10, color,
                             stroke_width=2, fill_mode='stroke'))
        # Title + verdict
        out.append(
            f'<text x="{qx + 50}" y="{qy + 27}" '
            f'font-family="Georgia,serif" font-size="15" font-weight="700" '
            f'fill="{PAL["text"]}">{escape_xml(title)}</text>'
        )
        # Verdict badge (top-right)
        vw = 70
        vx = qx + qw - vw - 10
        out.append(
            f'<rect x="{vx}" y="{qy + 10}" width="{vw}" height="22" rx="11" '
            f'fill="{verdict_color}" fill-opacity="0.25" stroke="{verdict_color}" '
            f'stroke-width="1.5"/>'
            f'<text x="{vx + vw/2}" y="{qy + 25}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="11" font-weight="700" '
            f'letter-spacing="1" fill="{verdict_color}">'
            f'{escape_xml(verdict)}</text>'
        )
        # Subtitle (below header)
        out.append(
            f'<text x="{qx + 14}" y="{qy + 58}" '
            f'font-family="Georgia,serif" font-size="12" font-style="italic" '
            f'fill="{color}" opacity="0.9">'
            f'{escape_xml(subtitle)}</text>'
        )

        # Mini-cladogram
        tree_x0 = qx + 14
        tree_y0 = qy + 78
        tree_w  = qw - 28
        tree_h  = qh - 78 - 50  # leave room for explanation at bottom
        root_x    = tree_x0 + 20
        split1_x  = tree_x0 + int(tree_w * 0.30)
        split2_x  = tree_x0 + int(tree_w * 0.55)
        tip_x     = tree_x0 + int(tree_w * 0.72)
        tip_label_x = tip_x + 10

        top_y = tree_y0 + 14
        bot_y = tree_y0 + tree_h - 10
        tip_ys = [top_y + (bot_y - top_y) * f for f in [0.10, 0.37, 0.63, 0.90]]
        node1_y = (tip_ys[0] + tip_ys[1]) / 2
        node2_y = (tip_ys[2] + tip_ys[3]) / 2
        root_y  = (node1_y + node2_y) / 2

        # Root dot
        out.append(
            f'<circle cx="{root_x}" cy="{root_y:.1f}" r="4" fill="{PAL["gold"]}"/>'
        )

        # Highlight clade rect (draw behind the branches)
        if group_members:
            member_ys = [tip_ys[{'A':0,'B':1,'C':2,'D':3}[m]] for m in group_members]
            gy_min = min(member_ys) - 16
            gy_max = max(member_ys) + 16
            if group_members in (['A','B','C'], ['B','C','D'], ['A','B'], ['C','D']):
                # contiguous monophyletic highlight
                g_x0 = split2_x - 4
                g_x1 = qx + qw - 14
                out.append(
                    f'<rect x="{g_x0}" y="{gy_min}" width="{g_x1 - g_x0}" '
                    f'height="{gy_max - gy_min}" fill="{color}" opacity="0.12" rx="10"/>'
                    f'<rect x="{g_x0}" y="{gy_min}" width="{g_x1 - g_x0}" '
                    f'height="{gy_max - gy_min}" fill="none" stroke="{color}" '
                    f'stroke-width="2" stroke-dasharray="5 3" rx="10"/>'
                )
            else:
                # non-contiguous (paraphyletic) → draw multiple separate highlights
                for m in group_members:
                    mi = {'A':0,'B':1,'C':2,'D':3}[m]
                    my = tip_ys[mi]
                    out.append(
                        f'<rect x="{split2_x - 4}" y="{my - 14}" '
                        f'width="{qx + qw - 18 - (split2_x - 4)}" '
                        f'height="28" fill="{color}" opacity="0.12" rx="6"/>'
                        f'<rect x="{split2_x - 4}" y="{my - 14}" '
                        f'width="{qx + qw - 18 - (split2_x - 4)}" '
                        f'height="28" fill="none" stroke="{color}" '
                        f'stroke-width="1.5" stroke-dasharray="3 3" rx="6"/>'
                    )

        # Branches
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
        marked_set = {m[0] for m in mark_branches}
        for bid, x1, y1, x2, y2 in branches:
            bc = color if bid in marked_set else PAL['muted']
            bw = 3 if bid in marked_set else 2
            out.append(
                f'<line x1="{x1}" y1="{y1:.1f}" x2="{x2}" y2="{y2:.1f}" '
                f'stroke="{bc}" stroke-width="{bw}"/>'
            )

        # Node dots
        for nx, ny in [(split1_x, root_y), (split2_x, node1_y), (split2_x, node2_y)]:
            out.append(
                f'<circle cx="{nx}" cy="{ny:.1f}" r="3" fill="{PAL["border"]}"/>'
            )

        # Character marks on branches
        for bid, mark_color in mark_branches:
            for b in branches:
                if b[0] == bid:
                    mx = (b[1] + b[3]) / 2
                    my = (b[2] + b[4]) / 2 - 10
                    out.append(
                        f'<circle cx="{mx:.0f}" cy="{my:.0f}" r="7" '
                        f'fill="{mark_color}" stroke="{PAL["bg"]}" stroke-width="2"/>'
                        f'<text x="{mx:.0f}" y="{my + 3:.0f}" text-anchor="middle" '
                        f'font-family="Georgia,serif" font-size="9" font-weight="700" '
                        f'fill="{PAL["bg"]}">★</text>'
                    )
                    break

        # Tip labels: Species A-D
        species = ['A', 'B', 'C', 'D']
        for i, ty in enumerate(tip_ys):
            in_group = group_members and species[i] in group_members
            tcolor = color if in_group else PAL['muted']
            out.append(
                f'<circle cx="{tip_x}" cy="{ty:.1f}" r="4" '
                f'fill="{PAL["bg"]}" stroke="{tcolor}" stroke-width="2"/>'
                f'<text x="{tip_label_x}" y="{ty + 4:.1f}" '
                f'font-family="Georgia,serif" font-size="11" font-weight="600" '
                f'fill="{PAL["text"]}">Sp. {species[i]}</text>'
            )

        # Explanation text at bottom
        exp_lines = wrap_text(explanation, max_chars=52)[:2]
        ey_start = qy + qh - 38
        for li, ln in enumerate(exp_lines):
            out.append(
                f'<text x="{qx + 14}" y="{ey_start + li * 14}" '
                f'font-family="Georgia,serif" font-size="11" '
                f'fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
            )
        return out

    # ---- QUAD 1 (top-left): SYNAPOMORPHY ----
    # A derived character shared by ALL and ONLY descendants of one ancestor
    # Mark: a star on 'trunk_mid' branch → inherited by A+B+C+D? no we want the clade
    parts.extend(quadrant(
        PAD, TITLE_H, QUAD_W, QUAD_H,
        '1. Synapomorphy',
        'shared DERIVED character → useful for grouping',
        C_SYN,
        'USEFUL', C_SYN,
        mark_branches=[('trunk_mid', C_SYN), ('to_n1', C_SYN),
                       ('n1_vert', C_SYN), ('tipA', C_SYN), ('tipB', C_SYN)],
        group_members=['A', 'B'],
        explanation='Novel trait (★) appears once and is inherited by clade {A,B}. This defines a valid group.',
        icon_key='star',
    ))

    # ---- QUAD 2 (top-right): PLESIOMORPHY ----
    # An ancestral character retained in some but not all lineages → misleading
    parts.extend(quadrant(
        PAD * 2 + QUAD_W, TITLE_H, QUAD_W, QUAD_H,
        '2. Plesiomorphy',
        'shared ANCESTRAL character → NOT useful for grouping',
        C_PLES,
        'NOT USEFUL', C_PLES,
        mark_branches=[('trunk', C_PLES)],  # character present at the root (ancestral)
        group_members=[],  # no highlighted group
        explanation='Trait (★) was present in the ANCESTOR. Sharing it tells us nothing about who is most related.',
        icon_key='hourglass',
    ))

    # ---- QUAD 3 (bottom-left): MONOPHYLETIC ----
    # A clade = ancestor + ALL descendants. Here: {A, B} (all descendants of node1)
    parts.extend(quadrant(
        PAD, TITLE_H + PAD + QUAD_H, QUAD_W, QUAD_H,
        '3. Monophyletic (Clade)',
        'ancestor + ALL its descendants',
        C_MONO,
        '✓ VALID', C_MONO,
        mark_branches=[('to_n1', C_MONO), ('n1_vert', C_MONO),
                       ('tipA', C_MONO), ('tipB', C_MONO)],
        group_members=['A', 'B'],
        explanation='Group {A,B} includes common ancestor and ALL its descendants. A valid evolutionary group.',
        icon_key='check',
    ))

    # ---- QUAD 4 (bottom-right): PARAPHYLETIC ----
    # Ancestor + SOME descendants (missing one or more)
    # Classic example: "reptiles" excludes birds
    parts.extend(quadrant(
        PAD * 2 + QUAD_W, TITLE_H + PAD + QUAD_H, QUAD_W, QUAD_H,
        '4. Paraphyletic',
        'ancestor + SOME descendants (missing one!)',
        C_PARA,
        '✗ INVALID', C_PARA,
        mark_branches=[],
        # {A, C, D} — skipping B → not contiguous
        group_members=['A', 'C', 'D'],
        explanation='Group {A,C,D} EXCLUDES B even though B shares the same ancestor. Example: "reptiles" excludes birds.',
        icon_key='cross',
    ))

    parts.append('</svg>')
    return ''.join(parts)


'''

# Insert the new function right after svg_cladogram (before svg_timeline)
insert_anchor = '\ndef svg_timeline(node):'
idx = src.index(insert_anchor)
src = src[:idx] + NEW_FUNC + src[idx:]

# Modify pick_svg to route "Cladistics" specifically to the new function
# Add a special case BEFORE the cladogram router
old_picker = '''def pick_svg(node):
    title = node['title'].lower()
    # Highest-priority specific biology illustrations
    if any(k in title for k in CLADOGRAM_KEYWORDS):
        return svg_cladogram(node)'''

new_picker = '''def pick_svg(node):
    title = node['title'].lower()
    # Special dedicated generators (must run before generic cladogram routing)
    if 'cladistics' in title:
        return svg_cladistics_special(node)
    # Highest-priority specific biology illustrations
    if any(k in title for k in CLADOGRAM_KEYWORDS):
        return svg_cladogram(node)'''

if old_picker in src:
    src = src.replace(old_picker, new_picker)
    print('pick_svg updated with Cladistics special route')
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
