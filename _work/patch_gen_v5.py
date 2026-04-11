"""patch_gen_v5.py — Rewrite all remaining SVG generators to presentation quality.

Replaces each generator's function body with a richer, icon-powered design
matching the reference-quality cladogram.
"""
import re

PATH = '_work/enrich_v3.py'

with open(PATH, 'r', encoding='utf-8') as f:
    src = f.read()

def replace_function(src, fn_name, new_body):
    """Replace a function's entire body with new_body (a complete def block
    starting with 'def fn_name(node):' and ending with the last return line
    before the next def).

    The new_body must include the 'def ...(node):' signature.
    """
    start = src.index(f'def {fn_name}(node):')
    # Find the next 'def ' at top level (zero indent) after start
    search_from = start + 10
    m = re.search(r'\ndef ', src[search_from:])
    if not m:
        raise ValueError(f'No function after {fn_name}')
    end = search_from + m.start() + 1  # keep the newline before next def
    return src[:start] + new_body + src[end:]


# ============================================================================
# svg_four_box — icon in header band, full-width definition footer
# ============================================================================

NEW_FOUR_BOX = '''def svg_four_box(node):
    """2x2 grid of term cards. Each card has: icon + term name in header band,
    definition below. Footer strip shows the node's overall definition."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W        = 860
    PAD      = 22
    TITLE_H  = 70
    FOOTER_H = 46
    HEADER_H = 44
    CELL_W   = (W - PAD * 3) // 2

    def cell_content_h(t):
        dl = wrap_text(t['def'], max_chars=42)
        return HEADER_H + 14 + min(len(dl), 6) * 16 + 16

    cell_heights = [cell_content_h(t) for t in kt[:4]]
    if len(cell_heights) < 4:
        cell_heights = (cell_heights + [80] * 4)[:4]
    row0_h = max(cell_heights[0], cell_heights[1])
    row1_h = max(cell_heights[2], cell_heights[3])
    H = TITLE_H + PAD + row0_h + PAD + row1_h + PAD + FOOTER_H + 10

    color_map = {k: v for k, v in nc.items()}
    defs_str, _ids = _arrow_defs(color_map)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:900px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
    ]

    # Title + subtitle
    main_title = node['title'].split(':')[0].strip()
    parts.append(
        f'<text x="{W//2}" y="36" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="24" font-weight="700" '
        f'fill="{PAL["text"]}">{escape_xml(main_title)}</text>'
    )
    subtitle_lines = wrap_text(v2['definition'], max_chars=88)[:1]
    if subtitle_lines:
        parts.append(
            f'<text x="{W//2}" y="58" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="13" font-style="italic" '
            f'fill="{PAL["gold"]}" opacity="0.85">'
            f'{escape_xml(subtitle_lines[0])}</text>'
        )

    positions = [
        (PAD,               TITLE_H,                   row0_h),
        (PAD*2 + CELL_W,    TITLE_H,                   row0_h),
        (PAD,               TITLE_H + PAD + row0_h,    row1_h),
        (PAD*2 + CELL_W,    TITLE_H + PAD + row0_h,    row1_h),
    ]

    for i, t in enumerate(kt[:4]):
        x, y, cell_h = positions[i]
        color = nc.get(t.get('color', 'gray'), PAL['muted'])
        ckey  = t.get('color', 'gray')
        icon_key = _pick_bio_icon(ckey, t['term'])

        # Card background
        parts.append(
            f'<rect x="{x}" y="{y}" width="{CELL_W}" height="{cell_h}" '
            f'fill="{PAL["bg"]}" stroke="{color}" stroke-width="2" rx="10"/>'
        )
        # Header band (translucent color fill)
        parts.append(
            f'<rect x="{x}" y="{y}" width="{CELL_W}" height="{HEADER_H}" '
            f'fill="{color}" opacity="0.18"/>'
            f'<line x1="{x}" y1="{y+HEADER_H}" x2="{x+CELL_W}" y2="{y+HEADER_H}" '
            f'stroke="{color}" stroke-width="2" opacity="0.6"/>'
        )
        # Big icon on the left of the header
        parts.append(
            f'<circle cx="{x+26}" cy="{y+HEADER_H//2}" r="17" '
            f'fill="{color}" fill-opacity="0.15" stroke="{color}" stroke-width="1.5"/>'
        )
        parts.append(_bio_icon(icon_key, x+26, y+HEADER_H//2, 11, color,
                               stroke_width=2, fill_mode='stroke'))
        # Term name (right of icon)
        term_lines = wrap_text(t['term'], max_chars=26)[:2]
        term_base_y = y + HEADER_H//2 - (len(term_lines) - 1) * 9 + 5
        for li, ln in enumerate(term_lines):
            parts.append(
                f'<text x="{x+50}" y="{term_base_y + li * 17}" '
                f'font-family="Georgia,serif" font-size="15" font-weight="700" '
                f'fill="{PAL["text"]}">{escape_xml(ln)}</text>'
            )
        # Definition text
        def_y = y + HEADER_H + 20
        def_lines = wrap_text(t['def'], max_chars=42)
        for li, ln in enumerate(def_lines[:6]):
            parts.append(
                f'<text x="{x+16}" y="{def_y + li * 16}" '
                f'font-family="Georgia,serif" font-size="13" '
                f'fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
            )

    # Footer strip: mnemonic or long definition
    footer_y = H - FOOTER_H - 6
    parts.append(
        f'<rect x="{PAD}" y="{footer_y}" width="{W - PAD*2}" height="{FOOTER_H}" '
        f'fill="{PAL["gold"]}" fill-opacity="0.08" stroke="{PAL["gold"]}" '
        f'stroke-width="1" stroke-opacity="0.4" rx="8"/>'
    )
    mnemonic_text = v2.get('mnemonic', {}).get('hook', v2['definition'])
    footer_lines = wrap_text(mnemonic_text, max_chars=110)[:2]
    for li, ln in enumerate(footer_lines):
        parts.append(
            f'<text x="{W//2}" y="{footer_y + 20 + li * 15}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="12" font-style="italic" '
            f'fill="{PAL["gold"]}" opacity="0.85">{escape_xml(ln)}</text>'
        )

    parts.append('</svg>')
    return ''.join(parts)
'''

src = replace_function(src, 'svg_four_box', NEW_FOUR_BOX)
print('Step A: svg_four_box replaced')

# ============================================================================
# svg_cycle — icon inside each circle + curved arrows + center hub
# ============================================================================

