import os

import pytest

from tokensniffer.api import TokenSnifferAPI

NULL_ADDRESS = "0x" + "0" * 40


@pytest.fixture
def api():
    return TokenSnifferAPI()


def test_api_key_in_env_vars(api):
    assert os.getenv("TOKENSNIFFER_API_KEY")


def test_request_limit(api):
    result = api.get_request_limit()
    assert isinstance(result["used"], int)


def test_token_info(api):
    chain_id = 1
    address = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
    result = api.get_token_info(chain_id, address)
    assert result["message"] == "OK"
    assert result["is_flagged"] is False


def test_scam_tokens_last_24_hours(api):
    result = api.get_scam_tokens_last_24_hours()
    assert result["message"] == "OK"


def test_scam_tokens_for_address(api):
    result = api.get_scam_tokens_for_address(NULL_ADDRESS)
    assert result["message"] == "OK"


@pytest.mark.skip
def test_addresses_with_scam_tokens(api):
    network = "BSC"
    result = api.get_addresses_with_scam_tokens_last_24_hours(network)
    assert result["message"] == "OK"
