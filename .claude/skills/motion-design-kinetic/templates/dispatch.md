# Worker brief (one per frame)

Fill the `{{...}}`, save one file per frame in the scratchpad, then launch ONE background Agent per frame with the text
between the two rules as its prompt (all frames in a single message so they run in parallel). Keep the agent IDs: every
correction later goes to the same agent with SendMessage (it keeps its context), never a new agent.

Per-frame lines to write yourself (the « Frame notes » block): the handoff in / out pixel facts that the neighbours
need (positions, sizes, colors of the seam object), the real assets this frame uses, numbers to bake (waveform heights,
digit sequences), and the one thing that must hit hardest.

---

You build ONE frame of a HyperFrames motion design (a launch film). You do not see my conversation: these files are your whole world.

Read first, in this order, and follow them as your role:
1. {{PROJECT_DIR}}/.hyperframes/frame-packets/_role.md (worker contract)
2. {{PROJECT_DIR}}/.hyperframes/frame-packets/{{FRAME_ID}}.md (your storyboard block, blueprint and motion rules)
3. {{PROJECT_DIR}}/frame.md (the look: colors, fonts, components, motion) and {{PROJECT_DIR}}/reference/fx.html (the executable FX kit)

## Dispatch context
- PROJECT_DIR: {{PROJECT_DIR}}
- frame_id: {{FRAME_ID}}
- output: {{PROJECT_DIR}}/compositions/frames/{{FRAME_ID}}.html (the only file you write)
- canvas: 1920x1080, 30 fps; frame duration: {{DURATION}} s; world: {{WORLD}}
- captions: disabled (the voice is shown by your own kinetic type and .fx-cap captions, as the Scene lines say)
- GSAP: load it ONLY with <script src="assets/vendor/gsap.min.js"></script> inside your <template>. Any CDN URL breaks the render.
- Shared look: copy the CSS block and the JS kit of {{PROJECT_DIR}}/reference/fx.html verbatim, between the « FX : début / fin » markers (only `../assets/` becomes `assets/`). ALL frames end up in ONE page: wrap your whole script in an IIFE `(() => { ... })();` (never a top-level const FX / const tl), scope every CSS selector under `[data-composition-id="{{FRAME_ID}}"]`, prefix every id with `f{{NN}}-`. Use the helpers (FX.slam, FX.rise, FX.cue, FX.shake, FX.flash, FX.whipOut/whipIn, FX.punch, FX.key, FX.shimmer, FX.roll, FX.chroma, FX.words). Always put .fx-vignette and .fx-grain on top.
- THE BAR: be bold and premium (think a 2026 Linear / Vercel / Arc launch film): something happens every 0.3–0.6 s, hard cuts on the words, impacts you can feel (slam + chromatic split + shake + flash), 3D depth, glow and grain — while every sentence stays readable and only one hero holds the eye at a time. Follow the Scene lines precisely for timing and content; you are free (and expected) to add craft within them: micro-drifts, parallax layers, light streaks, motion trails, ghost copies, subtle glows.
- Check your work before you answer: render stills of your file at its key-image times, around its cuts and at every 0.25 s with a local headless Chromium (Playwright is installed; load the frame through a tiny harness page, seek your own paused timeline with `window.__timelines["{{FRAME_ID}}"].seek(t); 0`), look at them, and fix what is not premium: an empty or cropped image, a hero that is not where the eye goes, text under 3:1 contrast, a hold longer than 0.6 s with nothing moving. Report: key images checked, cuts, deviations.

## Frame notes
{{FRAME_NOTES}}

## House rules (they override the contract where they differ)
- Word cues are frame-local seconds: each word appears on its cue (0 to 2 frames early), never late. Visible copy = exactly what the Scene lines quote, correct typography of the language ({{TYPO_RULES}}).
- BLOCKING. A frame is not masked before its start: every element not on screen at t=0 starts with `opacity: 0` in CSS, and every `fromTo` that starts after t=0 has `immediateRender: false`.
- BLOCKING. handoff_in and handoff_out are binding: your first image is exactly handoff_in, your last image is exactly handoff_out.
- BLOCKING. An inner `<template id="...">` goes INSIDE the root element (`<div id="root">`), never beside it.
- BLOCKING. Never set `style.visibility = "visible"`: use `"inherit"`.
- BLOCKING. Tween transforms, opacity, filter and CSS variables only: never top, left, width, height or letterSpacing. No backdrop-filter. No interpolated clip-path polygon (circle, ellipse, inset are fine). Every id starts with a letter and carries this frame's prefix. No blurred object over 1800 px wide.
- No `repeat: -1`, no CSS animation, no Math.random (use FX.rnd), no `<audio>`, no network asset, no onUpdate callback for visuals (it does not fire on seek). Fonts and images from `assets/...` only.
- Write a complete first version of your file early (every scene roughed in, timeline registered), then refine it.
- Do not run any `npx hyperframes` command, do not edit any other project file. Writing your file is your last action.

---
