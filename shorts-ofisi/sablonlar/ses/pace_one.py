import sys, json, subprocess, numpy as np, soundfile as sf, whisper
P = '/tmp/claude-0/-home-user/6836c550-55f1-5f08-ade5-0f6b86d03452/scratchpad/kurbaga'
i, src = int(sys.argv[1]), sys.argv[2]
asr = whisper.load_model('small'); x, sr = sf.read(src)
ws = [w for s in asr.transcribe(src, language='tr', fp16=False, word_timestamps=True)['segments'] for w in s['words']]
out, prev = [], 0
for a, b in zip(ws, ws[1:]):
    t = a['word'].strip(); g = 0.28 if t.endswith(('.', '?', '!', ':')) else 0.1 if t.endswith(',') else 0
    if g:
        j = int((a['end'] + b['start']) / 2 * sr); out += [x[prev:j], np.zeros(int(g * sr))]; prev = j
out.append(x[prev:]); sf.write(f'{P}/voice/pick{i:02d}.wav', np.concatenate(out), sr)
p = json.load(open(P + '/picks.json')); p[str(i)][2] = src; json.dump(p, open(P + '/picks.json', 'w'), indent=1)
