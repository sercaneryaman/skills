# Continuation-mode takes start with the tail of the prompt clip ("...kil tablet."). Cut it off.
import glob, re, subprocess, json, whisper
P = '/tmp/claude-0/-home-user/6836c550-55f1-5f08-ade5-0f6b86d03452/scratchpad/jole'
L = json.load(open(P + '/lines.json'))
norm = lambda s: re.sub(r"[^a-zçğıöşü]", '', s.replace('İ', 'i').replace('I', 'ı').lower())
asr = whisper.load_model('small')
for f in sorted(glob.glob(P + '/raw3/*.wav')):
    i = int(f.split('/l')[-1][:2]); first = norm(L[i - 1]['tr'].split()[0])
    ws = [w for s in asr.transcribe(f, language='tr', fp16=False, word_timestamps=True)['segments'] for w in s['words']]
    cut = None
    tab = [j for j, w in enumerate(ws) if 'tablet' in norm(w['word']) or norm(w['word']).startswith('tablt')]
    if tab and tab[-1] + 1 < len(ws):
        j = tab[-1]; cut = (ws[j]['end'] + ws[j + 1]['start']) / 2
    else:
        k = next((j for j, w in enumerate(ws) if norm(w['word'])[:3] == first[:3]), None)
        if k is not None: cut = max(0, ws[k]['start'] - 0.06)
    if cut is None:
        print('skip', f); continue
    out = P + '/voice/' + f.split('/')[-1]
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', f'{cut:.3f}', '-i', f, '-af', 'afade=t=in:d=0.02', out], check=True)
    print('cut', f.split('/')[-1], round(cut, 2))
