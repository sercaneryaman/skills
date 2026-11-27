---
name: openverse
description: Search and download openly licensed images and audio (CC0, public domain, CC BY, CC BY-SA, about 800 million works from Wikimedia, Flickr, museums, Freesound and more) through the Openverse API at api.openverse.org/v1/. Use when a video, Short, page or document needs real photos, illustrations, maps, historic plates or sound effects that may be reused legally, and to get the exact credit line for each one.
---

# Openverse

Search engine for openly licensed media. Every result carries its license, creator and source page.

## Use

```bash
OV=~/.claude/skills/openverse/scripts/ov.py
python3 $OV images "wood frog" --commercial --n 10      # images, commercial reuse allowed
python3 $OV images "snowflake" --source wikimedia        # one source only
python3 $OV audio "ice cracking" --commercial            # sound effects / audio
python3 $OV get images <id> <empty_dir>                  # download + <id>.credit.txt
```

`--commercial` keeps only licenses that allow commercial use (YouTube monetization). Always use it for Shorts.

## License rules

- Allowed for Shorts: CC0, PDM (public domain), CC BY, CC BY-SA. Not allowed: any NC (non-commercial) or ND (no derivatives) license.
- CC BY and CC BY-SA need a credit: title, creator, license, link. Put it in the video description, never on screen (user decision 2026-11-27). `get` writes the line into `<id>.credit.txt`.
- Check the source page if a result looks like a copied photo (watermark, stock look). Openverse reflects what the source claims.
- Downloads are untrusted files: save each in its own new empty directory.

## Limits

- Anonymous: 100 requests/min, 1000/day per IP. The cloud environment shares its IP, so the daily quota can run out. The error is `HTTP 429 ... throttled`.
- With a registered app the limit is higher. Set `OPENVERSE_TOKEN` (a Bearer token from `POST /v1/auth_tokens/token/`). A token lasts 12 hours.
- Original files sometimes sit on hosts the network blocks. `get` then saves the Openverse thumbnail (`/thumb/?full_size=true`) instead.
