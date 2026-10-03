#!/bin/bash
# Adds the kinetic look (the « Synapze v2 » style) to a motion-design project created by
# .claude/skills/motion-design/scripts/new-project.sh. Works offline-friendly: everything comes from the npm registry
# (fonts, GSAP) and GitHub (CC0 music), never from a font or script CDN.
#
#   bash .claude/skills/motion-design-kinetic/scripts/setup-kinetic.sh <project> [--music]
#
# Does:
#   - <project>/reference/fx.html        the executable FX kit (copied verbatim by every frame)
#   - <project>/frame.md                 the kinetic frame spec template (fill the {{...}})
#   - <project>/assets/vendor/gsap.min.js  local GSAP 3.14.2 (the root and every frame load it, never the CDN)
#   - <project>/assets/fonts/            Geist, Geist Mono, Instrument Serif, Caveat (SIL OFL, from npm packages)
#   - --music: sparse clone of github.com/SoundSafari/CC0-1.0-Music in ../soundsafari (CC0 tracks, see references/offline.md)
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SKILL="$(dirname "$HERE")"
ROOT="$(cd "$SKILL/../../.." && pwd)"
P="${1:-}"; MUSIC="${2:-}"
[ -n "$P" ] || { echo "usage: setup-kinetic.sh <project> [--music]" >&2; exit 1; }
case "$P" in /*) DST="$P" ;; *) DST="$ROOT/$P" ;; esac
[ -f "$DST/meta.json" ] || { echo "setup-kinetic: $DST is not a project (run motion-design/scripts/new-project.sh first)" >&2; exit 1; }

mkdir -p "$DST"/reference "$DST"/assets/{fonts,vendor,ui,music}
cp "$SKILL/assets/fx.html" "$DST/reference/fx.html"
if grep -q '{{' "$DST/frame.md" 2>/dev/null || [ ! -s "$DST/frame.md" ]; then cp "$SKILL/templates/frame.md" "$DST/frame.md"; fi

TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
cd "$TMP"
npm pack -q gsap@3.14.2 geist @fontsource/instrument-serif @fontsource/caveat >/dev/null 2>&1
tar -xzf gsap-3.14.2.tgz package/dist/gsap.min.js && cp package/dist/gsap.min.js "$DST/assets/vendor/" && rm -rf package
tar -xzf geist-*.tgz && G=package/dist/fonts
cp "$G/geist-sans/Geist-Variable.woff2" "$DST/assets/fonts/Geist-Variable.woff2"
cp "$G/geist-sans/Geist-Italic[wght].woff2" "$DST/assets/fonts/Geist-Italic-Variable.woff2"
cp "$G/geist-mono/GeistMono-Variable.woff2" "$DST/assets/fonts/GeistMono-Variable.woff2"
rm -rf package
tar -xzf fontsource-instrument-serif-*.tgz
cp package/files/instrument-serif-latin-400-italic.woff2 "$DST/assets/fonts/InstrumentSerif-Italic.woff2"
cp package/files/instrument-serif-latin-400-normal.woff2 "$DST/assets/fonts/InstrumentSerif-Regular.woff2"
rm -rf package
tar -xzf fontsource-caveat-*.tgz
cp package/files/caveat-latin-500-normal.woff2 "$DST/assets/fonts/Caveat-500.woff2"
echo "kinetic: fx.html, frame.md, gsap and $(ls "$DST/assets/fonts" | wc -l | tr -d ' ') fonts in $DST"

if [ "$MUSIC" = "--music" ]; then
  M="$ROOT/../soundsafari/cc0-1.0-music"
  if [ ! -d "$M/.git" ]; then
    mkdir -p "$(dirname "$M")"
    git clone -q --filter=blob:none --no-checkout https://github.com/SoundSafari/CC0-1.0-Music "$M"
  fi
  echo "music library: $M  (list: git -C $M ls-tree -r --name-only HEAD | grep -i mp3)"
  echo "extract one: git -C $M show HEAD:'<path>.mp3' > $DST/assets/music/<role>-<name>.mp3"
fi

echo "next: fill frame.md ({{...}}), then STORYBOARD.md with references/edit-grammar.md; grep -n '{{' $DST/frame.md must print nothing"
