# Goose with Outrun

[Goose](https://github.com/aaif-goose/goose) can use Outrun as a custom provider. Outrun is an
OpenAI-compatible API, so Goose talks to it through its `openai` engine. The provider file
[`outrun.json`](outrun.json) holds no secret: the key is read from `OUTRUN_API_KEY`.

Full API reference: [outrun.to/docs/api](https://outrun.to/docs/api)

## 1. Get a key

Create a key at [outrun.to/key](https://outrun.to/key) and export it:

```bash
export OUTRUN_API_KEY="your-key"
```

On Windows PowerShell: `$env:OUTRUN_API_KEY = "your-key"`.

## 2. Install the provider file

Copy `outrun.json` into Goose's `custom_providers` directory:

| OS | Directory |
|---|---|
| macOS / Linux | `~/.config/goose/custom_providers/` |
| Windows | `%APPDATA%\Block\goose\config\custom_providers\` |

```bash
mkdir -p ~/.config/goose/custom_providers
curl -fsSL https://raw.githubusercontent.com/OutrunAIAPI/outrun-examples/main/configs/goose/outrun.json \
  -o ~/.config/goose/custom_providers/outrun.json
```

Restart Goose Desktop if it is open. This is Goose's documented
[custom provider](https://goose-docs.ai/docs/getting-started/providers#configure-custom-provider)
file format.

## 3. Use it

- **Desktop:** open Settings, then Models, and pick `Outrun` from the provider list. If Goose asks
  for the key, paste it there to store it in the keychain.
- **CLI:** run `goose configure`, choose `Configure Providers`, and select `Outrun`. Or start a
  session directly:

  ```bash
  goose session start --provider outrun
  ```

Pick any listed model, for example `claude-sonnet-5-5` or `gpt-5.6-sol`. The file lists a few
model IDs with their context sizes. To use another model, add an entry to `models` using the ID from
[outrun.to/pricing](https://outrun.to/pricing), which also lists current rates.

## 4. Test

Send `Reply with OK only` and check that the model answers.
