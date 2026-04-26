#!/usr/bin/env node
/**
 * Convert content-final.js (and per-exam files) into a single comprehensive markdown
 * file suitable for upload to a Claude project.
 *
 * Output:
 *   - evolution_study_guide_FULL.md    (one master file with everything)
 *   - figures/                          (copied diagrams referenced inline)
 */

const fs = require('fs');
const path = require('path');

const SRC_DIR = path.resolve(__dirname, '..', 'public');
const OUT_DIR = path.resolve('C:/Users/johnn/Desktop/evolution_study_guide_export');
const FIG_OUT = path.join(OUT_DIR, 'figures');

// Load a content file by stripping the `window.COURSE = …;` wrapper and parsing JSON.
function loadCourse(file) {
  const raw = fs.readFileSync(file, 'utf8');
  const m = raw.match(/window\.COURSE\s*=\s*(\{[\s\S]*\});?\s*$/m);
  if (!m) throw new Error(`Could not parse ${file}`);
  return JSON.parse(m[1]);
}

// HTML entity decoding (the JSON uses HTML entities for special chars).
const ENTS = {
  '&ldquo;': '"', '&rdquo;': '"', '&lsquo;': "'", '&rsquo;': "'",
  '&amp;': '&', '&lt;': '<', '&gt;': '>', '&quot;': '"',
  '&ne;': '≠', '&plusmn;': '±', '&times;': '×', '&divide;': '÷',
  '&minus;': '−', '&deg;': '°', '&micro;': 'µ', '&hellip;': '…',
  '&mdash;': '—', '&ndash;': '–', '&middot;': '·',
  '&#9888;': '⚠', '&#9989;': '✅', '&#10060;': '❌',
  '&#9745;': '☑', '&#9744;': '☐', '&#10003;': '✓', '&#10005;': '✗',
  '&#8594;': '→', '&#8592;': '←', '&#8593;': '↑', '&#8595;': '↓',
  '&nbsp;': ' ',
};
function decode(s) {
  if (typeof s !== 'string') return s;
  let out = s;
  for (const [k, v] of Object.entries(ENTS)) out = out.split(k).join(v);
  // Numeric entities
  out = out.replace(/&#(\d+);/g, (_, n) => String.fromCodePoint(Number(n)));
  out = out.replace(/&#x([0-9a-f]+);/gi, (_, n) => String.fromCodePoint(parseInt(n, 16)));
  return out;
}

const KIND_LABELS = {
  wb: 'Concept',
  yb: 'Key Insight',
  hb: 'Steps / Equations',
  trap: '⚠ Trap',
  rem: '★ Remember',
  mn: '🧠 Mnemonic',
};

function blockToMd(b) {
  const body = decode(b.body || '');
  const label = decode(b.label || '');
  switch (b.kind) {
    case 'wb':
      return `${body}\n`;
    case 'yb':
      return `> **${KIND_LABELS.yb}.** ${body}\n`;
    case 'hb':
      return `**${KIND_LABELS.hb}**\n\n${body}\n`;
    case 'trap':
      return `> **${label || KIND_LABELS.trap}**  \n> ${body.replace(/\n/g, '  \n> ')}\n`;
    case 'rem':
      return `> **${label || KIND_LABELS.rem}** ${body}\n`;
    case 'mn':
      return `> **${label || KIND_LABELS.mn}.** ${body}\n`;
    case 'table': {
      const head = (b.head || []).map(decode);
      const rows = (b.rows || []).map(r => r.map(decode));
      const headerRow = `| ${head.join(' | ')} |`;
      const sep = `| ${head.map(() => '---').join(' | ')} |`;
      const body = rows.map(r => `| ${r.map(c => c.replace(/\|/g, '\\|').replace(/\n/g, ' ')).join(' | ')} |`).join('\n');
      return `${headerRow}\n${sep}\n${body}\n`;
    }
    case 'figure': {
      const src = b.src || '';
      const cap = decode(b.caption || '');
      // Translate site path to local file path under figures/
      const fname = path.basename(src);
      return `![${cap}](figures/${fname})\n*Figure: ${cap}*\n`;
    }
    case 'svg': {
      const cap = decode(b.caption || '');
      return `*[Interactive diagram: ${b.viz || 'visualization'} — ${cap}]*\n`;
    }
    default:
      return body ? `${body}\n` : '';
  }
}

function chapterToMd(ch) {
  const lines = [];
  const num = ch.num ? `${ch.num}. ` : '';
  lines.push(`## ${num}${decode(ch.title)}`);
  if (ch.tagline) lines.push(`*${decode(ch.tagline)}*`);
  lines.push('');
  for (const sec of ch.sections || []) {
    const snum = sec.num ? `${sec.num} ` : '';
    lines.push(`### ${snum}${decode(sec.title)}`);
    lines.push('');
    for (const blk of sec.blocks || []) {
      lines.push(blockToMd(blk));
    }
  }
  return lines.join('\n');
}

function mcqToMd(q, idx) {
  const letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];
  const choices = (q.choices || []).map((c, i) => `- **${letters[i]}.** ${decode(c)}`).join('\n');
  const ans = letters[q.answer] || '?';
  const why = decode(q.why || '');
  return `**Q${idx + 1}.** ${decode(q.prompt)}

${choices}

**Answer: ${ans}** — ${why}
`;
}

function flashcardToMd(fc, idx) {
  const lines = [`**FC${idx + 1}.** ${decode(fc.q)}`, '', decode(fc.a)];
  if (fc.hint)    lines.push('', `*Hint:* ${decode(fc.hint)}`);
  if (fc.analogy) lines.push('', `*Analogy:* ${decode(fc.analogy)}`);
  if (fc.source)  lines.push('', `*Source:* ${fc.source}`);
  return lines.join('\n') + '\n';
}

function buildMd(course, label) {
  const lines = [];
  lines.push(`# ${decode(course.title)}`);
  if (course.subtitle) lines.push(`### ${decode(course.subtitle)}`);
  lines.push('');
  lines.push(`*Source export: ${label}*`);
  lines.push('');

  // Chapters
  lines.push('---\n\n# Part 1 · Notes (Chapters & Sections)\n');
  for (const ch of course.chapters || []) {
    lines.push(chapterToMd(ch));
    lines.push('---\n');
  }

  // MCQs
  if (Array.isArray(course.test) && course.test.length) {
    lines.push(`# Part 2 · Practice Questions (${course.test.length} MCQs)\n`);
    course.test.forEach((q, i) => lines.push(mcqToMd(q, i)));
    lines.push('---\n');
  }

  // Flashcards
  if (Array.isArray(course.flashcards) && course.flashcards.length) {
    lines.push(`# Part 3 · Flashcards (${course.flashcards.length})\n`);
    course.flashcards.forEach((fc, i) => lines.push(flashcardToMd(fc, i)));
  }

  return lines.join('\n');
}

// Find every figure path the course references and copy it to OUT/figures.
function collectFigures(course) {
  const set = new Set();
  function walk(blocks) {
    for (const b of blocks || []) {
      if (b.kind === 'figure' && b.src) set.add(b.src);
    }
  }
  for (const ch of course.chapters || []) {
    for (const sec of ch.sections || []) walk(sec.blocks);
  }
  return [...set];
}

function copyFigures(srcs) {
  if (!fs.existsSync(FIG_OUT)) fs.mkdirSync(FIG_OUT, { recursive: true });
  let ok = 0, miss = 0;
  for (const s of srcs) {
    const rel = s.startsWith('/') ? s.slice(1) : s;
    const from = path.join(SRC_DIR, rel);
    const to = path.join(FIG_OUT, path.basename(s));
    if (fs.existsSync(from)) {
      fs.copyFileSync(from, to);
      ok++;
    } else {
      miss++;
      console.warn('  missing figure:', from);
    }
  }
  return { ok, miss };
}

// MAIN
if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR, { recursive: true });

