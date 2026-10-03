---
name: motion-design-kinetic
description: Makes a « bluffing », modern launch motion design (30-60 s, voice-over) in the kinetic style of the Synapze v2 film — kinetic typography as the hero, hard cuts on the words, slams with chromatic split and shake, whips, punch-ins, flashes, 3D glass interfaces, grain — on top of the motion-design skill (its 5 gated steps, packets, assembler, checks). Use when the user asks for a launch / promo / product film « comme Synapze v2 », « moderne », « dynamique », « qui en met plein la vue », or for a new client film with this method. Not for editing filmed footage.
---

# Kinetic launch film (the Synapze v2 method)

You are the orchestrator. This skill is a LAYER on `.claude/skills/motion-design/SKILL.md`: follow that skill's steps,
gates, commands and house rules, with the changes below. Read `AGENTS.md` first (pinned local CLI, telemetry off,
forbidden commands). Install anything missing without asking (CLAUDE.md preference).

**Reference film**: `synapze-v2/` (43.8 s, 11 frames). Imitate its `frame.md`, `STORYBOARD.md`, `reference/fx.html`,
`compositions/frames/*.html`, `build-music-options.py`, `assemble.sh`. Its v1 (`synapze-lancement/`) is the
counter-example: calm, linear, judged « pas assez moderne ».

**References of this skill**
- `references/edit-grammar.md` — the rules that made it bluffing: cut on the word, 3 text registers, effect
  vocabulary with numbers, acts and worlds, signatures and rhymes, storyboard block format. READ BEFORE STEP 3.
- `references/production.md` — sourcing behind a restricted network, audio (two-track music, SFX, loudness),
  assembly patches, the review loop.
- `templates/frame.md` — the kinetic look spec to fill. `templates/dispatch.md` — the worker brief per frame.
- `assets/fx.html` — the executable FX kit (slam, chroma, shake, flash, whip, punch, roll, key box, shimmer, grain…).

## Pipeline

0. **Brief + project.** One grouped question for what is missing (the client's pain and promise, where the film is
   seen, CTA + URL, real UI material: screenshots or a demo video, logo, brand color). Then:
   ```bash
   bash .claude/skills/motion-design/scripts/new-project.sh <project>
   bash .claude/skills/motion-design-kinetic/scripts/setup-kinetic.sh <project> --music
   ```
   Brand color ≠ #F24E1E: replace the accent family in `<project>/reference/fx.html` (`#f24e1e`, `#ff6a2b`,
   `#b8270a`, `#ffb08a`, `#ffd9c2`, `#ffc7a8`, `rgba(242,78,30,…)`) and in `assemble.sh` (ACCENT*), once, before any frame.
1. **Script (gate)** — as motion-design step 1. Six parts: dated concrete hook, silent gag 2-3 s, 3 concrete pains,
   pivot on black, solution + benefits, brand + CTA. Ask the pronunciation of the brand; write it phonetically in the
   ElevenLabs version.
2. **Voice (gate)** — the client's ElevenLabs take; montage to the agreed length (`build-audio.sh` CUTS, negative gaps
   shorten silences); `mots.py` word timings.
3. **Storyboard (gate)** — write `frame.md` from the template and `STORYBOARD.md` with `references/edit-grammar.md`:
   header blocks (MONDE, SIGNATURES with every firing time, 3 rhymes, PARTITION CAMÉRA, VOIX silences, COUPES ≈ 1 per
   second in the problem, RYTHME, SON), then per frame: word cues, Scenes dated every 0.1-0.4 s with TEXTE ÉCRAN /
   ÉTAPES / PISTE CAMÉRA / SON / IMAGE CLÉ, binding handoffs. Optional: 3 styleframe directions as stills
   (`render-styleframes.py`) for the client to choose from before animating.
4. **Animation** — packets (`node .claude/skills/product-launch-video/scripts/frame-packets.mjs --project <p>
   --storyboard <p>/STORYBOARD.md`), then ONE background Agent per frame, all in one message, prompt =
   `templates/dispatch.md` filled (absolute paths, Frame notes with seam pixel facts). Save `frame → agent id` in the
   scratchpad (`agents.txt`). Corrections always go to the same agent by SendMessage. In a later session (agents
  gone), launch ONE new agent for that frame with its filled brief + « the file already exists: change only this ».
  Real briefs of the reference film: `synapze-v2/dispatch/*.txt`.
5. **Music + SFX (gate)** — two CC0 tracks (tension until the pivot, elan whose drop lands on the light), ~80 SFX events
   from the storyboard SON lines, `build-music-options.py` → 2 options; mix at -16 LUFS.
6. **Assemble, render, review** — the loop of `references/production.md` (check, render high, contact sheets every
   0.25 s read in full, freeze / decode / loudness / duration, fixes through the frame agents, re-render). Never
   announce « fini » before the last render passed every check.
7. **Deliver** — the MP4 (re-encode `-crf 20` copy if over 30 MiB for upload), the music alternative, an honest
   list of what checks still flag, then commit and push (renders are git-ignored).

## Non-negotiables that cost the most when forgotten
- All frames share one page: IIFE-wrapped scripts, CSS scoped under `[data-composition-id]`, prefixed ids.
- No network asset anywhere (local GSAP, local fonts); no Math.random / repeat:-1 / CSS animation / onUpdate visuals.
- Every word on its cue (0-2 frames early). One hero at a time. No hold over 0.6 s without motion.
- No brand before it is spoken; the real UI is never redrawn; no invented numbers.
- Read the contact sheets yourself: the two fixes that made the final cut (a cropped phone, a 0.6 s empty gap before
  the payoff) were invisible in `hyperframes check`.
