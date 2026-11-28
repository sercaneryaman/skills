# 6 takes per line: 3 with the default 23 s reference, 3 with the calm documentary tone reference.
import json, sys, os, soundfile as sf, torch
from voxcpm import VoxCPM
P = sys.argv[1]; S = '/home/user/shorts-ofisi/ses'
m = VoxCPM.from_pretrained('openbmb/VoxCPM2', load_denoiser=False, optimize=False, device='cpu'); sr = m.tts_model.sample_rate
REFS = [S + '/vc_hedef.wav', S + '/ref/belgesel.wav']
for i, l in enumerate(json.load(open(P + '/lines.json')), 1):
    for k in range(6):
        if os.path.exists(f'{P}/voice/l{i:02d}_{k}.wav'): continue
        torch.manual_seed(37 * i + 1009 * k)
        w = m.generate(text=l['say'], reference_wav_path=REFS[k // 3], cfg_value=2.0, inference_timesteps=14)
        sf.write(f'{P}/voice/l{i:02d}_{k}.wav', w, sr); print('ok', i, k, flush=True)
