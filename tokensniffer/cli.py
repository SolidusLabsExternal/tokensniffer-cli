import json

import click

from tokensniffer.api import TokenSnifferAPI


def click_echo_json(d: dict):
    click.echo(json.dumps(d))


@click.group()
@click.option("--api-key", required=True)
@click.pass_context
def cli(ctx, api_key):
    ctx.obj = TokenSnifferAPI(api_key)


@cli.command()
@click.pass_obj
def get_usage(api):
    result = api.get_usage()
    click_echo_json(result)


@cli.command()
@click.option("--chain-id", required=True)
@click.option("--address", required=True)
@click.pass_obj
def get_token(api, chain_id, address):
    result = api.get_token(chain_id, address)
    click_echo_json(result)


@cli.command()
@click.pass_obj
def list_scam_tokens(api):
    result = api.list_scam_tokens()
    click_echo_json(result)


@cli.command()
@click.option("--address", required=True)
@click.pass_obj
def get_address(api, address):
    result = api.get_address(address)
    click_echo_json(result)


@cli.command()
@click.option("--network", required=True)
@click.pass_obj
def list_scam_addresses(api, network):
    result = api.list_scam_addresses(network)
    click_echo_json(result)


if __name__ == "__main__":
    cli()
