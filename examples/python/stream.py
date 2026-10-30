"""Streaming Chat Completions with the OpenAI Python SDK."""
import os

from openai import OpenAI

client = OpenAI(
    base_url="https://api.outrun.to/v1",
    api_key=os.environ["OUTRUN_API_KEY"],
    max_retries=0,
)

stream = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[{"role": "user", "content": "Count to five, one number per line."}],
    stream=True,
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()
