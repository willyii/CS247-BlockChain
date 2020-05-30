"""
BlockChain class

Implementation of a blockchain
store all confirmed blocks
"""
import json
from block import Block
from transaction import Transaction
import hashlib

NUM_TRANS_PER_BLOCK = 5

class BlockChain:
    """
    Initialize the blickchain
    chain is the blockchain 
    unused is a lost of all unsed/confirmed transactions
    currHash is the hash value of last block on the chain
    """
    def __init__(self):
        self.chain = [] 
        self.unused = [] 
        self.currHash = 0 

    
    """
    function for calculate sha256 
    input: block as string format which need to be checked 
    return: sha256 value
    """
    def hash_sha256(self,block_string):
        # hash block
        # from json to dictionary, sort by key
        #block_string = json.dumps(block,sort_keys=True).encode('utf-8')
        hashcode = hashlib.sha256(block_string).hexdigest()
        return hashcode
    
    """
    function for check validation of the block
    which requesting for adding to current chain
    input: block need to be checked 
    return: validation or not
    """
    #class ValidationError(Exception):
    #    pass
    
    # a gloabl value for storing hash value
    NextHash = 0

    def validation(self,block):
        status = 0
        #checkBlock = Block()
        checkBlock = block
        if checkBlock.blockIndex >= len(self.chain)+2:
            # this block is in the future
            status = 0
            raise Exception(" This Block is in the future")
            return status
        # 1. check nonce is satisfied with proof
        checkNonce = checkBlock.nonce
        checkHash = checkBlock.currHash
        print(checkHash)
        # get encode string format of block object
        checkEncode = checkBlock.tojson().encode('utf-8')
        if checkBlock.blockIndex == 1:
            checkEncode = str(0).encode('utf-8')
        # return sha256 value
        NextHash = self.hash_sha256(checkEncode + str(checkNonce).encode('utf-8'))
        if(NextHash == checkHash):
            status = 1
        else:
            status = 0
            raise Exception(" This Block has HASH error")
            return status
        # 2. TO DO check signature of all transactions in the block
        # 3. TO DO check signature of the Block
        return status 
    
    """
    function for adding a comfirmed block to crrent chain
    input: Block obejct
    return: latest vlaid block 
    """
    def addBlock(self,block):
        #checkBlock = Block()
        checkBlock = block
        # if blockchain contains the block
        # duplication
        if checkBlock in self.chain:
            raise Exception(" input block is a duplicated block")
            return checkBlock
    
        if self.validation(checkBlock) == 1: # if the block is valid
            trans = checkBlock.transactions
           # find out all trans corrsponding to input 
           # remove input transactions out of unused list
            for item in trans:
                for t in item.input:
                    exists = self.unused.remove(item)
                    if(exists == False): # input trans does not exists
                        raise Exception(" input transaction may not exists")
                        return checkBlock
                # add output transactions in the unused list
                for o in item.output:
                    self.unused.append(item)
                
            # update hash
            NextHash = checkBlock.currHash
            # update block confirmed value
            checkBlock.confirmed = True
            # add to chain
            self.chain.append(block)

        return checkBlock

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
