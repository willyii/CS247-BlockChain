from blockchain import BlockChain
from transaction import Transaction
from block import Block
import json
import time 


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
        self.public_key = "public key" # Test
        self.private_key = "private key" #Test
        self.BlockChain = None # Test
        self.nodes = {} # Test
        # self.public_key = self.generate_key() """TODO function generate key of this Node"""
        # self.private_key = self.generate_key()
        # self.BlockChain = self.getChain() """TODO function to get chain from net or generate empty one"""
        # self.nodes = self.getNodes() """TODO fucntion to get other nodes information in the network"""
        # self.WhoIam() """TODO function to broad the self information to other nodes"""
    

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
    When revice the measage from others add new node to self
    """
    def addNode(self):
        pass


    """
    Process the Block recived from others
    """
    def handleBlock(self):
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

    

