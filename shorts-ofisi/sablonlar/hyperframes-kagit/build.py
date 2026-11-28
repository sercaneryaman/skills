# Pineapple jelly Short: paper cut-out stop-motion look (1080x1920), timed from segs/words/caps.json.
import json, re, html
B = '/tmp/claude-0/-home-user/6836c550-55f1-5f08-ade5-0f6b86d03452/scratchpad/jole'
segs = json.load(open(B + '/segs.json')); caps = json.load(open(B + '/caps.json'))
words = json.load(open(B + '/words.json')); DUR = json.load(open(B + '/meta.json'))['total']
S = {s['i']: s['start'] for s in segs}; E = {s['i']: s['end'] for s in segs}
r = lambda x: round(x, 3)
norm = lambda s: re.sub(r"[^a-zçğıöşü0-9]", '', s.replace('İ', 'i').replace('I', 'ı').lower())
def Wd(p, ln, nth=0):
    hits = [w['s'] for w in words if w['line'] == ln and norm(w['w']).startswith(p)]
    return r(hits[min(nth, len(hits) - 1)]) if hits else r(S[ln])
T = dict(donmadi=Wd('donmad', 1), ayni1=Wd('ikisinde', 2), jelatin2=Wd('jelatin', 2), buzdolabi=Wd('buzdolab', 2),
         tek=Wd('tek', 2), ananas2=Wd('ananas', 2), tahmin=Wd('tahmin', 3), ne3=Wd('ne', 3),
         gorunmez=Wd('görünmez', 4), ag=Wd('ağ', 4), baglanir=Wd('bağlanır', 4), suyu=Wd('suyu', 4), hapseder=Wd('tutar', 4),
         bromelain=Wd('bromelain', 5), makas=Wd('makas', 5), keser=Wd('keser', 5), kurulamaz=Wd('kurulamay', 5), donmuyor=Wd('donmuyor', 5),
         konserve=Wd('konserve', 6), isit=Wd('ısıtıl', 6), bozulur=Wd('bozulur', 6), donar=Wd('donar', 6),
         kivi=Wd('kivi', 7), papaya=Wd('papaya', 7), abone=Wd('abone', 7))
TR = 0.45  # page slide
IN = {k: (0 if k == 1 else r(S[k] - TR - 0.05)) for k in range(1, 8)}
CREAM, PAPER, PINE, JELLY, JELLY2, WATER, INK, GREEN, ORANGE = '#F4EBD9', '#FFF8E7', '#F2B632', '#D8433B', '#B8322B', '#5BA4CF', '#2B2A33', '#6FAE3E', '#F08A3C'

# ---------- paper props ----------
def bowl(x, y, s=1.0, state='firm', id_=''):
    jelly = (f'<g class="jfirm" id="{id_}j"><path d="M-150 10 C-150 -120 150 -120 150 10 Z" fill="{JELLY}"/>'
             f'<path d="M-110 -40 C-95 -80 -40 -95 0 -96" stroke="#F08070" stroke-width="14" fill="none" stroke-linecap="round"/></g>')
    puddle = f'<g class="jrun" id="{id_}p"><ellipse cx="0" cy="18" rx="168" ry="34" fill="{JELLY2}"/><ellipse cx="-40" cy="10" rx="60" ry="10" fill="#E8665C"/></g>'
    return f'''<g transform="translate({x} {y}) scale({s})" filter="url(#paper)"><g id="{id_}">
  <ellipse cx="0" cy="96" rx="210" ry="26" fill="#C9B79A" opacity=".55"/>
  <path d="M-200 0 C-190 90 -120 110 0 110 C120 110 190 90 200 0 Z" fill="#E9F4F8"/>
  {jelly if state == 'firm' else puddle}{puddle if state == 'both' else ''}{jelly if state == 'both' else ''}
  <path d="M-200 0 C-190 90 -120 110 0 110 C120 110 190 90 200 0 Z" fill="#CFE6EF" opacity=".45"/>
  <ellipse cx="0" cy="0" rx="200" ry="22" fill="none" stroke="#B7D3DE" stroke-width="8"/>
</g></g>'''

def pine_chunk(x, y, s=1.0, id_=''):
    dots = ''.join(f'<circle cx="{cx}" cy="{cy}" r="4" fill="#C98A12"/>' for cx, cy in ((-20, 10), (5, -5), (22, 14), (-5, 25), (12, 34)))
    return f'<g transform="translate({x} {y}) scale({s})" filter="url(#paper)"><g id="{id_}"><path d="M-45 45 L0 -45 L45 45 Z" fill="{PINE}" stroke="#E09A1A" stroke-width="6" stroke-linejoin="round"/>{dots}</g></g>'

