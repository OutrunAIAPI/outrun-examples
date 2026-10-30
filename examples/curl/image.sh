#!/usr/bin/env bash
# Image generation. Each request is billed, so it is sent once (no retry loop).
# Gemini image models return one image per request (n = 1).
# gpt-image-2 and grok-imagine-image use the same request shape.
curl https://api.outrun.to/v1/images/generations \
  -H "Authorization: Bearer $OUTRUN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gemini-3-pro-image", "prompt": "A lighthouse at dawn, oil painting", "size": "16:9"}' \
  -o image-response.json

# Response: {"created": ..., "data": [{"b64_json": "<base64 PNG>"}], "usage": {...}}
# Decode it to image.png (needs python3):
python3 -c "import json,base64; d=json.load(open('image-response.json')); open('image.png','wb').write(base64.b64decode(d['data'][0]['b64_json']))" \
  && echo "Saved image.png"
