# OpenCode with Outrun

OpenCode connects through the `@ai-sdk/openai-compatible` provider. The config sets up
every Outrun text model (Claude, GPT, Gemini, Grok, DeepSeek, Kimi, MiniMax, GLM and the
uncensored models) on one key. The default is `outrun/claude-opus-5-5`; pick another with
`/models`.

Full guide: [outrun.to/docs/setup/opencode](https://outrun.to/docs/setup/opencode?utm_source=github&utm_medium=repo&utm_campaign=examples)

## 1. Install

```bash
npm install -g opencode-ai
```

## 2. Key

```bash
echo 'export OUTRUN_API_KEY="your-key"' >> ~/.zshrc   # or ~/.bashrc
```

## 3. Config

Copy [`opencode.json`](opencode.json) to `~/.config/opencode/opencode.json`
(Windows: `%USERPROFILE%\.config\opencode\opencode.json`). It reads the key from
`{env:OUTRUN_API_KEY}`, so the file itself holds no secret.

## 4. Test

Run `opencode`, choose an `outrun/...` model with `/models`, and send `Reply with OK only`.
