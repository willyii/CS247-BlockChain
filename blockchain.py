# Blockchain class

import hashlib
import json
from json import JSONEncoder
from time import time
from flask import Flask, jsonify, request,Response
import block
import node
import transaction
from urllib.parse import urlparse
from uuid import uuid4
from textwrap import dedent


class blockchain(object):
    def __init__(self):
        self.chains = []
        self.nodes = {}
        self.currentTrans = []
        self.nonces  = []

    @property
    def last_block(self):
        return self.chains[-1]
    @property
    def chain_index(self):
        return len(self.chains) 
   
    def nodes_list(self):
        node = []
        for i in range(len(self.nodes)):
            item = self.nodes[str(i+1)].get('Address')
            node.append(item)
        #node = json.dumps(node,sort_keys=True)
        #node = json.loads(node)
        return node

    def genesisBlock(self,numerPrefixZeros):
        # set up a temp block to generate nonce
        
        trans = self.addTransaction("master","master",0)
        newBlock = block.newBlock(1,self.currentTrans,0,0)
        nonce = block.proof_of_work(newBlock,0,numerPrefixZeros)
        # update genesis block value
        #newBlock = block.newBlock(1,nonce,self.currentTrans,0,0)
        if nonce > 0 :
        # add to blockchain
            self.chains.append(newBlock)
            self.nonces.append(nonce)
        return newBlock, nonce


    # add block to chain 
    def addBlock(self,nonce, prev_hash, pubKey):
        index = len(self.chains)
        newBlock = block.newBlock(index,nonce,self.currentTrans,prev_hash,pubKey)
        self.currentTrans = [] #reset current transactions
        self.chain.append(newBlock)
        return newBlock # return a Json data
    
    def addNode(self,address):
        parsed_url = urlparse(address)
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
            id = len(self.nodes) + 1
            newNode = node.newNode(id,address)
            self.nodes[str(id)] = newNode
        return newNode
    
    def addTransaction(self,from_p,to_p,value):
        trans = transaction.newTrans(from_p,to_p,value)
        # confirm
        self.currentTrans.append(trans)
        return trans
        
    def mineBlock(self,numerPrefixZeros):
        # get last block on the chain
        last_block = chain.last_block
        
        #proof = chain.proof_of_work(last_block,pubKey,numerPrefixZeros)

        # # We must receive a reward for finding the proof.
        # # The sender is "0" to signify that this node has mined a new coin.
        # blockchain.new_transaction(
        #     sender="0",
        #     recipient=node_identifier,
        #     amount=1,
        # )

        # # Forge the new Block by adding it to the chain
        # previous_hash = chain.hash_sha256(last_block)
        # block = chain.addBlock(proof, previous_hash)
        return last_block



# Instantiate the Node
app = Flask(__name__)
# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')
# Instantiate the Blockchain
chain = blockchain()

@app.route("/",methods=['POST'])
def newChain():
    index = chain.chain_index
    if index >= 1:
        return 'already initial with genesis block', 500

    values = request.get_json()
    required = ['numZero']
    if not all(k in values for k in required):
        return 'Missing values', 400
    
    numerPrefixZeros = int(values['numZero'])

    block = chain.genesisBlock(numerPrefixZeros)
    gene_block = block[0]
    nonce = block[1]
    print("Currently initial a genesis block, try staring a blockchain by adding some nodes / transactions ")
    response = {
        'message': "Genesis Block Forged",
        'index': gene_block['blocknum'],
        'timestampe': gene_block['timestampe'],
        'transactions': gene_block['transactions'],
        'prevhash':gene_block['prevhash'],
        'owner':gene_block['owner'],
        'nonce':nonce
    }
    #'nonce': block['nonce'],
    return jsonify(response), 200

@app.route('/newtrans', methods=['POST'])
def addTransaction():
    values = request.get_json()
    # Check that the required fields are in the POST'ed data
    required = ['sender', 'reciver', 'value']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Create a new Transaction
    trans = chain.addTransaction(values['sender'], values['reciver'], values['value'])

    response = {'message': f'Transaction will be added to Block {trans}'}
    return jsonify(response), 201

@app.route('/addnodes', methods=['POST'])
def addNodes():
    values = request.get_json()
    required = ['Address']
    if not all(k in values for k in required):
        return 'Missing values', 400
    
    node = chain.addNode(values['Address'])

    response = {
        'message': f'New nodes have been added{node}'
    }
    return jsonify(response), 201

@app.route('/getallnodes',methods=['GET'])
def getNodes():
    node = chain.nodes_list()
    response = {
        'nodes':node,
        'length':len(node)
    }
    return jsonify(response), 200

@app.route('/mine', methods=['GET'])
def mine():
    # We run the proof of work algorithm to get the next proof...
    block = chain.mineBlock()
    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200


if __name__ == '__main__':

    app.run("0.0.0.0", port=80, debug=True)

