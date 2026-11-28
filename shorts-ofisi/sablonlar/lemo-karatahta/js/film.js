// "Gökyüzü neden mavi?" as data: one front panel (FL, x 0…3200) read in three columns, the right panel (FR, x 3200…6400)
// for the sunset, one wipe of the pupil's guess, a vertical 9:16 camera that pans column to column.
// Units: world = the board's slate (x 0…6400, y 0…1700). No sliding panel, no wet band, no painted grids.
import { clamp, lerp, eio } from '/core/lib.js';
import { Stroke, catmull } from './chalk.js';
import { writeLatin, latinWidth } from './hand.js';
import { TIMING } from './timing.js';

const norm = s => s.replace(/İ/g, 'i').replace(/I/g, 'ı').toLowerCase().replace(/[^a-zçğıöşü0-9]/g, '');
const needOf = txt => Math.max(1.5, txt.replace(/\s/g, '').length / 15 + 1.5);

export function build(W = 1080, H = 1920) {
  const S = [], TX = [], EV = [], SUBS = [], T = {};
  const { segs, words, caps, total } = TIMING;
  const SG = Object.fromEntries(segs.map(s => [s.i, s]));
  const Wd = (p, ln, nth = 0) => { const h = words.filter(w => w.line === ln && norm(w.w).startsWith(norm(p))); return h.length ? h[Math.min(nth, h.length - 1)].s : SG[ln].start; };
  const add = (arr, layer, phase = 'pre') => { arr.forEach(s => { s.layer = layer; s.phase = phase; S.push(s); }); return arr; };
  const text = (id, txt, layer, strokes, t1 = 1e9, pad = 6) => {
    let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
    for (const s of strokes) for (const [x, y] of s.pts) { x0 = Math.min(x0, x); y0 = Math.min(y0, y); x1 = Math.max(x1, x); y1 = Math.max(y1, y); }
    TX.push({ id, text: txt, layer, box: [x0 - pad, y0 - pad, x1 + pad, y1 + pad], t0: strokes[0].t0, t1 });
  };
  const line = (pts, o, t0, dur) => { const s = new Stroke(o.smooth ? catmull(pts, 10) : pts, { kind: 'write', taper: .2, taperLen: .2, land: .6, skip: .14, endSpecks: true, specks: .6, w: 8, color: 'white', ...o }); s.t0 = t0; s.t1 = t0 + dur; return s; };
  const lat = (txt, cx, by, cap, t, o = {}) => writeLatin(txt, cx - latinWidth(txt, cap, o.hand === 'child' ? 'child' : 'main') / 2, by, cap, t, o);
  const latL = (txt, x, by, cap, t, o = {}) => writeLatin(txt, x, by, cap, t, o);
  const arrow = (a, b, t0, dur, o = {}) => {              // a straight chalk arrow a → b with a two-stroke head
    const ang = Math.atan2(b[1] - a[1], b[0] - a[0]), L = o.head ?? 34;
    const sh = line([a, b], { taper: .05, ...o }, t0, dur);
    const hd = line([[b[0] + Math.cos(ang + 2.6) * L, b[1] + Math.sin(ang + 2.6) * L], b, [b[0] + Math.cos(ang - 2.6) * L, b[1] + Math.sin(ang - 2.6) * L]], { taper: .1, ...o }, t0 + dur + .01, .1);
    return [sh, hd];
  };
  const circle = (cx, cy, r, t0, dur, o = {}) => { const P = []; for (let k = 0; k <= 24; k++) { const a = -Math.PI / 2 + k / 24 * Math.PI * 2.04; P.push([cx + Math.cos(a) * r, cy + Math.sin(a) * r * .97]); } return line(P, { smooth: true, taper: .04, ...o }, t0, dur); };

  // subtitles: the caption chunks from the voice timing (Turkish only)
  caps.forEach((c, k) => { SUBS.push({ id: 'c' + k, t0: c.s, t1: c.e, tr: c.tr }); EV.push({ t: c.s, type: 'sub', t1: c.e, tr: c.tr }); });
  segs.forEach(s => EV.push({ t: s.start, type: 'vo', id: 'l' + s.i }));

  // ───────── column A (cx 560): the question; the pupil's guess already on the board, wiped; the truth in its place
  const A = 560;
  const kid = add(lat('Denizin rengi mi?', A, 720, 68, -6, { hand: 'child', seed: 7, lspeed: 400 }), 'FL');
  kid.forEach(s => { s.t0 -= 0; s.wiped = true; });
  text('kid', 'Denizin rengi mi?', 'FL', kid, 0);
  let t = .08;
  const t1 = add(lat('Gökyüzü', A, 290, 120, t, { seed: 4, lspeed: 55 }), 'FL'); t = t1.end + .05;
  const t2a = add(latL('neden', A - 330, 470, 110, t, { seed: 5, lspeed: 60 }), 'FL'); t = t2a.end + .05;
  const t2b = add(latL('mavi?', t2a.x + 50, 470, 110, t, { seed: 6, lspeed: 60, color: 'blue' }), 'FL');
  text('title', 'Gökyüzü neden mavi?', 'FL', [...t1, ...t2a, ...t2b]);
  T.wipe0 = Math.max(t2b.end + .15, Wd('çünkü', 1) - .1); T.wipe1 = T.wipe0 + .55;
  const wipe = { t0: T.wipe0, t1: T.wipe1, w: 150, path: catmull([[150, 690], [560, 676], [990, 690]], 10) };
  EV.push({ t: T.wipe0, type: 'wipe', d: .55 });
  t = Math.max(T.wipe1 + .05, Wd('güneş', 1) - .1);
  const g1 = add(lat('Güneş ışığı', A, 720, 80, t, { seed: 8, lspeed: 70 }), 'FL', 'post'); t = Math.max(g1.end + .05, Wd('beyaz', 1) - .15);
  const g2 = add(lat('= beyaz', A, 860, 80, t, { seed: 9, lspeed: 70 }), 'FL', 'post');
  text('gunes', 'Güneş ışığı = beyaz', 'FL', [...g1, ...g2]);
  // the sun: a circle and eight rays
  t = Wd('güneş', 1) + .1;
  const SUN = [A, 1050];
  const sun = [circle(SUN[0], SUN[1], 80, t, .5, { w: 9 })];
  for (let k = 0; k < 8; k++) { const a = k / 8 * Math.PI * 2; sun.push(line([[SUN[0] + Math.cos(a) * 105, SUN[1] + Math.sin(a) * 105], [SUN[0] + Math.cos(a) * 140, SUN[1] + Math.sin(a) * 140]], { w: 8 }, t + .5 + k * .05, .07)); }
  add(sun, 'FL', 'post');

  // ───────── column B (cx 1720): white light fans out into the colours; then the molecules scatter it
  const B = 1720;
  t = SG[2].start + .15;
  const ray = add([line([[SUN[0] + 150, SUN[1] - 40], [1100, 760], [1330, 430]], { w: 10, smooth: true, taper: .03 }, t, .55)], 'FL', 'post');
  const O = [1330, 430]; t += .6;
  const names = ['kırmızı', 'turuncu', 'sarı', 'yeşil', 'mavi', 'mor'], cols = [];
  names.forEach((n, k) => {
    const y = 210 + k * 88, end = [1640, y];
    const st = add([line([O, end], { w: 7, taper: .06 }, t + k * .14, .16)], 'FL', 'post');
    const wd = add(latL(n, 1670, y + 22, 52, t + k * .14 + .1, { seed: 20 + k, lspeed: 180, color: n === 'mavi' ? 'blue' : 'white' }), 'FL', 'post');
    cols.push(...st, ...wd);
  });
  text('renkler', names.join(' '), 'FL', cols);
  // molecules (line 3)
  t = Wd('ışık', 3) + .05;
  const MOL = [[1400, 960, 46, 'N2'], [1720, 880, 52, 'O2'], [1990, 1010, 46, 'N2'], [1660, 1120, 40, 'N2']];
  const mol = [];
  add([line([[1160, 980], [1352, 962]], { w: 10, taper: .03 }, t, .35)], 'FL', 'post');
  MOL.forEach(([x, y, r, lb], k) => {
    const tt = Wd('molekül', 3) - .5 + k * .18;
    mol.push(...add([circle(x, y, r, tt, .3, { w: 7 })], 'FL', 'post'));
    mol.push(...add(lat(lb, x, y + 16, 34, tt + .3, { seed: 40 + k, lspeed: 200 }), 'FL', 'post'));
  });
  text('molekul', 'N2 O2', 'FL', mol);
  t = Wd('saçılır', 3) - .15; const sc = [];
  [[-150, -110], [10, -170], [160, -100], [-170, 60], [170, 80], [0, 160]].forEach(([dx, dy], k) => {
    const a = [1400 + dx * .4, 960 + dy * .4], b = [1400 + dx, 960 + dy];
    sc.push(...add(arrow(a, b, t + k * .08, .16, { color: k % 2 ? 'white' : 'blue', w: 7, head: 26 }), 'FL', 'post'));
  });
  EV.push({ t, type: 'scatter' });

  // ───────── column C (cx 2880): blue scatters far more; it reaches the eye from every direction
  const C = 2880;
  t = SG[4].start + .1;
  const m1 = add(latL('mavi', C - 430, 330, 82, t, { seed: 60, lspeed: 80, color: 'blue' }), 'FL', 'post');
  const m2 = add(latL('>>', m1.x + 30, 330, 70, m1.end + .05, { seed: 61, lspeed: 80 }), 'FL', 'post');
  const m3 = add(latL('kırmızı', m2.x + 30, 330, 70, Math.max(m2.end + .05, Wd('kırmızı', 4) - .1), { seed: 62, lspeed: 80 }), 'FL', 'post');
  text('mavikirmizi', 'mavi >> kırmızı', 'FL', [...m1, ...m2, ...m3]);
  // the eye
  t = Wd('bu', 4) - .05; const EY = [C, 900];
  const eye = [
    line([[EY[0] - 150, EY[1]], [EY[0] - 60, EY[1] - 70], [EY[0] + 60, EY[1] - 70], [EY[0] + 150, EY[1]]], { w: 9, smooth: true, taper: .05 }, t, .35),
    line([[EY[0] - 150, EY[1]], [EY[0] - 60, EY[1] + 68], [EY[0] + 60, EY[1] + 68], [EY[0] + 150, EY[1]]], { w: 9, smooth: true, taper: .05 }, t + .35, .3),
    circle(EY[0], EY[1], 42, t + .7, .3, { w: 8, color: 'blue' }), circle(EY[0], EY[1], 14, t + 1.0, .15, { w: 10 }),
  ];
  add(eye, 'FL', 'post');
  t = Wd('her', 4) - .1; const rays = [];
  [[-1, -1], [0, -1.25], [1, -1], [-1.3, -.2], [1.3, -.2], [-1, .9], [1, .9]].forEach(([dx, dy], k) => {
    const a = [EY[0] + dx * 330, EY[1] + dy * 300], b = [EY[0] + dx * 190, EY[1] + dy * 150];
    rays.push(...add(arrow(a, b, t + k * .1, .18, { color: 'blue', w: 7, head: 26 }), 'FL', 'post'));
  });
  EV.push({ t, type: 'arrive' });

  // ───────── column D (right panel, world cx 3820): the sunset, a long path, blue lost on the way
  const D = 3820;
  t = SG[5].start + .05;
  const hz = add([line([[3300, 1060], [3700, 1030], [4100, 1030], [4420, 1060]], { w: 9, smooth: true, taper: .03 }, t, .5)], 'FR');
  const sunD = [4260, 1030];
  const half = []; for (let k = 0; k <= 12; k++) { const a = Math.PI + k / 12 * Math.PI; half.push([sunD[0] + Math.cos(a) * 75, sunD[1] + Math.sin(a) * 75]); }
  add([line(half, { w: 9, smooth: true, taper: .04 }, t + .45, .35)], 'FR');
  const man = [3420, 1000];                                // the observer: a small stick figure
  add([circle(man[0], man[1] - 70, 16, t + .6, .15, { w: 7 }), line([[man[0], man[1] - 52], [man[0], man[1] + 5]], { w: 7 }, t + .76, .1), line([[man[0] - 20, man[1] + 50], [man[0], man[1] + 5], [man[0] + 20, man[1] + 50]], { w: 7 }, t + .87, .12)], 'FR');
  t = Wd('uzar', 5) - .5;
  const path = add([line([[sunD[0] - 80, sunD[1] - 20], [3900, 920], [3600, 930], [man[0] + 30, man[1] - 70]], { w: 8, smooth: true, taper: .03 }, t, .8)], 'FR');
  const yl = add(lat('uzun yol', 3860, 1150, 52, t + .6, { seed: 70, lspeed: 160 }), 'FR');
  text('uzunyol', 'uzun yol', 'FR', yl);
  t = Wd('mavi', 5) - .1; const lost = [];
  [[4080, 900], [3880, 915], [3680, 925]].forEach(([x, y], k) => lost.push(...add(arrow([x, y - 20], [x + (k - 1) * 40, y - 190], t + k * .15, .18, { color: 'blue', w: 7, head: 24 }), 'FR')));
  t = Math.max(Wd('turuncu', 5) - .15, lost[lost.length - 1].t1 + .05);
  const k1 = add(lat('turuncu', D, 360, 90, t, { seed: 72, lspeed: 80 }), 'FR'); t = k1.end + .05;
  const k2 = add(lat('ve kırmızı', D, 500, 90, Math.max(t, Wd('kırmızı', 5) - .2), { seed: 73, lspeed: 80 }), 'FR'); t = k2.end + .05;
  const k3 = add(lat('kalır', D, 640, 90, Math.max(t, Wd('kalır', 5) - .15), { seed: 74, lspeed: 80 }), 'FR');
  text('kalir', 'turuncu ve kırmızı kalır', 'FR', [...k1, ...k2, ...k3]);

  T.end = SG[5].end; T.wide = T.end + .4; T.DUR = +Math.max(total, T.wide + 2.4).toFixed(2);

  // ───────── camera (portrait): keys [t, cx, cy, s]; s is for a 1920-wide frame, so 1.75 shows about 1100 board units across
  const SC = 1.5, CY = 680;
  const at = (i, d = 0) => SG[i].start + d;
  const shots = [
    { t0: 0, keys: [[0, A, CY - 40, SC * 1.08], [at(1) + 1.2, A, CY, SC], [at(2) - .1, A, CY, SC], [at(2) + .7, B, CY, SC], [at(4) - .45, B, CY, SC], [at(4) + .35, C, CY, SC], [at(5) - .5, C, CY, SC], [at(5) + .45, D, CY, SC], [T.end, D, CY, SC], [T.wide + 1.3, 2180, 820, .6], [T.DUR, 2180, 820, .59]] },
  ];
  shots.forEach((s, i) => s.t1 = i + 1 < shots.length ? shots[i + 1].t0 : 1e9);
  const camAt = tt => {
    const K = shots[0].keys; let k = 0; while (k + 1 < K.length - 1 && tt > K[k + 1][0]) k++;
    const a = K[k], b = K[Math.min(K.length - 1, k + 1)], u = b[0] > a[0] ? eio(clamp((tt - a[0]) / (b[0] - a[0]))) : 1;
    return { cx: lerp(a[1], b[1], u), cy: lerp(a[2], b[2], u), s: lerp(a[3], b[3], u), shot: 0 };
  };
  for (const st of S) {
    if (st.t1 <= 0 || st.t0 >= T.DUR) continue;
    const c = camAt((st.t0 + st.t1) / 2), p = st.at(st.len / 2), x = p[0] + (st.layer === 'FR' ? 0 : 0);
    const sx = (x - c.cx) * c.s * (W / 1920) / W * 2;
    if (Math.abs(sx) > 1.3) continue;
    EV.push({ t: +st.t0.toFixed(3), type: 'chalk', d: +(st.t1 - st.t0).toFixed(3), len: Math.round(st.len * c.s), color: st.color, pan: +clamp(sx * .5, -.6, .6).toFixed(2), big: st.w > 12 ? 1 : 0 });
  }
  EV.sort((a, b) => a.t - b.t);
  return { S, TX, EV, SUBS, T: { ...T, back0: 1e9 }, wet: null, wipe, slideX: () => 0, camAt, shots, DUR: T.DUR, G1: null, G2: null, SMALL: [] };
}
