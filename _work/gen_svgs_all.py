#!/usr/bin/env python3
"""Generate concept-specific SVG flashcard images."""
import os
import sys
import math

def math_cos(a):
    return math.cos(a)
def math_sin(a):
    return math.sin(a)

OUT_DIR = r"C:/Users/johnn/Desktop/School/Evolution_EVOL4230/evolution-study-guide/public/img/fc"
os.makedirs(OUT_DIR, exist_ok=True)

FAILURES = []
WRITTEN = []

HDR = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 150" font-family="system-ui, -apple-system, sans-serif">'
BG = '<rect width="240" height="150" fill="#0a1220"/>'

def w(name, body):
    """Write SVG file to OUT_DIR/svg_{name}.svg"""
    try:
        path = os.path.join(OUT_DIR, f"svg_{name}.svg")
        content = HDR + BG + body + "</svg>"
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        WRITTEN.append(name)
    except Exception as e:
        FAILURES.append((name, str(e)))

def title(t, y=13):
    return f'<text x="120" y="{y}" fill="#fbbf24" font-weight="700" font-size="11" text-anchor="middle">{t}</text>'

def subtitle(t, y=145, x=120, anchor="middle", color="#94a3b8", size=9):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" text-anchor="{anchor}">{t}</text>'

def label(t, x, y, color="#e5e7eb", size=8, anchor="middle", weight="400"):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}">{t}</text>'

# ============================================================
# GROUP A: HISTORY OF LIFE / DATING
# ============================================================

def group_a():
    # Earth clock
    w("earth_clock", title("Earth's 24-hr Clock")
        + '<circle cx="120" cy="82" r="48" fill="#111827" stroke="#475569" stroke-width="2"/>'
        + '<path d="M 120 82 L 120 34 A 48 48 0 0 1 120.5 34 Z" fill="#ef4444"/>'
        + '<circle cx="120" cy="82" r="3" fill="#fbbf24"/>'
        + '<line x1="120" y1="82" x2="120" y2="40" stroke="#fbbf24" stroke-width="1.5"/>'
        + '<line x1="120" y1="82" x2="158" y2="82" stroke="#93c5fd" stroke-width="1.5"/>'
        + label("12", 120, 42, color="#94a3b8", size=7)
        + label("6", 162, 85, color="#94a3b8", size=7)
        + label("18", 78, 85, color="#94a3b8", size=7)
        + label("24", 120, 132, color="#94a3b8", size=7)
        + label("humans = last 2 sec", 190, 40, color="#ef4444", size=7, anchor="end")
        + '<line x1="155" y1="42" x2="122" y2="55" stroke="#ef4444" stroke-width="0.8"/>'
        + subtitle("4.568 bya \u2192 now"))

    # Decay curve
    w("decay_curve", title("Radioactive Decay")
        + '<line x1="30" y1="125" x2="220" y2="125" stroke="#475569" stroke-width="1"/>'
        + '<line x1="30" y1="30" x2="30" y2="125" stroke="#475569" stroke-width="1"/>'
        + '<path d="M 30 35 Q 70 70 110 90 Q 150 105 220 118" fill="none" stroke="#ef4444" stroke-width="2"/>'
        + '<path d="M 30 118 Q 70 100 110 85 Q 150 75 220 35" fill="none" stroke="#60a5fa" stroke-width="2" stroke-dasharray="3,2"/>'
        + '<line x1="82" y1="123" x2="82" y2="127" stroke="#fbbf24"/>'
        + '<line x1="134" y1="123" x2="134" y2="127" stroke="#fbbf24"/>'
        + '<line x1="186" y1="123" x2="186" y2="127" stroke="#fbbf24"/>'
        + label("t\u00bd", 82, 135, color="#fbbf24", size=7)
        + label("2t\u00bd", 134, 135, color="#fbbf24", size=7)
        + label("3t\u00bd", 186, 135, color="#fbbf24", size=7)
        + label("parent", 200, 115, color="#fca5a5", size=7, anchor="end")
        + label("daughter", 200, 45, color="#93c5fd", size=7, anchor="end")
        + label("%", 20, 35, color="#94a3b8", size=8)
        + label("half-lives", 125, 146, color="#94a3b8", size=8))

    # Half-life bars
    w("halflife", title("Half-Life Bars")
        + ''.join([
            f'<rect x="{40+i*45}" y="{125-h}" width="30" height="{h}" fill="#ef4444" opacity="0.85"/>'
            + label(f"{pct}%", 55+i*45, 120-h, color="#fde68a", size=8)
            + label(lbl, 55+i*45, 138, color="#94a3b8", size=7)
            for i,(h,pct,lbl) in enumerate([(80,"100","0"),(40,"50","t\u00bd"),(20,"25","2t\u00bd"),(10,"12.5","3t\u00bd")])
        ])
        + '<line x1="30" y1="125" x2="220" y2="125" stroke="#475569"/>')

    # Isotopes
    w("isotopes", title("Carbon Isotopes")
        + '<circle cx="75" cy="85" r="30" fill="none" stroke="#60a5fa" stroke-width="1.5"/>'
        + ''.join([f'<circle cx="{75+dx}" cy="{85+dy}" r="3" fill="#60a5fa"/>' for dx,dy in [(-8,-6),(-4,4),(4,-8),(8,2),(0,-10),(-10,2)]])
        + ''.join([f'<circle cx="{75+dx}" cy="{85+dy}" r="3" fill="#93c5fd" stroke="#60a5fa"/>' for dx,dy in [(10,10),(-12,8),(6,10),(-2,12),(0,6),(12,-4)]])
        + label("\u00b9\u00b2C", 75, 50, color="#60a5fa", size=11, weight="700")
        + label("6p + 6n", 75, 125, color="#93c5fd", size=8)
        + label("STABLE", 75, 137, color="#22c55e", size=8, weight="700")
        + '<circle cx="170" cy="85" r="30" fill="none" stroke="#ef4444" stroke-width="1.5"/>'
        + ''.join([f'<circle cx="{170+dx}" cy="{85+dy}" r="3" fill="#ef4444"/>' for dx,dy in [(-8,-6),(-4,4),(4,-8),(8,2),(0,-10),(-10,2)]])
        + ''.join([f'<circle cx="{170+dx}" cy="{85+dy}" r="3" fill="#fca5a5"/>' for dx,dy in [(10,10),(-12,8),(6,10),(-2,12),(0,6),(12,-4),(-8,12),(14,0)]])
        + label("\u00b9\u2074C", 170, 50, color="#ef4444", size=11, weight="700")
        + label("6p + 8n", 170, 125, color="#fca5a5", size=8)
        + label("RADIOACTIVE", 170, 137, color="#ef4444", size=8, weight="700"))

    # Biomarkers
    w("biomarkers", title("Biomarkers in Rock")
        + ''.join([f'<rect x="30" y="{30+i*18}" width="180" height="18" fill="{c}" opacity="0.7" stroke="#475569"/>' for i,c in enumerate(["#6b7280","#a78bfa","#8b5a3c","#7c4827"])])
        + '<rect x="30" y="48" width="180" height="18" fill="#a78bfa" opacity="0.9" stroke="#fbbf24" stroke-width="1.5"/>'
        + ''.join([f'<polygon points="{x},57 {x+4},54 {x+8},57 {x+8},63 {x+4},66 {x},63" fill="#fbbf24" stroke="#0a1220" stroke-width="0.4"/>' for x in [55,85,115,145,175]])
        + label("1.64 bya", 14, 60, color="#fbbf24", size=7, anchor="start")
        + '<line x1="180" y1="57" x2="215" y2="130" stroke="#fbbf24" stroke-width="1"/>'
        + label("Okenane", 220, 135, color="#fde68a", size=8, anchor="end")
        + subtitle("purple sulfur bacteria"))

    # Stromatolites
    w("stromatolites", title("Stromatolites")
        + '<rect x="0" y="80" width="240" height="70" fill="#1e3a5f" opacity="0.5"/>'
        + ''.join([f'<path d="M {x-20} 115 Q {x-20} {85+i*2} {x} {80+i*2} Q {x+20} {85+i*2} {x+20} 115 Z" fill="none" stroke="#86efac" stroke-width="0.8"/>' for x in [70,120,170] for i in range(8)])
        + ''.join([f'<ellipse cx="{x}" cy="115" rx="22" ry="4" fill="#22c55e" opacity="0.6"/>' for x in [70,120,170]])
        + label("shallow water", 30, 90, color="#93c5fd", size=7, anchor="start")
        + label("microbial mat laminations", 120, 140, color="#86efac", size=8))

    # KT boundary
    w("kt_boundary", title("K-Pg Boundary 66 mya")
        + '<rect x="30" y="25" width="180" height="45" fill="#6b4423"/>'
        + '<rect x="30" y="70" width="180" height="6" fill="#fbbf24"/>'
        + '<rect x="30" y="76" width="180" height="50" fill="#4a5568"/>'
        + label("Cretaceous", 40, 50, color="#fde68a", size=8, anchor="start")
        + label("dinosaurs", 180, 60, color="#fca5a5", size=7, anchor="end")
        + '<path d="M 55 45 L 58 42 L 60 45 L 63 40 L 66 46 L 60 48 Z" fill="#ef4444"/>'
        + label("Ir layer", 212, 75, color="#fbbf24", size=7, anchor="end", weight="700")
        + label("Paleogene", 40, 95, color="#e5e7eb", size=8, anchor="start")
        + label("mammals / birds", 180, 110, color="#86efac", size=7, anchor="end")
        + '<circle cx="195" cy="35" r="5" fill="#ef4444"/>'
        + '<line x1="190" y1="30" x2="198" y2="38" stroke="#fbbf24" stroke-width="0.8"/>'
        + '<line x1="198" y1="30" x2="190" y2="38" stroke="#fbbf24" stroke-width="0.8"/>'
        + subtitle("asteroid \u2192 iridium spike"))

    # RNA world
    w("rna_world", title("RNA World")
        + '<path d="M 120 75 Q 105 55 120 45 Q 135 55 120 75 Q 105 95 120 105 Q 135 95 120 75" fill="none" stroke="#a78bfa" stroke-width="2"/>'
        + ''.join([f'<circle cx="{120+dx}" cy="{75+dy}" r="2.5" fill="#c4b5fd"/>' for dx,dy in [(0,-28),(12,-18),(12,18),(0,28),(-12,18),(-12,-18)]])
        + label("RNA", 120, 79, color="#fde68a", size=9, weight="700")
        + '<line x1="90" y1="60" x2="50" y2="45" stroke="#60a5fa" stroke-width="1.2" marker-end="url(#ar1)"/>'
        + '<line x1="150" y1="60" x2="190" y2="45" stroke="#22c55e" stroke-width="1.2" marker-end="url(#ar1)"/>'
        + '<defs><marker id="ar1" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0,0 6,3 0,6" fill="#fbbf24"/></marker></defs>'
        + label("Information", 45, 40, color="#93c5fd", size=8, anchor="start")
        + label("Storage", 45, 50, color="#93c5fd", size=8, anchor="start")
        + label("Catalysis", 195, 40, color="#86efac", size=8, anchor="end")
        + label("(ribozyme)", 195, 50, color="#86efac", size=8, anchor="end")
        + subtitle("dual role \u2192 origin of life"))

    # LUCA
    w("luca", title("LUCA \u2192 3 Domains")
        + '<line x1="120" y1="125" x2="120" y2="80" stroke="#e5e7eb" stroke-width="2"/>'
        + '<circle cx="120" cy="125" r="4" fill="#fbbf24"/>'
        + label("LUCA", 120, 140, color="#fbbf24", size=9, weight="700")
        + '<line x1="120" y1="80" x2="55" y2="45" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="120" y1="80" x2="120" y2="45" stroke="#a78bfa" stroke-width="2"/>'
        + '<line x1="120" y1="80" x2="185" y2="45" stroke="#22c55e" stroke-width="2"/>'
        + label("BACTERIA", 50, 35, color="#60a5fa", size=8, weight="700")
        + label("ARCHAEA", 120, 35, color="#a78bfa", size=8, weight="700")
        + label("EUKARYA", 190, 35, color="#22c55e", size=8, weight="700"))

    # Endosymbiosis
    w("endosymbiosis", title("Endosymbiosis")
        + '<circle cx="45" cy="85" r="20" fill="none" stroke="#60a5fa" stroke-width="1.5"/>'
        + '<circle cx="60" cy="80" r="4" fill="#ef4444"/>'
        + label("1", 45, 115, color="#fbbf24", size=9, weight="700")
        + label("proto-euk + bac", 45, 128, color="#94a3b8", size=7)
        + '<path d="M 75 85 L 90 85" stroke="#fbbf24" stroke-width="1" marker-end="url(#m2)"/>'
        + '<defs><marker id="m2" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0,0 6,3 0,6" fill="#fbbf24"/></marker></defs>'
        + '<circle cx="120" cy="85" r="22" fill="none" stroke="#60a5fa" stroke-width="1.5"/>'
        + '<circle cx="120" cy="85" r="5" fill="#ef4444"/>'
        + label("2", 120, 115, color="#fbbf24", size=9, weight="700")
        + label("engulfed", 120, 128, color="#94a3b8", size=7)
        + '<path d="M 150 85 L 165 85" stroke="#fbbf24" stroke-width="1" marker-end="url(#m2)"/>'
        + '<ellipse cx="195" cy="85" rx="24" ry="22" fill="none" stroke="#22c55e" stroke-width="1.5"/>'
        + '<ellipse cx="200" cy="82" rx="7" ry="4" fill="#ef4444"/>'
        + '<path d="M 194 82 Q 200 79 205 82" stroke="#0a1220" stroke-width="0.5" fill="none"/>'
        + label("3", 195, 115, color="#fbbf24", size=9, weight="700")
        + label("mitochondrion", 195, 128, color="#86efac", size=7))

    # Oxygenation
    w("oxygenation", title("Great Oxygenation")
        + '<line x1="25" y1="120" x2="225" y2="120" stroke="#475569"/>'
        + '<line x1="25" y1="35" x2="25" y2="120" stroke="#475569"/>'
        + '<path d="M 25 118 L 90 117 L 110 75 L 150 55 L 225 35" fill="none" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="110" y1="75" x2="110" y2="120" stroke="#fbbf24" stroke-dasharray="2,2"/>'
        + label("GOE", 110, 70, color="#fbbf24", size=8, weight="700")
        + label("2.4 bya", 110, 132, color="#fde68a", size=7)
        + label("O\u2082 %", 14, 40, color="#93c5fd", size=8)
        + label("4.5 bya", 25, 142, color="#94a3b8", size=7)
        + label("now", 225, 142, color="#94a3b8", size=7, anchor="end"))

    # Cambrian
    w("cambrian", title("Cambrian Explosion")
        + '<line x1="30" y1="80" x2="90" y2="80" stroke="#e5e7eb" stroke-width="1.5"/>'
        + '<circle cx="90" cy="80" r="3" fill="#fbbf24"/>'
        + label("541 mya", 60, 72, color="#fbbf24", size=8)
        + ''.join([f'<line x1="90" y1="80" x2="{210}" y2="{30+i*8}" stroke="{c}" stroke-width="1.2"/>'
                   + label(n, 215, 33+i*8, color=c, size=6.5, anchor="start")
                   for i,(n,c) in enumerate([("Arthropoda","#60a5fa"),("Mollusca","#93c5fd"),("Chordata","#22c55e"),("Echinoderm","#86efac"),("Brachiopoda","#a78bfa"),("Porifera","#c4b5fd"),("Cnidaria","#fbbf24"),("Annelida","#fca5a5")])]))

    # Tiktaalik
    w("tiktaalik", title("Tiktaalik 375 mya")
        + '<path d="M 50 85 Q 70 70 100 72 Q 150 72 180 78 L 195 75 L 200 82 L 195 89 L 180 86 Q 150 92 100 92 Q 70 94 50 85 Z" fill="#8b7355" stroke="#fde68a" stroke-width="1"/>'
        + '<circle cx="70" cy="80" r="2" fill="#0a1220"/>'
        + '<path d="M 110 92 L 108 105 L 118 102 L 115 94" fill="#8b7355" stroke="#fde68a"/>'
        + '<path d="M 155 92 L 153 105 L 163 102 L 160 94" fill="#8b7355" stroke="#fde68a"/>'
        + label("NECK", 82, 65, color="#fbbf24", size=7)
        + '<line x1="82" y1="67" x2="82" y2="75" stroke="#fbbf24" stroke-width="0.5"/>'
        + label("weight-bearing fins", 135, 120, color="#86efac", size=7)
        + '<line x1="115" y1="108" x2="115" y2="115" stroke="#86efac" stroke-width="0.5"/>'
        + label("FISH", 25, 140, color="#60a5fa", size=8, weight="700", anchor="start")
        + label("\u2192", 120, 140, color="#94a3b8", size=10)
        + label("TETRAPOD", 215, 140, color="#22c55e", size=8, weight="700", anchor="end"))

    # Permian
    w("permian", title("Permian Extinction")
        + '<circle cx="85" cy="82" r="32" fill="#0a1220" stroke="#475569"/>'
        + '<path d="M 85 82 L 85 50 A 32 32 0 1 1 82 114 Z" fill="#ef4444"/>'
        + '<path d="M 85 82 L 82 114 A 32 32 0 0 1 85 50 Z" fill="#22c55e"/>'
        + label("96%", 70, 80, color="#fca5a5", size=9, weight="700")
        + label("extinct", 70, 92, color="#fca5a5", size=7)
        + label("4%", 105, 70, color="#86efac", size=8, weight="700")
        + label("The Great Dying", 165, 55, color="#fde68a", size=8)
        + label("252 mya", 165, 70, color="#94a3b8", size=8)
        + '<rect x="135" y="80" width="70" height="28" fill="#1f2937" stroke="#fbbf24" stroke-width="0.8"/>'
        + label("Siberian", 170, 93, color="#fbbf24", size=8)
        + label("Traps", 170, 103, color="#fbbf24", size=8))

    # Lagerstatte
    w("lagerstaette", title("Lagerst\u00e4tte")
        + '<rect x="20" y="30" width="200" height="25" fill="#8b6f47"/>'
        + '<rect x="20" y="55" width="200" height="30" fill="#374151"/>'
        + '<rect x="20" y="85" width="200" height="30" fill="#8b6f47"/>'
        + ''.join([f'<path d="M {x} 72 Q {x+8} 65 {x+15} 72 Q {x+20} 75 {x+15} 78 Q {x+8} 72 {x} 72" fill="none" stroke="#86efac" stroke-width="0.8"/>' for x in [50,110,170]])
        + '<path d="M 80 70 Q 95 68 100 72 L 92 75 Z" fill="none" stroke="#86efac" stroke-width="0.8"/>'
        + '<path d="M 145 75 Q 155 72 160 78" fill="none" stroke="#86efac" stroke-width="0.8"/>'
        + label("oxic", 27, 45, color="#fde68a", size=7, anchor="start")
        + label("ANOXIC \u2192 soft-body preserved", 27, 70, color="#86efac", size=7, anchor="start")
        + label("oxic", 27, 100, color="#fde68a", size=7, anchor="start")
        + subtitle("exceptional preservation"))

    # Geologic timeline
    periods = [("C","#60a5fa"),("O","#22c55e"),("S","#fbbf24"),("D","#a78bfa"),("C","#86efac"),("P","#ef4444"),("Tr","#c4b5fd"),("J","#93c5fd"),("K","#fde68a"),("Pg","#fca5a5"),("N","#e5e7eb")]
    bars = ""
    bw = 17
    for i,(n,c) in enumerate(periods):
        bars += f'<rect x="{25+i*bw}" y="60" width="{bw-1}" height="20" fill="{c}" opacity="0.8"/>'
        bars += label(n, 25+i*bw+bw/2, 74, color="#0a1220", size=7, weight="700")
    # Big 5 spikes
    spikes = [42,75,127,160,195]  # approx x positions
    for x in spikes:
        bars += f'<line x1="{x}" y1="55" x2="{x}" y2="95" stroke="#ef4444" stroke-width="1.5"/>'
        bars += f'<polygon points="{x-3},55 {x+3},55 {x},48" fill="#ef4444"/>'
    w("geologic_timeline", title("Geologic Time") + bars
        + label("Cambrian", 30, 110, color="#60a5fa", size=7, anchor="start")
        + label("Cenozoic", 215, 110, color="#fca5a5", size=7, anchor="end")
        + subtitle("red = Big 5 extinctions"))

    # Precambrian
    w("precambrian", title("Precambrian")
        + '<rect x="20" y="55" width="176" height="22" fill="#a78bfa" opacity="0.8"/>'
        + '<rect x="196" y="55" width="24" height="22" fill="#22c55e" opacity="0.8"/>'
        + label("Precambrian = 88%", 108, 70, color="#0a1220", size=9, weight="700")
        + label("Phan.", 208, 70, color="#0a1220", size=7, weight="700")
        + '<line x1="40" y1="85" x2="40" y2="95" stroke="#fbbf24"/>'
        + label("3.8 life", 40, 105, color="#fbbf24", size=6)
        + '<line x1="95" y1="85" x2="95" y2="95" stroke="#fbbf24"/>'
        + label("2.4 GOE", 95, 105, color="#fbbf24", size=6)
        + '<line x1="155" y1="85" x2="155" y2="95" stroke="#fbbf24"/>'
        + label("1.8 euk", 155, 105, color="#fbbf24", size=6)
        + '<line x1="190" y1="85" x2="190" y2="95" stroke="#fbbf24"/>'
        + label("635 multi", 190, 115, color="#fbbf24", size=6)
        + subtitle("4.0 \u2192 0.541 bya", y=138))

    # Earliest life
    w("earliest_life", title("Earliest Life")
        + '<rect x="20" y="45" width="200" height="25" fill="#6b4423"/>'
        + '<ellipse cx="60" cy="57" rx="15" ry="4" fill="#86efac" opacity="0.8"/>'
        + '<ellipse cx="110" cy="57" rx="15" ry="4" fill="#86efac" opacity="0.8"/>'
        + '<ellipse cx="160" cy="57" rx="15" ry="4" fill="#86efac" opacity="0.8"/>'
        + label("stromatolites 3.45 bya", 120, 38, color="#86efac", size=8)
        + '<rect x="20" y="85" width="200" height="25" fill="#4a5568"/>'
        + ''.join([f'<polygon points="{x},92 {x+4},88 {x+8},92 {x+8},97 {x+4},101 {x},97" fill="#fbbf24"/>' for x in [55,110,165]])
        + label("biomarkers 3.8 bya (graphite)", 120, 125, color="#fbbf24", size=8))

    # Ribozymes
    w("ribozymes", title("Ribozymes")
        + '<path d="M 50 85 Q 70 40 100 55 Q 130 80 115 105 Q 90 120 60 110 Q 30 95 50 85 Z" fill="none" stroke="#a78bfa" stroke-width="1.5"/>'
        + '<circle cx="90" cy="80" r="10" fill="none" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="2,1"/>'
        + label("active", 90, 75, color="#fbbf24", size=6)
        + label("site", 90, 85, color="#fbbf24", size=6)
        + '<rect x="140" y="55" width="16" height="10" fill="#ef4444"/>'
        + label("S", 148, 63, color="#0a1220", size=8, weight="700")
        + '<path d="M 160 60 L 180 60" stroke="#fbbf24" marker-end="url(#rb)"/>'
        + '<defs><marker id="rb" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0,0 6,3 0,6" fill="#fbbf24"/></marker></defs>'
        + '<rect x="182" y="55" width="8" height="10" fill="#22c55e"/>'
        + '<rect x="192" y="55" width="8" height="10" fill="#22c55e"/>'
        + label("P", 195, 63, color="#0a1220", size=8, weight="700")
        + label("catalytic RNA", 170, 100, color="#c4b5fd", size=7)
        + subtitle("RNA enzyme"))

    # K-Ar dating
    w("kar_dating", title("K-Ar Dating")
        + '<polygon points="60,115 90,50 120,115" fill="#6b4423" stroke="#fde68a"/>'
        + '<path d="M 85 55 Q 90 48 95 55 L 92 45 L 97 42 L 90 38 L 85 42 L 88 48 Z" fill="#ef4444"/>'
        + '<circle cx="175" cy="70" r="22" fill="none" stroke="#fbbf24" stroke-width="1.5"/>'
        + '<line x1="175" y1="70" x2="175" y2="52" stroke="#fbbf24"/>'
        + '<line x1="175" y1="70" x2="190" y2="70" stroke="#fbbf24"/>'
        + label("reset", 90, 130, color="#fca5a5", size=7)
        + label("at eruption", 90, 140, color="#fca5a5", size=7)
        + label("K \u2192 Ar", 175, 105, color="#fde68a", size=9, weight="700")
        + label("t\u00bd = 1.25 By", 175, 118, color="#93c5fd", size=7)
        + label("clock starts", 175, 135, color="#94a3b8", size=7))

    # Burgess shale
    w("burgess_shale", title("Burgess Shale")
        + '<rect x="20" y="35" width="200" height="90" fill="#374151"/>'
        + ''.join([f'<line x1="20" y1="{45+i*12}" x2="220" y2="{45+i*12}" stroke="#4b5563" stroke-width="0.5"/>' for i in range(7)])
        + '<path d="M 50 70 Q 60 60 85 65 Q 100 68 105 75 L 95 80 L 85 78 Q 70 82 55 78 Q 45 75 50 70 Z" fill="none" stroke="#fbbf24" stroke-width="0.8"/>'
        + label("Anomalocaris", 75, 55, color="#fbbf24", size=6)
        + '<ellipse cx="150" cy="95" rx="22" ry="7" fill="none" stroke="#86efac" stroke-width="0.8"/>'
        + ''.join([f'<line x1="{130+i*4}" y1="90" x2="{130+i*4}" y2="85" stroke="#86efac" stroke-width="0.5"/>' for i in range(6)])
        + label("Opabinia", 150, 112, color="#86efac", size=6)
        + subtitle("541 mya Cambrian"))

    # Ediacaran
    w("ediacaran", title("Ediacaran Fauna")
        + '<circle cx="60" cy="75" r="20" fill="none" stroke="#a78bfa" stroke-width="1"/>'
        + ''.join([f'<line x1="60" y1="75" x2="{60+20*math_cos(a)}" y2="{75+20*math_sin(a)}" stroke="#a78bfa" stroke-width="0.5"/>' for a in [0,0.785,1.57,2.36,3.14,3.93,4.71,5.5]])
        + label("Dickinsonia", 60, 108, color="#c4b5fd", size=7)
        + '<path d="M 150 95 L 150 50 Q 140 55 142 65 Q 148 62 150 68 Q 152 62 158 65 Q 160 55 150 50" fill="none" stroke="#86efac" stroke-width="1"/>'
        + ''.join([f'<line x1="{145+i*3}" y1="{55+i*3}" x2="{155-i*2}" y2="{58+i*3}" stroke="#86efac" stroke-width="0.4"/>' for i in range(6)])
        + label("Charniodiscus", 150, 108, color="#86efac", size=7)
        + subtitle("635\u2013541 mya"))

    # Three domains
    w("three_domains", title("Three Domains")
        + '<circle cx="120" cy="130" r="3" fill="#fbbf24"/>'
        + label("LUCA", 120, 140, color="#fbbf24", size=7)
        + '<line x1="120" y1="130" x2="50" y2="60" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="120" y1="130" x2="120" y2="40" stroke="#a78bfa" stroke-width="2"/>'
        + '<line x1="120" y1="130" x2="190" y2="60" stroke="#22c55e" stroke-width="2"/>'
        + ''.join([f'<line x1="50" y1="60" x2="{30+i*12}" y2="35" stroke="#60a5fa" stroke-width="1"/>' for i in range(3)])
        + ''.join([f'<line x1="120" y1="40" x2="{105+i*12}" y2="20" stroke="#a78bfa" stroke-width="1"/>' for i in range(3)])
        + ''.join([f'<line x1="190" y1="60" x2="{175+i*12}" y2="35" stroke="#22c55e" stroke-width="1"/>' for i in range(3)])
        + label("Bacteria", 45, 75, color="#60a5fa", size=8, weight="700")
        + label("Archaea", 120, 55, color="#a78bfa", size=8, weight="700")
        + label("Eukarya", 195, 75, color="#22c55e", size=8, weight="700"))

    # Circumstellar disk
    w("circumstellar_disk", title("Circumstellar Disk")
        + ''.join([f'<ellipse cx="120" cy="85" rx="{r}" ry="{r/4}" fill="none" stroke="#fbbf24" stroke-width="0.4" opacity="{0.9-r*0.01}"/>' for r in [30,50,70,90]])
        + '<circle cx="120" cy="85" r="10" fill="#fbbf24"/>'
        + '<circle cx="120" cy="85" r="14" fill="#fbbf24" opacity="0.3"/>'
        + '<circle cx="75" cy="85" r="3" fill="#60a5fa"/>'
        + '<circle cx="165" cy="88" r="4" fill="#86efac"/>'
        + '<circle cx="195" cy="82" r="2.5" fill="#fca5a5"/>'
        + label("young sun", 120, 115, color="#fde68a", size=8)
        + subtitle("4.6 bya \u2022 planet formation"))

    # Ordovician extinction
    w("ordovician_ext", title("Ordovician Extinction")
        + '<line x1="25" y1="110" x2="225" y2="110" stroke="#475569"/>'
        + '<line x1="25" y1="35" x2="25" y2="110" stroke="#475569"/>'
        + '<path d="M 25 100 L 70 95 L 100 30 L 115 40 L 160 65 L 225 60" fill="none" stroke="#ef4444" stroke-width="2"/>'
        + '<line x1="100" y1="30" x2="100" y2="110" stroke="#fbbf24" stroke-dasharray="2,2"/>'
        + label("445 mya", 100, 25, color="#fbbf24", size=7, weight="700")
        + label("86% species loss", 165, 50, color="#fca5a5", size=7)
        + label("glacial cooling", 165, 90, color="#93c5fd", size=7)
        + label("extinction %", 14, 40, color="#94a3b8", size=7)
        + subtitle("Ordovician glaciation"))


