"""Enrichment pass for v2 data.json (v4 — expanded quiz + readable SVGs).

Adds the following per node:

  v2.transcript    list[{n,title,main}]  Slide-by-slide from lecture files
                                          (only for Lec 1-15 which have transcripts)
  v2.quiz          list[{question,correct,distractors,rationale}]  12 Qs per node
  v2.flashcards    list[{front,back}]   4 flashcards per node
  v2.svg           str                  Inline SVG diagram (no text truncation)

Quiz pulls from:
  - v2.definition           (1 forward Q + 1 cloze Q)
  - v2.keyTerms             (4 forward + 4 reverse term-meaning Qs)
  - v2.mnemonic             (1 mnemonic-recognition Q)
  - v2.examTrap             (1 trap Q + 1 inverse trap Q)
  - legacy quiz             (1 original core Q)

The transcript pull uses n.lecture + n.slideRange to index into
_work/lectures/lec{N}.json, returning the slides in that range.

Run:  python _work/enrich_v3.py
"""
import json
import os
import sys
import io
import math

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA = os.path.join(ROOT, 'data.json')
LEC_DIR = os.path.join(ROOT, '_work', 'lectures')

# Map lecture number -> transcript filename (some lectures share a file)
LEC_FILES = {
    1: 'lec1.json',
    2: 'lec2.json',
    3: 'lec3.json',
    4: 'lec4.json',
    5: 'lec5_6.json',
    6: 'lec5_6.json',
    7: 'lec7.json',
    8: 'lec8.json',
    9: 'lec9.json',
    10: 'lec10_11.json',
    11: 'lec10_11.json',
    12: 'lec12.json',
    13: 'lec13.json',
    14: 'lec14.json',
    15: 'lec15.json',
}

_lec_cache = {}

def load_lec(num):
    if num not in LEC_FILES:
        return None
    if num in _lec_cache:
        return _lec_cache[num]
    path = os.path.join(LEC_DIR, LEC_FILES[num])
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as f:
        _lec_cache[num] = json.load(f)
    return _lec_cache[num]


def get_transcript_slides(node):
    """Return list of {n,title,main,notes} for slides in node's slideRange."""
    lec_data = load_lec(node['lecture'])
    if not lec_data:
        return []
    try:
        lo, hi = [int(x) for x in node['slideRange'].split('-')]
    except Exception:
        return []
    out = []
    for s in lec_data.get('slides', []):
        if lo <= s['n'] <= hi:
            out.append({
                'n': s['n'],
                'title': s.get('title', '').strip(),
                'main': s.get('main', '').strip(),
                'notes': s.get('notes', '').strip() if s.get('notes') not in (None, 'None.') else '',
            })
    return out


# ---------- Quiz expansion (12 questions per node) -----------------------

def _short_def(d, limit=110):
    """Trim a long definition for use as a distractor."""
    d = d.strip()
    if len(d) <= limit:
        return d
    cut = d[:limit].rsplit(' ', 1)[0]
    return cut + '.'


def expand_quiz(node):
    """Generate 12 quiz questions from v2 content.

    Strategy:
      1.  Legacy original core question
      2.  Forward definition recall ("which best defines X?")
      3.  Forward key term 0 ("what does <term0> mean?")
      4.  Forward key term 1 ("what does <term1> mean?")
      5.  Forward key term 2 ("what does <term2> mean?")
      6.  Forward key term 3 ("what does <term3> mean?")
      7.  Reverse key term 0 ("which term means <def0>?")
      8.  Reverse key term 1 ("which term means <def1>?")
      9.  Reverse key term 2 ("which term means <def2>?")
      10. Reverse key term 3 ("which term means <def3>?")
      11. Mnemonic recognition ("what concept does mnemonic '<hook>' represent?")
      12. Exam trap ("which is the common misconception about X?")
    """
    v2 = node['v2']
    legacy_quiz = node.get('quiz')
    if isinstance(legacy_quiz, list):
        legacy_quiz = legacy_quiz[0] if legacy_quiz else None
    out = []
    kt = v2['keyTerms']
    title_head = node['title'].split(':')[0].strip()
    term_names = [t['term'] for t in kt]
    full_title = node['title']

    # ------------------------------------------------------------------ 1.
    if legacy_quiz and isinstance(legacy_quiz, dict) and legacy_quiz.get('question'):
        out.append({
            'question': legacy_quiz['question'],
            'correct': legacy_quiz['correct'],
            'distractors': legacy_quiz['distractors'],
            'rationale': 'Tests the core concept for this node.',
        })

    # ------------------------------------------------------------------ 2.
    trap_first = v2['examTrap'].split('.')[0].replace('Wrong: ', '').replace("'", '').strip()
    swap_def = v2['definition']
    if 'populations' in swap_def:
        swap_def = swap_def.replace('populations', 'individuals').replace('generations', 'lifetimes')
    elif 'evolves' in swap_def:
        swap_def = swap_def.replace('evolves', 'changes within one lifetime')
    else:
        swap_def = f"A version of {title_head} that only affects single organisms during their lifetime."
    out.append({
        'question': f"Which of the following best defines {title_head}?",
        'correct': v2['definition'],
        'distractors': [
            swap_def,
            f"A process unrelated to heritable change: {trap_first}",
            f"A rare outcome requiring {kt[0]['term']} only, ignoring {kt[1]['term']}.",
        ],
        'rationale': f"The correct definition involves all four key terms: {', '.join(term_names)}.",
    })

    # ----------------------------------------------------------------- 3-6.
    # Forward key term — "what does X mean?"
    for i in range(4):
        ti = kt[i]
        others = [kt[j]['def'] for j in range(4) if j != i]
        out.append({
            'question': f'In the context of {title_head}, what does "{ti["term"]}" mean?',
            'correct': ti['def'].capitalize().rstrip('.') + '.',
            'distractors': [d.capitalize().rstrip('.') + '.' for d in others],
            'rationale': f'"{ti["term"]}" specifically refers to: {ti["def"]}.',
        })

    # ----------------------------------------------------------------- 7-10.
    # Reverse key term — "which term means X?"
    for i in range(4):
        ti = kt[i]
        others = [kt[j]['term'] for j in range(4) if j != i]
        out.append({
            'question': f'Which key term in {title_head} refers to: "{ti["def"]}"?',
            'correct': ti['term'],
            'distractors': others,
            'rationale': f'"{ti["term"]}" is defined as: {ti["def"]}.',
        })

    # ----------------------------------------------------------------- 11.
    # Mnemonic recognition
    mn_hook = v2['mnemonic']['hook']
    mn_exp = v2['mnemonic']['explanation']
    out.append({
        'question': f'The mnemonic "{mn_hook}" is used to remember which concept?',
        'correct': title_head,
        'distractors': [
            f'{kt[0]["term"]} (a sub-component, not the whole concept)',
            f'A diagnostic test for {trap_first}',
            f'The opposite of {kt[3]["term"]}',
        ],
        'rationale': f'Mnemonic explanation: {mn_exp}',
    })

    # ----------------------------------------------------------------- 12.
    # Exam trap — which is the misconception?
    trap = v2['examTrap']
    wrong_claim = trap
    if trap.startswith("Wrong: '"):
        end = trap.find("'", 8)
        if end > 0:
            wrong_claim = trap[8:end]
    out.append({
        'question': f'Which of the following is a common MISCONCEPTION about {title_head}?',
        'correct': wrong_claim,
        'distractors': [
            _short_def(v2['definition']),
            f"{kt[0]['term']} means {kt[0]['def']}.",
            _short_def(v2['mnemonic']['explanation']),
        ],
        'rationale': f"Why this is the trap: {trap}",
    })

    return out


