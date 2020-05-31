# from block import Block 
# from transaction import Transaction
# from blockchain import BlockChain
from node import Node
import hashlib
import json


# def getTestChain():
#     testblock = BlockChain()
#     test_trans = Transaction(f="master", to="0", header ="test1",value= 5)
#     testblock.addUnused(test_trans)
#     test_trans = Transaction(f="master", to="0", header="test2",value = 3)
#     testblock.addUnused(test_trans)
#     return testblock 
# 
# 
# def checkValid(prevHash,nonce,zeros):
#     zeroString = []
#     for i in range(zeros):
#         zeroString.append('0')
#     zeroString  = ''.join(zeroString)
#     currBlock = str(prevHash).encode('utf-8') + str(nonce).encode('utf-8')
#     guess_hash = hashlib.sha256(currBlock).hexdigest()
#     return guess_hash[:zeros] == zeroString
# 
# def getTestHash(prevHash,nonce):
#     currBlock = str(prevHash).encode('utf-8') + str(nonce).encode('utf-8')
#     return hashlib.sha256(currBlock).hexdigest()
# 
# def getTestBlock(node):
#     prevHash = node.BlockChain.currHash
#     zeros =2
#     guess_nonce = 0
#     while checkValid(prevHash, guess_nonce, zeros) is False:
#         guess_nonce += 1
# 
#     currHash = getTestHash(prevHash, guess_nonce)
# 
#      
#     testblock = Block(prevHash,currHash,testnode.BlockChain.getUnused(),testnode.address,zeros)
#     testblock.nonce = guess_nonce
#     testblock.blockIndex = len(testnode.BlockChain.chain)+1
# 
#     return testblock
# 


if __name__ == "__main__":

    """
    Initalize node test
    """
    testnode = Node(address = "Riverside", name = "fuck", min_ind = 1)
    print(testnode.tojson(1))
    print("========================Initialize Node Test Pass=================")


    """ Send Coint Test"""
    print(testnode.sendCoin(to="1", value = 10).tojson())
    print("=========================Send Coint Test Pass ===================")


    """Hanlde Transaction Test"""
    test_tran = testnode.sendCoin(to="1", value = 10).tojson()
    print(testnode.handleTransaction(test_tran).tojson())
    print("===========================Handle Transaction Test Pass=============")


    """Handle Unconfirmed Block Test"""
    unconfirmed_block = testnode.handleTransaction(test_tran).tojson()
    print(testnode.handleBlock(unconfirmed_block).tojson())
    print("=========================Handle Unconfirmed Block Test Pass==================")


    """Handle Confirmed Block Test"""
    confirmed_block = testnode.handleBlock(unconfirmed_block).tojson()
    status = testnode.handleBlock(confirmed_block)
    if status:
        print("Handle Confirmed Block Test Pass")
    print(testnode.tojson(1))





    # """
    # Initialize testnode
    # """
    # testnode = Node(address = "0", name="fuck", min_ind = 0)
    # testnode.BlockChain = getTestChain()
    # print("testnode info:")
    # print(testnode.tojson(1))
    # print("Initialization test pass")
    # 
    # """
    # Send Coint Test
    # """
    # send = testnode.sendCoin("1", 7)
    # print(send.tojson())
    # if type(send.tojson()) == type("sss"):
    #     print("Send Coin tojson test pass")
    # 
    # """
    # HandleTransaction Test 
    # """
    # test_trans = Transaction("master","0",header="test3", value = 7)
    # print("Before handle trans: ", testnode.transreviced)
    # testnode.handleTransaction(test_trans.tojson())
    # print("After handle trans: ", testnode.transreviced)
    # print("HanleTransaction Test Pass")
    # 
    # """
    # HanleBlock Test
    # """
    # testblock = getTestBlock(testnode)
    # if testnode.handleBlock(testblock.tojson()):
    #     print("HandleBlock Test Pass")
