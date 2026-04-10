"""
Phase 4 rewrite: strip SLIDE sections, bulletize prose, apply glossary format.
Modifies data.json in place, then injects into index.html.

Usage:  python _work/rewrite_all.py
"""
import json, re, os, sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT      = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_JSON = os.path.join(ROOT, 'data.json')
HTML_DEV  = os.path.join(ROOT, 'public', 'index.html')
HTML_PROD = os.path.join(ROOT, 'public', 'index_prod.html')
AUDIT_DIR = os.path.join(ROOT, 'audit', 'analysis')

os.makedirs(AUDIT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def is_slide_section(label: str) -> bool:
    """True if label is a raw slide dump."""
    l = label.strip().upper()
    return l.startswith('SLIDE') or 'TRANSCRIPT' in l or 'SPEAKER NOTES' in l

def is_table_body(body: str) -> bool:
    """Body uses markdown pipe-table syntax."""
    lines = [ln for ln in body.split('\n') if ln.strip()]
    pipe_lines = sum(1 for ln in lines if '|' in ln)
    return pipe_lines >= 3

def is_glossary_body(body: str) -> bool:
    """Body has TERM — Definition pattern on multiple lines."""
    lines = [ln.strip() for ln in body.split('\n') if ln.strip()]
    dash_lines = sum(1 for ln in lines if ' — ' in ln or ' - ' in ln)
    return dash_lines >= 2

def prose_to_bullets(body: str) -> str:
    """
    Convert unstructured prose to bullet list.
    - Split on newlines first.
    - Long single-paragraph text: split into sentences → bullets.
    - Already-bulleted text: pass through.
    Returns string with lines starting '• ' or numbered.
    """
    # Already structured?
    lines = [ln.strip() for ln in body.split('\n') if ln.strip()]
    if not lines:
        return body

    # Check if already has bullets/numbers
    bulletted = sum(1 for ln in lines if ln.startswith('•') or ln.startswith('-') or re.match(r'^\d+[.)]\s', ln))
    if bulletted > len(lines) * 0.4:
        return body  # already structured enough

    # Check for ALL-CAPS label lines (renderer handles those natively)
    caps_labels = sum(1 for ln in lines if re.match(r'^[A-Z][A-Z0-9 ()\/#&+\-]+:', ln) and len(ln) < 80)

    # If only 1-2 lines, keep as prose
    if len(lines) <= 2:
        return body

    # Split long single paragraph into sentences
    if len(lines) == 1 and len(body) > 200:
        # Split on '. ' boundaries
        sentences = re.split(r'(?<=[.!?])\s+', body.strip())
        sentences = [s.strip() for s in sentences if s.strip() and len(s.strip()) > 10]
        if len(sentences) >= 2:
            return '\n'.join('• ' + s for s in sentences)
        return body

    # Multiple lines but not bulleted — check if they're distinct facts
    result = []
    for ln in lines:
        # Skip pure separators
        if set(ln) <= set('-= '):
            continue
        # ALL-CAPS labels pass through (renderer handles them)
        if re.match(r'^[A-Z][A-Z0-9 ()\/#&+\-]+:', ln) and len(ln) < 80:
            result.append(ln)
        elif ln.startswith('•') or ln.startswith('-') or re.match(r'^\d+[.)]\s', ln):
            result.append(ln)
        else:
            # Convert to bullet if it's a full sentence
            if len(ln) > 30:
                result.append('• ' + ln)
            else:
                result.append(ln)
    return '\n'.join(result) if result else body

def table_to_glossary(body: str) -> str:
    """Convert markdown pipe table to TERM — definition lines."""
    lines = [ln for ln in body.split('\n') if ln.strip()]
    result = []
    for ln in lines:
        ln = ln.strip()
        if set(ln) <= set('|-: '):
            continue  # separator row
        if '|' in ln:
            cells = [c.strip() for c in ln.split('|') if c.strip()]
            if len(cells) >= 2:
                result.append(f'{cells[0]} — {" | ".join(cells[1:])}')
        else:
            result.append(ln)
    return '\n'.join(result)

def clean_section_body(body: str, label: str = '') -> str:
    """Clean up a section body: remove speaker notes, extra whitespace."""
    # Remove SPEAKER NOTES blocks
    body = re.sub(r'SPEAKER NOTES:.*?(?=\n[A-Z]|\Z)', '', body, flags=re.DOTALL | re.IGNORECASE)
    # Collapse multiple blank lines
    body = re.sub(r'\n{3,}', '\n\n', body)
    # Strip
    body = body.strip()
    return body

def extract_slide_key_facts(slide_sections: list) -> list:
    """
    From SLIDE sections, extract unique facts not already in structural sections.
    Returns list of bullet strings.
    """
    seen = set()
    facts = []
    for s in slide_sections:
        body = clean_section_body(s['body'])
        lines = [ln.strip() for ln in body.split('\n') if ln.strip()]
        for ln in lines:
            # Skip slide titles (repeated in label), short noise, speaker notes
            if len(ln) < 20:
                continue
            if 'SPEAKER NOTES' in ln.upper():
                continue
            # Deduplicate
            key = ln.lower()[:60]
            if key in seen:
                continue
            seen.add(key)
            facts.append(ln)
    return facts

def process_node(n: dict) -> tuple:
    """
    Rewrite a node's popup sections.
    Returns (new_sections, analysis_report).
    """
    pop = n.get('popup', {})
    sections = pop.get('sections', []) or []
    title = n.get('title', n['id'])

    slide_secs = [s for s in sections if is_slide_section(s['label'])]
    core_secs  = [s for s in sections if not is_slide_section(s['label'])]

    analysis_lines = [
        f'# {title}',
        f'**ID:** `{n["id"]}`',
        f'',
        f'**What it is:** {n.get("subtitle", "")}',
        f'',
        f'**Current format:**',
        f'- Total sections: {len(sections)}',
        f'- SLIDE sections: {len(slide_secs)} (dropped)',
        f'- Core sections: {len(core_secs)} (kept + reformatted)',
        f'- Total chars: {sum(len(s["body"]) for s in sections)}',
        f'',
        f'**Problems identified:**',
    ]

    problems = []
    if len(slide_secs) > 0:
        problems.append(f'- {len(slide_secs)} SLIDE dump sections removed (raw slide OCR)')
    prose_walls = [s for s in core_secs if len(s['body']) > 300 and '\n' not in s['body'][:100]]
    if prose_walls:
        problems.append(f'- {len(prose_walls)} prose-wall sections → converted to bullets')
    table_secs = [s for s in core_secs if is_table_body(s['body'])]
    if table_secs:
        problems.append(f'- {len(table_secs)} pipe-table sections → converted to glossary format')
    gloss_secs = [s for s in core_secs if is_glossary_body(s['body'])]
    if gloss_secs and not table_secs:
        problems.append(f'- {len(gloss_secs)} definition sections → glossary format applied')

    if not problems:
        problems.append('- Content already well-structured')

    analysis_lines.extend(problems)

    # Build new sections
    new_sections = []

    for s in core_secs:
        label = s['label']
        body  = clean_section_body(s['body'], label)
        fmt   = s.get('format', '')

        if not body:
            continue

        # Table body → glossary
        if is_table_body(body):
            body = table_to_glossary(body)
            fmt = 'glossary'
        # Glossary-style body
        elif is_glossary_body(body) and 'CORE CONCEPT' not in label.upper():
            fmt = 'glossary'
        # Long prose → bullets (but keep CORE CONCEPT as prose)
        elif (len(body) > 200
              and 'CORE CONCEPT' not in label.upper()
              and not body.startswith('•')
              and not fmt):
            body = prose_to_bullets(body)

        sec = {'label': label, 'body': body}
        if fmt:
            sec['format'] = fmt
        new_sections.append(sec)

    # If we dropped SLIDE sections but have < 3 remaining, salvage key facts
    if len(new_sections) < 3 and slide_secs:
        facts = extract_slide_key_facts(slide_secs)
        if facts:
            # Add up to 8 key facts as a bullets section
            facts_body = '\n'.join('• ' + f for f in facts[:8])
            new_sections.append({
                'label': 'KEY POINTS',
                'body': facts_body
            })

    # Handle nodes with NO non-slide content at all
    if not new_sections and sections:
        facts = extract_slide_key_facts(sections)
        if facts:
            new_sections.append({
                'label': 'CORE CONCEPT',
                'body': '\n'.join('• ' + f for f in facts[:6])
            })

    orig_chars = sum(len(s['body']) for s in sections)
    new_chars  = sum(len(s['body']) for s in new_sections)
    reduction  = round((1 - new_chars / max(orig_chars, 1)) * 100) if orig_chars else 0

    analysis_lines.extend([
        f'',
        f'**Better format:** Bullets + structured labels, glossary for definitions',
        f'',
        f'**Result:**',
        f'- New sections: {len(new_sections)} (was {len(sections)})',
        f'- New chars: {new_chars} (was {orig_chars}, {reduction}% reduction)',
    ])

    # Transcript integration note
    row = n.get('row', 0)
    transcript_map = {
        1: 'lec1.json', 2: 'lec2.json', 3: 'lec3.json', 4: 'lec4.json',
        5: 'lec5_6.json', 6: 'lec7.json', 7: 'lec8.json', 8: 'lec9.json',
        9: 'lec10_11.json', 10: 'lec12.json', 11: 'lec13.json',
        12: 'lec14.json', 13: 'lec15.json',
    }
    if row in transcript_map:
        analysis_lines.append(f'**Transcript:** {transcript_map[row]} — available for cross-reference')

    return new_sections, '\n'.join(analysis_lines)

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def inject_into_html(html: str, blob_json: str) -> str:
    """Replace the JSON blob in the HTML script tag."""
    return re.sub(
        r'(<script id="sd" type="application/json">)[\s\S]*?(</script>)',
        r'\g<1>' + blob_json + r'\g<2>',
        html
    )

def main():
    with open(DATA_JSON, encoding='utf-8') as f:
        data = json.load(f)

    nodes = data['nodes']
    report_rows = []

    for n in nodes:
        old_sections = n.get('popup', {}).get('sections', []) or []
        old_chars = sum(len(s['body']) for s in old_sections)
        old_fmt = 'prose/slide-dump' if any(s['label'].upper().startswith('SLIDE') for s in old_sections) else 'prose'

        new_sections, analysis_md = process_node(n)

        # Write analysis file
        slug = n['id']
        with open(os.path.join(AUDIT_DIR, f'{slug}.md'), 'w', encoding='utf-8') as f:
            f.write(analysis_md)

        # Apply new sections
        n['popup']['sections'] = new_sections

        new_chars = sum(len(s['body']) for s in new_sections)
        reduction = round((1 - new_chars / max(old_chars, 1)) * 100) if old_chars else 0

        # Transcript check
        has_transcript_row = n.get('row', 0) in range(1, 14)

        report_rows.append({
            'id': n['id'],
            'title': n.get('title', ''),
            'old_sections': len(old_sections),
            'new_sections': len(new_sections),
            'old_chars': old_chars,
            'new_chars': new_chars,
            'reduction': reduction,
            'old_fmt': old_fmt,
            'transcript': 'y' if has_transcript_row else 'n',
        })

        print(f'{n["id"]:45s} {len(old_sections):2d}sec -> {len(new_sections):2d}sec | {old_chars:5d} -> {new_chars:5d} chars ({reduction:3d}% reduction)')

    # Write updated data.json
    with open(DATA_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'\nWrote {DATA_JSON}')

    # Inject into HTML files
    blob_json = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    for html_path in (HTML_DEV, HTML_PROD):
        if not os.path.exists(html_path):
            continue
        with open(html_path, encoding='utf-8') as f:
            html = f.read()
        html = inject_into_html(html, blob_json)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Patched {html_path}')

    # Write REPORT.md
    report_path = os.path.join(ROOT, 'audit', 'REPORT.md')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('# Evolution Study Guide — Audit Report\n')
        f.write(f'**Date:** 2026-04-09\n\n')
        f.write('## Before / After Summary\n\n')
        f.write('| Node | Title | Old Secs | New Secs | Old Chars | New Chars | Reduction | Transcript |\n')
        f.write('|------|-------|----------|----------|-----------|-----------|-----------|------------|\n')
        for r in report_rows:
            f.write(f"| `{r['id']}` | {r['title'][:40]} | {r['old_sections']} | {r['new_sections']} | {r['old_chars']} | {r['new_chars']} | {r['reduction']}% | {r['transcript']} |\n")

        total_old = sum(r['old_chars'] for r in report_rows)
        total_new = sum(r['new_chars'] for r in report_rows)
        total_red = round((1 - total_new / max(total_old, 1)) * 100)
        f.write(f'\n**Total content reduction: {total_red}% ({total_old:,} → {total_new:,} chars)**\n')

    print(f'Wrote {report_path}')
    print(f'\nTotal content reduction: {total_red}% ({total_old:,} -> {total_new:,} chars)')

if __name__ == '__main__':
    main()
