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

_URL_RE      = re.compile(r'https?://\S+')
_PICTURE_RE  = re.compile(r'(?:File\s*)?"?(?:Picture|Graphic|Image|Figure|img|IMG|image)\d*\.(?:jpg|jpeg|png|gif|webp|svg|bmp|tif)"?', re.IGNORECASE)
_PAREN_ORIG  = re.compile(r'\s*\(originally from[^)]*\)', re.IGNORECASE)
_IMAGE_LBL   = re.compile(r'Image\s*\d+\s*:\s*', re.IGNORECASE)
_ALT_TEXT_RE = re.compile(r'\(?\s*alt\s*text\s*:\s*(?:"[^"]*")?\s*\)?', re.IGNORECASE)
_DESC_AUTO   = re.compile(r'Description\s+automatically\s+generated', re.IGNORECASE)
_HASH_LINE   = re.compile(r'#{3,}')
_TABLE_ROW   = re.compile(r'^\s*\|.*\|\s*$')
_TABLE_SEP   = re.compile(r'^\s*\|[\s:|-]+\|\s*$')
# Chart-noise detection: axis ticks, percentages, small integers alone on a line
_NUMERIC_LINE = re.compile(r'^[\s]*[-+]?\d+(?:[.,]\d+)?%?[\s]*$')
_AXIS_LABEL   = re.compile(
    r'^\s*('
    r'sex\s+ratio(?:\s*\(%\s*male\))?|'
    r'%\s*male|%\s*female|'
    r'incubation\s+temperature(?:\s*\(°?C\))?|'
    r'reproductive\s+success|'
    r'fitness|frequency|'
    r'n\s*=\s*\d+|p\s*=\s*\d+|q\s*=\s*\d+|'
    r'p\^?2|q\^?2|2pq|'
    r'counts?\s+of\s+\w+|genotypes?|'
    r'egg\s+incubation\s+temperature|'
    r'observed\s+(?:allele|genotypic?)\s+frequenc(?:y|ies)|'
    r'observed\s+genotypic?\s+counts?|'
    r'expected\s+genotypic?\s+counts?|'
    r'growth|reproduction|lifespan|'
    r'[♂♀]+|'              # lone sex symbols
    r'[a-z]{1,2}|'          # lone 1-2 letter labels (A, B, bb, Aa)
    r'\d+\s*(?:°C|°F|%)|'   # temperatures and percentages
    r')\s*$', re.IGNORECASE
)


def _parse_markdown_table(text):
    """Parse `| a | b |` markdown-style tables into rows (list of cells).

    Returns (rows, remaining_non_table_text) where rows is list-of-list-of-cells
    (header row first if detected, else None), and remaining is the original text
    with the table region removed.
    """
    lines = text.split('\n')
    table_blocks = []  # list of (start_idx, end_idx, rows)
    i = 0
    while i < len(lines):
        if _TABLE_ROW.match(lines[i]):
            start = i
            while i < len(lines) and (_TABLE_ROW.match(lines[i]) or lines[i].strip() == ''):
                i += 1
            # Collect only actual table lines (skip blank lines inside the block)
            block_lines = [l for l in lines[start:i] if _TABLE_ROW.match(l)]
            if len(block_lines) >= 2:
                rows = []
                for bl in block_lines:
                    if _TABLE_SEP.match(bl):
                        continue
                    cells = [c.strip() for c in bl.strip().strip('|').split('|')]
                    rows.append(cells)
                if rows:
                    table_blocks.append((start, i, rows))
        else:
            i += 1
    return table_blocks, lines


def _render_table_as_prose(rows):
    """Render table rows as clean bulleted lines (no markdown syntax).

    First row is treated as header. If all cells are non-empty, each data row
    becomes "header1: cell1 — header2: cell2 — ..." pattern.
    """
    if not rows:
        return ''
    # Filter out fully-empty rows
    rows = [r for r in rows if any(c.strip() for c in r)]
    if not rows:
        return ''
    # Identify header as first non-trivial row
    header = rows[0]
    data = rows[1:] if len(rows) > 1 else []
    # If header is mostly empty, treat all as data
    if sum(1 for c in header if c.strip()) < 2:
        header = None
        data = rows
    out_lines = []
    if header and data:
        # Clean header: drop empty trailing cells
        while header and not header[-1].strip():
            header.pop()
        for row in data:
            # Drop empty trailing cells
            while row and not row[-1].strip():
                row.pop()
            if not any(c.strip() for c in row):
                continue
            # Build "header: cell" pairs, skipping empty cells
            pairs = []
            for j, cell in enumerate(row):
                if not cell.strip():
                    continue
                if j < len(header) and header[j].strip():
                    pairs.append(f"{header[j].strip()}: {cell.strip()}")
                else:
                    pairs.append(cell.strip())
            if pairs:
                out_lines.append('• ' + ' — '.join(pairs))
    else:
        for row in data:
            cells = [c.strip() for c in row if c.strip()]
            if cells:
                out_lines.append('• ' + ' — '.join(cells))
    return '\n'.join(out_lines)


def _rebuild_tables(text):
    """Find markdown tables in text, rebuild them as clean bullet lists."""
    if '|' not in text:
        return text
    blocks, lines = _parse_markdown_table(text)
    if not blocks:
        return text
    # Replace each block (in reverse so indices stay valid)
    for start, end, rows in reversed(blocks):
        rendered = _render_table_as_prose(rows)
        replacement = rendered.split('\n') if rendered else []
        lines = lines[:start] + replacement + lines[end:]
    return '\n'.join(lines)


