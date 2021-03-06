from blockchain import BlockChain
from threading import Thread
from transaction import Transaction
from block import Block
import json
import time 
import hashlib
from tool import getNextHash, valid_proof_of_work, checkValid
import requests
import random


NUM_TRANS_PER_BLOCK= 1


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
        self.nodes = self.getNodes() 
        self.BlockChain = self.getChain() 
        self.NUM_ZEROS = 5
        self.threadjob = False
        # self.WhoIam() """TODO function to broad the self information to other nodes"""
  
    """
    Get Nodes infomation from network
    """
    def getNodes(self):
        """TODO Collect node info from other nodes"""
        nodes = [{"address": "http://0.0.0.0:100"}
                ,{"address": "http://0.0.0.0:200"}
                ,{"address": "http://0.0.0.0:300"}
                ,{"address": "http://0.0.0.0:400"}
                ,{"address": "http://0.0.0.0:500"}]
        return nodes 
        


    """
    Get blockchain info from others
    """
    def getChain(self):
        best_chain = BlockChain(self.address)
        # select best train
        for n in self.nodes:
            try:
                if n["address"] == self.address:# skip self
                    continue
                r = requests.get(url= n["address"] + "/getChain")
                if r.status_code == 200: # get chain from others
                    new_chain = BlockChain(firstNodeAddress = self.address)
                    new_chain.parseJson(r.content)
                    if len(new_chain.chain) >= len(best_chain.chain):
                        best_chain = new_chain
            except:
                print("an error in get chain")
                pass
        return best_chain        

    

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
        if self.BlockChain.getBalance(self.address)<1:
            print("Do not have enough money")
            return False


        coin = 0
        inputlist = []
        outputlist = []

        """ Looking for input list """
        for trans in self.BlockChain.unused:
            if trans.to != self.address:# if it is not  send to me 
                continue
            coin += trans.value
            inputlist.append(trans)
            if coin >= value:
                break
        if coin < value:
            print("I only have : ", coin)
            print("Do not have enough money")
            return False

        """ Generate outputlist"""
        msg="Cao ni ma de shou qian " + str(to) + " " + str(time.time())+" " + str(value)
        new_tran = Transaction(self.address, to=to, inlist=inputlist, outlist =[], header = msg, value = value)
        outputlist.append(new_tran)

        if coin > value: # if I have some change back
            msg ="Cao ni ma de zhao ling qian" + self.address + str(time.time()) + str(coin-value)
            new_tran = Transaction(self.address, self.address, inlist= inputlist, outlist=[], header=msg, value=(coin-value))
            outputlist.append(new_tran)

        msg = "I'm going to send money to " + str(to) + ". value:" + str(value)
        send_trans = Transaction(self.address, to, inputlist, outputlist, msg, value = 0)
        self.broadTrans(send_trans)
        return msg
  
    """
    When get new transaction, add it to list. If bigger than threshold, wrap as block and broadcast
    trans: New com transaction
    """
    def nextBlock(self, trans):
        self.transreviced.append(trans)
        if len(self.transreviced) >= NUM_TRANS_PER_BLOCK:
            new_block = Block()
            new_block.blockIndex = len(self.BlockChain.chain) + 1
            new_block.prevHash = self.BlockChain.getCurrHash()
            new_block.transactions = self.transreviced.copy()
            self.transreviced = []
            new_block.currHash = getNextHash(new_block.prevHash, new_block.transactions )
            new_block.zeros = self.NUM_ZEROS
            return new_block
        return False



    """
    Process the transaction reviced from others
    trans: transaction recived from other node: recived from others need to be parse
    """
    def handleTransaction(self, trans_str):
        # pharse the trans_str 
        """TODO handle the sinagture of the sender""" 
        trans = Transaction()
        trans.parseJson(trans_str)
        new_block = self.nextBlock(trans)
        
        # Do not generate Block
        if not new_block:
            return True
 
        self.boradBlock(new_block)

        return True # Temporae


    """
    Process the Block recived from others
    new_block: block send from others, "str" type need to be pharse
    """
    def handleBlock(self, block_str):
        
        """TODO hanle the signature of the sender"""

        new_block = Block()
        new_block.parseJson(block_str)
        if not self.checkBlock(new_block):
            return False

        if new_block.confirmed:# if confirmed by someone, check and add block
            if valid_proof_of_work(new_block):
                print("Someone done before me, I'm going to stop")
                self.threadjob = False
                self.BlockChain.addBlock(new_block) 
            else:
                raise Exception("Hey this Block's Hash is not valid")
                return False

        elif self.miner_indicator:
            if self.threadjob:
                print("This is miner, I should mine, but I'm already doing ")
                return True
            print("Hey this is miner, I'm going to mine")
            self.threadjob = True
            t = Thread(target=self.mine, args = (new_block,))
            t.start()
        else:
            print("Hey this is unconfirmed block , but I am not miner, so I gonna miss it")
        return True
    

    """
    Check the Block is valid or not
    """
    def checkBlock(self, block):
        # already have or not 
        if block in self.BlockChain.chain:
            print("I already have this block")
            return False
        # check if the past block   
        if block.blockIndex <= self.BlockChain.chain[-1].blockIndex:
            self.getChain()
            print("Block pos not valid")
            return False
        # Check if it is future blokc
        if block.blockIndex >= len(self.BlockChain.chain)+2:
            print("I have block index problem, refetch the Chain")
            self.BlockChain = self.getChain()
            return self.checkBlock(block)
        
        return True



    """
    When revice the measage from others add new node to self
    """
    def addNode(self):
        pass


    """
    Broad the transaction to other nodes 
    """
    def broadTrans(self, trans):
        for n in self.nodes:
            try:
                r = requests.post(url=n["address"]+"/handleTrans", data = trans.tojson().encode())
            except:
                pass


    """
    Broadcast the Block mined by this Node
    """
    def boradBlock(self, b ):
        for n in self.nodes:
            try:
                r = requests.post(url=n["address"]+"/handleBlock", data = b.tojson().encode())
            except:
                pass


    """
    If this node is a miner, it should always calling this function to mine new block 
    """
    def mine(self, block):
        print("===========================Mining coin in thread======================")
        nonce = self.proof_of_work(block.currHash, block.zeros)

        if nonce < 0 or not self.threadjob:
            return False

        block.miner = self.address
        block.confirmed = True
        block.nonce = nonce
        if not self.threadjob:
            return False
        print("==========================I mined out===============")
        self.boradBlock(block)
        # self.broadTrans(self.bonusTrans())
        self.threadjob = False
        return True

    def proof_of_work(self, block_hash, zeros_num):
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new hash
        :param last_proof: <int>
        :return: <int>
        """
        pass_flag = False
        nonce = random.randint(0,1000)
        while(not pass_flag and self.threadjob):
            nonce += 1
            guess_hash = hashlib.sha256(str(block_hash).encode("utf-8") + str(nonce).encode("utf-8")).hexdigest()
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
    def bonusTrans(self):
        msg = "Genesis Block reward for firstNode"
        outputs = Transaction("master", self.address, [], [], msg, 50)  # bonus 50 to reward miner
        aggregateTrans = Transaction("master", self.address, [], [outputs], msg, 0) # bonus 0 to confirm this transaction

        return aggregateTrans

    
    """
    Return the describution of this node
    """
    def tojson(self, debug = 0):
        if debug:
            ts = [{"from":x.f, "to":x.to, "value":x.value} for x in self.BlockChain.trans]
            node_info = {
              "address": self.address,
              "name": self.name,
              "miner": self.miner_indicator,
              "public key": self.public_key,
              "private key": self.private_key,
              "BlockChain": len(self.BlockChain.chain),
              "Balance": self.BlockChain.getBalance(self.address),
              "Unused": len(self.BlockChain.unused),
              "trans": ts
            }
        else:
            node_info = {
              "address": self.address,
              "name": self.name,
              "public key": self.public_key
            }
        return json.dumps(node_info, sort_keys = True, ensure_ascii=False)
