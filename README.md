# Vyper and ApeWorX Hello World Project

Use this template to get started with [Vyper](https://vyperlang.org/) smart contract development using [ApeWorX](https://www.apeworx.io/) framework.

You probably want to run this tutorial if 

- You like Python
- You like smart contracts
- You love [EVM-blockhains](https://tradingstrategy.ai/glossary/evm-compatible)

The example covers

- Installing tools
- Compiling contracts
- Running unit tests
- [Github Actions-based continuous integration integration]()

# Prerequisites

- [Python 3.10 installation](https://python.org)
- [Poetry installed on Python](https://python-poetry.org/docs/#installation)
- We recommend Visual Studio Code with [Vyper syntax highlighting](https://marketplace.visualstudio.com/items?itemName=tintinweb.vscode-vyper)

# Installation

First, clone this project:

```shell
git clone https://github.com/tradingstrategy-ai/vyper-ape-hello-world.git
```

Then install `ape` and all Python packages using Poetry:

```shell
cd project
poetry shell
poetry install
```

# Usage

## Compile the contracts

This will compile the contracts using the Vyper plugin for Ape.

```shell
ape compile
```

## Run unit tests

This will run the [pytest-based](https://pytest.org) test suite.

```shell
ape test
```

## Deploy

```
# TODO
```

# Learn more

- [See Vyper resources](https://docs.vyperlang.org/en/latest/resources.html)
- [The state of Python in blockchain ecosystem 2023 report](https://tradingstrategy.ai/blog/the-state-of-python-in-blockchain-in-2023)

Brought you by [Trading Strategy](https://tradingstrategy.ai).
For any questions and follow-ups:

- [Community Discord server](https://tradingstrategy.ai/community#discord)
- [Blog](https://tradingstrategy.ai/blog)
- [Twitter](https://twitter.com/TradingProtocol)
- [Telegram channel](https://t.me/trading_protocol)
- [Newsletter](https://tradingstrategy.ai/newsletter)

Please kindly give heads up and contact via other channels before opening issues or pull requests.

