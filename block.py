import json

class Block:
    """
    Initialize the block, 
    prevhash is the hash of previous block
    currenthash is the hash of this block
    trans is the list of transactions of this block
    miner is the node who mined out this block
    zeros is the target that this block was used 
    """
    def __init__(self, prevhash="", currenthash="",trans=[], miner="", zeros = None):
        self.blockIndex = None
        self.currHash = currenthash
        self.prevHash = prevhash
        self.transactions = trans
        self.confirmed = False 
        self.miner = miner
        self.zeros = zeros
        self.nonce = None """ the nonce of this block"""    

    def tojson(self):
        block = {
            "blockIndex":self.blockIndex,
            "currentHash": self.currHash,
            "prevHash": self.prevHash,
            "transactions": self.transactions,
            "confirmed": self.confirmed,
            "miner": self.miner,
            "zeors": self.zeros,
            "nonce": self.nonce
        }
        block = json.dumps(block, sort_keys=True)
        block_str = json.loads(block)
        return block_str