NEW_CYCLE = '''def svg_cycle(node):
    """Circular cycle of 4 terms with big biological icons inside each circle,
    curved bezier arrows between them, and a central hub label."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W, H = 900, 600
    cx, cy = W // 2, H // 2 + 28
    R = 200
    node_r = 88
    TITLE_H = 70

    color_map = {t.get('color', 'gray'): nc.get(t.get('color', 'gray'), PAL['muted'])
                 for t in kt[:4]}
    defs_str, marker_ids = _arrow_defs(color_map)

    n = len(kt[:4])
    positions = []
    for i in range(n):
        angle = -math.pi / 2 + (2 * math.pi * i / n)
        positions.append((cx + R * math.cos(angle), cy + R * math.sin(angle)))

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:900px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
    ]

    # Title + subtitle
    main_title = node['title'].split(':')[0].strip()
    parts.append(
        f'<text x="{cx}" y="38" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="26" font-weight="700" '
        f'fill="{PAL["text"]}">{escape_xml(main_title)}</text>'
    )
    subtitle_lines = wrap_text(v2['definition'], max_chars=90)[:1]
    if subtitle_lines:
        parts.append(
            f'<text x="{cx}" y="62" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="13" font-style="italic" '
            f'fill="{PAL["gold"]}" opacity="0.85">'
            f'{escape_xml(subtitle_lines[0])}</text>'
        )

    # Central dashed ring
    parts.append(
        f'<circle cx="{cx}" cy="{cy}" r="{R - 68}" fill="none" '
        f'stroke="{PAL["border"]}" stroke-width="1.5" stroke-dasharray="4 6"/>'
        f'<circle cx="{cx}" cy="{cy}" r="52" fill="{PAL["bg"]}" '
        f'stroke="{PAL["gold"]}" stroke-width="2.5"/>'
    )
    # Center hub label
    hub_lines = wrap_text(main_title, max_chars=14)[:2]
    hub_base = cy - (len(hub_lines) - 1) * 9 + 5
    for li, ln in enumerate(hub_lines):
        parts.append(
            f'<text x="{cx}" y="{hub_base + li * 17}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="14" font-weight="700" '
            f'fill="{PAL["gold"]}">{escape_xml(ln)}</text>'
        )

    # Curved bezier arrows between adjacent circles (CW)
    for i in range(n):
        j = (i + 1) % n
        px_i, py_i = positions[i]
        px_j, py_j = positions[j]
        color_i = nc.get(kt[i].get('color', 'gray'), PAL['muted'])
        mid_i   = marker_ids.get(kt[i].get('color', 'gray'))

        dx, dy = px_j - px_i, py_j - py_i
        dist   = math.sqrt(dx*dx + dy*dy) or 1
        ux, uy = dx / dist, dy / dist

        sx = px_i + ux * (node_r + 6)
        sy = py_i + uy * (node_r + 6)
        ex = px_j - ux * (node_r + 18)
        ey = py_j - uy * (node_r + 18)

        mid_mx = (px_i + px_j) / 2
        mid_my = (py_i + py_j) / 2
        omx, omy = mid_mx - cx, mid_my - cy
        omag = math.sqrt(omx*omx + omy*omy) or 1
        ctrl_x = cx + (omx / omag) * (R + 42)
        ctrl_y = cy + (omy / omag) * (R + 42)

        mk = f' marker-end="url(#{mid_i})"' if mid_i else ''
        parts.append(
            f'<path d="M {sx:.1f},{sy:.1f} Q {ctrl_x:.1f},{ctrl_y:.1f} {ex:.1f},{ey:.1f}" '
            f'fill="none" stroke="{color_i}" stroke-width="2.5" opacity="0.8"{mk}/>'
        )

    # Circles with icons + text
    for i, t in enumerate(kt[:4]):
        x, y  = positions[i]
        color = nc.get(t.get('color', 'gray'), PAL['muted'])
        ckey  = t.get('color', 'gray')
        icon_key = _pick_bio_icon(ckey, t['term'])

        parts.append(
            f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{node_r}" '
            f'fill="{PAL["bg"]}" stroke="{color}" stroke-width="3"/>'
            f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{node_r}" '
            f'fill="{color}" opacity="0.08"/>'
        )
        # Big icon at the top of the circle
        parts.append(_bio_icon(icon_key, x, y - 32, 18, color,
                               stroke_width=2.2, fill_mode='stroke'))
        # Term name below icon
        term_lines = wrap_text(t['term'], max_chars=14)[:2]
        tbase = y - 2
        for li, ln in enumerate(term_lines):
            parts.append(
                f'<text x="{x:.0f}" y="{tbase + li * 15:.0f}" text-anchor="middle" '
                f'font-family="Georgia,serif" font-size="13" font-weight="700" '
                f'fill="{PAL["text"]}">{escape_xml(ln)}</text>'
            )
        # Short def below term
        def_lines = wrap_text(t['def'], max_chars=16)[:3]
        def_base = y + 22 + len(term_lines) * 15 - 15
        for li, ln in enumerate(def_lines):
            parts.append(
                f'<text x="{x:.0f}" y="{def_base + li * 11:.0f}" text-anchor="middle" '
                f'font-family="Georgia,serif" font-size="9.5" '
                f'fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
            )

        # Step number badge on top-left
        parts.append(
            f'<circle cx="{x - node_r + 16:.0f}" cy="{y - node_r + 16:.0f}" '
            f'r="13" fill="{PAL["gold"]}" stroke="{PAL["panel"]}" stroke-width="2"/>'
            f'<text x="{x - node_r + 16:.0f}" y="{y - node_r + 21:.0f}" '
            f'text-anchor="middle" font-family="Georgia,serif" '
            f'font-size="13" font-weight="700" fill="{PAL["bg"]}">{i+1}</text>'
        )

    parts.append('</svg>')
    return ''.join(parts)
'''

src = replace_function(src, 'svg_cycle', NEW_CYCLE)
print('Step B: svg_cycle replaced')

# ============================================================================
# svg_process_flow — larger step tiles with big icons, chevron arrows, footer
# ============================================================================

