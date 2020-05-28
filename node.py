# Node class
import hashlib
import json
from time import time
from flask import Flask, jsonify, request
import cryptography
from Crypto.PublicKey import RSA
from Crypto import Random

class node:
    def __init__(self):
        self.ID = ""
        self.Address = ""
        self.pubKey = ""
        self.priKey = ""

    def newNode(self,id,address):
        random_generator = Random.new().read
        private_key = RSA.generate(1024,random_generator)
        public_key = private_key.publickey()
        node = {
            'ID':id,
            'Address':address,
            'pubKey': public_key,
            'priKey': private_key
        }
        return node


