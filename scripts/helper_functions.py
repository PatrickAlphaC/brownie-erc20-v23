from brownie import (
    network,
    accounts,
    config,
)
import time

NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "ganache"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS + [
    "mainnet-fork",
    "binance-fork",
    "matic-fork",
]

# Etherscan usually takes a few blocks to register the contract has been deployed
BLOCK_CONFIRMATIONS_FOR_VERIFICATION = (
    1 if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS else 6
)


def is_verifiable_contract() -> bool:
    return config["networks"][network.show_active()].get("verify", False)


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])
