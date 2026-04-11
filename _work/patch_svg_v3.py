"""patch_svg_v3.py — Add 5 new biology illustration generators and rewrite pick_svg.

New generators added BEFORE the '# -- layout picker' marker:
  svg_comparison(node)  — side-by-side X-vs-Y two-column panels
  svg_balance(node)     — trade-off balance scale (pros/cons)
  svg_stages(node)      — vertical 4-stage progression with arrows
  svg_landscape(node)   — fitness landscape with peaks and valleys
  svg_network(node)     — node-edge regulatory network

Then rewrites the entire keyword block + pick_svg to include the new types
with priority routing.
"""
import re

PATH = '_work/enrich_v3.py'

with open(PATH, 'r', encoding='utf-8') as f:
    src = f.read()

# ---- 1. Build the new generators block --------------------------------------

NEW_GENERATORS = r'''
# -- comparison layout (2-column side-by-side X vs Y) --------------------

def svg_comparison(node):
    """Side-by-side comparison: 2 columns x 2 rows. Each column gets a heading
    band ('LEFT' / 'RIGHT' or first-pair vs second-pair) and 2 stacked term
    cards. Best for X-vs-Y nodes (qualitative vs quantitative, model vs mimic,
    male vs female, trait vs process)."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W        = 760
    PAD      = 18
    TITLE_H  = 46
    HEAD_H   = 28
    GUTTER_W = 26  # vertical center divider
    COL_W    = (W - PAD * 2 - GUTTER_W) // 2  # ~342

    # Pairing strategy: kt[0,2] -> left column, kt[1,3] -> right column
    # so the visual contrast is between adjacent rows
    left_terms  = [kt[0], kt[2]] if len(kt) >= 3 else kt[:2]
    right_terms = [kt[1], kt[3]] if len(kt) >= 4 else kt[1:3]

    def card_h(t):
        dl = wrap_text(t['def'], max_chars=42)
        return 32 + min(len(dl), 5) * 15 + 14

    left_h  = sum(card_h(t) for t in left_terms) + 14
    right_h = sum(card_h(t) for t in right_terms) + 14
    body_h  = max(left_h, right_h)
    H       = TITLE_H + HEAD_H + 10 + body_h + PAD

    defs_str, _ids = _arrow_defs(nc)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:760px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
        # Title
        f'<text x="{W//2}" y="30" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="20" font-weight="700" '
        f'fill="{PAL["gold"]}">{escape_xml(node["title"].split(":")[0].strip())}</text>',
    ]

    # Column headings (use kt[0] color and kt[1] color as banner colors)
    left_color  = nc.get(left_terms[0].get('color','teal'),  PAL['teal'])
    right_color = nc.get(right_terms[0].get('color','coral') if right_terms else 'coral',
                         PAL['coral'])

    head_y = TITLE_H + 6
    # LEFT heading
    parts.append(
        f'<rect x="{PAD}" y="{head_y}" width="{COL_W}" height="{HEAD_H}" '
        f'fill="{left_color}" opacity="0.22" rx="6"/>'
        f'<text x="{PAD + COL_W//2}" y="{head_y + 19}" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="13" font-weight="700" '
        f'letter-spacing="2" fill="{left_color}">'
        f'{escape_xml(left_terms[0]["term"].upper())}</text>'
    )
    # RIGHT heading
    rx = PAD + COL_W + GUTTER_W
    parts.append(
        f'<rect x="{rx}" y="{head_y}" width="{COL_W}" height="{HEAD_H}" '
        f'fill="{right_color}" opacity="0.22" rx="6"/>'
        f'<text x="{rx + COL_W//2}" y="{head_y + 19}" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="13" font-weight="700" '
        f'letter-spacing="2" fill="{right_color}">'
        f'{escape_xml((right_terms[0]["term"] if right_terms else "VS").upper())}</text>'
    )

    # "vs" divider in the gutter
    div_x = PAD + COL_W + GUTTER_W // 2
    parts.append(
        f'<line x1="{div_x}" y1="{head_y - 2}" x2="{div_x}" y2="{H - PAD//2}" '
        f'stroke="{PAL["border"]}" stroke-width="1" stroke-dasharray="3,4" opacity="0.5"/>'
        f'<circle cx="{div_x}" cy="{head_y + HEAD_H//2}" r="11" '
        f'fill="{PAL["panel"]}" stroke="{PAL["gold"]}" stroke-width="1.5"/>'
        f'<text x="{div_x}" y="{head_y + HEAD_H//2 + 4}" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="11" font-weight="700" '
        f'font-style="italic" fill="{PAL["gold"]}">vs</text>'
    )

    # Body cards
    body_y = head_y + HEAD_H + 10

    def render_column(col_x, terms):
        local = []
        cy = body_y
        for t in terms:
            color = nc.get(t.get('color', 'gray'), PAL['muted'])
            ckey  = t.get('color', 'gray')
            ch    = card_h(t)
            local.append(
                f'<rect x="{col_x}" y="{cy}" width="{COL_W}" height="{ch}" '
                f'fill="{PAL["bg"]}" stroke="{color}" stroke-width="1.5" rx="8"/>'
                f'<rect x="{col_x}" y="{cy}" width="4" height="{ch}" '
                f'fill="{color}" rx="2"/>'
            )
            # Icon + term name
            local.append(_icon_shape(ckey, col_x + 22, cy + 16, 6, color))
            local.append(
                f'<text x="{col_x + 36}" y="{cy + 21}" '
                f'font-family="Georgia,serif" font-size="14" font-weight="700" '
                f'fill="{PAL["text"]}">{escape_xml(t["term"])}</text>'
            )
            # Definition
            def_lines = wrap_text(t['def'], max_chars=42)[:5]
            for li, ln in enumerate(def_lines):
                local.append(
                    f'<text x="{col_x + 14}" y="{cy + 38 + li * 15}" '
                    f'font-family="Georgia,serif" font-size="12" '
                    f'fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
                )
            cy += ch + 6
        return local

    parts.extend(render_column(PAD, left_terms))
    parts.extend(render_column(rx,  right_terms))

    parts.append('</svg>')
    return ''.join(parts)


# -- balance layout (trade-off scale: pros vs cons / costs vs benefits) --

def svg_balance(node):
    """Balance scale showing two opposing forces. Left pan holds first pair
    of terms, right pan holds second pair. Best for trade-off topics (Why Sex?
    costs vs benefits, parental investment, antagonistic pleiotropy)."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W, H     = 760, 460
    PAD      = 20
    TITLE_H  = 44
    cx       = W // 2
    fulcrum_y = H - 78
    beam_y    = fulcrum_y - 110
    pan_w     = 250
    pan_h     = 130
    pan_y     = beam_y + 8

    left_terms  = kt[:2]
    right_terms = kt[2:4] if len(kt) >= 4 else kt[2:3]

    left_color  = nc.get(left_terms[0].get('color','teal'),  PAL['teal'])
    right_color = nc.get(right_terms[0].get('color','coral') if right_terms else 'coral',
                         PAL['coral'])

    defs_str, _ids = _arrow_defs(nc)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:760px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
        f'<text x="{W//2}" y="30" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="20" font-weight="700" '
        f'fill="{PAL["gold"]}">{escape_xml(node["title"].split(":")[0].strip())}</text>',
    ]

    # Subtitle
    parts.append(
        f'<text x="{W//2}" y="52" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="12" font-style="italic" '
        f'fill="{PAL["muted"]}">Trade-off: opposing evolutionary forces</text>'
    )

    # Beam (horizontal balance bar)
    beam_x1 = cx - 290
    beam_x2 = cx + 290
    parts.append(
        f'<line x1="{beam_x1}" y1="{beam_y}" x2="{beam_x2}" y2="{beam_y}" '
        f'stroke="{PAL["gold"]}" stroke-width="4" stroke-linecap="round"/>'
    )
    # Beam pivot triangle
    parts.append(
        f'<polygon points="{cx-14},{fulcrum_y-2} {cx+14},{fulcrum_y-2} {cx},{beam_y}" '
        f'fill="{PAL["gold"]}" opacity="0.85"/>'
        f'<polygon points="{cx-32},{fulcrum_y+50} {cx+32},{fulcrum_y+50} {cx-12},{fulcrum_y-2} {cx+12},{fulcrum_y-2}" '
        f'fill="{PAL["border"]}" stroke="{PAL["gold"]}" stroke-width="2"/>'
    )
    # Chains from beam to pans
    left_pan_cx  = cx - 170
    right_pan_cx = cx + 170
    parts.append(
        f'<line x1="{left_pan_cx}" y1="{beam_y}" x2="{left_pan_cx - 60}" y2="{pan_y}" '
        f'stroke="{PAL["muted"]}" stroke-width="1.5" stroke-dasharray="2,3"/>'
        f'<line x1="{left_pan_cx}" y1="{beam_y}" x2="{left_pan_cx + 60}" y2="{pan_y}" '
        f'stroke="{PAL["muted"]}" stroke-width="1.5" stroke-dasharray="2,3"/>'
        f'<line x1="{right_pan_cx}" y1="{beam_y}" x2="{right_pan_cx - 60}" y2="{pan_y}" '
        f'stroke="{PAL["muted"]}" stroke-width="1.5" stroke-dasharray="2,3"/>'
        f'<line x1="{right_pan_cx}" y1="{beam_y}" x2="{right_pan_cx + 60}" y2="{pan_y}" '
        f'stroke="{PAL["muted"]}" stroke-width="1.5" stroke-dasharray="2,3"/>'
    )

    # PANS — each as a colored card
    def render_pan(pan_cx, color_hex, color_key, side_label, terms):
        local = []
        px = pan_cx - pan_w // 2
        local.append(
            f'<rect x="{px}" y="{pan_y}" width="{pan_w}" height="{pan_h}" '
            f'fill="{PAL["bg"]}" stroke="{color_hex}" stroke-width="2" rx="10"/>'
            f'<rect x="{px}" y="{pan_y}" width="{pan_w}" height="22" '
            f'fill="{color_hex}" opacity="0.22" rx="10"/>'
            f'<text x="{pan_cx}" y="{pan_y + 16}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="11" font-weight="700" '
            f'letter-spacing="2" fill="{color_hex}">{escape_xml(side_label.upper())}</text>'
        )
        # 2 stacked term-rows inside the pan
        ty = pan_y + 32
        for t in terms[:2]:
            tcolor = nc.get(t.get('color','gray'), PAL['muted'])
            tkey   = t.get('color','gray')
            local.append(_icon_shape(tkey, px + 18, ty + 8, 5, tcolor))
            local.append(
                f'<text x="{px + 32}" y="{ty + 12}" '
                f'font-family="Georgia,serif" font-size="13" font-weight="700" '
                f'fill="{PAL["text"]}">{escape_xml(t["term"])}</text>'
            )
            def_lines = wrap_text(t['def'], max_chars=30)[:2]
            for li, ln in enumerate(def_lines):
                local.append(
                    f'<text x="{px + 32}" y="{ty + 28 + li * 13}" '
                    f'font-family="Georgia,serif" font-size="11" '
                    f'fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
                )
            ty += 50
        return local

    parts.extend(render_pan(left_pan_cx,  left_color,  left_terms[0].get('color','teal'),
                            'Costs / Side A',  left_terms))
    parts.extend(render_pan(right_pan_cx, right_color, (right_terms[0].get('color','coral') if right_terms else 'coral'),
                            'Benefits / Side B', right_terms))

    parts.append('</svg>')
    return ''.join(parts)


# -- stages layout (vertical anatomical/developmental progression) -------

def svg_stages(node):
    """Vertical 4-stage progression with downward arrows between stages.
    Each stage gets a numbered badge and color band. Best for anatomical
    progressions (eye evolution, meiosis stages, central dogma)."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W        = 760
    PAD      = 22
    TITLE_H  = 46
    STAGE_H  = 84
    GAP      = 22  # space for the arrow between stages
    BOX_W    = W - PAD * 2

    n_stages = min(len(kt), 4)
    H = TITLE_H + 12 + STAGE_H * n_stages + GAP * (n_stages - 1) + PAD

    color_map = {t.get('color','gray'): nc.get(t.get('color','gray'), PAL['muted'])
                 for t in kt[:n_stages]}
    defs_str, marker_ids = _arrow_defs(color_map)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:760px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
        f'<text x="{W//2}" y="30" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="20" font-weight="700" '
        f'fill="{PAL["gold"]}">{escape_xml(node["title"].split(":")[0].strip())}</text>',
    ]

    cy = TITLE_H + 12
    for i, t in enumerate(kt[:n_stages]):
        color = nc.get(t.get('color','gray'), PAL['muted'])
        ckey  = t.get('color','gray')
        # Stage box
        parts.append(
            f'<rect x="{PAD}" y="{cy}" width="{BOX_W}" height="{STAGE_H}" '
            f'fill="{PAL["bg"]}" stroke="{color}" stroke-width="2" rx="10"/>'
            # Left color stripe
            f'<rect x="{PAD}" y="{cy}" width="6" height="{STAGE_H}" '
            f'fill="{color}" rx="3"/>'
        )
        # Stage number badge (large, on the left)
        badge_cx = PAD + 50
        badge_cy = cy + STAGE_H // 2
        parts.append(
            f'<circle cx="{badge_cx}" cy="{badge_cy}" r="24" '
            f'fill="{color}" opacity="0.2"/>'
            f'<circle cx="{badge_cx}" cy="{badge_cy}" r="20" '
            f'fill="none" stroke="{color}" stroke-width="2"/>'
            f'<text x="{badge_cx}" y="{badge_cy + 7}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="20" font-weight="700" '
            f'fill="{color}">{i+1}</text>'
        )
        # Type icon to the right of badge
        parts.append(_icon_shape(ckey, badge_cx + 38, badge_cy - 18, 7, color))
        # Term name (right of badge, top)
        parts.append(
            f'<text x="{badge_cx + 52}" y="{badge_cy - 14}" '
            f'font-family="Georgia,serif" font-size="16" font-weight="700" '
            f'fill="{PAL["text"]}">{escape_xml(t["term"])}</text>'
        )
        # Definition (wraps below term)
        def_lines = wrap_text(t['def'], max_chars=68)[:3]
        for li, ln in enumerate(def_lines):
            parts.append(
                f'<text x="{badge_cx + 52}" y="{badge_cy + 6 + li * 14}" '
                f'font-family="Georgia,serif" font-size="12" '
                f'fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
            )

        # Arrow to next stage
        if i < n_stages - 1:
            arrow_x  = W // 2
            arrow_y1 = cy + STAGE_H + 4
            arrow_y2 = cy + STAGE_H + GAP - 4
            mid = marker_ids[ckey]
            parts.append(
                f'<line x1="{arrow_x}" y1="{arrow_y1}" x2="{arrow_x}" y2="{arrow_y2}" '
                f'stroke="{color}" stroke-width="2.5" marker-end="url(#{mid})"/>'
            )

        cy += STAGE_H + GAP

    parts.append('</svg>')
    return ''.join(parts)


# -- landscape layout (fitness peaks, valleys, ridges) ------------------

def svg_landscape(node):
    """Fitness landscape with sinusoidal terrain, two labeled peaks, one
    valley, and four term cards positioned along the curve. Best for fitness
    landscape, adaptive peaks, optimization topics."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W, H     = 760, 460
    PAD      = 20
    TITLE_H  = 46
    BASE_Y   = 320  # the y of the curve baseline (high y = low fitness)
    AXIS_X1  = 60
    AXIS_X2  = W - 60

    defs_str, _ids = _arrow_defs(nc)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:760px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
        f'<text x="{W//2}" y="30" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="20" font-weight="700" '
        f'fill="{PAL["gold"]}">{escape_xml(node["title"].split(":")[0].strip())}</text>',
    ]

    # Y-axis label (Fitness)
    parts.append(
        f'<line x1="{AXIS_X1}" y1="{TITLE_H + 18}" x2="{AXIS_X1}" y2="{BASE_Y}" '
        f'stroke="{PAL["muted"]}" stroke-width="1.5"/>'
        f'<text x="{AXIS_X1 - 8}" y="{TITLE_H + 30}" text-anchor="end" '
        f'font-family="Georgia,serif" font-size="11" font-weight="700" '
        f'fill="{PAL["muted"]}">Fitness</text>'
        f'<text x="{AXIS_X1 - 8}" y="{TITLE_H + 44}" text-anchor="end" '
        f'font-family="Georgia,serif" font-size="10" '
        f'fill="{PAL["muted"]}">(high)</text>'
        f'<text x="{AXIS_X1 - 8}" y="{BASE_Y - 4}" text-anchor="end" '
        f'font-family="Georgia,serif" font-size="10" '
        f'fill="{PAL["muted"]}">(low)</text>'
    )
    # X-axis (genotype space)
    parts.append(
        f'<line x1="{AXIS_X1}" y1="{BASE_Y}" x2="{AXIS_X2}" y2="{BASE_Y}" '
        f'stroke="{PAL["muted"]}" stroke-width="1.5"/>'
        f'<text x="{(AXIS_X1+AXIS_X2)//2}" y="{BASE_Y + 22}" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="11" font-weight="700" '
        f'fill="{PAL["muted"]}">Genotype / Trait Space ?</text>'
    )

    # Build the landscape curve as a polyline (two peaks, one valley)
    import math as _m
    points = []
    span = AXIS_X2 - AXIS_X1
    for px in range(0, span + 1, 6):
        x = AXIS_X1 + px
        u = px / span  # 0..1
        # Two peaks at u~0.25 and u~0.75, valley at u~0.5
        y_norm = (_m.sin(u * _m.pi * 2) + 1) / 2  # 0..1
        # Make the right peak slightly higher
        y_norm = y_norm * (0.85 + 0.3 * u)
        y = BASE_Y - 10 - y_norm * 175
        points.append((x, y))

    # Filled area under curve
    poly = ' '.join(f'{p[0]},{p[1]}' for p in points)
    parts.append(
        f'<polygon points="{AXIS_X1},{BASE_Y} {poly} {AXIS_X2},{BASE_Y}" '
        f'fill="{PAL["teal"]}" opacity="0.10"/>'
        f'<polyline points="{poly}" fill="none" stroke="{PAL["teal"]}" stroke-width="2.5"/>'
    )

    # Mark two peaks and valley
    # Find approximate maxima/minima
    peaks = []
    valleys = []
    for i in range(1, len(points) - 1):
        if points[i][1] < points[i-1][1] and points[i][1] < points[i+1][1]:
            peaks.append(points[i])
        elif points[i][1] > points[i-1][1] and points[i][1] > points[i+1][1]:
            valleys.append(points[i])

    # Place 4 term cards along the curve at evenly spaced x's,
    # with each card pinned above its curve point
    if len(kt) >= 4:
        positions_idx = [int(len(points) * f) for f in (0.15, 0.4, 0.6, 0.85)]
        for i, idx in enumerate(positions_idx):
            cx, cy = points[idx]
            t = kt[i]
            color = nc.get(t.get('color','gray'), PAL['muted'])
            ckey  = t.get('color','gray')
            # Card placement: alternate above/below depending on space
            cw, ch = 152, 60
            cx0 = max(AXIS_X1 + 4, min(W - AXIS_X1 - cw, cx - cw // 2))
            cy0 = max(TITLE_H + 18, cy - ch - 18)
            # Connector dot on curve
            parts.append(
                f'<circle cx="{cx}" cy="{cy}" r="5" fill="{color}" '
                f'stroke="{PAL["panel"]}" stroke-width="2"/>'
            )
            # Connector line from card to curve
            parts.append(
                f'<line x1="{cx0 + cw//2}" y1="{cy0 + ch}" x2="{cx}" y2="{cy}" '
                f'stroke="{color}" stroke-width="1" stroke-dasharray="2,3" opacity="0.6"/>'
            )
            # Card
            parts.append(
                f'<rect x="{cx0}" y="{cy0}" width="{cw}" height="{ch}" '
                f'fill="{PAL["bg"]}" stroke="{color}" stroke-width="1.5" rx="6"/>'
                f'<rect x="{cx0}" y="{cy0}" width="{cw}" height="3" '
                f'fill="{color}" rx="2"/>'
            )
            parts.append(_icon_shape(ckey, cx0 + 12, cy0 + 16, 5, color))
            parts.append(
                f'<text x="{cx0 + 24}" y="{cy0 + 19}" '
                f'font-family="Georgia,serif" font-size="12" font-weight="700" '
                f'fill="{PAL["text"]}">{escape_xml(t["term"][:24])}</text>'
            )
            def_lines = wrap_text(t['def'], max_chars=24)[:2]
            for li, ln in enumerate(def_lines):
                parts.append(
                    f'<text x="{cx0 + 8}" y="{cy0 + 34 + li * 12}" '
                    f'font-family="Georgia,serif" font-size="10" '
                    f'fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
                )

    # Peak / valley labels
    if len(peaks) >= 2:
        parts.append(
            f'<text x="{peaks[0][0]}" y="{peaks[0][1] - 8}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="10" font-style="italic" '
            f'fill="{PAL["gold"]}" opacity="0.7">peak</text>'
        )
        parts.append(
            f'<text x="{peaks[-1][0]}" y="{peaks[-1][1] - 8}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="10" font-style="italic" '
            f'fill="{PAL["gold"]}" opacity="0.7">peak</text>'
        )
    if valleys:
        parts.append(
            f'<text x="{valleys[0][0]}" y="{valleys[0][1] + 16}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="10" font-style="italic" '
            f'fill="{PAL["muted"]}">valley</text>'
        )

    # Footer
    footer = wrap_text(v2['definition'], max_chars=92)[:2]
    fy = H - 40
    for li, ln in enumerate(footer):
        parts.append(
            f'<text x="{W//2}" y="{fy + li * 14}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="11" '
            f'fill="{PAL["gold"]}" opacity="0.65">{escape_xml(ln)}</text>'
        )

    parts.append('</svg>')
    return ''.join(parts)


# -- network layout (regulatory / interaction graph) --------------------

def svg_network(node):
    """Node-edge network diagram. Central hub node with 4 satellite nodes
    connected by labeled edges. Best for regulatory networks, gene
    interaction, evo-devo, food webs."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W, H = 760, 480
    cx, cy = W // 2, H // 2 + 18
    R      = 165
    sat_r  = 60
    hub_r  = 50

    color_map = {t.get('color','gray'): nc.get(t.get('color','gray'), PAL['muted'])
                 for t in kt[:4]}
    defs_str, marker_ids = _arrow_defs(color_map)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:760px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
        f'<text x="{W//2}" y="30" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="20" font-weight="700" '
        f'fill="{PAL["gold"]}">{escape_xml(node["title"].split(":")[0].strip())}</text>',
    ]

    import math as _m
    n_sat = min(len(kt), 4)
    # Place satellites at angles -90, 0, 90, 180 (top, right, bottom, left)
    angles = [-_m.pi/2, 0, _m.pi/2, _m.pi]
    sat_positions = []
    for i in range(n_sat):
        sx = cx + R * _m.cos(angles[i])
        sy = cy + R * _m.sin(angles[i])
        sat_positions.append((sx, sy))

    # Edges from hub to each satellite
    for i, (sx, sy) in enumerate(sat_positions):
        t = kt[i]
        color = nc.get(t.get('color','gray'), PAL['muted'])
        ckey  = t.get('color','gray')
        mid   = marker_ids.get(ckey, list(marker_ids.values())[0])
        # Stop short of the satellite circle
        dx = sx - cx
        dy = sy - cy
        length = (dx*dx + dy*dy) ** 0.5
        ux, uy = dx / length, dy / length
        x1 = cx + ux * (hub_r + 4)
        y1 = cy + uy * (hub_r + 4)
        x2 = sx - ux * (sat_r + 8)
        y2 = sy - uy * (sat_r + 8)
        parts.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{color}" stroke-width="2.5" marker-end="url(#{mid})" opacity="0.75"/>'
        )

    # Hub node (central)
    parts.append(
        f'<circle cx="{cx}" cy="{cy}" r="{hub_r}" fill="{PAL["bg"]}" '
        f'stroke="{PAL["gold"]}" stroke-width="3"/>'
        f'<circle cx="{cx}" cy="{cy}" r="{hub_r-6}" fill="none" '
        f'stroke="{PAL["gold"]}" stroke-width="1" opacity="0.5"/>'
    )
    hub_label = node['title'].split(':')[0].strip()
    hub_lines = wrap_text(hub_label, max_chars=12)[:2]
    base = cy + 4 - (len(hub_lines) - 1) * 8
    for li, ln in enumerate(hub_lines):
        parts.append(
            f'<text x="{cx}" y="{base + li * 14}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="12" font-weight="700" '
            f'fill="{PAL["gold"]}">{escape_xml(ln)}</text>'
        )

    # Satellite nodes
    for i, (sx, sy) in enumerate(sat_positions):
        t = kt[i]
        color = nc.get(t.get('color','gray'), PAL['muted'])
        ckey  = t.get('color','gray')
        sx, sy = int(sx), int(sy)
        parts.append(
            f'<circle cx="{sx}" cy="{sy}" r="{sat_r}" fill="{PAL["bg"]}" '
            f'stroke="{color}" stroke-width="2.5"/>'
            f'<circle cx="{sx}" cy="{sy}" r="{sat_r}" fill="{color}" opacity="0.10"/>'
        )
        parts.append(_icon_shape(ckey, sx, sy - 32, 6, color))
        # Term name (multi-line)
        term_lines = wrap_text(t['term'], max_chars=14)[:2]
        tbase = sy - 4
        for li, ln in enumerate(term_lines):
            parts.append(
                f'<text x="{sx}" y="{tbase + li * 13}" text-anchor="middle" '
                f'font-family="Georgia,serif" font-size="11" font-weight="700" '
                f'fill="{PAL["text"]}">{escape_xml(ln)}</text>'
            )
        # Short definition (1 line, very short)
        def_lines = wrap_text(t['def'], max_chars=16)[:2]
        dbase = sy + 22
        for li, ln in enumerate(def_lines):
            parts.append(
                f'<text x="{sx}" y="{dbase + li * 11}" text-anchor="middle" '
                f'font-family="Georgia,serif" font-size="9" '
                f'fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
            )

    parts.append('</svg>')
    return ''.join(parts)

'''