# ---------- Flashcards expansion (4 cards per node) ---------------------

def expand_flashcards(node):
    """Generate 4 flashcards per node."""
    v2 = node['v2']
    kt = v2['keyTerms']
    title_head = node['title'].split(':')[0].strip()
    out = [
        {'front': v2['actions']['flashcardFront'],
         'back':  v2['actions']['flashcardBack']},
        {'front': f"What mnemonic helps you remember {title_head}?",
         'back':  f"{v2['mnemonic']['hook']} — {v2['mnemonic']['explanation']}"},
        {'front': f"Name the 4 key terms for {title_head} and their meanings.",
         'back':  '; '.join(f"{t['term']}: {t['def']}" for t in kt) + '.'},
        {'front': f"What is the most common exam trap for {title_head}?",
         'back':  v2['examTrap']},
    ]
    return out


# ---------- SVG diagram generator (no truncation) -----------------------

PAL = {
    'teal':    '#7de2d1',
    'purple':  '#8a5cf6',
    'coral':   '#ff6b6b',
    'pink':    '#f472b6',
    'gold':    '#e0a85c',
    'blue':    '#4ea8de',
    'yellow':  '#ffc857',
    'emerald': '#34d399',   # strong green: "valid/correct/monophyletic"
    'crimson': '#ef4444',   # strong red: "invalid/wrong/paraphyletic"
    'amber':   '#f59e0b',   # warm amber: "warning/trap/exception"
    'sky':     '#38bdf8',   # strong blue: "neutral info/time/origin"
    'bg':      '#0d1117',
    'panel':   '#161b22',
    'border':  '#30363d',
    'text':    '#e6edf3',
    'muted':   '#7d8590',
}


def wrap_text(text, max_chars):
    """Greedy word-wrap. Returns list of lines, no truncation."""
    text = (text or '').strip()
    if not text:
        return []
    words = text.split()
    lines = []
    cur = ''
    for w in words:
        if not cur:
            cur = w
        elif len(cur) + 1 + len(w) <= max_chars:
            cur = cur + ' ' + w
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def escape_xml(s):
    return (s.replace('&', '&amp;')
             .replace('<', '&lt;')
             .replace('>', '&gt;')
             .replace('"', '&quot;')
             .replace("'", '&apos;'))


# -- shared SVG helpers --------------------------------------------------

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



# -- biological icon library (Lucide icons, ISC license) ---------------------
# https://github.com/lucide-icons/lucide
# Each value is the inner SVG content (paths, circles) for a 24x24 viewBox.
# Rendered by _bio_icon() inside a <g> wrapper that sets stroke color.

