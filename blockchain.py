# Blockchain class

import hashlib
import json
from time import time
from flask import Flask, jsonify, request
import block
import node
from urllib.parse import urlparse

class blockchain(object):
    def __init__(self):
        self.chains = []
        self.nodes = set()
        self.currentTrans = []


    # add block to chain 
    def addBlock(self,nonce, prev_hash, pubKey):
        newBlock = block.newBlock(nonce,prev_hash,pubKey)
        self.currentTrans = [] #reset current transactions
        self.chain.append(newBlock)
        return newBlock # return a Json data
    
    def addNode(self,id,address):
        parsed_url = urlparse(address)
        newNode = None
        addSuccess  = False
        if parsed_url.netloc:
            address = parsed_url.netloc
            addSuccess = True
        elif parsed_url.path:
            address = parsed_url.path
            addSuccess = True
        else:
            raise ValueError('Invalid URL')
        if(addSuccess):
            newNode = node.newNode(id,address)
            self.nodes.add(newNode)
        return newNode
        
    





