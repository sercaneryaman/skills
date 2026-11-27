#!/usr/bin/env python3
"""One-time Openverse app registration. Reads the contact address from env OPENVERSE_EMAIL
(set by the user), saves client credentials to ~/.config/openverse/credentials.json (0600), prints no secrets."""
import json, os, sys, urllib.request as u
mail = os.environ.get('OPENVERSE_EMAIL')
if not mail: sys.exit('OPENVERSE_EMAIL not set')
r = u.Request('https://api.openverse.org/v1/auth_tokens/register/', headers={'Content-Type': 'application/json', 'User-Agent': 'shorts-research/1.0'},
              data=json.dumps({'name': 'shorts-research-app', 'description': 'Openly licensed images and sounds for educational YouTube Shorts, with attribution.', 'email': mail}).encode())
d = json.load(u.urlopen(r, timeout=60))
p = os.path.expanduser('~/.config/openverse/credentials.json'); os.makedirs(os.path.dirname(p), mode=0o700, exist_ok=True)
fd = os.open(p, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600); os.write(fd, json.dumps(d).encode()); os.close(fd)
print('registered', d.get('name'), '- check the inbox for the verification link')
