from block import Block
from blockchain import BlockChain
from transaction import Transaction
from node import Node
import hashlib

def getTestChain():
    testblock = BlockChain()
    test_trans = Transaction(f="master", to="0", header ="test1",value= 5)
    testblock.addUnused(test_trans)
    test_trans = Transaction(f="master", to="0", header="test2",value = 3)
    testblock.addUnused(test_trans)
    return testblock 

def checkValid(prevHash,nonce,zeros):
    zeroString = []
    for i in range(zeros):
        zeroString.append('0')
    zeroString  = ''.join(zeroString)
    currBlock = str(prevHash).encode('utf-8') + str(nonce).encode('utf-8')
    guess_hash = hashlib.sha256(currBlock).hexdigest()
    return guess_hash[:zeros] == zeroString

def getTestHash(prevHash,nonce):
    currBlock = str(prevHash).encode('utf-8') + str(nonce).encode('utf-8')
    return hashlib.sha256(currBlock).hexdigest()

if __name__ == "__main__":

    testnode = Node(address = "0", name="fuck", min_ind = 0)
    testnode.BlockChain = getTestChain()
    # previous hash os the hash on the last one in bockchain
    prevHash = testnode.BlockChain.currHash
    zeros = 2
    # calculate nonce 
    guess_nonce = 0
    while checkValid(prevHash,guess_nonce,zeros) is False:
        guess_nonce += 1
    
    currHash = getTestHash(prevHash,guess_nonce)
    # update currenthash in the block
    testblock = Block(prevHash,currHash,testnode.BlockChain.getUnused(),testnode.address,zeros)
    testblock.nonce = guess_nonce
    testblock.blockIndex = len(testnode.BlockChain.chain)+1
    print(testblock.tojson())
    print("Block tojson test pass")
    res = testnode.BlockChain.addBlock(testblock)
    print(res.tojson())
    print("Block add to chain test pass")

    print(testnode.BlockChain.chain)
    print("Return current chain list pass")

    send = testnode.sendCoin("1", 7)
    print(send.tojson())
    print("Send Coint tojson test pass")

    # calculate nonce 