BIO_ICONS = {
    'arrow_down': "<path d=\"M12 5v14\" /> <path d=\"m19 12-7 7-7-7\" />",
    'arrow_r': "<path d=\"M5 12h14\" /> <path d=\"m12 5 7 7-7 7\" />",
    'arrow_up': "<path d=\"m5 12 7-7 7 7\" /> <path d=\"M12 19V5\" />",
    'atom': "<circle cx=\"12\" cy=\"12\" r=\"1\" /> <path d=\"M20.2 20.2c2.04-2.03.02-7.36-4.5-11.9-4.54-4.52-9.87-6.54-11.9-4.5-2.04 2.03-.02 7.36 4.5 11.9 4.54 4.52 9.87 6.54 11.9 4.5Z\" /> <path d=\"M15.7 15.7c4.52-4.54 6.54-9.87 4.5-11.9-2.03-2.04-7.36-.02-11.9 4.5-4.52 4.54-6.54 9.87-4.5 11.9 2.03 2.04 7.36.02 11.9-4.5Z\" />",
    'baby': "<path d=\"M10 16c.5.3 1.2.5 2 .5s1.5-.2 2-.5\" /> <path d=\"M15 12h.01\" /> <path d=\"M19.38 6.813A9 9 0 0 1 20.8 10.2a2 2 0 0 1 0 3.6 9 9 0 0 1-17.6 0 2 2 0 0 1 0-3.6A9 9 0 0 1 12 3c2 0 3.5 1.1 3.5 2.5s-.9 2.5-2 2.5c-.8 0-1.5-.4-1.5-1\" /> <path d=\"M9 12h.01\" />",
    'beaker': "<path d=\"M4.5 3h15\" /> <path d=\"M6 3v16a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V3\" /> <path d=\"M6 14h12\" />",
    'bird': "<path d=\"M16 7h.01\" /> <path d=\"M3.4 18H12a8 8 0 0 0 8-8V7a4 4 0 0 0-7.28-2.3L2 20\" /> <path d=\"m20 7 2 .5-2 .5\" /> <path d=\"M10 18v3\" /> <path d=\"M14 17.75V21\" /> <path d=\"M7 18a6 6 0 0 0 3.84-10.61\" />",
    'bolt': "<path d=\"M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z\" />",
    'bone': "<path d=\"M17 10c.7-.7 1.69 0 2.5 0a2.5 2.5 0 1 0 0-5 .5.5 0 0 1-.5-.5 2.5 2.5 0 1 0-5 0c0 .81.7 1.8 0 2.5l-7 7c-.7.7-1.69 0-2.5 0a2.5 2.5 0 0 0 0 5c.28 0 .5.22.5.5a2.5 2.5 0 1 0 5 0c0-.81-.7-1.8 0-2.5Z\" />",
    'brain': "<path d=\"M12 18V5\" /> <path d=\"M15 13a4.17 4.17 0 0 1-3-4 4.17 4.17 0 0 1-3 4\" /> <path d=\"M17.598 6.5A3 3 0 1 0 12 5a3 3 0 1 0-5.598 1.5\" /> <path d=\"M17.997 5.125a4 4 0 0 1 2.526 5.77\" /> <path d=\"M18 18a4 4 0 0 0 2-7.464\" /> <path d=\"M19.967 17.483A4 4 0 1 1 12 18a4 4 0 1 1-7.967-.517\" /> <path d=\"M6 18a4 4 0 0 1-2-7.464\" /> <path d=\"M6.003 5.125a4 4 0 0 0-2.526 5.77\" />",
    'branch': "<path d=\"M15 6a9 9 0 0 0-9 9V3\" /> <circle cx=\"18\" cy=\"6\" r=\"3\" /> <circle cx=\"6\" cy=\"18\" r=\"3\" />",
    'bug': "<path d=\"M12 20v-9\" /> <path d=\"M14 7a4 4 0 0 1 4 4v3a6 6 0 0 1-12 0v-3a4 4 0 0 1 4-4z\" /> <path d=\"M14.12 3.88 16 2\" /> <path d=\"M21 21a4 4 0 0 0-3.81-4\" /> <path d=\"M21 5a4 4 0 0 1-3.55 3.97\" /> <path d=\"M22 13h-4\" /> <path d=\"M3 21a4 4 0 0 1 3.81-4\" /> <path d=\"M3 5a4 4 0 0 0 3.55 3.97\" /> <path d=\"M6 13H2\" /> <path d=\"m8 2 1.88 1.88\" /> <path d=\"M9 7.13V6a3 3 0 1 1 6 0v1.13\" />",
    'calendar': "<path d=\"M8 2v4\" /> <path d=\"M16 2v4\" /> <rect width=\"18\" height=\"18\" x=\"3\" y=\"4\" rx=\"2\" /> <path d=\"M3 10h18\" />",
    'cat': "<path d=\"M12 5c.67 0 1.35.09 2 .26 1.78-2 5.03-2.84 6.42-2.26 1.4.58-.42 7-.42 7 .57 1.07 1 2.24 1 3.44C21 17.9 16.97 21 12 21s-9-3-9-7.56c0-1.25.5-2.4 1-3.44 0 0-1.89-6.42-.5-7 1.39-.58 4.72.23 6.5 2.23A9.04 9.04 0 0 1 12 5Z\" /> <path d=\"M8 14v.5\" /> <path d=\"M16 14v.5\" /> <path d=\"M11.25 16.25h1.5L12 17l-.75-.75Z\" />",
    'check': "<path d=\"M20 6 9 17l-5-5\" />",
    'clock': "<circle cx=\"12\" cy=\"12\" r=\"10\" /> <path d=\"M12 6v6l4 2\" />",
    'cloud': "<path d=\"M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z\" />",
    'compass': "<circle cx=\"12\" cy=\"12\" r=\"10\" /> <path d=\"m16.24 7.76-1.804 5.411a2 2 0 0 1-1.265 1.265L7.76 16.24l1.804-5.411a2 2 0 0 1 1.265-1.265z\" />",
    'cross': "<path d=\"M18 6 6 18\" /> <path d=\"m6 6 12 12\" />",
    'crown': "<path d=\"M11.562 3.266a.5.5 0 0 1 .876 0L15.39 8.87a1 1 0 0 0 1.516.294L21.183 5.5a.5.5 0 0 1 .798.519l-2.834 10.246a1 1 0 0 1-.956.734H5.81a1 1 0 0 1-.957-.734L2.02 6.02a.5.5 0 0 1 .798-.519l4.276 3.664a1 1 0 0 0 1.516-.294z\" /> <path d=\"M5 21h14\" />",
    'dna': "<path d=\"m10 16 1.5 1.5\" /> <path d=\"m14 8-1.5-1.5\" /> <path d=\"M15 2c-1.798 1.998-2.518 3.995-2.807 5.993\" /> <path d=\"m16.5 10.5 1 1\" /> <path d=\"m17 6-2.891-2.891\" /> <path d=\"M2 15c6.667-6 13.333 0 20-6\" /> <path d=\"m20 9 .891.891\" /> <path d=\"M3.109 14.109 4 15\" /> <path d=\"m6.5 12.5 1 1\" /> <path d=\"m7 18 2.891 2.891\" /> <path d=\"M9 22c1.798-1.998 2.518-3.995 2.807-5.993\" />",
    'dog': "<path d=\"M11.25 16.25h1.5L12 17z\" /> <path d=\"M16 14v.5\" /> <path d=\"M4.42 11.247A13.152 13.152 0 0 0 4 14.556C4 18.728 7.582 21 12 21s8-2.272 8-6.444a11.702 11.702 0 0 0-.493-3.309\" /> <path d=\"M8 14v.5\" /> <path d=\"M8.5 8.5c-.384 1.05-1.083 2.028-2.344 2.5-1.931.722-3.576-.297-3.656-1-.113-.994 1.177-6.53 4-7 1.923-.321 3.651.845 3.651 2.235A7.497 7.497 0 0 1 14 5.277c0-1.39 1.844-2.598 3.767-2.277 2.823.47 4.113 6.006 4 7-.08.703-1.725 1.722-3.656 1-1.261-.472-1.855-1.45-2.239-2.5\" />",
    'drop': "<path d=\"M12 22a7 7 0 0 0 7-7c0-2-1-3.9-3-5.5s-3.5-4-4-6.5c-.5 2.5-2 4.9-4 6.5C6 11.1 5 13 5 15a7 7 0 0 0 7 7z\" />",
    'egg': "<path d=\"M12 2C8 2 4 8 4 14a8 8 0 0 0 16 0c0-6-4-12-8-12\" />",
    'equal': "<line x1=\"5\" x2=\"19\" y1=\"9\" y2=\"9\" /> <line x1=\"5\" x2=\"19\" y1=\"15\" y2=\"15\" />",
    'eye': "<path d=\"M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0\" /> <circle cx=\"12\" cy=\"12\" r=\"3\" />",
    'feather': "<path d=\"M12.67 19a2 2 0 0 0 1.416-.588l6.154-6.172a6 6 0 0 0-8.49-8.49L5.586 9.914A2 2 0 0 0 5 11.328V18a1 1 0 0 0 1 1z\" /> <path d=\"M16 8 2 22\" /> <path d=\"M17.5 15H9\" />",
    'fish': "<path d=\"M6.5 12c.94-3.46 4.94-6 8.5-6 3.56 0 6.06 2.54 7 6-.94 3.47-3.44 6-7 6s-7.56-2.53-8.5-6Z\" /> <path d=\"M18 12v.5\" /> <path d=\"M16 17.93a9.77 9.77 0 0 1 0-11.86\" /> <path d=\"M7 10.67C7 8 5.58 5.97 2.73 5.5c-1 1.5-1 5 .23 6.5-1.24 1.5-1.24 5-.23 6.5C5.58 18.03 7 16 7 13.33\" /> <path d=\"M10.46 7.26C10.2 5.88 9.17 4.24 8 3h5.8a2 2 0 0 1 1.98 1.67l.23 1.4\" /> <path d=\"m16.01 17.93-.23 1.4A2 2 0 0 1 13.8 21H9.5a5.96 5.96 0 0 0 1.49-3.98\" />",
    'flame': "<path d=\"M12 3q1 4 4 6.5t3 5.5a1 1 0 0 1-14 0 5 5 0 0 1 1-3 1 1 0 0 0 5 0c0-2-1.5-3-1.5-5q0-2 2.5-4\" />",
    'flask': "<path d=\"M14 2v6a2 2 0 0 0 .245.96l5.51 10.08A2 2 0 0 1 18 22H6a2 2 0 0 1-1.755-2.96l5.51-10.08A2 2 0 0 0 10 8V2\" /> <path d=\"M6.453 15h11.094\" /> <path d=\"M8.5 2h7\" />",
    'flower': "<circle cx=\"12\" cy=\"12\" r=\"3\" /> <path d=\"M12 16.5A4.5 4.5 0 1 1 7.5 12 4.5 4.5 0 1 1 12 7.5a4.5 4.5 0 1 1 4.5 4.5 4.5 4.5 0 1 1-4.5 4.5\" /> <path d=\"M12 7.5V9\" /> <path d=\"M7.5 12H9\" /> <path d=\"M16.5 12H15\" /> <path d=\"M12 16.5V15\" /> <path d=\"m8 8 1.88 1.88\" /> <path d=\"M14.12 9.88 16 8\" /> <path d=\"m8 16 1.88-1.88\" /> <path d=\"M14.12 14.12 16 16\" />",
    'foot': "<path d=\"M4 16v-2.38C4 11.5 2.97 10.5 3 8c.03-2.72 1.49-6 4.5-6C9.37 2 10 3.8 10 5.5c0 3.11-2 5.66-2 8.68V16a2 2 0 1 1-4 0Z\" /> <path d=\"M20 20v-2.38c0-2.12 1.03-3.12 1-5.62-.03-2.72-1.49-6-4.5-6C14.63 6 14 7.8 14 9.5c0 3.11 2 5.66 2 8.68V20a2 2 0 1 0 4 0Z\" /> <path d=\"M16 17h4\" /> <path d=\"M4 13h4\" />",
    'footprints': "<path d=\"M4 16v-2.38C4 11.5 2.97 10.5 3 8c.03-2.72 1.49-6 4.5-6C9.37 2 10 3.8 10 5.5c0 3.11-2 5.66-2 8.68V16a2 2 0 1 1-4 0Z\" /> <path d=\"M20 20v-2.38c0-2.12 1.03-3.12 1-5.62-.03-2.72-1.49-6-4.5-6C14.63 6 14 7.8 14 9.5c0 3.11 2 5.66 2 8.68V20a2 2 0 1 0 4 0Z\" /> <path d=\"M16 17h4\" /> <path d=\"M4 13h4\" />",
    'fork': "<circle cx=\"12\" cy=\"18\" r=\"3\" /> <circle cx=\"6\" cy=\"6\" r=\"3\" /> <circle cx=\"18\" cy=\"6\" r=\"3\" /> <path d=\"M18 9v2c0 .6-.4 1-1 1H7c-.6 0-1-.4-1-1V9\" /> <path d=\"M12 12v3\" />",
    'fuel': "<path d=\"M14 13h2a2 2 0 0 1 2 2v2a2 2 0 0 0 4 0v-6.998a2 2 0 0 0-.59-1.42L18 5\" /> <path d=\"M14 21V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v16\" /> <path d=\"M2 21h13\" /> <path d=\"M3 9h11\" />",
    'gem': "<path d=\"M10.5 3 8 9l4 13 4-13-2.5-6\" /> <path d=\"M17 3a2 2 0 0 1 1.6.8l3 4a2 2 0 0 1 .013 2.382l-7.99 10.986a2 2 0 0 1-3.247 0l-7.99-10.986A2 2 0 0 1 2.4 7.8l2.998-3.997A2 2 0 0 1 7 3z\" /> <path d=\"M2 9h20\" />",
    'globe': "<circle cx=\"12\" cy=\"12\" r=\"10\" /> <path d=\"M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20\" /> <path d=\"M2 12h20\" />",
    'hand': "<path d=\"M18 11V6a2 2 0 0 0-2-2a2 2 0 0 0-2 2\" /> <path d=\"M14 10V4a2 2 0 0 0-2-2a2 2 0 0 0-2 2v2\" /> <path d=\"M10 10.5V6a2 2 0 0 0-2-2a2 2 0 0 0-2 2v8\" /> <path d=\"M18 8a2 2 0 1 1 4 0v6a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.86-5.99-2.34l-3.6-3.6a2 2 0 0 1 2.83-2.82L7 15\" />",
    'heart': "<path d=\"M2 9.5a5.5 5.5 0 0 1 9.591-3.676.56.56 0 0 0 .818 0A5.49 5.49 0 0 1 22 9.5c0 2.29-1.5 4-3 5.5l-5.492 5.313a2 2 0 0 1-3 .019L5 15c-1.5-1.5-3-3.2-3-5.5\" />",
    'hourglass': "<path d=\"M5 22h14\" /> <path d=\"M5 2h14\" /> <path d=\"M17 22v-4.172a2 2 0 0 0-.586-1.414L12 12l-4.414 4.414A2 2 0 0 0 7 17.828V22\" /> <path d=\"M7 2v4.172a2 2 0 0 0 .586 1.414L12 12l4.414-4.414A2 2 0 0 0 17 6.172V2\" />",
    'infinity': "<path d=\"M6 16c5 0 7-8 12-8a4 4 0 0 1 0 8c-5 0-7-8-12-8a4 4 0 1 0 0 8\" />",
    'key': "<path d=\"m15.5 7.5 2.3 2.3a1 1 0 0 0 1.4 0l2.1-2.1a1 1 0 0 0 0-1.4L19 4\" /> <path d=\"m21 2-9.6 9.6\" /> <circle cx=\"7.5\" cy=\"15.5\" r=\"5.5\" />",
    'layers': "<path d=\"M12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83z\" /> <path d=\"M2 12a1 1 0 0 0 .58.91l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9A1 1 0 0 0 22 12\" /> <path d=\"M2 17a1 1 0 0 0 .58.91l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9A1 1 0 0 0 22 17\" />",
    'leaf': "<path d=\"M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z\" /> <path d=\"M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12\" />",
    'leg': "<path d=\"M4 16v-2.38C4 11.5 2.97 10.5 3 8c.03-2.72 1.49-6 4.5-6C9.37 2 10 3.8 10 5.5c0 3.11-2 5.66-2 8.68V16a2 2 0 1 1-4 0Z\" /> <path d=\"M20 20v-2.38c0-2.12 1.03-3.12 1-5.62-.03-2.72-1.49-6-4.5-6C14.63 6 14 7.8 14 9.5c0 3.11 2 5.66 2 8.68V20a2 2 0 1 0 4 0Z\" /> <path d=\"M16 17h4\" /> <path d=\"M4 13h4\" />",
    'link': "<path d=\"M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71\" /> <path d=\"M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71\" />",
    'lock': "<rect width=\"18\" height=\"11\" x=\"3\" y=\"11\" rx=\"2\" ry=\"2\" /> <path d=\"M7 11V7a5 5 0 0 1 10 0v4\" />",
    'merge': "<circle cx=\"18\" cy=\"18\" r=\"3\" /> <circle cx=\"6\" cy=\"6\" r=\"3\" /> <path d=\"M6 21V9a9 9 0 0 0 9 9\" />",
    'microscope': "<path d=\"M6 18h8\" /> <path d=\"M3 22h18\" /> <path d=\"M14 22a7 7 0 1 0 0-14h-1\" /> <path d=\"M9 14h2\" /> <path d=\"M9 12a2 2 0 0 1-2-2V6h6v4a2 2 0 0 1-2 2Z\" /> <path d=\"M12 6V3a1 1 0 0 0-1-1H9a1 1 0 0 0-1 1v3\" />",
    'minus': "<path d=\"M5 12h14\" />",
    'moon': "<path d=\"M20.985 12.486a9 9 0 1 1-9.473-9.472c.405-.022.617.46.402.803a6 6 0 0 0 8.268 8.268c.344-.215.825-.004.803.401\" />",
    'mountain': "<path d=\"m8 3 4 8 5-5 5 15H2L8 3z\" />",
    'network': "<rect x=\"16\" y=\"16\" width=\"6\" height=\"6\" rx=\"1\" /> <rect x=\"2\" y=\"16\" width=\"6\" height=\"6\" rx=\"1\" /> <rect x=\"9\" y=\"2\" width=\"6\" height=\"6\" rx=\"1\" /> <path d=\"M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3\" /> <path d=\"M12 12V8\" />",
    'paw': "<circle cx=\"11\" cy=\"4\" r=\"2\" /> <circle cx=\"18\" cy=\"8\" r=\"2\" /> <circle cx=\"20\" cy=\"16\" r=\"2\" /> <path d=\"M9 10a5 5 0 0 1 5 5v3.5a3.5 3.5 0 0 1-6.84 1.045Q6.52 17.48 4.46 16.84A3.5 3.5 0 0 1 5.5 10Z\" />",
    'peak': "<path d=\"m8 3 4 8 5-5 5 15H2L8 3z\" />",
    'percent': "<line x1=\"19\" x2=\"5\" y1=\"5\" y2=\"19\" /> <circle cx=\"6.5\" cy=\"6.5\" r=\"2.5\" /> <circle cx=\"17.5\" cy=\"17.5\" r=\"2.5\" />",
    'pill': "<path d=\"m10.5 20.5 10-10a4.95 4.95 0 1 0-7-7l-10 10a4.95 4.95 0 1 0 7 7Z\" /> <path d=\"m8.5 8.5 7 7\" />",
    'plus': "<path d=\"M5 12h14\" /> <path d=\"M12 5v14\" />",
    'rabbit': "<path d=\"M13 16a3 3 0 0 1 2.24 5\" /> <path d=\"M18 12h.01\" /> <path d=\"M18 21h-8a4 4 0 0 1-4-4 7 7 0 0 1 7-7h.2L9.6 6.4a1 1 0 1 1 2.8-2.8L15.8 7h.2c3.3 0 6 2.7 6 6v1a2 2 0 0 1-2 2h-1a3 3 0 0 0-3 3\" /> <path d=\"M20 8.54V4a2 2 0 1 0-4 0v3\" /> <path d=\"M7.612 12.524a3 3 0 1 0-1.6 4.3\" />",
    'refresh': "<path d=\"M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8\" /> <path d=\"M21 3v5h-5\" /> <path d=\"M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16\" /> <path d=\"M8 16H3v5\" />",
    'repeat': "<path d=\"m17 2 4 4-4 4\" /> <path d=\"M3 11v-1a4 4 0 0 1 4-4h14\" /> <path d=\"m7 22-4-4 4-4\" /> <path d=\"M21 13v1a4 4 0 0 1-4 4H3\" />",
    'scale': "<path d=\"M12 3v18\" /> <path d=\"m19 8 3 8a5 5 0 0 1-6 0zV7\" /> <path d=\"M3 7h1a17 17 0 0 0 8-2 17 17 0 0 0 8 2h1\" /> <path d=\"m5 8 3 8a5 5 0 0 1-6 0zV7\" /> <path d=\"M7 21h10\" />",
    'scissors': "<circle cx=\"6\" cy=\"6\" r=\"3\" /> <path d=\"M8.12 8.12 12 12\" /> <path d=\"M20 4 8.12 15.88\" /> <circle cx=\"6\" cy=\"18\" r=\"3\" /> <path d=\"M14.8 14.8 20 20\" />",
    'shell': "<path d=\"M14 11a2 2 0 1 1-4 0 4 4 0 0 1 8 0 6 6 0 0 1-12 0 8 8 0 0 1 16 0 10 10 0 1 1-20 0 11.93 11.93 0 0 1 2.42-7.22 2 2 0 1 1 3.16 2.44\" />",
    'shield': "<path d=\"M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z\" />",
    'shuffle': "<path d=\"m18 14 4 4-4 4\" /> <path d=\"m18 2 4 4-4 4\" /> <path d=\"M2 18h1.973a4 4 0 0 0 3.3-1.7l5.454-8.6a4 4 0 0 1 3.3-1.7H22\" /> <path d=\"M2 6h1.972a4 4 0 0 1 3.6 2.2\" /> <path d=\"M22 18h-6.041a4 4 0 0 1-3.3-1.8l-.359-.45\" />",
    'skull': "<path d=\"m12.5 17-.5-1-.5 1h1z\" /> <path d=\"M15 22a1 1 0 0 0 1-1v-1a2 2 0 0 0 1.56-3.25 8 8 0 1 0-11.12 0A2 2 0 0 0 8 20v1a1 1 0 0 0 1 1z\" /> <circle cx=\"15\" cy=\"12\" r=\"1\" /> <circle cx=\"9\" cy=\"12\" r=\"1\" />",
    'snail': "<path d=\"M2 13a6 6 0 1 0 12 0 4 4 0 1 0-8 0 2 2 0 0 0 4 0\" /> <circle cx=\"10\" cy=\"13\" r=\"8\" /> <path d=\"M2 21h12c4.4 0 8-3.6 8-8V7a2 2 0 1 0-4 0v6\" /> <path d=\"M18 3 19.1 5.2\" /> <path d=\"M22 3 20.9 5.2\" />",
    'snowflake': "<path d=\"m10 20-1.25-2.5L6 18\" /> <path d=\"M10 4 8.75 6.5 6 6\" /> <path d=\"m14 20 1.25-2.5L18 18\" /> <path d=\"m14 4 1.25 2.5L18 6\" /> <path d=\"m17 21-3-6h-4\" /> <path d=\"m17 3-3 6 1.5 3\" /> <path d=\"M2 12h6.5L10 9\" /> <path d=\"m20 10-1.5 2 1.5 2\" /> <path d=\"M22 12h-6.5L14 15\" /> <path d=\"m4 10 1.5 2L4 14\" /> <path d=\"m7 21 3-6-1.5-3\" /> <path d=\"m7 3 3 6h4\" />",
    'sperm': "<path d=\"M6.5 12c.94-3.46 4.94-6 8.5-6 3.56 0 6.06 2.54 7 6-.94 3.47-3.44 6-7 6s-7.56-2.53-8.5-6Z\" /> <path d=\"M18 12v.5\" /> <path d=\"M16 17.93a9.77 9.77 0 0 1 0-11.86\" /> <path d=\"M7 10.67C7 8 5.58 5.97 2.73 5.5c-1 1.5-1 5 .23 6.5-1.24 1.5-1.24 5-.23 6.5C5.58 18.03 7 16 7 13.33\" /> <path d=\"M10.46 7.26C10.2 5.88 9.17 4.24 8 3h5.8a2 2 0 0 1 1.98 1.67l.23 1.4\" /> <path d=\"m16.01 17.93-.23 1.4A2 2 0 0 1 13.8 21H9.5a5.96 5.96 0 0 0 1.49-3.98\" />",
    'sprout': "<path d=\"M14 9.536V7a4 4 0 0 1 4-4h1.5a.5.5 0 0 1 .5.5V5a4 4 0 0 1-4 4 4 4 0 0 0-4 4c0 2 1 3 1 5a5 5 0 0 1-1 3\" /> <path d=\"M4 9a5 5 0 0 1 8 4 5 5 0 0 1-8-4\" /> <path d=\"M5 21h14\" />",
    'star': "<path d=\"M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z\" />",
    'sun': "<circle cx=\"12\" cy=\"12\" r=\"4\" /> <path d=\"M12 2v2\" /> <path d=\"M12 20v2\" /> <path d=\"m4.93 4.93 1.41 1.41\" /> <path d=\"m17.66 17.66 1.41 1.41\" /> <path d=\"M2 12h2\" /> <path d=\"M20 12h2\" /> <path d=\"m6.34 17.66-1.41 1.41\" /> <path d=\"m19.07 4.93-1.41 1.41\" />",
    'target': "<circle cx=\"12\" cy=\"12\" r=\"10\" /> <circle cx=\"12\" cy=\"12\" r=\"6\" /> <circle cx=\"12\" cy=\"12\" r=\"2\" />",
    'test_tube': "<path d=\"M14.5 2v17.5c0 1.4-1.1 2.5-2.5 2.5c-1.4 0-2.5-1.1-2.5-2.5V2\" /> <path d=\"M8.5 2h7\" /> <path d=\"M14.5 16h-5\" />",
    'thermometer': "<path d=\"M14 4v10.54a4 4 0 1 1-4 0V4a2 2 0 0 1 4 0Z\" />",
    'tree': "<path d=\"M10 10v.2A3 3 0 0 1 8.9 16H5a3 3 0 0 1-1-5.8V10a3 3 0 0 1 6 0Z\" /> <path d=\"M7 16v6\" /> <path d=\"M13 19v3\" /> <path d=\"M12 19h8.3a1 1 0 0 0 .7-1.7L18 14h.3a1 1 0 0 0 .7-1.7L16 9h.2a1 1 0 0 0 .8-1.7L13 3l-1.4 1.5\" />",
    'trophy': "<path d=\"M10 14.66v1.626a2 2 0 0 1-.976 1.696A5 5 0 0 0 7 21.978\" /> <path d=\"M14 14.66v1.626a2 2 0 0 0 .976 1.696A5 5 0 0 1 17 21.978\" /> <path d=\"M18 9h1.5a1 1 0 0 0 0-5H18\" /> <path d=\"M4 22h16\" /> <path d=\"M6 9a6 6 0 0 0 12 0V3a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1z\" /> <path d=\"M6 9H4.5a1 1 0 0 1 0-5H6\" />",
    'turtle': "<path d=\"m12 10 2 4v3a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-3a8 8 0 1 0-16 0v3a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-3l2-4h4Z\" /> <path d=\"M4.82 7.9 8 10\" /> <path d=\"M15.18 7.9 12 10\" /> <path d=\"M16.93 10H20a2 2 0 0 1 0 4H2\" />",
    'waves': "<path d=\"M2 6c.6.5 1.2 1 2.5 1C7 7 7 5 9.5 5c2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1\" /> <path d=\"M2 12c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1\" /> <path d=\"M2 18c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1\" />",
    'wind': "<path d=\"M12.8 19.6A2 2 0 1 0 14 16H2\" /> <path d=\"M17.5 8a2.5 2.5 0 1 1 2 4H2\" /> <path d=\"M9.8 4.4A2 2 0 1 1 11 8H2\" />",
    'wing': "<path d=\"M12.67 19a2 2 0 0 0 1.416-.588l6.154-6.172a6 6 0 0 0-8.49-8.49L5.586 9.914A2 2 0 0 0 5 11.328V18a1 1 0 0 0 1 1z\" /> <path d=\"M16 8 2 22\" /> <path d=\"M17.5 15H9\" />",
    'worm': "<path d=\"m19 12-1.5 3\" /> <path d=\"M19.63 18.81 22 20\" /> <path d=\"M6.47 8.23a1.68 1.68 0 0 1 2.44 1.93l-.64 2.08a6.76 6.76 0 0 0 10.16 7.67l.42-.27a1 1 0 1 0-2.73-4.21l-.42.27a1.76 1.76 0 0 1-2.63-1.99l.64-2.08A6.66 6.66 0 0 0 3.94 3.9l-.7.4a1 1 0 1 0 2.55 4.34z\" />",
}


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