# ============================================================
# GROUP B: PHYLOGENETICS
# ============================================================

def group_b():
    # Phylo tree
    w("phylo_tree", title("Phylogenetic Tree")
        + '<line x1="30" y1="85" x2="70" y2="85" stroke="#ef4444" stroke-width="2"/>'
        + '<circle cx="30" cy="85" r="3.5" fill="#ef4444"/>'
        + '<line x1="70" y1="85" x2="110" y2="50" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="70" y1="85" x2="110" y2="120" stroke="#60a5fa" stroke-width="2"/>'
        + '<circle cx="70" cy="85" r="3" fill="#a78bfa"/>'
        + '<line x1="110" y1="50" x2="180" y2="40" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="110" y1="50" x2="180" y2="65" stroke="#60a5fa" stroke-width="2"/>'
        + '<circle cx="110" cy="50" r="3" fill="#a78bfa"/>'
        + '<line x1="110" y1="120" x2="180" y2="110" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="110" y1="120" x2="180" y2="130" stroke="#60a5fa" stroke-width="2"/>'
        + '<circle cx="110" cy="120" r="3" fill="#a78bfa"/>'
        + ''.join([f'<circle cx="180" cy="{y}" r="3" fill="#fde68a"/>' for y in [40,65,110,130]])
        + '<path d="M 188 36 L 195 36 L 195 69 L 188 69" fill="none" stroke="#22c55e" stroke-width="1.2"/>'
        + label("CLADE", 205, 55, color="#22c55e", size=7, anchor="start")
        + label("root", 22, 98, color="#ef4444", size=7, anchor="start")
        + label("node", 70, 100, color="#a78bfa", size=7)
        + label("branch", 90, 35, color="#60a5fa", size=7)
        + label("tips", 188, 138, color="#fde68a", size=7, anchor="start"))

    # Sister taxa
    w("sister_taxa", title("Sister Taxa")
        + '<line x1="70" y1="110" x2="70" y2="60" stroke="#e5e7eb" stroke-width="2"/>'
        + '<line x1="70" y1="60" x2="120" y2="40" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="70" y1="60" x2="120" y2="80" stroke="#60a5fa" stroke-width="2"/>'
        + '<circle cx="70" cy="60" r="4" fill="#a78bfa"/>'
        + '<circle cx="120" cy="40" r="4" fill="#fde68a"/>'
        + '<circle cx="120" cy="80" r="4" fill="#fde68a"/>'
        + label("Taxon A", 128, 43, color="#fde68a", size=8, anchor="start")
        + label("Taxon B", 128, 83, color="#fde68a", size=8, anchor="start")
        + label("common", 70, 125, color="#a78bfa", size=7)
        + label("ancestor", 70, 135, color="#a78bfa", size=7)
        + '<path d="M 195 35 L 210 35 L 210 85 L 195 85" fill="none" stroke="#22c55e" stroke-width="1.2"/>'
        + label("closest", 220, 55, color="#22c55e", size=7, anchor="start")
        + label("relatives", 220, 65, color="#22c55e", size=7, anchor="start"))

    # Synapomorphy
    w("synapomorphy", title("Synapomorphy")
        + '<line x1="40" y1="85" x2="80" y2="85" stroke="#e5e7eb" stroke-width="2"/>'
        + '<line x1="80" y1="85" x2="130" y2="50" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="80" y1="85" x2="130" y2="120" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="130" y1="50" x2="190" y2="40" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="130" y1="50" x2="190" y2="65" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="105" y1="70" x2="105" y2="60" stroke="#ef4444" stroke-width="3"/>'
        + label("trait X", 75, 55, color="#ef4444", size=7, anchor="start")
        + label("appears", 75, 65, color="#ef4444", size=7, anchor="start")
        + '<path d="M 198 36 L 208 36 L 208 69 L 198 69" fill="none" stroke="#22c55e" stroke-width="1.2"/>'
        + label("CLADE", 212, 55, color="#22c55e", size=8, anchor="start", weight="700")
        + label("shared derived -> defines group", 120, 135, color="#fde68a", size=7))

    # Symplesiomorphy
    w("symplesiomorphy", title("Symplesiomorphy")
        + '<line x1="25" y1="85" x2="60" y2="85" stroke="#e5e7eb" stroke-width="2"/>'
        + '<line x1="60" y1="85" x2="110" y2="45" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="60" y1="85" x2="110" y2="125" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="110" y1="45" x2="200" y2="35" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="110" y1="45" x2="200" y2="65" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="40" y1="90" x2="40" y2="80" stroke="#ef4444" stroke-width="3"/>'
        + label("trait", 40, 72, color="#ef4444", size=7)
        + ''.join([f'<circle cx="205" cy="{y}" r="3" fill="#ef4444"/>' for y in [35,65]])
        + '<circle cx="205" cy="125" r="3" fill="#ef4444"/>'
        + label("ingroup + outgroup", 120, 135, color="#fca5a5", size=7)
        + '<line x1="140" y1="108" x2="155" y2="118" stroke="#ef4444" stroke-width="2"/>'
        + '<line x1="155" y1="108" x2="140" y2="118" stroke="#ef4444" stroke-width="2"/>'
        + label("NOT informative", 165, 115, color="#ef4444", size=7, anchor="start", weight="700"))

    # Monophyletic
    w("monophyletic", title("Monophyletic")
        + '<line x1="35" y1="85" x2="70" y2="85" stroke="#e5e7eb" stroke-width="2"/>'
        + '<line x1="70" y1="85" x2="110" y2="50" stroke="#22c55e" stroke-width="2"/>'
        + '<line x1="70" y1="85" x2="110" y2="120" stroke="#22c55e" stroke-width="2"/>'
        + '<line x1="110" y1="50" x2="180" y2="40" stroke="#22c55e" stroke-width="2"/>'
        + '<line x1="110" y1="50" x2="180" y2="65" stroke="#22c55e" stroke-width="2"/>'
        + '<line x1="110" y1="120" x2="180" y2="110" stroke="#22c55e" stroke-width="2"/>'
        + '<line x1="110" y1="120" x2="180" y2="130" stroke="#22c55e" stroke-width="2"/>'
        + ''.join([f'<circle cx="180" cy="{y}" r="4" fill="#86efac"/>' for y in [40,65,110,130]])
        + '<circle cx="70" cy="85" r="5" fill="#fbbf24"/>'
        + label("ancestor", 70, 103, color="#fbbf24", size=7)
        + '<path d="M 190 33 L 210 33 L 210 137 L 190 137" fill="none" stroke="#22c55e" stroke-width="1.5"/>'
        + label("ALL kids", 220, 85, color="#22c55e", size=8, anchor="start", weight="700")
        + subtitle("ancestor + all descendants"))

    # Paraphyletic
    w("paraphyletic", title("Paraphyletic")
        + '<line x1="35" y1="85" x2="70" y2="85" stroke="#e5e7eb" stroke-width="2"/>'
        + '<line x1="70" y1="85" x2="110" y2="50" stroke="#22c55e" stroke-width="2"/>'
        + '<line x1="70" y1="85" x2="110" y2="120" stroke="#22c55e" stroke-width="2"/>'
        + '<line x1="110" y1="50" x2="180" y2="40" stroke="#22c55e" stroke-width="2"/>'
        + '<line x1="110" y1="50" x2="180" y2="65" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,2"/>'
        + '<line x1="110" y1="120" x2="180" y2="110" stroke="#22c55e" stroke-width="2"/>'
        + '<line x1="110" y1="120" x2="180" y2="130" stroke="#22c55e" stroke-width="2"/>'
        + '<circle cx="180" cy="40" r="4" fill="#86efac"/>'
        + '<circle cx="180" cy="65" r="4" fill="#ef4444"/>'
        + label("birds", 190, 68, color="#ef4444", size=7, anchor="start")
        + label("excluded", 190, 78, color="#ef4444", size=7, anchor="start")
        + '<circle cx="180" cy="110" r="4" fill="#86efac"/>'
        + '<circle cx="180" cy="130" r="4" fill="#86efac"/>'
        + label("Reptilia w/o birds = INVALID", 120, 143, color="#ef4444", size=8, weight="700"))

    # Polyphyletic
    w("polyphyletic", title("Polyphyletic")
        + '<line x1="35" y1="85" x2="70" y2="85" stroke="#e5e7eb" stroke-width="2"/>'
        + '<line x1="70" y1="85" x2="120" y2="45" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="70" y1="85" x2="120" y2="125" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="120" y1="45" x2="180" y2="35" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="120" y1="45" x2="180" y2="60" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="120" y1="125" x2="180" y2="110" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="120" y1="125" x2="180" y2="135" stroke="#60a5fa" stroke-width="2"/>'
        + ''.join([f'<circle cx="182" cy="{y}" r="4" fill="#fde68a"/>' for y in [35,60,110,135]])
        + '<ellipse cx="190" cy="47" rx="14" ry="18" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,2"/>'
        + '<ellipse cx="190" cy="122" rx="14" ry="16" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,2"/>'
        + '<line x1="204" y1="47" x2="204" y2="122" stroke="#ef4444" stroke-width="0.8" stroke-dasharray="2,2"/>'
        + label("elephant", 40, 45, color="#94a3b8", size=7, anchor="start")
        + label("hippo", 40, 130, color="#94a3b8", size=7, anchor="start")
        + subtitle("separate ancestries", y=138))

    # Homoplasy
    w("homoplasy", title("Homoplasy")
        + '<line x1="30" y1="85" x2="60" y2="85" stroke="#e5e7eb" stroke-width="2"/>'
        + '<line x1="60" y1="85" x2="110" y2="50" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="60" y1="85" x2="110" y2="120" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="110" y1="50" x2="200" y2="50" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="110" y1="120" x2="200" y2="120" stroke="#60a5fa" stroke-width="2"/>'
        + '<path d="M 195 45 L 210 35 L 215 40 L 205 55 Z" fill="#fbbf24"/>'
        + '<path d="M 195 115 L 210 105 L 215 110 L 205 125 Z" fill="#fbbf24"/>'
        + label("WINGS", 225, 55, color="#fde68a", size=7, anchor="end")
        + label("WINGS", 225, 125, color="#fde68a", size=7, anchor="end")
        + label("convergence", 120, 90, color="#ef4444", size=7)
        + subtitle("independent origins"))

    # Parsimony
    w("parsimony", title("Parsimony")
        + '<line x1="30" y1="85" x2="55" y2="85" stroke="#fca5a5"/>'
        + '<line x1="55" y1="85" x2="80" y2="60" stroke="#fca5a5"/>'
        + '<line x1="55" y1="85" x2="80" y2="110" stroke="#fca5a5"/>'
        + '<line x1="80" y1="60" x2="110" y2="50" stroke="#fca5a5"/>'
        + '<line x1="80" y1="60" x2="110" y2="70" stroke="#fca5a5"/>'
        + ''.join([f'<line x1="{x}" y1="{y-4}" x2="{x}" y2="{y+4}" stroke="#ef4444" stroke-width="2"/>' for x,y in [(67,72),(75,87),(90,62),(95,95),(100,55)]])
        + label("Tree A: 5", 70, 125, color="#ef4444", size=8)
        + '<line x1="130" y1="85" x2="155" y2="85" stroke="#86efac"/>'
        + '<line x1="155" y1="85" x2="180" y2="60" stroke="#86efac"/>'
        + '<line x1="155" y1="85" x2="180" y2="110" stroke="#86efac"/>'
        + '<line x1="180" y1="60" x2="210" y2="50" stroke="#86efac"/>'
        + '<line x1="180" y1="60" x2="210" y2="70" stroke="#86efac"/>'
        + ''.join([f'<line x1="{x}" y1="{y-4}" x2="{x}" y2="{y+4}" stroke="#22c55e" stroke-width="2"/>' for x,y in [(170,72),(175,87),(195,60)]])
        + '<polygon points="165,30 168,36 174,36 169,40 171,46 165,42 159,46 161,40 156,36 162,36" fill="#fbbf24"/>'
        + label("Tree B: 3", 175, 125, color="#22c55e", size=8, weight="700")
        + subtitle("Occam: fewest changes"))

    # Homology
    w("homology", title("Homology: Forelimbs")
        + ''.join([
            f'<g transform="translate({x},30)">'
            + f'<rect x="0" y="0" width="10" height="20" fill="#60a5fa" rx="2"/>'
            + f'<rect x="-2" y="22" width="6" height="18" fill="#93c5fd" rx="1"/>'
            + f'<rect x="6" y="22" width="6" height="18" fill="#93c5fd" rx="1"/>'
            + f'<rect x="-4" y="42" width="18" height="14" fill="#a78bfa" rx="1"/>'
            + f'<text x="5" y="75" fill="#e5e7eb" font-size="7" text-anchor="middle">{n}</text>'
            + '</g>'
            for x,n in [(35,"human"),(90,"whale"),(145,"bat"),(200,"bird")]
        ])
        + subtitle("same bones, different uses"))

    # Exaptation
    w("exaptation", title("Exaptation")
        + '<rect x="15" y="45" width="55" height="20" fill="#1f2937" stroke="#60a5fa"/>'
        + label("Feathers", 42, 56, color="#93c5fd", size=8)
        + label("(insulation)", 42, 75, color="#94a3b8", size=7)
        + '<line x1="70" y1="55" x2="95" y2="55" stroke="#fbbf24" stroke-width="1.5" marker-end="url(#ex1)"/>'
        + '<defs><marker id="ex1" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0,0 6,3 0,6" fill="#fbbf24"/></marker></defs>'
        + '<rect x="100" y="45" width="50" height="20" fill="#1f2937" stroke="#22c55e"/>'
        + label("FLIGHT", 125, 58, color="#86efac", size=9, weight="700")
        + '<rect x="15" y="100" width="65" height="18" fill="#1f2937" stroke="#60a5fa"/>'
        + label("swim bladder", 47, 112, color="#93c5fd", size=8)
        + '<line x1="80" y1="109" x2="105" y2="109" stroke="#fbbf24" stroke-width="1.5" marker-end="url(#ex1)"/>'
        + '<rect x="110" y="100" width="40" height="18" fill="#1f2937" stroke="#22c55e"/>'
        + label("lungs", 130, 112, color="#86efac", size=9, weight="700")
        + subtitle("co-opted for new function"))

    # Outgroup
    w("outgroup", title("Outgroup Rooting")
        + '<line x1="40" y1="120" x2="80" y2="120" stroke="#ef4444" stroke-width="2"/>'
        + '<line x1="80" y1="120" x2="120" y2="40" stroke="#ef4444" stroke-width="2"/>'
        + '<circle cx="120" cy="40" r="4" fill="#ef4444"/>'
        + label("OUTGROUP", 128, 43, color="#ef4444", size=8, anchor="start", weight="700")
        + '<line x1="80" y1="120" x2="110" y2="125" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="110" y1="125" x2="150" y2="90" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="110" y1="125" x2="150" y2="135" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="150" y1="90" x2="200" y2="80" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="150" y1="90" x2="200" y2="105" stroke="#60a5fa" stroke-width="2"/>'
        + ''.join([f'<circle cx="200" cy="{y}" r="3" fill="#fde68a"/>' for y in [80,105]])
        + '<circle cx="150" cy="135" r="3" fill="#fde68a"/>'
        + '<path d="M 190 75 L 215 75 L 215 140 L 190 140" fill="none" stroke="#22c55e" stroke-width="1"/>'
        + label("INGROUP", 220, 110, color="#22c55e", size=8, anchor="start", weight="700"))

    # Cladistics
    w("cladistics", title("Cladistics")
        + '<rect x="20" y="30" width="90" height="65" fill="#1f2937" stroke="#475569"/>'
        + ''.join([label(h, 40+i*20, 42, color="#94a3b8", size=7) for i,h in enumerate(["c1","c2","c3"])])
        + ''.join([label(t, 30, 55+i*12, color="#fde68a", size=7, anchor="start") for i,t in enumerate(["A","B","C","D"])])
        + ''.join([label(str(v), 40+j*20, 55+i*12, color="#e5e7eb", size=7)
                   for i,row in enumerate([[0,0,0],[1,0,0],[1,1,0],[1,1,1]])
                   for j,v in enumerate(row)])
        + '<line x1="115" y1="62" x2="135" y2="62" stroke="#fbbf24" stroke-width="1.5" marker-end="url(#cl1)"/>'
        + '<defs><marker id="cl1" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0,0 6,3 0,6" fill="#fbbf24"/></marker></defs>'
        + '<line x1="140" y1="85" x2="160" y2="85" stroke="#60a5fa" stroke-width="1.5"/>'
        + '<line x1="160" y1="85" x2="185" y2="40" stroke="#60a5fa" stroke-width="1.5"/>'
        + '<line x1="160" y1="85" x2="185" y2="95" stroke="#60a5fa" stroke-width="1.5"/>'
        + '<line x1="185" y1="40" x2="215" y2="40" stroke="#60a5fa" stroke-width="1.5"/>'
        + '<line x1="185" y1="40" x2="210" y2="55" stroke="#60a5fa" stroke-width="1.5"/>'
        + subtitle("matrix -> cladogram", y=115))

    # Molecular clock
    w("molecular_clock", title("Molecular Clock")
        + '<line x1="30" y1="120" x2="220" y2="120" stroke="#475569"/>'
        + '<line x1="30" y1="35" x2="30" y2="120" stroke="#475569"/>'
        + '<line x1="30" y1="115" x2="215" y2="40" stroke="#60a5fa" stroke-width="2"/>'
        + ''.join([f'<circle cx="{30+i*45}" cy="{115-i*18.5}" r="3" fill="#fbbf24"/>' for i in range(5)])
        + label("time (mya)", 125, 140, color="#94a3b8", size=8)
        + label("div %", 18, 40, color="#93c5fd", size=7)
        + label("slope = mu", 160, 70, color="#fde68a", size=7)
        + subtitle("steady mutations"))

    # Bootstrap
    w("bootstrap", title("Bootstrap Support")
        + ''.join([
            f'<g transform="translate({20+i*55},30)">'
            + '<line x1="0" y1="45" x2="15" y2="45" stroke="#60a5fa" stroke-width="1.5"/>'
            + '<line x1="15" y1="45" x2="30" y2="25" stroke="#60a5fa" stroke-width="1.5"/>'
            + '<line x1="15" y1="45" x2="30" y2="65" stroke="#60a5fa" stroke-width="1.5"/>'
            + f'<text x="18" y="42" fill="{c}" font-size="8" font-weight="700">{v}</text>'
            + f'<text x="15" y="88" fill="#94a3b8" font-size="7" text-anchor="middle">{lab}</text>'
            + '</g>'
            for i,(v,c,lab) in enumerate([("95","#22c55e","high"),("78","#fbbf24","med"),("52","#fb923c","low"),("28","#ef4444","poor")])
        ])
        + subtitle("% support across resamples"))

    # Convergent examples
    w("convergent_examples", title("Convergent Evolution")
        + '<path d="M 30 55 Q 60 40 100 50 Q 115 52 125 55 L 125 60 Q 115 60 100 58 Q 90 57 85 60 L 90 65 L 85 67 L 80 63 Q 60 68 30 55 Z" fill="#60a5fa" stroke="#93c5fd"/>'
        + '<path d="M 105 48 L 115 38 L 120 48 Z" fill="#60a5fa"/>'
        + label("dolphin (mammal)", 80, 85, color="#93c5fd", size=7)
        + '<path d="M 30 110 Q 60 95 100 105 Q 115 107 125 110 L 125 115 Q 115 115 100 113 Q 90 112 85 115 L 90 120 L 85 122 L 80 118 Q 60 123 30 110 Z" fill="#a78bfa" stroke="#c4b5fd"/>'
        + '<path d="M 105 103 L 115 93 L 120 103 Z" fill="#a78bfa"/>'
        + label("shark (fish)", 80, 138, color="#c4b5fd", size=7)
        + label("same shape", 190, 82, color="#fde68a", size=7)
        + label("diff ancestor", 190, 92, color="#fde68a", size=7))

    # Morpho vs molec
    w("morpho_vs_molec", title("Morphology vs Molecules")
        + '<rect x="20" y="30" width="95" height="55" fill="#1f2937" stroke="#60a5fa"/>'
        + '<ellipse cx="45" cy="55" rx="10" ry="3" fill="#93c5fd"/>'
        + '<rect x="60" y="50" width="4" height="12" fill="#93c5fd"/>'
        + '<rect x="70" y="52" width="4" height="10" fill="#93c5fd"/>'
        + '<ellipse cx="90" cy="60" rx="8" ry="4" fill="#93c5fd"/>'
        + label("fossils / bones", 67, 78, color="#93c5fd", size=7)
        + '<rect x="125" y="30" width="95" height="55" fill="#1f2937" stroke="#a78bfa"/>'
        + ''.join([label(c, 135+i*12, 55, color="#c4b5fd", size=8, weight="700") for i,c in enumerate(["A","T","G","C","G","T","A"])])
        + label("DNA sequences", 172, 78, color="#c4b5fd", size=7)
        + '<line x1="105" y1="125" x2="135" y2="125" stroke="#22c55e" stroke-width="1.5"/>'
        + '<line x1="135" y1="125" x2="145" y2="118" stroke="#22c55e"/>'
        + '<line x1="135" y1="125" x2="145" y2="132" stroke="#22c55e"/>'
        + label("tree", 145, 145, color="#22c55e", size=7))

    # Tree topology
    w("tree_topology", title("Topology vs Branch Length")
        + '<g transform="translate(10,30)">'
        + '<line x1="15" y1="50" x2="35" y2="50" stroke="#60a5fa"/>'
        + '<line x1="35" y1="50" x2="60" y2="25" stroke="#60a5fa"/>'
        + '<line x1="35" y1="50" x2="60" y2="75" stroke="#60a5fa"/>'
        + '<line x1="60" y1="25" x2="95" y2="20" stroke="#60a5fa"/>'
        + '<line x1="60" y1="25" x2="95" y2="35" stroke="#60a5fa"/>'
        + '<text x="55" y="100" fill="#93c5fd" font-size="7" text-anchor="middle">same topology</text>'
        + '</g>'
        + '<g transform="translate(130,30)">'
        + '<line x1="5" y1="50" x2="15" y2="50" stroke="#22c55e"/>'
        + '<line x1="15" y1="50" x2="30" y2="25" stroke="#22c55e"/>'
        + '<line x1="15" y1="50" x2="55" y2="75" stroke="#22c55e"/>'
        + '<line x1="30" y1="25" x2="95" y2="15" stroke="#22c55e"/>'
        + '<line x1="30" y1="25" x2="60" y2="40" stroke="#22c55e"/>'
        + '<text x="55" y="100" fill="#86efac" font-size="7" text-anchor="middle">diff lengths</text>'
        + '</g>'
        + subtitle("branch length = time/change"))

    # Max likelihood
    w("max_likelihood", title("Maximum Likelihood")
        + ''.join([
            f'<g transform="translate({20+i*70},35)">'
            + '<line x1="5" y1="35" x2="20" y2="35" stroke="#60a5fa"/>'
            + '<line x1="20" y1="35" x2="40" y2="20" stroke="#60a5fa"/>'
            + '<line x1="20" y1="35" x2="40" y2="50" stroke="#60a5fa"/>'
            + f'<text x="30" y="70" fill="{c}" font-size="8" text-anchor="middle" font-weight="{ww}">lnL={v}</text>'
            + '</g>'
            for i,(v,c,ww) in enumerate([("-412","#94a3b8","400"),("-389","#fbbf24","700"),("-401","#94a3b8","400")])
        ])
        + '<circle cx="105" cy="55" r="28" fill="none" stroke="#22c55e" stroke-width="1.5" stroke-dasharray="3,2"/>'
        + label("BEST TREE", 120, 125, color="#22c55e", size=9, weight="700")
        + subtitle("highest likelihood wins"))

    # Rooting tree
    w("rooting_tree", title("Rooting a Tree")
        + '<g transform="translate(15,30)">'
        + '<polygon points="20,40 50,20 80,25 85,55 55,70 25,60" fill="none" stroke="#60a5fa" stroke-width="1.5"/>'
        + ''.join([f'<circle cx="{x}" cy="{y}" r="3" fill="#93c5fd"/>' for x,y in [(20,40),(50,20),(80,25),(85,55),(55,70),(25,60)]])
        + '<text x="55" y="95" fill="#93c5fd" font-size="7" text-anchor="middle">unrooted</text>'
        + '</g>'
        + '<line x1="110" y1="75" x2="130" y2="75" stroke="#fbbf24" marker-end="url(#rt1)"/>'
        + '<defs><marker id="rt1" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0,0 6,3 0,6" fill="#fbbf24"/></marker></defs>'
        + label("outgroup", 120, 65, color="#fbbf24", size=7)
        + '<g transform="translate(140,30)">'
        + '<line x1="0" y1="45" x2="20" y2="45" stroke="#ef4444" stroke-width="2"/>'
        + '<line x1="20" y1="45" x2="45" y2="25" stroke="#22c55e" stroke-width="1.5"/>'
        + '<line x1="20" y1="45" x2="45" y2="65" stroke="#22c55e" stroke-width="1.5"/>'
        + '<line x1="45" y1="25" x2="85" y2="20" stroke="#22c55e" stroke-width="1.5"/>'
        + '<line x1="45" y1="25" x2="85" y2="35" stroke="#22c55e" stroke-width="1.5"/>'
        + '<line x1="45" y1="65" x2="85" y2="60" stroke="#22c55e" stroke-width="1.5"/>'
        + '<line x1="45" y1="65" x2="85" y2="75" stroke="#22c55e" stroke-width="1.5"/>'
        + '<text x="50" y="95" fill="#86efac" font-size="7" text-anchor="middle">rooted</text>'
        + '</g>')

    # Character matrix
    w("character_matrix", title("Character Matrix")
        + '<rect x="30" y="30" width="180" height="95" fill="#1f2937" stroke="#475569"/>'
        + '<rect x="110" y="30" width="25" height="95" fill="#22c55e" opacity="0.15"/>'
        + ''.join([label(h, 60+i*25, 42, color="#fde68a", size=7, weight="700") for i,h in enumerate(["c1","c2","c3","c4","c5"])])
        + ''.join([
            label(tax, 40, 58+i*14, color="#e5e7eb", size=7, anchor="start", weight=("700" if i==0 else "400"))
            + ''.join([label(str(v), 60+j*25, 58+i*14, color=("#86efac" if j==2 and v==1 and i>0 else "#e5e7eb"), size=7) for j,v in enumerate(row)])
            for i,(tax,row) in enumerate([("OUT",[0,0,0,0,0]),("A",[1,0,1,0,0]),("B",[1,1,1,1,0]),("C",[1,1,1,1,1]),("D",[1,1,1,0,0])])
        ])
        + label("synapomorphy", 122, 138, color="#22c55e", size=8, weight="700"))

    # Transitional fossil
    w("transitional_fossil", title("Transitional Fossil")
        + '<g transform="translate(15,55)">'
        + '<ellipse cx="25" cy="15" rx="22" ry="8" fill="#60a5fa"/>'
        + '<polygon points="45,15 55,5 55,25" fill="#60a5fa"/>'
        + '<circle cx="10" cy="13" r="1.5" fill="#0a1220"/>'
        + '<text x="25" y="40" fill="#93c5fd" font-size="7" text-anchor="middle">fish</text>'
        + '</g>'
        + '<line x1="65" y1="75" x2="85" y2="75" stroke="#fbbf24" marker-end="url(#tf1)"/>'
        + '<defs><marker id="tf1" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0,0 6,3 0,6" fill="#fbbf24"/></marker></defs>'
        + '<g transform="translate(90,50)">'
        + '<ellipse cx="30" cy="20" rx="28" ry="9" fill="#fbbf24"/>'
        + '<polygon points="55,20 62,12 62,28" fill="#fbbf24"/>'
        + '<rect x="18" y="28" width="4" height="8" fill="#fbbf24"/>'
        + '<rect x="38" y="28" width="4" height="8" fill="#fbbf24"/>'
        + '<text x="30" y="50" fill="#fde68a" font-size="7" text-anchor="middle" font-weight="700">Tiktaalik</text>'
        + '</g>'
        + '<line x1="160" y1="75" x2="180" y2="75" stroke="#fbbf24" marker-end="url(#tf1)"/>'
        + '<g transform="translate(182,55)">'
        + '<ellipse cx="25" cy="15" rx="20" ry="7" fill="#22c55e"/>'
        + '<line x1="12" y1="20" x2="10" y2="30" stroke="#22c55e" stroke-width="3"/>'
        + '<line x1="22" y1="20" x2="22" y2="32" stroke="#22c55e" stroke-width="3"/>'
        + '<line x1="32" y1="20" x2="34" y2="32" stroke="#22c55e" stroke-width="3"/>'
        + '<line x1="42" y1="20" x2="45" y2="30" stroke="#22c55e" stroke-width="3"/>'
        + '<text x="25" y="45" fill="#86efac" font-size="7" text-anchor="middle">tetrapod</text>'
        + '</g>'
        + subtitle("intermediate form"))

    # Phylo classification
    w("phylo_classification", title("Linnaean vs Phylogenetic")
        + '<g transform="translate(10,30)">'
        + ''.join([f'<line x1="0" y1="{10+i*12}" x2="100" y2="{10+i*12}" stroke="#94a3b8" stroke-width="0.5"/>' for i in range(6)])
        + ''.join([f'<text x="5" y="{17+i*12}" fill="#fca5a5" font-size="6" text-anchor="start">{t}</text>' for i,t in enumerate(["Kingdom","Phylum","Class","Order","Family","Genus"])])
        + '<text x="50" y="100" fill="#fca5a5" font-size="8" text-anchor="middle" font-weight="700">Linnaean</text>'
        + '</g>'
        + '<g transform="translate(130,30)">'
        + '<line x1="0" y1="45" x2="15" y2="45" stroke="#22c55e"/>'
        + '<line x1="15" y1="45" x2="35" y2="25" stroke="#22c55e"/>'
        + '<line x1="15" y1="45" x2="35" y2="65" stroke="#22c55e"/>'
        + '<line x1="35" y1="25" x2="70" y2="15" stroke="#22c55e"/>'
        + '<line x1="35" y1="25" x2="70" y2="35" stroke="#22c55e"/>'
        + '<line x1="35" y1="65" x2="70" y2="55" stroke="#22c55e"/>'
        + '<line x1="35" y1="65" x2="70" y2="75" stroke="#22c55e"/>'
        + '<text x="45" y="100" fill="#86efac" font-size="8" text-anchor="middle" font-weight="700">Phylogenetic</text>'
        + '</g>')