def _strip_chart_noise(text):
    """Delete orphaned chart axis labels, tick values, and legend fragments.

    An "orphan" line is a line with only a number, a percentage, or a known
    axis label string. We only drop such lines when they appear in clusters
    (>=2 consecutive) so we do not accidentally kill data in normal prose.
    """
    if not text:
        return text
    lines = text.split('\n')
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        is_noise = bool(_NUMERIC_LINE.match(line) or _AXIS_LABEL.match(line))
        if is_noise:
            # Look ahead for more noise lines
            j = i
            while j < len(lines) and (
                _NUMERIC_LINE.match(lines[j])
                or _AXIS_LABEL.match(lines[j])
                or lines[j].strip() == ''
            ):
                j += 1
            # If we found a cluster (>= 2 noise lines), drop all of them
            cluster = [l for l in lines[i:j] if _NUMERIC_LINE.match(l) or _AXIS_LABEL.match(l)]
            if len(cluster) >= 2:
                i = j
                continue
        out.append(line)
        i += 1
    return '\n'.join(out)

def _scrub_visuals(text):
    """Remove raw URLs, Picture refs, alt-text stubs, table shrapnel, chart noise."""
    if not text:
        return ''
    t = _PAREN_ORIG.sub('', text)
    t = _URL_RE.sub('', t)
    t = _PICTURE_RE.sub('', t)
    t = _ALT_TEXT_RE.sub('', t)
    t = _DESC_AUTO.sub('', t)
    t = _HASH_LINE.sub('', t)
    t = _IMAGE_LBL.sub('', t)
    # Rebuild markdown tables as clean bullets BEFORE collapsing whitespace
    t = _rebuild_tables(t)
    # Remove orphan chart axis labels and tick values
    t = _strip_chart_noise(t)
    # Collapse runs of >2 blank lines to 1 blank line (preserve paragraph breaks)
    t = re.sub(r'\n{3,}', '\n\n', t)
    # Collapse inline whitespace and trailing punctuation, but PRESERVE newlines
    lines = t.split('\n')
    cleaned = []
    for line in lines:
        if not line.strip():
            cleaned.append('')
            continue
        cl = re.sub(r'\s*,\s*,+', ',', line)
        cl = re.sub(r'[ \t]{2,}', ' ', cl)
        cl = re.sub(r' +([,.;:)])', r'\1', cl)
        cl = re.sub(r'\(\s*\)', '', cl)
        cleaned.append(cl.strip(' ,.;:'))
    t = '\n'.join(cleaned)
    # Collapse trailing/leading whitespace but preserve internal structure
    return t.strip()

def slide_section(slide):
    """Format a single slide as a section dict with label and body.
    Label = 'Slide N: title'
    Body = main + speaker notes + (scrubbed) visuals description.
    """
    title = slide.get('title','').strip() or '(no title)'
    # Scrub table shrapnel out of titles too (some titles are parsed from table headers)
    if '|' in title:
        title = re.sub(r'\|', ' ', title)
        title = re.sub(r'\s{2,}', ' ', title).strip()
        if not title:
            title = '(no title)'
    label = f"Slide {slide['n']}: {title}"[:110]
    body_parts = []
    main = (slide.get('main','') or '').strip()
    notes = (slide.get('notes','') or '').strip()
    visuals = (slide.get('visuals','') or '').strip()
    if main:
        body_parts.append(_scrub_visuals(main))
    if notes and notes.lower() not in ('none.', 'none'):
        cleaned_notes = _scrub_visuals(notes)
        if cleaned_notes:
            body_parts.append(f"SPEAKER NOTES: {cleaned_notes}")
    if visuals and visuals.lower() not in ('none.', 'none'):
        cleaned_vis = _scrub_visuals(visuals)
        # Strip any leading "File" that may be left behind
        cleaned_vis = re.sub(r'^\s*[Ff]ile\s*[:\-]?\s*', '', cleaned_vis).strip(' ,.;:')
        # Only include if meaningful descriptive text remains after scrubbing
        if cleaned_vis and len(cleaned_vis) > 8 and re.search(r'[a-zA-Z]{4,}', cleaned_vis):
            body_parts.append(f"DIAGRAM: {cleaned_vis}")
    body_parts = [p for p in body_parts if p]
    return {'label': label, 'body': '\n\n'.join(body_parts) if body_parts else '(blank slide)'}

def slides_to_sections(lec_data, slide_range):
    out = []
    for s in get_slides(lec_data, slide_range):
        sec = slide_section(s)
        body = sec['body'].strip()
        label = sec['label']
        # Skip orphan slides: blank, placeholder, or body that just repeats the title
        title_part = label.split(':', 1)[-1].strip().lower()
        body_norm = body.lower()
        if body == '(blank slide)':
            continue
        if body_norm == title_part:
            continue
        if body_norm in ('no text content', 'no text', '(no title)'):
            continue
        if len(body) < 20 and not re.search(r'\w{4,}', body):
            continue
        out.append(sec)
    return out

def audio_section(label, body):
    """Build a lecture-transcript section (historical name: audio_section).

    Despite the name, there is no audio playback — the body is plain transcript
    text from the lecture recording. Labeled "LECTURE TRANSCRIPT — ..." to avoid
    implying playable audio that does not exist.
    """
    return {'label': f'LECTURE TRANSCRIPT — {label}', 'body': body.strip()}

def build_node(*, id, title, subtitle, color, row, heading, sections,
               quotes=None, examples=None, warnings=None, mnemonic='',
               flashcard, quiz, visual, diagram=None):
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
    if diagram is not None:
        node['diagram'] = diagram
    return node
