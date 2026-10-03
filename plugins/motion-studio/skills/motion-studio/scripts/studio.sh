#!/bin/bash
# Finds or installs the Motion Studio workspace (the MOTION-DISIGN repository: HyperFrames pinned, audited skills,
# FX kits, SFX, scripts), makes it ready, and prints its path on the last line: STUDIO=<path>
#
# Order: $MOTION_STUDIO_DIR, the current folder (or a parent) if it is the studio, ~/motion-studio, then a fresh
# clone of $MOTION_STUDIO_REPO (default https://github.com/MedusaSH/MOTION-DISIGN) into ~/motion-studio.
# Films are always built inside the studio (its scripts reach the skills through ../.claude/skills/).
set -uo pipefail
REPO="${MOTION_STUDIO_REPO:-https://github.com/MedusaSH/MOTION-DISIGN}"
REF="${MOTION_STUDIO_REF:-}"
is_studio() { [ -f "$1/.claude/skills/motion-design-kinetic/SKILL.md" ] && [ -f "$1/package.json" ]; }

STUDIO=""
if [ -n "${MOTION_STUDIO_DIR:-}" ] && is_studio "$MOTION_STUDIO_DIR"; then STUDIO="$MOTION_STUDIO_DIR"; fi
if [ -z "$STUDIO" ]; then
  d="$PWD"
  while [ "$d" != "/" ]; do is_studio "$d" && { STUDIO="$d"; break; }; d="$(dirname "$d")"; done
fi
if [ -z "$STUDIO" ]; then
  for c in "$HOME/motion-studio" "$HOME/MOTION-DISIGN" /home/user/MOTION-DISIGN; do is_studio "$c" && { STUDIO="$c"; break; }; done
fi
if [ -z "$STUDIO" ]; then
  STUDIO="${MOTION_STUDIO_DIR:-$HOME/motion-studio}"
  echo "motion-studio: cloning $REPO into $STUDIO" >&2
  if ! git clone -q --depth 50 ${REF:+--branch "$REF"} "$REPO" "$STUDIO"; then
    echo "motion-studio: clone failed. Private repository? Log in to GitHub (gh auth login && gh auth setup-git), or in a" >&2
    echo "claude.ai/code session add the MOTION-DISIGN repository to the session, or set MOTION_STUDIO_DIR to an existing copy." >&2
    exit 2
  fi
fi

cd "$STUDIO" || exit 2
# keep the studio current when it is clean (never touch local work)
if git rev-parse --is-inside-work-tree >/dev/null 2>&1 && [ -z "$(git status --porcelain 2>/dev/null)" ]; then
  git pull -q --ff-only 2>/dev/null || true
fi
export HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1 HYPERFRAMES_SKIP_SKILLS=1 HYPERFRAMES_NO_UPDATE_CHECK=1
[ -f .env ] || { [ -f .env.example ] && cp .env.example .env || : > .env; }
if [ -x .claude/hooks/session-start.sh ] || [ -f .claude/hooks/session-start.sh ]; then
  CLAUDE_PROJECT_DIR="$STUDIO" bash .claude/hooks/session-start.sh >/dev/null 2>&1
else
  [ -x node_modules/.bin/hyperframes ] || npm ci --no-audit --no-fund >/dev/null 2>&1
fi
command -v ffmpeg >/dev/null || echo "motion-studio: ffmpeg missing (install it: brew install ffmpeg / apt-get install -y ffmpeg)" >&2
[ -x node_modules/.bin/hyperframes ] || echo "motion-studio: npm ci failed (Node 20+ required)" >&2
python3 -c "import playwright" 2>/dev/null || echo "motion-studio: python playwright missing (pip install playwright && python3 -m playwright install chromium)" >&2
echo "STUDIO=$STUDIO"
