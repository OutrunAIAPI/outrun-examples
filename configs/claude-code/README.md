# Claude Code with Outrun

Claude Code speaks the Anthropic Messages API, so it points at the bare host
`https://api.outrun.to` (no `/v1`). Every Claude model works: `claude-opus-5-5`
(default), `claude-opus-5`, `claude-sonnet-5-5`, `claude-sonnet-5`, `claude-fable-5-1`
and `claude-fable-5`. Each also has a lower-cost route 2: add `-2` to the ID
(for example `claude-opus-5-5-2`).

Full guide: [outrun.to/docs/setup/claude](https://outrun.to/docs/setup/claude?utm_source=github&utm_medium=repo&utm_campaign=examples)

## 1. Install

```bash
npm install -g @anthropic-ai/claude-code
```

## 2. Settings file

Merge [`settings.json`](settings.json) into `~/.claude/settings.json`
(Windows: `%USERPROFILE%\.claude\settings.json`). Keep your other settings, and remove
any `ANTHROPIC_API_KEY` entry. Replace `KEY` with your Outrun key on your own machine.

## 3. Or use environment variables (macOS / Linux)

```bash
# Add to ~/.zshrc and/or ~/.bashrc. The base URL is the bare host: no /v1 at the end.
export ANTHROPIC_BASE_URL="https://api.outrun.to"
export ANTHROPIC_AUTH_TOKEN="$OUTRUN_API_KEY"
export ANTHROPIC_MODEL="claude-opus-5-5"
export ANTHROPIC_DEFAULT_OPUS_MODEL="claude-opus-5-5"
export ANTHROPIC_DEFAULT_SONNET_MODEL="claude-sonnet-5-5"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="claude-haiku-5-5"
# Remove any older ANTHROPIC_API_KEY line: having both causes an auth conflict.
```

## 4. Test

Open a new terminal and run `claude`. If you are signed in with an Anthropic account,
run `/logout` first and accept the custom API key if asked. Send `Reply with OK only`.
Switch models with `/model <model>`.
