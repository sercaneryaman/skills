# Turkish narration in the cloned voice: 3 candidates per line, pick by Whisper match.
import json, re, difflib, sys, torch, torchaudio, whisper
torch.set_num_threads(4)
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
B = sys.argv[1]; REF = sys.argv[2]
m = ChatterboxMultilingualTTS.from_pretrained(device='cpu'); asr = whisper.load_model('small')
L = json.load(open(B + '/lines.json'))
norm = lambda s: re.sub(r"[^a-zçğıöşü0-9 ]", "", s.replace('İ', 'i').replace('I', 'ı').lower()).split()
picks = {}
for i, l in enumerate(L, 1):
    best = None
    for k, (seed, ex, cfg) in enumerate([(3, 0.5, 0.5), (11, 0.55, 0.45), (29, 0.45, 0.5)]):
        torch.manual_seed(seed)
        wav = m.generate(l['tr'], language_id='tr', audio_prompt_path=l.get('ref', REF), exaggeration=ex, cfg_weight=cfg, temperature=0.7)
        f = f'{B}/voice/l{i:02d}_{k}.wav'; torchaudio.save(f, wav, m.sr)
        hyp = asr.transcribe(f, language='tr', fp16=False)['text']
        sc = difflib.SequenceMatcher(None, norm(l['tr']), norm(hyp)).ratio()
        print(i, k, round(sc, 3), round(wav.shape[-1] / m.sr, 2), hyp.strip(), flush=True)
        if not best or sc > best[0] + 0.02: best = (sc, f, hyp.strip())
    picks[str(i)] = best; json.dump(picks, open(B + '/picks.json', 'w'), ensure_ascii=False, indent=1)