# -- four-box layout (2x2 grid, colored header bands + icons) ------------

def svg_four_box(node):
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
def svg_cycle(node):
    """Circular cycle of 4 terms with big biological icons inside each circle,
    curved bezier arrows between them, and a central hub label."""
    v2 = node['v2']
    kt = v2['keyTerms']
    nc = {'teal': PAL['teal'], 'purple': PAL['purple'],
          'coral': PAL['coral'], 'pink': PAL['pink']}

    W, H = 900, 640
    cx, cy = W // 2, H // 2 + 30
    R = 186
    node_r = 82
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
def svg_hierarchy(node):
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

# -- per-node content overrides (per lecture variation) --------------------

# For cladogram nodes: real taxa instead of generic "Species A/B/C/D".
# The mapping is by node title substring.
CLADO_OVERRIDES = {
    'Tree Thinking': {
        'taxa': ['Taxon 1', 'Taxon 2', 'Taxon 3', 'Taxon 4'],
        'group_members': ['A', 'B'],
        'group_label': 'Clade',
        'subtitle': 'How to read a phylogenetic tree: tips, nodes, clades, root',
        'character_marks': [],
    },
    'Cladistics': {
        'taxa': ['Mammals', 'Birds', 'Reptiles', 'Fish'],
        'group_members': ['A', 'B', 'C'],
        'group_label': 'Amniotes (monophyletic)',
        'subtitle': 'Amniotic egg = synapomorphy uniting mammals + birds + reptiles',
        'character_marks': [
            ('trunk_to_n1', 'egg', 'Amniotic egg'),
            ('tipA', 'hand', 'Hair/milk'),
            ('tipB', 'feather', 'Feathers'),
        ],
    },
    'Parsimony': {
        'taxa': ['Shark', 'Dolphin', 'Tuna', 'Seal'],
        'group_members': ['B', 'D'],
        'group_label': 'Streamlined body (homoplasy)',
        'subtitle': 'Convergence: shark + dolphin both streamlined, but not closest relatives',
        'character_marks': [
            ('tipB', 'fish', 'Fins (convergent)'),
            ('tipD', 'fish', 'Fins (convergent)'),
        ],
    },
    'Fins to Limbs': {
        'taxa': ['Fish', 'Tiktaalik', 'Amphibian', 'Tetrapod'],
        'group_members': ['B', 'C', 'D'],
        'group_label': 'Tetrapod lineage (limbed)',
        'subtitle': 'Tiktaalik (375 Mya) = transitional fish with limb-like fins',
        'character_marks': [
            ('tipB', 'bone', 'Proto-limbs'),
            ('tipC', 'leg', 'True limbs'),
            ('tipD', 'footprints', 'Walking'),
        ],
    },
    'Feathers': {
        'taxa': ['Theropod', 'Feathered Dino', 'Archaeopteryx', 'Modern Bird'],
        'group_members': ['B', 'C', 'D'],
        'group_label': 'Feathered clade',
        'subtitle': 'Feathers evolved ~160 Mya before flight; exapted for flight in birds',
        'character_marks': [
            ('tipB', 'feather', 'Proto-feathers'),
            ('tipC', 'feather', 'Flight feathers'),
            ('tipD', 'bird', 'Powered flight'),
        ],
    },
    'Human Evolution': {
        'taxa': ['Chimpanzee', 'Australopithecus', 'H. erectus', 'H. sapiens'],
        'group_members': ['B', 'C', 'D'],
        'group_label': 'Hominin lineage',
        'subtitle': 'Bipedalism first (~6 Mya), then brain expansion (~2 Mya)',
        'character_marks': [
            ('tipB', 'footprints', 'Bipedalism'),
            ('tipC', 'brain', 'Big brain'),
            ('tipD', 'atom', 'Culture'),
        ],
    },
    'Descent with Modification': {
        'taxa': ['Wolf', 'Dog', 'Coyote', 'Fox'],
        'group_members': ['A', 'B', 'C'],
        'group_label': 'Canid family',
        'subtitle': 'Common descent + modification explains observable diversity',
        'character_marks': [
            ('trunk_top', 'dna', 'Shared DNA'),
        ],
    },
}