NEW_PROCESS = '''def svg_process_flow(node):
    """Horizontal 4-step process flow with LARGE icon tiles, numbered badges,
    chevron-shaped arrow connectors, and a footer strip with the overall def."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W = 900
    PAD = 22
    TITLE_H = 70
    FOOTER_H = 52

    BOX_W    = 192
    BOX_H    = 220
    ARROW_W  = 28
    total_content_w = BOX_W * 4 + ARROW_W * 3
    start_x = (W - total_content_w) // 2

    H = TITLE_H + BOX_H + FOOTER_H + 30

    color_map = {t.get('color', 'gray'): nc.get(t.get('color', 'gray'), PAL['muted'])
                 for t in kt[:4]}
    defs_str, _mids = _arrow_defs(color_map)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:900px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
    ]

    # Title + subtitle
    main_title = node['title'].split(':')[0].strip()
    parts.append(
        f'<text x="{W//2}" y="38" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="26" font-weight="700" '
        f'fill="{PAL["text"]}">{escape_xml(main_title)}</text>'
    )
    subtitle_lines = wrap_text(v2['definition'], max_chars=100)[:1]
    if subtitle_lines:
        parts.append(
            f'<text x="{W//2}" y="62" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="13" font-style="italic" '
            f'fill="{PAL["gold"]}" opacity="0.85">'
            f'{escape_xml(subtitle_lines[0])}</text>'
        )

    cy_top = TITLE_H + 10
    for i, t in enumerate(kt[:4]):
        color = nc.get(t.get('color', 'gray'), PAL['muted'])
        ckey  = t.get('color', 'gray')
        icon_key = _pick_bio_icon(ckey, t['term'])
        box_x = start_x + i * (BOX_W + ARROW_W)

        # Tile background
        parts.append(
            f'<rect x="{box_x}" y="{cy_top}" width="{BOX_W}" height="{BOX_H}" '
            f'fill="{PAL["bg"]}" stroke="{color}" stroke-width="2.5" rx="12"/>'
        )
        # Colored top band
        parts.append(
            f'<rect x="{box_x}" y="{cy_top}" width="{BOX_W}" height="6" '
            f'fill="{color}" rx="3"/>'
        )
        # Step number badge (top-right)
        parts.append(
            f'<circle cx="{box_x + BOX_W - 22}" cy="{cy_top + 26}" r="15" '
            f'fill="{color}" stroke="{PAL["panel"]}" stroke-width="2"/>'
            f'<text x="{box_x + BOX_W - 22}" y="{cy_top + 31}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="14" font-weight="700" '
            f'fill="{PAL["bg"]}">{i+1}</text>'
        )
        # Large icon in upper portion (circle background)
        icon_cx = box_x + BOX_W // 2
        icon_cy = cy_top + 72
        parts.append(
            f'<circle cx="{icon_cx}" cy="{icon_cy}" r="38" '
            f'fill="{color}" fill-opacity="0.10" stroke="{color}" '
            f'stroke-width="1.5" stroke-opacity="0.5"/>'
        )
        parts.append(_bio_icon(icon_key, icon_cx, icon_cy, 26, color,
                               stroke_width=2.2, fill_mode='stroke'))
        # Term name below icon
        term_lines = wrap_text(t['term'], max_chars=16)[:2]
        tbase = cy_top + 132
        for li, ln in enumerate(term_lines):
            parts.append(
                f'<text x="{icon_cx}" y="{tbase + li * 18}" text-anchor="middle" '
                f'font-family="Georgia,serif" font-size="15" font-weight="700" '
                f'fill="{PAL["text"]}">{escape_xml(ln)}</text>'
            )
        # Definition below term
        def_lines = wrap_text(t['def'], max_chars=22)[:3]
        def_base = tbase + len(term_lines) * 18 + 6
        for li, ln in enumerate(def_lines):
            parts.append(
                f'<text x="{icon_cx}" y="{def_base + li * 13}" text-anchor="middle" '
                f'font-family="Georgia,serif" font-size="11" '
                f'fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
            )

        # Chevron arrow to next tile
        if i < 3:
            ax = box_x + BOX_W
            ay = cy_top + BOX_H // 2
            arrow_color = color
            pts = [
                f'{ax + 2},{ay - 14}',
                f'{ax + ARROW_W - 4},{ay}',
                f'{ax + 2},{ay + 14}',
                f'{ax + 8},{ay}',
            ]
            parts.append(
                f'<polygon points="{" ".join(pts)}" fill="{arrow_color}" '
                f'opacity="0.85"/>'
            )

    # Footer: mnemonic or exam trap
    footer_y = H - FOOTER_H - 10
    parts.append(
        f'<rect x="{PAD}" y="{footer_y}" width="{W - PAD*2}" height="{FOOTER_H}" '
        f'fill="{PAL["gold"]}" fill-opacity="0.08" stroke="{PAL["gold"]}" '
        f'stroke-width="1" stroke-opacity="0.4" rx="8"/>'
    )
    mnemonic_text = v2.get('mnemonic', {}).get('hook', '')
    if mnemonic_text:
        footer_lines = wrap_text(mnemonic_text, max_chars=120)[:2]
        for li, ln in enumerate(footer_lines):
            parts.append(
                f'<text x="{W//2}" y="{footer_y + 22 + li * 16}" text-anchor="middle" '
                f'font-family="Georgia,serif" font-size="13" font-style="italic" '
                f'fill="{PAL["gold"]}" opacity="0.9">{escape_xml(ln)}</text>'
            )

    parts.append('</svg>')
    return ''.join(parts)
'''

src = replace_function(src, 'svg_process_flow', NEW_PROCESS)
print('Step C: svg_process_flow replaced')

# ============================================================================
# svg_timeline — fossil icons on timeline with Mya dates
# ============================================================================

NEW_TIMELINE = '''def svg_timeline(node):
    """Horizontal geological timeline with era background bands, Mya dates,
    and fossil icons for each event."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W, H    = 920, 560
    TITLE_H = 70
    axis_y  = H // 2 + 40

    event_xs = [110, 280, 500, 740]
    era_colors = ['#1a0d0d', '#0d1a0d', '#1a160d', '#0d0d1a']
    era_labels = ['PRECAMBRIAN', 'PALEOZOIC', 'MESOZOIC', 'CENOZOIC']
    era_dates  = ['4600-541 Mya', '541-252 Mya', '252-66 Mya', '66-0 Mya']
    era_bounds = [60, 220, 430, 660, 880]

    color_map = {t.get('color', 'gray'): nc.get(t.get('color', 'gray'), PAL['muted'])
                 for t in kt[:4]}
    defs_str, _mids = _arrow_defs(color_map)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:920px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
    ]

    # Title + subtitle
    main_title = node['title'].split(':')[0].strip()
    parts.append(
        f'<text x="{W//2}" y="38" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="26" font-weight="700" '
        f'fill="{PAL["text"]}">{escape_xml(main_title)}</text>'
    )
    subtitle_lines = wrap_text(v2['definition'], max_chars=100)[:1]
    if subtitle_lines:
        parts.append(
            f'<text x="{W//2}" y="62" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="13" font-style="italic" '
            f'fill="{PAL["gold"]}" opacity="0.85">'
            f'{escape_xml(subtitle_lines[0])}</text>'
        )

    # Era bands
    band_y = TITLE_H + 20
    band_h = H - TITLE_H - 60
    for i in range(4):
        x0, x1 = era_bounds[i], era_bounds[i+1]
        parts.append(
            f'<rect x="{x0}" y="{band_y}" width="{x1-x0}" height="{band_h}" '
            f'fill="{era_colors[i]}" opacity="0.8"/>'
            f'<text x="{(x0+x1)//2}" y="{band_y + 18}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="11" font-weight="700" '
            f'letter-spacing="2" fill="{PAL["muted"]}" '
            f'opacity="0.75">{era_labels[i]}</text>'
            f'<text x="{(x0+x1)//2}" y="{band_y + 32}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="9" fill="{PAL["muted"]}" '
            f'opacity="0.6">{era_dates[i]}</text>'
        )
    # Era dividers
    for i in range(1, 4):
        parts.append(
            f'<line x1="{era_bounds[i]}" y1="{band_y}" '
            f'x2="{era_bounds[i]}" y2="{band_y + band_h}" '
            f'stroke="{PAL["border"]}" stroke-width="1" opacity="0.4"/>'
        )

    # Main axis
    parts.append(
        f'<line x1="60" y1="{axis_y}" x2="880" y2="{axis_y}" '
        f'stroke="{PAL["muted"]}" stroke-width="3"/>'
        f'<polygon points="880,{axis_y} 868,{axis_y-6} 868,{axis_y+6}" '
        f'fill="{PAL["muted"]}"/>'
        f'<text x="50" y="{axis_y + 5}" text-anchor="end" '
        f'font-family="Georgia,serif" font-size="10" letter-spacing="1" '
        f'fill="{PAL["muted"]}">PAST</text>'
        f'<text x="886" y="{axis_y + 5}" '
        f'font-family="Georgia,serif" font-size="10" letter-spacing="1" '
        f'fill="{PAL["muted"]}">NOW</text>'
    )

    # Events with icons
    for i, t in enumerate(kt[:4]):
        ex = event_xs[i]
        color = nc.get(t.get('color', 'gray'), PAL['muted'])
        ckey  = t.get('color', 'gray')
        icon_key = _pick_bio_icon(ckey, t['term'])
        above = (i % 2 == 0)

        # Event circle on axis
        parts.append(
            f'<circle cx="{ex}" cy="{axis_y}" r="11" '
            f'fill="{PAL["bg"]}" stroke="{color}" stroke-width="3"/>'
            f'<circle cx="{ex}" cy="{axis_y}" r="4" fill="{color}"/>'
        )

        # Dashed connector
        conn_len = 95
        if above:
            ly1, ly2 = axis_y - 14, axis_y - conn_len
        else:
            ly1, ly2 = axis_y + 14, axis_y + conn_len
        parts.append(
            f'<line x1="{ex}" y1="{ly1}" x2="{ex}" y2="{ly2}" '
            f'stroke="{color}" stroke-width="1.5" stroke-dasharray="3 3" opacity="0.7"/>'
        )

        # Event card with icon
        card_w = 172
        card_h = 110
        cx = ex - card_w // 2
        if above:
            cy_card = ly2 - card_h
        else:
            cy_card = ly2
        parts.append(
            f'<rect x="{cx}" y="{cy_card}" width="{card_w}" height="{card_h}" '
            f'fill="{PAL["bg"]}" stroke="{color}" stroke-width="2" rx="10"/>'
            f'<rect x="{cx}" y="{cy_card}" width="{card_w}" height="4" '
            f'fill="{color}" rx="2"/>'
        )
        # Big icon in circle at the top of the card
        parts.append(
            f'<circle cx="{ex}" cy="{cy_card + 32}" r="20" '
            f'fill="{color}" fill-opacity="0.12" stroke="{color}" stroke-width="1.5"/>'
        )
        parts.append(_bio_icon(icon_key, ex, cy_card + 32, 13, color,
                               stroke_width=2, fill_mode='stroke'))
        # Term name
        term_lines = wrap_text(t['term'], max_chars=18)[:2]
        tbase = cy_card + 66
        for li, ln in enumerate(term_lines):
            parts.append(
                f'<text x="{ex}" y="{tbase + li * 15}" text-anchor="middle" '
                f'font-family="Georgia,serif" font-size="13" font-weight="700" '
                f'fill="{PAL["text"]}">{escape_xml(ln)}</text>'
            )
        # Short def
        def_lines = wrap_text(t['def'], max_chars=22)[:2]
        def_base = tbase + len(term_lines) * 15 + 4
        for li, ln in enumerate(def_lines):
            parts.append(
                f'<text x="{ex}" y="{def_base + li * 12}" text-anchor="middle" '
                f'font-family="Georgia,serif" font-size="10" '
                f'fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
            )

    parts.append('</svg>')
    return ''.join(parts)
'''

