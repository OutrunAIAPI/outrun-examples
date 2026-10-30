#!/usr/bin/env bash
# OpenAI Responses API (GPT models; this is the format Codex uses).
curl https://api.outrun.to/v1/responses \
  -H "Authorization: Bearer $OUTRUN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-5.6-sol", "input": "Write a haiku about rivers.", "reasoning": {"effort": "high"}}'
