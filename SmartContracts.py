
from web3 import Web3, HTTPProvider
import json
import sys
import urllib
from eth_account import Account

#bytecode
byte = "608060405234801561001057600080fd5b506109cc806100206000396000f3fe608060405234801561001057600080fd5b5060043610610074576000357c010000000000000000000000000000000000000000000000000000000090048063019848921461007957806317e4bcbd146101365780637713e71714610229578063a5440fa014610285578063d3a72ea1146102e4575b600080fd5b6100bb6004803603602081101561008f57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506103a1565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156100fb5780820151818401526020810190506100e0565b50505050905090810190601f1680156101285780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b61020f6004803603604081101561014c57600080fd5b810190808035906020019064010000000081111561016957600080fd5b82018360208201111561017b57600080fd5b8035906020019184600183028401116401000000008311171561019d57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610451565b604051808215151515815260200191505060405180910390f35b61026b6004803603602081101561023f57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919050505061066b565b604051808215151515815260200191505060405180910390f35b61028d61078d565b6040518080602001828103825283818151815260200191508051906020019060200280838360005b838110156102d05780820151818401526020810190506102b5565b505050509050019250505060405180910390f35b610326600480360360208110156102fa57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919050505061081b565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561036657808201518184015260208101905061034b565b50505050905090810190601f1680156103935780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b60006020528060005260406000206000915090508054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156104495780601f1061041e57610100808354040283529160200191610449565b820191906000526020600020905b81548152906001019060200180831161042c57829003601f168201915b505050505081565b6000600160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16151561066057826000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002090805190602001906104f89291906108fb565b5060018060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055506000600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054141561065757600360008154809291906001019190505550600354600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555060043390806001815401808255809150509060018203906000526020600020016000909192909190916101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550505b60019050610665565b600090505b92915050565b6000600160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff1615610783576000600160003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff02191690831515021790555060206040519081016040528060008152506000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002090805190602001906107799291906108fb565b5060019050610788565b600090505b919050565b6060600480548060200260200160405190810160405280929190818152602001828054801561081157602002820191906000526020600020905b8160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190600101908083116107c7575b5050505050905090565b60606000808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156108ef5780601f106108c4576101008083540402835291602001916108ef565b820191906000526020600020905b8154815290600101906020018083116108d257829003601f168201915b50505050509050919050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061093c57805160ff191683800117855561096a565b8280016001018555821561096a579182015b8281111561096957825182559160200191906001019061094e565b5b509050610977919061097b565b5090565b61099d91905b80821115610999576000816000905550600101610981565b5090565b9056fea165627a7a72305820c1ea668b8f69f59e6fa6e3b4f84bd5a947d8db54d3b46fe24b8c5963704c189c0029"

