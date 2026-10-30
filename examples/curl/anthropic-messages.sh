#!/usr/bin/env bash
# Anthropic Messages format for Claude model IDs.
# The key goes in x-api-key, plus the anthropic-version header.
curl https://api.outrun.to/v1/messages \
  -H "x-api-key: $OUTRUN_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{"model": "claude-sonnet-5", "max_tokens": 256, "messages": [{"role": "user", "content": "Hello, Claude"}]}'

# Count tokens before sending:
curl https://api.outrun.to/v1/messages/count_tokens \
  -H "x-api-key: $OUTRUN_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{"model": "claude-sonnet-5", "messages": [{"role": "user", "content": "Hello, Claude"}]}'
