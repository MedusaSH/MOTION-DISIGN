---
version: 2
name: "Synapze v2 vertical: launch frame 9:16"
description: >
  Version 2 of the Synapze launch film (43.8 s, same voice as v1). Modern, fast, edited like a 2026 product launch:
  kinetic typography as the hero, hard cuts on the words and on the beat, flash frames, whip pans, punch-ins, chromatic
  slams, camera shake on impacts, 3D-tilted real interfaces with glow, film grain. Problem on a deep night ground with an
  ember glow; a pivot on black; the solution on warm paper with orange gradient light; the end card back on night.
  The look is defined by the executable kit reference/fx.html (copied verbatim by every frame).
unit: 1080×1920 (9:16 vertical, TikTok / Instagram Reels; safe zone x 70-930, y 220-1500; visual center 500, 880)
principle: readable without sound · one hero per shot · cut on the word · every impact is felt (slam, shake, flash, sound)

colors:
  night: "#050507"            # problem + end card ground (radial to #1a1210 near the glow)
  night-card: "rgba(24,22,26,.82)"
  paper: "#F6F1EA"            # solution ground, with orange gradient blobs #FFD9C2 / #FFC7A8
  ink: "#F6F1EA"              # text on night
  ink-dark: "#0C0C0F"         # text on paper
  mute: "#9A948C"             # labels, secondary
  accent: "#F24E1E"           # Synapze orange: keyword box, glow, hot text, button, waveform
  accent-hot: "#FF6A2B"
  accent-light: "#FFB08A"
  accent-deep: "#B8270A"
  chroma-r: "#FF2D55"         # chromatic split copies, only during a slam (≤ 0.3 s)
  chroma-b: "#2DE1FF"

fonts:
  Geist: { files: ["assets/fonts/Geist-Variable.woff2 (100-900)", "assets/fonts/Geist-Italic-Variable.woff2 (100-900 italic)"], use: "kinetic type 800-900, tracking -0.045em; captions 600; UI 500" }
  Instrument Serif: { files: ["assets/fonts/InstrumentSerif-Italic.woff2", "assets/fonts/InstrumentSerif-Regular.woff2"], use: "ONE emotional word per beat in italic (conseil, lundi, d'écrire ?, parlez, imbattable, le reste.)" }
  Geist Mono: { files: ["assets/fonts/GeistMono-Variable.woff2"], use: "labels, hours, dates, UI micro-copy, uppercase tracking .14em" }
  Caveat: { files: ["assets/fonts/Caveat-500.woff2"], use: "only the broker's handwritten notes" }

typography:
  kinetic-xl: { family: Geist, px: "170-260 (one word per line, stack vertically)", weight: 900, tracking: "-0.045em", note: "one or two words, the sentence IS the image; slams in (FX.slam) or rises (FX.rise)" }
  kinetic-serif: { family: Instrument Serif italic, px: "150-220", note: "the emotional word, often next to or over a Geist word" }
  caption: { family: Geist, px: 54, weight: 600, note: "the voice, word by word on its cue, band y 1270-1420, x 70-930, 54 px, 2 lines max, ONE keyword in the orange box (.fx-key). Present in every shot where the kinetic type does not already say the sentence word for word." }
  clock: { family: Geist, px: "230-300", weight: 800, tabular: true, note: "hours roll digit by digit (FX.roll), never faded" }
  label: { family: Geist Mono, px: "16-22", weight: 500, upper: true, tracking: ".14em" }

components:
  kit: "reference/fx.html — CSS block + FX helpers (slam, rise, cue, shake, flash, whipOut/whipIn, punch, key, shimmer, roll, chroma, words). Copy verbatim between the « FX : début / fin » markers."
  grounds: ".fx-night (problem, end card) · .fx-orange (impact cards) · .fx-paper (solution) · black #050507 (pivot). Always add .fx-vignette and .fx-grain on top."
  glow: ".fx-glow ember disc behind the hero, drifts slowly"
  glass-card: ".fx-card (night) / .fx-card.light (paper): radius 22, layered shadows, inside a .fx-3d stage, tilted rotateX/rotateY 6-18° and settling"
  real-ui: "The REAL Synapze screen: assets/ui/voice-note/vn-01.jpg … vn-22.jpg (1440×810 stills of the site video, every 0.5 s) — swapped discretely, inside a floating 3D glass frame with orange glow, never redrawn"
  whatsapp-ios: "copy of WhatsApp iOS, no logo (see ../synapze-lancement/styleframes/sf.css .wa2 and C3.html): header « Camille R. · en ligne », beige doodle ground, white / #D9FDD3 bubbles, blue ticks"
  iphone: "black bezel 14 px, radius 62, lock screen gradient #1B2840 → #0B111D, glass notification « WhatsApp · Camille R. »"
  advice-form: "« Fiche de conseil · Santé Individuel » white document, 5 check rows (Besoins exprimés, Situation familiale, Budget, Garanties proposées, Justification du conseil); problem: ticked by a mouse arrow; solution: ticks itself with « IA » chips + completeness ring, stamp « PISTE D'AUDIT · HORODATÉE »"
  waveform: "orange bars 8 px / gap 8, rounded, heights from the real voice (assets/audio/voix-montage.wav)"
  cursor: "white macOS arrow with dark outline; one curved move, direct click, ripple"
  logo: "« Synapze » in Geist 800, the two orange dots of the site « • Synapze • »"

motion:
  - "Cut on the word: a new shot starts on the first word of each idea (±1 frame) or on a beat; most seams are hard cuts, sold by a 2-frame flash (FX.flash), a whip (FX.whipOut/whipIn) or a match on an object."
  - "Two speeds: gestures of 1-6 frames (expo.out) and linear drifts (2-5 %/s) that never stop. No frozen hold."
  - "Impacts are physical: slam (×1.6 + blur 18 → ×1 in 0.12 s) + chromatic split + shake (14 px, 0.32 s) + sound."
  - "Depth: 3D-tilted cards with perspective, a glow behind, grain and vignette over everything."
  - "Rhythm: hook and pain cut every 0.3-0.9 s (the silent gag every 0.25 s); the solution breathes a little more (1-1.8 s) but keeps punch-ins."

negative:
  - "No more than one hue besides night/paper/ink: everything colored is the Synapze orange family (chroma copies only during a slam)."
  - "No Synapze brand before 22.31 s (« Synapze » spoken): the problem CRM is a generic « MON CRM »."
  - "No invented numbers or features; the real UI is never redrawn."
  - "No Math.random, no repeat:-1, no CSS animation, no backdrop-filter, no letterSpacing tween, no network asset."
  - "Never more than 2 kinetic words fighting for attention; captions never overlap a kinetic word."
---

# Synapze v2: frame spec

v1 was a calm travelling along a time line; v2 is edited. The voice stays the clock, but the picture cuts on its
words: « MARDI » slams, « 19:00 » rolls, a calendar card is swiped out on « partir », the silent gag is a time-lapse of
hard cuts (20:12 / caret / 21:30 / coffee / 22:15 / caret / 22:47), « SAISIE » gets crossed out on orange, forms
multiply into a wall, each « case » is a macro cut with a shake, the weekend scrolls as giant days behind a glowing
phone. The pivot is silence on black in serif italic; the caret becomes a bar of light. The solution is warm paper and
orange light: a full-width waveform, the real Synapze screen floating in 3D with punch-ins on what fills itself, a
cascade of ticks and a stamp, WhatsApp answering day and night (split screen), « IMBATTABLE » in hot gradient, then the
logo, the promise and the click.