def pine_slice(x, y, s=1.0, id_=''):
    return f'''<g transform="translate({x} {y}) scale({s})" filter="url(#paper)"><g id="{id_}">
  <circle r="150" fill="#E8A21C"/><circle r="128" fill="{PINE}"/>
  {''.join(f'<path d="M0 0 L{128*__import__("math").cos(a*0.5236):.0f} {128*__import__("math").sin(a*0.5236):.0f}" stroke="#E7A626" stroke-width="5"/>' for a in range(12))}
  <circle r="34" fill="#F7D576"/>
  <path d="M-30 -150 C-60 -230 -10 -250 0 -170 C10 -260 60 -240 30 -150 Z" fill="{GREEN}"/>
</g></g>'''

def scissors(x, y, s=1.0, id_='', col='#8A93A3'):
    return f'''<g transform="translate({x} {y}) scale({s})" filter="url(#paper)"><g id="{id_}">
  <g class="bladeA" id="{id_}a"><path d="M0 0 L190 -18 L196 -6 L4 12 Z" fill="{col}"/><circle cx="-46" cy="22" r="30" fill="none" stroke="{ORANGE}" stroke-width="16"/></g>
  <g class="bladeB" id="{id_}b"><path d="M0 0 L190 18 L196 6 L4 -12 Z" fill="#A9B1BF"/><circle cx="-46" cy="-22" r="30" fill="none" stroke="{ORANGE}" stroke-width="16"/></g>
  <circle r="9" fill="{INK}"/>
</g></g>'''

def net(id_, cx, cy, n=6, sz=360):
    """protein mesh: orange paper threads (segments) + blue water drops in the cells"""
    step = sz / (n - 1); x0, y0 = cx - sz / 2, cy - sz / 2
    segs_, drops = [], []
    k = 0
    for i in range(n):
        for j in range(n):
            x, y = x0 + i * step, y0 + j * step
            wob = 10 if (i + j) % 2 else -10
            if i < n - 1:
                segs_.append(f'<path class="th" id="{id_}t{k}" d="M{x:.0f} {y:.0f} Q{x+step/2:.0f} {y+wob:.0f} {x+step:.0f} {y:.0f}" pathLength="1"/>'); k += 1
            if j < n - 1:
                segs_.append(f'<path class="th" id="{id_}t{k}" d="M{x:.0f} {y:.0f} Q{x+wob:.0f} {y+step/2:.0f} {x:.0f} {y+step:.0f}" pathLength="1"/>'); k += 1
            if i < n - 1 and j < n - 1:
                drops.append(f'<path class="dr" id="{id_}d{len(drops)}" transform="translate({x+step/2:.0f} {y+step/2:.0f})" d="M0 -16 C10 -2 14 6 0 14 C-14 6 -10 -2 0 -16 Z" fill="{WATER}"/>')
    return (f'<g id="{id_}" filter="url(#paper)"><g fill="none" stroke="{ORANGE}" stroke-width="9" stroke-linecap="round">{"".join(segs_)}</g>'
            f'{"".join(drops)}</g>'), k, len(drops)

def can(x, y, id_=''):
    return f'''<g transform="translate({x} {y})" filter="url(#paper)"><g id="{id_}">
  <rect x="-110" y="-140" width="220" height="280" rx="18" fill="#C7CCD4"/><ellipse cx="0" cy="-140" rx="110" ry="22" fill="#E1E5EA"/>
  <rect x="-110" y="-80" width="220" height="150" fill="{PINE}"/>
  <text x="0" y="-22" text-anchor="middle" font-family="Mont" font-weight="900" font-size="34" fill="{INK}">KONSERVE</text>
  <text x="0" y="24" text-anchor="middle" font-family="Mont" font-weight="900" font-size="34" fill="{INK}">ANANAS</text>
</g></g>'''

def flame(x, y, id_=''):
    return f'<g transform="translate({x} {y})" filter="url(#paper)"><g id="{id_}"><path d="M0 -110 C60 -40 70 10 40 50 C20 75 -20 75 -40 50 C-70 10 -40 -20 -10 -60 C-4 -20 14 -10 0 -110 Z" fill="{ORANGE}"/><path d="M0 -30 C24 0 26 30 8 46 C-12 56 -26 40 -20 20 Z" fill="{PINE}"/></g></g>'

