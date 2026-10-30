"""Chat Completions with the official OpenAI Python SDK.

    pip install -r requirements.txt
    export OUTRUN_API_KEY="your-key"
    python chat.py
"""
import os

from openai import OpenAI

client = OpenAI(
    base_url="https://api.outrun.to/v1",
    api_key=os.environ["OUTRUN_API_KEY"],
    max_retries=0,  # requests are billed; check Activity before retrying by hand
)

resp = client.chat.completions.create(
    model="gpt-5.6-sol",  # any text model ID from CATALOG.md, e.g. claude-sonnet-5
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say hello in five words."},
    ],
    max_tokens=64,
)
print(resp.choices[0].message.content)
print(resp.usage)
