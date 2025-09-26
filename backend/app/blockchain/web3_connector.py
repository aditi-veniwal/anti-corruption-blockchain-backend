import json
from web3 import Web3

# ✅ Connect to your local Hardhat blockchain
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Verify the connection
if not w3.is_connected():
    raise Exception("❌ Web3 connection failed. Make sure Hardhat node is running on 8545.")

# ✅ Load ABI (Application Binary Interface) for the FundRelease contract
with open("D:/AntiCorruptionDapp/blockchain/artifacts/contracts/FundRelease.sol/FundRelease.json", "r") as f:
    contract_json = json.load(f)
    abi = contract_json["abi"]

# ✅ Use the deployed contract address from Hardhat deploy script
contract_address = "0x5FbDB2315678afecb367f032d93F642f64180aa3"

# ✅ Create contract instance
contract = w3.eth.contract(address=contract_address, abi=abi)

# ✅ Print for quick sanity check (optional)
print("Connected to blockchain:", w3.is_connected())
print("Contract loaded at:", contract.address)
