# segs/words/caps/meta.json (from assemble_tr.py) -> js/timing.js for the page; with --fake, estimate from lines.json
import json, sys, os
P = os.path.dirname(os.path.abspath(__file__))
if '--fake' in sys.argv:
    L = json.load(open(P + '/lines.json')); t = .3; segs = []; words = []; caps = []
    for i, l in enumerate(L, 1):
        s0 = t; cur = []
        for w in l['tr'].split():
            words.append({'w': w, 's': round(t, 3), 'line': i}); cur.append(w); t += .36 + (.3 if w[-1] in '.?' else .1 if w[-1] == ',' else 0)
            if len(cur) >= 4 or w[-1] in '.?,': caps.append({'tr': ' '.join(cur), 's': words[-len(cur)]['s'], 'e': round(t, 3)}); cur = []
        if cur: caps.append({'tr': ' '.join(cur), 's': words[-len(cur)]['s'], 'e': round(t, 3)})
        segs.append({'i': i, 'start': round(s0, 3), 'end': round(t, 3)}); t += .4
    total = round(t + 1.5, 2)
else:
    segs = json.load(open(P + '/segs.json')); words = json.load(open(P + '/words.json')); caps = json.load(open(P + '/caps.json')); total = json.load(open(P + '/meta.json'))['total']
open(P + '/timing.json', 'w').write(json.dumps({'segs': segs, 'words': words, 'caps': caps, 'total': total}, ensure_ascii=False))
print('timing', total, len(caps), 'caps')
