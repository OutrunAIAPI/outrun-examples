"""Call Outrun from the LiteLLM Python SDK.

    pip install litellm
    export OUTRUN_API_KEY="your-key"
    python sdk_example.py

Outrun is OpenAI-compatible, so use LiteLLM's openai/ prefix plus api_base.
The part after "openai/" is the exact Outrun model ID from CATALOG.md.
"""
import os

import litellm

resp = litellm.completion(
    model="openai/gpt-5.6-sol",
    api_base="https://api.outrun.to/v1",
    api_key=os.environ["OUTRUN_API_KEY"],
    messages=[{"role": "user", "content": "Say hello in five words."}],
    max_tokens=64,
    num_retries=0,  # requests are billed; don't retry automatically
)
print(resp.choices[0].message.content)

# Streaming works the same way:
for chunk in litellm.completion(
    model="openai/claude-sonnet-5",
    api_base="https://api.outrun.to/v1",
    api_key=os.environ["OUTRUN_API_KEY"],
    messages=[{"role": "user", "content": "Count to five."}],
    stream=True,
    num_retries=0,
):
    print(chunk.choices[0].delta.content or "", end="", flush=True)
print()