src = replace_function(src, 'svg_timeline', NEW_TIMELINE)
print('Step D: svg_timeline replaced')

# ============================================================================
# svg_stages — vertical progression with icons
# ============================================================================

NEW_STAGES = '''def svg_stages(node):
    """Vertical 4-stage progression. Each stage: big icon tile on the left,
    numbered badge, term + definition on the right, arrow connector between stages."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W = 900
    PAD = 22
    TITLE_H = 70
    STAGE_H = 110
    GAP = 26

    n_stages = min(len(kt), 4)
    H = TITLE_H + STAGE_H * n_stages + GAP * (n_stages - 1) + PAD + 10

    color_map = {t.get('color', 'gray'): nc.get(t.get('color', 'gray'), PAL['muted'])
                 for t in kt[:n_stages]}
    defs_str, marker_ids = _arrow_defs(color_map)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:900px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
    ]

    # Title + subtitle
    main_title = node['title'].split(':')[0].strip()
    parts.append(
        f'<text x="{W//2}" y="38" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="26" font-weight="700" '
        f'fill="{PAL["text"]}">{escape_xml(main_title)}</text>'
    )
    subtitle_lines = wrap_text(v2['definition'], max_chars=100)[:1]
    if subtitle_lines:
        parts.append(
            f'<text x="{W//2}" y="62" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="13" font-style="italic" '
            f'fill="{PAL["gold"]}" opacity="0.85">'
            f'{escape_xml(subtitle_lines[0])}</text>'
        )

    cy = TITLE_H + 16
    for i, t in enumerate(kt[:n_stages]):
        color = nc.get(t.get('color', 'gray'), PAL['muted'])
        ckey  = t.get('color', 'gray')
        icon_key = _pick_bio_icon(ckey, t['term'])

        # Row card
        parts.append(
            f'<rect x="{PAD}" y="{cy}" width="{W - PAD*2}" height="{STAGE_H}" '
            f'fill="{PAL["bg"]}" stroke="{color}" stroke-width="2" rx="12"/>'
            f'<rect x="{PAD}" y="{cy}" width="8" height="{STAGE_H}" '
            f'fill="{color}" rx="4"/>'
        )
        # Large icon tile on the left
        tile_cx = PAD + 60
        tile_cy = cy + STAGE_H // 2
        parts.append(
            f'<circle cx="{tile_cx}" cy="{tile_cy}" r="38" '
            f'fill="{color}" fill-opacity="0.12" stroke="{color}" '
            f'stroke-width="2"/>'
        )
        parts.append(_bio_icon(icon_key, tile_cx, tile_cy, 24, color,
                               stroke_width=2.2, fill_mode='stroke'))
        # Stage number badge on top-left of tile
        parts.append(
            f'<circle cx="{tile_cx - 32}" cy="{tile_cy - 32}" r="15" '
            f'fill="{PAL["gold"]}" stroke="{PAL["panel"]}" stroke-width="2"/>'
            f'<text x="{tile_cx - 32}" y="{tile_cy - 27}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="14" font-weight="700" '
            f'fill="{PAL["bg"]}">{i+1}</text>'
        )
        # Term name (big)
        content_x = tile_cx + 54
        parts.append(
            f'<text x="{content_x}" y="{cy + 36}" '
            f'font-family="Georgia,serif" font-size="19" font-weight="700" '
            f'fill="{PAL["text"]}">{escape_xml(t["term"])}</text>'
        )
        # Underline
        parts.append(
            f'<line x1="{content_x}" y1="{cy + 42}" x2="{content_x + 80}" y2="{cy + 42}" '
            f'stroke="{color}" stroke-width="2"/>'
        )
        # Definition
        def_lines = wrap_text(t['def'], max_chars=70)[:3]
        for li, ln in enumerate(def_lines):
            parts.append(
                f'<text x="{content_x}" y="{cy + 62 + li * 16}" '
                f'font-family="Georgia,serif" font-size="13" '
                f'fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
            )

        # Arrow to next stage
        if i < n_stages - 1:
            arrow_x = W // 2
            ay1 = cy + STAGE_H + 4
            ay2 = cy + STAGE_H + GAP - 4
            mid = marker_ids.get(ckey, list(marker_ids.values())[0])
            parts.append(
                f'<line x1="{arrow_x}" y1="{ay1}" x2="{arrow_x}" y2="{ay2}" '
                f'stroke="{color}" stroke-width="3" marker-end="url(#{mid})"/>'
            )

        cy += STAGE_H + GAP

    parts.append('</svg>')
    return ''.join(parts)
'''

src = replace_function(src, 'svg_stages', NEW_STAGES)
print('Step E: svg_stages replaced')

# ============================================================================
# svg_comparison — side-by-side X vs Y with topped icons
# ============================================================================

