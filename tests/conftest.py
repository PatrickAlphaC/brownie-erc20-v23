import pytest
from scripts.deploy_erc20 import deploy_erc20


@pytest.fixture
def erc20():
    return deploy_erc20()
