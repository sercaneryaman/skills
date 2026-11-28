"""Sound for "Gökyüzü neden mavi?" (Chalkboard) -> mix.wav (48 kHz stereo, DUR seconds).
Voice: assets/voice.wav (the user's cloned voice, already laid out by assemble_tr.py). Chalk: CC0 Freesound recordings
(via Openverse) cut into grains, one grain chain per stroke. Score: a quiet nylon-guitar arpeggio (Karplus-Strong),
ducked under the voice. Room tone very low. Run with the library venv:  $LIB/.venv/bin/python audio.py"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); LIB = '/home/user/sercaneryaman/lemo-opuscar'
sys.path.insert(0, LIB)
import numpy as np, soundfile as sf, soxr
from core.audio.sfx import SR, add, hp, lp, brown

rng = np.random.default_rng(7)
EV = json.load(open(os.path.join(HERE, 'events.json')))
DUR = EV['dur']; ev = EV['ev']; N = int(round(DUR * SR))
voice, fx, mus = (np.zeros((N, 2), np.float32) for _ in range(3))

def fade(x, a=.004, b=.03):
    n = len(x); a, b = min(int(a * SR), n // 2), min(int(b * SR), n // 2)
    x = x.copy(); x[:a] *= np.linspace(0, 1, a); x[n - b:] *= np.linspace(1, 0, b); return x

# voice
x, sr = sf.read(os.path.join(HERE, 'assets/voice.wav'), dtype='float32')
if x.ndim > 1: x = x.mean(1)
if sr != SR: x = soxr.resample(x, sr, SR)
add(voice, x[:N], 0, 1.0, 0)
vp = np.abs(voice[:, 0]); k = int(.3 * SR); vp = np.convolve(vp, np.ones(k) / k, 'same'); vp = np.clip(vp / (vp.max() + 1e-9) * 3, 0, 1)

# chalk
IDX = json.load(open(os.path.join(HERE, 'foley/lib/index.json')))
strokes = [g for g in IDX if g['kind'] == 'stroke']; taps = [g for g in IDX if g['kind'] == 'tap']
cache = {}
def grain(g):
    if g['file'] not in cache:
        y, s = sf.read(os.path.join(HERE, 'foley/lib', g['file']), dtype='float32')
        if y.ndim > 1: y = y.mean(1)
        if s != SR: y = soxr.resample(y, s, SR)
        cache[g['file']] = y / (np.abs(y).max() + 1e-9)
    return cache[g['file']]
def chalk(d, v, soft=False):
    out = np.zeros(int((d + .06) * SR), np.float32); pos = 0
    while pos < len(out) - int(.03 * SR):
        g = grain(strokes[rng.integers(len(strokes))]); n = min(len(g), len(out) - pos)
        out[pos:pos + n] += fade(g[:n], .006, .02); pos += max(int(.6 * n), int(.04 * SR))
    env = np.ones(len(out)); a = int(.012 * SR); env[:a] = np.linspace(.3, 1, a); m = int(.05 * SR); env[-m:] *= np.linspace(1, 0, m)
    out = out * env; out = lp(out, 3800) if soft else hp(out, 500)
    return (out * v).astype(np.float32)
for e in ev:
    if e['type'] != 'chalk' or e['t'] < 0: continue
    d = max(.04, e['d']); size = min(1.0, e['len'] / 700); v = (.10 + .26 * size) * (1.2 if e['big'] else .8)
    add(fx, chalk(d, v, e['color'] in ('blue', 'kid')), e['t'], 1.0, e['pan'])
    if d > .12 and rng.random() < .5:
        add(fx, fade(grain(taps[rng.integers(len(taps))]), .002, .03) * .3 * v, e['t'] - .005, 1.0, e['pan'])
for e in [x for x in ev if x['type'] == 'wipe']:                 # the felt pass
    d = e['d']; w = lp(brown(d + .2), 1400) * np.sin(np.pi * np.clip(np.arange(int((d + .2) * SR)) / SR / (d + .2), 0, 1)) ** .6
    add(fx, (w * .25).astype(np.float32), e['t'], 1.0, 0)
room = lp(brown(DUR), 900) * .005; fx[:, 0] += room[:N]; fx[:, 1] += np.roll(room, 997)[:N]

# score: nylon-guitar arpeggio, C major -> A minor -> F -> G, slow; warmer at the sunset
def pluck(f, d=2.2, b=.5):
    n = int(d * SR); p = max(2, int(SR / f)); buf = rng.uniform(-1, 1, p) * b; out = np.zeros(n)
    for i in range(n):
        out[i] = buf[i % p]; buf[i % p] = .5 * (buf[i % p] + buf[(i + 1) % p]) * .997
    return lp(out * np.exp(-np.arange(n) / SR * 1.6), 2600)
mf = lambda m: 440 * 2 ** ((m - 69) / 12); C = {}
prog = [[48, 55, 60, 64, 67], [45, 52, 57, 60, 64], [41, 48, 53, 57, 60], [43, 50, 55, 59, 62]]
beat = 60 / 76 / 2; t = .4; i = 0
while t < DUR - 1.2:
    ch = prog[(i // 8) % 4]; m = ch[[0, 2, 3, 4, 3, 2, 1, 2][i % 8]]
    if m not in C: C[m] = pluck(mf(m))
    pan = -.3 + .6 * ((i % 8) / 7)
    add(mus, C[m].astype(np.float32) * (.22 if i % 8 == 0 else .14), t, 1.0, pan); t += beat; i += 1
duck = 1 - .55 * vp; mus *= duck[:, None]
tail = int(1.2 * SR); mus[-tail:] *= np.linspace(1, 0, tail)[:, None]

mix = voice * 1.0 + fx * .9 + mus * .5
mix = hp(mix.T, 35).T
mix /= max(1e-9, np.abs(mix).max()) / .89
sf.write(os.path.join(HERE, 'mix.wav'), mix.astype(np.float32), SR)
print('mix', DUR)
