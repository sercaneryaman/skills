#!/bin/sh
set -e
P=/home/user/shorts-ofisi/filmler/point-nemo; cd $P
while pgrep -f "vox.py $P" >/dev/null; do sleep 30; done
python3 prep_voice.py > prep.log 2>&1
/opt/voxenv/bin/python assemble_tr.py > asm.log 2>&1
python3 mk_timing.py
python3 build.py
python3 audio.py
echo PREP_DONE; exit 0
cd .. && ffmpeg -loglevel error -y -i raw.mp4 -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=9 -c:a aac -b:a 192k -ar 48000 -ac 2 -movflags +faststart point_nemo.mp4
echo CHAIN_DONE
