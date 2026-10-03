# Production notes: sourcing, audio, assembly, review, delivery

## Sourcing that works behind a restricted network

| need | source that worked | blocked / avoided |
|---|---|---|
| fonts | `npm pack geist @fontsource/<family>` then copy `files/*-latin-*.woff2` (`scripts/setup-kinetic.sh`) | jsDelivr / fontsource CDN, Google Fonts |
| GSAP | `npm pack gsap@3.14.2` → `assets/vendor/gsap.min.js`; `assemble.sh` rewrites the root's CDN tag to it | any `<script src=https://…>` in a frame breaks the render |
| music (CC0) | `git clone --filter=blob:none --no-checkout https://github.com/SoundSafari/CC0-1.0-Music`, list with `git ls-tree -r --name-only HEAD`, extract with `git show HEAD:<path>` (only the blobs you take are downloaded) | Free Music Archive site |
| SFX | the Pixabay set of `.claude/skills/media-use/audio/assets/sfx/` (whoosh, impact-bass, click-soft, key-press, notification…) | |
| word timings | `mots.py`; if Whisper weights are blocked, sherpa-onnx + `sherpa-onnx-whisper-small` from the sherpa-onnx GitHub releases (`OfflineRecognizer.from_whisper(..., language="fr")`), then map words to phrases yourself | openai-whisper weights host |
| real UI | stills of the client's own video: `ffmpeg -i demo.mp4 -vf fps=2,scale=1440:-1 assets/ui/x/vn-%02d.jpg`; swap stills discretely in a 3D frame | redrawing the UI |
| icons | `npm pack simple-icons` | |
| WebGL shaders | none: software GPU in the container, avoid shader registry blocks | |

Python Playwright: pin `playwright==1.56.0` (matches the preinstalled Chromium); never `playwright install`.

## Audio

- Montage of the client's voice: `build-audio.sh` CUTS `"t:gap"` (negative gap = shorten a raw silence); target the
  agreed duration (here 40-45 s → 43.8 s).
- Music in two tracks (`build-music-options.py`): a TENSION track until the pivot (cut to silence with a low impact,
  riser cresting exactly on it), an ELAN track whose drop lands on the light flash (`analyze-music.py --drop-at LIGHT`
  gives `track_start`). Ducked under the voice; keep ≥ 8 dB voice / music before the pivot. Build 2 options (V2 / V2b)
  so the client chooses by ear; `--mux` swaps the soundtrack of a rendered MP4 without re-rendering.
- SFX: one event per visual impact, written in the storyboard SON lines, collected into `assets/audio/sfx-events.json`
  (`[["name", t, gain], …]`, ~80 events for 44 s): impact on every slam, whoosh on every whip, click on every tick /
  digit step, key-press on typed labels, glitch on gag cuts, two-tone notification on the rhymes.
- Loudness: measure the RENDERED MP4 (`ffmpeg -i v.mp4 -af ebur128=peak=true -f null -`). Target -16 LUFS ±1,
  true peak ≤ -1.5 dBTP. If short, apply the gap with `volume=+XdB` to the mix, re-assemble, re-render.

## Assembly patches (already folded into motion-design/templates/assemble.sh)

- Local GSAP replaces the CDN tag in `index.html`.
- Newer HyperFrames assembler registers `window.__timelines["main"]` bare: assemble.sh wraps it so the orchestrator
  layer (flash, paper bed, audio) can add tweens.
- All frames live in ONE page: IIFE per frame script, CSS scoped under `[data-composition-id="<id>"]`, ids prefixed.
  A duplicate `const FX` at top level silently kills every frame after the first.

## Review loop (do not skip: it is where the film went from good to « bluffant »)

1. `bash <project>/assemble.sh && npx hyperframes check` — 0 errors. `content_overlap` warnings on digit rollers or
   stacked cards are expected; read every contrast warning.
2. `npx hyperframes render --quality high --output renders/video.mp4` (≈ 3.5 min for 44 s on software GPU).
3. `bash .claude/skills/motion-design/scripts/contact-sheets.sh <project>/renders/video.mp4` → one image every 0.25 s.
   Read EVERY sheet. Hunt: an empty or near-empty image (fix: fill with a build-up, ghosts, a drift), a cropped hero
   (the WhatsApp phone was cut by the frame: rescale), a hold over 0.6 s, two heroes, text under 3:1, a seam that jumps.
4. Technical: `ffprobe` (video and audio = TOTAL), `ffmpeg -v error -i v.mp4 -f null -` (no output), freezedetect
   `n=0.001:d=1.0` (none outside the end card), loudness as above.
5. Each fix goes to THAT frame's agent by SendMessage (agent IDs kept in `agents.txt`), with the time, what you see,
   what you want. Then re-assemble, re-render, re-read the sheets of that span.
6. Deliver: `scripts/export.sh <render.mp4>` → `-web` (H.264 High 4.1 CRF 17), `-social` (High 4.0, CRF 18 ≤ 6 Mb/s,
   2 s GOP: TikTok / Reels / Shorts / LinkedIn), `-whatsapp` (High 4.0, ref 3, 15 MB two-pass: shown as a video when
   sent from the Gallery, not as a Document). Each printed with profile/level, size, loudness, decode check. Send the
   right file (≤ 30 MB upload), the music alternative, an honest list of what the checks still flag.

## Why a video becomes a « document » on WhatsApp (diagnosed on the reference film)
Most often the sending path (Files / Document picker instead of Gallery); then size (> ~16 MB); then H.264 level 5.0
caused by ref=5 at 1080p (HyperFrames' high render) — the `-whatsapp` export fixes the last two.
