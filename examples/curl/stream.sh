#!/usr/bin/env bash
# Streaming: add "stream": true and read the server-sent events.
curl -N https://api.outrun.to/v1/chat/completions \
  -H "Authorization: Bearer $OUTRUN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.6-sol",
    "stream": true,
    "messages": [{"role": "user", "content": "Count to five, one number per line."}]
  }'
