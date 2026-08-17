/* =========================================================================
 *  마커 밀도 — 67곳에 얼굴 마커를 얹으면 어떻게 되는가
 *
 *  게임 저장소 tools/check-mapdata.js §3 의 재계산이다. 두 가지를 더 본다.
 *    1. 겹침이 지도의 «종횡비»에 얼마나 좌우되는가 (원본은 현재 종횡비 하나만 봤다)
 *    2. 겹치지 않게 동시에 놓을 수 있는 마커가 몇 개인가 (크기 ↔ 개수 맞바꿈)
 *
 *  결론 — 밀도는 배치로 풀리지 않는다. 겹침 0 에 필요한 지도 높이는 화면의 28배다.
 *         「67곳을 한꺼번에 보여주지 않는 규칙」이 있어야 한다.
 *
 *  실행:  node marker_density.js  [게임저장소경로]
 *  기본값: ~/Desktop/Projects/three-kingdoms
 * ========================================================================= */
'use strict';
const fs = require('fs');
const vm = require('vm');
const path = require('path');
const os = require('os');

const GAME = process.argv[2] || path.join(os.homedir(), 'Desktop/Projects/three-kingdoms');
const dataPath = path.join(GAME, 'js', 'data.js');
if (!fs.existsSync(dataPath)) {
  console.error(`게임 저장소를 찾지 못했다: ${dataPath}`);
  console.error('사용:  node marker_density.js /path/to/three-kingdoms');
  process.exit(1);
}

const sb = { console }; sb.globalThis = sb; vm.createContext(sb);
vm.runInContext(fs.readFileSync(dataPath, 'utf8'), sb, { filename: 'data.js' });
const D = vm.runInContext('({ CITIES, PASSES })', sb);

const pts = [
  ...D.CITIES.map(c => ({ name: c.name, nx: c.nx, ny: c.ny, kind: 'city', size: c.size })),
  ...D.PASSES.map(p => ({ name: p.name, nx: p.nx, ny: p.ny, kind: 'pass', size: 0 })),
];

const W = 941;                 // 기준 폭. 겹침은 폭에 비례하므로 어느 해상도든 같다
const MARKER = 0.083;          // 목업 실측 78/941
const MAP_ASPECT_NOW = 378 / 640;   // 현재 지도의 종횡비

const dist = (a, b, H) => Math.hypot((a.nx - b.nx) * W, (a.ny - b.ny) * H);

function overlap(H, m) {
  let pairs = 0; const hit = new Set(); let worst = 0; const deg = [];
  for (let i = 0; i < pts.length; i++) {
    let d = 0;
    for (let j = 0; j < pts.length; j++) {
      if (i === j) continue;
      if (dist(pts[i], pts[j], H) < m) { d++; if (j > i) { pairs++; hit.add(i); hit.add(j); } }
    }
    deg.push([pts[i].name, d]); worst = Math.max(worst, d);
  }
  deg.sort((a, b) => b[1] - a[1]);
  return { pairs, hit: hit.size, worst, busiest: deg.slice(0, 8) };
}

/** 큰 도시 우선으로, 겹치지 않게 놓을 수 있는 만큼 놓는다 */
function fit(H, m) {
  const keep = [];
  for (const p of [...pts].sort((a, b) => b.size - a.size)) {
    if (keep.every(q => dist(p, q, H) >= m)) keep.push(p);
  }
  return keep;
}

const head = s => console.log('\n' + s + '\n' + '─'.repeat(64));

console.log(`지점 ${pts.length}곳 (도시 ${D.CITIES.length} + 관문 ${D.PASSES.length})`);
console.log(`마커 = 화면 폭의 ${(MARKER * 100).toFixed(1)}%  →  폭 ${W} 기준 ${Math.round(MARKER * W)}px`);

head('1. 겹침은 지도 종횡비에 좌우된다');
console.log('  지도높이  종횡비   겹치는쌍  겹치는곳   최다');
const rows = [Math.round(W * MAP_ASPECT_NOW), 700, 900, 1100, 1300, 1421, 1672, 2000, 2500, 3000];
for (const H of rows) {
  const r = overlap(H, MARKER * W);
  const tag = H === Math.round(W * MAP_ASPECT_NOW) ? '  ← 현재 640×378 종횡비'
            : H === 1421 ? '  ← 콘텐츠 영역(85%)을 채움' : '';
  console.log(`  ${String(H).padStart(6)}  ${(H / W).toFixed(2).padStart(5)}  ${String(r.pairs).padStart(7)}`
            + `  ${String(r.hit).padStart(4)}/${pts.length}  ${String(r.worst).padStart(5)}${tag}`);
}

