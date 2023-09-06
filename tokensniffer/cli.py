import json

import click

from tokensniffer.api import TokenSnifferAPI


def click_echo_json(d: dict):
    click.echo(json.dumps(d))


@click.group()
@click.option("--api-key", required=True, help="Your TokenSniffer API key.")
@click.pass_context
def cli(ctx, api_key):
    ctx.obj = TokenSnifferAPI(api_key)


@cli.command()
@click.pass_obj
def request_limit(api):
    result = api.get_request_limit()
    click_echo_json(result)


@cli.command()
@click.argument("chain_id")
@click.argument("address")
@click.pass_obj
def token_info(api, chain_id, address):
    result = api.get_token_info(chain_id, address)
    click_echo_json(result)


@cli.command()
@click.pass_obj
def scam_tokens_last_24_hours(api):
    result = api.get_scam_tokens_last_24_hours()
    click_echo_json(result)


@cli.command()
@click.argument("address")
@click.pass_obj
def scam_tokens_for_address(api, address):
    result = api.get_scam_tokens_for_address(address)
    click_echo_json(result)


@cli.command()
@click.argument("network")
@click.pass_obj
def addresses_with_scam_tokens_last_24_hours(api, network):
    result = api.get_addresses_with_scam_tokens_last_24_hours(network)
    click_echo_json(result)


if __name__ == "__main__":
    cli()