NEW_COMPARISON = '''def svg_comparison(node):
    """Two-column comparison with big topping icon per column, column headings,
    and stacked term cards below. Center 'vs' divider."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W = 900
    PAD = 22
    TITLE_H = 70
    HEAD_H = 110  # tall header to fit big icons
    GUTTER_W = 28
    COL_W = (W - PAD * 2 - GUTTER_W) // 2

    left_terms  = [kt[0], kt[2]] if len(kt) >= 3 else kt[:2]
    right_terms = [kt[1], kt[3]] if len(kt) >= 4 else kt[1:3]

    def card_h(t):
        dl = wrap_text(t['def'], max_chars=44)
        return 42 + min(len(dl), 5) * 15 + 16

    left_h  = sum(card_h(t) for t in left_terms) + 14
    right_h = sum(card_h(t) for t in right_terms) + 14
    body_h  = max(left_h, right_h)
    H = TITLE_H + HEAD_H + 12 + body_h + PAD

    defs_str, _ids = _arrow_defs(nc)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:900px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
    ]

    # Title + subtitle
    main_title = node['title'].split(':')[0].strip()
    parts.append(
        f'<text x="{W//2}" y="38" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="26" font-weight="700" '
        f'fill="{PAL["text"]}">{escape_xml(main_title)}</text>'
    )
    subtitle_lines = wrap_text(v2['definition'], max_chars=100)[:1]
    if subtitle_lines:
        parts.append(
            f'<text x="{W//2}" y="62" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="13" font-style="italic" '
            f'fill="{PAL["gold"]}" opacity="0.85">'
            f'{escape_xml(subtitle_lines[0])}</text>'
        )

    left_term_main  = left_terms[0]
    right_term_main = right_terms[0] if right_terms else kt[1]
    left_color  = nc.get(left_term_main.get('color', 'teal'),  PAL['teal'])
    right_color = nc.get(right_term_main.get('color', 'coral'), PAL['coral'])

    left_icon  = _pick_bio_icon(left_term_main.get('color', 'teal'),  left_term_main['term'])
    right_icon = _pick_bio_icon(right_term_main.get('color', 'coral'), right_term_main['term'])

    # Column headings with big icons
    head_y = TITLE_H + 12
    # LEFT header
    parts.append(
        f'<rect x="{PAD}" y="{head_y}" width="{COL_W}" height="{HEAD_H}" '
        f'fill="{left_color}" opacity="0.12" rx="10"/>'
        f'<circle cx="{PAD + COL_W // 2}" cy="{head_y + 40}" r="32" '
        f'fill="{left_color}" fill-opacity="0.18" stroke="{left_color}" stroke-width="2"/>'
    )
    parts.append(_bio_icon(left_icon, PAD + COL_W // 2, head_y + 40, 22, left_color,
                           stroke_width=2.4, fill_mode='stroke'))
    parts.append(
        f'<text x="{PAD + COL_W // 2}" y="{head_y + 90}" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="17" font-weight="700" '
        f'letter-spacing="1" fill="{left_color}">'
        f'{escape_xml(left_term_main["term"].upper())}</text>'
    )

    # RIGHT header
    rx = PAD + COL_W + GUTTER_W
    parts.append(
        f'<rect x="{rx}" y="{head_y}" width="{COL_W}" height="{HEAD_H}" '
        f'fill="{right_color}" opacity="0.12" rx="10"/>'
        f'<circle cx="{rx + COL_W // 2}" cy="{head_y + 40}" r="32" '
        f'fill="{right_color}" fill-opacity="0.18" stroke="{right_color}" stroke-width="2"/>'
    )
    parts.append(_bio_icon(right_icon, rx + COL_W // 2, head_y + 40, 22, right_color,
                           stroke_width=2.4, fill_mode='stroke'))
    parts.append(
        f'<text x="{rx + COL_W // 2}" y="{head_y + 90}" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="17" font-weight="700" '
        f'letter-spacing="1" fill="{right_color}">'
        f'{escape_xml(right_term_main["term"].upper())}</text>'
    )

    # "vs" divider in the gutter
    div_x = PAD + COL_W + GUTTER_W // 2
    parts.append(
        f'<line x1="{div_x}" y1="{head_y + 10}" x2="{div_x}" y2="{H - PAD}" '
        f'stroke="{PAL["border"]}" stroke-width="1" stroke-dasharray="3 5" opacity="0.5"/>'
        f'<circle cx="{div_x}" cy="{head_y + HEAD_H // 2}" r="18" '
        f'fill="{PAL["panel"]}" stroke="{PAL["gold"]}" stroke-width="2.5"/>'
        f'<text x="{div_x}" y="{head_y + HEAD_H // 2 + 6}" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="16" font-weight="700" '
        f'font-style="italic" fill="{PAL["gold"]}">vs</text>'
    )

    # Body cards
    body_y = head_y + HEAD_H + 14

    def render_column(col_x, terms):
        local = []
        cy2 = body_y
        for t in terms:
            color = nc.get(t.get('color', 'gray'), PAL['muted'])
            ckey  = t.get('color', 'gray')
            icon_key = _pick_bio_icon(ckey, t['term'])
            ch = card_h(t)
            local.append(
                f'<rect x="{col_x}" y="{cy2}" width="{COL_W}" height="{ch}" '
                f'fill="{PAL["bg"]}" stroke="{color}" stroke-width="1.5" rx="8"/>'
                f'<rect x="{col_x}" y="{cy2}" width="5" height="{ch}" '
                f'fill="{color}" rx="2"/>'
            )
            # Small icon + term name row
            local.append(
                f'<circle cx="{col_x + 28}" cy="{cy2 + 22}" r="14" '
                f'fill="{color}" fill-opacity="0.15" stroke="{color}" stroke-width="1.5"/>'
            )
            local.append(_bio_icon(icon_key, col_x + 28, cy2 + 22, 9, color,
                                   stroke_width=1.8, fill_mode='stroke'))
            local.append(
                f'<text x="{col_x + 50}" y="{cy2 + 27}" '
                f'font-family="Georgia,serif" font-size="14" font-weight="700" '
                f'fill="{PAL["text"]}">{escape_xml(t["term"])}</text>'
            )
            # Definition
            def_lines = wrap_text(t['def'], max_chars=44)[:5]
            for li, ln in enumerate(def_lines):
                local.append(
                    f'<text x="{col_x + 16}" y="{cy2 + 50 + li * 15}" '
                    f'font-family="Georgia,serif" font-size="12" '
                    f'fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
                )
            cy2 += ch + 8
        return local

    parts.extend(render_column(PAD, left_terms))
    parts.extend(render_column(rx,  right_terms))

    parts.append('</svg>')
    return ''.join(parts)
'''

src = replace_function(src, 'svg_comparison', NEW_COMPARISON)
print('Step F: svg_comparison replaced')

# ============================================================================
# svg_balance — weighted pans with icons + large title
# ============================================================================

