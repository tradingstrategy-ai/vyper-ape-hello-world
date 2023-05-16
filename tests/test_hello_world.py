from typing import List

import pytest
from ape_test.accounts import TestAccount
from ape.managers.project.manager import ProjectManager
from ape.contracts.base import ContractInstance


@pytest.fixture
def deployer(accounts: List[TestAccount]) -> TestAccount:
    """Choose the account number 0 as the deployer account.

    Each EVM backend gives you a list of predefined test accounts
    loaded with ETH.
    """
    return accounts[0]


@pytest.fixture
def hello_world_contract(
    project: ProjectManager, deployer: TestAccount
) -> ContractInstance:
    """Deploy our Vyper contract on our unit testing EVM backend."""
    return deployer.deploy(project.HelloWorld)


def test_hello_world(hello_world_contract: ContractInstance):
    """We receive Hello World from the deployed contract accessor method"""
    assert hello_world_contract.helloWorld() == "Hello Vyper!"
