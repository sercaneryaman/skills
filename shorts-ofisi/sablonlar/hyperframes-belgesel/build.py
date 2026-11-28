# Wood frog Short: night-blue documentary look, ECG monitor, Bentley (1902, PD) snow crystals,
# translucent frog illustration. Timed from segs/words/caps.json (1080x1920).
import json, re, html, math
B = '/tmp/claude-0/-home-user/6836c550-55f1-5f08-ade5-0f6b86d03452/scratchpad/kurbaga'
segs = json.load(open(B + '/segs.json')); caps = json.load(open(B + '/caps.json'))
words = json.load(open(B + '/words.json')); DUR = json.load(open(B + '/meta.json'))['total']
S = {s['i']: s['start'] for s in segs}; E = {s['i']: s['end'] for s in segs}
r = lambda x: round(x, 3)
norm = lambda s: re.sub(r"[^a-zçğıöşü0-9]", '', s.replace('İ', 'i').replace('I', 'ı').lower())
def Wd(p, ln, nth=0):
    hits = [w['s'] for w in words if w['line'] == ln and norm(w['w']).startswith(p)]
    return r(hits[min(nth, len(hits) - 1)]) if hits else r(S[ln])
T = dict(duruyor=Wd('duruyor', 1), donuyor=Wd('donuyor', 1), baharda=Wd('baharda', 1), atiyor=Wd('atıyor', 1),
         orman=Wd('orman', 2), kuzey=Wd('kuzey', 2), yaprak=Wd('yaprak', 2),
         hava=Wd('kış', 3), ucte=Wd('üçte', 3), buza=Wd('buza', 3), yavas=Wd('yavaşlar', 3), durur=Wd('durur', 3),
         peki4=Wd('peki', 4), karaciger=Wd('karaciğer', 4), glikoz=Wd('glikoz', 4), gonderir=Wd('gönderir', 4), antifriz=Wd('antifriz', 4),
         bahar5=Wd('bahar', 5), icten=Wd('içten', 5), cozulur=Wd('çözülür', 5), ilk=Wd('ilk', 5), kalptir=Wd('kalptir', 5),
         neyin=Wd('neyin', 6), bilinmiyor=Wd('bilinmiyor', 6),
         olu=Wd('ölü', 7), diri=Wd('diri', 7), abone=Wd('abone', 7))
TR = 0.6
IN = {k: (0 if k == 1 else r(S[k] - TR * 0.5 - 0.1)) for k in range(1, 8)}
NAVY, ICE, FROST, MON, GOLD, SPRING = '#0B1A2E', '#BFE6F5', '#F4FBFF', '#3CFF8A', '#FFC857', '#7FC96B'

# ---------- heartbeat schedule (drives the monitor and the beeps) ----------
beats = []
t = 0.12
while t < T['duruyor'] + 0.05: beats.append(t); t += 0.72
beats.append(r(T['atiyor'] + 0.05)); beats.append(r(T['atiyor'] + 1.1))
t = IN[2] + 0.4
while t < T['hava']: beats.append(t); t += 0.95
iv = 1.1
while t < T['durur'] - 0.2: beats.append(t); t += iv; iv *= 1.35
t = T['kalptir'] + 0.02; iv = 1.7
while t < DUR - 0.3:
    beats.append(t); t += iv; iv = max(0.72, iv * 0.85)
beats = sorted(set(r(b) for b in beats))
json.dump({'beats': beats, 'T': T, 'IN': IN}, open(B + '/cues.json', 'w'), indent=1)

# ---------- frog illustration (dorsal view, translucent) ----------
def frog(id_, x, y, s=1.0, fill='rgba(191,230,245,.10)', stroke=ICE, organs=True, mask=True):
    leg = (f'<path d="M140 -60 Q250 -40 255 -120" fill="none" stroke="{stroke}" stroke-width="10" stroke-linecap="round"/>'
           f'<path d="M255 -120 l-28 -40 M255 -120 l6 -50 M255 -120 l36 -34" stroke="{stroke}" stroke-width="7" stroke-linecap="round"/>'
           f'<path d="M150 160 Q330 110 300 230 Q290 300 250 330 Q300 380 330 440" fill="none" stroke="{stroke}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>'
           f'<path d="M330 440 l-40 50 M330 440 l-4 66 M330 440 l34 56 M330 440 l60 30" stroke="{stroke}" stroke-width="7" stroke-linecap="round"/>')
    body = 'M0 -300 C70 -300 130 -250 150 -180 C175 -100 185 0 170 90 C155 180 90 235 0 240 C-90 235 -155 180 -170 90 C-185 0 -175 -100 -150 -180 C-130 -250 -70 -300 0 -300 Z'
    msk = ''.join(f'<path d="M{sx*58} -268 L{sx*148} -196 L{sx*168} -112 L{sx*118} -150 Z" fill="{stroke}" opacity=".35"/>' for sx in (1, -1)) if mask else ''
    ridges = ''.join(f'<path d="M{sx*78} -160 C{sx*92} -40 {sx*96} 80 {sx*84} 180" fill="none" stroke="{stroke}" stroke-width="4" opacity=".45" stroke-dasharray="2 12" stroke-linecap="round"/>' for sx in (1, -1))
    eyes = ''.join(f'<circle cx="{sx*118}" cy="-196" r="32" fill="{NAVY}" stroke="{stroke}" stroke-width="6"/><circle cx="{sx*122}" cy="-200" r="11" fill="{stroke}"/>' for sx in (1, -1))
    org = ''
    if organs:
        org = (f'<g id="{id_}liv" opacity=".9"><path d="M-95 -20 C-110 40 -60 80 -10 60 C-20 20 -40 -10 -95 -20 Z" fill="#B9774A" opacity=".75"/>'
               f'<path d="M95 -20 C110 40 60 80 10 60 C20 20 40 -10 95 -20 Z" fill="#B9774A" opacity=".75"/></g>'
               f'<path d="M0 -230 L0 210" stroke="{stroke}" stroke-width="5" stroke-dasharray="14 10" opacity=".35"/>'
               f'<g transform="translate(0 -70)"><g id="{id_}h"><path d="M0 26 C-46 -6 -36 -44 -12 -40 C-4 -38 0 -32 0 -28 C0 -32 4 -38 12 -40 C36 -44 46 -6 0 26 Z" fill="#FF5A6E"/></g></g>')
    half = f'<g>{leg}</g><g transform="scale(-1 1)">{leg}</g>'
    return (f'<g transform="translate({x} {y}) scale({s})"><g id="{id_}" filter="url(#glow)">{half}'
            f'<path d="{body}" fill="{fill}" stroke="{stroke}" stroke-width="7"/>{msk}{ridges}{org}{eyes}</g></g>')

