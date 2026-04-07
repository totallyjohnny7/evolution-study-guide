"""Helper functions for building Evolution study guide nodes from parsed lecture JSON."""
import json, os, re

LEC_DIR = os.path.join(os.path.dirname(__file__), '..', 'lectures')

def load_lec(fname):
    with open(os.path.join(LEC_DIR, f'{fname}.json'), 'r', encoding='utf-8') as f:
        return json.load(f)

def get_slides(lec_data, slide_range):
    """Return the list of slide dicts within the inclusive slide_range tuple (start, end)."""
    s, e = slide_range
    return [sl for sl in lec_data['slides'] if s <= sl['n'] <= e]

def slide_section(slide):
    """Format a single slide as a section dict with label and body.
    Label = 'Slide N: title'
    Body = verbatim MAIN TEXT + SPEAKER NOTES (if any) + VISUALS (if any).
    """
    title = slide.get('title','').strip() or '(no title)'
    label = f"Slide {slide['n']}: {title}"[:110]
    body_parts = []
    main = (slide.get('main','') or '').strip()
    notes = (slide.get('notes','') or '').strip()
    visuals = (slide.get('visuals','') or '').strip()
    if main:
        body_parts.append(main)
    if notes and notes.lower() != 'none.' and notes.lower() != 'none':
        body_parts.append(f"SPEAKER NOTES: {notes}")
    if visuals and visuals.lower() != 'none.' and visuals.lower() != 'none':
        body_parts.append(f"VISUALS: {visuals}")
    return {'label': label, 'body': '\n\n'.join(body_parts) if body_parts else '(blank slide)'}

def slides_to_sections(lec_data, slide_range):
    return [slide_section(s) for s in get_slides(lec_data, slide_range)]

def audio_section(label, body):
    """Build a lecture-audio section that will be styled distinctly on the site."""
    return {'label': f'LECTURE AUDIO — {label}', 'body': body.strip()}

def build_node(*, id, title, subtitle, color, row, heading, sections,
               quotes=None, examples=None, warnings=None, mnemonic='',
               flashcard, quiz, visual):
    node = {
        'id': id,
        'title': title,
        'subtitle': subtitle,
        'color': color,
        'row': row,
        'popup': {
            'heading': heading,
            'sections': sections,
            'quotes': quotes or [],
            'examples': examples or [],
            'warnings': warnings or [],
            'mnemonic': mnemonic,
        },
        'flashcard': flashcard,
        'quiz': quiz,
        'visual': visual,
    }
    return node
