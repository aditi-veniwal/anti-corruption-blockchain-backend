# from app.blockchain.web3_connector import w3

# def sign_and_send(tx: dict, private_key: str):
#     """
#     Signs a transaction with the given private key and sends it to the blockchain.
#     Compatible with web3.py v6+.
#     """
#     try:
#         # Sign the transaction
#         signed_tx = w3.eth.account.sign_transaction(tx, private_key)

#         # Send the raw transaction
#         # tx_hash = w3.eth.send_raw_transaction(signed_tx["rawTransaction"])
#         tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

        
#         # Wait for the transaction receipt
#         receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
#         return receipt

#     except Exception as e:
#         return {"error": str(e)}



def sign_and_send(tx: dict, private_key: str, w3):
    """
    Signs a transaction with the given private key and sends it to the blockchain.
    Compatible with web3.py v6+.
    """
    try:
        # Sign the transaction
        signed_tx = w3.eth.account.sign_transaction(tx, private_key)

        # Send raw transaction
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

        # Wait for transaction receipt
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt

    except Exception as e:
        return {"error": str(e)}