const finalFile = path.join(SRC_DIR, 'js', 'content-final.js');
const finalCourse = loadCourse(finalFile);

console.log('Building master markdown from content-final.js …');
const md = buildMd(finalCourse, 'content-final.js (Exam 1+2+3 + textbook + visuals)');
const outMd = path.join(OUT_DIR, 'evolution_study_guide_FULL.md');
fs.writeFileSync(outMd, md, 'utf8');
console.log('  wrote', outMd, '(', md.length.toLocaleString(), 'chars )');

console.log('Copying figures …');
const figs = collectFigures(finalCourse);
const { ok, miss } = copyFigures(figs);
console.log(`  ${ok} figures copied, ${miss} missing  (total referenced: ${figs.length})`);

// Per-exam exports too (handy if user wants smaller files)
for (const id of ['exam1', 'exam2', 'exam3']) {
  const f = path.join(SRC_DIR, 'js', `content-${id}.js`);
  if (!fs.existsSync(f)) continue;
  const c = loadCourse(f);
  const m = buildMd(c, `content-${id}.js`);
  const o = path.join(OUT_DIR, `evolution_${id}.md`);
  fs.writeFileSync(o, m, 'utf8');
  console.log(`  wrote ${o} (${m.length.toLocaleString()} chars)`);
}

console.log('Done. Output dir:', OUT_DIR);
