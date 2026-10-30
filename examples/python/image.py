"""Generate one image and save it as image.png.

Each image request is billed, so the client never retries on its own.
Gemini image models return one image per request (n = 1).
"""
import base64
import os

from openai import OpenAI

client = OpenAI(
    base_url="https://api.outrun.to/v1",
    api_key=os.environ["OUTRUN_API_KEY"],
    max_retries=0,
)

result = client.images.generate(
    model="gemini-3-pro-image",  # or gemini-3.1-flash-image, gpt-image-2, grok-imagine-image
    prompt="A lighthouse at dawn, oil painting",
    size="16:9",
)
with open("image.png", "wb") as f:
    f.write(base64.b64decode(result.data[0].b64_json))
print("Saved image.png")
