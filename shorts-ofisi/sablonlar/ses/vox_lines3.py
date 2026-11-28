# Continuation mode: the prompt is the wife's own clip that contains "kase jöle", so the model copies her /ʒ/.
import json, sys, soundfile as sf, torch
from voxcpm import VoxCPM
P = sys.argv[1]; lines = [int(x) for x in sys.argv[2].split(',')]
S = '/home/user/shorts-ofisi/ses/'
PT2 = 'Bazen en sıradan şeylerin arkasında en şaşırtıcı hikâyeler saklanır. Mutfaktaki bir kase jöle, gökyüzündeki bir yıldız ya da binlerce yıl önce yazılmış bir kil tablet.'
m = VoxCPM.from_pretrained('openbmb/VoxCPM2', load_denoiser=False, optimize=False, device='cpu'); sr = m.tts_model.sample_rate
L = json.load(open(P + '/lines.json'))
for i in lines:
    for k in range(4):
        torch.manual_seed(4000 + 37 * i + k)
        w = m.generate(text=L[i - 1]['tr'], prompt_wav_path=S + 'ref2/notr_tam.wav', prompt_text=PT2, reference_wav_path=S + 'vc_hedef.wav', cfg_value=2.0, inference_timesteps=14)
        sf.write(f'{P}/raw3/l{i:02d}_c{k}.wav', w, sr); print('ok', i, k, flush=True)
