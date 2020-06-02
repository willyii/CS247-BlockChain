import json
from transaction import Transaction

class Block:
    """
    Initialize the block, 
    prevhash is the hash of previous block
    currenthash is the hash of this block
    trans is the list of transactions of this block
    miner is the node who mined out this block, use node's address
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
        self.nonce = None 
    
    """
    Return the descirbtion of this block in json format
    """
    def tojson(self):
        block = {
            "blockIndex":self.blockIndex,
            "currentHash": self.currHash,
            "prevHash": self.prevHash,
            "transactions": [x.tojson() for x in self.transactions],
            "confirmed": self.confirmed,
            "miner": self.miner,
            "zeros": self.zeros,
            "nonce": self.nonce
        }
        block_str = json.dumps(block, sort_keys=True, ensure_ascii=False)
        return block_str


    """
    parse the str data to Block
    """ 
    def parseJson(self, input_str):
        tmp = json.loads(input_str)
        self.blockIndex = tmp["blockIndex"]
        self.currHash = tmp["currentHash"]
        self.prevHash = tmp["prevHash"]
        self.miner = tmp["miner"]
        self.zeros = tmp["zeros"]
        self.nonce = tmp["nonce"]
        self.confirmed = tmp["confirmed"]
        self.transactions = []
        for t in tmp["transactions"]:
            tmp_t = Transaction()
            tmp_t.parseJson(t)
            self.transactions.append(tmp_t)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