def kiwi(x, y, id_=''):
    seeds = ''.join(f'<ellipse cx="{70*__import__("math").cos(a*0.3927):.0f}" cy="{70*__import__("math").sin(a*0.3927):.0f}" rx="5" ry="9" transform="rotate({a*22.5} {70*__import__("math").cos(a*0.3927):.0f} {70*__import__("math").sin(a*0.3927):.0f})" fill="#2B2A33"/>' for a in range(16))
    return f'<g transform="translate({x} {y})" filter="url(#paper)"><g id="{id_}"><circle r="120" fill="#8A6A3B"/><circle r="108" fill="#8CC63F"/><circle r="45" fill="#E8F5C8"/>{seeds}</g></g>'

def papaya(x, y, id_=''):
    seeds = ''.join(f'<circle cx="{cx}" cy="{cy}" r="9" fill="#2B2A33"/>' for cx, cy in ((-14, -30), (10, -20), (-6, 0), (14, 10), (-10, 22), (6, 34)))
    return f'<g transform="translate({x} {y})" filter="url(#paper)"><g id="{id_}"><ellipse rx="110" ry="160" fill="#7FA84A"/><ellipse rx="96" ry="146" fill="{ORANGE}"/><ellipse rx="40" ry="70" fill="#E4692B"/>{seeds}</g></g>'

def spoon(x, y, id_=''):
    return f'<g transform="translate({x} {y})" filter="url(#paper)"><g id="{id_}"><rect x="-14" y="-260" width="28" height="230" rx="14" fill="#B9C1CC"/><ellipse cx="0" cy="-10" rx="46" ry="62" fill="#D3D9E1"/><ellipse cx="-10" cy="-24" rx="16" ry="26" fill="#EEF1F5"/></g></g>'

def pot(x, y, id_=''):
    bub = ''.join(f'<circle class="bub" cx="{cx}" cy="{cy}" r="{r_}" fill="#DDEFF7" stroke="#B7D3DE" stroke-width="4"/>' for cx, cy, r_ in ((-90, -150, 16), (-20, -165, 12), (60, -155, 18), (110, -170, 10), (10, -150, 9)))
    return f'''<g transform="translate({x} {y})" filter="url(#paper)"><g id="{id_}">
  <rect x="-210" y="-150" width="420" height="230" rx="40" fill="#5D6B7D"/><rect x="-235" y="-170" width="470" height="40" rx="20" fill="#7B8899"/>
  <rect x="-290" y="-150" width="80" height="26" rx="13" fill="#3E4856"/><rect x="210" y="-150" width="80" height="26" rx="13" fill="#3E4856"/>
  <ellipse cx="0" cy="-160" rx="200" ry="26" fill="#8EC5E6"/>
  <g id="{id_}c"><path d="M-110 -180 L-75 -240 L-40 -180 Z" fill="{PINE}"/><path d="M20 -175 L55 -235 L90 -175 Z" fill="{PINE}"/></g>
  <g id="{id_}b">{bub}</g></g></g>'''

def label(id_, text, top, size=96, col=INK, bg=None, rot=-2):
    st = f'background:{bg};padding:6px 34px 14px;' if bg else ''
    return f'<div class="lab" id="{id_}" style="top:{top}px;font-size:{size}px;color:{col};{st}transform:translateX(-50%) rotate({rot}deg)">{text}</div>'

