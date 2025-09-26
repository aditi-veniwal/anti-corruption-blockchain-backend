import traceback
from app.blockchain.web3_connector import allocate_funds, mark_complete, release_funds, get_allocation

# -----------------------------
# Service: Allocate funds
# -----------------------------
def allocate_funds_service(recipient: str, amount: int):
    try:
        receipt = allocate_funds(recipient, amount)
        # Return only transaction hash (hex string)
        tx_hash = receipt["transactionHash"].hex()
        return {"success": True, "tx_hash": tx_hash}
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "trace": traceback.format_exc()
        }

# -----------------------------
# Service: Mark allocation complete
# -----------------------------
def mark_complete_service(recipient: str):
    try:
        receipt = mark_complete(recipient)
        tx_hash = receipt["transactionHash"].hex()
        return {"success": True, "tx_hash": tx_hash}
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "trace": traceback.format_exc()
        }

# -----------------------------
# Service: Release funds
# -----------------------------
def release_funds_service(recipient: str):
    try:
        receipt = release_funds(recipient)
        tx_hash = receipt["transactionHash"].hex()
        return {"success": True, "tx_hash": tx_hash}
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "trace": traceback.format_exc()
        }

# -----------------------------
# Service: Get allocation
# -----------------------------
def get_allocation_service(recipient: str):
    try:
        allocation = get_allocation(recipient)
        return {"success": True, "allocation": allocation}
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "trace": traceback.format_exc()
        }
