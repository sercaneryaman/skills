# Cold-to-warm ambient bed + monitor beeps and SFX for the wood frog Short (timed from cues.json).
import json, wave
import numpy as np, soundfile as sf, librosa
from scipy.signal import butter, sosfilt

B = '/tmp/claude-0/-home-user/6836c550-55f1-5f08-ade5-0f6b86d03452/scratchpad/kurbaga'
A = B + '/proj/assets'; SR = 48000
TOT = json.load(open(B + '/meta.json'))['total']; C = json.load(open(B + '/cues.json'))
T, IN, BEATS = C['T'], {int(k): v for k, v in C['IN'].items()}, C['beats']
N = int(SR * TOT); t = np.arange(N) / SR; rng = np.random.default_rng(5)
lp = lambda x, f: sosfilt(butter(2, f, fs=SR, output='sos'), x)
hp = lambda x, f: sosfilt(butter(2, f, btype='high', fs=SR, output='sos'), x)
mf = lambda n: 440 * 2 ** ((n - 69) / 12)

def env(a, b, fade=1.5):
    e = np.clip((t - a) / fade, 0, 1) * np.clip((b - t) / fade, 0, 1); return e

# ---- music: detuned pad chords, cold (Am, Fmaj7) then warm (C, F, G) from scene 5
L = np.zeros(N); R = np.zeros(N)
def pad(notes, a, b, gain=0.05):
    e = env(a, b, 1.2)
    for n in notes:
        for d, pan in ((-0.07, 0.3), (0.07, 0.7)):
            ph = rng.uniform(0, 6.28); s = np.sin(2 * np.pi * mf(n + d) * t + ph) + 0.3 * np.sin(4 * np.pi * mf(n + d) * t + ph)
            L[:] += s * e * gain * (1 - pan); R[:] += s * e * gain * pan
warm = IN[5]
cold = [[45, 57, 60, 64], [41, 57, 60, 64], [43, 55, 59, 62], [45, 57, 60, 64]]
seg = warm / len(cold)
for i, ch in enumerate(cold): pad(ch, i * seg - 0.6, (i + 1) * seg + 0.6, 0.035)
wch = [[48, 60, 64, 67], [41, 60, 65, 69], [43, 59, 62, 67], [48, 60, 64, 67]]
seg2 = (TOT - warm) / len(wch)
for i, ch in enumerate(wch): pad(ch, warm + i * seg2 - 0.6, warm + (i + 1) * seg2 + 0.6, 0.04)
L = lp(L, 1800); R = lp(R, 1800)
# soft piano-like note on the first heartbeat in spring, then a few more
def piano(f, at, g=0.22, d=3.5):
    i = int(at * SR); n = min(int(d * SR), N - i)
    if n <= 0: return
    tt = np.arange(n) / SR
    s = sum(np.sin(2 * np.pi * f * k * tt) * (0.6 ** (k - 1)) for k in range(1, 6)) * np.exp(-tt * 1.6) * (1 - np.exp(-tt * 300))
    L[i:i + n] += s * g; R[i:i + n] += s * g
piano(mf(72), T['kalptir']); piano(mf(76), T['kalptir'] + 0.02, 0.12)
piano(mf(67), T['neyin'], 0.12); piano(mf(72), T['diri'], 0.15); piano(mf(76), T['diri'] + 0.3, 0.1)
m = np.stack([L, R], 1); m /= np.abs(m).max() + 1e-9; m *= 0.6
sf.write(A + '/music.wav', m, SR)

# ---- sfx
X = np.zeros((N, 2))
def put(sig, at, g=1.0):
    if sig.ndim == 1: sig = np.stack([sig, sig], 1)
    i = int(at * SR)
    if i >= N: return
    if i < 0: sig = sig[-i:]; i = 0
    n = min(len(sig), N - i); X[i:i + n] += sig[:n] * g
def load(name, dur=None):
    y, _ = librosa.load(f'{B}/sfx/{name}', sr=SR, mono=False)
    y = y.T if y.ndim == 2 else y
    if dur: y = y[:int(dur * SR)]
    y = y / (np.abs(y).max() + 1e-9)
    f = np.minimum(1, np.minimum(np.arange(len(y)), len(y) - np.arange(len(y))) / (0.05 * SR))
    return y * (f[:, None] if y.ndim == 2 else f)
# monitor beeps: louder when the big monitor shows (scenes 1 and 7)
bt = np.arange(int(0.09 * SR)) / SR; beep = np.sin(2 * np.pi * 980 * bt) * np.exp(-bt * 18) * (1 - np.exp(-bt * 900))
for b in BEATS:
    big = b < IN[2] or b > IN[7]
    put(beep, b + 0.015, 0.33 if big else 0.13)
    # low heart thump under each beat
    th = np.sin(2 * np.pi * 55 * bt * 2) * np.exp(-bt * 30); put(th, b, 0.35 if big else 0.18)
# flatline tones
def flat(a, b, g):
    n = int((b - a) * SR); tt = np.arange(n) / SR; s = np.sin(2 * np.pi * 980 * tt)
    s *= np.minimum(1, np.minimum(tt, (b - a) - tt) / 0.08); put(s, a, g)
flat(T['duruyor'] + 0.35, T['baharda'] - 0.2, 0.12)
flat(T['durur'] + 0.3, IN[4] + 0.3, 0.07)
put(load('ice.wav', 2.0), T['duruyor'] - 0.4, 0.55)
put(load('ice.wav', 2.0), T['hava'] - 0.1, 0.45); put(load('ice.wav', 2.0), T['buza'] - 0.2, 0.35)
w = load('wind.wav'); w = w[:int((IN[5] - IN[2] + 1) * SR)]; w = w * np.minimum(1, np.minimum(np.arange(len(w)), len(w) - np.arange(len(w))) / SR / 1.0).reshape(-1, *([1] * (w.ndim - 1))); put(w, IN[2], 0.22)
put(load('leaves.wav', 2.5), IN[2] + 0.2, 0.35)
put(load('shimmer.wav', 2.5), T['glikoz'] - 0.1, 0.3); put(load('shimmer.wav', 2.0), T['antifriz'] - 0.1, 0.25)
put(load('drip.wav', 1.5), T['cozulur'] + 0.35, 0.5)
X = hp(X.T, 40).T
X /= np.abs(X).max() + 1e-9; X *= 0.8
sf.write(A + '/sfx.wav', X, SR)
print('audio ok', TOT)
