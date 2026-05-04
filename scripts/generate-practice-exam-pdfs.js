/* ============================================================
   generate-practice-exam-pdfs.js
   Reads public/data/practice-exams.json (4 exams) and produces
   4 PDFs styled as cumulative-final practice exams for the
   BIOL 4230 Evolution course. Uses headless Chrome for HTML→PDF.
   Output: public/practice-exams/EVOL4230_Practice_Final_Variation_*.pdf
   ============================================================ */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..');
const DATA = path.join(ROOT, 'public', 'data', 'practice-exams.json');
const TMP = path.join(ROOT, '_practice-exam-html');
const OUT_DIR = path.join(ROOT, 'public', 'practice-exams');
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';

if (!fs.existsSync(TMP)) fs.mkdirSync(TMP, { recursive: true });
if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR, { recursive: true });

const data = JSON.parse(fs.readFileSync(DATA, 'utf8'));

function escape(s) {
  return String(s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function buildExamHtml(exam) {
  const versionLabel = `Practice ${exam.id}`;
  const titleLine = `BIOL 4230 — ${exam.title}`;
  const mcRows = exam.mc.map(q => {
    const choices = q.choices
      .map((c, i) => `      <div class="choice">${String.fromCharCode(65 + i)})&nbsp; ${escape(c)}</div>`)
      .join('\n');
    return `
    <div class="q">
      <div class="stem"><b>${q.n}.</b>&nbsp; ${escape(q.q)}</div>
${choices}
    </div>`;
  }).join('\n');
  const saRows = exam.sa.map(q => `
    <div class="q sa">
      <div class="stem"><b>${q.n}.</b>&nbsp; ${escape(q.q)}</div>
      <div class="answer-space"></div>
    </div>`).join('\n');
  const ansEntries = exam.mc.map(q => `${q.n}. ${q.ans}`);
  const colSize = Math.ceil(ansEntries.length / 3);
  const cols = [
    ansEntries.slice(0, colSize),
    ansEntries.slice(colSize, colSize * 2),
    ansEntries.slice(colSize * 2),
  ];
  const ansHtml = cols.map(col => `<div class="col">${col.map(a => `<div>${a}</div>`).join('')}</div>`).join('');
  const saAnsHtml = exam.sa.map(q => `
    <div class="sa-ans">
      <div class="sa-stem"><b>${q.n}. ${escape(q.q)}</b></div>
      <div class="sa-body">${escape(q.ans)}</div>
    </div>`).join('\n');

  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>${escape(titleLine)}</title>
<style>
  @page {
    size: 8.5in 11in;
    margin: 0.7in 0.85in 0.85in 0.85in;
    @bottom-center {
      content: "${versionLabel} — Page " counter(page);
      font-family: 'Times New Roman', Times, serif;
      font-size: 9.5pt;
      color: #444;
    }
  }
  html, body {
    margin: 0; padding: 0;
    font-family: 'Times New Roman', Times, serif;
    font-size: 11pt;
    color: #111;
    line-height: 1.32;
  }
  .header {
    text-align: center;
    font-weight: 700;
    font-size: 12pt;
    margin-bottom: 6px;
  }
  .sub {
    text-align: center;
    font-size: 10pt;
    color: #555;
    margin-bottom: 14px;
  }
  .instr {
    font-size: 10.5pt;
    margin-bottom: 14px;
    line-height: 1.4;
  }
  .section-title {
    font-weight: 700;
    margin: 16px 0 8px;
    font-size: 11.5pt;
  }
  .q {
    margin: 0 0 12px 0;
    page-break-inside: avoid;
  }
  .q .stem {
    margin-bottom: 4px;
    padding-left: 1.6em;
    text-indent: -1.6em;
    font-size: 11pt;
  }
  .choice {
    padding-left: 3.2em;
    text-indent: -1.5em;
    margin-bottom: 1px;
    font-size: 10.8pt;
  }
  .q.sa .answer-space {
    border-bottom: 1px solid #888;
    height: 84px;
    margin-top: 6px;
  }
  .pagebreak { page-break-after: always; }
  .ans-key-title {
    text-align: center;
    font-weight: 700;
    font-size: 12pt;
    margin: 0 0 14px;
  }
  .ans-cols {
    display: flex;
    gap: 80px;
    justify-content: center;
    font-size: 11pt;
    line-height: 1.7;
    margin-bottom: 24px;
  }
  .ans-cols .col { min-width: 90px; }
  .sa-ans {
    margin-bottom: 14px;
    page-break-inside: avoid;
  }
  .sa-ans .sa-stem { font-size: 10.8pt; }
  .sa-ans .sa-body {
    font-size: 10.5pt;
    margin-top: 3px;
    padding-left: 1.5em;
    line-height: 1.4;
  }
</style>
</head>
<body>

<div class="header">BIOL 4230 — ${escape(exam.title)}</div>
<div class="sub">${escape(exam.subtitle)}</div>

<div class="instr">
  Cumulative practice final for BIOL 4230 (Evolution). Mark your answers to all multiple-choice
  questions on a separate sheet (this is <b>practice variation ${escape(exam.id)}</b>). Time yourself ~50 minutes
  closed-note. The answer key and sample short-answer responses are on the last pages.
</div>

<div class="section-title">Multiple choice: 3 points each</div>

${mcRows}

<div class="pagebreak"></div>

<div class="header">BIOL 4230 — ${escape(exam.title)} — Short Answer Section &nbsp;&nbsp;&nbsp; Name __________________________</div>

${saRows}

<div class="pagebreak"></div>

<div class="ans-key-title">Answer Key for ${escape(exam.title)}</div>

<div class="ans-cols">${ansHtml}</div>

<div class="section-title" style="margin-top: 18px;">Short Answer — Sample Answers</div>
${saAnsHtml}

</body>
</html>`;
}

const targets = [];
for (const exam of data.exams) {
  const html = buildExamHtml(exam);
  const htmlPath = path.join(TMP, `practice-exam-${exam.id}.html`);
  fs.writeFileSync(htmlPath, html, 'utf8');
  // ID format expected: "Final-A", "Final-B", "Final-C", "Final-D"
  // Output: EVOL4230_Practice_Final_Variation_<letter>.pdf
  const parts = exam.id.split('-');
  const letter = parts[parts.length - 1];
  const pdfName = `EVOL4230_Practice_Final_Variation_${letter}.pdf`;
  const pdfPath = path.join(OUT_DIR, pdfName);
  targets.push({ exam, htmlPath, pdfPath, pdfName });
}

console.log(`Generated ${targets.length} HTML files. Converting to PDF via headless Chrome...\n`);

for (const t of targets) {
  const fileUrl = 'file:///' + t.htmlPath.replace(/\\/g, '/');
  const pdfOut = t.pdfPath.replace(/\\/g, '/');
  const cmd = `"${CHROME}" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf-no-header --print-to-pdf="${pdfOut}" "${fileUrl}"`;
  try {
    execSync(cmd, { stdio: 'pipe' });
    const sz = fs.existsSync(t.pdfPath) ? fs.statSync(t.pdfPath).size : 0;
    console.log(`✓ ${t.pdfName}  (${(sz/1024).toFixed(1)} KB)`);
  } catch (e) {
    console.error(`✗ ${t.pdfName}  failed:`, e.message.slice(0, 200));
  }
}

console.log(`\nAll 4 PDFs written to: ${OUT_DIR}`);
