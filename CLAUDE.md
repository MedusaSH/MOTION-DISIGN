# Instructions

Read and follow `AGENTS.md` (guardrails of this workspace).

## User preference

Always install everything the method needs without asking first: npm dependencies (`npm ci`), the empty `.env`,
`npx hyperframes browser ensure`, ffmpeg, Python packages (`openai-whisper`, `playwright`) and any other missing
prerequisite, even large downloads. `.claude/hooks/session-start.sh` does this automatically at session start.
This does not lift the guardrails of `AGENTS.md`: still no telemetry, feedback, publish, cloud, upgrade or
`skills update` unless explicitly asked.