SC = {}
SC[1] = f'''<svg viewBox="0 0 1080 1920" class="art">{bowl(540, 920, 1.9, 'both', 'b1')}{spoon(760, 760, 'sp1')}</svg>
{label('l1', 'DONMADI?!', 300, 170, JELLY)}'''
SC[2] = f'''<svg viewBox="0 0 1080 1920" class="art">{bowl(290, 960, 1.1, 'firm', 'b2a')}{bowl(790, 960, 1.1, 'run', 'b2b')}{pine_chunk(800, 640, 1.2, 'pc2')}</svg>
<div class="tag" id="tg1" style="left:90px;top:590px">✓ Aynı jelatin</div><div class="tag" id="tg2" style="left:560px;top:590px">✓ Aynı buzdolabı</div>
{label('l2', 'TEK FARK:<br><span style="color:#E09A1A">TAZE ANANAS</span>', 270, 116)}'''
SC[3] = f'''<svg viewBox="0 0 1080 1920" class="art">{pine_chunk(180, 300, 1.3, 'pk3')}{bowl(880, 330, 0.6, 'firm', 'b3')}</svg>
<div class="card" id="cd3"><div style="font-size:88px;line-height:1">Ananas jöleye<br>ne yapıyor olabilir?</div>
<div class="qs"><span id="q1">?</span><span id="q2">?</span><span id="q3">?</span></div>
<div class="dots"><i id="dt1"></i><i id="dt2"></i><i id="dt3"></i></div></div>'''
n4, nt4, nd4 = net('n4', 520, 820, 6, 400)
SC[4] = f'''<svg viewBox="0 0 1080 1920" class="art"><g id="mg4">
<path d="M760 1060 L920 1220" stroke="#8A5A3C" stroke-width="56" stroke-linecap="round" filter="url(#paper)"/>
<circle cx="520" cy="820" r="320" fill="#F7D9D4" filter="url(#paper)"/>{n4}
<circle cx="520" cy="820" r="320" fill="none" stroke="#C9A24B" stroke-width="26" filter="url(#paper)"/>
<path d="M330 640 C380 590 450 560 520 556" stroke="#fff" stroke-width="18" fill="none" stroke-linecap="round" opacity=".6"/></g></svg>
{label('l4', 'GÖRÜNMEZ AĞ', 290, 120, JELLY)}<div class="tag" id="tg4" style="left:150px;top:420px">ip = jelatin proteini · damla = su</div>'''
n5, nt5, nd5 = net('n5', 650, 880, 5, 340)
SC[5] = f'''<svg viewBox="0 0 1080 1920" class="art"><circle cx="650" cy="880" r="270" fill="#F7D9D4" filter="url(#paper)"/>{n5}
{pine_slice(210, 620, 0.85, 'ps5')}{scissors(240, 900, 1.35, 'sz5')}</svg>
{label('l5', 'BROMELAİN<br><span style="font-size:84px">= minik makas</span>', 270, 120, '#C98A12')}'''
n6, nt6, nd6 = net('n6', 790, 760, 5, 230)
SC[6] = f'''<svg viewBox="0 0 1080 1920" class="art">{flame(300, 1075, 'fl6')}{pot(300, 950, 'pt6')}{can(150, 640, 'cn6')}
<circle cx="790" cy="760" r="205" fill="#F7D9D4" filter="url(#paper)"/>{n6}{scissors(720, 560, 0.75, 'sz6')}{bowl(790, 1080, 0.75, 'firm', 'b6')}</svg>
{label('l6', 'ISI, ENZİMİ BOZAR', 290, 112, JELLY)}<div class="src" id="src6">Kaynak: Scientific American · McGill OSS</div>'''
SC[7] = f'''<svg viewBox="0 0 1080 1920" class="art">{kiwi(290, 760, 'kw7')}{papaya(790, 760, 'pp7')}{scissors(350, 950, 0.6, 'sk7')}{scissors(840, 980, 0.6, 'sp7')}</svg>
{label('l7', 'ONLAR DA KESER', 300, 116, '#5E8F2E')}<div class="sub" id="sub7">ABONE OL</div>'''
scenes = ''.join(f'<div class="scene" id="sc{k}"><div class="push" id="pu{k}"><div class="jit" id="jt{k}">{SC[k]}</div></div></div>' for k in range(1, 8))

# ---------- captions: word timings from words.json in order ----------
KEY = ('ananas', 'jelatin', 'bromelain', 'makas', 'donmuyor', 'donar', 'donmadı', 'ağ', 'enzim', 'kivi', 'papaya', 'abone', 'tahmin', 'ısıtıl', 'bozulur', 'görünmez')
wi = 0; cap_html = []; CW = []
for k, c in enumerate(caps):
    ws = c['tr'].split(); spans = []
    for j, w in enumerate(ws):
        t = words[wi]['s']; wi += 1
        hl = any(norm(w).startswith(norm(x)) for x in KEY)
        spans.append(f'<span class="w{" hl" if hl else ""}" id="c{k}w{j}">{html.escape(w)}</span>'); CW.append([f'c{k}w{j}', r(t)])
    cap_html.append(f'<div class="cap" id="cap{k}" data-cs="{c["s"]}" data-ce="{c["e"]}"><div class="capin">{" ".join(spans)}</div></div>')
cap_html = ''.join(cap_html)

