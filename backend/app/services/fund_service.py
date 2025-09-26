from app.blockchain.web3_connector import w3, contract
from app.core.config import settings
from app.utils.signer import sign_and_send

def get_allocation(recipient: str):
    return contract.functions.allocations(recipient).call()

# def allocate_funds(recipient: str, amount: int):
#     tx = contract.functions.allocateFunds(recipient, amount).build_transaction({
#         "from": w3.eth.accounts[0],
#         "nonce": w3.eth.get_transaction_count(w3.eth.accounts[0])
#     })
#     return sign_and_send(tx, settings.PRIVATE_KEY)


def allocate_funds(recipient: str, amount: int):
    try:
        # Estimate gas
        gas_estimate = w3.eth.estimate_gas({
            "from": w3.eth.accounts[0],
            "to": contract.address,
            "data": contract.encodeABI(fn_name="allocateFunds", args=[recipient, amount])
        })

        tx = contract.functions.allocateFunds(recipient, amount).build_transaction({
            "from": w3.eth.accounts[0],
            "nonce": w3.eth.get_transaction_count(w3.eth.accounts[0], 'pending'),
            "gas": gas_estimate
        })

        return sign_and_send(tx, settings.PRIVATE_KEY)
    except Exception as e:
        return {"error": str(e)}



def mark_project_complete(recipient: str):
    tx = contract.functions.markProjectCompleted(recipient).build_transaction({
        "from": w3.eth.accounts[0],
        "nonce": w3.eth.get_transaction_count(w3.eth.accounts[0])
    })
    return sign_and_send(tx, settings.PRIVATE_KEY)

def release_funds(recipient: str):
    tx = contract.functions.releaseFunds(recipient).build_transaction({
        "from": w3.eth.accounts[0],
        "nonce": w3.eth.get_transaction_count(w3.eth.accounts[0])
    })
    return sign_and_send(tx, settings.PRIVATE_KEY)
