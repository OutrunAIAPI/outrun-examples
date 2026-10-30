#!/usr/bin/env bash
# Chat Completions with curl. Set your key first: export OUTRUN_API_KEY="your-key"
curl https://api.outrun.to/v1/chat/completions \
  -H "Authorization: Bearer $OUTRUN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.6-sol",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Say hello in five words."}
    ],
    "max_tokens": 64
  }'
