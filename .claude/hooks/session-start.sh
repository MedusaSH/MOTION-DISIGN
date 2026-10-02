#!/bin/bash
# Installs every prerequisite of the method at session start, without asking (user preference).
set -uo pipefail
cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}"

export HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1 HYPERFRAMES_SKIP_SKILLS=1 HYPERFRAMES_NO_UPDATE_CHECK=1

[ -f .env ] || cp .env.example .env

# HyperFrames, pinned to 0.8.82 by package-lock.json
[ -x node_modules/.bin/hyperframes ] || npm ci --no-audit --no-fund

# Python prerequisites: openai-whisper (transcription) and playwright
python3 -c "import whisper" 2>/dev/null || python3 -m pip install -q -U openai-whisper
if ! python3 -c "import playwright" 2>/dev/null; then
  if [ -d /opt/pw-browsers/chromium_headless_shell-1194 ]; then
    # Cloud container: match the preinstalled Chromium instead of downloading one
    python3 -m pip install -q "playwright==1.56.0"
  else
    python3 -m pip install -q playwright && python3 -m playwright install chromium
  fi
fi

npx hyperframes telemetry disable >/dev/null 2>&1
npx hyperframes browser ensure >/dev/null 2>&1
exit 0
