#!/usr/bin/env python3
"""Openverse search/download helper. Usage:
  ov.py images "wood frog" [--commercial] [--n 10] [--source wikimedia,flickr]
  ov.py audio "ice cracking" [--commercial] [--n 10]
  ov.py get images <id> <out_dir>      # downloads file (falls back to Openverse thumbnail) + writes <id>.credit.txt
Auth: optional env OPENVERSE_TOKEN (Bearer). Without it, anonymous limits apply (100/min, 1000/day per IP)."""
import json, os, sys, urllib.parse, urllib.request
API = 'https://api.openverse.org/v1/'
UA = {'User-Agent': 'shorts-research/1.0 (openverse skill)'}
def req(url, raw=False):
    h = dict(UA)
    if os.environ.get('OPENVERSE_TOKEN'): h['Authorization'] = 'Bearer ' + os.environ['OPENVERSE_TOKEN']
    import re, time
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=60) as r:
                return r.read() if raw else json.load(r)
        except urllib.error.HTTPError as e:
            body = e.read().decode('utf-8', 'replace')[:200]
            m = re.search(r'available in (\d+) seconds', body)
            if e.code == 429 and m and int(m.group(1)) <= 30 and attempt < 3:
                time.sleep(int(m.group(1)) + 1); continue
            sys.exit(f'HTTP {e.code} for {url}: {body}')
def credit(r):
    lic = f"{r.get('license','').upper()} {r.get('license_version') or ''}".strip()
    if lic.startswith('PDM') or lic.startswith('CC0'): lic += ' (kamu malı)'
    return f"{r.get('title') or 'Untitled'} — {r.get('creator') or 'bilinmiyor'} ({r.get('source')}), {lic}. {r.get('foreign_landing_url') or ''}"
def search(kind, q, args):
    p = {'q': q, 'page_size': args.get('n', '10'), 'mature': 'false'}
    if 'commercial' in args: p['license_type'] = 'commercial'
    if 'source' in args: p['source'] = args['source']
    d = req(API + kind + '/?' + urllib.parse.urlencode(p))
    print(f"{d.get('result_count')} sonuç")
    for r in d['results']:
        size = f"{r.get('width')}x{r.get('height')}" if kind == 'images' else f"{(r.get('duration') or 0)/1000:.1f}s"
        print(json.dumps({'id': r['id'], 'size': size, 'license': f"{r['license']} {r.get('license_version') or ''}".strip(),
                          'title': r.get('title'), 'creator': r.get('creator'), 'source': r.get('source'), 'url': r.get('url')}, ensure_ascii=False))
def get(kind, id_, out):
    os.makedirs(out, exist_ok=True)
    r = req(f'{API}{kind}/{id_}/')
    ext = (r.get('filetype') or os.path.splitext(urllib.parse.urlparse(r['url']).path)[1].lstrip('.') or 'bin')
    path = os.path.join(out, f'{id_}.{ext}')
    try:
        with urllib.request.urlopen(urllib.request.Request(r['url'], headers=UA), timeout=120) as f: data = f.read()
    except Exception as e:
        if kind != 'images': sys.exit(f'download failed: {e}')
        data = req(f'{API}images/{id_}/thumb/?full_size=true', raw=True); path = os.path.join(out, f'{id_}_thumb.jpg')
        print('original host blocked; saved Openverse thumbnail')
    open(path, 'wb').write(data)
    open(os.path.join(out, f'{id_}.credit.txt'), 'w').write(credit(r) + '\n')
    print(path); print(credit(r))
if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) < 2: sys.exit(__doc__)
    opts = {}; pos = []
    i = 0
    while i < len(a):
        if a[i].startswith('--'):
            k = a[i][2:]
            if k == 'commercial': opts[k] = True; i += 1
            else: opts[k] = a[i + 1]; i += 2
        else: pos.append(a[i]); i += 1
    if pos[0] in ('images', 'audio'): search(pos[0], ' '.join(pos[1:]), opts)
    elif pos[0] == 'get': get(pos[1], pos[2], pos[3])
    else: sys.exit(__doc__)
