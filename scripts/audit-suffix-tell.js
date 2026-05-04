/* Detect whether formulaic suffixes are clustered on distractors only.
   If a student notices that distractors disproportionately end in
   formulaic suffixes ("under standard assumptions",
   "in evolutionary biology", etc.) and correct answers don't, they
   can use suffix-presence as a 75%+ predictor of wrongness.

   Target: <5pp gap between suffix-rate on correct vs distractor.
*/
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const data = JSON.parse(fs.readFileSync(path.join(ROOT, 'public/data/practice-exams.json'), 'utf8'));

// Suffixes commonly used as padding in evolutionary biology MC distractors.
// If any of these end up clustered on wrong answers, that's a tell.
const SUFFIXES = [
  'under standard assumptions',
  'in evolutionary biology',
  'as described in lecture',
  'as described in the lecture material',
  'in natural populations',
  'under random mating',
  'when allele frequencies are stable',
  'under Hardy-Weinberg assumptions',
  'under directional selection',
  'in the context of evolutionary theory',
  'as observed in classic studies',
  'in evolutionary timescales',
  'in long-term studies',
  'under the modern synthesis',
  'in real biological populations',
  'across generations',
  'over geological time',
  'consistent with the breeder’s equation',
  'consistent with kin-selection theory',
  'consistent with Hamilton’s rule',
  'in keeping with neutral theory',
  'in the long run',
  'under typical field conditions',
  'as predicted by theory',
  'when the population is large',
  'when migration is negligible',
  'with no other evolutionary forces acting',
];
function hasSuffix(c) { return SUFFIXES.some(s => String(c).endsWith(s)); }

console.log('Suffix-as-tell audit:\n');
let cumCorrectWith = 0, cumCorrectTotal = 0, cumDistWith = 0, cumDistTotal = 0;
const reportLines = ['# Suffix-as-Tell Audit', ''];
for (const exam of data.exams) {
  let correctWith = 0, correctTotal = 0, distWith = 0, distTotal = 0;
  for (const q of exam.mc) {
    const correctIdx = q.ans.charCodeAt(0) - 65;
    q.choices.forEach((c, i) => {
      if (i === correctIdx) {
        correctTotal++;
        if (hasSuffix(c)) correctWith++;
      } else {
        distTotal++;
        if (hasSuffix(c)) distWith++;
      }
    });
  }
  cumCorrectWith += correctWith; cumCorrectTotal += correctTotal;
  cumDistWith += distWith; cumDistTotal += distTotal;
  const corPct = correctTotal ? (correctWith / correctTotal * 100) : 0;
  const distPct = distTotal ? (distWith / distTotal * 100) : 0;
  const gap = distPct - corPct;
  console.log(`${exam.id}:`);
  console.log(`  CORRECT  with suffix: ${correctWith}/${correctTotal} (${corPct.toFixed(0)}%)`);
  console.log(`  DISTRACT with suffix: ${distWith}/${distTotal} (${distPct.toFixed(0)}%)`);
  console.log(`  Gap: ${gap.toFixed(0)}pp ${gap > 5 ? '⚠️' : '✓'}`);
  console.log();
  reportLines.push(`### ${exam.id}`);
  reportLines.push(`- Correct with suffix: ${correctWith}/${correctTotal} (${corPct.toFixed(0)}%)`);
  reportLines.push(`- Distractor with suffix: ${distWith}/${distTotal} (${distPct.toFixed(0)}%)`);
  reportLines.push(`- Gap: ${gap.toFixed(0)}pp ${gap > 5 ? '⚠️ FAIL — suffix is a tell' : '✓ pass'}`);
  reportLines.push('');
}
const overallCorPct = cumCorrectTotal ? (cumCorrectWith / cumCorrectTotal * 100) : 0;
const overallDistPct = cumDistTotal ? (cumDistWith / cumDistTotal * 100) : 0;
const overallGap = overallDistPct - overallCorPct;
console.log(`OVERALL CORRECT  with suffix: ${cumCorrectWith}/${cumCorrectTotal} (${overallCorPct.toFixed(0)}%)`);
console.log(`OVERALL DISTRACT with suffix: ${cumDistWith}/${cumDistTotal} (${overallDistPct.toFixed(0)}%)`);
console.log(`OVERALL gap: ${overallGap.toFixed(0)}pp ${overallGap > 5 ? '⚠️ FAIL' : '✓ pass'}`);
reportLines.push('---');
reportLines.push(`**Overall:** ${overallGap.toFixed(0)}pp gap ${overallGap > 5 ? '⚠️ FAIL' : '✓ pass'}`);
fs.writeFileSync(path.join(ROOT, 'suffix-tell-audit.md'), reportLines.join('\n'), 'utf8');
console.log('\nWrote suffix-tell-audit.md');
process.exit(overallGap > 5 ? 1 : 0);