def flakes(prefix, spots):
    return ''.join(f'<img class="fl" id="{prefix}{i}" src="assets/img/flake{(i*5+len(prefix))%12}.png" style="left:{x-sz/2}px;top:{y-sz/2}px;width:{sz}px">'
                   for i, (x, y, sz) in enumerate(spots))

def trees():
    out = []
    for i, (x, w, h, op) in enumerate([(70, 46, 1300, .35), (230, 30, 1100, .22), (420, 54, 1360, .4), (640, 26, 1000, .2), (820, 60, 1380, .45), (990, 34, 1150, .28)]):
        br = ''.join(f'<path d="M{x} {1250-h*f:.0f} q{d*90} -{60+30*f:.0f} {d*150} -{150+40*f:.0f}" stroke="#5E7FA3" stroke-width="{max(4,w/5):.0f}" fill="none" stroke-linecap="round" opacity="{op}"/>'
                     for f, d in ((.55, 1), (.68, -1), (.8, 1), (.9, -1)))
        out.append(f'<rect x="{x-w/2}" y="{1250-h}" width="{w}" height="{h}" fill="#5E7FA3" opacity="{op}"/>{br}')
    return ''.join(out)

def leaves(n, cx, cy, spread, seed, cols=('#7A4E2D', '#9C6A3C', '#5E3B22', '#B07A45')):
    out = []
    for i in range(n):
        a = math.sin(i * 12.9898 + seed) * 43758.5453; a -= math.floor(a)
        b = math.sin(i * 78.233 + seed) * 12345.678; b -= math.floor(b)
        x = cx + (a - .5) * spread; y = cy + (b - .5) * spread * 0.2; rot = (a * 360) % 360
        out.append(f'<g transform="translate({x:.0f} {y:.0f}) rotate({rot:.0f})"><path class="lf" d="M0 -40 C26 -20 26 20 0 42 C-26 20 -26 -20 0 -40 Z M0 -40 L0 42" fill="{cols[i % 4]}" stroke="#3B2414" stroke-width="3" opacity=".95"/></g>')
    return ''.join(out)

def glucose(id_, x, y, s=1.0):
    pts = [(math.cos(math.radians(a)) * 60, math.sin(math.radians(a)) * 60) for a in range(-90, 270, 60)]
    ring = ' '.join(f'{px:.0f},{py:.0f}' for px, py in pts)
    oh = ''.join(f'<path d="M{px:.0f} {py:.0f} l{px*0.55:.0f} {py*0.55:.0f}" stroke="{GOLD}" stroke-width="6"/><text x="{px*1.75:.0f}" y="{py*1.75+10:.0f}" text-anchor="middle" font-family="NS" font-weight="800" font-size="26" fill="{GOLD}">OH</text>'
                 for px, py in pts[1:5])
    return (f'<g transform="translate({x} {y}) scale({s})"><g id="{id_}"><polygon points="{ring}" fill="rgba(255,200,87,.15)" stroke="{GOLD}" stroke-width="7"/>'
            f'<circle cx="{pts[0][0]:.0f}" cy="{pts[0][1]:.0f}" r="20" fill="{NAVY}" stroke="{GOLD}" stroke-width="6"/><text x="{pts[0][0]:.0f}" y="{pts[0][1]+10:.0f}" text-anchor="middle" font-family="NS" font-weight="900" font-size="28" fill="{GOLD}">O</text>{oh}</g></g>')

def hexmol(id_):
    pts = ' '.join(f'{math.cos(math.radians(a))*16:.1f},{math.sin(math.radians(a))*16:.1f}' for a in range(-90, 270, 60))
    return f'<g id="{id_}" opacity="0"><polygon points="{pts}" fill="{GOLD}" stroke="#FFE3A3" stroke-width="3"/></g>'

