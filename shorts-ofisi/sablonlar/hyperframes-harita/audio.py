# Point Nemo sound: cloned voice, ocean + wind beds (earshot), whoosh on both ISS passes, sonar ping on Point Nemo,
# soft pings on the islands, muted splashes for the spacecraft, and a slow synthesized drone pad ducked under the voice.
import json, numpy as np, soundfile as sf, librosa
from scipy.signal import butter, sosfilt
B = '/home/user/shorts-ofisi/filmler/point-nemo'; A = B + '/proj/assets'; SR = 48000
T = json.load(open(B + '/cues.json')); DUR = T['DUR']; N = int(SR * DUR); t = np.arange(N) / SR
lp = lambda x, f: sosfilt(butter(2, f, fs=SR, output='sos'), x, axis=0)
hp = lambda x, f: sosfilt(butter(2, f, btype='high', fs=SR, output='sos'), x, axis=0)
def load(n):
    y, _ = librosa.load(f'{B}/sfx/{n}', sr=SR, mono=True); return y / (np.abs(y).max() + 1e-9)
def put(buf, x, at, g=1.0, pan=0.0):
    i = int(at * SR)
    if i >= N: return
    if i < 0: x = x[-i:]; i = 0
    n = min(len(x), N - i); buf[i:i + n, 0] += x[:n] * g * (1 - pan) ** .5; buf[i:i + n, 1] += x[:n] * g * (1 + pan) ** .5
def env(a, b, fa=1.0, fb=1.0): return np.clip((t - a) / fa, 0, 1) * np.clip((b - t) / fb, 0, 1)
def bed(name, g):
    y = load(name); reps = int(np.ceil(N / len(y))) + 1
    out = np.zeros(N)                                                        # crossfaded loop
    pos, L, xf = 0, len(y), int(1.5 * SR); w = np.ones(L); w[:xf] = np.linspace(0, 1, xf); w[-xf:] = np.linspace(1, 0, xf)
    while pos < N:
        n = min(L, N - pos); out[pos:pos + n] += (y * w)[:n]; pos += L - xf
    return out * g
voice, fx, mus = (np.zeros((N, 2)) for _ in range(3))
v, sr = sf.read(A + '/voice.wav');  v = v.mean(1) if v.ndim > 1 else v
v = librosa.resample(v, orig_sr=sr, target_sr=SR) if sr != SR else v
voice[:min(N, len(v)), 0] = v[:N]; voice[:min(N, len(v)), 1] = v[:N]
vp = np.convolve(np.abs(voice[:, 0]), np.ones(int(.3 * SR)) / (.3 * SR), 'same'); vp = np.clip(vp / (vp.max() + 1e-9) * 3, 0, 1)
# beds: ocean while the sea is on screen (start and loop end), wind everywhere, quieter over the globe
oc = bed('ocean.wav', .16) * (env(-1, T['gecer'] + .9, 1, 1.4) + env(T['S']['7'] if '7' in T['S'] else T['E']['7'], DUR + 1, 1.2, 1))
wd = bed('wind.wav', .07) * (0.6 + 0.4 * env(-1, T['gecer'] + .8, 1, 1.2))
fx[:, 0] += oc + wd; fx[:, 1] += np.roll(oc, 2111) + np.roll(wd, 1777)
wh = load('whoosh.wav'); put(fx, wh, 1.4, .35, -.2); put(fx, wh, T['E']['7'] + 1.2, .35, .2)
pg = load('ping.wav'); pg = np.concatenate([pg, np.zeros(int(1.5 * SR))])
put(fx, pg, T['nemo'] - .05, .45, 0)
for k in range(3): put(fx, pg, T['uc'] + k * .18, .18, (k - 1) * .4)
sp = load('splash.wav')
for k in range(14): put(fx, lp(sp, 1800), T['omur'] - .3 + k * .3 + 1.5, .22, (k % 3 - 1) * .3)
# drone pad: D minor-ish open fifths, slow swell, warmer at the end
mf = lambda m: 440 * 2 ** ((m - 69) / 12)
def pad(notes, a, b, g):
    e = env(a, b, 2.5, 2.0)
    for m in notes:
        for det in (-.06, .06):
            f = mf(m + det); ph = np.random.default_rng(m).uniform(0, 6.28)
            x = np.sin(2 * np.pi * f * t + ph) + .35 * np.sin(4 * np.pi * f * t + ph) + .12 * np.sin(6 * np.pi * f * t)
            mus[:, 0] += x * e * g * (.6 if det < 0 else .4); mus[:, 1] += x * e * g * (.4 if det < 0 else .6)
s3 = T['S']['3']
pad([38, 45, 50], -1, s3 + 1, .035)
pad([38, 45, 50, 57], s3 - 1, T['S']['6'] + .5, .03)
pad([34, 41, 46, 53], T['S']['5'] - .5, T['S']['7'] + .5, .028)
pad([38, 45, 50, 54], T['S']['6'] - .5, DUR + 2, .03)
mus = lp(mus, 1500) * (1 - .5 * vp)[:, None]
mus[-int(1.5 * SR):] *= np.linspace(1, 0, int(1.5 * SR))[:, None]
mix = voice * 1.0 + fx * .9 + mus * .9
mix = hp(mix, 30); mix /= np.abs(mix).max() / .89
sf.write(A + '/mix.wav', mix.astype(np.float32), SR); print('mix', DUR)
