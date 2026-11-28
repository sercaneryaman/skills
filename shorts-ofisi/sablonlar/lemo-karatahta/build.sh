#!/bin/sh
# Gökyüzü neden mavi? — Chalkboard (Lemo-Opuscar), 1080x1920. Voice takes are picked by prep_voice.py first.
set -e
P=$(cd "$(dirname "$0")" && pwd); LIB=/home/user/sercaneryaman/lemo-opuscar; VX=/opt/voxenv/bin/python
cd "$P"
$VX assemble_tr.py > out_asm.log 2>&1
python3 mk_timing.py
cd "$LIB"
node core/render/events.mjs "$P" --size 1080x1920
"$LIB/.venv/bin/python" "$P/audio.py"
node core/render/video.mjs "$P" --fps 30 --workers 3 --size 1080x1920 --out "$P/out/video.mp4"
sh core/render/mux.sh "$P/out/video.mp4" "$P/mix.wav" "$P/gokyuzu-neden-mavi.mp4" 30 1
echo "done: $P/gokyuzu-neden-mavi.mp4"
