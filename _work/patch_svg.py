"""Patch enrich_v3.py: replace the three SVG generator functions with
improved versions (arrowheads, auto-height, cycle arrows, colored headers)."""
import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

NEW_SVG = (
'''# -- shared SVG helpers --------------------------------------------------

def _arrow_defs(color_map):
    """<defs> with one arrowhead <marker> per color key. Returns (str, {key:id})."""
    lines = ['<defs>']
    ids = {}
    for key, hex_color in color_map.items():
        mid = f'ah-{key}'
        ids[key] = mid
        lines.append(
            f'<marker id="{mid}" markerWidth="8" markerHeight="6" '
            f'refX="7" refY="3" orient="auto" markerUnits="userSpaceOnUse">'
            f'<polygon points="0 0, 8 3, 0 6" fill="{hex_color}"/>'
            f'</marker>'
        )
    lines.append('</defs>')
    return ''.join(lines), ids


def _icon_shape(color_key, cx, cy, sz, color_hex):
    """Small geometric type-icon:
       teal=mechanism (double-circle), purple=entity (square),
       coral=outcome (right triangle), pink=exception (diamond)."""
    k, s = color_key, sz
    if k == 'teal':
        return (f'<circle cx="{cx}" cy="{cy}" r="{s}" fill="none" '
                f'stroke="{color_hex}" stroke-width="2"/>'
                f'<circle cx="{cx}" cy="{cy}" r="{s//2}" fill="{color_hex}"/>')
    elif k == 'purple':
        return (f'<rect x="{cx-s}" y="{cy-s}" width="{2*s}" height="{2*s}" '
                f'fill="{color_hex}" rx="2"/>')
    elif k == 'coral':
        pts = f'{cx-s},{cy-s} {cx+s},{cy} {cx-s},{cy+s}'
        return f'<polygon points="{pts}" fill="{color_hex}"/>'
    elif k == 'pink':
        pts = f'{cx},{cy-s} {cx+s},{cy} {cx},{cy+s} {cx-s},{cy}'
        return f'<polygon points="{pts}" fill="{color_hex}"/>'
    else:
        return f'<circle cx="{cx}" cy="{cy}" r="{s}" fill="{color_hex}"/>'


# -- four-box layout (2x2 grid, colored header bands + icons) ------------

def svg_four_box(node):
    """2x2 grid. Colored header band with icon + term; full definition below.
    Content-sized rows — no wasted vertical space."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W        = 720
    PAD      = 18
    TITLE_H  = 46
    HEADER_H = 36
    CELL_W   = (W - PAD * 3) // 2   # 333

    def cell_content_h(t):
        dl = wrap_text(t['def'], max_chars=36)
        return HEADER_H + 10 + min(len(dl), 6) * 15 + 16

    cell_heights = [cell_content_h(t) for t in kt[:4]]
    row0_h = max(cell_heights[0], cell_heights[1])
    row1_h = max(cell_heights[2], cell_heights[3])
    H = TITLE_H + PAD + row0_h + PAD + row1_h + PAD

    defs_str, _ids = _arrow_defs({k: v for k, v in nc.items()})

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:720px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
        f'<text x="{W//2}" y="30" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="19" font-weight="700" '
        f'fill="{PAL["gold"]}">{escape_xml(node["title"].split(":")[0].strip())}</text>',
    ]

    positions = [
        (PAD,          TITLE_H + PAD,             row0_h),
        (PAD*2+CELL_W, TITLE_H + PAD,             row0_h),
        (PAD,          TITLE_H + PAD*2 + row0_h,  row1_h),
        (PAD*2+CELL_W, TITLE_H + PAD*2 + row0_h,  row1_h),
    ]

    for i, t in enumerate(kt[:4]):
        x, y, cell_h = positions[i]
        color = nc.get(t.get('color', 'gray'), PAL['muted'])
        ckey  = t.get('color', 'gray')

        parts.append(
            f'<rect x="{x}" y="{y}" width="{CELL_W}" height="{cell_h}" '
            f'fill="{PAL["bg"]}" stroke="{color}" stroke-width="2" rx="8"/>'
        )
        # Header band: translucent fill + solid bottom strip
        parts.append(
            f'<rect x="{x}" y="{y}" width="{CELL_W}" height="{HEADER_H}" '
            f'fill="{color}" opacity="0.18" rx="8"/>'
            f'<rect x="{x}" y="{y+HEADER_H-4}" width="{CELL_W}" height="4" '
            f'fill="{color}" opacity="0.45"/>'
        )
        # Icon in header
        parts.append(_icon_shape(ckey, x + 18, y + HEADER_H // 2, 7, color))

        # Term name in header
        term_lines = wrap_text(t['term'], max_chars=30)[:2]
        term_base  = y + (HEADER_H - (len(term_lines) - 1) * 16) // 2 + 5
        for li, ln in enumerate(term_lines):
            parts.append(
                f'<text x="{x + 34}" y="{term_base + li * 16}" '
                f'font-family="Georgia,serif" font-size="14" font-weight="700" '
                f'fill="{PAL["text"]}">{escape_xml(ln)}</text>'
            )

        # Definition text below header
        def_y = y + HEADER_H + 14
        def_lines = wrap_text(t['def'], max_chars=36)
        for li, ln in enumerate(def_lines[:6]):
            parts.append(
                f'<text x="{x + 14}" y="{def_y + li * 15}" '
                f'font-family="Georgia,serif" font-size="12" '
                f'fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
            )

    # Subtle center divider cross
    mid_x = PAD + CELL_W + PAD // 2
    mid_y = TITLE_H + PAD + row0_h + PAD // 2
    parts.append(
        f'<line x1="{mid_x}" y1="{TITLE_H + PAD//2}" '
        f'x2="{mid_x}" y2="{H - PAD//2}" '
        f'stroke="{PAL["border"]}" stroke-width="1" opacity="0.5"/>'
        f'<line x1="{PAD//2}" y1="{mid_y}" '
        f'x2="{W - PAD//2}" y2="{mid_y}" '
        f'stroke="{PAL["border"]}" stroke-width="1" opacity="0.5"/>'
    )

    parts.append('</svg>')
    return ''.join(parts)


# -- cycle layout (4 circles + curved directional arrows) ----------------

def svg_cycle(node):
    """Circular cycle: circles with term/def + curved bezier arrows showing
    clockwise flow direction between adjacent steps."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W, H   = 760, 530
    cx, cy = W // 2, H // 2 + 20
    R      = 168
    node_r = 74

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
        f'width="100%" style="max-width:760px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
        f'<text x="{cx}" y="30" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="19" font-weight="700" '
        f'fill="{PAL["gold"]}">{escape_xml(node["title"].split(":")[0].strip())}</text>',
        f'<circle cx="{cx}" cy="{cy}" r="{R - 58}" fill="none" '
        f'stroke="{PAL["border"]}" stroke-width="1.5" stroke-dasharray="4 6"/>',
        f'<text x="{cx}" y="{cy + 5}" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="14" font-weight="700" '
        f'fill="{PAL["gold"]}">{escape_xml(node["title"].split(":")[0].strip())}</text>',
    ]

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

        sx = px_i + ux * (node_r + 4)
        sy = py_i + uy * (node_r + 4)
        ex = px_j - ux * (node_r + 16)
        ey = py_j - uy * (node_r + 16)

        mid_mx = (px_i + px_j) / 2
        mid_my = (py_i + py_j) / 2
        omx, omy = mid_mx - cx, mid_my - cy
        omag = math.sqrt(omx*omx + omy*omy) or 1
        ctrl_x = cx + (omx / omag) * (R + 38)
        ctrl_y = cy + (omy / omag) * (R + 38)

        mk = f' marker-end="url(#{mid_i})"' if mid_i else ''
        parts.append(
            f'<path d="M {sx:.1f},{sy:.1f} Q {ctrl_x:.1f},{ctrl_y:.1f} {ex:.1f},{ey:.1f}" '
            f'fill="none" stroke="{color_i}" stroke-width="2" opacity="0.75"{mk}/>'
        )

    # Circles + text (on top of arrows)
    for i, t in enumerate(kt[:4]):
        x, y  = positions[i]
        color = nc.get(t.get('color', 'gray'), PAL['muted'])

        parts.append(
            f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{node_r}" '
            f'fill="{PAL["bg"]}" stroke="{color}" stroke-width="3"/>'
        )

        term_lines = wrap_text(t['term'], max_chars=14)[:2]
        def_lines  = wrap_text(t['def'],  max_chars=18)[:3]

        lh_t, lh_d, gap = 14, 12, 6
        block_h = (len(term_lines) * lh_t
                   + (gap if def_lines else 0)
                   + len(def_lines) * lh_d)
        first_y = y - block_h / 2 + lh_t - 2

        for li, ln in enumerate(term_lines):
            parts.append(
                f'<text x="{x:.0f}" y="{first_y + li * lh_t:.0f}" '
                f'text-anchor="middle" font-family="Georgia,serif" '
                f'font-size="12" font-weight="700" '
                f'fill="{PAL["text"]}">{escape_xml(ln)}</text>'
            )
        def_y0 = first_y + len(term_lines) * lh_t + gap
        for li, ln in enumerate(def_lines):
            parts.append(
                f'<text x="{x:.0f}" y="{def_y0 + li * lh_d:.0f}" '
                f'text-anchor="middle" font-family="Georgia,serif" '
                f'font-size="9.5" fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
            )

    # Step badges on top
    for i in range(n):
        x, y = positions[i]
        parts.append(
            f'<circle cx="{x - node_r + 14:.0f}" cy="{y - node_r + 14:.0f}" '
            f'r="11" fill="{PAL["gold"]}"/>'
            f'<text x="{x - node_r + 14:.0f}" y="{y - node_r + 18:.0f}" '
            f'text-anchor="middle" font-family="Georgia,serif" '
            f'font-size="12" font-weight="700" '
            f'fill="{PAL["bg"]}">{i+1}</text>'
        )

    parts.append('</svg>')
    return ''.join(parts)


# -- hierarchy layout (tree, auto-height boxes, arrowheads) ---------------

def svg_hierarchy(node):
    """Tree: arrowheads on connector lines, auto-height child boxes,
    separator between term and def, small type-icon, fan-out trunk+beam."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W      = 760
    KID_W  = 170
    GAP    = 13
    total_kids_w = 4 * KID_W + 3 * GAP
    start_x      = (W - total_kids_w) // 2

    def _kid_h(t):
        tl = wrap_text(t['term'], max_chars=18)[:2]
        dl = wrap_text(t['def'],  max_chars=22)[:6]
        return 8 + 10 + len(tl) * 17 + 8 + len(dl) * 14 + 16

    child_heights = [_kid_h(t) for t in kt[:4]]
    max_kid_h     = max(child_heights)

    ROOT_W, ROOT_H = 680, 78
    root_x = (W - ROOT_W) // 2
    root_y = 48
    kids_y = root_y + ROOT_H + 48
    H      = kids_y + max_kid_h + 26

    color_map = {t.get('color', 'gray'): nc.get(t.get('color', 'gray'), PAL['muted'])
                 for t in kt[:4]}
    defs_str, marker_ids = _arrow_defs(color_map)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="100%" style="max-width:760px;display:block;margin:0 auto">',
        f'<rect width="{W}" height="{H}" fill="{PAL["panel"]}" rx="14"/>',
        defs_str,
        f'<text x="{W//2}" y="30" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="19" font-weight="700" '
        f'fill="{PAL["gold"]}">{escape_xml(node["title"].split(":")[0].strip())}</text>',
        f'<rect x="{root_x}" y="{root_y}" width="{ROOT_W}" height="{ROOT_H}" '
        f'fill="{PAL["bg"]}" stroke="{PAL["gold"]}" stroke-width="2" rx="8"/>',
    ]

    def_lines = wrap_text(v2['definition'], max_chars=72)[:3]
    lh = 18
    block_h = len(def_lines) * lh
    text_y  = root_y + (ROOT_H - block_h) // 2 + lh - 4
    for li, ln in enumerate(def_lines):
        parts.append(
            f'<text x="{W//2}" y="{text_y + li * lh}" '
            f'text-anchor="middle" font-family="Georgia,serif" '
            f'font-size="13" font-weight="600" '
            f'fill="{PAL["gold"]}">{escape_xml(ln)}</text>'
        )

    # Fan-out trunk + horizontal beam
    hub_y    = root_y + ROOT_H
    beam_y   = kids_y - 18
    left_cx  = start_x + KID_W // 2
    right_cx = start_x + 3 * (KID_W + GAP) + KID_W // 2
    parts.append(
        f'<line x1="{W//2}" y1="{hub_y}" x2="{W//2}" y2="{beam_y}" '
        f'stroke="{PAL["border"]}" stroke-width="1.5" opacity="0.6"/>'
        f'<line x1="{left_cx}" y1="{beam_y}" x2="{right_cx}" y2="{beam_y}" '
        f'stroke="{PAL["border"]}" stroke-width="1.5" opacity="0.6"/>'
    )

    for i, t in enumerate(kt[:4]):
        kx     = start_x + i * (KID_W + GAP)
        kid_cx = kx + KID_W // 2
        color  = nc.get(t.get('color', 'gray'), PAL['muted'])
        ckey   = t.get('color', 'gray')
        mid    = marker_ids.get(ckey)
        kid_h  = child_heights[i]

        # Vertical drop with arrowhead
        mk = f' marker-end="url(#{mid})"' if mid else ''
        parts.append(
            f'<line x1="{kid_cx}" y1="{beam_y}" '
            f'x2="{kid_cx}" y2="{kids_y + 2}"'
            f' stroke="{color}" stroke-width="1.5" opacity="0.8"{mk}/>'
        )
        # Child box (auto-height)
        parts.append(
            f'<rect x="{kx}" y="{kids_y}" width="{KID_W}" height="{kid_h}" '
            f'fill="{PAL["bg"]}" stroke="{color}" stroke-width="2" rx="8"/>'
        )
        # Colored top bar (two rects for rounded-top only effect)
        parts.append(
            f'<rect x="{kx}" y="{kids_y}" width="{KID_W}" height="8" '
            f'fill="{color}" rx="7"/>'
            f'<rect x="{kx}" y="{kids_y+4}" width="{KID_W}" height="4" fill="{color}"/>'
        )
        # Type icon
        parts.append(_icon_shape(ckey, kx + 14, kids_y + 8 + 16, 5, color))

        # Term name
        term_lines = wrap_text(t['term'], max_chars=18)[:2]
        for li, ln in enumerate(term_lines):
            parts.append(
                f'<text x="{kid_cx}" y="{kids_y + 8 + 10 + (li + 1) * 17 - 2}" '
                f'text-anchor="middle" font-family="Georgia,serif" '
                f'font-size="13" font-weight="700" '
                f'fill="{PAL["text"]}">{escape_xml(ln)}</text>'
            )

        # Separator line
        sep_y = kids_y + 8 + 10 + len(term_lines) * 17 + 6
        parts.append(
            f'<line x1="{kx+10}" y1="{sep_y}" x2="{kx+KID_W-10}" y2="{sep_y}" '
            f'stroke="{color}" stroke-width="0.75" opacity="0.4"/>'
        )

        # Definition (up to 6 lines)
        def_y_start = sep_y + 13
        kid_def_lines = wrap_text(t['def'], max_chars=22)[:6]
        for li, ln in enumerate(kid_def_lines):
            parts.append(
                f'<text x="{kid_cx}" y="{def_y_start + li * 14}" '
                f'text-anchor="middle" font-family="Georgia,serif" '
                f'font-size="11" fill="{PAL["muted"]}">{escape_xml(ln)}</text>'
            )

    parts.append('</svg>')
    return ''.join(parts)

'''
)

path = r'C:\Users\johnn\Desktop\evolution-study-guide\_work\enrich_v3.py'
with open(path, 'r', encoding='utf-8') as f:
    src = f.read()

idx_start = src.find('# -- four-box layout (2x2 grid of cards)')
idx_end   = src.find('\n# -- layout picker')
assert idx_start > 0, f'Start marker not found'
assert idx_end   > 0, f'End marker not found'

new_src = src[:idx_start] + NEW_SVG + src[idx_end+1:]

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_src)

print(f'OK: wrote {len(new_src)} bytes (delta {len(new_src)-len(src):+d})')
