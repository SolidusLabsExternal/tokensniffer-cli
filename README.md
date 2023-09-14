# tokensniffer-cli

CLI and Python modules for accessing the TokenSniffer API.
See docs:
https://tokensniffer.readme.io/reference/introduction

PyPI packages may be released over time.
For now, installing the CLI and modules from the git repo on your favorite project:

```shell
pip install git+ssh://git@github.com/SolidusLabsExternal/tokensniffer-cli.git@tokensniffer-py
```

Alternatively, if you want to modify the code and install, you may wish to clone the repo and install manually.

```sh
git clone git@github.com:SolidusLabsExternal/tokensniffer-cli.git
mkdir your_project
cd your_project
python -m venv venv
source ./venv/bin/activate
pip install ../tokensniffer-cli/
```

# CLI use examples

By default, API key is fetched from your environment variable `TOKENSNIFFER_API_KEY`. It can also be passed as a parameter.

```sh
tokensniffer get-usage

tokensniffer get-token --chain-id 1 --address "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"

tokensniffer list-scam-tokens

tokensniffer get-address --address "0x0000000000000000000000000000000000000000"

tokensniffer list-scam-addresses --chain-id 1

```

NOTE:
`list-scam-addresses` & `list-scam-tokens` endpoints are not available in the subscription plans,
for access please contact us: https://www.soliduslabs.com/contact
