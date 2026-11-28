# Point Nemo Short (1080x1920): one canvas drawn as a function of t (ocean, ISS pass, rising camera, d3 orthographic
# globe from Natural Earth land, distance lines, spacecraft cemetery, ISS orbit and deorbit path), DOM labels and
# word-timed captions. Timing from timing.json (segs/words/caps from the voice).
import json, re, html
B = '/home/user/shorts-ofisi/filmler/point-nemo'
TM = json.load(open(B + '/timing.json'))
segs, words, caps, DUR = TM['segs'], TM['words'], TM['caps'], TM['total']
S = {s['i']: s['start'] for s in segs}; E = {s['i']: s['end'] for s in segs}
r = lambda x: round(x, 3)
norm = lambda s: re.sub(r"[^a-zçğıöşü0-9]", '', s.replace('İ', 'i').replace('I', 'ı').lower())
def Wd(p, ln, nth=0):
    hits = [w['s'] for w in words if w['line'] == ln and norm(w['w']).startswith(norm(p))]
    return r(hits[min(nth, len(hits) - 1)]) if hits else r(S[ln])
T = dict(
    bazen=Wd('bazen', 1), km1=Wd('400', 1), yukari=Wd('yukarıda', 1),
    yalniz=Wd('yalnızca', 2), tepe=Wd('tependen', 2), gecer=Wd('geçerken', 2),
    nemo=Wd('point', 3), uzak3=Wd('uzak', 3),
    kara=Wd('kara', 4), km4=Wd('2700', 4), uzakta=Wd('uzakta', 4), uc=Wd('üç', 4), issiz=Wd('ıssız', 4),
    omur=Wd('ömrünü', 5), kontrol=Wd('bilerek', 5), bolge=Wd('bölgeye', 5), dusur=Wd('düşürülür', 5),
    iss6=Wd('uluslararası', 6), indir=Wd('indirilmesi', 6), plan=Wd('planlanıyor', 6),
    harita=Wd('haritanın', 7), kose=Wd('köşesi', 7), abone=Wd('abone', 7),
    S=S, E=E, DUR=DUR)

KEY = ('bazen', 'ıssız', 'planlanıyor', 'point', 'nemo', '400', '2.700')
cap_html, CW, wi = [], [], 0
for k, c in enumerate(caps):
    ws = c['tr'].split(); sp = []
    for j, w in enumerate(ws):
        t = words[wi]['s']; wi += 1
        hl = any(norm(w).startswith(norm(x)) for x in KEY)
        sp.append(f'<span class="w{" hl" if hl else ""}" id="c{k}w{j}">{html.escape(w)}</span>'); CW.append([f'c{k}w{j}', r(t)])
    cap_html.append(f'<div class="cap" data-cs="{c["s"]}" data-ce="{c["e"]}"><div class="capin">{" ".join(sp)}</div></div>')