def cell(id_, x, y, rr=78):
    return (f'<g transform="translate({x} {y})"><circle id="{id_}halo" r="{rr+26}" fill="none" stroke="{GOLD}" stroke-width="12" opacity="0" filter="url(#glow)"/>'
            f'<circle r="{rr}" fill="rgba(191,230,245,.16)" stroke="{ICE}" stroke-width="5"/><circle cx="-12" cy="-8" r="{rr*0.32:.0f}" fill="rgba(191,230,245,.35)"/></g>')

# ---------- scenes ----------
SC = {}
SC[1] = f'''<div class="mon big" id="m1"><canvas id="ecg1" width="860" height="520"></canvas><div class="mlab">♥ <b id="bpm1">atıyor</b></div><div class="frost" id="fr1"></div></div>
{flakes('f1', [(150, 470, 280), (930, 520, 300), (120, 1060, 260), (960, 1040, 280), (540, 400, 200), (100, 760, 170), (985, 790, 170)])}
<div class="ttl" id="t1">Kalbi duruyor.</div>'''
SC[2] = f'''<svg viewBox="0 0 1080 1920" class="art">{trees()}
<path d="M-20 1180 C200 1150 400 1200 600 1170 C800 1145 950 1190 1100 1165 L1100 1228 L-20 1228 Z" fill="#E9F3F8" opacity=".9"/>
<g id="fg2w">{frog('fg2', 540, 1110, 0.48, fill='rgba(150,110,70,.75)', stroke='#D9B48A', organs=False)}</g>
<g id="lv2">{leaves(26, 540, 1115, 820, 3)}</g></svg>
<div class="card photo" id="ph2"><img src="assets/img/frog_usgs.jpg"><div class="cap2">Gerçek bir orman kurbağası</div></div>
<div class="card map" id="mp2"><img src="assets/img/range.png"><div class="cap2"><i class="dot"></i>Yaşadığı bölge · Kuzey Amerika</div></div>
<div class="name" id="nm2">Orman kurbağası<small>Rana sylvatica</small></div>
'''
SC[3] = f'''<svg viewBox="0 0 1080 1920" class="art">{frog('fg3', 440, 760, 1.0)}</svg>
<div class="ice" id="ice3"></div>
{flakes('f3', [(220, 470, 150), (660, 460, 140), (170, 1010, 160), (690, 1060, 150), (440, 1180, 120), (110, 760, 120)])}
<div class="bar" id="bar3"><div class="bfill" id="bf3"></div><div class="bmark"></div></div>
<div class="blab" id="bl3">Vücut suyu</div><div class="bval" id="bv3">≈ ⅔ buz</div>
'''
cells = ''.join(cell(f'c4{i}', x, y) for i, (x, y) in enumerate([(330, 930), (560, 1010), (790, 920), (440, 1170), (700, 1170)]))
mols = ''.join(hexmol(f'gm{i}') for i in range(15))
SC[4] = f'''<svg viewBox="0 0 1080 1920" class="art">
<g transform="translate(250 560)"><g id="lv4"><path d="M-170 -30 C-190 70 -90 140 10 110 C-10 40 -60 -20 -170 -30 Z" fill="#B9774A"/><path d="M170 -40 C200 60 110 140 20 110 C40 30 80 -30 170 -40 Z" fill="#9E6238"/>
<text x="0" y="200" text-anchor="middle" font-family="NS" font-weight="800" font-size="40" fill="#E7B48A">Karaciğer</text></g></g>
{glucose('gl4', 800, 560, 1.0)}
<text id="gt4" x="800" y="720" text-anchor="middle" font-family="NS" font-weight="800" font-size="38" fill="{GOLD}">Glikoz · C₆H₁₂O₆</text>
{cells}<g id="mols">{mols}</g></svg>
{flakes('f4', [(160, 1080, 120), (930, 1080, 120), (560, 800, 90)])}
<div class="pill" id="pl4">Glikoz = antifriz</div>'''
SC[5] = f'''<svg viewBox="0 0 1080 1920" class="art"><g id="sp5">{''.join(f'<path class="spr" d="M{x} 1250 C{x-10} 1180 {x+20} 1140 {x+4} {1080-h}" stroke="{SPRING}" stroke-width="9" fill="none" stroke-linecap="round" pathLength="1"/><g transform="translate({x+4} {1080-h})"><path class="spl" d="M0 0 C30 -30 60 -10 50 10 C30 20 10 10 0 0 Z" fill="{SPRING}"/></g>' for x, h in [(90, 40), (200, 10), (330, 60), (760, 30), (880, 70), (1000, 20)])}</g>
<path id="snow5" d="M-20 1180 C200 1150 400 1200 600 1170 C800 1145 950 1190 1100 1165 L1100 1300 L-20 1300 Z" fill="#E9F3F8" opacity=".9"/>
{frog('fg5', 540, 740, 1.0)}</svg>
<div class="ice" id="ice5"></div><div class="ring" id="rg5"></div>
<div class="drop" id="dp5"></div>
<div class="pill green" id="pl5">İçten dışa çözülme</div>'''
SC[6] = f'''<svg viewBox="0 0 1080 1920" class="art">{frog('fg6', 540, 860, 0.9)}</svg>
<div class="qm" id="qm6">?</div><div class="pill" id="pl6">Neyin başlattığı: bilinmiyor</div>'''
SC[7] = f'''<div class="mon big" id="m7"><canvas id="ecg7" width="860" height="520"></canvas><div class="mlab">♥ <b>atıyor</b></div></div>
<div class="q7" id="q7"><span id="q7a">Ölü mü,</span> <em id="q7b">diri mi?</em></div>
<div class="sub" id="sub7">Abone ol</div>'''
scenes = ''.join(f'<div class="scene" id="sc{k}"><div class="push" id="pu{k}">{SC[k]}</div></div>' for k in range(1, 8))