#abi code
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
		"inputs": [
			{
				"name": "_name",
				"type": "string"
			},
			{
				"name": "_person",
				"type": "address"
			}
		],
		"name": "AddName",
		"outputs": [
			{
				"name": "",
				"type": "bool"
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
				"name": "_person",
				"type": "address"
			}
		],
		"name": "RemoveName",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "GetAll",
		"outputs": [
			{
				"name": "",
				"type": "address[]"
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
	}
]""")

def GetGas():
    f = urllib.request.urlopen("https://gasprice.poa.network")
    gasinfo = json.loads(f.read().decode('utf-8'))['fast']
    return int(gasinfo * 1000000000)


def GetAdres(privateKey):
    adress = Account.privateKeyToAccount("0x"+privateKey)
    return adress

def SetTransaction(abi, byte, person):

	#create transaction
	contract = web3.eth.contract(abi=abi, bytecode=byte)
	SignedTX = contract.constructor().buildTransaction({
	'from': person.address,
	'nonce': web3.eth.getTransactionCount(person.address),
	'gasPrice': GetGas()
	})
	SignedTX = person.signTransaction(SignedTX)
	RawTX = web3.eth.sendRawTransaction(SignedTX.rawTransaction)
	TXReceipt = web3.eth.waitForTransactionReceipt(RawTX)
	#write transaction info
	f = open('database.json', 'w')
	f.close()
	with open('database.json', 'w') as file:
		file.write(json.dumps({'registrar': TXReceipt['contractAddress'], 'startBlock': TXReceipt['blockNumber']}))
	return {'registrar': TXReceipt['contractAddress'], 'startBlock': TXReceipt['blockNumber']}

def AddName(Caddres, abi, byte, person, name):
	#create transaction
	contract_by_address =  web3.eth.contract(address = Caddres, abi = abi)
	tx_wo_sign = contract_by_address.functions.AddName(name, person.address).buildTransaction({
		'from': person.address,
		'nonce': web3.eth.getTransactionCount(person.address),
		'gas': 8000000,
		'gasPrice': GetGas()
    })
	signed_tx = person.signTransaction(tx_wo_sign)
	#sending transaction
	TX = {'status': 0, 'transactionHash': 0}
	TX['status'] = int(contract_by_address.functions.AddName(name, person.address).call())
	if TX['status'] == 0:
		return TX
	try:
		txId = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
	except:
		return {'status': -1, 'transactionHash': 0}

	txReceipt = web3.eth.waitForTransactionReceipt(txId)
	TX['transactionHash'] = txReceipt['transactionHash']
	return TX

def RemoveName(person, abi):
	#create transaction
	contract_by_address =  web3.eth.contract(address = Caddres, abi = abi)
	tx_wo_sign = contract_by_address.functions.RemoveName(person.address).buildTransaction({
    	'from': person.address,
    	'gas': 8000000,
    	'nonce': web3.eth.getTransactionCount(person.address),
    	'gasPrice': GetGas()
	})
	signed_tx = person.signTransaction(tx_wo_sign)
	#sending transaction
	TX = {'status': 0, 'transactionHash': 0}
	TX['status'] = int(contract_by_address.functions.RemoveName(person.address).call())
	try:
		txId = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
	except:
		return {'status': -1, 'transactionHash': 0}

	txReceipt = web3.eth.waitForTransactionReceipt(txId)
	TX['transactionHash'] = txReceipt['transactionHash']
	return TX

def GetName(Caddres, abi, person):
    contract_by_address = web3.eth.contract(address = Caddres, abi = abi)
    return contract_by_address.functions.GetName(person).call()

def GetList(Caddres, abi):
	contract_by_address = web3.eth.contract(address = Caddres, abi = abi)
	RawList = contract_by_address.functions.GetAll().call()
	list = {}
	for i in RawList:
		name = GetName(Caddres, abi, i)
		if name != '':
			list[name] = i
	return list

def GetAcc(Caddres, abi, name):
	RawList = GetList(Caddres, abi)
	list = []
	for i in RawList:
		if i == name:
			list.append(RawList[i])
	return list


#Connection
web3 = Web3(HTTPProvider('https://sokol.poa.network'))

#Get account info
with open('account.json') as file:
    privateKey = json.load(file)['account']
address = GetAdres(privateKey)

#get arguments
args = (sys.argv)[1:]
if(len(args) > 2):
	for i in range(2, len(args)):
		args[1] = args[1] + " " + args[i]



if args[0] == '--deploy':
	TRInfo = SetTransaction(abi, byte, address)
	print("Contract address:", TRInfo['registrar'])
    #print(TRInfo)

#Get transaction info
with open('database.json') as file:
	Caddres = json.load(file)['registrar']

if args[0] == '--add':
	TRInfo = AddName(Caddres, abi, byte, address, args[1])
	if(TRInfo['status'] == 0):
		print("One account must correspond one name")
	if(TRInfo['status'] == -1):
		print("No enough funds to add name")
	if(TRInfo['status'] == 1):
		print("Successfully added by", (TRInfo["transactionHash"]).hex())
	#print(TRInfo)

if args[0] == '--del':
	TRInfo = RemoveName(address, abi)
	if(TRInfo['status'] == 0):
		print("No name found for your account")
	if(TRInfo['status'] == -1):
		print("No enough funds to delete name")
	if(TRInfo['status'] == 1):
		print("Successfully deleted by",  TRInfo["transactionHash"].hex())
	#print(TRInfo)

if args[0] == '--getname':
	name = GetName(Caddres, abi, web3.toChecksumAddress(args[1]))
	if(name == ''):
		print("No name registered for this account")
	else:
		print("Registered account is ",'"', name, '"', sep='')

if args[0] == '--list':
	list = GetList(Caddres, abi)
	for i in list:
		print('"',i,'"',': ', list[i], sep ='')

if args[0] == '--getacc':
	list = GetAcc(Caddres, abi, args[1])
	if(len(list) == 0):
		print("No account registered for this name")
	if(len(list) == 1):
		print("Registered account is", list[0])
	if(len(list) > 1):
		print("Registered accounts are:")
		for i in list:
			print(i)

"""
print("\nFile Info:\n")
print(privateKey)
"""
