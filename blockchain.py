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

NUM_TRANS_PER_BLOCK = 5

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
        outputs = Transaction()
        outputs.f = "master"
        outputs.t = firstNodeAddress
        outputs.value = 50
        outputs.header = " Genesis Block reward for firstNode"

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
            self.currentHash = block.currentHash
            for o in block.transactions[0].output:
                self.unused.append(o)
            return True

        # if complete proofofwork, add to blockchain
        success = False
        checkBlock = block
        # if blockchain contains the block
        # duplication
        if checkBlock in self.chain:
            raise Exception(" input block is a duplicated block")
            return success

        if checkBlock.blockIndex >= len(self.chain)+2:
            raise Exception(" This Block is in the future")
            return success
    
        trans = checkBlock.transactions
        # find out all trans corrsponding to input 
        # remove input transactions out of unused list
        for item in trans:
            for t in item.input:
                exists = self.unused.remove(item)
                if(exists == False): # input trans does not exists
                    raise Exception(" input transaction may not exists")
                    return success
            # add output transactions in the unused list
            for o in item.output:
                self.unused.append(item)
            
        # add block to chain
        self.chain.append(block)
        # update currenthash
        self.currHash = block.currHash
        success = True

        return success

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
