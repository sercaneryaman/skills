# Playful ukulele-style bed (Karplus-Strong plucks) and SFX for the pineapple jelly Short.
import json, re, subprocess, wave
import numpy as np
from scipy.signal import butter, sosfilt

B = '/tmp/claude-0/-home-user/6836c550-55f1-5f08-ade5-0f6b86d03452/scratchpad/jole'
A = B + '/proj/assets'; SR = 48000
TOT = json.load(open(B + '/meta.json'))['total']
segs = json.load(open(B + '/segs.json')); words = json.load(open(B + '/words.json'))
S = {s['i']: s['start'] for s in segs}; E = {s['i']: s['end'] for s in segs}
norm = lambda s: re.sub(r"[^a-zçğıöşü0-9]", '', s.replace('İ', 'i').replace('I', 'ı').lower())
def Wd(p, ln):
    return next((w['s'] for w in words if w['line'] == ln and norm(w['w']).startswith(p)), S[ln])
N = int(SR * TOT); t = np.arange(N) / SR; rng = np.random.default_rng(11)
hp = lambda x, f: sosfilt(butter(2, f, btype='high', fs=SR, output='sos'), x)
lp = lambda x, f: sosfilt(butter(2, f, fs=SR, output='sos'), x)
mf = lambda n: 440 * 2 ** ((n - 69) / 12)

def pluck(f, d=0.9, bright=0.5):
    n = int(d * SR); p = max(2, int(SR / f)); buf = rng.uniform(-1, 1, p) * bright + rng.uniform(-1, 1, p) * (1 - bright) * 0.3
    out = np.zeros(n)
    for i in range(n):
        out[i] = buf[i % p]; buf[i % p] = 0.5 * (buf[i % p] + buf[(i + 1) % p]) * 0.996
    return out * np.exp(-np.arange(n) / SR * 2.2)

L = np.zeros(N); R = np.zeros(N)
def put(sig, at, gl=1.0, gr=1.0):
    i = int(at * SR)
    if i >= N or i < 0: return
    n = min(len(sig), N - i); L[i:i + n] += sig[:n] * gl; R[i:i + n] += sig[:n] * gr
cache = {}
def P(n, d=0.9):
    if (n, d) not in cache: cache[(n, d)] = pluck(mf(n), d)
    return cache[(n, d)]
bpm = 104; beat = 60 / bpm
prog = [[60, 64, 67, 72], [57, 60, 64, 69], [53, 57, 60, 65], [55, 59, 62, 67]]  # C Am F G
pattern = [0, 2, 1, 3, 2, 1, 3, 2]  # eighth-note strum picking
start = 0.2
for k in range(int((TOT - start) / (beat / 2))):
    at = start + k * beat / 2; ch = prog[(k // 8) % 4]
    put(P(ch[pattern[k % 8]] , 0.8) * (0.16 if k % 2 == 0 else 0.11), at, 0.9 if k % 2 else 1.0, 1.0 if k % 2 else 0.85)
    if k % 8 == 0: put(P(ch[0] - 12, 1.6) * 0.22, at)
    if k % 2 == 1:  # soft shaker
        x = np.arange(int(0.05 * SR)) / SR; put(hp(rng.standard_normal(len(x)), 5500) * np.exp(-x * 70) * 0.05, at)
# little glockenspiel sparkle on key moments
def glock(n):
    x = np.arange(int(1.2 * SR)) / SR; f = mf(n)
    return (np.sin(2 * np.pi * f * x) + 0.4 * np.sin(2 * np.pi * 2.76 * f * x)) * np.exp(-x * 4)
for at, n in ((Wd('donar', 6), 84), (Wd('abone', 7), 88)): put(glock(n) * 0.18, at); put(glock(n + 7) * 0.12, at + 0.12)
M = np.stack([L, R], 1)
env = np.clip(t / 0.4, 0, 1) * np.clip((TOT - t) / 1.0, 0, 1)
# duck a little under the thinking pause, drop out at the hook collapse for impact
dip = np.ones(N); i0, i1 = int((E[3]) * SR), int((S[4]) * SR); dip[i0:i1] = 0.55
M *= (env * dip)[:, None]; M /= np.max(np.abs(M)) * 1.2

X = np.zeros((N, 2))
def load(name):
    raw = subprocess.check_output(['ffmpeg', '-loglevel', 'error', '-i', f'{B}/sfx/{name}.wav', '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-'])
    return np.frombuffer(raw, np.float32).reshape(-1, 2)
def place(name, at, g=1.0, maxlen=None):
    a = load(name)
    if maxlen: a = a[:int(maxlen * SR)] * np.linspace(1, 0, min(len(a), int(maxlen * SR)))[:, None] ** 0.5
    i = int(at * SR)
    if i < 0: a = a[-i:]; i = 0
    n = min(len(a), N - i); X[i:i + n] += a[:n] * g
TR = 0.45
place('slurp', Wd('donmad', 1) - 0.05, 0.75, maxlen=1.2)
for k in range(2, 8): place('flip', S[k] - TR - 0.05, 0.55)
place('pop', Wd('jelatin', 2), 0.35); place('pop', Wd('buzdolab', 2), 0.35)
place('pop', Wd('ananas', 2) + 0.1, 0.6); place('slurp', Wd('ananas', 2) + 0.35, 0.35, maxlen=0.6)
place('rustle', S[3], 0.4, maxlen=0.8)
place('pop', Wd('suyu', 4), 0.3); place('pop', Wd('hapseder', 4), 0.3)
for c in range(3): place('snip', Wd('keser', 5) - 0.05 + c * 0.35, 0.65, maxlen=0.5)
place('bubbles', Wd('ısıtıl', 6) - 0.2, 0.4, maxlen=2.0)
place('pof', Wd('bozulur', 6), 0.7)
place('ding', Wd('donar', 6), 0.4)
place('pop', Wd('kivi', 7), 0.5); place('pop', Wd('papaya', 7), 0.5)
place('ding', Wd('abone', 7), 0.45)
X /= max(1.0, np.max(np.abs(X)) * 1.05)
def save(x, p):
    w = wave.open(p, 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(x, -1, 1) * 32767).astype('<i2').tobytes()); w.close()
save(M, A + '/music.wav'); save(X, A + '/sfx.wav'); print('ok', TOT)
