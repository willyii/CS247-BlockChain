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
    zeroString = []
    for i in range(zeros):
        zeroString.append('0')
    zeroString  = ''.join(zeroString)
    return hashval[:zeros] == zeroString

"""
check the proof-of-work of a block 
which want to add to blockchain
"""
def proof_of_work(incomeBlock):
    completed = False
    if(incomeBlock.confirmed is True):
        # do proof of work
        checkZero = incomeBlock.zeros
        checkHash = incomeBlock.currHash # prevhash + all transactions from incomeBlock
        checkNonce = incomeBlock.nonce
        # calculate nonce 
        guess_nonce = 0
        getHash = hashlib.sha256(checkHash + str(checkNonce).encode('utf-8')).hexdigest()
        if checkValid(getHash,checkZero) is True:
            completed = True
        else:
            raise Exception("This Block has not been complete proof of work")
        return completed
    else:
        raise Exception("This Block has not been confirmed")
        return completed

    return completed

"""
combine previous hash and current transactions
calculate hash256 value as nexthash
"""
def getNextHash(prevHash,transList):
    prevHash = str(prevHash).encode('utf-8')
    trans_str = ""
    for item in transList:
        item = item.tojson().encode('utf-8')
        trans_str += item
    nextHash = hashlib.sha256(prevHash + trans_str).hexdigest()
    return nextHash

