"""
BlockChain class

Implementation of a blockchain
store all confirmed blocks
"""
import json
from block import Block
from transaction import Transaction
import hashlib
import tool

NUM_TRANS_PER_BLOCK = 1

class BlockChain:
    """
    Initialize the blickchain
    chain is the blockchain 
    unused is a lost of all unsed/confirmed transactions
    currHash is the hash value of last block on the chain
    """
    def __init__(self,firstNodeAddress):
        self.chain = [] 
        self.unused = [] 
        self.currHash = 0
        if not self.addBlock(self.genesisBlock(firstNodeAddress)):
            raise Exception(" Gensis Block create false")

        
  
    """
    Generate a Genesis Block
    """
    def genesisBlock(self,firstNodeAddress):
        # generate a genesisiblock
        # index:1,  prevHash: 0
        # with one output transaction

        # generate output transaction
        msg = " Genesis Block reward for firstNode"
        outputs = Transaction("master", firstNodeAddress, [],[], msg, 50)

        # genesis transfer
        aggregateTrans = Transaction("master",firstNodeAddress,[],[],"Genesis Block transaction",0)
        aggregateTrans.output.append(outputs)

        genesis_block = Block()
        genesis_block.prevHash = 0
        genesis_block.blockIndex = 1
        genesis_block.transactions = [aggregateTrans]

        # calculate getNext hash
        genesis_block.currHash = tool.getNextHash(genesis_block.prevHash,genesis_block.transactions)
        genesis_block.confirmed = True
        genesis_block.miner = firstNodeAddress
        
        return genesis_block
        
    
    """
    function for adding a comfirmed block to current chain
    input: Block obejct, hash256 of this new block
    return: latest valid block 
    """
    def addBlock(self,block):

        # ADD genesis block
        if not self.chain:
            self.chain.append(block)
            self.currHash = block.currHash
            for o in block.transactions[0].output:
                self.unused.append(o)
            return True

        # if blockchain contains the block
        # duplication
        if block in self.chain:
            raise Exception(" input block is a duplicated block")
            return False

        if block.blockIndex >= len(self.chain)+2:
            raise Exception(" This Block is in the future")
            return False
    
        # find out all trans corrsponding to input 
        # remove input transactions out of unused list
        for item in block.transactions:
            for t in item.input:
                try:
                    self.unused.remove(t)
                except ValueError:
                    raise Exception(" input transaction may not exists")
                    return False
            # add output transactions in the unused list
            for o in item.output:
                self.unused.append(t)
            
        # add block to chain
        self.chain.append(block)
        # update currenthash
        self.currHash = block.currHash

        return True

    """
    function for adding new unused transactions
    input: Transaction object
    return: current unused transactions
    """
    def addUnused(self,trans):
        self.unused.append(trans)
        return self.unused


    """
    function for getting whole blockchain
    input: /
    return: current whole blockchain
    """
    def getBlockChain(self):
        return self.chain

    """
    function for getting all unused transactions
    input: /
    return: unused transactions list
    """
    def getUnused(self):
        return self.unused
    
    """
    function for getting last block's hash
    input: /
    return: last block's hash
    """
    def getCurrHash(self):
        return self.currHash

    
    """
    convert blockchain information into json format
    """
    def tojson(self):
        blockchain = {
            "chain":[x.tojson() for x in self.chain],
            "unused":[x.tojson() for x in self.unused],
            "currHash":self.currHash
        }
        blockchain = json.dumps(blockchain,sort_keys=True)
        return blockchain
