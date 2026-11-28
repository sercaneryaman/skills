import json, sys, soundfile as sf, torch
from voxcpm import VoxCPM
P = sys.argv[1]
m = VoxCPM.from_pretrained('openbmb/VoxCPM2', load_denoiser=False, optimize=False, device='cpu'); sr = m.tts_model.sample_rate
for i, l in enumerate(json.load(open(P + '/lines.json')), 1):
    n = 6 if 'jöle' in l['tr'] or 'konserve' in l['tr'] else 4
    for k in range(n):
        torch.manual_seed(31 * i + 977 * k)
        w = m.generate(text=l['tr'], reference_wav_path='/home/user/shorts-ofisi/ses/vc_hedef.wav', cfg_value=2.0 if k % 2 == 0 else 2.6, inference_timesteps=14)
        sf.write(f'{P}/voice/l{i:02d}_{k}.wav', w, sr); print('ok', i, k, flush=True)