# ============================================================
# GROUP C: SPECIATION
# ============================================================

def group_c():
    # BSC
    w("bsc", title("Biological Species Concept")
        + '<rect x="20" y="30" width="200" height="30" fill="#1f2937" stroke="#fbbf24"/>'
        + label("Can they produce FERTILE offspring?", 120, 50, color="#fde68a", size=9)
        + '<line x1="120" y1="60" x2="70" y2="80" stroke="#22c55e" stroke-width="1.5" marker-end="url(#bs1)"/>'
        + '<line x1="120" y1="60" x2="170" y2="80" stroke="#ef4444" stroke-width="1.5" marker-end="url(#bs1)"/>'
        + '<defs><marker id="bs1" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0,0 6,3 0,6" fill="#fbbf24"/></marker></defs>'
        + label("YES", 70, 75, color="#22c55e", size=9, weight="700")
        + '<rect x="30" y="85" width="80" height="40" fill="#064e3b" stroke="#22c55e"/>'
        + label("SAME", 70, 102, color="#86efac", size=9, weight="700")
        + label("species", 70, 115, color="#86efac", size=8)
        + label("NO", 170, 75, color="#ef4444", size=9, weight="700")
        + '<rect x="130" y="85" width="80" height="40" fill="#7f1d1d" stroke="#ef4444"/>'
        + label("DIFFERENT", 170, 102, color="#fca5a5", size=9, weight="700")
        + label("species", 170, 115, color="#fca5a5", size=8))

    # Speciation 3-step
    w("speciation_3step", title("Speciation: 3 Steps")
        + ''.join([
            f'<g transform="translate({10+i*75},30)">'
            + f'<rect x="0" y="10" width="65" height="60" fill="#1f2937" stroke="{c}"/>'
            + content + '</g>'
            + f'<text x="{42+i*75}" y="125" fill="{c}" font-size="7" text-anchor="middle" font-weight="700">{lab}</text>'
            for i,(c,lab,content) in enumerate([
                ("#60a5fa","(1) one pop",
                  '<circle cx="20" cy="30" r="4" fill="#93c5fd"/><circle cx="35" cy="40" r="4" fill="#93c5fd"/><circle cx="50" cy="30" r="4" fill="#93c5fd"/><line x1="20" y1="30" x2="50" y2="30" stroke="#93c5fd" stroke-width="0.5" stroke-dasharray="1,1"/><text x="32" y="60" fill="#93c5fd" font-size="6" text-anchor="middle">gene flow</text>'),
                ("#fbbf24","(2) barrier",
                  '<circle cx="15" cy="35" r="4" fill="#93c5fd"/><line x1="32" y1="10" x2="32" y2="70" stroke="#fbbf24" stroke-width="2"/><circle cx="50" cy="35" r="4" fill="#93c5fd"/><text x="32" y="60" fill="#fbbf24" font-size="6" text-anchor="middle">isolated</text>'),
                ("#ef4444","(3) isolation",
                  '<circle cx="15" cy="35" r="4" fill="#60a5fa"/><line x1="32" y1="10" x2="32" y2="70" stroke="#ef4444" stroke-width="2"/><circle cx="50" cy="35" r="4" fill="#a78bfa"/><text x="32" y="60" fill="#fca5a5" font-size="6" text-anchor="middle">RI locked</text>'),
            ])
        ]))

    # Prezygotic
    w("prezygotic", title("Prezygotic Barriers")
        + '<rect x="20" y="25" width="200" height="18" fill="#1f2937" stroke="#fbbf24"/>'
        + label("MATING ATTEMPT", 120, 38, color="#fde68a", size=9, weight="700")
        + '<line x1="120" y1="43" x2="120" y2="55" stroke="#fbbf24" stroke-width="1" marker-end="url(#pz1)"/>'
        + '<defs><marker id="pz1" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0,0 6,3 0,6" fill="#fbbf24"/></marker></defs>'
        + ''.join([f'<rect x="{10+i*46}" y="58" width="42" height="30" fill="#1e3a5f" stroke="#60a5fa"/><text x="{31+i*46}" y="73" fill="#93c5fd" font-size="7" text-anchor="middle">{t}</text><text x="{31+i*46}" y="83" fill="#93c5fd" font-size="7" text-anchor="middle">{t2}</text>' for i,(t,t2) in enumerate([("habitat",""),("temporal",""),("behav.",""),("mech.",""),("gametic","")])])
        + '<line x1="120" y1="90" x2="120" y2="105" stroke="#ef4444" stroke-width="1.5" marker-end="url(#pz1)"/>'
        + '<rect x="60" y="108" width="120" height="28" fill="#7f1d1d" stroke="#ef4444"/>'
        + label("blocks fertilization", 120, 127, color="#fca5a5", size=9, weight="700"))

    # Postzygotic
    w("postzygotic", title("Postzygotic Barriers")
        + '<circle cx="120" cy="40" r="12" fill="#fbbf24"/>'
        + '<circle cx="115" cy="38" r="3" fill="#ef4444"/>'
        + '<circle cx="125" cy="42" r="3" fill="#60a5fa"/>'
        + label("zygote", 120, 44, color="#0a1220", size=7, weight="700")
        + '<line x1="120" y1="55" x2="120" y2="70" stroke="#fbbf24" marker-end="url(#po1)"/>'
        + '<defs><marker id="po1" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0,0 6,3 0,6" fill="#fbbf24"/></marker></defs>'
        + '<rect x="20" y="75" width="90" height="30" fill="#1f2937" stroke="#ef4444"/>'
        + label("hybrid inviability", 65, 90, color="#fca5a5", size=8)
        + label("(dies)", 65, 100, color="#fca5a5", size=7)
        + '<rect x="130" y="75" width="90" height="30" fill="#1f2937" stroke="#ef4444"/>'
        + label("hybrid sterility", 175, 90, color="#fca5a5", size=8)
        + label("(mule)", 175, 100, color="#fca5a5", size=7)
        + subtitle("after fertilization"))

    # Mule sterility
    w("mule_sterility", title("Mule Sterility")
        + '<g transform="translate(15,30)"><ellipse cx="30" cy="30" rx="22" ry="14" fill="#8b6f47"/><rect x="15" y="38" width="4" height="15" fill="#8b6f47"/><rect x="45" y="38" width="4" height="15" fill="#8b6f47"/><text x="30" y="65" fill="#fde68a" font-size="7" text-anchor="middle">Horse</text><text x="30" y="75" fill="#94a3b8" font-size="7" text-anchor="middle">2n=64</text></g>'
        + '<text x="95" y="65" fill="#fbbf24" font-size="12" text-anchor="middle">x</text>'
        + '<g transform="translate(110,30)"><ellipse cx="30" cy="30" rx="20" ry="12" fill="#6b5840"/><rect x="15" y="38" width="4" height="15" fill="#6b5840"/><rect x="45" y="38" width="4" height="15" fill="#6b5840"/><text x="30" y="65" fill="#fde68a" font-size="7" text-anchor="middle">Donkey</text><text x="30" y="75" fill="#94a3b8" font-size="7" text-anchor="middle">2n=62</text></g>'
        + '<line x1="140" y1="50" x2="175" y2="50" stroke="#fbbf24" marker-end="url(#ms1)"/>'
        + '<defs><marker id="ms1" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0,0 6,3 0,6" fill="#fbbf24"/></marker></defs>'
        + '<g transform="translate(180,30)"><ellipse cx="25" cy="30" rx="20" ry="13" fill="#7a5c3e"/><rect x="12" y="38" width="4" height="15" fill="#7a5c3e"/><rect x="38" y="38" width="4" height="15" fill="#7a5c3e"/><text x="25" y="65" fill="#fde68a" font-size="7" text-anchor="middle">Mule</text><text x="25" y="75" fill="#94a3b8" font-size="7" text-anchor="middle">2n=63</text></g>'
        + '<rect x="60" y="105" width="120" height="28" fill="#7f1d1d" stroke="#ef4444"/>'
        + label("meiosis fails -> STERILE", 120, 123, color="#fca5a5", size=9, weight="700"))

    # Allopatric
    w("allopatric", title("Allopatric Speciation")
        + '<path d="M 30 90 L 80 50 L 130 90 L 110 95 L 80 65 L 50 95 Z" fill="#6b7280" stroke="#94a3b8"/>'
        + '<path d="M 110 90 L 160 50 L 210 90 L 190 95 L 160 65 L 130 95 Z" fill="#6b7280" stroke="#94a3b8"/>'
        + '<circle cx="60" cy="105" r="8" fill="#60a5fa"/>'
        + label("A", 60, 108, color="#0a1220", size=8, weight="700")
        + '<circle cx="180" cy="105" r="8" fill="#a78bfa"/>'
        + label("B", 180, 108, color="#0a1220", size=8, weight="700")
        + '<path d="M 100 110 Q 120 125 140 110" stroke="#93c5fd" stroke-width="2" fill="none"/>'
        + label("river/mountain barrier", 120, 135, color="#93c5fd", size=7)
        + subtitle("geographic separation", y=145))

    # Sympatric
    w("sympatric", title("Sympatric Speciation")
        + '<rect x="30" y="35" width="180" height="70" fill="#1e3a5f" stroke="#60a5fa" opacity="0.3"/>'
        + label("same habitat", 120, 48, color="#93c5fd", size=8)
        + '<rect x="50" y="60" width="40" height="15" fill="#22c55e"/>'
        + label("host A", 70, 70, color="#0a1220", size=7, weight="700")
        + '<rect x="150" y="60" width="40" height="15" fill="#fbbf24"/>'
        + label("host B", 170, 70, color="#0a1220", size=7, weight="700")
        + ''.join([f'<circle cx="{x}" cy="{y}" r="3" fill="#60a5fa"/>' for x,y in [(60,88),(75,90),(68,95)]])
        + ''.join([f'<circle cx="{x}" cy="{y}" r="3" fill="#a78bfa"/>' for x,y in [(160,88),(175,90),(168,95)]])
        + label("specialize -> diverge", 120, 122, color="#fde68a", size=8))

    # Reinforcement
    w("reinforcement", title("Reinforcement")
        + '<circle cx="70" cy="75" r="28" fill="#60a5fa" opacity="0.3" stroke="#60a5fa"/>'
        + '<circle cx="170" cy="75" r="28" fill="#a78bfa" opacity="0.3" stroke="#a78bfa"/>'
        + '<ellipse cx="120" cy="75" rx="28" ry="25" fill="#fbbf24" opacity="0.25" stroke="#fbbf24"/>'
        + label("A", 60, 78, color="#93c5fd", size=10, weight="700")
        + label("B", 180, 78, color="#c4b5fd", size=10, weight="700")
        + label("hybrid", 120, 72, color="#fde68a", size=8)
        + label("zone", 120, 82, color="#fde68a", size=7)
        + '<text x="120" y="115" fill="#ef4444" font-size="8" text-anchor="middle" font-weight="700">low fitness hybrids</text>'
        + label("-> prezygotic barriers strengthen", 120, 138, color="#fca5a5", size=7))

    # BDM
    w("bdm", title("Bateson-Dobzhansky-Muller")
        + '<rect x="20" y="35" width="65" height="40" fill="#1f2937" stroke="#60a5fa"/>'
        + label("Genome A", 52, 48, color="#93c5fd", size=8)
        + label("allele A1", 52, 62, color="#e5e7eb", size=7)
        + label("OK", 52, 72, color="#22c55e", size=7, weight="700")
        + '<rect x="155" y="35" width="65" height="40" fill="#1f2937" stroke="#a78bfa"/>'
        + label("Genome B", 188, 48, color="#c4b5fd", size=8)
        + label("allele B2", 188, 62, color="#e5e7eb", size=7)
        + label("OK", 188, 72, color="#22c55e", size=7, weight="700")
        + '<line x1="85" y1="95" x2="100" y2="110" stroke="#fbbf24"/>'
        + '<line x1="155" y1="95" x2="140" y2="110" stroke="#fbbf24"/>'
        + '<rect x="75" y="110" width="90" height="30" fill="#7f1d1d" stroke="#ef4444"/>'
        + label("A1 + B2 hybrid", 120, 124, color="#fca5a5", size=8)
        + label("INCOMPATIBLE", 120, 135, color="#ef4444", size=8, weight="700"))

    # Allopolyploidy
    w("allopolyploidy", title("Allopolyploidy")
        + '<rect x="10" y="30" width="50" height="25" fill="#1e3a5f" stroke="#60a5fa"/>'
        + label("A (2n=4)", 35, 46, color="#93c5fd", size=7)
        + '<text x="70" y="46" fill="#fbbf24" font-size="11">x</text>'
        + '<rect x="80" y="30" width="50" height="25" fill="#4c1d95" stroke="#a78bfa"/>'
        + label("B (2n=6)", 105, 46, color="#c4b5fd", size=7)
        + '<line x1="70" y1="60" x2="70" y2="70" stroke="#fbbf24" marker-end="url(#ap1)"/>'
        + '<defs><marker id="ap1" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0,0 6,3 0,6" fill="#fbbf24"/></marker></defs>'
        + '<rect x="25" y="72" width="90" height="22" fill="#7f1d1d" stroke="#ef4444"/>'
        + label("sterile hybrid (n=5)", 70, 87, color="#fca5a5", size=7)
        + '<line x1="140" y1="85" x2="160" y2="85" stroke="#fbbf24" marker-end="url(#ap1)"/>'
        + label("2x", 150, 78, color="#fbbf24", size=7)
        + '<rect x="165" y="72" width="70" height="22" fill="#064e3b" stroke="#22c55e"/>'
        + label("fertile 2n=10", 200, 87, color="#86efac", size=7)
        + label("chromosome doubling -> new species", 120, 115, color="#fde68a", size=7))

    # Peripatric
    w("peripatric", title("Peripatric Speciation")
        + '<ellipse cx="80" cy="80" rx="55" ry="35" fill="#1e3a5f" stroke="#60a5fa"/>'
        + label("mainland (large)", 80, 85, color="#93c5fd", size=8)
        + ''.join([f'<circle cx="{x}" cy="{y}" r="2" fill="#60a5fa"/>' for x,y in [(55,65),(70,75),(90,70),(105,80),(60,95),(95,95),(80,55),(100,60)]])
        + '<circle cx="185" cy="65" r="15" fill="#4c1d95" stroke="#a78bfa"/>'
        + label("colony", 185, 69, color="#c4b5fd", size=7)
        + '<circle cx="180" cy="60" r="2" fill="#a78bfa"/>'
        + '<circle cx="190" cy="68" r="2" fill="#a78bfa"/>'
        + '<line x1="135" y1="75" x2="170" y2="65" stroke="#fbbf24" stroke-dasharray="2,1"/>'
        + label("founders", 155, 58, color="#fbbf24", size=6)
        + label("drift + selection -> fast divergence", 120, 125, color="#fde68a", size=7))

    # Hybrid zone
    w("hybrid_zone", title("Hybrid Zone")
        + '<rect x="20" y="50" width="80" height="50" fill="#60a5fa" opacity="0.4"/>'
        + '<rect x="140" y="50" width="80" height="50" fill="#a78bfa" opacity="0.4"/>'
        + '<rect x="80" y="50" width="80" height="50" fill="url(#hzg)" opacity="0.5"/>'
        + '<defs><linearGradient id="hzg" x1="0" x2="1"><stop offset="0" stop-color="#60a5fa"/><stop offset="1" stop-color="#a78bfa"/></linearGradient></defs>'
        + label("Species A", 55, 78, color="#93c5fd", size=8)
        + label("hybrids", 120, 78, color="#fde68a", size=8)
        + label("Species B", 180, 78, color="#c4b5fd", size=8)
        + ''.join([f'<circle cx="{x}" cy="95" r="2.5" fill="{c}"/>' for x,c in [(40,"#60a5fa"),(60,"#60a5fa"),(90,"#7c8ce0"),(115,"#8a7fd4"),(140,"#9478c9"),(170,"#a78bfa"),(195,"#a78bfa")]])
        + subtitle("gradient of intermediates"))

    # Character displacement
    w("character_displacement", title("Character Displacement")
        + label("BEFORE (allopatric)", 120, 30, color="#94a3b8", size=8)
        + '<path d="M 30 55 Q 60 40 90 55 Q 60 65 30 55" fill="#60a5fa" opacity="0.5"/>'
        + '<path d="M 60 55 Q 90 40 120 55 Q 90 65 60 55" fill="#a78bfa" opacity="0.5"/>'
        + label("overlap", 75, 58, color="#fde68a", size=7)
        + label("AFTER (sympatric)", 120, 90, color="#94a3b8", size=8)
        + '<path d="M 20 110 Q 45 95 70 110 Q 45 120 20 110" fill="#60a5fa" opacity="0.5"/>'
        + '<path d="M 140 110 Q 170 95 200 110 Q 170 120 140 110" fill="#a78bfa" opacity="0.5"/>'
        + label("diverged", 110, 130, color="#22c55e", size=8, weight="700")
        + subtitle("reduced competition"))

    # Tempo evolution
    w("tempo_evolution", title("Tempo of Evolution")
        + '<g transform="translate(5,25)"><line x1="10" y1="80" x2="100" y2="80" stroke="#475569"/><line x1="10" y1="20" x2="10" y2="80" stroke="#475569"/><path d="M 10 75 L 30 60 L 60 40 L 90 25" fill="none" stroke="#60a5fa" stroke-width="2"/><text x="55" y="100" fill="#93c5fd" font-size="7" text-anchor="middle">gradualism</text></g>'
        + '<g transform="translate(125,25)"><line x1="10" y1="80" x2="100" y2="80" stroke="#475569"/><line x1="10" y1="20" x2="10" y2="80" stroke="#475569"/><path d="M 10 70 L 30 70 L 32 45 L 60 45 L 62 25 L 90 25" fill="none" stroke="#a78bfa" stroke-width="2"/><text x="55" y="100" fill="#c4b5fd" font-size="7" text-anchor="middle">punctuated</text></g>'
        + subtitle("smooth vs stasis+jumps"))

    # Parapatric
    w("parapatric", title("Parapatric Speciation")
        + '<rect x="20" y="50" width="95" height="50" fill="#1e3a5f" stroke="#60a5fa"/>'
        + '<rect x="125" y="50" width="95" height="50" fill="#7c4827" stroke="#fbbf24"/>'
        + label("wet", 65, 75, color="#93c5fd", size=8)
        + label("dry", 170, 75, color="#fde68a", size=8)
        + ''.join([f'<circle cx="{x}" cy="85" r="3" fill="{c}"/>' for x,c in [(40,"#60a5fa"),(70,"#60a5fa"),(100,"#7c8ce0"),(120,"#8ab078"),(150,"#86efac"),(190,"#22c55e")]])
        + '<line x1="120" y1="45" x2="120" y2="105" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="2,2"/>'
        + label("selection gradient", 120, 125, color="#ef4444", size=7)
        + subtitle("adjacent, no barrier"))

    # Temporal isolation
    w("temporal_isolation", title("Temporal Isolation")
        + '<rect x="20" y="35" width="200" height="30" fill="#1f2937" stroke="#60a5fa"/>'
        + ''.join([f'<line x1="{30+i*16}" y1="35" x2="{30+i*16}" y2="65" stroke="#475569" stroke-width="0.5"/>' for i in range(12)])
        + ''.join([f'<text x="{38+i*16}" y="32" fill="#94a3b8" font-size="6" text-anchor="middle">{m}</text>' for i,m in enumerate(["J","F","M","A","M","J","J","A","S","O","N","D"])])
        + '<rect x="60" y="42" width="30" height="10" fill="#60a5fa"/>'
        + label("Species A: April", 75, 80, color="#93c5fd", size=7)
        + '<rect x="160" y="52" width="30" height="10" fill="#a78bfa"/>'
        + label("Species B: Sept", 175, 80, color="#c4b5fd", size=7)
        + label("no overlap -> no mating", 120, 115, color="#fde68a", size=8))

    # Gametic incompatibility
    w("gametic_incompatibility", title("Gametic Incompatibility")
        + '<circle cx="75" cy="80" r="28" fill="#fbbf24" opacity="0.6"/>'
        + label("egg", 75, 82, color="#0a1220", size=8, weight="700")
        + ''.join([f'<path d="M {75+28*math.cos(a):.1f} {80+28*math.sin(a):.1f} l {3*math.cos(a):.1f} {3*math.sin(a):.1f}" stroke="#fbbf24" stroke-width="2"/>' for a in [0,0.6,1.2,1.8,2.4,3.0,3.6,4.2,4.8,5.4]])
        + '<g transform="translate(160,70)"><circle cx="10" cy="10" r="8" fill="#60a5fa"/><line x1="18" y1="10" x2="40" y2="10" stroke="#60a5fa" stroke-width="2"/><polygon points="10,2 13,5 10,8 7,5" fill="#93c5fd"/></g>'
        + '<line x1="140" y1="115" x2="155" y2="130" stroke="#ef4444" stroke-width="2"/>'
        + '<line x1="155" y1="115" x2="140" y2="130" stroke="#ef4444" stroke-width="2"/>'
        + label("sperm proteins", 175, 110, color="#93c5fd", size=7)
        + label("don't match", 175, 122, color="#ef4444", size=7, weight="700")
        + subtitle("lock-and-key fails"))

