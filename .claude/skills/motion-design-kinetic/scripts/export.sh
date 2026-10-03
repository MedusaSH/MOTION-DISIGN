#!/bin/bash
# Delivery exports of a rendered film, one per destination, each checked (codec, level, size, loudness).
#
#   bash export.sh <render.mp4> [out_dir]      -> <name>-web.mp4, <name>-social.mp4, <name>-whatsapp.mp4
#
#   web       site / YouTube / LinkedIn upload: H.264 High 4.1, CRF 17, AAC 192k, faststart (the master quality)
#   social    TikTok / Instagram Reels / Shorts / LinkedIn: H.264 High 4.0, CRF 18 capped 6 Mb/s, 2 s GOP, AAC 192k
#   whatsapp  shown as a video in the chat: H.264 High 4.0, ref 3, size budget 15 MB, AAC 128k
# All: yuv420p, 30 fps constant, BT.709, -movflags +faststart. Works for 16:9 and 9:16 (dimensions are kept).
# WhatsApp also needs the file to be sent from the Gallery/Photos picker, not as a Document.
set -euo pipefail
IN="${1:?usage: export.sh <render.mp4> [out_dir]}"
OUT="${2:-$(dirname "$IN")}"
mkdir -p "$OUT"
NAME="$(basename "${IN%.*}")"
DUR="$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$IN")"
COMMON=(-pix_fmt yuv420p -r 30 -colorspace bt709 -color_primaries bt709 -color_trc bt709 -movflags +faststart -ar 48000 -ac 2)

ffmpeg -v error -y -i "$IN" -c:v libx264 -profile:v high -level:v 4.1 -preset slow -crf 17 \
  -x264-params ref=4:bframes=3:keyint=60:min-keyint=30:open-gop=0 "${COMMON[@]}" -c:a aac -b:a 192k "$OUT/$NAME-web.mp4"
ffmpeg -v error -y -i "$IN" -c:v libx264 -profile:v high -level:v 4.0 -preset slow -crf 18 -maxrate 6000k -bufsize 12000k \
  -x264-params ref=3:bframes=2:keyint=60:min-keyint=30:open-gop=0 "${COMMON[@]}" -c:a aac -b:a 192k "$OUT/$NAME-social.mp4"
# WhatsApp: bitrate from a 15 MB budget (minus audio), two-pass for an exact size
VBR=$(python3 -c "d=float('$DUR'); print(max(600, int((15*8*1000*1000/d - 128000)/1000*0.97)))")
P2="$(mktemp -d)"
ffmpeg -v error -y -i "$IN" -c:v libx264 -profile:v high -level:v 4.0 -preset slow -b:v ${VBR}k -maxrate $((VBR*3/2))k -bufsize $((VBR*3))k \
  -x264-params ref=3:bframes=2:keyint=60:min-keyint=30:open-gop=0 -pass 1 -passlogfile "$P2/x" -an -f mp4 /dev/null
ffmpeg -v error -y -i "$IN" -c:v libx264 -profile:v high -level:v 4.0 -preset slow -b:v ${VBR}k -maxrate $((VBR*3/2))k -bufsize $((VBR*3))k \
  -x264-params ref=3:bframes=2:keyint=60:min-keyint=30:open-gop=0 -pass 2 -passlogfile "$P2/x" "${COMMON[@]}" -c:a aac -b:a 128k "$OUT/$NAME-whatsapp.mp4"
rm -rf "$P2"

for f in web social whatsapp; do
  F="$OUT/$NAME-$f.mp4"
  V=$(ffprobe -v error -select_streams v -show_entries stream=width,height,profile,level -of csv=p=0 "$F")
  S=$(du -m "$F" | cut -f1)
  L=$(ffmpeg -i "$F" -af ebur128=peak=true -f null - 2>&1 | awk '/Summary/{s=1} s&&/I:/{print $2" LUFS"; exit}')
  E=$(ffmpeg -v error -i "$F" -f null - 2>&1 | head -1)
  printf "%-9s %s  %s MB  %s  %s\n" "$f" "$V" "$S" "$L" "${E:-decode ok}"
done
