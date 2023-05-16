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
- [Github Actions-based continuous integration integration](./.github/workflows/test.yml)

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
ape plugins install vyper  # TODO: How to get rid of this step and automate it?
```

# Usage

## Compile the contracts

This will compile the contracts using the Vyper plugin for Ape.

```shell
ape compile
```

## Run unit tests

This will run the [pytest-based](https://pytest.org) test suite after recompiling the contracts:

```shell
ape test
```

More verbose:

```shell
ape test --log-cli-level=info
```

### Adding breakpoints to tests

The easiest way is with [ipdb console debugger based on Jupyter](https://pypi.org/project/ipdb/).

Edit [test.py](./tests/test.py):

```python
def test_hello_world(hello_world_contract):
    """We receive Hello World from the deployed contract accessor method"""
    import ipdb ; ipdb.set_trace()
    assert hello_world_contract.helloWorld() == "Hello Vyper!"

```

And run tests without stdin enabled:

```shell
ape test -s
```

You get interrupted at the breakpoint:

```text
tests/test_hello_world.py::test_hello_world SUCCESS: Contract 'HelloWorld' deployed to: 0x274b028b03A250cA03644E6c578D81f019eE1323
> /Users/moo/code/ts/ape-vyper-hello-world/tests/test_hello_world.py(27)test_hello_world()
     25     """We receive Hello World from the deployed contract accessor method"""
     26     import ipdb ; ipdb.set_trace()
---> 27     assert hello_world_contract.helloWorld() == "Hello Vyper!"

ipdb> 
```

Now you can poke around:

```
ipdb> type(hello_world_contract)
<class 'ape.contracts.base.ContractInstance'>
```

Or drop to ipython (gives better command line editor for typing Python):

```
ipdb> interact
*interactive*
In [1]: dir(hello_world_contract)
Out[1]: 
['address',
 'balance',
 'call_view_method',
 'code',
 'codesize',
 'contract_type',
 'decode_input',
 'get_event_by_signature',
 'helloWorld',
 'invoke_transaction',
 'is_contract',
 'nonce',
 'provider',
 'receipt',
 'txn_hash']

In [5]: hello_world_contract.balance
Out[5]: 0
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

