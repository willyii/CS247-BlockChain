# block class
# Block number, prev hash, timestamp, transfer data, hash of block, nonce

import hashlib
import json
from time import time
from flask import Flask, jsonify, request

class block:
    def __init__(self):
        self.blocknum = 0
        self.timestampe = 0
        self.transactions = []
        self.nonce = 0
        self.prevhash = 0
        self.owner = ""
    
    # add block to chain 
    def newBlock(self,nonce, prev_hash, pubKey):
        block = {
            'blocknum':len(self.chains) + 1,
            'timestampe': time(),
            'transactions':self.currentTrans,
            'nonce':nonce,
            'prevhash':prev_hash,
            'owner':pubKey
        }
        return block # return a Json data

    def hash_sha256(self,block):
        # hash block
        # from json to dictionary, sort by key
        block_string = json.dumps(block).encode()
        hashcode = hashlib.sha256(block_string,sort_keys=True).hexdigest()
        return hashcode

    def checkValid(self,currBlock, numerPrefixZeros):
        zeroString = None
        for i in range(numerPrefixZeros):
            zeroString+="0"
        guess_hash = hash_sha256(currBlock)
        return guess_hash[:numerPrefixZeros] == zeroString

    # update block nonce for calculating
    def tempBlock(self,nonce,prev_hash,pubKey):
        block = {
            'blocknum':len(self.chains) + 1,
            'timestampe': time(),
            'transactions':self.currentTrans,
            'nonce':nonce,
            'prevhash':prev_hash,
            'owner':pubKey
        }
        return block

    # process of miner
    def proof_of_work(self,prevBlock,pubKey,numerPrefixZeros):
        pre_hash = self.hash_sha256(prevBlock)
        nonce = 0
        # check sha256 if is satisfied or not
        while self.checkValid(self.tempBlock(nonce,pre_hash,pubKey),numerPrefixZeros) is False:
            nonce += 1
        return nonce