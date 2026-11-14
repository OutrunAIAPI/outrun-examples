# Continue with Outrun

[Continue](https://github.com/continuedev/continue) connects to Outrun through its `openai`
provider with a custom `apiBase`. The config file [`config.yaml`](config.yaml) holds no secret:
the key is read from the Continue secret `OUTRUN_API_KEY`.

Full API reference: [outrun.to/docs/api](https://outrun.to/docs/api?utm_source=github&utm_medium=repo&utm_campaign=examples)

## 1. Get a key

Create a key at [outrun.to/key](https://outrun.to/key?utm_source=github&utm_medium=repo&utm_campaign=examples)
and save it in Continue as a secret named `OUTRUN_API_KEY`.

## 2. Add the models

Merge the `models` list from [`config.yaml`](config.yaml) into your Continue `config.yaml`
(open it from the Continue panel's settings). Keep the trailing `/v1/` in `apiBase`.

## 3. Pick a model

Choose `Claude Sonnet 5.5` (or another entry) in the Continue model picker and send
`Reply with OK only` to check the connection.

To add another model, copy an entry and change `name` and `model` to an ID from
[outrun.to/pricing](https://outrun.to/pricing?utm_source=github&utm_medium=repo&utm_campaign=examples),
which also lists current rates.
