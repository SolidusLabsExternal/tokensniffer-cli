#!/bin/bash

# Example shell script

set -e

echo "\nGetting request limit..."
tokensniffer --api-key "$TOKENSNIFFER_API_KEY" request-limit

echo "\nGetting token info..."
tokensniffer --api-key "$TOKENSNIFFER_API_KEY" token-info 1 "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"

echo "\nGetting scam tokens in the last 24 hours..."
tokensniffer --api-key "$TOKENSNIFFER_API_KEY" scam-tokens-last-24-hours

echo "\nGetting scam tokens for an address..."
tokensniffer --api-key "$TOKENSNIFFER_API_KEY" scam-tokens-for-address "0x0000000000000000000000000000000000000000"
