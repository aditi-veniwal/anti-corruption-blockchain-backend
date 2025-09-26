from web3 import Web3
import json
from app.core.config import settings

w3 = Web3(Web3.HTTPProvider(settings.WEB3_PROVIDER))

with open("D:/AntiCorruptionDapp/blockchain/artifacts/contracts/FundRelease.sol/FundRelease.json") as f:
    contract_json = json.load(f)
    abi = contract_json["abi"]

contract = w3.eth.contract(address=settings.CONTRACT_ADDRESS, abi=abi)
