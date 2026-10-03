---
name: motion-design-kinetic
description: Makes a « bluffing », modern launch / promo motion design film (15-60 s, voice-over) for ANY brand, product or client, from just a website URL and a brief — kinetic typography as the hero, hard cuts on the words, slams with chromatic split and shake, whips, punch-ins, flashes, the brand's real interfaces in 3D, grain, sound design. Reads the client's site (texts, proofs, palette, fonts, logo, screenshots, demo videos), themes the kit to the brand, writes script and storyboard, animates with one agent per shot, mixes music + SFX, renders 16:9 and/or 9:16 and exports for web, social and WhatsApp. Use for « fais un motion design pour <site/marque> », « vidéo de lancement », « promo produit », « reel / TikTok de présentation ». Not for editing filmed footage.
---

# Kinetic launch film — any brand

You are the director and the orchestrator. You run every step yourself except building the shots (one sub-agent per
frame). This skill is a LAYER on `.claude/skills/motion-design/SKILL.md` (its gates, packets, assembler, checks):
follow it with the changes below. Read `AGENTS.md` first (pinned local CLI, telemetry off, forbidden commands).
Install anything missing without asking. Never put a client's name in this skill's files: everything brand-specific
lives in the project folder.

**Bar**: every image could be a thumbnail; something happens every 0.3-0.6 s; one hero at a time; every sentence
readable without sound; nothing invented (numbers and UI come from the client). Reference film for the craft (one
example, not a template to copy): `synapze-v2/` (16:9) and `synapze-v2-vertical/` (9:16).

## References (read when the step needs them)
| file | when |
|---|---|
| `references/site-intel.md` | step 0: the website → brand dossier, and the fallback when the site is unreachable |
| `references/story.md` | step 1: story archetypes by business type, hooks, pivots, rhymes, how to turn BRAND.md into a script |
| `references/edit-grammar.md` | step 3: cut on the word, 3 text registers, effect vocabulary with numbers, worlds, signatures, block format |
| `references/vertical.md` | 9:16 (native or port of a 16:9): safe zones, layout rules, port brief |
| `references/production.md` | steps 4-7: sourcing behind a restricted network, audio, assembly, review loop, exports |
| `templates/frame.md`, `templates/dispatch.md` | the look spec to fill, the worker brief per frame |
| `assets/fx.html`, `assets/fx-9x16.html` | the executable FX kit (themable through CSS variables) |

## Pipeline

**0. Intake (5 min).** Ask in ONE grouped question only what you cannot find: the website URL, the format(s)
(16:9 site / 9:16 TikTok-Reels / both), duration (15/30/45/60 s), the call to action, language and voice, any real
material (screen recording of the product, logo SVG). Then:
```bash
bash .claude/skills/motion-design/scripts/new-project.sh <project>
bash .claude/skills/motion-design-kinetic/scripts/setup-kinetic.sh <project> --url <site> [--format 9:16] [--music]
```
`--url` runs `site-intel.py`: `brand/BRAND.md` (promise, features, verbatim proofs with source URL, testimonials,
prices, CTAs, tone, palette, fonts), `brand/palette.json`, screenshots desktop/mobile/sub-pages in `assets/ui/site/`,
logo candidates in `assets/brand/`, demo videos. Then `theme.py --from-site` themes the kit (accent family, grounds
preset, the brand's fonts or their free equivalents). Without a site: `--accent "#hex" [--preset encre|foret|mono|creme]
[--display "<Family>"]`. Site unreachable (exit 3): `references/site-intel.md` § fallback (WebFetch + client material).
Then READ `brand/BRAND.md` and LOOK at the screenshots (Read the PNGs): you must know the product before writing.

**1. Script (gate).** From BRAND.md, write `<project>/BRIEF.md` (audience, pain n°1 in their words, promise, 3 concrete
pains, 3 proofs allowed, CTA, tone) and show it in 8 lines; then follow `references/story.md`: 5-7 concepts in one line,
2 full versions (staged + ElevenLabs text), 6 parts (dated hook, silent gag, 3 pains, pivot on black, solution, brand +
CTA), 170-180 words/min. Ask the pronunciation of the brand name. Only verbatim proofs from BRAND.md, flagged to the user.

**2. Voice (gate).** The user generates it (ElevenLabs settings in motion-design `references/voice-elevenlabs.md`);
montage to the agreed length (`build-audio.sh` CUTS, negative gaps shorten silences); `mots.py` word timings.

**3. Storyboard (gate).** `frame.md` from the template (theme.py already filled the colors) and `STORYBOARD.md` with
`references/edit-grammar.md` (+ `references/vertical.md` in 9:16): MONDE, SIGNATURES, 3 RIMES, PARTITION CAMÉRA,
VOIX, COUPES (≈ 1/s in the problem), RYTHME, SON; per frame: word cues, scenes dated every 0.1-0.4 s, binding handoffs.
Map the real material: which screenshot / demo-video still / logo appears in which shot (UI is never redrawn; stills
of a demo video: `ffmpeg -i demo.mp4 -vf fps=2,scale=1440:-1 assets/ui/x/vn-%02d.jpg`). Show 3 styleframe directions
(`motion-design/scripts/render-styleframes.py`) when the client wants a choice.

**4. Animation.** Packets (`node .claude/skills/product-launch-video/scripts/frame-packets.mjs --project <p>
--storyboard <p>/STORYBOARD.md`), then ONE background Agent per frame, all in one message, prompt =
`<p>/reference/dispatch-template.md` filled (absolute paths, Frame notes with seam pixel facts and the real assets of
that frame). Keep `frame → agent id` (scratchpad `agents.txt`); corrections go to the same agent (SendMessage). In a
later session, one new agent per frame to fix, with its brief + « the file exists: change only this ».

**5. Music + SFX (gate).** Two CC0 tracks (tension until the pivot, elan whose drop lands on the light), SFX from the
storyboard SON lines into `sfx-events.json` (long textures are sliced automatically, `SFX_SLICE`),
`build-music-options.py` → 2 options at -16 LUFS. `references/production.md` § audio.

**6. Assemble, render, review.** `bash <p>/assemble.sh`, `npx hyperframes check`, `render --quality high`,
`contact-sheets.sh` read in FULL (every 0.25 s), freeze / decode / loudness / duration, seam strips. Fix through the
frame agents, re-render. Never say « fini » before the last render passed every check.

**7. Deliver.** `bash .claude/skills/motion-design-kinetic/scripts/export.sh <p>/renders/<film>.mp4` → `-web`, `-social`,
`-whatsapp` (each verified). Send the right one(s) (≤ 30 MB for upload), the music alternative, an honest list of what
the checks still flag. Commit and push (renders are git-ignored). Offer the other format (9:16 ↔ 16:9:
`references/vertical.md` § port, one agent per frame, same audio).

## Non-negotiables
- All frames share one page: IIFE-wrapped scripts, CSS scoped under `[data-composition-id]`, prefixed ids.
- No network asset (local GSAP, local fonts); no Math.random / repeat:-1 / CSS animation / onUpdate visuals.
- Colors and fonts only through the THEME variables of `reference/fx.html` (theme.py), never hard-coded per frame.
- Every word on its cue (0-2 frames early). One hero at a time. No hold over 0.6 s without motion.
- No brand before it is spoken; real UI never redrawn; no number that is not verbatim in BRAND.md and confirmed.
- Read the contact sheets yourself: cropped heroes, empty images and unreadable UI are invisible to `hyperframes check`.
