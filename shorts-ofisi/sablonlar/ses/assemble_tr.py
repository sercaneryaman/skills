# Turkish narration layout: trim each picked line, lay out with gaps, Whisper word times, caption chunks.
import json, subprocess, re, difflib, sys
import whisper

B = '/tmp/claude-0/-home-user/6836c550-55f1-5f08-ade5-0f6b86d03452/scratchpad/jole'
A = B + '/proj/assets'
SR = 48000
TEMPO = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
L = json.load(open(B + '/lines.json')); picks = json.load(open(B + '/picks.json'))
def dur(f): return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]))
def norm(s): return re.sub(r"[^a-zçğıöşü0-9]", '', s.replace('İ', 'i').replace('I', 'ı').lower())
asr = whisper.load_model('small')

files, hyps = [], []
for i in range(1, len(L) + 1):
    src = picks[str(i)][1]; out = f'{B}/voice/c{i:02d}.wav'
    af = ('silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.04,areverse,'
          'silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.06,areverse')
    if TEMPO != 1.0: af += f',atempo={TEMPO}'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', src, '-af', af, '-ar', str(SR), out], check=True)
    rr = asr.transcribe(out, language='tr', fp16=False, word_timestamps=True)
    ws = [w for s in rr['segments'] for w in s['words']]
    if ws and dur(out) - ws[-1]['end'] > 0.35:  # cut trailing noise after the last word
        cut = ws[-1]['end'] + 0.15
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', out, '-af', f'atrim=0:{cut:.3f},afade=t=out:st={cut-0.08:.3f}:d=0.08', out + '.t.wav'], check=True)
        subprocess.run(['mv', out + '.t.wav', out], check=True)
    files.append(out); hyps.append(ws)
D = [dur(f) for f in files]
lead, gap, end_hold = 0.25, 0.4, 1.8
EXTRA = {2: 0.6, 4: 0.8}  # thinking pause after the guess question
t = lead; segs = []; args = []; flt = []
for k, (f, d) in enumerate(zip(files, D), 1):
    if k > 1: t += gap + EXTRA.get(k, 0)
    segs.append({'i': k, 'start': round(t, 3), 'end': round(t + d, 3)})
    args += ['-i', f]; flt.append(f'[{k-1}:a]adelay={int(t*1000)}:all=1[a{k}]'); t += d
TOT = round(t + end_hold, 2)
flt.append(''.join(f'[a{k}]' for k in range(1, len(files) + 1)) + f'amix=inputs={len(files)}:normalize=0,apad,atrim=0:{TOT},'
           'highpass=f=70,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120,loudnorm=I=-15:TP=-1.5:LRA=7[out]')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *args, '-filter_complex', ';'.join(flt), '-map', '[out]', '-ar', str(SR), A + '/voice.wav'], check=True)
json.dump(segs, open(B + '/segs.json', 'w'), indent=1); json.dump({'total': TOT}, open(B + '/meta.json', 'w'))

# script words with absolute times
words = []
for s, ws, l in zip(segs, hyps, L):
    disp = l['tr'].split()
    a = [norm(w) for w in disp]; b = [norm(w['word']) for w in ws]
    fix = [None] * len(disp)
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op in ('equal', 'replace') and i2 - i1 == j2 - j1:
            for q in range(i2 - i1): fix[i1 + q] = ws[j1 + q]['start']
    Ld = s['end'] - s['start']
    for q in range(len(disp)):
        if fix[q] is None:
            prev = fix[q - 1] if q else 0.0
            nxt = next((fix[r] for r in range(q + 1, len(disp)) if fix[r] is not None), Ld)
            fix[q] = prev + (nxt - prev) * 0.5
        words.append({'w': disp[q], 's': round(s['start'] + min(fix[q], Ld), 3), 'line': s['i']})
json.dump(words, open(B + '/words.json', 'w'), ensure_ascii=False, indent=1)

# caption chunks: up to 5 words, break after punctuation and at line end
caps = []
for s in segs:
    lw = [w for w in words if w['line'] == s['i']]
    cur = []
    for k, w in enumerate(lw):
        cur.append(w)
        left = len(lw) - 1 - k
        if norm(w['w']) in ('ve', 'da', 'de', 'ile', 'ama'):
            continue
        if k == len(lw) - 1 or (len(cur) >= 2 and re.search(r'[,.?!:]$', w['w']) and left != 1) or (len(cur) >= 5 and left > 2 and not any(re.search(r'[,.?!:]$', x['w']) for x in lw[k+1:k+3])):
            caps.append({'tr': ' '.join(x['w'] for x in cur), 's': round(max(0, cur[0]['s'] - 0.05), 3), 'line': s['i']}); cur = []
ends = {s['i']: s['end'] for s in segs}
for k, c in enumerate(caps):
    if k + 1 < len(caps) and caps[k + 1]['line'] == c['line']:
        c['e'] = caps[k + 1]['s']
    else:
        c['e'] = round(min(ends[c['line']] + 0.35, caps[k + 1]['s'] if k + 1 < len(caps) else TOT), 3)
caps[-1]['e'] = round(TOT - 0.3, 3)
json.dump(caps, open(B + '/caps.json', 'w'), ensure_ascii=False, indent=1)
print('total', TOT); [print(s) for s in segs]; print(len(caps), 'caps')
