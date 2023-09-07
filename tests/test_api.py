import os

import pytest

from tokensniffer.api import TokenSnifferAPI

NULL_ADDRESS = "0x" + "0" * 40


@pytest.fixture
def api():
    return TokenSnifferAPI()


def test_api_key_in_env_vars(api):
    assert os.getenv("TOKENSNIFFER_API_KEY")


def test_get_usage(api):
    result = api.get_usage()
    assert isinstance(result["used"], int)


def test_get_token(api):
    chain_id = 1
    address = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
    result = api.get_token(chain_id, address)
    assert result["message"] == "OK"
    assert result["is_flagged"] is False


def test_list_scam_tokens(api):
    result = api.list_scam_tokens()
    assert result["message"] == "OK"


def test_get_address(api):
    result = api.get_address(NULL_ADDRESS)
    assert result["message"] == "OK"


@pytest.mark.skip
def test_list_scam_addresses(api):
    network = "BSC"
    result = api.list_scam_addresses(network)
    assert result["message"] == "OK"
