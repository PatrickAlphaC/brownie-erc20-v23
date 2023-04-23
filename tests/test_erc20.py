from scripts.deploy_erc20 import INITIAL_SUPPLY
from brownie import reverts, accounts, Wei
from scripts.helper_functions import get_account


RANDOM_USER = accounts.add()


def test_initial_supply(erc20):
    assert erc20.totalSupply() == INITIAL_SUPPLY


def test_users_cant_mint(erc20):
    with reverts():
        erc20.mint(RANDOM_USER, 1000, {"from": RANDOM_USER})


def test_transfer_from(erc20):
    account = get_account()
    initial_account_balance = erc20.balanceOf(account)
    alice = accounts.add()
    amount = Wei("1 ether")
    erc20.approve(alice, amount, {"from": account})

    erc20.transferFrom(account, alice, amount, {"from": alice})
    assert erc20.balanceOf(alice) == amount
    assert erc20.balanceOf(account) == initial_account_balance - amount


# Can you get the coverage up?