NEW_BALANCE = '''def svg_balance(node):
    """Trade-off balance scale with two weighted pans (costs vs benefits),
    icons inside each pan, central fulcrum, and term details below."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W, H = 900, 620
    PAD = 22
    TITLE_H = 70
    cx = W // 2
    beam_y = 170
    pan_y = beam_y + 18
    pan_w = 260
    pan_h = 110

    left_terms  = kt[:2]
    right_terms = kt[2:4] if len(kt) >= 4 else kt[2:3]

    left_main  = left_terms[0]
    right_main = right_terms[0] if right_terms else kt[0]
    left_color  = nc.get(left_main.get('color', 'coral'),  PAL['coral'])
    right_color = nc.get(right_main.get('color', 'teal'),  PAL['teal'])

    left_icon  = _pick_bio_icon(left_main.get('color', 'coral'),  left_main['term'])
    right_icon = _pick_bio_icon(right_main.get('color', 'teal'),  right_main['term'])

    defs_str, _ids = _arrow_defs(nc)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:900px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
    ]

    # Title + subtitle
    main_title = node['title'].split(':')[0].strip()
    parts.append(
        f'<text x="{cx}" y="38" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="26" font-weight="700" '
        f'fill="{PAL["text"]}">{escape_xml(main_title)}</text>'
    )
    subtitle_lines = wrap_text(v2['definition'], max_chars=100)[:1]
    if subtitle_lines:
        parts.append(
            f'<text x="{cx}" y="62" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="13" font-style="italic" '
            f'fill="{PAL["gold"]}" opacity="0.85">'
            f'{escape_xml(subtitle_lines[0])}</text>'
        )

    # TRADE-OFF label
    parts.append(
        f'<text x="{cx}" y="{TITLE_H + 18}" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="12" font-weight="700" '
        f'letter-spacing="3" fill="{PAL["gold"]}" opacity="0.75">'
        f'? TRADE-OFF ?</text>'
    )

    # Beam
    beam_x1 = cx - 330
    beam_x2 = cx + 330
    parts.append(
        f'<line x1="{beam_x1}" y1="{beam_y}" x2="{beam_x2}" y2="{beam_y}" '
        f'stroke="{PAL["gold"]}" stroke-width="5" stroke-linecap="round"/>'
    )
    # Fulcrum
    fulcrum_y = beam_y + 150
    parts.append(
        f'<polygon points="{cx-24},{fulcrum_y} {cx+24},{fulcrum_y} {cx},{beam_y+4}" '
        f'fill="{PAL["gold"]}" opacity="0.9"/>'
        f'<rect x="{cx-44}" y="{fulcrum_y}" width="88" height="16" '
        f'fill="{PAL["border"]}" stroke="{PAL["gold"]}" stroke-width="2" rx="4"/>'
    )
    # Chains from beam to pans
    left_pan_cx = cx - 200
    right_pan_cx = cx + 200
    for pan_cx in (left_pan_cx, right_pan_cx):
        parts.append(
            f'<line x1="{pan_cx}" y1="{beam_y}" x2="{pan_cx - 70}" y2="{pan_y}" '
            f'stroke="{PAL["muted"]}" stroke-width="1.5" stroke-dasharray="2 3"/>'
            f'<line x1="{pan_cx}" y1="{beam_y}" x2="{pan_cx + 70}" y2="{pan_y}" '
            f'stroke="{PAL["muted"]}" stroke-width="1.5" stroke-dasharray="2 3"/>'
        )

    # Pans with icons
    def render_pan(pcx, color, side_label, terms, icon_key):
        local = []
        px = pcx - pan_w // 2
        local.append(
            f'<rect x="{px}" y="{pan_y}" width="{pan_w}" height="{pan_h}" '
            f'fill="{PAL["bg"]}" stroke="{color}" stroke-width="2.5" rx="12"/>'
            f'<rect x="{px}" y="{pan_y}" width="{pan_w}" height="26" '
            f'fill="{color}" opacity="0.2" rx="12"/>'
        )
        local.append(
            f'<text x="{pcx}" y="{pan_y + 18}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="12" font-weight="700" '
            f'letter-spacing="2" fill="{color}">'
            f'{escape_xml(side_label.upper())}</text>'
        )
        # Big icon in pan
        local.append(
            f'<circle cx="{pcx}" cy="{pan_y + 64}" r="28" '
            f'fill="{color}" fill-opacity="0.15" stroke="{color}" stroke-width="2"/>'
        )
        local.append(_bio_icon(icon_key, pcx, pan_y + 64, 19, color,
                               stroke_width=2.2, fill_mode='stroke'))
        return local

    parts.extend(render_pan(left_pan_cx,  left_color,  'COSTS / SIDE A',   left_terms, left_icon))
    parts.extend(render_pan(right_pan_cx, right_color, 'BENEFITS / SIDE B', right_terms, right_icon))

    # Term details below the scale
    detail_y = fulcrum_y + 50
    detail_card_w = (W - PAD * 3) // 2
    detail_card_h = 190

    def render_detail_column(col_x, terms, color_default, hdr_color):
        local = []
        local.append(
            f'<rect x="{col_x}" y="{detail_y}" width="{detail_card_w}" '
            f'height="{detail_card_h}" '
            f'fill="{PAL["bg"]}" stroke="{hdr_color}" stroke-width="1.5" rx="10"/>'
        )
        cy2 = detail_y + 16
        for t in terms[:2]:
            color = nc.get(t.get('color', 'gray'), color_default)
            ckey  = t.get('color', 'gray')
            icon_key = _pick_bio_icon(ckey, t['term'])
            # Icon
            local.append(
                f'<circle cx="{col_x + 26}" cy="{cy2 + 18}" r="13" '
                f'fill="{color}" fill-opacity="0.15" stroke="{color}" stroke-width="1.5"/>'
            )
            local.append(_bio_icon(icon_key, col_x + 26, cy2 + 18, 9, color,
                                   stroke_width=1.8, fill_mode='stroke'))
            # Term
            local.append(
                f'<text x="{col_x + 48}" y="{cy2 + 22}" '
                f'font-family="Georgia,serif" font-size="14" font-weight="700" '
                f'fill="{PAL["text"]}">{escape_xml(t["term"])}</text>'
            )
            def_lines = wrap_text(t['def'], max_chars=46)[:3]
            for li, ln in enumerate(def_lines):
                local.append(
                    f'<text x="{col_x + 48}" y="{cy2 + 40 + li * 13}" '
                    f'font-family="Georgia,serif" font-size="11" '
                    f'fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
                )
            cy2 += 86
        return local

    parts.extend(render_detail_column(PAD, left_terms, left_color, left_color))
    parts.extend(render_detail_column(PAD*2 + detail_card_w, right_terms, right_color, right_color))

    parts.append('</svg>')
    return ''.join(parts)
'''

src = replace_function(src, 'svg_balance', NEW_BALANCE)
print('Step G: svg_balance replaced')

# ============================================================================
# svg_network — hub + satellites with icons and labels
# ============================================================================

