# block class
# Block number, prev hash, timestamp, transfer data, hash of block, nonce

import hashlib
import json
from time import time
#from flask import Flask, jsonify, request

# class block(object):
#     def __init__(self):
#         self.blocknum = 0
#         self.timestampe = 0
#         self.transactions = []
#         self.nonce = 0
#         self.prevhash = 0
#         self.owner = ""
    
# add block to chain 
def newBlock(index,trans,prev_hash,pubKey):
    block = {
        'blocknum':index,
        'timestampe': time(),
        'transactions':trans,
        'prevhash':prev_hash,
        'owner':pubKey
    }
    #  'nonce':nonce,
    return block # return a Json data

def hash_sha256(block_string):
    # hash block
    # from json to dictionary, sort by key
    #block_string = json.dumps(block,sort_keys=True).encode('utf-8')
    hashcode = hashlib.sha256(block_string).hexdigest()
    return hashcode

def checkValid(prevBlock, nonce,numerPrefixZeros):
    zeroString = []
    for i in range(numerPrefixZeros):
        zeroString.append('0')
    zeroString  = ''.join(zeroString)
    currBlock = prevBlock + str(nonce).encode('utf-8')
    guess_hash = hash_sha256(currBlock)
    return guess_hash[:numerPrefixZeros] == zeroString


# process of miner
def proof_of_work(prevBlock,pubKey,numerPrefixZeros):
    #prev_hash = 0
    block = json.dumps(prevBlock,sort_keys=True)
    block_str = json.loads(block)
    index = int(block_str['blocknum'])
    #if index > 1:
     #   prev_hash = hash_sha256(prevBlock)
    nonce = 0
    #tempBlock = newBlock(index,nonce,block_str['transactions'],prev_hash,pubKey)
    # check sha256 if is satisfied or not
    while checkValid(block.encode('utf-8'),nonce,numerPrefixZeros) is False:
        nonce += 1
    return nonce