

# from web3 import Web3,HTTPProvider
# import json

# def connect_with_blockchain(acc):
#     rpcServer = "HTTP.//127.0.0.1:7545"
#     web3=web3(HTTPProvider(rpcServer))
#     print('connected to blockchain')

#     if acc==0:
#      web3.eth.defaultAccount=web3.eth.account[0]
#     else:
#          web3.eth.defaultAccount=acc
#     with open/contracts('/Users/neerajkachhap/Desktop/truffle assignment/build') as f:
#             contract_json =json.load(f)
#             contract_abi=contract_json['abi']
#             contract_address = contract_json['networks']['5777']['address']

#             contract =  web3.eth.contract(address=contract_address,abi=contract_abi)
#             return(contract,web3)

# try:
#     contract,web3=connect_with_blockchain(0)
#     tx_hash=contract.functions.add(2,3).transact()
#     web3.eth.waitForTransactionReceipt(tx_hash)

#     output=contract.function.result()
# except:
#          print('This contract information is already avail')



# from web3 import Web3, HTTPProvider
# import json

# def connect_with_blockchain(acc):
#     # Corrected RPC server URL
#     rpcServer = "http://127.0.0.1:7545"
#     web3 = Web3(HTTPProvider(rpcServer))  # Correct initialization
#     print('Connected to blockchain')

#     # Check connection
#     if not web3.isConnected():
#         print("Failed to connect to the blockchain.")
#         return None, None

#     # Set default account
#     if acc == 0:
#         default_account = web3.eth.accounts[0]  # Use the first account as default
#     else:
#         default_account = acc

#     web3.eth.defaultAccount = default_account  # Set the default account

#     # Load contract ABI and address
#     try:
#         with open(r'C:\Users\rajen\OneDrive\Desktop\contractDapp\build\contracts\Contact.json', 'r') as f:
#             contract_json = json.load(f)
#             contract_abi = contract_json['abi']
#             contract_address = contract_json['networks']['5777']['address']

#             contract = web3.eth.contract(address=contract_address, abi=contract_abi)
#             return contract, web3
#     except FileNotFoundError:
#         print("Contract JSON file not found.")
#     except KeyError:
#         print("ABI or address not found in contract JSON file.")
#     except Exception as e:
#         print(f"An error occurred while loading the contract: {e}")

#     return None, None

# try:
#     contract, web3 = connect_with_blockchain(0)
    
#     if contract and web3:
#         # Example of inserting a contact
#         tx_hash = contract.functions.insertContact(
#             'Rajendra', '987654321', 'raj@example.com', 'Rajendra.Org'
#         ).transact({'from': web3.eth.defaultAccount})
#         web3.eth.wait_for_transaction_receipt(tx_hash)  # Corrected method name
#         print("Contact inserted successfully.")

#         # Example of viewing contacts
#         contacts = contract.functions.viewContacts().call()
#         print("Names:", contacts[0])
#         print("Mobiles:", contacts[1])
#         print("Emails:", contacts[2])
#         print("Organizations:", contacts[3])
# except Exception as e:
#     print(f'An error occurred: {e}')


from web3 import Web3, HTTPProvider
import json
import time

def connect_with_blockchain(acc):
    rpcServer = "http://127.0.0.1:7545"
    web3 = Web3(HTTPProvider(rpcServer))
    print('connected a blockchain')

    if acc == 0:
        web3.eth.defaultAccount = web3.eth.accounts[0]
    else:
        web3.eth.defaultAccount = web3.eth.accounts[acc]

    with open('C:\Users\rajen\OneDrive\Desktop\contractDapp\build\contracts\Contact.json') as f:
        contract_json = json.load(f)
        contract_abi = contract_json['abi']
        contract_address = contract_json['networks']['5777']['address']

    contract = web3.eth.contract(address=contract_address, abi=contract_abi)

    return(contract,web3)

try:
    contract,web3 = connect_with_blockchain(0)
    print("Sending Transation....\n")
    tx_hash = contract.functions.insertContact("Raushan", "9334188618", "abc@gmail.com", "Google").transact()
    print(f"Transation Hash: {tx_hash.hex()}\n")
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print("This contact information was added successfully")
        
except Exception as e:
    print("This contact is already available");

contract,web3 = connect_with_blockchain(0)

name, mobile, email, org = contract.functions.viewContacts().call()
print(name)
print(mobile)
print(email)
print(org)