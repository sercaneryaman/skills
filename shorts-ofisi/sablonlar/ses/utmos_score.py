# UTMOS naturalness score (1-5) for wav files, on CPU. utmos_cpu.jit is balacoon/utmos with its hardcoded
# "cuda:0" device strings replaced by "cpu". Usage: python3 utmos_score.py a.wav b.wav ...
import sys, torch, librosa, numpy as np
M = torch.jit.load('/opt/models/utmos/utmos_cpu.jit', map_location='cpu').eval()
def score(f):
    y, _ = librosa.load(f, sr=16000, mono=True)
    y = y / (np.abs(y).max() + 1e-9) * .9
    with torch.no_grad(): return float(M(torch.tensor((y * 32767).astype(np.int16)).unsqueeze(0)).item())
if __name__ == '__main__':
    for f in sys.argv[1:]: print(f'{score(f):.3f}  {f}')