# ---------- captions ----------
KEY = ('duruyor', 'donuyor', 'atıyor', 'antifriz', 'glikoz', 'içten', 'kalp', 'diri', 'buza', 'üçte', 'bilinmiyor', 'abone')
wi = 0; cap_html = []; CW = []
for k, c in enumerate(caps):
    ws = c['tr'].split(); spans = []
    for j, w in enumerate(ws):
        t = words[wi]['s']; wi += 1
        hl = any(norm(w).startswith(norm(x)) for x in KEY)
        spans.append(f'<span class="w{" hl" if hl else ""}" id="c{k}w{j}">{html.escape(w)}</span>'); CW.append([f'c{k}w{j}', r(t)])
    cap_html.append(f'<div class="cap" id="cap{k}" data-cs="{c["s"]}" data-ce="{c["e"]}"><div class="capin">{" ".join(spans)}</div></div>')
cap_html = ''.join(cap_html)

F = lambda fam, w, f, st='normal': ''.join(f"@font-face{{font-family:{fam};font-weight:{w};font-style:{st};src:url(assets/fonts/{f}-{sub}-{w}-{st}.woff2){';unicode-range:U+0100-024F' if sub == 'latin-ext' else ''}}}" for sub in ('latin', 'latin-ext'))
fonts = F('NS', 600, 'nunito-sans') + F('NS', 800, 'nunito-sans') + F('NS', 900, 'nunito-sans') + F('CG', 700, 'cormorant-garamond') + F('CG', 700, 'cormorant-garamond', 'italic')

