from blockchain import BlockChain
from transaction import Transaction
from block import Block
import json
import time 
import hashlib


NUM_TRANS_PER_BLOKC = 5


"""
Initialize the node.
address: address of this node
name: name of this node
min_ind: if this node a miner or not. default 0
"""
class Node:
    def __init__(self, address="", name="", min_ind = 0):
        self.transreviced = [] # Transactions reviced from other nodes but not added to the blockchian, use trans in here to mine 
        self.address = address
        self.name = name
        self.miner_indicator = min_ind
        # self.BlockChain = None # Test
        # self.nodes = {} # Test
        self.public_key = self.generate_key() 
        self.private_key = self.generate_key()
        self.BlockChain = self.getChain() 
        self.nodes = self.getNodes() 
        # self.WhoIam() """TODO function to broad the self information to other nodes"""
  

    """
    Get Nodes infomation from network
    """
    def getNodes(self):
        """TODO Collect node info from other nodes"""
        nodes = [{self.tojson()}]
        return nodes 
        


    """
    Get blockchain info from others
    """
    def getChain(self):
        """TODO Collect info from other nodes"""
        collected_chain = []

        if not collected_chain:
            tmp = BlockChain()
            # caculate the initial block
            return tmp


    """
    Generate the key randomly for this node
    """
    def generate_key(self):
        return hashlib.sha256(str(time.time()).encode("utf-8")).hexdigest()



    """
    sendCoin to "to" with value coins
    to: address of the node I will send money to 
    value: amount of coin I will send
    """
    def sendCoin(self, to="", value=0):

        coin = 0
        inputlist = []
        outputlist = []

        """ Looking for input list """
        for trans in self.BlockChain.getUnused():
            if trans.to != self.address:# if it is not  send to me 
                continue
            coin += trans.value
            inputlist.append(trans)
            if coin >= value:
                break
        if coin < value: 
            return None

        """ Generate outputlist"""
        msg="Cao ni ma de shou qian " + to + str(time.time()) + str(value)
        new_tran = Transaction(self.address, to=to, inlist=inputlist, outlist =[], header = msg, value = value)
        outputlist.append(new_tran)

        if coin > value: # if I have some change back
            msg ="Cao ni ma de zhao ling qian" + self.address + str(time.time()) + str(coin-value)
            new_tran = Transaction(self.address, self.address, inlist= inputlist, outlist=[], header=msg, value=coin-value)
            outputlist.append(new_tran)

        msg = "I, "+ str(self.address) + ", going to send money to " + str(to) + " money:" + str(value)
        send_trans = Transaction(self.address, to, inputlist, outputlist, msg, value = 0)

        """
        TODO broadcast the transaction
        """

        return send_trans
  

    """
    Process the transaction reviced from others
    trans: transaction recived from other node
    """
    def handleTransaction(self, trans):
        """TODO handle the sinagture of the sender"""
        
        signcheck = True
        if not signcheck:# failed in singature check
            return None
        
        self.transreviced.append(trans) # if pass the check, add it to recived
        if self.miner_indicator:
            # This is miner, mine
            self.mine()

        return True


    """
    Process the Block recived from others
    new_block: block send from others
    """
    def handleBlock(self, new_block):
        """TODO hanle the signature of the sender"""
        signcheck = True
        if not signcheck:
            return None

        self.BlockChain.addBlock(new_block)
        return True


    """
    When revice the measage from others add new node to self
    """
    def addNode(self):
        pass


    """
    Broad the transaction to other nodes 
    """
    def broadTrans(self):
        pass


    """
    Broadcast the Block mined by this Node
    """
    def boradBlock(self):
        pass


    """
    If this node is a miner, it should always calling this function to mine new block 
    """
    def mine():
        pass

    
    """
    Return the describution of this node
    """
    def tojson(self, debug = 0):
        if debug:
            node_info = {
              "address": self.address,
              "name": self.name,
              "miner": self.miner_indicator,
              "public key": self.public_key,
              "private key": self.private_key,
              "BlockChain": self.BlockChain.tojson()
            }
        else:
            node_info = {
              "address": self.address,
              "name": self.name,
              "public key": self.public_key
            }
        return json.dumps(node_info, sort_keys = True)
