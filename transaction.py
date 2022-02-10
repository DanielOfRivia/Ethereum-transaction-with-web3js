from encodings import utf_8
from web3 import Web3

ganache_url = 'https://ropsten.infura.io/v3/ba19ad63f7e14e27ab84bd3e2d41e65f'
web3 = Web3(Web3.HTTPProvider(ganache_url))
account_1 = '0xe9e44c610B3B455CF86A1f24cCc02443b49F811B'
private_key1 = '179fccb62b40cf0c4fcd56a7e15a04ee75607b4a340527a32eecbdd884aa32c6'
account_2 = '0xc53D6C0148ddC28Efe623Ab3aD54da5C7779b25C'

#get the nonce.  Prevents one from sending the transaction twice
nonce = web3.eth.getTransactionCount(account_1)

#build a transaction in a dictionary
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(0.01, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
    'data': bytes("Ustymenko_Danylo", "utf_8")
}

#sign the transaction
signed_tx = web3.eth.account.sign_transaction(tx, private_key1)

#send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

#get transaction hash
print(web3.toHex(tx_hash))