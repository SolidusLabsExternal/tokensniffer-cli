import os
from typing import Optional

import requests

BASE_URL = "https://tokensniffer.com/api/v2"


class TokenSnifferAPI:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("TOKENSNIFFER_API_KEY")

    def get_usage(self):
        url = f"{BASE_URL}/usage"
        params = {"apikey": self.api_key}
        response = requests.get(url, params=params)
        return response.json()

    def get_token(self, chain_id, address):
        url = f"{BASE_URL}/tokens/{chain_id}/{address}"
        params = {"apikey": self.api_key}
        response = requests.get(url, params=params)
        return response.json()

    def list_scam_tokens(self):
        url = f"{BASE_URL}/tokens/scams"
        params = {"apikey": self.api_key}
        response = requests.get(url, params=params)
        return response.json()

    def get_address(self, address):
        url = f"{BASE_URL}/addresses/{address}"
        params = {"apikey": self.api_key}
        response = requests.get(url, params=params)
        return response.json()

    def list_scam_addresses(self, chain_id):
        """
        Get the addresses that deployed a known scam token in the last 24 hours.
        NOTE: this endpoint is not available in the subscription plans,
              for access please contact us: https://www.soliduslabs.com/contact
        """
        url = f"{BASE_URL}/addresses/scams"
        params = {"chain_id": chain_id, "apikey": self.api_key}
        response = requests.get(url, params=params)
        return response.json()