# ============================================================
# GROUP D: BIOGEOGRAPHY
# ============================================================

def group_d():
    # Continental drift
    w("continental_drift", title("Continental Drift")
        + ''.join([
            f'<g transform="translate({5+i*60},30)">'
            + f'<rect x="0" y="5" width="55" height="55" fill="#1e3a5f" stroke="#60a5fa" opacity="0.4"/>'
            + shape
            + f'<text x="27" y="78" fill="#fde68a" font-size="7" text-anchor="middle">{lab}</text>'
            + '</g>'
            for i,(shape,lab) in enumerate([
                ('<path d="M 10 15 Q 25 10 40 15 Q 48 30 40 45 Q 25 50 10 45 Q 5 30 10 15 Z" fill="#22c55e" stroke="#86efac"/>',"Pangaea 300"),
                ('<path d="M 8 15 Q 22 12 35 20 L 33 35 Q 22 40 10 35 Z" fill="#22c55e"/><path d="M 38 25 Q 48 30 45 45 L 38 45 Z" fill="#22c55e"/>',"split 200"),
                ('<path d="M 5 15 L 15 12 L 18 28 L 10 35 Z" fill="#22c55e"/><path d="M 25 20 L 35 18 L 38 32 L 28 38 Z" fill="#22c55e"/><path d="M 42 15 L 52 20 L 50 40 L 42 40 Z" fill="#22c55e"/>',"near-mod 65"),
                ('<path d="M 5 18 L 12 15 L 14 30 L 8 35 Z" fill="#22c55e"/><path d="M 20 20 L 30 18 L 32 40 L 22 45 Z" fill="#22c55e"/><path d="M 40 15 L 52 18 L 50 42 L 42 42 Z" fill="#22c55e"/>',"today"),
            ])
        ]))

    # Vicariance
    w("vicariance", title("Vicariance")
        + '<rect x="20" y="35" width="200" height="55" fill="#1e3a5f" stroke="#60a5fa" opacity="0.4"/>'
        + '<line x1="120" y1="35" x2="120" y2="90" stroke="#fbbf24" stroke-width="3"/>'
        + '<polygon points="115,35 125,35 120,28" fill="#fbbf24"/>'
        + label("barrier", 120, 25, color="#fbbf24", size=7)
        + ''.join([f'<circle cx="{x}" cy="{y}" r="4" fill="#60a5fa"/>' for x,y in [(50,55),(75,75),(95,55)]])
        + ''.join([f'<circle cx="{x}" cy="{y}" r="4" fill="#a78bfa"/>' for x,y in [(145,55),(170,75),(195,55)]])
        + label("stays", 60, 105, color="#93c5fd", size=7)
        + label("stays", 170, 105, color="#c4b5fd", size=7)
        + label("barrier forms AROUND stationary orgs", 120, 125, color="#fde68a", size=7))

    # Dispersal bio
    w("dispersal_bio", title("Dispersal")
        + '<path d="M 15 90 Q 25 75 50 80 Q 70 90 50 100 Q 25 105 15 90 Z" fill="#22c55e" opacity="0.6"/>'
        + '<path d="M 170 70 Q 195 60 215 70 Q 220 85 200 95 Q 180 90 170 70 Z" fill="#22c55e" opacity="0.6"/>'
        + label("mainland", 35, 120, color="#86efac", size=7)
        + label("island", 195, 110, color="#86efac", size=7)
        + ''.join([f'<path d="M 60 75 Q 110 40 170 70" stroke="#3b82f6" fill="none" stroke-width="0.4" stroke-dasharray="2,3"/>' for _ in [0]])
        + '<path d="M 60 75 Q 110 40 170 70" stroke="#fbbf24" fill="none" stroke-width="1.5" marker-end="url(#di1)"/>'
        + '<defs><marker id="di1" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0,0 6,3 0,6" fill="#fbbf24"/></marker></defs>'
        + '<circle cx="115" cy="50" r="4" fill="#60a5fa"/>'
        + label("organism crosses barrier", 120, 135, color="#fde68a", size=8))

    # Island biogeography
    w("island_biogeography", title("Island Biogeography")
        + '<line x1="30" y1="120" x2="220" y2="120" stroke="#475569"/>'
        + '<line x1="30" y1="30" x2="30" y2="120" stroke="#475569"/>'
        + '<path d="M 30 40 Q 100 90 220 115" fill="none" stroke="#22c55e" stroke-width="2"/>'
        + '<path d="M 30 115 Q 100 90 220 40" fill="none" stroke="#ef4444" stroke-width="2"/>'
        + '<circle cx="125" cy="90" r="5" fill="#fbbf24"/>'
        + label("S*", 140, 93, color="#fde68a", size=8, anchor="start", weight="700")
        + label("immigration", 90, 50, color="#86efac", size=7)
        + label("extinction", 180, 55, color="#fca5a5", size=7)
        + label("# species", 22, 40, color="#94a3b8", size=7)
        + subtitle("equilibrium at crossing"))

    # Adaptive radiation
    w("adaptive_radiation", title("Adaptive Radiation")
        + '<circle cx="40" cy="85" r="5" fill="#fbbf24"/>'
        + label("ancestor", 40, 105, color="#fde68a", size=7)
        + ''.join([
            f'<line x1="45" y1="85" x2="{180}" y2="{25+i*17}" stroke="#60a5fa" stroke-width="1"/>'
            + beak
            + f'<text x="230" y="{28+i*17}" fill="#e5e7eb" font-size="6" text-anchor="end">{n}</text>'
            for i,(beak,n) in enumerate([
                ('<path d="M 185 22 L 195 20 L 195 28 Z" fill="#fbbf24"/>',"seed"),
                ('<path d="M 185 39 L 200 38 L 200 42 Z" fill="#fbbf24"/>',"insect"),
                ('<path d="M 185 56 L 198 54 L 195 60 Z" fill="#fbbf24"/>',"fruit"),
                ('<path d="M 185 73 L 205 73 L 185 76 Z" fill="#fbbf24"/>',"nectar"),
                ('<path d="M 185 90 L 195 87 L 196 93 Z" fill="#fbbf24"/>',"bud"),
                ('<path d="M 185 107 L 197 106 L 193 111 Z" fill="#fbbf24"/>',"tool"),
                ('<path d="M 185 124 L 192 122 L 194 127 Z" fill="#fbbf24"/>',"grub"),
                ('<path d="M 185 140 L 193 138 L 195 143 Z" fill="#fbbf24"/>',"cactus"),
            ])
        ]))

    # Wallace line
    w("wallace_line", title("Wallace Line")
        + '<rect x="20" y="35" width="200" height="80" fill="#1e3a5f" opacity="0.4"/>'
        + '<path d="M 30 50 Q 60 45 90 55 Q 100 65 90 75" fill="#6b4423"/>'
        + '<path d="M 100 55 L 110 55 L 110 70 L 100 70 Z" fill="#6b4423"/>'
        + label("Bali", 105, 63, color="#fde68a", size=5)
        + '<line x1="115" y1="40" x2="115" y2="110" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,2"/>'
        + '<path d="M 120 55 L 130 55 L 130 70 L 120 70 Z" fill="#6b4423"/>'
        + label("Lombok", 125, 80, color="#fde68a", size=5)
        + '<path d="M 140 55 Q 180 45 210 70 L 180 90 Q 150 75 140 55" fill="#6b4423"/>'
        + label("Asian fauna", 65, 108, color="#93c5fd", size=7)
        + label("Australian", 180, 108, color="#c4b5fd", size=7)
        + label("Wallace", 115, 32, color="#ef4444", size=7, weight="700"))

    # Species area
    w("species_area", title("Species-Area Curve")
        + '<line x1="30" y1="120" x2="220" y2="120" stroke="#475569"/>'
        + '<line x1="30" y1="30" x2="30" y2="120" stroke="#475569"/>'
        + '<line x1="30" y1="115" x2="215" y2="40" stroke="#60a5fa" stroke-width="2"/>'
        + ''.join([f'<circle cx="{30+i*45}" cy="{115-i*18.5}" r="3" fill="#fbbf24"/>' for i in range(5)])
        + label("log S", 20, 40, color="#93c5fd", size=7)
        + label("log A", 210, 135, color="#93c5fd", size=7)
        + label("S = cA^z", 140, 65, color="#fde68a", size=9, weight="700")
        + subtitle("power law"))

    # Standing diversity
    w("standing_diversity", title("Standing Diversity")
        + '<rect x="30" y="50" width="180" height="35" fill="#1f2937" stroke="#fbbf24"/>'
        + label("D\u2082 = D\u2081 + Orig - Ext", 120, 72, color="#fde68a", size=10, weight="700")
        + '<line x1="30" y1="105" x2="210" y2="105" stroke="#475569"/>'
        + '<line x1="30" y1="100" x2="30" y2="110" stroke="#475569"/>'
        + '<line x1="210" y1="100" x2="210" y2="110" stroke="#475569"/>'
        + label("t\u2081", 30, 122, color="#94a3b8", size=8)
        + label("t\u2082", 210, 122, color="#94a3b8", size=8)
        + '<line x1="80" y1="100" x2="80" y2="110" stroke="#22c55e" stroke-width="2"/>'
        + label("+ orig", 80, 122, color="#86efac", size=7)
        + '<line x1="160" y1="100" x2="160" y2="110" stroke="#ef4444" stroke-width="2"/>'
        + label("- ext", 160, 122, color="#fca5a5", size=7))

    # Big 5
    w("big5", title("Big 5 Extinctions")
        + '<line x1="25" y1="125" x2="225" y2="125" stroke="#475569"/>'
        + '<line x1="25" y1="30" x2="25" y2="125" stroke="#475569"/>'
        + ''.join([
            f'<line x1="{x}" y1="125" x2="{x}" y2="{125-h}" stroke="#ef4444" stroke-width="3"/>'
            + f'<text x="{x}" y="{120-h}" fill="{fc}" font-size="6" text-anchor="middle">{lab}</text>'
            for x,h,lab,fc in [(55,45,"O 86%","#fca5a5"),(90,55,"D 75%","#fca5a5"),(130,85,"P 96%","#ef4444"),(170,50,"Tr 80%","#fca5a5"),(210,65,"K 76%","#fca5a5")]
        ])
        + label("600 mya", 28, 140, color="#94a3b8", size=7)
        + label("now", 225, 140, color="#94a3b8", size=7, anchor="end")
        + label("intensity", 20, 40, color="#93c5fd", size=7))

    # Metapopulation
    w("metapopulation", title("Metapopulation")
        + ''.join([
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" stroke="#60a5fa" stroke-width="1"/>'
            for x,y,r,c in [(60,60,14,"#1e3a5f"),(120,50,12,"#1e3a5f"),(180,70,15,"#064e3b"),(70,100,13,"#1f2937"),(140,105,14,"#064e3b"),(195,110,11,"#1f2937")]
        ])
        + ''.join([f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#fbbf24" stroke-width="0.8" marker-end="url(#mp1)"/>' for x1,y1,x2,y2 in [(70,62,110,50),(130,52,170,68),(75,98,130,103),(155,103,185,108),(70,75,130,100)]])
        + '<defs><marker id="mp1" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto"><polygon points="0,0 5,2.5 0,5" fill="#fbbf24"/></marker></defs>'
        + label("occupied", 30, 140, color="#86efac", size=7, anchor="start")
        + label("empty", 155, 140, color="#94a3b8", size=7))

    # Gondwana Laurasia
    w("gondwana_laurasia", title("Gondwana & Laurasia")
        + '<path d="M 30 40 Q 120 35 210 45 L 210 75 Q 120 70 30 75 Z" fill="#60a5fa" opacity="0.6" stroke="#93c5fd"/>'
        + label("LAURASIA (north)", 120, 62, color="#0a1220", size=8, weight="700")
        + '<path d="M 30 85 Q 120 80 210 90 L 210 120 Q 120 115 30 120 Z" fill="#22c55e" opacity="0.6" stroke="#86efac"/>'
        + label("GONDWANA (south)", 120, 107, color="#0a1220", size=8, weight="700")
        + '<text x="50" y="55" font-size="9">\U0001F98C</text>'
        + '<text x="180" y="55" font-size="9">\U0001F43B</text>'
        + '<text x="50" y="103" font-size="9">\U0001F998</text>'
        + '<text x="180" y="103" font-size="9">\U0001F99C</text>'
        + subtitle("Pangaea split"))

    # Vicariance vs dispersal
    w("vicariance_vs_dispersal", title("Vicariance vs Dispersal")
        + '<g transform="translate(5,25)"><rect x="5" y="10" width="100" height="60" fill="#1e3a5f" stroke="#60a5fa"/><circle cx="30" cy="40" r="3" fill="#60a5fa"/><circle cx="80" cy="40" r="3" fill="#60a5fa"/><line x1="55" y1="10" x2="55" y2="70" stroke="#fbbf24" stroke-width="2"/><text x="55" y="85" fill="#fbbf24" font-size="7" text-anchor="middle">vicariance</text><text x="55" y="95" fill="#94a3b8" font-size="6" text-anchor="middle">land moves</text></g>'
        + '<g transform="translate(125,25)"><rect x="5" y="10" width="45" height="60" fill="#064e3b"/><rect x="65" y="10" width="45" height="60" fill="#064e3b"/><circle cx="20" cy="40" r="3" fill="#a78bfa"/><path d="M 30 40 Q 57 25 80 40" stroke="#fbbf24" fill="none" marker-end="url(#vd1)"/><defs><marker id="vd1" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto"><polygon points="0,0 5,2.5 0,5" fill="#fbbf24"/></marker></defs><text x="55" y="85" fill="#fbbf24" font-size="7" text-anchor="middle">dispersal</text><text x="55" y="95" fill="#94a3b8" font-size="6" text-anchor="middle">organism moves</text></g>')

    # Endemism
    w("endemism", title("Endemism")
        + '<ellipse cx="120" cy="80" rx="70" ry="45" fill="#064e3b" stroke="#22c55e" stroke-width="1.5"/>'
        + ''.join([f'<circle cx="{x}" cy="{y}" r="5" fill="{c}"/>' for x,y,c in [(80,65,"#ef4444"),(110,55,"#fbbf24"),(145,70,"#a78bfa"),(100,90,"#60a5fa"),(140,95,"#22c55e")]])
        + label("island", 120, 45, color="#86efac", size=8)
        + label("found ONLY HERE", 120, 130, color="#fde68a", size=9, weight="700"))

    # Taxon cycle
    w("taxon_cycle", title("Taxon Cycle")
        + '<circle cx="120" cy="80" r="45" fill="none" stroke="#60a5fa" stroke-width="1" stroke-dasharray="3,2"/>'
        + ''.join([
            f'<circle cx="{120+45*math.cos(a):.1f}" cy="{80+45*math.sin(a):.1f}" r="18" fill="#1f2937" stroke="{c}"/>'
            + f'<text x="{120+45*math.cos(a):.1f}" y="{82+45*math.sin(a):.1f}" fill="{c}" font-size="6" text-anchor="middle">{t}</text>'
            for a,(c,t) in zip([-math.pi/2, 0, math.pi/2, math.pi], [("#22c55e","colonize"),("#fbbf24","expand"),("#fb923c","contract"),("#ef4444","extinct")])
        ])
        + ''.join([f'<polygon points="{120+52*math.cos(a):.1f},{80+52*math.sin(a):.1f} {120+55*math.cos(a+0.2):.1f},{80+55*math.sin(a+0.2):.1f} {120+48*math.cos(a+0.1):.1f},{80+48*math.sin(a+0.1):.1f}" fill="#fbbf24"/>' for a in [-math.pi/4, math.pi/4, 3*math.pi/4, -3*math.pi/4]])
        + subtitle("cyclical island biogeography"))

    # Great American Interchange
    w("great_american_interchange", title("Great American Interchange")
        + '<path d="M 60 30 Q 80 30 85 50 Q 80 65 100 75 L 105 85 L 100 95 Q 110 100 110 110 Q 100 115 85 110 L 70 95 Q 60 75 55 55 Z" fill="#22c55e" opacity="0.6"/>'
        + '<path d="M 120 30 Q 140 35 145 55 Q 150 70 160 80 L 165 100 L 155 125 Q 145 135 135 125 Q 130 110 130 90 Q 125 60 120 40 Z" fill="#a78bfa" opacity="0.6"/>'
        + '<rect x="102" y="76" width="15" height="8" fill="#fbbf24"/>'
        + label("isthmus", 110, 95, color="#fde68a", size=6)
        + '<path d="M 95 75 Q 110 80 125 75" stroke="#60a5fa" fill="none" marker-end="url(#ga1)"/>'
        + '<path d="M 125 80 Q 110 85 95 80" stroke="#ef4444" fill="none" marker-end="url(#ga1)"/>'
        + '<defs><marker id="ga1" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto"><polygon points="0,0 5,2.5 0,5" fill="#fbbf24"/></marker></defs>'
        + label("N. America", 75, 25, color="#86efac", size=7)
        + label("S. America", 170, 25, color="#c4b5fd", size=7)
        + subtitle("~3 mya"))

    # Darwin finches
    w("darwin_finches", title("Darwin's Finches")
        + '<circle cx="40" cy="85" r="4" fill="#fbbf24"/>'
        + ''.join([
            f'<line x1="45" y1="85" x2="165" y2="{30+i*16}" stroke="#60a5fa" stroke-width="0.8"/>'
            + f'<ellipse cx="175" cy="{30+i*16}" rx="10" ry="6" fill="#8b6f47"/>'
            + f'<path d="M 185 {30+i*16} {beak}" fill="#fbbf24"/>'
            + f'<text x="220" y="{33+i*16}" fill="#fde68a" font-size="6" text-anchor="end">{n}</text>'
            for i,(beak,n) in enumerate([
                ("L 198 {0} L 185 {1} Z".format(27,33),"ground"),
                ("L 195 {0} L 185 {1} Z".format(44,49),"large seed"),
                ("L 200 {0} L 185 {1} Z".format(60,65),"cactus"),
                ("L 193 {0} L 185 {1} Z".format(76,81),"insect"),
                ("L 197 {0} L 185 {1} Z".format(92,97),"warbler"),
                ("L 194 {0} L 185 {1} Z".format(108,113),"tree"),
                ("L 198 {0} L 185 {1} Z".format(124,129),"tool"),
            ])
        ]))

    # Cichlid radiation
    w("cichlid_radiation", title("Cichlid Radiation")
        + '<ellipse cx="55" cy="55" rx="18" ry="12" fill="#1e3a5f" stroke="#60a5fa"/>'
        + label("Tanganyika", 55, 58, color="#93c5fd", size=6)
        + '<ellipse cx="120" cy="75" rx="18" ry="12" fill="#1e3a5f" stroke="#60a5fa"/>'
        + label("Victoria", 120, 78, color="#93c5fd", size=6)
        + '<ellipse cx="185" cy="95" rx="18" ry="12" fill="#1e3a5f" stroke="#60a5fa"/>'
        + label("Malawi", 185, 98, color="#93c5fd", size=6)
        + ''.join([f'<ellipse cx="{x}" cy="{y}" rx="3" ry="1.5" fill="{c}"/>' for x,y,c in [(48,52,"#ef4444"),(60,58,"#fbbf24"),(112,72,"#22c55e"),(125,78,"#a78bfa"),(178,92,"#ec4899"),(190,98,"#3b82f6")]])
        + label("500+ species per lake", 120, 130, color="#fde68a", size=8))

    # SLOSS debate
    w("sloss_debate", title("SLOSS Debate")
        + '<g transform="translate(5,30)"><circle cx="50" cy="45" r="35" fill="#064e3b" stroke="#22c55e"/><text x="50" y="48" fill="#86efac" font-size="9" text-anchor="middle" font-weight="700">SL</text><text x="50" y="95" fill="#86efac" font-size="7" text-anchor="middle">Single Large</text></g>'
        + '<g transform="translate(125,30)"><circle cx="20" cy="35" r="14" fill="#4c1d95" stroke="#a78bfa"/><circle cx="55" cy="25" r="12" fill="#4c1d95" stroke="#a78bfa"/><circle cx="85" cy="50" r="13" fill="#4c1d95" stroke="#a78bfa"/><circle cx="40" cy="60" r="11" fill="#4c1d95" stroke="#a78bfa"/><text x="50" y="95" fill="#c4b5fd" font-size="7" text-anchor="middle">Several Small</text></g>'
        + subtitle("reserve design tradeoff"))

    # Area phylogeny
    w("area_phylogeny", title("Area Phylogeny")
        + '<g transform="translate(10,30)"><text x="5" y="12" fill="#86efac" font-size="7">organism tree</text><line x1="10" y1="30" x2="25" y2="30" stroke="#22c55e"/><line x1="25" y1="30" x2="50" y2="18" stroke="#22c55e"/><line x1="25" y1="30" x2="50" y2="42" stroke="#22c55e"/><line x1="50" y1="42" x2="95" y2="35" stroke="#22c55e"/><line x1="50" y1="42" x2="95" y2="50" stroke="#22c55e"/><text x="100" y="20" fill="#86efac" font-size="6">sp1</text><text x="100" y="38" fill="#86efac" font-size="6">sp2</text><text x="100" y="53" fill="#86efac" font-size="6">sp3</text></g>'
        + '<g transform="translate(10,85)"><text x="5" y="12" fill="#fde68a" font-size="7">area tree</text><line x1="10" y1="30" x2="25" y2="30" stroke="#fbbf24"/><line x1="25" y1="30" x2="50" y2="18" stroke="#fbbf24"/><line x1="25" y1="30" x2="50" y2="42" stroke="#fbbf24"/><line x1="50" y1="42" x2="95" y2="35" stroke="#fbbf24"/><line x1="50" y1="42" x2="95" y2="50" stroke="#fbbf24"/><text x="100" y="20" fill="#fde68a" font-size="6">A</text><text x="100" y="38" fill="#fde68a" font-size="6">B</text><text x="100" y="53" fill="#fde68a" font-size="6">C</text></g>'
        + label("mirror = shared history", 175, 75, color="#93c5fd", size=7))

# ============================================================
# GROUP E: CONSERVATION
# ============================================================

def group_e():
    # 50/500 rule
    w("50_500_rule", title("50/500 Rule")
        + '<line x1="20" y1="90" x2="225" y2="90" stroke="#475569"/>'
        + ''.join([f'<line x1="{x}" y1="88" x2="{x}" y2="92" stroke="#94a3b8"/>' for x in [50,100,150,200]])
        + label("Ne", 14, 94, color="#93c5fd", size=8)
        + label("10", 50, 105, color="#94a3b8", size=7)
        + label("100", 100, 105, color="#94a3b8", size=7)
        + label("1000", 200, 105, color="#94a3b8", size=7)
        + '<line x1="80" y1="40" x2="80" y2="90" stroke="#fbbf24" stroke-width="2" stroke-dasharray="3,2"/>'
        + label("Ne=50", 80, 32, color="#fbbf24", size=8, weight="700")
        + label("(short-term)", 80, 55, color="#fde68a", size=7)
        + label("avoid inbreeding", 80, 68, color="#94a3b8", size=6)
        + '<line x1="180" y1="40" x2="180" y2="90" stroke="#22c55e" stroke-width="2" stroke-dasharray="3,2"/>'
        + label("Ne=500", 180, 32, color="#22c55e", size=8, weight="700")
        + label("(long-term)", 180, 55, color="#86efac", size=7)
        + label("adaptive", 180, 68, color="#94a3b8", size=6)
        + subtitle("Franklin thresholds", y=130))

    # Inbreeding depression
    w("inbreeding_depression", title("Inbreeding Depression")
        + '<circle cx="75" cy="40" r="8" fill="#60a5fa"/>'
        + label("A/a", 75, 43, color="#0a1220", size=7, weight="700")
        + '<circle cx="165" cy="40" r="8" fill="#60a5fa"/>'
        + label("A/a", 165, 43, color="#0a1220", size=7, weight="700")
        + '<line x1="75" y1="48" x2="95" y2="65" stroke="#94a3b8"/>'
        + '<line x1="165" y1="48" x2="145" y2="65" stroke="#94a3b8"/>'
        + '<circle cx="95" cy="72" r="8" fill="#a78bfa"/>'
        + '<circle cx="145" cy="72" r="8" fill="#a78bfa"/>'
        + label("cousins", 120, 77, color="#c4b5fd", size=8)
        + '<line x1="95" y1="80" x2="115" y2="95" stroke="#fbbf24"/>'
        + '<line x1="145" y1="80" x2="125" y2="95" stroke="#fbbf24"/>'
        + '<circle cx="120" cy="103" r="10" fill="#ef4444"/>'
        + label("a/a", 120, 107, color="#0a1220", size=8, weight="700")
        + label("homozygous recessive -> disease", 120, 133, color="#fca5a5", size=7))

    # Extinction vortex
    w("extinction_vortex", title("Extinction Vortex")
        + ''.join([
            f'<circle cx="{120+r*math.cos(a):.1f}" cy="{80+r*math.sin(a):.1f}" r="{12-i}" fill="#1f2937" stroke="{c}"/>'
            + f'<text x="{120+r*math.cos(a):.1f}" y="{82+r*math.sin(a):.1f}" fill="{c}" font-size="5" text-anchor="middle">{t}</text>'
            for i,(a,r,c,t) in enumerate([(-math.pi/2,45,"#fbbf24","small pop"),(0,35,"#fb923c","inbreed"),(math.pi/2,25,"#ef4444","low fit"),(math.pi,15,"#7f1d1d","smaller")])
        ])
        + '<circle cx="120" cy="80" r="4" fill="#000" stroke="#ef4444"/>'
        + label("EXTINCT", 120, 145, color="#ef4444", size=8, weight="700")
        + ''.join([f'<path d="M {120+(45-i*10)*math.cos(a):.1f} {80+(45-i*10)*math.sin(a):.1f} A 1 1 0 0 1 {120+(45-i*10)*math.cos(a+0.5):.1f} {80+(45-i*10)*math.sin(a+0.5):.1f}" stroke="#fbbf24" stroke-width="0.5" fill="none"/>' for i,a in enumerate([-math.pi/2,0,math.pi/2,math.pi])]))

    # Fishing evolution
    w("fishing_evolution", title("Fishing \u2192 Evolution")
        + label("BEFORE", 60, 30, color="#94a3b8", size=8)
        + ''.join([f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r/3}" fill="#60a5fa"/>' for x,y,r in [(30,45,8),(55,50,12),(85,47,14),(110,52,10)]])
        + '<path d="M 10 65 Q 60 65 110 65" stroke="#ef4444" fill="none" stroke-width="1" stroke-dasharray="2,1"/>'
        + label("net catches big ones", 60, 80, color="#ef4444", size=6)
        + label("AFTER", 180, 30, color="#94a3b8", size=8)
        + ''.join([f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r/3}" fill="#93c5fd"/>' for x,y,r in [(140,50,5),(160,55,4),(180,52,5),(200,54,4),(215,53,5)]])
        + label("small & slow-growing", 180, 80, color="#86efac", size=6)
        + subtitle("evolutionary selection by fishing", y=130))

    # Habitat fragmentation
    w("habitat_fragmentation", title("Habitat Fragmentation")
        + '<rect x="20" y="30" width="90" height="90" fill="#064e3b" stroke="#22c55e"/>'
        + label("intact", 65, 80, color="#86efac", size=8, weight="700")
        + ''.join([f'<circle cx="{x}" cy="{y}" r="2" fill="#fbbf24"/>' for x,y in [(35,45),(50,55),(70,50),(90,60),(45,75),(75,85),(60,100),(95,90),(40,90),(80,105)]])
        + '<line x1="120" y1="75" x2="140" y2="75" stroke="#ef4444" marker-end="url(#hf1)"/>'
        + '<defs><marker id="hf1" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto"><polygon points="0,0 5,2.5 0,5" fill="#ef4444"/></marker></defs>'
        + '<rect x="150" y="40" width="20" height="20" fill="#064e3b" stroke="#22c55e"/>'
        + '<rect x="180" y="55" width="18" height="18" fill="#064e3b" stroke="#22c55e"/>'
        + '<rect x="155" y="85" width="22" height="22" fill="#064e3b" stroke="#22c55e"/>'
        + '<rect x="190" y="95" width="16" height="16" fill="#064e3b" stroke="#22c55e"/>'
        + ''.join([f'<circle cx="{x}" cy="{y}" r="1.5" fill="#fbbf24"/>' for x,y in [(160,50),(190,62),(165,95),(197,103)]])
        + label("-> species loss", 180, 135, color="#fca5a5", size=7))

    # Bottleneck
    w("bottleneck", title("Bottleneck")
        + ''.join([f'<circle cx="{30+((i*13)%60)}" cy="{40+((i*7)%40)}" r="3" fill="{c}"/>' for i,c in enumerate(["#ef4444","#fbbf24","#22c55e","#60a5fa","#a78bfa","#ec4899","#f97316","#10b981","#6366f1","#eab308","#14b8a6","#f43f5e","#84cc16","#06b6d4","#d946ef","#0ea5e9","#8b5cf6","#f59e0b"])])
        + '<path d="M 95 55 L 115 85 L 115 95 L 95 125 Z" fill="none" stroke="#fbbf24" stroke-width="1.5"/>'
        + '<path d="M 145 55 L 125 85 L 125 95 L 145 125 Z" fill="none" stroke="#fbbf24" stroke-width="1.5"/>'
        + ''.join([f'<circle cx="120" cy="{85+i*3.5}" r="2" fill="{c}"/>' for i,c in enumerate(["#ef4444","#22c55e","#60a5fa"])])
        + ''.join([f'<circle cx="{170+((i*11)%50)}" cy="{55+((i*9)%55)}" r="3" fill="{c}"/>' for i,c in enumerate(["#ef4444","#ef4444","#22c55e","#60a5fa","#22c55e","#ef4444","#60a5fa","#22c55e","#ef4444"])])
        + label("few survivors", 195, 135, color="#fde68a", size=7)
        + label("lost diversity", 60, 135, color="#fca5a5", size=7))

    # Founder effect
    w("founder_effect", title("Founder Effect")
        + '<ellipse cx="60" cy="75" rx="40" ry="30" fill="#064e3b" stroke="#22c55e"/>'
        + ''.join([f'<circle cx="{x}" cy="{y}" r="3" fill="{c}"/>' for x,y,c in [(45,60,"#ef4444"),(70,55,"#fbbf24"),(80,70,"#22c55e"),(55,80,"#60a5fa"),(40,85,"#a78bfa"),(75,90,"#ec4899"),(50,70,"#f97316"),(65,95,"#10b981")]])
        + label("mainland (diverse)", 60, 120, color="#86efac", size=7)
        + '<path d="M 100 75 Q 140 50 175 75" stroke="#fbbf24" fill="none" stroke-width="1.5" marker-end="url(#fe1)"/>'
        + '<defs><marker id="fe1" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto"><polygon points="0,0 5,2.5 0,5" fill="#fbbf24"/></marker></defs>'
        + label("few founders", 135, 45, color="#fde68a", size=7)
        + '<circle cx="195" cy="80" r="22" fill="#1e3a5f" stroke="#60a5fa"/>'
        + '<circle cx="188" cy="75" r="3" fill="#fbbf24"/>'
        + '<circle cx="200" cy="82" r="3" fill="#fbbf24"/>'
        + label("island (limited)", 195, 120, color="#93c5fd", size=7))

    # Genetic rescue
    w("genetic_rescue", title("Genetic Rescue")
        + '<circle cx="75" cy="80" r="35" fill="#7f1d1d" opacity="0.5" stroke="#ef4444"/>'
        + ''.join([f'<circle cx="{x}" cy="{y}" r="3" fill="#ef4444"/>' for x,y in [(65,75),(85,80),(75,90)]])
        + label("small + inbred", 75, 130, color="#fca5a5", size=7)
        + '<path d="M 115 80 L 140 80" stroke="#fbbf24" stroke-width="2" marker-end="url(#gr1)"/>'
        + '<defs><marker id="gr1" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0,0 6,3 0,6" fill="#fbbf24"/></marker></defs>'
        + label("migrants", 127, 70, color="#fde68a", size=6)
        + '<circle cx="145" cy="80" r="3" fill="#22c55e"/>'
        + '<circle cx="125" cy="78" r="3" fill="#60a5fa"/>'
        + '<circle cx="180" cy="80" r="38" fill="#064e3b" opacity="0.6" stroke="#22c55e"/>'
        + ''.join([f'<circle cx="{x}" cy="{y}" r="3" fill="{c}"/>' for x,y,c in [(170,70,"#ef4444"),(190,75,"#22c55e"),(175,90,"#60a5fa"),(195,95,"#a78bfa"),(185,80,"#fbbf24")]])
        + label("hybrid vigor", 180, 130, color="#86efac", size=7, weight="700"))

    # Sixth extinction
    w("sixth_extinction", title("6th Extinction")
        + '<line x1="25" y1="125" x2="225" y2="125" stroke="#475569"/>'
        + ''.join([f'<line x1="{x}" y1="125" x2="{x}" y2="{125-h}" stroke="#fca5a5" stroke-width="3"/>' for x,h in [(50,40),(85,50),(125,80),(160,45),(190,55)]])
        + '<line x1="215" y1="125" x2="215" y2="25" stroke="#ef4444" stroke-width="4"/>'
        + label("NOW", 215, 20, color="#ef4444", size=8, weight="700")
        + label("Big 5", 130, 140, color="#94a3b8", size=7)
        + label("100-1000x normal", 180, 70, color="#ef4444", size=6, anchor="end")
        + label("Anthropocene", 215, 90, color="#fca5a5", size=6, anchor="end"))

    # Allee effect
    w("allee_effect", title("Allee Effect")
        + '<line x1="30" y1="85" x2="225" y2="85" stroke="#475569"/>'
        + '<line x1="30" y1="30" x2="30" y2="130" stroke="#475569"/>'
        + '<path d="M 30 115 Q 50 120 75 100 Q 110 75 150 65 Q 200 55 220 55" fill="none" stroke="#60a5fa" stroke-width="2"/>'
        + '<line x1="75" y1="90" x2="75" y2="100" stroke="#ef4444" stroke-dasharray="2,2"/>'
        + label("r<0", 55, 115, color="#ef4444", size=7)
        + label("can't find mates", 50, 128, color="#fca5a5", size=6)
        + label("r>0", 180, 55, color="#22c55e", size=7)
        + label("population size", 125, 142, color="#94a3b8", size=7)
        + label("growth", 22, 40, color="#93c5fd", size=7))

    # MVP
    w("mvp", title("Minimum Viable Pop.")
        + '<line x1="30" y1="120" x2="225" y2="120" stroke="#475569"/>'
        + '<line x1="30" y1="30" x2="30" y2="120" stroke="#475569"/>'
        + '<path d="M 30 35 Q 60 50 100 90 Q 150 115 220 118" fill="none" stroke="#ef4444" stroke-width="2"/>'
        + '<line x1="125" y1="105" x2="125" y2="120" stroke="#fbbf24" stroke-dasharray="2,2"/>'
        + label("MVP", 125, 98, color="#fbbf24", size=8, weight="700")
        + label("5% risk/100yr", 155, 95, color="#fde68a", size=6, anchor="start")
        + label("pop size", 125, 138, color="#94a3b8", size=7)
        + label("P(ext)", 22, 40, color="#fca5a5", size=7))

    # Effective pop size
    w("effective_pop_size", title("Effective Pop Size")
        + '<rect x="30" y="40" width="180" height="25" fill="#1e3a5f" stroke="#60a5fa"/>'
        + label("Census N = 1000", 120, 57, color="#93c5fd", size=9, weight="700")
        + '<line x1="120" y1="67" x2="120" y2="80" stroke="#fbbf24" marker-end="url(#ep1)"/>'
        + '<defs><marker id="ep1" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0,0 6,3 0,6" fill="#fbbf24"/></marker></defs>'
        + '<rect x="70" y="82" width="100" height="25" fill="#4c1d95" stroke="#a78bfa"/>'
        + label("Ne = 100-250", 120, 99, color="#c4b5fd", size=9, weight="700")
        + label("only reproducers count", 120, 125, color="#fde68a", size=7)
        + label("Ne = 10-25% of N", 120, 138, color="#94a3b8", size=7))

    # Pesticide resistance
    w("pesticide_resistance", title("Pesticide Resistance")
        + label("BEFORE", 60, 30, color="#94a3b8", size=8)
        + ''.join([f'<circle cx="{x}" cy="{y}" r="3" fill="#22c55e"/>' for x,y in [(25,45),(40,50),(55,45),(70,52),(90,48),(35,65),(60,68),(85,65),(50,80),(75,82),(25,75)]])
        + '<circle cx="65" cy="58" r="3" fill="#ef4444"/>'
        + label("pesticide", 120, 55, color="#fbbf24", size=8)
        + '<line x1="105" y1="65" x2="140" y2="65" stroke="#fbbf24" stroke-width="2" marker-end="url(#pr1)"/>'
        + '<defs><marker id="pr1" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0,0 6,3 0,6" fill="#fbbf24"/></marker></defs>'
        + label("AFTER", 190, 30, color="#94a3b8", size=8)
        + ''.join([f'<circle cx="{x}" cy="{y}" r="3" fill="#ef4444"/>' for x,y in [(155,45),(175,50),(195,45),(215,52),(165,68),(190,70),(210,65),(170,82),(200,85),(155,75)]])
        + subtitle("rare resistant -> common", y=125))

# ============================================================
# GROUP F: HUMAN EVOLUTION
# ============================================================

def group_f():
    # Hominin timeline
    w("hominin_timeline", title("Hominin Timeline")
        + '<line x1="25" y1="80" x2="225" y2="80" stroke="#fbbf24" stroke-width="1.5"/>'
        + ''.join([
            f'<line x1="{x}" y1="75" x2="{x}" y2="85" stroke="#fbbf24"/>'
            + f'<text x="{x}" y="{ty}" fill="{c}" font-size="6" text-anchor="middle">{t}</text>'
            + f'<text x="{x}" y="{95 if i%2==0 else 105}" fill="#94a3b8" font-size="6" text-anchor="middle">{d}</text>'
            for i,(x,t,d,c,ty) in enumerate([
                (30,"Sahelanthropus","7 mya","#fca5a5",50),
                (60,"Ardipithecus","4.4","#fca5a5",62),
                (90,"Australopith.","3.9","#fbbf24",50),
                (125,"habilis","2.4","#86efac",62),
                (160,"erectus","1.9","#86efac",50),
                (190,"Neanderth.","0.4","#c4b5fd",62),
                (220,"sapiens","0.3","#60a5fa",50),
            ])
        ])
        + subtitle("7 mya \u2192 now"))

    # Bipedalism anatomy
    w("bipedalism_anatomy", title("Bipedalism Anatomy")
        + '<g transform="translate(10,30)"><circle cx="25" cy="25" r="10" fill="#94a3b8"/><line x1="25" y1="35" x2="25" y2="75" stroke="#94a3b8" stroke-width="3"/><line x1="25" y1="50" x2="10" y2="65" stroke="#94a3b8" stroke-width="2"/><line x1="25" y1="50" x2="40" y2="65" stroke="#94a3b8" stroke-width="2"/><line x1="25" y1="75" x2="15" y2="95" stroke="#94a3b8" stroke-width="2"/><line x1="25" y1="75" x2="35" y2="95" stroke="#94a3b8" stroke-width="2"/><text x="25" y="110" fill="#94a3b8" font-size="7" text-anchor="middle">quadruped</text></g>'
        + '<g transform="translate(130,25)"><circle cx="30" cy="20" r="11" fill="#fde68a"/><circle cx="30" cy="30" r="2" fill="#ef4444"/><line x1="30" y1="31" x2="30" y2="50" stroke="#ef4444" stroke-width="0.8"/><line x1="30" y1="30" x2="30" y2="75" stroke="#fde68a" stroke-width="3"/><path d="M 30 55 Q 32 62 30 70" stroke="#ef4444" stroke-width="0.8" fill="none"/><line x1="30" y1="75" x2="22" y2="100" stroke="#fde68a" stroke-width="2"/><line x1="30" y1="75" x2="38" y2="100" stroke="#fde68a" stroke-width="2"/><line x1="22" y1="100" x2="15" y2="105" stroke="#fde68a" stroke-width="2"/><line x1="38" y1="100" x2="45" y2="105" stroke="#fde68a" stroke-width="2"/><path d="M 12 105 Q 18 108 23 105" stroke="#ef4444" fill="none"/><text x="30" y="120" fill="#fde68a" font-size="7" text-anchor="middle">biped</text></g>'
        + label("foramen magnum", 215, 40, color="#ef4444", size=5, anchor="end")
        + label("valgus knee", 215, 80, color="#ef4444", size=5, anchor="end")
        + label("arched foot", 215, 110, color="#ef4444", size=5, anchor="end"))

    # Out of Africa
    w("out_of_africa", title("Out of Africa ~60-70 kya")
        + '<rect x="20" y="35" width="200" height="75" fill="#1e3a5f" opacity="0.3"/>'
        + '<path d="M 80 60 Q 95 55 100 75 Q 105 90 95 95 Q 85 92 82 80 Z" fill="#22c55e" stroke="#86efac"/>'
        + label("Africa", 90, 80, color="#0a1220", size=6, weight="700")
        + '<path d="M 105 55 Q 130 50 150 55 L 145 75 Q 125 72 105 70 Z" fill="#a78bfa" opacity="0.5"/>'
        + '<path d="M 155 50 Q 190 48 210 55 L 205 75 Q 185 70 160 72 Z" fill="#a78bfa" opacity="0.5"/>'
        + '<path d="M 115 80 Q 140 85 165 82" fill="#a78bfa" opacity="0.5"/>'
        + '<circle cx="90" cy="75" r="3" fill="#ef4444"/>'
        + '<path d="M 95 70 Q 120 55 160 60" stroke="#fbbf24" fill="none" stroke-width="1.2" marker-end="url(#oa1)"/>'
        + '<path d="M 95 78 Q 130 85 190 78" stroke="#fbbf24" fill="none" stroke-width="1.2" marker-end="url(#oa1)"/>'
        + '<path d="M 100 82 Q 140 95 210 90" stroke="#fbbf24" fill="none" stroke-width="1.2" marker-end="url(#oa1)"/>'
        + '<defs><marker id="oa1" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto"><polygon points="0,0 5,2.5 0,5" fill="#fbbf24"/></marker></defs>'
        + subtitle("single origin \u2192 dispersal"))

    # Neanderthal DNA
    w("neanderthal_dna", title("Neanderthal DNA")
        + '<ellipse cx="75" cy="80" rx="20" ry="35" fill="#fde68a"/>'
        + '<circle cx="75" cy="55" r="12" fill="#fde68a"/>'
        + ''.join([f'<rect x="{60+((i*7)%28)}" y="{60+i*4}" width="2" height="2" fill="#c4b5fd"/>' for i in range(14)])
        + label("1-4%", 75, 130, color="#c4b5fd", size=9, weight="700")
        + label("Neanderthal DNA", 75, 142, color="#c4b5fd", size=7)
        + '<rect x="125" y="45" width="90" height="65" fill="#1f2937" stroke="#475569"/>'
        + label("non-African", 170, 58, color="#fde68a", size=8)
        + label("humans today", 170, 70, color="#94a3b8", size=7)
        + ''.join([f'<rect x="{130+i*6}" y="85" width="4" height="12" fill="{c}"/>' for i,c in enumerate(["#60a5fa","#60a5fa","#c4b5fd","#60a5fa","#60a5fa","#60a5fa","#c4b5fd","#60a5fa","#60a5fa","#60a5fa","#c4b5fd","#60a5fa","#60a5fa"])])
        + label("introgressed segments", 170, 108, color="#c4b5fd", size=6))

    # Brain evolution
    w("brain_evolution", title("Brain Size Evolution")
        + ''.join([
            f'<rect x="{20+i*30}" y="{125-h/8}" width="22" height="{h/8}" fill="{c}"/>'
            + f'<text x="{31+i*30}" y="{120-h/8}" fill="{c}" font-size="6" text-anchor="middle">{h}</text>'
            + f'<text x="{31+i*30}" y="138" fill="#94a3b8" font-size="6" text-anchor="middle">{n}</text>'
            for i,(h,c,n) in enumerate([
                (390,"#94a3b8","Chimp"),
                (450,"#fca5a5","Austral"),
                (600,"#fbbf24","habilis"),
                (900,"#fb923c","erectus"),
                (1400,"#22c55e","sapiens"),
                (1500,"#a78bfa","Neander"),
            ])
        ])
        + label("cc", 12, 40, color="#93c5fd", size=7))

    # Cooking hypothesis
    w("cooking_hypothesis", title("Cooking Hypothesis")
        + '<line x1="30" y1="115" x2="220" y2="115" stroke="#475569"/>'
        + '<line x1="30" y1="30" x2="30" y2="115" stroke="#475569"/>'
        + '<path d="M 30 95 Q 80 90 120 70 Q 170 45 220 35" fill="none" stroke="#22c55e" stroke-width="2"/>'
        + label("brain", 205, 45, color="#86efac", size=7, anchor="end")
        + '<path d="M 30 45 Q 80 55 120 80 Q 170 100 220 108" fill="none" stroke="#ef4444" stroke-width="2"/>'
        + label("gut", 205, 102, color="#fca5a5", size=7, anchor="end")
        + '<line x1="120" y1="30" x2="120" y2="115" stroke="#fbbf24" stroke-dasharray="3,2"/>'
        + label("~1.8 mya", 120, 25, color="#fbbf24", size=7)
        + label("cook food", 120, 135, color="#fde68a", size=8)
        + label("external digestion", 120, 145, color="#94a3b8", size=7))

    # Multiregional vs OOA
    w("multiregional_vs_ooa", title("Multiregional vs OOA")
        + '<g transform="translate(0,25)"><text x="60" y="15" fill="#94a3b8" font-size="8" text-anchor="middle">Multiregional</text><line x1="15" y1="60" x2="105" y2="60" stroke="#60a5fa" stroke-width="2"/><line x1="15" y1="45" x2="105" y2="45" stroke="#a78bfa" stroke-width="2"/><line x1="15" y1="75" x2="105" y2="75" stroke="#fbbf24" stroke-width="2"/><text x="15" y="95" fill="#94a3b8" font-size="6">H. erectus</text><text x="105" y="95" fill="#94a3b8" font-size="6" text-anchor="end">sapiens</text></g>'
        + '<line x1="120" y1="30" x2="120" y2="125" stroke="#475569" stroke-dasharray="2,2"/>'
        + '<g transform="translate(125,25)"><text x="55" y="15" fill="#94a3b8" font-size="8" text-anchor="middle">Out of Africa</text><line x1="10" y1="75" x2="35" y2="60" stroke="#60a5fa" stroke-width="2"/><line x1="35" y1="60" x2="95" y2="45" stroke="#60a5fa" stroke-width="2"/><line x1="35" y1="60" x2="95" y2="60" stroke="#60a5fa" stroke-width="2"/><line x1="35" y1="60" x2="95" y2="75" stroke="#60a5fa" stroke-width="2"/><text x="55" y="100" fill="#94a3b8" font-size="6">replacement model</text></g>')

    # Tool traditions
    w("tool_traditions", title("Tool Traditions")
        + '<line x1="25" y1="120" x2="225" y2="120" stroke="#fbbf24"/>'
        + ''.join([
            f'<line x1="{x}" y1="115" x2="{x}" y2="125" stroke="#fbbf24"/>'
            + f'<polygon points="{x-6},{92} {x+6},{92} {x+3},{108} {x-3},{108}" fill="{c}"/>'
            + f'<text x="{x}" y="{80}" fill="{c}" font-size="7" text-anchor="middle" font-weight="700">{n}</text>'
            + f'<text x="{x}" y="{138}" fill="#94a3b8" font-size="6" text-anchor="middle">{d}</text>'
            for x,n,d,c in [(50,"Oldowan","2.6 mya","#94a3b8"),(100,"Acheulean","1.7","#fbbf24"),(150,"Mousterian","0.3","#a78bfa"),(200,"Aurignacian","40 kya","#22c55e")]
        ])
        + subtitle("stone tool progression"))

    # Denisovan
    w("denisovan", title("Denisovans")
        + '<rect x="20" y="35" width="200" height="75" fill="#1e3a5f" opacity="0.3"/>'
        + '<circle cx="110" cy="55" r="4" fill="#ef4444"/>'
        + label("Denisova Cave", 110, 48, color="#fca5a5", size=6)
        + label("Siberia", 110, 68, color="#94a3b8", size=6)
        + '<ellipse cx="190" cy="95" rx="15" ry="8" fill="#22c55e" opacity="0.6"/>'
        + label("Melanesia", 190, 85, color="#86efac", size=6)
        + '<path d="M 115 60 Q 150 80 180 92" stroke="#fbbf24" fill="none" stroke-width="1.2" marker-end="url(#de1)"/>'
        + '<defs><marker id="de1" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto"><polygon points="0,0 5,2.5 0,5" fill="#fbbf24"/></marker></defs>'
        + label("~5% in Melanesians", 120, 125, color="#fde68a", size=8))

    # Adaptive introgression
    w("adaptive_introgression", title("Adaptive Introgression")
        + '<rect x="20" y="40" width="200" height="30" fill="#1e3a5f" stroke="#60a5fa"/>'
        + label("modern human genome", 120, 57, color="#93c5fd", size=8)
        + ''.join([f'<rect x="{30+i*11}" y="42" width="8" height="26" fill="{c}"/>' for i,c in enumerate(["#60a5fa","#60a5fa","#c4b5fd","#60a5fa","#60a5fa","#60a5fa","#c4b5fd","#60a5fa","#60a5fa","#fca5a5","#60a5fa","#60a5fa","#60a5fa","#c4b5fd","#60a5fa","#60a5fa","#60a5fa"])])
        + '<line x1="55" y1="72" x2="55" y2="85" stroke="#c4b5fd"/>'
        + label("EPAS1", 55, 95, color="#c4b5fd", size=6)
        + label("(high alt)", 55, 105, color="#94a3b8", size=5)
        + '<line x1="130" y1="72" x2="130" y2="85" stroke="#fca5a5"/>'
        + label("HLA", 130, 95, color="#fca5a5", size=6)
        + label("(immunity)", 130, 105, color="#94a3b8", size=5)
        + '<line x1="180" y1="72" x2="180" y2="85" stroke="#c4b5fd"/>'
        + label("skin pig", 180, 95, color="#c4b5fd", size=6)
        + subtitle("Neander/Deniso gifts"))

    # Hominins vs hominids
    w("hominins_vs_hominids", title("Hominins vs Hominids")
        + '<circle cx="120" cy="80" r="55" fill="#4c1d95" opacity="0.3" stroke="#a78bfa"/>'
        + label("HOMINIDAE", 120, 40, color="#c4b5fd", size=9, weight="700")
        + label("(great apes)", 120, 52, color="#c4b5fd", size=7)
        + '<circle cx="120" cy="95" r="28" fill="#7f1d1d" opacity="0.5" stroke="#ef4444"/>'
        + label("HOMININI", 120, 95, color="#fca5a5", size=8, weight="700")
        + label("(bipedal)", 120, 108, color="#fca5a5", size=6)
        + '<text x="55" y="70" font-size="12">\U0001F98D</text>'
        + '<text x="175" y="70" font-size="12">\U0001F9A7</text>'
        + label("humans + ancestors", 120, 140, color="#fde68a", size=7))

# ============================================================
# GROUP G: EVOLUTIONARY MEDICINE
# ============================================================

def group_g():
    # Nesse 6 reasons
    w("nesse_6_reasons", title("Nesse's 6 Reasons")
        + ''.join([
            f'<polygon points="{cx},{cy-14} {cx+12},{cy-7} {cx+12},{cy+7} {cx},{cy+14} {cx-12},{cy+7} {cx-12},{cy-7}" fill="#1f2937" stroke="{c}" stroke-width="1.2"/>'
            + f'<text x="{cx}" y="{cy-2}" fill="{c}" font-size="6" text-anchor="middle" font-weight="700">{t1}</text>'
            + f'<text x="{cx}" y="{cy+6}" fill="#94a3b8" font-size="5" text-anchor="middle">{t2}</text>'
            for cx,cy,c,t1,t2 in [
                (60,50,"#ef4444","pathogens","evolve fast"),
                (120,50,"#fbbf24","mismatch","env change"),
                (180,50,"#a78bfa","trade-off","cost/benefit"),
                (60,100,"#60a5fa","constraint","no redesign"),
                (120,100,"#22c55e","pleiotropy","1 gene many"),
                (180,100,"#ec4899","defense","fever/pain"),
            ]
        ])
        + subtitle("why we get sick", y=140))

    # Mismatch disease
    w("mismatch_disease", title("Mismatch Disease")
        + '<rect x="15" y="35" width="90" height="40" fill="#064e3b" stroke="#22c55e"/>'
        + label("ancestral", 60, 50, color="#86efac", size=8, weight="700")
        + label("active + lean", 60, 65, color="#e5e7eb", size=7)
        + '<rect x="135" y="35" width="90" height="40" fill="#7f1d1d" stroke="#ef4444"/>'
        + label("modern", 180, 50, color="#fca5a5", size=8, weight="700")
        + label("sedentary + hi-cal", 180, 65, color="#e5e7eb", size=7)
        + '<line x1="105" y1="55" x2="135" y2="55" stroke="#fbbf24" stroke-width="2" marker-end="url(#mi1)"/>'
        + '<defs><marker id="mi1" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0,0 6,3 0,6" fill="#fbbf24"/></marker></defs>'
        + '<line x1="120" y1="85" x2="120" y2="100" stroke="#ef4444" marker-end="url(#mi1)"/>'
        + label("obesity | T2DM | allergies", 120, 120, color="#fca5a5", size=8))

    # Virulence tradeoff
    w("virulence_tradeoff", title("Virulence Trade-off")
        + '<line x1="30" y1="120" x2="220" y2="120" stroke="#475569"/>'
        + '<line x1="30" y1="30" x2="30" y2="120" stroke="#475569"/>'
        + '<path d="M 30 115 Q 80 70 125 45 Q 170 70 220 115" fill="none" stroke="#ef4444" stroke-width="2"/>'
        + '<circle cx="125" cy="45" r="4" fill="#fbbf24"/>'
        + label("optimum", 125, 38, color="#fbbf24", size=8, weight="700")
        + label("too mild", 55, 110, color="#86efac", size=6)
        + label("kills host", 195, 110, color="#fca5a5", size=6)
        + label("virulence", 125, 138, color="#94a3b8", size=7)
        + label("R\u2080", 22, 40, color="#93c5fd", size=7))

    # Red queen
    w("red_queen", title("Red Queen")
        + '<circle cx="80" cy="80" r="25" fill="#1e3a5f" stroke="#60a5fa"/>'
        + label("HOST", 80, 83, color="#93c5fd", size=9, weight="700")
        + '<circle cx="165" cy="80" r="25" fill="#7f1d1d" stroke="#ef4444"/>'
        + label("PATHO", 165, 83, color="#fca5a5", size=9, weight="700")
        + '<path d="M 105 65 Q 122 55 140 65" stroke="#fbbf24" fill="none" stroke-width="1.5" marker-end="url(#rq1)"/>'
        + '<path d="M 140 95 Q 122 105 105 95" stroke="#fbbf24" fill="none" stroke-width="1.5" marker-end="url(#rq1)"/>'
        + '<defs><marker id="rq1" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><polygon points="0,0 6,3 0,6" fill="#fbbf24"/></marker></defs>'
        + label("resist", 122, 52, color="#93c5fd", size=6)
        + label("evolve", 122, 115, color="#fca5a5", size=6)
        + subtitle("arms race coevolution"))

    # Antagonistic pleiotropy
    w("antagonistic_pleiotropy", title("Antagonistic Pleiotropy")
        + '<line x1="30" y1="80" x2="220" y2="80" stroke="#fbbf24" stroke-width="1.5"/>'
        + label("early life", 70, 55, color="#22c55e", size=8, weight="700")
        + '<rect x="40" y="62" width="60" height="14" fill="#064e3b" stroke="#22c55e"/>'
        + label("BENEFIT", 70, 73, color="#86efac", size=8, weight="700")
        + label("tumor suppress", 70, 95, color="#86efac", size=6)
        + label("late life", 180, 55, color="#ef4444", size=8, weight="700")
        + '<rect x="150" y="62" width="60" height="14" fill="#7f1d1d" stroke="#ef4444"/>'
        + label("COST", 180, 73, color="#fca5a5", size=8, weight="700")
        + label("senescence", 180, 95, color="#fca5a5", size=6)
        + '<polygon points="125,78 135,74 135,82" fill="#fbbf24"/>'
        + subtitle("same allele, two fates"))

    # Sickle cell advantage
    w("sickle_cell_advantage", title("Sickle Cell")
        + ''.join([
            f'<rect x="{20+i*70}" y="55" width="60" height="{h}" fill="{c}"/>'
            + f'<text x="{50+i*70}" y="{50-h+55}" fill="{c}" font-size="8" text-anchor="middle" font-weight="700">{gt}</text>'
            + f'<text x="{50+i*70}" y="125" fill="#94a3b8" font-size="7" text-anchor="middle">{lbl}</text>'
            for i,(gt,h,c,lbl) in enumerate([
                ("AA",40,"#fbbf24","normal"),
                ("AS",60,"#22c55e","HETERO"),
                ("SS",15,"#ef4444","sickle"),
            ])
        ])
        + label("fitness in malaria", 120, 30, color="#fde68a", size=8)
        + label("heterozygote advantage", 120, 140, color="#86efac", size=8))

    # Cancer evolution
    w("cancer_evolution", title("Cancer Evolution")
        + '<circle cx="30" cy="80" r="6" fill="#22c55e"/>'
        + label("normal", 30, 100, color="#86efac", size=6)
        + '<line x1="38" y1="80" x2="60" y2="80" stroke="#fbbf24" marker-end="url(#ca1)"/>'
        + '<defs><marker id="ca1" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto"><polygon points="0,0 5,2.5 0,5" fill="#fbbf24"/></marker></defs>'
        + '<circle cx="70" cy="80" r="7" fill="#fbbf24"/>'
        + label("clone", 70, 100, color="#fde68a", size=6)
        + '<line x1="78" y1="75" x2="100" y2="65" stroke="#fbbf24"/>'
        + '<line x1="78" y1="85" x2="100" y2="95" stroke="#fbbf24"/>'
        + '<circle cx="110" cy="63" r="8" fill="#fb923c"/>'
        + '<circle cx="110" cy="95" r="8" fill="#fb923c"/>'
        + label("subclones", 110, 115, color="#fb923c", size=6)
        + '<line x1="118" y1="63" x2="140" y2="55" stroke="#ef4444"/>'
        + '<line x1="118" y1="95" x2="140" y2="100" stroke="#ef4444"/>'
        + '<circle cx="150" cy="52" r="8" fill="#ef4444"/>'
        + '<circle cx="150" cy="80" r="8" fill="#ef4444"/>'
        + '<circle cx="150" cy="108" r="8" fill="#ef4444"/>'
        + label("metastasis", 195, 80, color="#fca5a5", size=8, weight="700")
        + '<line x1="158" y1="80" x2="180" y2="80" stroke="#ef4444" marker-end="url(#ca1)"/>'
        + subtitle("tumor as evolving population"))

    # Fever adaptive
    w("fever_adaptive", title("Fever is Adaptive")
        + '<line x1="30" y1="115" x2="220" y2="115" stroke="#475569"/>'
        + '<line x1="30" y1="30" x2="30" y2="115" stroke="#475569"/>'
        + '<path d="M 30 50 Q 90 55 130 75 Q 180 100 220 110" fill="none" stroke="#ef4444" stroke-width="2"/>'
        + label("pathogen", 205, 50, color="#fca5a5", size=7, anchor="end")
        + '<path d="M 30 110 Q 90 100 130 80 Q 180 55 220 45" fill="none" stroke="#22c55e" stroke-width="2"/>'
        + label("immune", 205, 108, color="#86efac", size=7, anchor="end")
        + '<rect x="115" y="30" width="30" height="85" fill="#fbbf24" opacity="0.2"/>'
        + label("fever", 130, 45, color="#fbbf24", size=7, weight="700")
        + label("zone", 130, 55, color="#fde68a", size=6)
        + label("temp", 125, 135, color="#94a3b8", size=7)
        + label("37C", 30, 132, color="#94a3b8", size=6)
        + label("40C", 220, 132, color="#94a3b8", size=6))

    # Hygiene hypothesis
    w("hygiene_hypothesis", title("Hygiene Hypothesis")
        + '<g transform="translate(5,30)"><rect x="5" y="10" width="100" height="70" fill="#1e3a5f" stroke="#60a5fa"/><text x="55" y="25" fill="#93c5fd" font-size="7" text-anchor="middle" font-weight="700">developed</text><rect x="20" y="35" width="70" height="8" fill="#22c55e"/><text x="15" y="42" fill="#86efac" font-size="6" text-anchor="end">inf</text><rect x="20" y="50" width="20" height="8" fill="#22c55e"/><rect x="20" y="65" width="65" height="8" fill="#ef4444"/><text x="15" y="72" fill="#fca5a5" font-size="6" text-anchor="end">all</text></g>'
        + '<g transform="translate(125,30)"><rect x="5" y="10" width="100" height="70" fill="#7c4827" stroke="#fbbf24"/><text x="55" y="25" fill="#fde68a" font-size="7" text-anchor="middle" font-weight="700">developing</text><rect x="20" y="35" width="15" height="8" fill="#ef4444"/><rect x="20" y="50" width="70" height="8" fill="#22c55e"/><text x="15" y="57" fill="#86efac" font-size="6" text-anchor="end">inf</text><rect x="20" y="65" width="20" height="8" fill="#22c55e"/><text x="15" y="72" fill="#86efac" font-size="6" text-anchor="end">all</text></g>'
        + subtitle("less infection \u2192 more allergy"))

    # P53 pleiotropy
    w("p53_pleiotropy", title("p53 Pleiotropy")
        + '<rect x="20" y="40" width="200" height="18" fill="#1f2937" stroke="#fbbf24"/>'
        + label("p53 gene", 120, 53, color="#fde68a", size=9, weight="700")
        + '<line x1="60" y1="60" x2="60" y2="75" stroke="#22c55e" marker-end="url(#p5)"/>'
        + '<line x1="180" y1="60" x2="180" y2="75" stroke="#ef4444" marker-end="url(#p5)"/>'
        + '<defs><marker id="p5" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto"><polygon points="0,0 5,2.5 0,5" fill="#fbbf24"/></marker></defs>'
        + '<rect x="25" y="78" width="75" height="35" fill="#064e3b" stroke="#22c55e"/>'
        + label("young adult", 62, 93, color="#86efac", size=8, weight="700")
        + label("suppress tumors", 62, 106, color="#86efac", size=7)
        + '<rect x="140" y="78" width="75" height="35" fill="#7f1d1d" stroke="#ef4444"/>'
        + label("old adult", 177, 93, color="#fca5a5", size=8, weight="700")
        + label("senescence", 177, 106, color="#fca5a5", size=7)
        + subtitle("same gene, opposite roles"))

    # Myxoma coevolution
    w("myxoma_coevolution", title("Myxoma Coevolution")
        + '<line x1="30" y1="115" x2="220" y2="115" stroke="#475569"/>'
        + '<line x1="30" y1="30" x2="30" y2="115" stroke="#475569"/>'
        + '<path d="M 30 35 Q 80 55 130 75 Q 180 90 220 100" fill="none" stroke="#ef4444" stroke-width="2"/>'
        + label("virus virulence", 205, 45, color="#fca5a5", size=6, anchor="end")
        + '<path d="M 30 110 Q 80 100 130 80 Q 180 60 220 50" fill="none" stroke="#22c55e" stroke-width="2"/>'
        + label("rabbit resist", 205, 108, color="#86efac", size=6, anchor="end")
        + label("1950", 30, 132, color="#94a3b8", size=7)
        + label("1970", 220, 132, color="#94a3b8", size=7, anchor="end")
        + subtitle("Australia natural experiment"))

    # Peto's paradox
    w("peto_paradox", title("Peto's Paradox")
        + '<line x1="30" y1="115" x2="220" y2="115" stroke="#475569"/>'
        + '<line x1="30" y1="30" x2="30" y2="115" stroke="#475569"/>'
        + '<line x1="30" y1="105" x2="220" y2="45" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,2"/>'
        + label("expected", 205, 50, color="#fca5a5", size=6, anchor="end")
        + '<line x1="30" y1="85" x2="220" y2="85" stroke="#22c55e" stroke-width="2"/>'
        + label("actual: flat", 205, 78, color="#86efac", size=7, anchor="end", weight="700")
        + ''.join([f'<circle cx="{30+i*45}" cy="85" r="3" fill="#fbbf24"/>' for i in range(5)])
        + label("mouse", 40, 132, color="#94a3b8", size=6)
        + label("whale", 210, 132, color="#94a3b8", size=6, anchor="end")
        + label("cancer rate", 22, 40, color="#93c5fd", size=6)
        + label("body mass", 125, 132, color="#94a3b8", size=7))

    # Evolutionary constraints
    w("evolutionary_constraints", title("Evolutionary Constraints")
        + '<circle cx="120" cy="75" r="40" fill="#1e3a5f" stroke="#60a5fa"/>'
        + '<circle cx="120" cy="75" r="22" fill="#0a1220" stroke="#93c5fd"/>'
        + '<circle cx="120" cy="75" r="7" fill="#000"/>'
        + ''.join([f'<line x1="{120+42*math.cos(a):.1f}" y1="{75+42*math.sin(a):.1f}" x2="{120+48*math.cos(a):.1f}" y2="{75+48*math.sin(a):.1f}" stroke="#fbbf24" stroke-width="0.8"/>' for a in [0.3,0.9,1.5,2.1,2.7,3.3,3.9,4.5,5.1,5.7,6.2]])
        + '<circle cx="153" cy="82" r="3" fill="#ef4444"/>'
        + label("blind spot", 200, 80, color="#ef4444", size=6, anchor="end")
        + '<line x1="156" y1="82" x2="180" y2="82" stroke="#ef4444" stroke-width="0.5"/>'
        + label("inverted retina", 120, 130, color="#fca5a5", size=7)
        + label("designer would fix", 120, 140, color="#94a3b8", size=7))

    # Horizontal gene transfer
    w("horizontal_gene_transfer", title("Horizontal Gene Transfer")
        + '<ellipse cx="70" cy="80" rx="25" ry="15" fill="#1e3a5f" stroke="#60a5fa"/>'
        + '<circle cx="65" cy="75" r="6" fill="none" stroke="#fbbf24" stroke-width="1.2"/>'
        + label("R", 65, 78, color="#fbbf24", size=7, weight="700")
        + label("bacterium 1", 70, 105, color="#93c5fd", size=7)
        + '<ellipse cx="180" cy="80" rx="25" ry="15" fill="#1e3a5f" stroke="#60a5fa"/>'
        + label("bacterium 2", 180, 105, color="#93c5fd", size=7)
        + '<line x1="95" y1="78" x2="155" y2="78" stroke="#fbbf24" stroke-width="2"/>'
        + '<line x1="95" y1="82" x2="155" y2="82" stroke="#fbbf24" stroke-width="2"/>'
        + label("pilus", 125, 72, color="#fde68a", size=7)
        + '<circle cx="125" cy="80" r="4" fill="none" stroke="#fbbf24"/>'
        + label("R", 125, 83, color="#fbbf24", size=6, weight="700")
        + label("resistance jumps!", 120, 130, color="#fde68a", size=8, weight="700"))

    # Nausea pregnancy
    w("nausea_pregnancy", title("Pregnancy Nausea")
        + '<line x1="30" y1="115" x2="220" y2="115" stroke="#475569"/>'
        + '<line x1="30" y1="30" x2="30" y2="115" stroke="#475569"/>'
        + '<path d="M 30 110 L 60 105 L 80 45 L 110 40 L 140 65 L 180 105 L 220 110" fill="none" stroke="#ef4444" stroke-width="2"/>'
        + '<rect x="55" y="35" width="85" height="75" fill="#fbbf24" opacity="0.15"/>'
        + label("wks 6-12", 95, 45, color="#fbbf24", size=7, weight="700")
        + label("organogenesis", 95, 135, color="#fde68a", size=7)
        + label("severity", 22, 40, color="#fca5a5", size=7)
        + subtitle("protects embryo"))

    # MHC diversity
    w("mhc_diversity", title("MHC Diversity")
        + '<circle cx="60" cy="55" r="14" fill="#1e3a5f" stroke="#60a5fa"/>'
        + label("T", 60, 59, color="#93c5fd", size=9, weight="700")
        + ''.join([
            f'<line x1="73" y1="55" x2="{120+i*1}" y2="{30+i*20}" stroke="#fbbf24" stroke-width="0.5"/>'
            + f'<rect x="{125}" y="{25+i*20}" width="35" height="12" fill="{c}"/>'
            + f'<circle cx="{145}" cy="{31+i*20}" r="3" fill="#ef4444"/>'
            + f'<text x="{170}" y="{33+i*20}" fill="{c}" font-size="6" text-anchor="start">MHC-{pt}</text>'
            for i,(c,pt) in enumerate([("#22c55e","A"),("#fbbf24","B"),("#a78bfa","C"),("#ec4899","D"),("#60a5fa","E")])
        ])
        + label("diverse MHC = broader coverage", 120, 140, color="#86efac", size=7))

    # Inflammation mismatch
    w("inflammation_mismatch", title("Inflammation Mismatch")
        + '<rect x="15" y="40" width="95" height="50" fill="#064e3b" stroke="#22c55e"/>'
        + label("acute", 62, 55, color="#86efac", size=8, weight="700")
        + label("infection", 62, 68, color="#e5e7eb", size=7)
        + label("HELPFUL", 62, 83, color="#22c55e", size=8, weight="700")
        + '<rect x="130" y="40" width="95" height="50" fill="#7f1d1d" stroke="#ef4444"/>'
        + label("chronic", 177, 55, color="#fca5a5", size=8, weight="700")
        + label("stress/obesity", 177, 68, color="#e5e7eb", size=7)
        + label("DISEASE", 177, 83, color="#ef4444", size=8, weight="700")
        + subtitle("same response, diff context", y=115)
        + label("CVD | T2DM | Alzheimer's", 120, 132, color="#fde68a", size=8))

    # Co-evolution
    w("co_evolution", title("Co-evolution")
        + '<path d="M 60 110 L 60 70 L 52 65 L 60 55 L 68 65 L 60 70" fill="#22c55e"/>'
        + '<ellipse cx="60" cy="55" rx="10" ry="6" fill="#ec4899"/>'
        + '<ellipse cx="55" cy="48" rx="8" ry="8" fill="#ec4899"/>'
        + '<ellipse cx="65" cy="50" rx="8" ry="8" fill="#ec4899"/>'
        + '<ellipse cx="60" cy="58" rx="6" ry="6" fill="#f472b6"/>'
        + label("long corolla", 60, 130, color="#ec4899", size=7)
        + '<ellipse cx="170" cy="70" rx="15" ry="8" fill="#8b6f47"/>'
        + '<circle cx="155" cy="68" r="4" fill="#000"/>'
        + '<path d="M 155 72 Q 145 75 135 72 L 140 68" stroke="#fbbf24" stroke-width="1.5" fill="none"/>'
        + label("long tongue", 170, 100, color="#fbbf24", size=7)
        + label("moth", 170, 45, color="#94a3b8", size=7)
        + '<path d="M 90 65 Q 110 50 130 65" stroke="#fbbf24" fill="none" stroke-dasharray="2,1"/>'
        + '<path d="M 130 85 Q 110 95 90 85" stroke="#fbbf24" fill="none" stroke-dasharray="2,1"/>'
        + subtitle("reciprocal adaptation"))


# ============================================================
# MAIN
# ============================================================

if __name__ == '__main__':
    groups = [group_a, group_b, group_c, group_d, group_e, group_f, group_g]
    for g in groups:
        try:
            g()
        except Exception as e:
            FAILURES.append((g.__name__, str(e)))
            import traceback
            traceback.print_exc()
    files = [f for f in os.listdir(OUT_DIR) if f.startswith('svg_') and f.endswith('.svg')]
    print(f'Written this run: {len(WRITTEN)}')
    print(f'Total svg_*.svg in dir: {len(files)}')
    if FAILURES:
        print(f'FAILURES: {len(FAILURES)}')
        for n,e in FAILURES:
            print(f'  - {n}: {e}')
    else:
        print('No failures.')
