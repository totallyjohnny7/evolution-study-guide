"""svg_library_v4.py — Biological icon library + presentation-quality generators.

This module is imported by enrich_v3.py (or replaces its SVG section wholesale).
All icons are 24x24 viewBox path strings, rendered via _bio_icon(key, cx, cy, size, color).

Icon palette (24x24 path 'd' strings):
  feather, wing, leg, foot, hand, egg, skull, dna, eye, cell, bone, bird,
  fish, lizard, leaf, flame, drop, snowflake, star, atom, cross, check

Rule: all paths fit inside [0..24, 0..24] and use a single fill.
"""

# ---- Biological icon paths (24x24) ------------------------------------------
# Each entry is a path 'd' string fitting in the 24x24 viewBox.

BIO_ICONS = {
    # Feather: curved shaft with vanes branching off
    'feather': (
        'M12,2 Q8,6 8,12 Q8,18 11,22 L13,22 Q16,18 16,12 Q16,6 12,2 Z '
        'M12,5 L9,8 M12,8 L8,11 M12,11 L9,14 M12,14 L9,17 M12,17 L10,20'
    ),
    # Wing: broad outlined feathered wing
    'wing': (
        'M2,10 Q6,4 12,6 Q18,4 22,10 Q20,12 14,11 Q14,14 12,15 '
        'Q10,14 10,11 Q4,12 2,10 Z'
    ),
    # Leg/limb: simple leg with knee bend
    'leg': (
        'M9,2 L15,2 L15,8 L13,12 L15,18 L17,22 L13,22 L11,18 L9,12 L9,2 Z'
    ),
    # Foot / paw print (5 toes + heel pad)
    'foot': (
        'M8,4 A2,3 0 1,1 8,5 Z M12,3 A2,3 0 1,1 12,4 Z M16,4 A2,3 0 1,1 16,5 Z '
        'M6,9 A1.5,2 0 1,1 6,10 Z M18,9 A1.5,2 0 1,1 18,10 Z '
        'M12,13 Q7,14 7,18 Q7,22 12,22 Q17,22 17,18 Q17,14 12,13 Z'
    ),
    # Hand (simplified: palm + 4 fingers stub)
    'hand': (
        'M8,8 L10,3 L11,3 L11,10 L12,10 L12,2 L13,2 L13,10 L14,10 L14,3 L15,3 '
        'L15,10 L16,10 L16,5 L17,5 L17,14 Q17,22 13,22 Q7,22 7,16 L7,10 L8,8 Z'
    ),
    # Egg: oval
    'egg': (
        'M12,2 Q5,6 5,14 Q5,22 12,22 Q19,22 19,14 Q19,6 12,2 Z'
    ),
    # Skull: rounded top + jaw + eye sockets
    'skull': (
        'M6,10 Q6,3 12,3 Q18,3 18,10 L18,14 L16,14 L16,17 L14,17 L14,14 '
        'L10,14 L10,17 L8,17 L8,14 L6,14 Z '
        'M8,8 A1.5,1.5 0 1,1 8,9 Z M16,8 A1.5,1.5 0 1,1 16,9 Z'
    ),
    # DNA: double helix (two sine curves + rungs)
    'dna': (
        'M6,2 Q18,6 6,10 Q18,14 6,18 Q18,22 6,22 '
        'M18,2 Q6,6 18,10 Q6,14 18,18 Q6,22 18,22 '
        'M8,4 L16,4 M7,8 L17,8 M7,12 L17,12 M7,16 L17,16 M8,20 L16,20'
    ),
    # Eye: almond shape + pupil
    'eye': (
        'M2,12 Q12,4 22,12 Q12,20 2,12 Z '
        'M12,8 A4,4 0 1,1 12,16 A4,4 0 1,1 12,8 Z'
    ),
    # Cell: circle with nucleus
    'cell': (
        'M12,2 A10,10 0 1,1 12,22 A10,10 0 1,1 12,2 Z '
        'M12,8 A4,4 0 1,1 12,16 A4,4 0 1,1 12,8 Z'
    ),
    # Bone: dumbbell shape
    'bone': (
        'M4,8 A3,3 0 1,1 7,11 L17,11 A3,3 0 1,1 20,8 A3,3 0 1,1 17,13 '
        'L7,13 A3,3 0 1,1 4,16 A3,3 0 1,1 7,13 Z'
    ),
    # Bird silhouette
    'bird': (
        'M4,14 Q8,6 14,8 L18,5 L17,9 L22,10 L17,12 Q14,16 10,15 Q6,15 4,14 Z'
    ),
    # Fish silhouette
    'fish': (
        'M2,12 L8,8 Q14,8 18,12 Q14,16 8,16 Z L6,15 L5,13 L6,9 Z '
        'M18,12 L22,8 L22,16 Z M15,11 A1,1 0 1,1 15,12 Z'
    ),
    # Lizard (body + 4 legs + tail)
    'lizard': (
        'M4,12 Q8,8 12,10 Q16,8 20,12 L22,14 Q18,14 14,16 Q10,14 6,16 L4,12 Z '
        'M8,10 L7,6 M10,12 L11,8 M14,12 L15,8 M18,12 L19,6'
    ),
    # Leaf
    'leaf': (
        'M4,20 Q4,4 20,4 Q20,20 4,20 Z M4,20 L14,10'
    ),
    # Flame
    'flame': (
        'M12,2 Q8,6 8,10 Q8,14 12,12 Q14,16 12,20 Q18,18 18,12 Q18,6 12,2 Z'
    ),
    # Drop (water)
    'drop': (
        'M12,2 Q4,12 8,18 Q12,22 16,18 Q20,12 12,2 Z'
    ),
    # Star (5 point)
    'star': (
        'M12,2 L14.8,9 L22,9.5 L16,14 L18,21 L12,17 L6,21 L8,14 L2,9.5 L9.2,9 Z'
    ),
    # Atom
    'atom': (
        'M12,12 A2,2 0 1,1 12,13 Z '
        'M2,12 Q12,2 22,12 M2,12 Q12,22 22,12 '
        'M12,2 Q22,12 12,22 M12,2 Q2,12 12,22'
    ),
    # Check mark
    'check': 'M4,12 L10,18 L20,4',
    # Cross / X
    'cross': 'M4,4 L20,20 M20,4 L4,20',
    # Lightning
    'bolt': 'M13,2 L6,14 L11,14 L9,22 L18,10 L13,10 Z',
    # Bacterium (rod)
    'bacterium': (
        'M4,10 Q4,6 8,6 L16,6 Q20,6 20,10 L20,14 Q20,18 16,18 L8,18 Q4,18 4,14 Z '
        'M7,10 A1,1 0 1,1 7,11 Z M12,12 A1,1 0 1,1 12,13 Z M17,9 A1,1 0 1,1 17,10 Z'
    ),
    # Sperm (tadpole)
    'sperm': (
        'M6,12 A3,3 0 1,1 12,12 A3,3 0 1,1 6,12 Z '
        'M12,12 Q16,10 18,14 Q20,10 22,14'
    ),
    # Tree (trunk + crown)
    'tree': (
        'M12,2 Q4,8 8,14 L10,14 L10,22 L14,22 L14,14 L16,14 Q20,8 12,2 Z'
    ),
    # Tooth
    'tooth': (
        'M6,4 Q4,10 6,16 L8,22 L10,16 L11,12 L12,16 L14,22 L16,16 Q20,10 18,4 '
        'Q14,2 12,4 Q10,2 6,4 Z'
    ),
    # Dinosaur (simple T-rex silhouette)
    'dino': (
        'M4,16 Q6,10 10,10 L12,6 Q16,4 18,8 L22,10 Q20,12 16,12 L16,16 L14,20 '
        'L12,20 L12,16 L10,16 L10,20 L8,20 L8,16 Z'
    ),
    # Mushroom
    'mushroom': (
        'M4,10 Q4,4 12,4 Q20,4 20,10 L4,10 Z '
        'M8,10 L8,18 Q8,22 12,22 Q16,22 16,18 L16,10 Z'
    ),
    # Arrow right
    'arrow_r': 'M2,12 L18,12 M14,8 L18,12 L14,16',
    # Heart
    'heart': (
        'M12,20 Q2,14 6,6 Q10,2 12,6 Q14,2 18,6 Q22,14 12,20 Z'
    ),
    # Peak (mountain)
    'peak': 'M2,20 L9,6 L14,14 L17,10 L22,20 Z',
    # Flask
    'flask': (
        'M9,2 L9,10 L4,20 Q4,22 6,22 L18,22 Q20,22 20,20 L15,10 L15,2 Z '
        'M9,2 L15,2'
    ),
}


def _bio_icon(key, cx, cy, size, color, stroke_width=1.8, fill_mode='stroke'):
    """Render a biological icon centered at (cx, cy), size=radius.
    fill_mode: 'stroke' (outline only), 'fill' (solid), 'both' (fill + stroke)."""
    path = BIO_ICONS.get(key)
    if not path:
        return ''
    # Scale: 24x24 viewBox -> 2*size target.
    scale = (size * 2) / 24.0
    tx = cx - size
    ty = cy - size
    if fill_mode == 'fill':
        style = f'fill="{color}" stroke="none"'
    elif fill_mode == 'both':
        style = f'fill="{color}" fill-opacity="0.3" stroke="{color}" stroke-width="{stroke_width}"'
    else:
        style = f'fill="none" stroke="{color}" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"'
    return (
        f'<g transform="translate({tx:.1f},{ty:.1f}) scale({scale:.3f})">'
        f'<path d="{path}" {style}/>'
        f'</g>'
    )
