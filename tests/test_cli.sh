#!/bin/bash

set -e

response=$(tokensniffer get-token --chain-id 1 --address "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48")

# Check if the response contains the key-value pair 'message': 'OK'
if [[ "$(jq -r '.message' <<< "$response")" != "OK" ]]; then
  echo "Response incorrect:"
  echo "$response"
  exit 1
fi