/* ── 겹침 0 은 도달 가능한가 ────────────────────────────────────────
 * 주의: 세로 거리가 0 인 쌍은 높이를 아무리 늘려도 멀어지지 않는다.
 *       늘리기는 «세로» 간격만 벌리기 때문이다.
 *       (이 함정에 두 번 걸렸다 — 반복 상한을 답으로 읽었다.) */
head('1-1. 겹침 0 은 도달 가능한가 — 아니다');
const stuck = [];
for (let i = 0; i < pts.length; i++) {
  for (let j = i + 1; j < pts.length; j++) {
    if (pts[i].ny !== pts[j].ny) continue;
    const gap = Math.abs(pts[i].nx - pts[j].nx) * W;
    if (gap < MARKER * W) stuck.push([pts[i].name, pts[j].name, gap]);
  }
}
if (stuck.length) {
  console.log('  세로 거리가 0 이라 «높이와 무관하게» 영원히 겹치는 쌍:');
  stuck.forEach(([a, b, g]) => console.log(`    ${a} · ${b}  —  가로 간격 ${g.toFixed(1)}px < 마커 ${Math.round(MARKER * W)}px`));
  console.log('  → 늘리기는 세로 간격만 벌린다. 이 쌍은 원리적으로 분리되지 않는다.');
}
const stuckKey = new Set(stuck.map(([a, b]) => a + '|' + b));
const pairsExcl = H => {
  let n = 0;
  for (let i = 0; i < pts.length; i++)
    for (let j = i + 1; j < pts.length; j++) {
      if (stuckKey.has(pts[i].name + '|' + pts[j].name)) continue;
      if (dist(pts[i], pts[j], H) < MARKER * W) n++;
    }
  return n;
};
let H = 1000, CAP = 200000;
while (H < CAP && pairsExcl(H) > 0) H += 100;
console.log(`\n  그 쌍을 빼면 겹침 0 높이: ${H >= CAP ? '상한 내에 없음' : H + 'px'}`
          + (H < CAP ? `  (화면 1672 의 ${(H / 1672).toFixed(0)}배 · 콘텐츠 1421 의 ${(H / 1421).toFixed(0)}배)` : ''));
console.log('  → 어느 쪽이든 배치로는 풀리지 않는다. 보여주는 규칙이 «필수»다.');

head('2. 크기 ↔ 개수 맞바꿈 — 겹치지 않게 동시에 놓을 수 있는 마커 수');
const sizes = [0.083, 0.064, 0.040, 0.026];
console.log('  지도높이   ' + sizes.map(s => `${Math.round(s * W)}px`.padStart(6)).join('   '));
for (const h of [Math.round(W * MAP_ASPECT_NOW), 1421, 1672]) {
  console.log(`  ${String(h).padStart(6)}   ` + sizes.map(s => `${fit(h, s * W).length}곳`.padStart(6)).join('   '));
}
console.log('\n  현재 빌드가 67곳을 다 찍는 것은 마커가 24px 이기 때문이고,');
console.log('  목업이 얼굴 마커를 쓸 수 있었던 것은 5개만 얹었기 때문이다. 둘 다는 안 된다.');

head('3. 1421 높이 · 78px 에서 살아남는 곳');
const keep = fit(1421, MARKER * W);
const dropped = pts.filter(p => !keep.includes(p));
console.log(`  남는 ${keep.length}곳 — ${keep.map(p => p.name).join(' ')}`);
console.log(`\n  빠지는 ${dropped.length}곳 — ${dropped.map(p => p.name).join(' ')}`);
console.log(`\n  빠지는 것 중 관문 ${dropped.filter(p => p.kind === 'pass').length}`
          + ` / 도시 ${dropped.filter(p => p.kind === 'city').length}`);
console.log('  → 버려지는 것이 무작위가 아니다. 붐비는 중원과 관문에 몰린다.');