NEW_NETWORK = '''def svg_network(node):
    """Central hub with 4 satellite nodes. Each satellite has a big icon,
    term label, short definition. Directed edges radiate from hub."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W, H = 900, 620
    TITLE_H = 70
    cx, cy = W // 2, H // 2 + 28
    R = 195
    sat_r = 70
    hub_r = 60

    color_map = {t.get('color', 'gray'): nc.get(t.get('color', 'gray'), PAL['muted'])
                 for t in kt[:4]}
    defs_str, marker_ids = _arrow_defs(color_map)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:900px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
    ]

    # Title + subtitle
    main_title = node['title'].split(':')[0].strip()
    parts.append(
        f'<text x="{W//2}" y="38" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="26" font-weight="700" '
        f'fill="{PAL["text"]}">{escape_xml(main_title)}</text>'
    )
    subtitle_lines = wrap_text(v2['definition'], max_chars=100)[:1]
    if subtitle_lines:
        parts.append(
            f'<text x="{W//2}" y="62" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="13" font-style="italic" '
            f'fill="{PAL["gold"]}" opacity="0.85">'
            f'{escape_xml(subtitle_lines[0])}</text>'
        )

    import math as _m
    n_sat = min(len(kt), 4)
    angles = [-_m.pi / 2, 0, _m.pi / 2, _m.pi]
    sat_positions = []
    for i in range(n_sat):
        sx = cx + R * _m.cos(angles[i])
        sy = cy + R * _m.sin(angles[i])
        sat_positions.append((sx, sy))

    # Edges
    for i, (sx, sy) in enumerate(sat_positions):
        t = kt[i]
        color = nc.get(t.get('color', 'gray'), PAL['muted'])
        ckey  = t.get('color', 'gray')
        mid   = marker_ids.get(ckey, list(marker_ids.values())[0])
        dx = sx - cx
        dy = sy - cy
        length = (dx*dx + dy*dy) ** 0.5
        ux, uy = dx / length, dy / length
        x1 = cx + ux * (hub_r + 6)
        y1 = cy + uy * (hub_r + 6)
        x2 = sx - ux * (sat_r + 10)
        y2 = sy - uy * (sat_r + 10)
        parts.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{color}" stroke-width="3" marker-end="url(#{mid})" opacity="0.8"/>'
        )

    # Hub
    parts.append(
        f'<circle cx="{cx}" cy="{cy}" r="{hub_r}" fill="{PAL["bg"]}" '
        f'stroke="{PAL["gold"]}" stroke-width="3.5"/>'
        f'<circle cx="{cx}" cy="{cy}" r="{hub_r-8}" fill="none" '
        f'stroke="{PAL["gold"]}" stroke-width="1" opacity="0.4"/>'
    )
    hub_label = main_title
    hub_lines = wrap_text(hub_label, max_chars=14)[:2]
    base = cy - (len(hub_lines) - 1) * 9 + 5
    for li, ln in enumerate(hub_lines):
        parts.append(
            f'<text x="{cx}" y="{base + li * 16}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="14" font-weight="700" '
            f'fill="{PAL["gold"]}">{escape_xml(ln)}</text>'
        )

    # Satellites with icons
    for i, (sx, sy) in enumerate(sat_positions):
        t = kt[i]
        color = nc.get(t.get('color', 'gray'), PAL['muted'])
        ckey  = t.get('color', 'gray')
        icon_key = _pick_bio_icon(ckey, t['term'])
        sx, sy = int(sx), int(sy)
        parts.append(
            f'<circle cx="{sx}" cy="{sy}" r="{sat_r}" fill="{PAL["bg"]}" '
            f'stroke="{color}" stroke-width="3"/>'
            f'<circle cx="{sx}" cy="{sy}" r="{sat_r}" fill="{color}" opacity="0.10"/>'
        )
        # Big icon at the top of the satellite
        parts.append(_bio_icon(icon_key, sx, sy - 28, 18, color,
                               stroke_width=2.2, fill_mode='stroke'))
        term_lines = wrap_text(t['term'], max_chars=14)[:2]
        tbase = sy + 4
        for li, ln in enumerate(term_lines):
            parts.append(
                f'<text x="{sx}" y="{tbase + li * 14}" text-anchor="middle" '
                f'font-family="Georgia,serif" font-size="12" font-weight="700" '
                f'fill="{PAL["text"]}">{escape_xml(ln)}</text>'
            )
        def_lines = wrap_text(t['def'], max_chars=16)[:2]
        dbase = sy + 28 + (len(term_lines) - 1) * 14
        for li, ln in enumerate(def_lines):
            parts.append(
                f'<text x="{sx}" y="{dbase + li * 11}" text-anchor="middle" '
                f'font-family="Georgia,serif" font-size="9" '
                f'fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
            )

    parts.append('</svg>')
    return ''.join(parts)
'''

src = replace_function(src, 'svg_network', NEW_NETWORK)
print('Step H: svg_network replaced')

# ============================================================================
# svg_landscape — mountain curve with organism positions
# ============================================================================

NEW_LANDSCAPE = '''def svg_landscape(node):
    """Fitness landscape: sinusoidal terrain with peaks/valleys, icons
    positioned at their local fitness, with term cards below."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W, H = 900, 580
    PAD = 22
    TITLE_H = 70
    AXIS_X1 = 80
    AXIS_X2 = W - 60
    CURVE_BOTTOM = 340

    defs_str, _ids = _arrow_defs(nc)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:900px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
    ]

    # Title + subtitle
    main_title = node['title'].split(':')[0].strip()
    parts.append(
        f'<text x="{W//2}" y="38" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="26" font-weight="700" '
        f'fill="{PAL["text"]}">{escape_xml(main_title)}</text>'
    )
    subtitle_lines = wrap_text(v2['definition'], max_chars=100)[:1]
    if subtitle_lines:
        parts.append(
            f'<text x="{W//2}" y="62" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="13" font-style="italic" '
            f'fill="{PAL["gold"]}" opacity="0.85">'
            f'{escape_xml(subtitle_lines[0])}</text>'
        )

    # Y-axis
    parts.append(
        f'<line x1="{AXIS_X1}" y1="{TITLE_H + 20}" x2="{AXIS_X1}" y2="{CURVE_BOTTOM}" '
        f'stroke="{PAL["muted"]}" stroke-width="1.5"/>'
        f'<text x="{AXIS_X1 - 10}" y="{TITLE_H + 34}" text-anchor="end" '
        f'font-family="Georgia,serif" font-size="12" font-weight="700" '
        f'fill="{PAL["muted"]}">FITNESS</text>'
        f'<text x="{AXIS_X1 - 10}" y="{TITLE_H + 50}" text-anchor="end" '
        f'font-family="Georgia,serif" font-size="10" '
        f'fill="{PAL["muted"]}">(high)</text>'
        f'<text x="{AXIS_X1 - 10}" y="{CURVE_BOTTOM - 4}" text-anchor="end" '
        f'font-family="Georgia,serif" font-size="10" '
        f'fill="{PAL["muted"]}">(low)</text>'
    )
    # X-axis
    parts.append(
        f'<line x1="{AXIS_X1}" y1="{CURVE_BOTTOM}" x2="{AXIS_X2}" y2="{CURVE_BOTTOM}" '
        f'stroke="{PAL["muted"]}" stroke-width="1.5"/>'
        f'<polygon points="{AXIS_X2},{CURVE_BOTTOM} {AXIS_X2-10},{CURVE_BOTTOM-5} {AXIS_X2-10},{CURVE_BOTTOM+5}" '
        f'fill="{PAL["muted"]}"/>'
        f'<text x="{(AXIS_X1+AXIS_X2)//2}" y="{CURVE_BOTTOM + 24}" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="12" font-weight="700" '
        f'fill="{PAL["muted"]}">GENOTYPE / TRAIT SPACE ?</text>'
    )

    # Curve
    import math as _m
    points = []
    span = AXIS_X2 - AXIS_X1
    for px in range(0, span + 1, 5):
        x = AXIS_X1 + px
        u = px / span
        y_norm = (_m.sin(u * _m.pi * 2) + 1) / 2
        y_norm = y_norm * (0.85 + 0.3 * u)
        y = CURVE_BOTTOM - 12 - y_norm * 210
        points.append((x, y))

    poly = ' '.join(f'{p[0]},{p[1]:.1f}' for p in points)
    parts.append(
        f'<polygon points="{AXIS_X1},{CURVE_BOTTOM} {poly} {AXIS_X2-10},{CURVE_BOTTOM}" '
        f'fill="{PAL["teal"]}" opacity="0.12"/>'
        f'<polyline points="{poly}" fill="none" stroke="{PAL["teal"]}" stroke-width="3"/>'
    )

    # Icons positioned at key points
    peaks = []
    valleys = []
    for i in range(1, len(points) - 1):
        if points[i][1] < points[i-1][1] and points[i][1] < points[i+1][1]:
            peaks.append(points[i])
        elif points[i][1] > points[i-1][1] and points[i][1] > points[i+1][1]:
            valleys.append(points[i])

    # Peak / valley annotations
    if len(peaks) >= 2:
        parts.append(
            f'<text x="{peaks[0][0]}" y="{peaks[0][1] - 12}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="12" font-style="italic" '
            f'fill="{PAL["gold"]}">adaptive peak</text>'
        )
        parts.append(
            f'<text x="{peaks[-1][0]}" y="{peaks[-1][1] - 12}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="12" font-style="italic" '
            f'fill="{PAL["gold"]}">adaptive peak</text>'
        )
    if valleys:
        parts.append(
            f'<text x="{valleys[0][0]}" y="{valleys[0][1] + 20}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="12" font-style="italic" '
            f'fill="{PAL["muted"]}">fitness valley</text>'
        )

    # Term cards below the landscape
    card_y = CURVE_BOTTOM + 50
    card_w = (W - PAD * 5) // 4
    card_h = 130
    for i, t in enumerate(kt[:4]):
        color = nc.get(t.get('color', 'gray'), PAL['muted'])
        ckey  = t.get('color', 'gray')
        icon_key = _pick_bio_icon(ckey, t['term'])
        cx2 = PAD + i * (card_w + PAD) + card_w // 2
        card_x = cx2 - card_w // 2
        parts.append(
            f'<rect x="{card_x}" y="{card_y}" width="{card_w}" height="{card_h}" '
            f'fill="{PAL["bg"]}" stroke="{color}" stroke-width="1.5" rx="8"/>'
            f'<rect x="{card_x}" y="{card_y}" width="{card_w}" height="4" '
            f'fill="{color}" rx="2"/>'
        )
        # Icon
        parts.append(
            f'<circle cx="{cx2}" cy="{card_y + 30}" r="18" '
            f'fill="{color}" fill-opacity="0.15" stroke="{color}" stroke-width="1.5"/>'
        )
        parts.append(_bio_icon(icon_key, cx2, card_y + 30, 12, color,
                               stroke_width=2, fill_mode='stroke'))
        # Term
        term_lines = wrap_text(t['term'], max_chars=16)[:2]
        tbase = card_y + 64
        for li, ln in enumerate(term_lines):
            parts.append(
                f'<text x="{cx2}" y="{tbase + li * 14}" text-anchor="middle" '
                f'font-family="Georgia,serif" font-size="12" font-weight="700" '
                f'fill="{PAL["text"]}">{escape_xml(ln)}</text>'
            )
        # Def
        def_lines = wrap_text(t['def'], max_chars=18)[:3]
        def_base = tbase + len(term_lines) * 14 + 4
        for li, ln in enumerate(def_lines):
            parts.append(
                f'<text x="{cx2}" y="{def_base + li * 11}" text-anchor="middle" '
                f'font-family="Georgia,serif" font-size="9.5" '
                f'fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
            )

    parts.append('</svg>')
    return ''.join(parts)
'''

