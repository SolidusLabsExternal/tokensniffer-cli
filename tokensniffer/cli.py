import json

import click

from tokensniffer.api import TokenSnifferAPI


def click_echo_json(resp: dict):
    click.echo(json.dumps(resp))


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
@click.option("--chain-id", required=True, type=int)
@click.option("--address", required=True, type=str)
@click.option('--include-metrics', required=False, type=bool)
@click.option('--include-tests', required=False, type=bool)
@click.option('--block-until-ready', required=False, type=bool)
@click.pass_obj
def get_token(api, chain_id, address, include_metrics, include_tests, block_until_ready):
    result = api.get_token(chain_id, address, include_metrics, include_tests, block_until_ready)
    click_echo_json(result)


@cli.command()
@click.option("--chain-id", required=False)
@click.option('--limit', required=False)
@click.option('--offset', required=False)
@click.option('--deployer-address', required=False)
@click.pass_obj
def list_scam_tokens(api, chain_id, limit, offset, deployer_address):
    result = api.list_scam_tokens(chain_id, limit, offset, deployer_address)
    click_echo_json(result)


@cli.command()
@click.option("--address", required=True)
@click.pass_obj
def get_address(api, address):
    result = api.get_address(address)
    click_echo_json(result)


@cli.command()
@click.option("--chain_id", required=False)
@click.option('--limit', required=False)
@click.option('--offset', required=False)
@click.pass_obj
def list_scam_addresses(api, chain_id, limit, offset):
    result = api.list_scam_addresses(chain_id, limit, offset)
    click_echo_json(result)


if __name__ == "__main__":
    cli()
