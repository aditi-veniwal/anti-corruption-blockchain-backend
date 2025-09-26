from app.blockchain.web3_connector import w3

def sign_and_send(tx, private_key: str):
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return {"tx_hash": tx_hash.hex()}