# For timeline nodes: per-topic era labels + dates.
TIMELINE_OVERRIDES = {
    'Pre-Darwin': {
        'era_labels': ['Greeks', 'Medieval', 'Renaissance', 'Pre-Darwin'],
        'era_dates':  ['-500 BCE', '500-1500', '1500-1750', '1750-1859'],
        'axis_past':  'ANCIENT',
        'axis_now':   '1859',
        'subtitle':   'From Aristotle\'s Scala Naturae to Lamarck — ideas before Darwin',
    },
    'Voyage of the Beagle': {
        'era_labels': ['Departure', 'S. America', 'Galápagos', 'Return'],
        'era_dates':  ['1831', '1832-1835', '1835', '1836'],
        'axis_past':  'DEC 1831',
        'axis_now':   'OCT 1836',
        'subtitle':   'Darwin\'s 5-year voyage gathering the evidence for Origin',
    },
    'Age of the Earth': {
        'era_labels': ['PRECAMBRIAN', 'PALEOZOIC', 'MESOZOIC', 'CENOZOIC'],
        'era_dates':  ['4600-541 Mya', '541-252 Mya', '252-66 Mya', '66-0 Mya'],
        'axis_past':  '4.6 BYA',
        'axis_now':   'NOW',
        'subtitle':   'Earth = 4.568 billion years; most of that is Precambrian',
    },
    'Origin of Life': {
        'era_labels': ['Hadean', 'Early Archean', 'Late Archean', 'Proterozoic'],
        'era_dates':  ['4600-4000', '4000-3500', '3500-2500', '2500-541'],
        'axis_past':  '4.6 BYA',
        'axis_now':   '541 MYA',
        'subtitle':   'Abiogenesis: prebiotic chemistry → RNA world → LUCA',
    },
    'Early Life': {
        'era_labels': ['Stromatolites', 'GOE', 'Eukaryotes', 'Multicellular'],
        'era_dates':  ['3500 Mya', '2400 Mya', '1800 Mya', '1000 Mya'],
        'axis_past':  '3.5 BYA',
        'axis_now':   '541 MYA',
        'subtitle':   'First cells → oxygen → eukaryotes → multicellularity',
    },
    'Cambrian Explosion': {
        'era_labels': ['Cambrian', 'Ordovician', 'Silurian', 'Devonian'],
        'era_dates':  ['541-485', '485-443', '443-419', '419-359'],
        'axis_past':  '541 MYA',
        'axis_now':   '359 MYA',
        'subtitle':   'Cambrian explosion: all major animal phyla in ~25 Myr',
    },
    'Mesozoic': {
        'era_labels': ['Triassic', 'Jurassic', 'Cretaceous', 'Cenozoic'],
        'era_dates':  ['252-201', '201-145', '145-66', '66-0'],
        'axis_past':  '252 MYA',
        'axis_now':   'NOW',
        'subtitle':   'Age of dinosaurs → K-T extinction → Age of mammals',
    },
}


