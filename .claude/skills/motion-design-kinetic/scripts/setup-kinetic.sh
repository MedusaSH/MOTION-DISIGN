#!/bin/bash
# Prepares a motion-design project for the kinetic method, for ANY brand, in one command.
# The project must exist (motion-design/scripts/new-project.sh <project>). Sources: npm registry (fonts, GSAP) and
# GitHub (CC0 music) only, never a font or script CDN.
#
#   bash .claude/skills/motion-design-kinetic/scripts/setup-kinetic.sh <project> [options]
#     --format 16:9|9:16     canvas 1920x1080 (site, YouTube, LinkedIn) or 1080x1920 (TikTok, Reels, Shorts). Default 16:9
#     --url <site>           run site-intel.py (brand dossier, screenshots, logo, palette, demo videos) then theme it
#     --accent "#RRGGBB"     brand color (else: from the site with --url, else the default orange)
#     --preset <name>        grounds: nuit-papier (default), encre, foret, mono, creme (theme.py --list-presets)
#     --display/--serif/--mono "<Family>"   fonts from npm @fontsource (default Geist / Instrument Serif / Geist Mono)
#     --music                sparse clone of the CC0 music library (github.com/SoundSafari/CC0-1.0-Music)
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SKILL="$(dirname "$HERE")"
ROOT="$(cd "$SKILL/../../.." && pwd)"
P="${1:-}"; shift || true
[ -n "$P" ] || { echo "usage: setup-kinetic.sh <project> [--format 16:9|9:16] [--url URL] [--accent #hex] [--preset name] [--music]" >&2; exit 1; }
FORMAT="16:9"; URL=""; ACCENT=""; PRESET="nuit-papier"; MUSIC=""; FONTS=()
while [ $# -gt 0 ]; do
  case "$1" in
    --format) FORMAT="$2"; shift 2 ;;
    --url) URL="$2"; shift 2 ;;
    --accent) ACCENT="$2"; shift 2 ;;
    --preset) PRESET="$2"; shift 2 ;;
    --display|--serif|--mono) FONTS+=("$1" "$2"); shift 2 ;;
    --music) MUSIC=1; shift ;;
    *) echo "setup-kinetic: unknown option $1" >&2; exit 1 ;;
  esac
done
case "$P" in /*) DST="$P" ;; *) DST="$ROOT/$P" ;; esac
[ -f "$DST/meta.json" ] || { echo "setup-kinetic: $DST is not a project (run motion-design/scripts/new-project.sh first)" >&2; exit 1; }

mkdir -p "$DST"/reference "$DST"/assets/{fonts,vendor,ui,music,brand}
if [ "$FORMAT" = "9:16" ]; then
  cp "$SKILL/assets/fx-9x16.html" "$DST/reference/fx.html"
  python3 - "$DST" <<'EOF'
import json, re, sys
d = sys.argv[1]
m = json.load(open(f"{d}/meta.json")); m["width"], m["height"] = 1080, 1920
json.dump(m, open(f"{d}/meta.json", "w"), indent=2)
s = open(f"{d}/STORYBOARD.md", encoding="utf-8").read()
s = re.sub(r"(?m)^format: .*$", "format: 1080x1920", s, count=1)
open(f"{d}/STORYBOARD.md", "w", encoding="utf-8").write(s)
a = open(f"{d}/assemble.sh", encoding="utf-8").read()
a = re.sub(r'(?m)^LEAK_X="[^"]*"', 'LEAK_X="500"', a); a = re.sub(r'(?m)^LEAK_Y="[^"]*"', 'LEAK_Y="880"', a)
open(f"{d}/assemble.sh", "w", encoding="utf-8").write(a)
EOF
  echo "format: 9:16 (1080x1920, safe zone x 70-930 y 220-1500, visual centre 500,880; references/vertical.md)"
else
  cp "$SKILL/assets/fx.html" "$DST/reference/fx.html"
fi
if grep -q '{{' "$DST/frame.md" 2>/dev/null || [ ! -s "$DST/frame.md" ]; then
  cp "$SKILL/templates/frame.md" "$DST/frame.md"
  [ "$FORMAT" = "9:16" ] && sed -i 's/^unit: 1920×1080/unit: 1080×1920 (9:16; safe zone x 70-930, y 220-1500; visual centre 500, 880)/' "$DST/frame.md"
fi
cp "$SKILL/templates/dispatch.md" "$DST/reference/dispatch-template.md"

TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
( cd "$TMP"
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
  cp package/files/caveat-latin-500-normal.woff2 "$DST/assets/fonts/Caveat-500.woff2" )
echo "kinetic kit: fx.html ($FORMAT), frame.md, gsap, $(ls "$DST/assets/fonts" | wc -l | tr -d ' ') fonts"

THEME_ARGS=(--preset "$PRESET")
if [ -n "$URL" ]; then
  if python3 "$HERE/site-intel.py" "$URL" "$DST"; then
    THEME_ARGS+=(--from-site)
  else
    echo "site-intel: site not reachable from here; fallback in references/site-intel.md (WebFetch + client screenshots)"
  fi
fi
[ -n "$ACCENT" ] && THEME_ARGS+=(--accent "$ACCENT")
if [ -n "$ACCENT" ] || [ -n "$URL" ] || [ ${#FONTS[@]} -gt 0 ]; then
  if [ -z "$ACCENT" ] && [[ ! " ${THEME_ARGS[*]} " =~ " --from-site " ]]; then THEME_ARGS+=(--accent "#F24E1E"); fi
  python3 "$HERE/theme.py" "$DST" "${THEME_ARGS[@]}" "${FONTS[@]}" || echo "theme: not applied (no accent found on the site: rerun theme.py with --accent)"
fi

if [ -n "$MUSIC" ]; then
  M="$ROOT/../soundsafari/cc0-1.0-music"
  if [ ! -d "$M/.git" ]; then
    mkdir -p "$(dirname "$M")"
    git clone -q --filter=blob:none --no-checkout https://github.com/SoundSafari/CC0-1.0-Music "$M"
  fi
  echo "music library: $M  (list: git -C $M ls-tree -r --name-only HEAD | grep -i mp3)"
fi
echo "next: brand/BRAND.md (if --url) -> SCRIPT.md; fill frame.md and STORYBOARD.md (grep -n '{{' must print nothing)"
