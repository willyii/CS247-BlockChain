"""
BlockChain class

Implementation of a blockchain
store all confirmed blocks
"""

class blockchain(object):
    self.chain = [] # blockchain
    self.unused = [] # unused transaction list
    self.currHash = 0 # previous block's hash


    """
    function for adding a comfirmed block to crrent chain
    input: Block obejct
    return: current blockchain 
    """
    def addBlock(self,block):
        self.chain.append(block)
        return self.chain

    """
    function for adding new unused transactions
    input: Transaction object
    return: current unused transactions
    """
    def addUnused(self,trans):
        self.unused.append(trans)
        return self.unused

    """
    function for updating current hash
    input: current hash value
    return: new current hash value
    """
    def updateHashVal(self,hashVal):
        self.currHash = hashVal
        return self.currHash

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
        return self.prevHash