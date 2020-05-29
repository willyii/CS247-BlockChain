# Node class
import hashlib
import json
from time import time
from flask import Flask, jsonify, request
from Crypto.PublicKey import RSA
from Crypto import Random

# class node(object):
#     def __init__(self):
#         self.ID = ""
#         self.Address = ""
#         self.pubKey = ""
#         self.priKey = ""

def newNode(id,address):
    keyPair = RSA.generate(2048)
    pubKey = keyPair.publickey()
    priKey = keyPair.exportKey()

    node = {
        'ID':id,
        'Address':address,
        'pubKey': pubKey,
        'priKey': priKey
    }
    # self.ID = id
    # self.Address = address
    # self.priKey = priKey
    # self.pubKey = pubKey 
    return node