doc = f'''<!doctype html><html><head><meta charset="utf-8"><script src="assets/lib/gsap.min.js"></script>
<style>{fonts}
html,body{{margin:0;background:{NAVY}}}
#root{{position:relative;width:1080px;height:1920px;overflow:hidden;background:{NAVY};font-family:NS}}
#sky{{position:absolute;inset:0;background:radial-gradient(120% 70% at 50% 35%,#16304F 0%,{NAVY} 60%,#060E1A 100%)}}
#warm{{position:absolute;inset:0;opacity:0;background:radial-gradient(120% 70% at 50% 40%,#2F5A3A 0%,#16301F 55%,#0A1810 100%)}}
#snowfx{{position:absolute;inset:0;z-index:3;pointer-events:none}} .sn{{position:absolute;left:0;top:0;border-radius:50%;background:{FROST}}}
#vig{{position:absolute;inset:0;z-index:30;pointer-events:none;background:radial-gradient(130% 85% at 50% 45%,transparent 55%,rgba(0,0,0,.55) 100%)}}
.scene{{position:absolute;inset:0;z-index:5;visibility:hidden}} .push{{position:absolute;inset:0;transform-origin:50% 42%}}
.art{{position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:visible}}
.fl{{position:absolute;opacity:0;mix-blend-mode:screen;filter:drop-shadow(0 0 14px rgba(191,230,245,.55))}}
.mon{{position:absolute;left:90px;width:900px;top:430px;height:600px;border-radius:36px;background:rgba(6,16,28,.82);border:3px solid rgba(191,230,245,.35);
  box-shadow:0 0 0 10px rgba(191,230,245,.06),0 30px 80px rgba(0,0,0,.6);overflow:hidden}}
.mon canvas{{position:absolute;left:20px;top:50px}}
.mon:before{{content:'';position:absolute;inset:0;background-image:linear-gradient(rgba(60,255,138,.07) 2px,transparent 2px),linear-gradient(90deg,rgba(60,255,138,.07) 2px,transparent 2px);background-size:60px 60px}}
.mlab{{position:absolute;right:36px;top:22px;font-family:NS;font-weight:800;font-size:40px;color:{MON};text-shadow:0 0 18px rgba(60,255,138,.7)}}
.frost{{position:absolute;inset:0;opacity:0;background:radial-gradient(70% 60% at 50% 50%,rgba(244,251,255,0) 30%,rgba(220,240,250,.55) 75%,rgba(244,251,255,.85) 100%)}}
#strip{{position:absolute;left:300px;top:70px;width:480px;height:130px;border-radius:22px;background:rgba(6,16,28,.7);border:2px solid rgba(191,230,245,.3);overflow:hidden;z-index:20;opacity:0}}
#strip canvas{{position:absolute;left:10px;top:10px}}
.ttl{{position:absolute;left:0;right:0;top:1080px;text-align:center;font-family:CG;font-weight:700;font-style:italic;font-size:110px;color:{FROST};text-shadow:0 0 30px rgba(191,230,245,.6);opacity:0;z-index:8}}
.credit{{position:absolute;left:60px;right:60px;top:1240px;text-align:center;font-family:NS;font-weight:600;font-size:24px;color:rgba(191,230,245,.62);z-index:8}}
.card{{position:absolute;background:{FROST};padding:14px 14px 0;border-radius:6px;box-shadow:0 24px 50px rgba(0,0,0,.55);z-index:7;opacity:0}}
.card img{{display:block;width:100%;border-radius:3px}} .cap2{{font-family:NS;font-weight:800;font-size:28px;color:#1B2C42;text-align:center;padding:12px 6px 16px}}
.photo{{left:55px;top:350px;width:440px}} .map{{left:500px;top:560px;width:520px;background:#12263F}} .map .cap2{{color:{FROST}}}
.dot{{display:inline-block;width:22px;height:22px;border-radius:50%;background:{MON};margin-right:10px;vertical-align:-2px}}
.name{{position:absolute;left:0;right:0;top:230px;text-align:center;font-family:NS;font-weight:900;font-size:76px;color:{FROST};z-index:8;text-shadow:0 6px 24px rgba(0,0,0,.6);opacity:0}}
.name small{{display:block;font-family:CG;font-style:italic;font-weight:700;font-size:56px;color:{ICE};margin-top:-4px}}
.ice{{position:absolute;inset:0;z-index:6;pointer-events:none;--r:100%;
  background:radial-gradient(circle at 41% 40%,rgba(191,230,245,0) 0,rgba(191,230,245,0) var(--r),rgba(191,230,245,.2) calc(var(--r) + 6%),rgba(220,242,252,.4) calc(var(--r) + 22%));mix-blend-mode:screen}}
#ice5{{background:radial-gradient(circle at 50% 39%,rgba(191,230,245,0) 0,rgba(191,230,245,0) var(--r),rgba(191,230,245,.2) calc(var(--r) + 6%),rgba(220,242,252,.4) calc(var(--r) + 22%))}}
.bar{{position:absolute;left:880px;top:440px;width:110px;height:620px;border-radius:55px;border:4px solid rgba(191,230,245,.6);background:rgba(6,16,28,.6);overflow:hidden;z-index:9;opacity:0}}
.bfill{{position:absolute;left:0;right:0;bottom:0;height:0;background:linear-gradient(0deg,#9FD8F0,{FROST})}}
.bmark{{position:absolute;left:0;right:0;bottom:66.6%;border-top:4px dashed {NAVY}}}
.blab{{position:absolute;left:815px;top:370px;width:240px;text-align:center;font-family:NS;font-weight:800;font-size:32px;color:{ICE};z-index:9;opacity:0}}
.bval{{position:absolute;left:800px;top:1080px;width:270px;text-align:center;font-family:NS;font-weight:900;font-size:46px;color:{FROST};z-index:9;opacity:0}}
.pill{{position:absolute;left:50%;top:300px;margin-left:-300px;width:600px;text-align:center;white-space:nowrap;font-family:NS;font-weight:900;font-size:56px;color:{NAVY};background:{GOLD};padding:16px 0;border-radius:999px;box-shadow:0 0 40px rgba(255,200,87,.55);z-index:9;opacity:0}}
#pl6{{width:800px;margin-left:-400px;top:1110px}} #pl5{{top:250px}} #pl4{{top:250px;width:560px;margin-left:-280px}}
.pill.green{{background:{SPRING};box-shadow:0 0 40px rgba(127,201,107,.55)}}
.ring{{position:absolute;left:540px;top:670px;width:10px;height:10px;margin:-5px 0 0 -5px;border-radius:50%;border:8px solid rgba(255,200,87,.8);opacity:0;z-index:7}}
.drop{{position:absolute;left:527px;top:250px;width:26px;height:36px;border-radius:50% 50% 50% 50%/60% 60% 40% 40%;background:{ICE};opacity:0;z-index:9}}
.qm{{position:absolute;left:0;right:0;top:250px;text-align:center;font-family:CG;font-weight:700;font-size:360px;line-height:1;color:{GOLD};text-shadow:0 0 60px rgba(255,200,87,.6);opacity:0;z-index:9}}
.q7{{position:absolute;left:0;right:0;top:200px;text-align:center;font-family:CG;font-weight:700;font-size:120px;color:{FROST};z-index:9}}
.q7 span,.q7 em{{display:inline-block;opacity:0}} .q7 em{{color:{MON};text-shadow:0 0 30px rgba(60,255,138,.6)}}
.sub{{position:absolute;left:50%;top:1085px;width:420px;margin-left:-210px;text-align:center;font-family:NS;font-weight:900;font-size:58px;color:{NAVY};background:{FROST};padding:16px 0;border-radius:999px;z-index:9;opacity:0;box-shadow:0 0 0 6px rgba(191,230,245,.35)}}
.cap{{position:absolute;left:110px;right:110px;top:1320px;display:flex;justify-content:center;z-index:50;visibility:hidden}}
.capin{{font-family:NS;font-weight:800;font-size:60px;line-height:1.12;text-align:center;color:{FROST};padding:18px 34px 22px;border-radius:26px;
  background:rgba(191,230,245,.16);border:2px solid rgba(244,251,255,.35);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);
  text-shadow:0 2px 0 rgba(11,26,46,.6),0 0 14px rgba(11,26,46,.5);box-shadow:0 18px 40px rgba(0,0,0,.35)}}
.w{{display:inline-block;opacity:0}} .hl{{color:{MON}}} .warm .hl{{color:{GOLD}}}
#veil{{position:absolute;inset:0;z-index:40;background:{FROST};opacity:0;pointer-events:none}}
</style></head><body>
<div id="root" data-composition-id="root" data-width="1080" data-height="1920" data-start="0" data-duration="{DUR}">
<svg width="0" height="0" style="position:absolute"><defs>
 <filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs></svg>
<div id="sky"></div><div id="warm"></div>
<div id="snowfx">{''.join(f'<i class="sn" id="sn{i}"></i>' for i in range(46))}</div>
{scenes}
<div id="strip"><canvas id="ecgS" width="460" height="110"></canvas></div>
<div id="vig"></div><div id="veil"></div>
{cap_html}
<audio id="vo" class="clip" src="assets/voice.wav" data-start="0" data-duration="{DUR}" data-volume="1"></audio>
<audio id="bgm" class="clip" src="assets/music.wav" data-start="0" data-duration="{DUR}" data-volume="0.32"></audio>
<audio id="sfx" class="clip" src="assets/sfx.wav" data-start="0" data-duration="{DUR}" data-volume="0.85"></audio>
</div>
<script>
(function(){{
const T={json.dumps(T)};const S={json.dumps(S)};const E={json.dumps(E)};const IN={json.dumps(IN)};const CW={json.dumps(CW)};
const BEATS={json.dumps(beats)};const DUR={DUR},TR={TR};
const tl=gsap.timeline({{paused:true}});
const pop=(sel,t,f=0.45)=>tl.fromTo(sel,{{scale:0,opacity:0,transformOrigin:'50% 50%'}},{{scale:1,opacity:1,duration:f,ease:'back.out(2)'}},t);
tl.set('#sc1',{{visibility:'visible'}},0);
for(let k=2;k<=7;k++){{const t0=IN[k];
  tl.fromTo('#veil',{{opacity:0}},{{opacity:0.85,duration:TR*0.5,ease:'power2.in',immediateRender:false}},t0);
  tl.set('#sc'+(k-1),{{visibility:'hidden'}},t0+TR*0.5);tl.set('#sc'+k,{{visibility:'visible'}},t0+TR*0.5);
  tl.to('#veil',{{opacity:0,duration:TR*0.5,ease:'power2.out'}},t0+TR*0.5);}}
for(let k=1;k<=7;k++){{const a=IN[k],b=(k<7?IN[k+1]:DUR);tl.fromTo('#pu'+k,{{scale:1}},{{scale:1.06,duration:b-a+TR,ease:'none',immediateRender:false}},a);}}
// --- 1 hook
const f1=[...document.querySelectorAll('#sc1 .fl')];
f1.forEach((el,i)=>tl.fromTo(el,{{opacity:0,scale:0.2,rotation:-40}},{{opacity:0.95,scale:1,rotation:0,duration:0.9,ease:'power2.out'}},Math.max(0.1,T.duruyor-0.5)+i*0.12));
tl.to('#fr1',{{opacity:1,duration:1.2,ease:'power1.in'}},T.duruyor);
tl.fromTo('#t1',{{opacity:0,y:30}},{{opacity:1,y:0,duration:0.4,ease:'power2.out'}},T.duruyor);
tl.to('#t1',{{opacity:0,duration:0.3}},T.baharda-0.2);
tl.to('#fr1',{{opacity:0.2,duration:0.6}},T.atiyor-0.3);
f1.forEach(el=>tl.to(el,{{opacity:0.3,duration:0.5}},T.atiyor-0.3));
tl.to('#m1',{{scale:1.03,duration:0.12,yoyo:true,repeat:1,ease:'power1.out'}},T.atiyor+0.05);
tl.fromTo('#strip',{{opacity:0}},{{opacity:1,duration:0.4,immediateRender:false}},IN[2]+TR*0.5);tl.to('#strip',{{opacity:0,duration:0.3}},IN[7]);
// --- 2 forest
tl.fromTo('#fg2w',{{opacity:0}},{{opacity:1,duration:0.6,immediateRender:false}},IN[2]+0.3);
document.querySelectorAll('#lv2 .lf').forEach((el,i)=>tl.fromTo(el,{{y:-700-(i*53)%300,opacity:0}},{{y:0,opacity:0.95,duration:0.9,ease:'power1.out'}},IN[2]+0.2+(i%9)*0.08));
tl.fromTo('#nm2',{{opacity:0,y:-20}},{{opacity:1,y:0,duration:0.4}},T.orman-0.1);
tl.fromTo('#ph2',{{opacity:0,scale:0.6,rotation:-14}},{{opacity:1,scale:1,rotation:-4,duration:0.5,ease:'back.out(1.8)'}},T.orman);
tl.fromTo('#mp2',{{opacity:0,x:300,rotation:10}},{{opacity:1,x:0,rotation:3,duration:0.55,ease:'back.out(1.6)'}},T.kuzey-0.1);
tl.to('#ph2',{{opacity:0.6,scale:0.92,duration:0.3}},T.kuzey);
tl.to(['#mp2','#ph2'],{{opacity:0,y:-60,duration:0.4}},T.yaprak);
tl.to('#fg2w',{{scale:1.12,transformOrigin:'50% 58%',duration:1.2}},T.yaprak);
// --- 3 freezing
tl.set('#ice3',{{'--r':'60%'}},0);
tl.to('#ice3',{{'--r':'0%',duration:Math.max(1.5,T.durur-T.hava),ease:'power1.inOut'}},T.hava);
document.querySelectorAll('#sc3 .fl').forEach((el,i)=>tl.fromTo(el,{{opacity:0,scale:0.2,rotation:30}},{{opacity:0.9,scale:1,rotation:0,duration:0.8,ease:'power2.out'}},T.hava+i*0.22));
tl.fromTo(['#bar3','#bl3'],{{opacity:0,x:60}},{{opacity:1,x:0,duration:0.4}},IN[3]+0.4);
tl.to('#bf3',{{height:'66.6%',duration:Math.max(1.2,T.buza-T.hava+0.6),ease:'power2.inOut'}},T.hava);
tl.fromTo('#bv3',{{opacity:0,scale:0.6}},{{opacity:1,scale:1,duration:0.4,ease:'back.out(2)'}},T.ucte);
tl.to('#fg3',{{opacity:0.75,duration:1.5}},T.yavas);
tl.to('#fg3h',{{opacity:0.3,duration:1.0}},T.durur);
// --- 4 glucose
tl.fromTo('#lv4',{{opacity:0,scale:0.7,transformOrigin:'50% 50%'}},{{opacity:1,scale:1,duration:0.5,ease:'back.out(2)'}},T.karaciger-0.15);
pop('#gl4',T.glikoz-0.1,0.5);tl.fromTo('#gt4',{{opacity:0}},{{opacity:1,duration:0.3}},T.glikoz+0.1);
tl.to('#gl4',{{rotation:60,transformOrigin:'50% 50%',duration:4,ease:'none'}},T.glikoz+0.4);
const C4=[[330,930],[560,1010],[790,920],[440,1170],[700,1170]];
for(let i=0;i<15;i++){{const c=C4[i%5],a=i*2.4,t0=T.karaciger+0.3+i*0.1;
  tl.fromTo('#gm'+i,{{x:250,y:600,opacity:0,scale:0.4}},{{x:c[0]+Math.cos(a)*100,y:c[1]+Math.sin(a)*100,opacity:1,scale:1,duration:1.0,ease:'power2.inOut'}},t0);}}
for(let i=0;i<5;i++)tl.to('#c4'+i+'halo',{{opacity:0.9,duration:0.4}},T.gonderir+i*0.1);
document.querySelectorAll('#sc4 .fl').forEach((el,i)=>{{tl.set(el,{{opacity:0.8}},IN[4]);
  tl.to(el,{{opacity:0,scale:0.3,rotation:90,duration:0.6}},T.antifriz+i*0.1);}});
tl.fromTo('#pl4',{{opacity:0,scale:0.5}},{{opacity:1,scale:1,duration:0.4,ease:'back.out(2.4)'}},T.antifriz-0.1);
// --- 5 spring
tl.to('#warm',{{opacity:1,duration:1.4}},IN[5]+0.2);
tl.set('#ice5',{{'--r':'0%'}},0);
tl.to('#ice5',{{'--r':'75%',duration:Math.max(1.6,T.ilk-T.icten+0.5),ease:'power1.inOut'}},T.icten-0.1);
tl.fromTo('#snow5',{{scaleY:1,opacity:0.9,transformOrigin:'50% 100%'}},{{scaleY:0.15,opacity:0.3,duration:2.2,immediateRender:false}},IN[5]+0.4);
document.querySelectorAll('#sp5 .spr').forEach((el,i)=>tl.fromTo(el,{{strokeDasharray:1,strokeDashoffset:1}},{{strokeDashoffset:0,duration:0.8}},IN[5]+0.6+i*0.15));
document.querySelectorAll('#sp5 .spl').forEach((el,i)=>pop(el,IN[5]+1.3+i*0.15,0.35));
tl.fromTo('#pl5',{{opacity:0,y:-20}},{{opacity:1,y:0,duration:0.4}},T.icten-0.05);
tl.fromTo('#rg5',{{width:10,height:10,marginLeft:-5,marginTop:-5,opacity:0.9}},{{width:900,height:900,marginLeft:-450,marginTop:-450,opacity:0,duration:1.6,ease:'power2.out'}},T.icten);
tl.fromTo('#dp5',{{y:0,opacity:0}},{{y:300,opacity:1,duration:0.7,ease:'power2.in'}},T.cozulur-0.3);tl.to('#dp5',{{opacity:0,duration:0.1}},T.cozulur+0.4);
// --- 6 question
tl.fromTo('#qm6',{{opacity:0,y:300,scale:0.2}},{{opacity:1,y:0,scale:1,duration:0.8,ease:'back.out(1.6)'}},T.neyin-0.1);
tl.to('#qm6',{{rotation:8,duration:0.5,yoyo:true,repeat:5,ease:'sine.inOut'}},T.neyin+0.7);
tl.fromTo('#pl6',{{opacity:0}},{{opacity:1,duration:0.4}},T.bilinmiyor-0.1);
// --- 7 dead or alive
tl.fromTo('#q7a',{{opacity:0,y:30}},{{opacity:1,y:0,duration:0.4}},T.olu-0.05);
tl.fromTo('#q7b',{{opacity:0,y:30}},{{opacity:1,y:0,duration:0.4}},T.diri-0.05);
tl.fromTo('#sub7',{{opacity:0,scale:0.4}},{{opacity:1,scale:1,duration:0.4,ease:'back.out(3)'}},T.abone-0.1);
tl.to(['#q7','#sub7'],{{opacity:0,duration:0.5}},DUR-0.7);
// hearts pulse on every beat
BEATS.forEach(b=>['#fg3h','#fg5h','#fg6h'].forEach(h=>tl.fromTo(h,{{scale:1,transformOrigin:'50% 50%'}},{{scale:1.4,duration:0.1,yoyo:true,repeat:1,ease:'power1.out',immediateRender:false}},b)));
// captions
document.querySelectorAll('.cap').forEach(el=>{{const s=parseFloat(el.dataset.cs),e=parseFloat(el.dataset.ce);
  if(s>=IN[5])el.classList.add('warm');
  tl.set(el,{{visibility:'visible'}},s);tl.set(el,{{visibility:'hidden'}},Math.max(s+0.2,e));
  tl.fromTo(el.querySelector('.capin'),{{scale:0.94}},{{scale:1,duration:0.18,ease:'power2.out'}},s);}});
CW.forEach(([id,t])=>tl.fromTo('#'+id,{{opacity:0,y:8}},{{opacity:1,y:0,duration:0.16,ease:'power2.out'}},Math.max(0,t-0.04)));
// ECG + snow, driven by the timeline clock
function ecgv(tau){{let v=0;for(const b of BEATS){{const d=tau-b;if(d<-0.1||d>0.5)continue;
  v+=0.12*Math.exp(-(((d+0.06)/0.025)**2))-0.15*Math.exp(-((d/0.008)**2))+1.0*Math.exp(-(((d-0.02)/0.01)**2))-0.28*Math.exp(-(((d-0.045)/0.012)**2))+0.22*Math.exp(-(((d-0.26)/0.05)**2));}}return v;}}
function draw(id,t,win,lw,glow){{const c=document.getElementById(id);if(!c)return;const g=c.getContext('2d'),W=c.width,H=c.height;g.clearRect(0,0,W,H);
  g.lineWidth=lw;g.strokeStyle='{MON}';g.shadowColor='{MON}';g.shadowBlur=glow;g.lineJoin='round';g.beginPath();
  const N=Math.floor(W/2);for(let i=0;i<=N;i++){{const x=i*W/N,tau=t-win+win*i/N;const y=H*0.6-ecgv(tau)*H*0.45;i?g.lineTo(x,y):g.moveTo(x,y);}}g.stroke();
  g.shadowBlur=glow*2;g.fillStyle='#E9FFF2';const y=H*0.6-ecgv(t)*H*0.45;g.beginPath();g.arc(W-6,y,lw*1.4,0,7);g.fill();}}
function hs(n){{const x=Math.sin(n*12.9898+78.233)*43758.5453;return x-Math.floor(x);}}
const SN=[...document.querySelectorAll('.sn')];
SN.forEach((el,i)=>{{const s=2+hs(i)*7;el.style.width=s+'px';el.style.height=s+'px';el.style.opacity=(0.25+hs(i+3)*0.5).toFixed(2);el.style.filter=s>6?'blur(1.5px)':'none';}});
const clk={{t:0}};
function frame(){{const t=clk.t;
  draw('ecg1',t,3.2,7,18);draw('ecg7',t,3.2,7,18);draw('ecgS',t,3.2,4,10);
  const b=document.getElementById('bpm1');if(b)b.textContent=(t<T.duruyor+0.4||t>T.atiyor)?'atıyor':'durdu';
  const melt=t>IN[5]?Math.min(1,(t-IN[5])/2):0;
  SN.forEach((el,i)=>{{const sp=40+hs(i+7)*70,x=hs(i)*1080+Math.sin(t*0.6+i)*30,y=((hs(i+11)*1920+t*sp)%2000)-40;
    el.style.transform=`translate(${{x.toFixed(1)}}px,${{y.toFixed(1)}}px)`;}});
  document.getElementById('snowfx').style.opacity=(1-melt).toFixed(2);}}
tl.to(clk,{{t:DUR,duration:DUR,ease:'none',onUpdate:frame}},0);
frame();
tl.to({{}},{{duration:0.001}},DUR-0.001);
window.__timelines=window.__timelines||{{}};window.__timelines.root=tl;
}})();
</script></body></html>'''
open(B + '/proj/index.html', 'w').write(doc)
print('written', len(doc), DUR, len(beats), 'beats')
