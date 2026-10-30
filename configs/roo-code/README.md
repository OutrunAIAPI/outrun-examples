# Roo Code (VS Code) with Outrun

Roo Code connects with its **OpenAI Compatible** provider. Outrun's guide uses it for the
uncensored and abliterated models; GLM Abliterated and GLM Flash Abliterated were verified
with Roo Code native tool calls. Each model page shows whether it is Roo Code ready and
lists its own setup values.

Full guide: [outrun.to/docs/setup/uncensored](https://outrun.to/docs/setup/uncensored?utm_source=github&utm_medium=repo&utm_campaign=examples)

## Settings

```text
API Provider:        OpenAI Compatible
Base URL:            https://api.outrun.to/v1
API Key:             enter your key locally
Model ID:            glm-5.3-abliterated

# GLM Abliterated / Flash Abliterated model capabilities
Context Window:      1000000
Max Output Tokens:   65536

# Separate request limit, if shown
Include Max Tokens:  on
Request Max Tokens:  1024 for a first test
Streaming:           on
Tool Protocol:       Native
Image Support:       off
Computer Use:        off
```

The capability values above apply to GLM only. For other models, use the limits on that
model's page, and never use the context size as the output-token limit.

Other uncensored model IDs (one Roo profile each): `glm-5.3-uncensored`,
`glm-5.3-flash-uncensored`, `deepseek-v4-pro-uncensored`, `deepseek-v4.1-flash-abliterated`,
`deepseek-v4.1-flash-abliterated-fast`. Abliterated variants are designed to reduce
refusals; responses can still vary. Full list: [CATALOG.md](../../CATALOG.md).

## Test

Save and select the profile, then send `Reply with OK only`.
