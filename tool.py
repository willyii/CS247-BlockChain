"""
Tool class for handeling 
proof-of-work (confirmed block)
confirmation

"""
import hashlib
import json
from block import Block
from blockchain import BlockChain
from transaction import Transaction

"""
hasval, is the hash256 calculate by node who do proof-of-work
zeros, is number of prefix zeros 
compare if hashval satisify thet has correct number of prefix zeros
"""
def checkValid(hashval,zeros):
    valid = True
    for c in hashval[:zeros]:
        if c!= "0":
            valid = False
    return valid


"""
check the proof-of-work of a block 
which want to add to blockchain
"""
def valid_proof_of_work(incomeBlock):
    completed = False
    # do proof of work
    checkZero = incomeBlock.zeros
    checkHash = incomeBlock.currHash # prevhash + all transactions from incomeBlock
    checkNonce = incomeBlock.nonce

    # validate nonce
    getHash = hashlib.sha256(checkHash + str(checkNonce).encode('utf-8')).hexdigest()
    return checkValid(getHash,checkZero) 


"""
combine previous hash and current transactions
calculate hash256 value as nexthash
"""
def getNextHash(prevHash,transList):
    prevHash = str(prevHash).encode("utf-8")
    trans_str = "".join([str(t.tojson()) for t in transList]).encode("utf-8")
    nextHash = hashlib.sha256(prevHash + trans_str).hexdigest()
    return nextHash

