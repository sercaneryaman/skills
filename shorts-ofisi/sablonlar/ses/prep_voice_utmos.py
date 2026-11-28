# Pick the best take per line: (1) Whisper transcript match against the spoken text (gate: within 0.04 of the best),
# (2) among those, speaker similarity to the real voice and UTMOS naturalness, each scaled within the line, 55/45.
# Then pace it: 0.3 s after sentence ends, 0.1 s after commas, natural tempo.
import json, re, difflib, glob, sys, numpy as np, soundfile as sf, librosa, whisper
sys.path.insert(0, '/opt/models'); from utmos_score import score as utmos
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
P = '/home/user/shorts-ofisi/filmler/point-nemo'
L = json.load(open(P + '/lines.json'))
asr = whisper.load_model('small')
ve = ChatterboxMultilingualTTS.from_pretrained(device='cpu').ve
emb = lambda f: ve.embeds_from_wavs([librosa.load(f, sr=16000)[0]], sample_rate=16000)[0]
real = np.mean([emb(f'/home/user/shorts-ofisi/ses/temiz/bolum{k}.wav') for k in (2, 10, 17)], axis=0)
norm = lambda s: re.sub(r"[^a-zçğıöşü ]", "", s.replace('İ', 'i').replace('I', 'ı').lower().replace('point', 'poynt')).split()
picks = {}
for i, l in enumerate(L, 1):
    rows = []
    for f in sorted(glob.glob(f'{P}/voice/l{i:02d}_*.wav')):
        h = asr.transcribe(f, language='tr', fp16=False)['text']
        acc = difflib.SequenceMatcher(None, norm(l['say']), norm(h)).ratio()
        e = emb(f); sim = float(np.dot(real, e) / np.linalg.norm(real) / np.linalg.norm(e))
        rows.append([f, acc, sim, utmos(f), h.strip()])
    best = max(r[1] for r in rows); ok = [r for r in rows if r[1] >= best - .04]
    z = lambda v, a: (v - min(a)) / (max(a) - min(a) + 1e-9)
    S_ = [r[2] for r in ok]; U_ = [r[3] for r in ok]
    for r in ok: r.append(.55 * z(r[2], S_) + .45 * z(r[3], U_))
    win = max(ok, key=lambda r: r[5])
    for r in rows: print(i, r[0][-6:-4], f'acc={r[1]:.3f} sim={r[2]:.3f} mos={r[3]:.2f}', '*' if r is win else ' ', r[4], flush=True)
    picks[str(i)] = win[:4]
    x, sr = sf.read(win[0])
    ws = [w for s in asr.transcribe(win[0], language='tr', fp16=False, word_timestamps=True)['segments'] for w in s['words']]
    out, prev = [], 0
    for a, b in zip(ws, ws[1:]):
        tt = a['word'].strip(); g = .3 if tt.endswith(('.', '?', '!', ':')) else .1 if tt.endswith(',') else 0
        if g: j = int((a['end'] + b['start']) / 2 * sr); out += [x[prev:j], np.zeros(int(g * sr))]; prev = j
    out.append(x[prev:]); sf.write(f'{P}/voice/pick{i:02d}.wav', np.concatenate(out), sr)
json.dump({k: [v[1], f'{P}/voice/pick{int(k):02d}.wav', v[0]] for k, v in picks.items()}, open(P + '/picks.json', 'w'), indent=1)
print('done')
