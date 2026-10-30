"""Claude model IDs through the Anthropic Messages format, with the Anthropic SDK.

    pip install -r requirements.txt
    export OUTRUN_API_KEY="your-key"
    python anthropic_messages.py

The SDK adds /v1/messages itself, so base_url is the bare host (no /v1),
the same value Claude Code uses for ANTHROPIC_BASE_URL.
"""
import os

import anthropic

client = anthropic.Anthropic(
    base_url="https://api.outrun.to",
    api_key=os.environ["OUTRUN_API_KEY"],
    max_retries=0,
)

msg = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=256,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(msg.content[0].text)
