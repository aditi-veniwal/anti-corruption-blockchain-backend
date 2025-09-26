import json
from web3 import Web3
from web3.exceptions import ContractLogicError
from app.core.config import settings

# ----------------------------
# Initialize Web3
# ----------------------------
w3 = Web3(Web3.HTTPProvider(settings.WEB3_PROVIDER))
if not w3.is_connected():
    raise ConnectionError(f"Unable to connect to blockchain at {settings.WEB3_PROVIDER}")

# ----------------------------
# Default account (from private key)
# ----------------------------
account = w3.eth.account.from_key(settings.PRIVATE_KEY)
default_account = account.address

# ----------------------------
# Contract instance
# ----------------------------
contract = w3.eth.contract(address=Web3.to_checksum_address(settings.CONTRACT_ADDRESS), abi=settings.CONTRACT_ABI)

# ----------------------------
# Helper: Sign and send transaction
# ----------------------------
def sign_and_send(tx: dict):
    """
    Signs and sends a transaction, then waits for the receipt.
    """
    try:
        signed_tx = w3.eth.account.sign_transaction(tx, settings.PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt
    except ContractLogicError as e:
        return {"error": f"Contract execution failed: {str(e)}"}
    except Exception as e:
        return {"error": str(e)}

# ----------------------------
# Blockchain operations
# ----------------------------
def get_allocation(recipient: str):
    """
    Returns allocation for a recipient.
    """
    try:
        recipient = Web3.to_checksum_address(recipient)
        return contract.functions.allocations(recipient).call()
    except Exception as e:
        return {"error": str(e)}

def allocate_funds(recipient: str, amount: int):
    """
    Allocates funds to a recipient.
    """
    try:
        recipient = Web3.to_checksum_address(recipient)
        tx = contract.functions.allocateFunds(recipient, amount).build_transaction({
            "from": default_account,
            "nonce": w3.eth.get_transaction_count(default_account, "pending"),
            "gasPrice": w3.to_wei("1", "gwei")
        })

        # Estimate gas
        tx["gas"] = w3.eth.estimate_gas({
            "from": default_account,
            "to": contract.address,
            "data": tx["data"]
        })

        return sign_and_send(tx)
    except Exception as e:
        return {"error": str(e)}

def mark_complete(recipient: str):
    """
    Marks a project as completed for the recipient.
    """
    try:
        recipient = Web3.to_checksum_address(recipient)
        tx = contract.functions.markProjectCompleted(recipient).build_transaction({
            "from": default_account,
            "nonce": w3.eth.get_transaction_count(default_account, "pending"),
            "gasPrice": w3.to_wei("1", "gwei")
        })

        tx["gas"] = w3.eth.estimate_gas({
            "from": default_account,
            "to": contract.address,
            "data": tx["data"]
        })

        return sign_and_send(tx)
    except Exception as e:
        return {"error": str(e)}

def release_funds(recipient: str):
    """
    Releases funds to a recipient.
    """
    try:
        recipient = Web3.to_checksum_address(recipient)
        tx = contract.functions.releaseFunds(recipient).build_transaction({
            "from": default_account,
            "nonce": w3.eth.get_transaction_count(default_account, "pending"),
            "gasPrice": w3.to_wei("1", "gwei")
        })

        tx["gas"] = w3.eth.estimate_gas({
            "from": default_account,
            "to": contract.address,
            "data": tx["data"]
        })

        return sign_and_send(tx)
    except Exception as e:
        return {"error": str(e)}
