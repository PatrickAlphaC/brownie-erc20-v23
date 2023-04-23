#!/usr/bin/python3
from brownie import ManualToken, network
from scripts.helper_functions import (
    BLOCK_CONFIRMATIONS_FOR_VERIFICATION,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    is_verifiable_contract,
)

NAME = "ManualToken"
SYMBOL = "MT"
DECIMALS = 18
INITIAL_SUPPLY = 1_000_000_000_000_000_000


def deploy_erc20() -> ManualToken:
    account = get_account()
    print(f"On network {network.show_active()}")
    erc20 = ManualToken.deploy(
        NAME,
        SYMBOL,
        DECIMALS,
        INITIAL_SUPPLY,
        {"from": account},
    )

    if is_verifiable_contract():
        erc20.tx.wait(BLOCK_CONFIRMATIONS_FOR_VERIFICATION)
        ManualToken.publish_source(erc20)
    return erc20


def main():
    deploy_erc20()
