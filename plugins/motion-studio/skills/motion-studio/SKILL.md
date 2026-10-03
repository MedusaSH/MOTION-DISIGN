---
name: motion-studio
description: Makes an agency-grade, « bluffing » launch / promo motion design film for ANY brand from a website URL — kinetic typography, hard cuts on the words, impacts, the brand's real interfaces in 3D, music and sound design — in 16:9 and/or 9:16 (TikTok, Reels), verified and exported for web, social networks and WhatsApp. Works from any folder or session: it installs and uses the Motion Studio workspace. Use for « fais un motion design / une vidéo de lancement / une promo / un reel pour <site ou marque> ». Not for editing filmed footage.
---

# Motion Studio (entry point, any session)

1. **Studio.** Run, and read the last line:
   ```bash
   bash "${CLAUDE_PLUGIN_ROOT}/skills/motion-studio/scripts/studio.sh"
   ```
   (if `CLAUDE_PLUGIN_ROOT` is empty: `bash "$(dirname "$(find ~/.claude -path '*motion-studio/scripts/studio.sh' 2>/dev/null | head -1)")/studio.sh"`).
   It prints `STUDIO=<path>`: the Motion Studio workspace (HyperFrames pinned, audited skills, FX kits, SFX, scripts),
   cloned and installed if needed. On exit 2 relay its message (GitHub login, or attach the repository to the
   claude.ai session) and stop.
2. **Rules.** Read `<STUDIO>/AGENTS.md` (guardrails: pinned local CLI, telemetry off, no publish/cloud/feedback
   commands) and `<STUDIO>/.claude/skills/motion-design-kinetic/SKILL.md`, then follow that skill end to end. Every
   relative path it gives is relative to `<STUDIO>`; run its commands from `<STUDIO>` (`cd <STUDIO> && …`). The skill
   in turn layers on `<STUDIO>/.claude/skills/motion-design/SKILL.md`: read it when it says so.
3. **Where things go.** The film project lives in `<STUDIO>/<project>/`. If the session started in another folder
   (the user's own repository), copy the deliverables there at the end: `./motion/<project>/` with the exported MP4s,
   `SCRIPT.md`, `STORYBOARD.md` and `brand/BRAND.md`, and tell the user both locations. Commit / push only where the
   user asks.
4. **Install everything without asking** (npm ci, ffmpeg, Python packages, browser): the studio's preference. Never
   run telemetry, feedback, publish, cloud, upgrade or skills-update commands unless the user explicitly asks.
