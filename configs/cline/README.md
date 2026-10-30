# Cline (VS Code) with Outrun

Cline connects with its **OpenAI Compatible** provider.

Full guide: [outrun.to/docs/setup/cline](https://outrun.to/docs/setup/cline?utm_source=github&utm_medium=repo&utm_campaign=examples)

## 1. Install

```bash
code --install-extension saoudrizwan.claude-dev
```

## 2. Settings (gear icon in the Cline panel)

```text
API Provider:  OpenAI Compatible
Base URL:      https://api.outrun.to/v1
API Key:       your Outrun key (type it into this field yourself)
Model ID:      claude-sonnet-5
```

Do not append `/chat/completions` to the Base URL. Cline keeps the key in its own settings
screen, so don't write it into a VS Code settings or workspace file.

Other model IDs you can switch to: `gpt-6-astra`, `gpt-5.6-sol`, `gpt-5.6-terra`,
`gpt-6-sol`, `gpt-6.1-sol`, `claude-opus-5-5`, `claude-opus-5`, `claude-fable-5-1`,
`claude-fable-5`, `claude-sonnet-5-5`, `gemini-3.8-flash`, `gemini-3.1-pro-preview`,
`gemini-3.7-flash`, `grok-4.7`, `kimi-k3`, `kimi-k3.1-pro`, `MiniMax-M3`,
`deepseek-v4-pro`, `deepseek-v4-flash`, `deepseek-v4.1-flash`, `glm-5.3`, `glm-5.3-flash`,
and the uncensored models `glm-5.3-uncensored`, `glm-5.3-flash-uncensored`,
`glm-5.3-abliterated`, `deepseek-v4-pro-uncensored`. Full list: [CATALOG.md](../../CATALOG.md).

## 3. Test

Click Save or Done, start a new chat and send `Reply with OK only`.