src = replace_function(src, 'svg_landscape', NEW_LANDSCAPE)
print('Step I: svg_landscape replaced')

# ============================================================================
# svg_hierarchy — keep existing (used for species concepts) but improve
# ============================================================================

NEW_HIERARCHY = '''def svg_hierarchy(node):
    """Hierarchical tree: trunk + 4 child boxes with arrowheads, icons, and
    short definitions. Used for taxonomic/classification concepts."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W = 900
    KID_W = 200
    KID_H = 140
    PAD = 22
    TITLE_H = 70
    TRUNK_H = 50
    BEAM_H = 40
    H = TITLE_H + 20 + TRUNK_H + BEAM_H + KID_H + PAD + 20

    color_map = {t.get('color', 'gray'): nc.get(t.get('color', 'gray'), PAL['muted'])
                 for t in kt[:4]}
    defs_str, marker_ids = _arrow_defs(color_map)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:900px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
    ]

    # Title + subtitle
    main_title = node['title'].split(':')[0].strip()
    parts.append(
        f'<text x="{W//2}" y="38" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="26" font-weight="700" '
        f'fill="{PAL["text"]}">{escape_xml(main_title)}</text>'
    )
    subtitle_lines = wrap_text(v2['definition'], max_chars=100)[:1]
    if subtitle_lines:
        parts.append(
            f'<text x="{W//2}" y="62" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="13" font-style="italic" '
            f'fill="{PAL["gold"]}" opacity="0.85">'
            f'{escape_xml(subtitle_lines[0])}</text>'
        )

    # Root (hub box)
    root_cx = W // 2
    root_y = TITLE_H + 20
    root_w = 280
    root_h = TRUNK_H
    parts.append(
        f'<rect x="{root_cx - root_w//2}" y="{root_y}" width="{root_w}" height="{root_h}" '
        f'fill="{PAL["bg"]}" stroke="{PAL["gold"]}" stroke-width="2.5" rx="10"/>'
        f'<text x="{root_cx}" y="{root_y + root_h//2 + 5}" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="15" font-weight="700" '
        f'fill="{PAL["gold"]}">{escape_xml(main_title)}</text>'
    )

    # Beam line from root
    beam_y = root_y + root_h + BEAM_H
    trunk_y = root_y + root_h
    parts.append(
        f'<line x1="{root_cx}" y1="{trunk_y}" x2="{root_cx}" y2="{beam_y - 20}" '
        f'stroke="{PAL["muted"]}" stroke-width="2"/>'
    )

    # Child positions
    total_w = KID_W * 4 + PAD * 3
    start_x = (W - total_w) // 2
    beam_left = start_x + KID_W // 2
    beam_right = start_x + 4 * KID_W + 3 * PAD - KID_W // 2
    # Horizontal beam
    parts.append(
        f'<line x1="{beam_left}" y1="{beam_y - 20}" x2="{beam_right}" y2="{beam_y - 20}" '
        f'stroke="{PAL["muted"]}" stroke-width="2"/>'
    )

    for i, t in enumerate(kt[:4]):
        color = nc.get(t.get('color', 'gray'), PAL['muted'])
        ckey  = t.get('color', 'gray')
        icon_key = _pick_bio_icon(ckey, t['term'])
        mid = marker_ids.get(ckey, list(marker_ids.values())[0])

        kx = start_x + i * (KID_W + PAD)
        kcx = kx + KID_W // 2
        ky = beam_y
        # Vertical drop to kid
        parts.append(
            f'<line x1="{kcx}" y1="{beam_y - 20}" x2="{kcx}" y2="{ky - 4}" '
            f'stroke="{color}" stroke-width="2.5" marker-end="url(#{mid})"/>'
        )
        # Kid box
        parts.append(
            f'<rect x="{kx}" y="{ky}" width="{KID_W}" height="{KID_H}" '
            f'fill="{PAL["bg"]}" stroke="{color}" stroke-width="2" rx="10"/>'
            f'<rect x="{kx}" y="{ky}" width="{KID_W}" height="4" fill="{color}" rx="2"/>'
        )
        # Icon at top
        parts.append(
            f'<circle cx="{kcx}" cy="{ky + 32}" r="22" '
            f'fill="{color}" fill-opacity="0.15" stroke="{color}" stroke-width="1.5"/>'
        )
        parts.append(_bio_icon(icon_key, kcx, ky + 32, 15, color,
                               stroke_width=2, fill_mode='stroke'))
        # Term
        term_lines = wrap_text(t['term'], max_chars=20)[:2]
        tbase = ky + 70
        for li, ln in enumerate(term_lines):
            parts.append(
                f'<text x="{kcx}" y="{tbase + li * 15}" text-anchor="middle" '
                f'font-family="Georgia,serif" font-size="13" font-weight="700" '
                f'fill="{PAL["text"]}">{escape_xml(ln)}</text>'
            )
        # Def
        def_lines = wrap_text(t['def'], max_chars=24)[:3]
        def_base = tbase + len(term_lines) * 15 + 4
        for li, ln in enumerate(def_lines):
            parts.append(
                f'<text x="{kcx}" y="{def_base + li * 12}" text-anchor="middle" '
                f'font-family="Georgia,serif" font-size="10" '
                f'fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
            )

    parts.append('</svg>')
    return ''.join(parts)
'''

src = replace_function(src, 'svg_hierarchy', NEW_HIERARCHY)
print('Step J: svg_hierarchy replaced')

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
    print(f'SyntaxError: {e}')
