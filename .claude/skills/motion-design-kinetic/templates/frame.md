---
version: 2
name: "{{BRAND}}: kinetic launch frame"
description: >
  {{BRAND}} launch film ({{DURATION}} s, voice-over). Modern, fast, edited like a 2026 product launch: kinetic
  typography as the hero, hard cuts on the words and on the beat, flash frames, whip pans, punch-ins, chromatic slams,
  camera shake on impacts, 3D-tilted real interfaces with glow, film grain. Problem on a deep night ground with an ember
  glow; a pivot on black; the solution on warm paper with accent gradient light; the end card back on night.
  The look is defined by the executable kit reference/fx.html (copied verbatim by every frame).
unit: 1920×1080
principle: readable without sound · one hero per shot · cut on the word · every impact is felt (slam, shake, flash, sound)

colors:
  night: "#050507"            # problem + end card ground
  night-card: "rgba(24,22,26,.82)"
  paper: "#F6F1EA"            # solution ground, with accent gradient blobs
  ink: "#F6F1EA"              # text on night
  ink-dark: "#0C0C0F"         # text on paper
  mute: "#9A948C"             # labels, secondary
  accent: "{{ACCENT}}"        # brand color: keyword box, glow, hot text, button, waveform (default kit: #F24E1E)
  accent-hot: "{{ACCENT_HOT}}"
  accent-light: "{{ACCENT_LIGHT}}"
  accent-deep: "{{ACCENT_DEEP}}"
  chroma-r: "#FF2D55"         # chromatic split copies, only during a slam (≤ 0.3 s)
  chroma-b: "#2DE1FF"

fonts:
  Geist: { files: ["assets/fonts/Geist-Variable.woff2", "assets/fonts/Geist-Italic-Variable.woff2"], use: "kinetic type 800-900, tracking -0.045em; captions 600; UI 500" }
  Instrument Serif: { files: ["assets/fonts/InstrumentSerif-Italic.woff2", "assets/fonts/InstrumentSerif-Regular.woff2"], use: "ONE emotional word per beat in italic ({{EMOTION_WORDS}})" }
  Geist Mono: { files: ["assets/fonts/GeistMono-Variable.woff2"], use: "labels, hours, dates, UI micro-copy, uppercase tracking .14em" }
  Caveat: { files: ["assets/fonts/Caveat-500.woff2"], use: "only handwritten notes, if any" }

typography:
  kinetic-xl: { family: Geist, px: "260-420", weight: 900, tracking: "-0.045em", note: "one or two words, the sentence IS the image; slams in (FX.slam) or rises (FX.rise)" }
  kinetic-serif: { family: Instrument Serif italic, px: "180-320", note: "the emotional word, often next to or over a Geist word" }
  caption: { family: Geist, px: 46, weight: 600, note: "the voice, word by word on its cue, bottom center y 905 (band 890-980), ONE keyword in the accent box (.fx-key). Present in every shot where the kinetic type does not already say the sentence word for word." }
  clock: { family: Geist, px: "300-460", weight: 800, tabular: true, note: "numbers roll digit by digit (FX.roll), never faded" }
  label: { family: Geist Mono, px: "16-22", weight: 500, upper: true, tracking: ".14em" }

components:
  kit: "reference/fx.html — CSS block + FX helpers (slam, rise, cue, shake, flash, whipOut/whipIn, punch, key, shimmer, roll, chroma, words). Copy verbatim between the « FX : début / fin » markers."
  grounds: ".fx-night (problem, end card) · .fx-orange (impact cards) · .fx-paper (solution) · black #050507 (pivot). Always add .fx-vignette and .fx-grain on top."
  glow: ".fx-glow ember disc behind the hero, drifts slowly"
  glass-card: ".fx-card (night) / .fx-card.light (paper): radius 22, layered shadows, inside a .fx-3d stage, tilted rotateX/rotateY 6-18° and settling"
  real-ui: "{{REAL_UI}}  (real screenshots / stills of the product, swapped discretely inside a floating 3D glass frame, never redrawn)"
  logo: "{{LOGO}}"
  {{EXTRA_COMPONENTS}}

motion:
  - "Cut on the word: a new shot starts on the first word of each idea (±1 frame) or on a beat; most seams are hard cuts, sold by a 2-frame flash (FX.flash), a whip (FX.whipOut/whipIn) or a match on an object."
  - "Two speeds: gestures of 1-6 frames (expo.out) and linear drifts (2-5 %/s) that never stop. No frozen hold."
  - "Impacts are physical: slam (×1.6 + blur 18 → ×1 in 0.12 s) + chromatic split + shake (14 px, 0.32 s) + sound."
  - "Depth: 3D-tilted cards with perspective, a glow behind, grain and vignette over everything."
  - "Rhythm: hook and pain cut every 0.3-0.9 s (a silent gag every 0.25 s); the solution breathes a little more (1-1.8 s) but keeps punch-ins."

negative:
  - "No more than one hue besides night/paper/ink: everything colored is the accent family (chroma copies only during a slam)."
  - "No brand before {{BRAND_TIME}} s (the brand name spoken): the problem tool is generic."
  - "No invented numbers or features; the real UI is never redrawn."
  - "No Math.random, no repeat:-1, no CSS animation, no backdrop-filter, no letterSpacing tween, no network asset."
  - "Never more than 2 kinetic words fighting for attention; captions never overlap a kinetic word."
---

# {{BRAND}}: frame spec

{{ONE_PARAGRAPH_FILM_SUMMARY: what each act shows, in the order of the voice, naming the slams, the rhymes and the pivot}}