def svg_cladogram(node):
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

    # Look up per-node content overrides by title substring match
    override = None
    for key, config in CLADO_OVERRIDES.items():
        if key.lower() in node['title'].lower():
            override = config
            break

    W, H = 900, 580
    TITLE_H = 74
    PANEL_PAD = 16
    PANEL_W = (W - PANEL_PAD * 3) // 2  # two panels side by side
    PANEL_H = H - TITLE_H - PANEL_PAD - 30

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
        f'width="100%" style="max-width:900px;display:block;margin:0 auto">',
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
    subtitle_text = (override['subtitle'] if override and 'subtitle' in override
                     else v2['definition'])
    subtitle_lines = wrap_text(subtitle_text, max_chars=90)[:1]
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
        # Layout: legend on top (spans panel), tree below
        # Or legend on left (narrower) + tree on right (wider)
        legend_w = int(pw * 0.30)
        tree_x0 = px + legend_w + 4
        tree_w = pw - legend_w - 14
        # Cladogram geometry — leave room for "Species X" labels at the right
        root_x   = tree_x0 + 30
        split1_x = tree_x0 + int(tree_w * 0.30)
        split2_x = tree_x0 + int(tree_w * 0.50)
        tip_x    = tree_x0 + int(tree_w * 0.68)
        tip_text_x = tip_x + 10

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

        # Highlight clade (draw BEHIND the tree) — bounded to panel right edge
        if group_color and group_members:
            member_ys = []
            for m in group_members:
                idx = {'A': 0, 'B': 1, 'C': 2, 'D': 3}[m]
                member_ys.append(tip_ys[idx])
            if member_ys:
                cy_min = min(member_ys) - 18
                cy_max = max(member_ys) + 18
                panel_right = px + pw - 8
                hlt_x = split2_x - 4
                hlt_w = panel_right - hlt_x
                # Solid background tint
                out.append(
                    f'<rect x="{hlt_x}" y="{cy_min}" '
                    f'width="{hlt_w}" '
                    f'height="{cy_max - cy_min}" '
                    f'fill="{group_color}" opacity="0.08" rx="12"/>'
                )
                # Dashed outline
                out.append(
                    f'<rect x="{hlt_x}" y="{cy_min}" '
                    f'width="{hlt_w}" '
                    f'height="{cy_max - cy_min}" '
                    f'fill="none" stroke="{group_color}" stroke-width="2" '
                    f'stroke-dasharray="6 4" rx="12" opacity="0.85"/>'
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

        # Tip labels: use override taxa if provided, else generic Species A-D
        species_labels = ['A', 'B', 'C', 'D']
        tip_taxa = (override['taxa'] if override and 'taxa' in override
                    else ['Species A', 'Species B', 'Species C', 'Species D'])
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
                f'fill="{PAL["text"]}">{escape_xml(tip_taxa[i])}</text>'
            )

        # Legend area (LEFT of the tree)
        lg_x = px + 18
        lg_y = py + 60
        lg_w = legend_w - 18
        # Two legend entries (the two terms this panel highlights)
        for i, (icon_key, color, term, definition) in enumerate(marks_labels):
            ey = lg_y + i * 82
            # Icon circle at top-left
            out.append(
                f'<circle cx="{lg_x + 22}" cy="{ey + 18}" r="18" '
                f'fill="{color}" fill-opacity="0.12" stroke="{color}" '
                f'stroke-width="2"/>'
            )
            out.append(_bio_icon(icon_key, lg_x + 22, ey + 18, 11, color,
                                 stroke_width=2, fill_mode='stroke'))
            # Term name next to icon
            out.append(
                f'<text x="{lg_x + 46}" y="{ey + 22}" '
                f'font-family="Georgia,serif" font-size="13" font-weight="700" '
                f'fill="{PAL["text"]}">{escape_xml(str(i+1) + ". " + term)}</text>'
            )
            # Short def below
            max_chars_legend = max(18, (lg_w - 4) // 6)
            def_lines = wrap_text(definition, max_chars=max_chars_legend)[:2]
            for li, ln in enumerate(def_lines):
                out.append(
                    f'<text x="{lg_x + 2}" y="{ey + 46 + li * 13}" '
                    f'font-family="Georgia,serif" font-size="10" '
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
        group_members=(override['group_members'] if override and 'group_members' in override
                       else ['A', 'B']),
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



def svg_timeline(node):
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
    era_bounds = [60, 220, 430, 660, 880]

    # Look up per-node timeline config
    tl_override = None
    for key, config in TIMELINE_OVERRIDES.items():
        if key.lower() in node['title'].lower():
            tl_override = config
            break
    if tl_override:
        era_labels = [s.upper() for s in tl_override['era_labels']]
        era_dates  = tl_override['era_dates']
        axis_past  = tl_override['axis_past']
        axis_now   = tl_override['axis_now']
    else:
        era_labels = ['PRECAMBRIAN', 'PALEOZOIC', 'MESOZOIC', 'CENOZOIC']
        era_dates  = ['4600-541 Mya', '541-252 Mya', '252-66 Mya', '66-0 Mya']
        axis_past  = 'PAST'
        axis_now   = 'NOW'

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
        f'fill="{PAL["muted"]}">{escape_xml(axis_past)}</text>'
        f'<text x="886" y="{axis_y + 5}" '
        f'font-family="Georgia,serif" font-size="10" letter-spacing="1" '
        f'fill="{PAL["muted"]}">{escape_xml(axis_now)}</text>'
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
def svg_process_flow(node):
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
def svg_comparison(node):
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
def svg_balance(node):
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
def svg_stages(node):
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
def svg_landscape(node):
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
def svg_network(node):
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


# -- layout picker (routing) ---------------------------------------------

CLADOGRAM_KEYWORDS = [
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
    # Special dedicated generators (must run before generic cladogram routing)
    if 'cladistics' in title:
        return svg_cladistics_special(node)
    if 'tree thinking' in title:
        return svg_tree_thinking_special(node)
    if 'parsimony' in title:
        return svg_parsimony_special(node)
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


# ---------- Main --------------------------------------------------------

def main():
    with open(DATA, 'r', encoding='utf-8') as f:
        data = json.load(f)

    quiz_total = 0
    card_total = 0
    svg_total = 0
    trans_total = 0
    trans_slides_total = 0

    for node in data['nodes']:
        node['v2']['quiz'] = expand_quiz(node)
        quiz_total += len(node['v2']['quiz'])

        node['v2']['flashcards'] = expand_flashcards(node)
        card_total += len(node['v2']['flashcards'])

        node['v2']['svg'] = pick_svg(node)
        svg_total += 1

        slides = get_transcript_slides(node)
        if slides:
            node['v2']['transcript'] = slides
            trans_total += 1
            trans_slides_total += len(slides)

    # Legacy compat: keep top-level node.quiz / node.flashcard as
    # SINGLE objects (matching legacy shape) so unpatched code paths
    # still work. flatten_data.py will overwrite node.quiz with the
    # full v2.quiz LIST for the renderer.
    for node in data['nodes']:
        first_q = node['v2']['quiz'][0]
        node['quiz'] = {
            'question':    first_q['question'],
            'correct':     first_q['correct'],
            'distractors': first_q['distractors'],
        }
        node['flashcard'] = {
            'front': node['v2']['flashcards'][0]['front'],
            'back':  node['v2']['flashcards'][0]['back'],
        }

    # Update meta
    data['meta']['v2Enriched'] = '2026-04-07'
    data['meta']['quizPerNode'] = 12
    data['meta']['flashcardsPerNode'] = 4

    with open(DATA, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Sanity check: nothing got truncated
    import re as _re
    bad = 0
    for n in data['nodes']:
        svg = n['v2'].get('svg', '')
        for tx in _re.findall(r'<text[^>]*>([^<]*)</text>', svg):
            if '\ufffd' in tx or '\u2026' in tx:
                bad += 1
    print(f'Truncated SVG text elements: {bad}')

    print(f'Quiz questions: {quiz_total} total ({quiz_total / 57:.1f} per node)')
    print(f'Flashcards:     {card_total} total ({card_total / 57:.1f} per node)')
    print(f'SVG diagrams:   {svg_total} / 57')
    print(f'Transcripts:    {trans_total} / 57 nodes ({trans_slides_total} slides total)')
    size_kb = os.path.getsize(DATA) / 1024
    print(f'data.json: {size_kb:.1f} KB')


if __name__ == '__main__':
    main()
