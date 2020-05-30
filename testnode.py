from block import Block 
from transaction import Transaction
from blockchain import BlockChain
from node import Node


def getTestChain():
    testblock = BlockChain()
    test_trans = Transaction(f="master", to="0", header ="test1",value= 5)
    testblock.addUnused(test_trans)
    test_trans = Transaction(f="master", to="0", header="test2",value = 3)
    testblock.addUnused(test_trans)
    return testblock 

if __name__ == "__main__":
    """
    Initialize testnode
    """
    testnode = Node(address = "0", name="fuck", min_ind = 0)
    testnode.BlockChain = getTestChain()

    """
    Send Coint Test
    """
    send = testnode.sendCoin("1", 7)
    print(type(send.tojson()))
    print("Send Coint tojson test pass")

    """
    HandleTransaction Test 
    """
    test_trans = Transaction("master","0",header="test3", value = 7)
    print("Before handle trans: ", testnode.transreviced)
    testnode.handleTransaction(test_trans)
    print("After handle trans: ", testnode.transreviced)
    print("HanleTransaction Test Pass")
