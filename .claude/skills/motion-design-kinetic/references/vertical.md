# 9:16 (TikTok, Instagram Reels, YouTube Shorts)

Native: `setup-kinetic.sh <p> --format 9:16` (1080×1920 canvas, 9:16 FX kit, meta.json, storyboard format, flash
centre). Port of an existing 16:9 film: § Port below. Same audio either way.

## Layout rules (write them into the storyboard header and every brief)
- App UI covers: top 0-220 (header), bottom 1500-1920 (username, caption, music), right 930-1080 (like/comment/share).
  Every text and every hero inside **x 70-930, y 220-1500**. Visual centre **(500, 880)**. Grounds, glows, grain,
  decorative depth may fill the canvas.
- Kinetic words: display 900, 160-260 px, one word per line, 2 lines max, stacked, centred on x 500 (`.fx-k` is
  already centred on 0-1000). Long words: split on two lines rather than shrink below ~150 px (« IMBAT / TABLE. »).
  Emotion serif 150-220 px. Clocks 230-300 px.
- Captions `.fx-cap`: band y 1270-1420, 54 px, 2 lines max (the 9:16 kit wraps); the hero sits above (y 300-1220).
  Split a long caption into two groups rather than three lines.
- Real interfaces: never the whole 16:9 screen small. Macro: the card wider than the canvas (×1.9-2.7 on the source
  still), a camera that FOLLOWS the action (pan along the typed line synced to the stills, whip-pan to the next block),
  UI text ≥ 22-26 px on screen. A blurred, scaled-up copy of the screen behind fills the vertical.
- Phone UIs (WhatsApp, apps): the phone 40-70 % of the height; enlarge the notification / bubble that matters.
- Split screens: stacked top / bottom (first on top). Sideways whips may become vertical.
- Seams with a matched object: give pixel coordinates in the 9:16 canvas (e.g. a line 300 × 4 px centred at (500, 880)).

## Port of a 16:9 film (what produced synapze-v2-vertical)
1. Copy the project without renders/snapshots/index.html; move `compositions/frames/*.html` to
   `compositions/frames-16x9/`; `meta.json` 1080×1920; `STORYBOARD.md` `format: 1080x1920` + a « FORMAT 9:16 —
   PRIORITAIRE » block (the rules above) before « Video direction »; seam coordinates rewritten; `assemble.sh`
   LEAK_X/Y = 500/880; `reference/fx.html` = `assets/fx-9x16.html` with the project's THEME block.
2. Rebuild packets, then one agent per frame with the frame's original brief + this section prepended:
   « THIS IS A PORT TO 9:16: the approved 16:9 file is compositions/frames-16x9/<id>.html — same timeline, cues,
   sounds, effects, content; RECOMPOSE every shot for 1080×1920 (never a 16:9 shrunk into a band); root
   data-width 1080 data-height 1920; copy the 9:16 kit; safe zones …; check stills every 0.25 s at 9:16 size. »
3. Assemble, render, contact sheets: look hardest at real-UI shots (too small is the typical failure) and at
   kinetic words touching the safe edges.
