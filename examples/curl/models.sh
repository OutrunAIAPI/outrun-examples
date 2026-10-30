#!/usr/bin/env bash
# List the model IDs available to your key.
curl https://api.outrun.to/v1/models \
  -H "Authorization: Bearer $OUTRUN_API_KEY"

# Public model and price list as JSON (no key needed):
# curl https://api.outrun.to/pricing
