# Codex CLI with Outrun

Codex talks to Outrun through a custom model provider over the OpenAI Responses API.
GPT models: `gpt-6.1-sol` (default), `gpt-6-sol`, `gpt-6-astra`, `gpt-5.6-sol` and
`gpt-5.6-terra`.

Full guide: [outrun.to/docs/setup/codex](https://outrun.to/docs/setup/codex?utm_source=github&utm_medium=repo&utm_campaign=examples)

## 1. Install

```bash
npm install -g @openai/codex
```

## 2. Key

```bash
echo 'export OUTRUN_API_KEY="your-key"' >> ~/.zshrc   # or ~/.bashrc
```

Windows (PowerShell): `[Environment]::SetEnvironmentVariable("OUTRUN_API_KEY", "your-key", "User")`,
then reopen PowerShell.

## 3. Config

Copy [`config.toml`](config.toml) into `~/.codex/config.toml`
(Windows: `%USERPROFILE%\.codex\config.toml`). The base URL ends in `/v1`; do not append
`/responses`.

## 4. Test

Run `codex` and send `Reply with OK only`. Switch models with `codex -p gpt-6-astra`
(or `codex -m gpt-6-astra`).
