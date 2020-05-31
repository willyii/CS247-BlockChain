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

def checkValid(hashval,zeros):
    zeroString = []
    for i in range(zeros):
        zeroString.append('0')
    zeroString  = ''.join(zeroString)
    return hashval[:zeros] == zeroString

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

def getNextHash(prevHash,transList):
    prevHash = str(prevHash).encode('utf-8')
    transList = transList.tojson().encode('utf-8')
    nextHash = hashlib.sha256(prevHash + transList).hexdigest()
    return nextHash

