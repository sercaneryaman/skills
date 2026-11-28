# Pick the best VoxCPM2 candidate per line (transcript match first, then speaker similarity),
# then pace it: short pauses after sentence ends / commas, natural tempo (user found -8% too slow).
import json, re, difflib, subprocess, numpy as np, soundfile as sf, librosa, whisper
from chatterbox.mtl_tts import ChatterboxMultilingualTTS

P = '/tmp/claude-0/-home-user/6836c550-55f1-5f08-ade5-0f6b86d03452/scratchpad/jole'
L = json.load(open(P + '/lines.json'))
asr = whisper.load_model('small')
ve = ChatterboxMultilingualTTS.from_pretrained(device='cpu').ve
emb = lambda f: ve.embeds_from_wavs([librosa.load(f, sr=16000)[0]], sample_rate=16000)[0]
real = emb('/home/user/shorts-ofisi/ses/temiz/bolum17.wav')
norm = lambda s: re.sub(r"[^a-zçğıöşü ]", "", s.replace('İ', 'i').replace('I', 'ı').lower()).split()
picks = {}
for i, l in enumerate(L, 1):
    best = None
    import glob
    for f in sorted(glob.glob(f'{P}/voice/l{i:02d}_*.wav')):
        k = f.rsplit('_', 1)[1][:-4]
        h = asr.transcribe(f, language='tr', fp16=False)['text']
        acc = difflib.SequenceMatcher(None, norm(l['tr']), norm(h)).ratio()
        # Whisper hears the real /ʒ/ of "jöle" as jöle/jole; coley/zöle/yöle mean a bad pronunciation
        need = len(re.findall(r'jöle', l['tr'].lower())); got = len(re.findall(r'j[öo]le', h.lower()))
        acc -= 0.08 * max(0, need - got)
        e = emb(f); sim = float(np.dot(real, e) / np.linalg.norm(real) / np.linalg.norm(e))
        print(i, k, round(acc, 3), round(sim, 3), h.strip(), flush=True)
        if best is None or acc > best[0] + 0.02 or (abs(acc - best[0]) <= 0.02 and sim > best[1]):
            best = (acc, sim, f)
    picks[str(i)] = best
    # pace: insert pauses at punctuation (word gaps), then slow 8%
    x, sr = sf.read(best[2])
    ws = [w for s in asr.transcribe(best[2], language='tr', fp16=False, word_timestamps=True)['segments'] for w in s['words']]
    out, prev = [], 0
    for a, b in zip(ws, ws[1:]):
        t = a['word'].strip(); g = 0.28 if t.endswith(('.', '?', '!', ':')) else 0.1 if t.endswith(',') else 0
        if g:
            j = int((a['end'] + b['start']) / 2 * sr); out += [x[prev:j], np.zeros(int(g * sr))]; prev = j
    out.append(x[prev:]); sf.write(f'{P}/voice/p{i:02d}.wav', np.concatenate(out), sr)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{P}/voice/p{i:02d}.wav', '-af', 'atempo=1.0', f'{P}/voice/pick{i:02d}.wav'], check=True)
json.dump({k: [v[0], f'{P}/voice/pick{int(k):02d}.wav', v[2]] for k, v in picks.items()}, open(P + '/picks.json', 'w'), indent=1)
print('done')
