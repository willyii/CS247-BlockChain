from blockchain import BlockChain
from transaction import Transaction
from block import Block
import json
import time 
import hashlib
import tool 


NUM_TRANS_PER_BLOKC = 1


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
        self.public_key = self.generate_key() 
        self.private_key = self.generate_key()
        self.BlockChain = self.getChain() 
        self.nodes = self.getNodes() 
        self.NUM_ZEROS = 1
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
    When get new transaction, add it to list. If bigger than threshold, wrap as block and broadcast
    trans: New com transaction
    """
    def nextBlock(self, trans):
        self.transreviced.append(trans)
        if len(self.transreviced) >= NUM_TRANS_PER_BLOCK:
            new_block = Block()
            new_block.prevHash = self.BlockChain.getCurrHash()
            new_block.transactions = self.transreviced.copy()
            self.transreviced = []
            new_block.currHash = getNextHash(new_block.prevHash, new_block.transactions )
            return new_block
        return None



    """
    Process the transaction reviced from others
    trans: transaction recived from other node: recived from others need to be parse
    """
    def handleTransaction(self, trans_str):
        # pharse the trans_str 
        """TODO handle the sinagture of the sender""" 
        trans = Transaction()
        trans.parseJson(trans_str)
        new_block = nextBlock(trans)
        
        # Do not generate Block
        if not new_block:
            return True
 
        """TODO Broad New Block """

        return True


    """
    Process the Block recived from others
    new_block: block send from others, "str" type need to be pharse
    """
    def handleBlock(self, block_str):
        
        """TODO hanle the signature of the sender"""

        new_block = Block()
        new_block.parseJson(block_str)

        if new_block.confirmed:# if confirmed by someone, check and add block
            if proof_of_work(new_block):
                self.BlockChain.addBlock(new_block) 
                """TODO stop the mine thread"""
            else:
                print("Error in valid new block")
                pass

        elif self.miner_indicator:
            pass
            """TODO start thread to mine"""
        
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
    def mine(self, block):
        nonce = blockchain.proof_of_work(self, blcok.currHash, block.zeros)

        if nonce < 0:
            return

        block.confirmed = True
        block.nonce = nonce
        return block

    def proof_of_work(self, block_hash, zeros_num):
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new hash
        :param last_proof: <int>
        :return: <int>
        """
        pass_flag = False
        nonce = -1
        while(not pass_flag):
            nonce += 1
            guess_hash = hashlib.sha256(block_hash + str(nonce).encode("utf-8")).hexdigest()
            pass_flag = checkValid(guess_hash, zeros_num)
        return nonce


        # flag = 0
        # nonce = 0
        # guess = f'{block_hash}{nonce}'.encode()
        # guess_hash = hashlib.sha256(guess).hexdigest()
        # for i in range(zeros_num):
        #     if guess_hash[i] == "0":
        #         flag = flag + 1
        # 
        # while flag != zeros_num:
        #     flag = 0
        #     nonce += 1
        #     guess = f'{block_hash}{nonce}'.encode()
        #     guess_hash = hashlib.sha256(guess).hexdigest()
        #     for i in range(zeros_num):
        #         if guess_hash[i] == "0":
        #             flag = flag + 1
        # print("guess_hash=", guess_hash)
        # print("guess_hash[]=", guess_hash[:zeros_num])
        # return nonce


    
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
