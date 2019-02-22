
from web3 import Web3, HTTPProvider
import json
import sys
import urllib
from eth_account import Account


byte = "608060405234801561001057600080fd5b5061068c806100206000396000f3fe608060405234801561001057600080fd5b5060043610610073577c01000000000000000000000000000000000000000000000000000000006000350463019848928114610078578063a191247214610120578063c18c749d1461012a578063d3a72ea1146101d0578063f6b9ef4c14610203575b600080fd5b6100ab6004803603602081101561008e57600080fd5b503573ffffffffffffffffffffffffffffffffffffffff166102f9565b6040805160208082528351818301528351919283929083019185019080838360005b838110156100e55781810151838201526020016100cd565b50505050905090810190601f1680156101125780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b610128610393565b005b6101286004803603602081101561014057600080fd5b81019060208101813564010000000081111561015b57600080fd5b82018360208201111561016d57600080fd5b8035906020019184600183028401116401000000008311171561018f57600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295506103ef945050505050565b6100ab600480360360208110156101e657600080fd5b503573ffffffffffffffffffffffffffffffffffffffff1661044b565b6102a96004803603602081101561021957600080fd5b81019060208101813564010000000081111561023457600080fd5b82018360208201111561024657600080fd5b8035906020019184600183028401116401000000008311171561026857600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929550610501945050505050565b60408051602080825283518183015283519192839290830191858101910280838360005b838110156102e55781810151838201526020016102cd565b505050509050019250505060405180910390f35b600060208181529181526040908190208054825160026001831615610100026000190190921691909104601f81018590048502820185019093528281529290919083018282801561038b5780601f106103605761010080835404028352916020019161038b565b820191906000526020600020905b81548152906001019060200180831161036e57829003601f168201915b505050505081565b3360009081526001602052604090205460ff1615156103b157600080fd5b336000818152600160209081526040808320805460ff1916905580518083018083528482529484529183905290912090516103ec92906105c5565b50565b3360009081526001602052604090205460ff161561040c57600080fd5b33600090815260208181526040909120825161042a928401906105c5565b5050336000908152600160208190526040909120805460ff19169091179055565b73ffffffffffffffffffffffffffffffffffffffff81166000908152602081815260409182902080548351601f60026000196101006001861615020190931692909204918201849004840281018401909452808452606093928301828280156104f55780601f106104ca576101008083540402835291602001916104f5565b820191906000526020600020905b8154815290600101906020018083116104d857829003601f168201915b50505050509050919050565b60606002826040518082805190602001908083835b602083106105355780518252601f199092019160209182019101610516565b51815160209384036101000a6000190180199092169116179052920194855250604080519485900382018520805480840287018401909252818652935091508301828280156104f557602002820191906000526020600020905b815473ffffffffffffffffffffffffffffffffffffffff16815260019091019060200180831161058f5750505050509050919050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061060657805160ff1916838001178555610633565b82800160010185558215610633579182015b82811115610633578251825591602001919060010190610618565b5061063f929150610643565b5090565b61065d91905b8082111561063f5760008155600101610649565b9056fea165627a7a72305820f921059aa401501dd52be284799f9cb6d3eecbf1fd06ffb264661fa8263750f00029"

abi = json.loads("""[
	{
		"constant": true,
		"inputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"name": "name",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "RemoveName",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_name",
				"type": "string"
			}
		],
		"name": "AddName",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_person",
				"type": "address"
			}
		],
		"name": "GetName",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_name",
				"type": "string"
			}
		],
		"name": "GetAddresses",
		"outputs": [
			{
				"name": "",
				"type": "address[]"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	}
]""")

def GetGas():
    f = urllib.request.urlopen("https://gasprice.poa.network")
    gasinfo = json.loads(f.read().decode('utf-8'))['fast']
    return int(gasinfo) * 1000000000

def GetAdres(privateKey):
    adress = Account.privateKeyToAccount("0x"+privateKey)
    return adress

def SetTransaction(abi, byte, person):

    contract = web3.eth.contract(abi=abi, bytecode=byte)
    SignedTX = contract.constructor().buildTransaction({
    'from': person.address,
    'nonce': web3.eth.getTransactionCount(person.address),
    'gasPrice': GetGas()
    })
    SignedTX = person.signTransaction(SignedTX)
    RawTX = web3.eth.sendRawTransaction(SignedTX.rawTransaction)
    TXReceipt = web3.eth.waitForTransactionReceipt(RawTX)

    with open('database.json', 'w') as file:
        file.write(json.dumps({'registrar': TXReceipt['contractAddress'], 'startBlock': TXReceipt['blockNumber']}))
    return {'registrar': TXReceipt['contractAddress'], 'startBlock': TXReceipt['blockNumber']}

def AddName(Caddres, person, name):
    contract_by_address =  web3.eth.contract(address = Caddres, abi = abi)
    tx_wo_sign = contract_by_address.functions.AddName(name).buildTransaction({
        'from': person.address,
        'nonce': web3.eth.getTransactionCount(person.address),
        'gas': 8000000,
        'gasPrice': GetGas()
    })
    signed_tx = person.signTransaction(tx_wo_sign)
    try:
        txId = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    except:
        return {'status': -1}

    #txId = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    txReceipt = web3.eth.waitForTransactionReceipt(txId)
    return txReceipt

def RemoveName(person):
    contract_by_address =  web3.eth.contract(address = Caddres, abi = abi)
    tx_wo_sign = contract_by_address.functions.RemoveName().buildTransaction({
        'from': person.address,
        'gas': 8000000,
        'nonce': web3.eth.getTransactionCount(person.address),
        'gasPrice': GetGas()
    })
    signed_tx = person.signTransaction(tx_wo_sign)
    txId = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    txReceipt = web3.eth.waitForTransactionReceipt(txId)
    return txReceipt

def GetName(Caddres, person):
    contract_by_address = web3.eth.contract(address = Caddres, abi = abi)
    return contract_by_address.functions.GetName(person).call()


web3 = Web3(HTTPProvider('https://sokol.poa.network'))

with open('account.json') as file:
    privateKey = json.load(file)['account']
address = GetAdres(privateKey)

args = (sys.argv)[1:]

with open('database.json') as file:
    Caddres = json.load(file)['registrar']

if args[0] == '--deploy':
    TRInfo = SetTransaction(abi, byte, address)
    #print(TRInfo)

if args[0] == '--add':
    TRInfo = AddName(Caddres, address, args[1])
    #print(TRInfo)
    if(TRInfo['status'] == 0):
        print("One account must correspond one name")
    if(TRInfo['status'] == -1):
        print("No enough funds to add name")

if args[0] == '--del':
    TRInfo = RemoveName(address)
    if TRInfo['status'] == 0:
        print("No name found for your account")

if args[0] == '--getname':
    print(GetName(Caddres, web3.toChecksumAddress(args[1])))

"""
print("\nFile Info:\n")
print(privateKey)
"""