F = ''.join(f"@font-face{{font-family:In;font-weight:{w};src:url(assets/fonts/inter-{sub}-{w}-normal.woff2){';unicode-range:U+0100-024F' if sub == 'latin-ext' else ''}}}" for w in (300, 400, 600, 700) for sub in ('latin', 'latin-ext'))
doc = f'''<!doctype html><html><head><meta charset="utf-8">
<script src="assets/lib/gsap.min.js"></script><script src="assets/lib/d3.min.js"></script><script src="assets/lib/topojson-client.min.js"></script>
<style>{F}
html,body{{margin:0;background:#1d3434}}
#root{{position:relative;width:1080px;height:1920px;overflow:hidden;background:#1d3434;font-family:In}}
#cv{{position:absolute;inset:0}}
.lab{{position:absolute;left:0;right:0;text-align:center;color:#F2F7FA;opacity:0;letter-spacing:.14em;text-transform:uppercase}}
#hook{{top:210px;font-weight:300;font-size:92px;letter-spacing:.12em}}
#hook b{{font-weight:600}}
#nemo{{top:190px;font-weight:600;font-size:76px}}
#coord{{top:290px;font-weight:300;font-size:36px;letter-spacing:.22em;color:#DDE5E8}}
#dist{{top:190px;font-weight:300;font-size:84px}}
#dist2{{top:300px;font-weight:400;font-size:40px;letter-spacing:.2em;color:#DDE5E8}}
#cem{{top:200px;font-weight:600;font-size:58px}}
#plan{{top:200px;font-weight:300;font-size:58px}}
#plan b{{font-weight:600}}
#more{{top:210px;font-weight:300;font-size:56px}}
#sub{{position:absolute;left:50%;top:1210px;width:400px;margin-left:-200px;text-align:center;font-weight:600;font-size:52px;letter-spacing:.1em;color:#1d3434;background:#F2F7FA;border-radius:999px;padding:18px 0;opacity:0}}
.cap{{position:absolute;left:90px;right:90px;top:1370px;display:flex;justify-content:center;visibility:hidden;z-index:9}}
.capin{{font-weight:400;font-size:56px;line-height:1.18;text-align:center;color:#F2F7FA;text-shadow:0 2px 14px rgba(0,0,0,.6),0 0 2px rgba(0,0,0,.6)}}
.w{{display:inline-block;opacity:0}} .hl{{font-weight:700;color:#fff}}
#vig{{position:absolute;inset:0;pointer-events:none;background:radial-gradient(120% 80% at 50% 45%,transparent 55%,rgba(0,0,0,.5) 100%)}}
#grain{{position:absolute;inset:0;pointer-events:none;opacity:.07;mix-blend-mode:overlay}}
</style></head><body>
<div id="root" data-composition-id="root" data-width="1080" data-height="1920" data-start="0" data-duration="{DUR}">
<canvas id="cv" width="1080" height="1920"></canvas>
<svg id="grain" viewBox="0 0 1080 1920"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="4"/></filter><rect width="1080" height="1920" filter="url(#n)"/></svg>
<div id="vig"></div>
<div class="lab" id="hook"><b>400 km</b> yukarıda</div>
<div class="lab" id="nemo">Point Nemo</div><div class="lab" id="coord">48°52′ G · 123°23′ B</div>
<div class="lab" id="dist">≈ 2.700 km</div><div class="lab" id="dist2">en yakın kara · 3 ıssız ada</div>
<div class="lab" id="cem">Uzay aracı mezarlığı</div>
<div class="lab" id="plan">ISS de buraya: <b>planlanıyor</b></div>
<div class="lab" id="more">Haritanın daha nice uç köşesi var</div>
<div id="sub">ABONE OL</div>
{''.join(cap_html)}
<audio id="mix" class="clip" src="assets/mix.wav" data-start="0" data-duration="{DUR}" data-volume="1"></audio>
</div>
<script>
(function(){{
const T={json.dumps(T)}, CW={json.dumps(CW)}, DUR={DUR};
const cv=document.getElementById('cv'), g=cv.getContext('2d'), W=1080, H=1920;
const LAND=topojson.feature(LANDJSON, LANDJSON.objects.land);
const GRAT=d3.geoGraticule10();
const NEMO=[-123.393,-48.877], ISL=[[-124.787,-24.677],[-109.367,-27.117],[-126.37,-72.97]];
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)), ss=x=>{{x=cl(x);return x*x*(3-2*x)}}, eio=x=>{{x=cl(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2}};
const seg=(t,a,b)=>cl((t-a)/(b-a));
function hs(n){{const x=Math.sin(n*12.9898+78.233)*43758.5453;return x-Math.floor(x)}}
// ---------- ocean: perspective wave lines, fog, a horizon that curves as the camera rises (alt 0..1)
function ocean(t,alt,alpha){{
  if(alpha<=0)return; g.save(); g.globalAlpha=alpha;
  const hz=lerp(820,600,alt), R=lerp(60000,1400,Math.pow(alt,1.6));           // horizon height and its curvature radius
  const sky=g.createLinearGradient(0,0,0,hz); sky.addColorStop(0,'#16292a'); sky.addColorStop(.75,'#2b4646'); sky.addColorStop(1,'#8fa6a8');
  g.fillStyle=sky; g.fillRect(0,0,W,hz+40);
  // stars appear as the camera rises
  for(let i=0;i<90;i++){{const a=alt*hs(i+3); if(a<.05)continue; g.fillStyle=`rgba(242,247,250,${{(.25+.5*hs(i+9))*a}})`; g.fillRect(hs(i)*W,hs(i+1)*hz*.85,1.6,1.6)}}
  const sea=g.createLinearGradient(0,hz,0,H); sea.addColorStop(0,'#5E7C7C'); sea.addColorStop(.25,'#3b5a5a'); sea.addColorStop(1,'#203a3a');
  g.beginPath(); const cy=hz+R; g.arc(W/2,cy,R,Math.PI*1.0,Math.PI*2.0); g.lineTo(W,H); g.lineTo(0,H); g.closePath(); g.fillStyle=sea; g.fill();
  g.save(); g.clip();
  const N=46;
  for(let k=1;k<=N;k++){{
    const u=k/N, d=Math.pow(u,2.2), y0=hz+d*(H-hz)*(1-alt*.55), amp=(2+16*d)*(1-alt*.7), wl=lerp(40,260,d), sp=.6+.8*(1-d);
    g.beginPath();
    for(let x=-20;x<=W+20;x+=12){{const yc=cy-Math.sqrt(Math.max(0,R*R-(x-W/2)*(x-W/2)))+(y0-hz);
      const y=yc+amp*Math.sin(x/wl+t*sp+k*1.7)+amp*.4*Math.sin(x/(wl*.37)-t*sp*1.3+k);
      x<=-20?g.moveTo(x,y):g.lineTo(x,y)}}
    g.strokeStyle=`rgba(221,229,232,${{.08+.24*d}})`; g.lineWidth=.8+1.8*d; g.stroke();
  }}
  for(let k=0;k<160;k++){{const d=Math.pow(hs(k+11),1.6), y=hz+8+d*(H-hz)*.85*(1-alt*.5), w=(4+40*d)*(.4+hs(k+7)), x=W*.62+(hs(k+3)-.5)*(60+380*d), f=.5+.5*Math.sin(t*3+k*2.1);
    g.fillStyle=`rgba(242,247,250,${{(.05+.22*(1-d))*f}})`; g.fillRect(x-w/2,y,w,1.6+2*d)}}
  g.restore();
  // fog band on the horizon
  const fog=g.createLinearGradient(0,hz-120,0,hz+160); fog.addColorStop(0,'rgba(221,229,232,0)'); fog.addColorStop(.45,'rgba(221,229,232,.28)'); fog.addColorStop(1,'rgba(221,229,232,0)');
  g.fillStyle=fog; g.fillRect(0,hz-120,W,280);
  g.restore(); return {{hz}};
}}
function lerp(a,b,u){{return a+(b-a)*u}}
// ---------- the ISS: a bright point with a fading trail along a shallow arc; a small vector silhouette when close
function issAt(u){{const x=lerp(-80,W+80,u), y=lerp(700,470,Math.sin(u*Math.PI))-40*u; return [x,y]}}
function issPass(t,t0,t1,alpha,slowMid){{
  if(alpha<=0||t<t0-0.01)return null; let u=cl((t-t0)/(t1-t0)); if(slowMid)u=u+.7*Math.sin(u*Math.PI*2)/(Math.PI*2);
  g.save(); g.globalAlpha=alpha;
  for(let k=0;k<40;k++){{const v=u-k*.006; if(v<0)break; const [x,y]=issAt(v); g.fillStyle=`rgba(255,255,255,${{(1-k/40)*.55}})`; g.beginPath(); g.arc(x,y,3.2*(1-k/50),0,7); g.fill()}}
  const [x,y]=issAt(u); const gl=g.createRadialGradient(x,y,0,x,y,40); gl.addColorStop(0,'rgba(255,255,255,.95)'); gl.addColorStop(.15,'rgba(255,255,255,.5)'); gl.addColorStop(1,'rgba(255,255,255,0)');
  g.fillStyle=gl; g.beginPath(); g.arc(x,y,40,0,7); g.fill(); g.restore(); return [x,y];
}}
function station(x,y,s,a,rot=0){{                                                    // simple vector station: truss, modules, four wing pairs
  g.save(); g.translate(x,y); g.rotate(rot); g.scale(s,s); g.globalAlpha=a; g.strokeStyle='#F2F7FA'; g.fillStyle='rgba(242,247,250,.9)'; g.lineWidth=2;
  g.fillRect(-60,-2,120,4); for(const sx of [-52,-34,34,52]){{g.fillRect(sx-5,-30,10,26); g.fillRect(sx-5,4,10,26)}}
  g.fillRect(-8,-6,16,22); g.fillRect(-3,16,6,10); g.restore();
}}
// ---------- globe
const proj=d3.geoOrthographic().clipAngle(90).precision(.4), path=d3.geoPath(proj,g);
function globe(t,cx,cy,R,rot,alpha){{
  if(alpha<=0)return; proj.translate([cx,cy]).scale(R).rotate(rot);
  g.save(); g.globalAlpha=alpha;
  const at=g.createRadialGradient(cx-R*.3,cy-R*.35,R*.1,cx,cy,R*1.08); at.addColorStop(0,'#3e5d5d'); at.addColorStop(.85,'#243f3f'); at.addColorStop(1,'rgba(36,63,63,0)');
  g.fillStyle=at; g.beginPath(); g.arc(cx,cy,R*1.08,0,7); g.fill();
  g.beginPath(); path({{type:'Sphere'}}); g.fillStyle='#2F4F4F'; g.fill();
  g.beginPath(); path(GRAT); g.strokeStyle='rgba(221,229,232,.10)'; g.lineWidth=1; g.stroke();
  g.beginPath(); path(LAND); g.fillStyle='rgba(94,124,124,.55)'; g.fill(); g.strokeStyle='rgba(221,229,232,.85)'; g.lineWidth=1.3; g.stroke();
  g.beginPath(); path({{type:'Sphere'}}); g.strokeStyle='rgba(221,229,232,.5)'; g.lineWidth=1.5; g.stroke();
  g.restore();
}}
const P=c=>proj(c);
// ---------- one frame
function frame(t){{
  g.setTransform(1,0,0,1,0,0); g.fillStyle='#1d3434'; g.fillRect(0,0,W,H);
  const s2=T.S[2], s3=T.S[3], end7=T.E[7];
  // ocean phase: t < globe-in; camera rises from line 2; loop back at the end
  const rise=eio(seg(t,T.yalniz,T.gecer+.6)), loopIn=ss(seg(t,end7+.1,end7+1.0));
  const oceanA=1-ss(seg(t,T.gecer+.3,T.nemo-.05)), globeIn=ss(seg(t,T.gecer+.3,T.nemo+.2));
  const oc=ocean(t,rise*(1-loopIn),Math.max(oceanA,loopIn));
  // ISS passes: the hook (slow in the middle so the 400 km line can be read), and the loop pass at the end
  if(oceanA>0){{
    const p=issPass(t,-1.6,T.gecer+.2,oceanA,true);
    if(p&&t>T.km1-.2){{                                                            // 400 km: a dashed line down to the sea
      const a=ss(seg(t,T.km1-.2,T.km1+.3))*(1-ss(seg(t,T.yalniz,T.yalniz+.5)))*oceanA, y1=(oc?oc.hz:800)+120;
      g.save(); g.globalAlpha=a; g.setLineDash([10,12]); g.strokeStyle='#F2F7FA'; g.lineWidth=2; g.beginPath(); g.moveTo(p[0],p[1]+24); g.lineTo(p[0],y1); g.stroke(); g.setLineDash([]);
      g.beginPath(); g.arc(p[0],y1,7,0,7); g.fillStyle='#F2F7FA'; g.fill(); g.font='400 46px In'; g.textAlign='left'; g.fillStyle='#fff'; g.shadowColor='rgba(0,0,0,.6)'; g.shadowBlur=10; g.fillText('≈ 400 km',p[0]+24,(p[1]+y1)/2); g.shadowBlur=0; g.restore();
    }}
  }}
  if(loopIn>0) issPass(t,end7+.2,end7+4.2,loopIn,false);
  // globe phase
  const gA=globeIn*(1-loopIn); if(gA>0){{
    // spin in to Point Nemo, then hold; line 6 pulls back for the orbit; line 7 turns the globe slowly
    const spin=eio(seg(t,T.gecer+.3,T.nemo+.9)), back=eio(seg(t,T.S[6]-.4,T.S[6]+.6)), far=eio(seg(t,T.S[7]-.3,T.S[7]+1.2));
    const R=lerp(lerp(440,330,back),300,far), cy=lerp(860,lerp(900,860,far),back), cx=540;
    const rot=[lerp(40,123.39,spin)+far*(t-T.S[7])*14, lerp(-20,48.88,spin)*(1-far*.6), 0];
    globe(t,cx,cy,R,rot,gA);
    g.save(); g.globalAlpha=gA;
    const N=P(NEMO);
    // the empty circle: 2,688 km around Point Nemo (24.2 degrees)
    const cA=ss(seg(t,T.kara-.2,T.kara+.6))*(1-far);
    if(cA>0){{g.globalAlpha=gA*cA*.9; g.beginPath(); path(d3.geoCircle().center(NEMO).radius(24.17)()); g.setLineDash([6,10]); g.strokeStyle='rgba(242,247,250,.55)'; g.lineWidth=1.6; g.stroke(); g.setLineDash([]); g.globalAlpha=gA}}
    // distance lines to the three islands, drawn out as the voice gives the distance
    const dl=ss(seg(t,T.kara,T.uzakta+.3))*(1-far);
    if(dl>0) ISL.forEach((c,i)=>{{const ip=d3.geoInterpolate(NEMO,c), u=cl(dl*1.15-i*.08); const pts=d3.range(0,1.0001,.02).filter(v=>v<=u).map(v=>ip(v));
      if(pts.length>1){{g.beginPath(); path({{type:'LineString',coordinates:pts}}); g.strokeStyle='#F2F7FA'; g.lineWidth=2.2; g.stroke()}}
      const isA=ss(seg(t,T.uc-.1+i*.18,T.uc+.25+i*.18))*(1-far); if(isA>0){{const q=P(c); g.globalAlpha=gA*isA; g.beginPath(); g.arc(q[0],q[1],7,0,7); g.fillStyle='#F2F7FA'; g.fill(); g.beginPath(); g.arc(q[0],q[1],15,0,7); g.strokeStyle='rgba(242,247,250,.6)'; g.lineWidth=1.5; g.stroke(); g.globalAlpha=gA}}}});
    // spacecraft brought down on purpose: thin streaks falling into the zone (line 5)
    const cem=seg(t,T.omur-.2,T.E[5]+.6);
    if(cem>0&&cem<1){{for(let k=0;k<14;k++){{const st=T.omur-.3+k*.3, u=cl((t-st)/1.6); if(u<=0||u>=1)continue;
      const tgt=P([NEMO[0]+(hs(k)-.5)*10,NEMO[1]+(hs(k+5)-.5)*6]); const dir=hs(k+2)>.5?1:-.7, sx=tgt[0]+lerp(-200,0,u)*dir, sy=tgt[1]+lerp(-380,0,u);
      const tr=g.createLinearGradient(sx,sy,sx+40,sy-90); tr.addColorStop(0,`rgba(255,255,255,${{.9*(1-u*.3)}})`); tr.addColorStop(1,'rgba(255,255,255,0)');
      g.strokeStyle=tr; g.lineWidth=3; g.beginPath(); g.moveTo(sx,sy); g.lineTo(sx-dir*70,sy-135); g.stroke();
      g.beginPath(); g.arc(sx,sy,3.5,0,7); g.fillStyle='#fff'; g.fill();
      if(u>.93){{g.beginPath(); g.arc(tgt[0],tgt[1],(u-.93)*400,0,7); g.strokeStyle=`rgba(242,247,250,${{1-(u-.93)/.07}})`; g.lineWidth=1.5; g.stroke()}}}}}}
    // orbit and the planned deorbit of the ISS (line 6)
    const ob=ss(seg(t,T.S[6]-.2,T.S[6]+.8))*(1-ss(seg(t,T.S[7]+.4,T.S[7]+1.2)));
    if(ob>0){{
      const oR=R*1.32, tilt=.28; g.globalAlpha=gA*ob*.8; g.strokeStyle='rgba(242,247,250,.5)'; g.lineWidth=1.6; g.setLineDash([3,9]);
      g.beginPath(); g.ellipse(cx,cy,oR,oR*tilt,-.18,0,Math.PI*2); g.stroke(); g.setLineDash([]); g.globalAlpha=gA*ob;
      const a0=(t-T.S[6])*.55-1.2, ox=cx+Math.cos(a0)*oR*Math.cos(-.18)-Math.sin(a0)*oR*tilt*Math.sin(-.18), oy=cy+Math.cos(a0)*oR*Math.sin(-.18)+Math.sin(a0)*oR*tilt*Math.cos(-.18);
      const dd=eio(seg(t,T.indir-.2,T.plan+.4));
      const sx=lerp(ox,N[0],dd), sy=lerp(oy,N[1],dd)-Math.sin(dd*Math.PI)*60;
      if(dd>0){{g.setLineDash([8,8]); g.strokeStyle='rgba(255,255,255,.85)'; g.lineWidth=2; g.beginPath(); g.moveTo(ox,oy); g.quadraticCurveTo((ox+N[0])/2+60,Math.min(oy,N[1])-120,sx,sy); g.stroke(); g.setLineDash([])}}
      station(sx,sy,lerp(1.1,.45,dd),gA*ob,-.18+dd*.6);
    }}
    // Point Nemo itself: a white point with slow pulse rings
    const nA=ss(seg(t,T.nemo-.3,T.nemo+.2))*(1-ss(seg(t,T.S[7]+.4,T.S[7]+1.2)));
    if(nA>0){{for(let k=0;k<3;k++){{const ph=((t*.6+k/3)%1); g.globalAlpha=gA*nA*(1-ph)*.8; g.beginPath(); g.arc(N[0],N[1],8+ph*60,0,7); g.strokeStyle='#F2F7FA'; g.lineWidth=1.6; g.stroke()}}
      g.globalAlpha=gA*nA; g.beginPath(); g.arc(N[0],N[1],8,0,7); g.fillStyle='#fff'; g.fill()}}
    g.restore();
  }}
}}
const tl=gsap.timeline({{paused:true}}), L=(id,a,b,f=.35)=>{{tl.fromTo(id,{{opacity:0,y:18}},{{opacity:1,y:0,duration:f,ease:'power2.out'}},a); if(b!=null)tl.to(id,{{opacity:0,y:-12,duration:.3,ease:'power2.in'}},b)}};
tl.set('#hook',{{opacity:1}},0); tl.to('#hook',{{opacity:0,duration:.35}},T.gecer-.2); tl.to('#hook',{{opacity:1,duration:.6}},DUR-1.4);
L('#nemo',T.nemo-.1,T.kara-.3); L('#coord',T.nemo+.25,T.kara-.3);
L('#dist',T.km4-.15,T.omur-.35); L('#dist2',T.uc-.1,T.omur-.35);
L('#cem',T.omur+.6,T.S[6]-.3);
L('#plan',T.plan-.3,T.S[7]-.2);
L('#more',T.harita-.05,T.E[7]+.1);
tl.fromTo('#sub',{{opacity:0,scale:.6}},{{opacity:1,scale:1,duration:.4,ease:'back.out(2.5)'}},T.abone-.1); tl.to('#sub',{{opacity:0,duration:.3}},T.E[7]+.4);
document.querySelectorAll('.cap').forEach(el=>{{const s=+el.dataset.cs,e=+el.dataset.ce; tl.set(el,{{visibility:'visible'}},s); tl.set(el,{{visibility:'hidden'}},Math.max(s+.2,e))}});
CW.forEach(([id,t])=>tl.fromTo('#'+id,{{opacity:0,y:10,filter:'blur(4px)'}},{{opacity:1,y:0,filter:'blur(0px)',duration:.18,ease:'power2.out'}},Math.max(0,t-.05)));
const clk={{t:0}}; tl.to(clk,{{t:DUR,duration:DUR,ease:'none',onUpdate:()=>frame(clk.t)}},0); frame(0);
tl.to({{}},{{duration:.001}},DUR-.001);
window.__timelines=window.__timelines||{{}}; window.__timelines.root=tl;
}})();
</script></body></html>'''
land = open(B + '/proj/assets/lib/land-50m.json').read()
doc = doc.replace('<script>\n(function(){', '<script>const LANDJSON=' + land + ';\n(function(){', 1)
open(B + '/proj/index.html', 'w').write(doc)
json.dump(T, open(B + '/cues.json', 'w'), indent=1)
print('written', len(doc), DUR)