doc = f'''<!doctype html><html><head><meta charset="utf-8"><script src="assets/lib/gsap.min.js"></script>
<style>
@font-face{{font-family:Hand;font-weight:700;src:url(assets/fonts/caveat-latin-700-normal.woff2)}}
@font-face{{font-family:Hand;font-weight:700;src:url(assets/fonts/caveat-latin-ext-700-normal.woff2);unicode-range:U+0100-024F}}
@font-face{{font-family:Mont;font-weight:900;src:url(assets/fonts/montserrat-latin-900-normal.woff2)}}
@font-face{{font-family:Mont;font-weight:900;src:url(assets/fonts/montserrat-latin-ext-900-normal.woff2);unicode-range:U+0100-024F}}
@font-face{{font-family:Mont;font-weight:800;src:url(assets/fonts/montserrat-latin-800-normal.woff2)}}
@font-face{{font-family:Mont;font-weight:800;src:url(assets/fonts/montserrat-latin-ext-800-normal.woff2);unicode-range:U+0100-024F}}
html,body{{margin:0;background:{CREAM}}}
#root{{position:relative;width:1080px;height:1920px;overflow:hidden;background:{CREAM};font-family:Hand}}
#grain{{position:absolute;inset:0;z-index:1;opacity:.55;pointer-events:none}}
#cloth{{position:absolute;left:-40px;right:-40px;bottom:-60px;height:420px;z-index:2;
  background:repeating-linear-gradient(90deg,rgba(216,67,59,.16) 0 60px,transparent 60px 120px),repeating-linear-gradient(0deg,rgba(216,67,59,.16) 0 60px,transparent 60px 120px);transform:rotate(-1.5deg)}}
.scene{{position:absolute;inset:0;z-index:5;visibility:hidden}}
.jit{{position:absolute;inset:0}} .push{{position:absolute;inset:0;transform-origin:50% 45%}}
.art{{position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:visible}}
.lab{{position:absolute;left:50%;white-space:nowrap;text-align:center;font-family:Hand;font-weight:700;line-height:.9;z-index:6;filter:drop-shadow(0 5px 0 rgba(90,62,27,.18))}}
.tag{{position:absolute;font-family:Mont;font-weight:800;font-size:40px;color:{INK};background:{PAPER};padding:12px 24px;border-radius:6px;box-shadow:0 6px 12px rgba(90,62,27,.25);transform:rotate(-2deg);z-index:6}}
.card{{position:absolute;left:120px;right:120px;top:420px;padding:70px 40px 60px;background:{PAPER};text-align:center;font-family:Hand;font-weight:700;color:{INK};
  box-shadow:0 14px 26px rgba(90,62,27,.3);transform:rotate(-2deg);clip-path:polygon(0 2%,6% 0,14% 2%,24% 0,36% 2%,48% 0,60% 2%,72% 0,84% 2%,94% 0,100% 3%,99% 97%,92% 100%,80% 98%,66% 100%,52% 98%,38% 100%,24% 98%,10% 100%,0 98%)}}
.qs{{margin-top:30px;font-size:170px;color:{JELLY};line-height:1}} .qs span{{display:inline-block;margin:0 22px}}
.dots{{margin-top:20px}} .dots i{{display:inline-block;width:34px;height:34px;border-radius:50%;margin:0 14px;background:#E6D6B8}}
.src{{position:absolute;left:0;right:0;top:415px;text-align:center;font-family:Mont;font-weight:800;font-size:30px;color:#7A6A55;z-index:6}}
.sub{{position:absolute;left:50%;top:1010px;transform:translateX(-50%) rotate(-3deg);font-family:Mont;font-weight:900;font-size:64px;color:#fff;background:{JELLY};padding:18px 48px;border-radius:14px;box-shadow:0 10px 0 {JELLY2};z-index:7;opacity:0}}
.th{{stroke-dasharray:1;stroke-dashoffset:1}}
.cap{{position:absolute;left:70px;right:150px;top:1200px;display:flex;justify-content:center;z-index:50;visibility:hidden}}
.capin{{font-family:Hand;font-weight:700;font-size:74px;line-height:1.02;text-align:center;color:{INK};padding:14px 34px 22px;background:{PAPER};
  box-shadow:0 10px 18px rgba(90,62,27,.28);transform:rotate(-1.5deg);
  clip-path:polygon(0 4%,8% 0,20% 3%,33% 0,47% 3%,61% 0,75% 3%,88% 0,100% 4%,98% 96%,86% 100%,72% 97%,58% 100%,44% 97%,30% 100%,16% 97%,2% 100%)}}
.w{{display:inline-block;opacity:0}} .hl{{background:linear-gradient(transparent 55%,rgba(242,182,50,.75) 55%);padding:0 4px}}
#pager{{position:absolute;top:0;left:0;width:1200px;height:1920px;background:{CREAM};z-index:40;transform:translateX(1200px);box-shadow:-18px 0 30px rgba(90,62,27,.35)}}
</style></head><body>
<div id="root" data-composition-id="root" data-width="1080" data-height="1920" data-start="0" data-duration="{DUR}">
<svg width="0" height="0" style="position:absolute"><defs>
 <filter id="paper" x="-20%" y="-20%" width="140%" height="140%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="3" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="3" result="d"/><feDropShadow in="d" dx="0" dy="7" stdDeviation="4" flood-color="#5a3e1b" flood-opacity=".3"/></filter>
 <filter id="fib"><feTurbulence type="fractalNoise" baseFrequency="0.6" numOctaves="3" seed="8"/><feColorMatrix values="0 0 0 0 .45 0 0 0 0 .36 0 0 0 0 .22 0 0 0 .22 0"/></filter>
</defs></svg>
<svg id="grain" viewBox="0 0 1080 1920"><rect width="1080" height="1920" filter="url(#fib)"/></svg>
<div id="cloth"></div>
{scenes}
{cap_html}
<div id="pager"></div>
<audio id="vo" class="clip" src="assets/voice.wav" data-start="0" data-duration="{DUR}" data-volume="1"></audio>
<audio id="bgm" class="clip" src="assets/music.wav" data-start="0" data-duration="{DUR}" data-volume="0.28"></audio>
<audio id="sfx" class="clip" src="assets/sfx.wav" data-start="0" data-duration="{DUR}" data-volume="0.8"></audio>
</div>
<script>
(function(){{
const T={json.dumps(T)};const S={json.dumps(S)};const E={json.dumps(E)};const IN={json.dumps(IN)};const CW={json.dumps(CW)};
const DUR={DUR},TR={TR};const NT={{n4:{nt4},n5:{nt5},n6:{nt6}}},ND={{n4:{nd4},n5:{nd5},n6:{nd6}}};
const tl=gsap.timeline({{paused:true}});
const st=n=>`steps(${{n}})`;
const pop=(sel,t,f=0.4)=>tl.fromTo(sel,{{scale:0,transformOrigin:'50% 50%'}},{{scale:1,duration:f,ease:'back.out(2.6)'}},t);
// scene visibility + paper page slides between scenes
tl.set('#sc1',{{visibility:'visible'}},0);
for(let k=2;k<=7;k++){{
  const t0=IN[k];
  tl.fromTo('#pager',{{x:1200}},{{x:-60,duration:TR*0.55,ease:st(5)}},t0);
  tl.set('#sc'+(k-1),{{visibility:'hidden'}},t0+TR*0.55);tl.set('#sc'+k,{{visibility:'visible'}},t0+TR*0.55);
  tl.to('#pager',{{x:-1300,duration:TR*0.45,ease:st(4)}},t0+TR*0.55);
}}
// --- 1: hook, jelly wobbles then collapses
tl.set('#b1p',{{opacity:0}},0);
tl.fromTo('#b1j',{{scaleX:1,scaleY:1,transformOrigin:'50% 100%'}},{{scaleX:1.06,scaleY:0.94,duration:0.12,ease:'none',yoyo:true,repeat:5}},0.05);
tl.to('#b1j',{{scaleY:0.18,scaleX:1.12,duration:0.35,ease:st(4)}},T.donmadi-0.1);
tl.to('#b1j',{{opacity:0,duration:0.1}},T.donmadi+0.25);
tl.fromTo('#b1p',{{opacity:0,scaleX:0.6,transformOrigin:'50% 50%'}},{{opacity:1,scaleX:1,duration:0.35,ease:st(4)}},T.donmadi+0.05);
tl.fromTo('#l1',{{opacity:0,scale:2.4}},{{opacity:1,scale:1,duration:0.22,ease:'power4.in'}},T.donmadi);
// --- 2: same jelly, same fridge, one difference
pop('#tg1',T.jelatin2-0.1,0.3);pop('#tg2',T.buzdolabi-0.1,0.3);
tl.fromTo('#l2',{{opacity:0,y:-40}},{{opacity:1,y:0,duration:0.3,ease:st(4)}},T.tek-0.1);
tl.fromTo('#pc2',{{y:-500,rotation:-30}},{{y:0,rotation:8,duration:0.5,ease:'bounce.out'}},T.ananas2-0.3);
tl.to('#pc2',{{y:230,opacity:0,duration:0.3,ease:st(3)}},T.ananas2+0.35);
tl.fromTo('#b2aj',{{scaleY:1,transformOrigin:'50% 100%'}},{{scaleY:0.93,duration:0.14,yoyo:true,repeat:5,ease:'none'}},T.ayni1);
// --- 3: guess card + thinking dots in the pause
tl.fromTo('#cd3',{{scale:0.4,rotation:-12,opacity:0}},{{scale:1,rotation:-2,opacity:1,duration:0.35,ease:'back.out(2)'}},IN[3]+0.4);
['#q1','#q2','#q3'].forEach((q,i)=>tl.fromTo(q,{{y:0}},{{y:-40,duration:0.25,yoyo:true,repeat:5,ease:'sine.inOut'}},T.tahmin+i*0.12));
{{const t0=E[3]+0.1,gap=(IN[4]-t0)/3; ['#dt1','#dt2','#dt3'].forEach((d,i)=>tl.to(d,{{backgroundColor:'{JELLY}',scale:1.25,duration:0.15,ease:st(2)}},t0+i*gap));}}
// --- 4: invisible net draws, water drops get trapped
tl.fromTo('#l4',{{opacity:0,scale:1.6}},{{opacity:1,scale:1,duration:0.3,ease:'back.out(2)'}},T.gorunmez-0.1);
{{const t0=T.baglanir-0.6,t1=T.suyu; for(let i=0;i<NT.n4;i++)tl.to('#n4t'+i,{{strokeDashoffset:0,duration:0.25,ease:st(3)}},t0+(t1-t0)*i/NT.n4);
  for(let i=0;i<ND.n4;i++)pop('#n4d'+i,T.suyu+i*((T.hapseder+0.4-T.suyu)/ND.n4),0.25);}}
pop('#tg4',T.hapseder,0.3);
// --- 5: bromelain scissors cut the net
tl.set('#n5 .th',{{strokeDashoffset:0}},IN[5]);
tl.fromTo('#ps5',{{x:-500,rotation:-90}},{{x:0,rotation:0,duration:0.5,ease:st(6)}},IN[5]+0.3);
tl.fromTo('#l5',{{opacity:0,y:30}},{{opacity:1,y:0,duration:0.3,ease:st(4)}},T.bromelain-0.1);
tl.fromTo('#sz5',{{x:-400,y:200,rotation:30,opacity:0}},{{x:0,y:0,rotation:0,opacity:1,duration:0.45,ease:st(6)}},T.makas-0.3);
for(let c=0;c<3;c++){{const t=T.keser-0.2+c*0.35;
  tl.to('#sz5',{{x:110+c*140,y:-30+c*40,duration:0.3,ease:st(3)}},t);
  tl.to('#sz5a',{{rotation:-16,transformOrigin:'0 0',duration:0.08,yoyo:true,repeat:1}},t+0.15);tl.to('#sz5b',{{rotation:16,transformOrigin:'0 0',duration:0.08,yoyo:true,repeat:1}},t+0.15);}}
for(let i=0;i<NT.n5;i++)tl.to('#n5t'+i,{{y:'+='+(180+(i*37)%160),rotation:(i%2?50:-50),opacity:0,transformOrigin:'50% 50%',duration:0.7,ease:'power2.in'}},T.keser+0.1+(i%7)*0.06);
for(let i=0;i<ND.n5;i++)tl.to('#n5d'+i,{{y:'+='+(260+(i*29)%120),opacity:0,duration:0.6,ease:'power2.in'}},T.kurulamaz+(i%5)*0.05);
// --- 6: heat kills the enzyme, net comes back, jelly sets
pop('#cn6',IN[6]+0.35,0.4);pop('#pt6',IN[6]+0.25,0.35);
tl.fromTo('#fl6',{{scaleY:0,transformOrigin:'50% 100%'}},{{scaleY:1,duration:0.3,ease:st(3)}},T.isit-0.2);
tl.to('#fl6',{{scaleY:0.85,scaleX:1.08,duration:0.12,yoyo:true,repeat:11,ease:st(2)}},T.isit+0.1);
tl.fromTo('#sz6',{{opacity:1}},{{opacity:0,scale:0.2,rotation:180,transformOrigin:'50% 50%',duration:0.35,ease:st(4)}},T.bozulur);
tl.fromTo('#l6',{{opacity:0,scale:1.6}},{{opacity:1,scale:1,duration:0.3,ease:'back.out(2)'}},T.bozulur-0.1);
for(let i=0;i<NT.n6;i++)tl.to('#n6t'+i,{{strokeDashoffset:0,duration:0.2,ease:st(2)}},T.bozulur+0.3+i*0.025);
for(let i=0;i<ND.n6;i++)pop('#n6d'+i,T.donar-0.3+i*0.03,0.2);
tl.fromTo('#b6',{{y:60,opacity:0}},{{y:0,opacity:1,duration:0.35,ease:'back.out(2)'}},T.donar-0.2);
tl.fromTo('#src6',{{opacity:0}},{{opacity:1,duration:0.2}},T.konserve);
// --- 7: kiwi, papaya, subscribe
pop('#kw7',T.kivi-0.1,0.45);pop('#pp7',T.papaya-0.1,0.45);
pop('#sk7',T.kivi+0.3,0.3);pop('#sp7',T.papaya+0.3,0.3);
tl.fromTo('#l7',{{opacity:0,y:-30}},{{opacity:1,y:0,duration:0.3,ease:st(4)}},T.kivi+0.4);
tl.fromTo('#sub7',{{opacity:0,scale:0.3}},{{opacity:1,scale:1,duration:0.35,ease:'back.out(3)'}},T.abone-0.1);
tl.to('#sub7',{{y:8,duration:0.1,yoyo:true,repeat:3,ease:'none'}},T.abone+0.6);
// slow push-in on every scene
for(let k=1;k<=7;k++){{const a=IN[k],b=(k<7?IN[k+1]:DUR);tl.fromTo('#pu'+k,{{scale:1}},{{scale:1.045,duration:b-a+TR,ease:'none'}},a);}}
// hook: spoon pokes the jelly before it collapses
tl.fromTo('#sp1',{{x:240,y:-260,rotation:25}},{{x:0,y:0,rotation:0,duration:0.35,ease:st(4)}},0.05);
tl.to('#sp1',{{y:40,duration:0.12,yoyo:true,repeat:1,ease:'none'}},0.45);
tl.to('#sp1',{{x:260,y:-300,rotation:30,duration:0.3,ease:st(3)}},T.donmadi+0.1);
tl.to('#l1',{{rotation:3,duration:0.06,yoyo:true,repeat:5,ease:'none'}},T.donmadi+0.25);
// guess scene props bob
tl.fromTo('#pk3',{{y:0,rotation:0}},{{y:-24,rotation:-10,duration:0.4,yoyo:true,repeat:7,ease:st(3)}},IN[3]+0.3);
// pot: pineapple drops in, bubbles rise
tl.fromTo('#pt6c',{{y:-220,opacity:0}},{{y:0,opacity:1,duration:0.4,ease:'bounce.out'}},T.konserve);
document.querySelectorAll('#pt6b .bub').forEach((b,i)=>tl.fromTo(b,{{y:0,opacity:0}},{{y:-90,opacity:1,duration:0.6,repeat:3,ease:st(4)}},T.isit-0.1+i*0.12));
// captions: chunk on/off, words appear as they are spoken
document.querySelectorAll('.cap').forEach(el=>{{const s=parseFloat(el.dataset.cs),e=parseFloat(el.dataset.ce);
  tl.set(el,{{visibility:'visible'}},s);tl.set(el,{{visibility:'hidden'}},Math.max(s+0.2,e));
  tl.fromTo(el.querySelector('.capin'),{{scale:0.9}},{{scale:1,duration:0.2,ease:'back.out(3)'}},s);}});
CW.forEach(([id,t])=>tl.fromTo('#'+id,{{opacity:0,y:10,rotation:-4}},{{opacity:1,y:0,rotation:0,duration:0.12,ease:st(2)}},Math.max(0,t-0.04)));
// stop-motion jitter at 12 fps on every scene layer
function hs(n){{const x=Math.sin(n*12.9898+78.233)*43758.5453;return x-Math.floor(x);}}
const clk={{t:0}};
tl.to(clk,{{t:DUR,duration:DUR,ease:'none',onUpdate:()=>{{const f=Math.floor(clk.t*12);
  for(let k=1;k<=7;k++){{const el=document.getElementById('jt'+k);
    el.style.transform=`translate(${{((hs(f*3+k)-.5)*3).toFixed(2)}}px,${{((hs(f*7+k)-.5)*3).toFixed(2)}}px) rotate(${{((hs(f*5+k)-.5)*0.4).toFixed(3)}}deg)`;}}
  document.getElementById('grain').style.transform=`translate(${{((hs(f)-.5)*10).toFixed(1)}}px,${{((hs(f+9)-.5)*10).toFixed(1)}}px)`;}}}},0);
tl.to({{}},{{duration:0.001}},DUR-0.001);
window.__timelines=window.__timelines||{{}};window.__timelines.root=tl;
}})();
</script></body></html>'''
open(B + '/proj/index.html', 'w').write(doc)
print('written', len(doc), DUR, T)