# ---- 2. Splice the new generators in BEFORE '# -- layout picker' -----------

MARKER = '\n# -- layout picker'
idx = src.index(MARKER)
src_new = src[:idx] + NEW_GENERATORS + src[idx:]

# ---- 3. Replace the keyword/routing block --------------------------------

# Find the start of CLADOGRAM_KEYWORDS = and end at the closing of pick_svg
kw_start = src_new.index('CLADOGRAM_KEYWORDS = [')
# Find end: the next blank line after pick_svg's `return svg_four_box(node)`
end_marker = '    return svg_four_box(node)\n'
end_pos = src_new.index(end_marker, kw_start) + len(end_marker)

NEW_ROUTING = '''CLADOGRAM_KEYWORDS = [
    'tree thinking', 'cladistic', 'synapomorph', 'monophyletic',
    'parsimony', 'homoplasy', 'convergence', 'tiktaalik',
    'fins to limb', 'feather', 'exaptation', 'transitional fossil',
    'phylo', 'clade', 'descent with modification', 'common ancestry',
    'human evolution',
]
TIMELINE_KEYWORDS = [
    'deep time', 'age of earth', 'age of the earth', 'origin of life',
    'prebiotic', 'stromatolite', 'cambrian', 'mesozoic', 'paleozoic',
    'cenozoic', 'history of life', 'mass extinction', 'k-t', 'early life',
    'darwin', 'beagle', 'pre-darwin',
]
PROCESS_KEYWORDS = [
    'four ingredients', 'mechanism', 'genetic drift', 'bottleneck',
    'founder', 'hardy-weinberg', 'breeders equation', 'heritability',
    'reaction norm', 'plasticity', 'genotype-phenotype', 'mutation',
    'sources of evolutionary', 'gene expression', 'flu virus',
    'evolution in action', 'biogeograph', 'speciation',
]
STAGES_KEYWORDS = [
    'eye evolution', 'photoreceptor', 'camera eye', 'meiosis', 'meiotic',
    'sex cells', 'central dogma', 'protein synthesis',
    'evo-devo', 'regulatory network', 'hox',
    'endosymbiosis', 'origin of', 'multicellular',
]
COMPARISON_KEYWORDS = [
    'qualitative vs', 'quantitative', 'trait vs process',
    'mullerian', 'batesian', 'mimicry',
    'male strategies', 'female choice', 'beach mice', 'parallel evolution',
    'temperature-dependent', 'sex determination',
    'qualitative', 'group vs individual', 'levels of selection',
    'evolutionary medicine',
]
BALANCE_KEYWORDS = [
    'why sex', 'cost', 'benefit', 'trade-off', 'tradeoff',
    'imperfect adaptation', 'antagonistic pleiotropy',
    'parental investment', 'sex allocation',
    'extrinsic mortality', 'aging', 'senescence',
    'sperm competition', 'sexual conflict',
]
LANDSCAPE_KEYWORDS = [
    'fitness landscape', 'adaptive peak', 'fitness peak', 'landscape',
]
NETWORK_KEYWORDS = [
    'network', 'kin selection', 'inclusive fitness', 'altruism',
    'conservation', 'humans as selective force',
    'lecture 1 take-home',
]

# Generic conceptual layouts (lower-priority fallbacks)
CYCLE_KEYWORDS = [
    'selection', 'cycle', 'reproduction', 'coevolution', 'life history',
    'game', 'mating', 'strategy', 'ingredients', 'arms race',
    'anisogamy',
]
HIERARCHY_KEYWORDS = [
    'species concept', 'reproductive isolation', 'taxonom',
    'classification',
]


def pick_svg(node):
    title = node['title'].lower()
    # Highest-priority specific biology illustrations
    if any(k in title for k in CLADOGRAM_KEYWORDS):
        return svg_cladogram(node)
    if any(k in title for k in TIMELINE_KEYWORDS):
        return svg_timeline(node)
    if any(k in title for k in STAGES_KEYWORDS):
        return svg_stages(node)
    if any(k in title for k in LANDSCAPE_KEYWORDS):
        return svg_landscape(node)
    if any(k in title for k in NETWORK_KEYWORDS):
        return svg_network(node)
    if any(k in title for k in BALANCE_KEYWORDS):
        return svg_balance(node)
    if any(k in title for k in COMPARISON_KEYWORDS):
        return svg_comparison(node)
    if any(k in title for k in PROCESS_KEYWORDS):
        return svg_process_flow(node)
    # Lower-priority generics
    if any(k in title for k in CYCLE_KEYWORDS):
        return svg_cycle(node)
    if any(k in title for k in HIERARCHY_KEYWORDS):
        return svg_hierarchy(node)
    return svg_four_box(node)
'''

src_final = src_new[:kw_start] + NEW_ROUTING + src_new[end_pos:]

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(src_final)

print(f'Patched {PATH}')
print(f'  Old size: {len(src):,} bytes')
print(f'  New size: {len(src_final):,} bytes')
print(f'  Delta:    +{len(src_final) - len(src):,} bytes')
