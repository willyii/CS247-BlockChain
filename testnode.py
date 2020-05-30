from block import Block 
from transaction import Transaction
from blockchain import BlockChain
from node import Node


def getTestBlock():
    testblock = BlockChain()
    test_trans = Transaction(f="master", to="0", header ="test1",value= 5)
    testblock.addUnused(test_trans)
    test_trans = Transaction(f="master", to="0", header="test2",value = 3)
    testblock.addUnused(test_trans)
    return testblock 

if __name__ == "__main__":
    testnode = Node(address = "0", name="fuck", min_ind = 0)
    testnode.BlockChain = getTestBlock()

    send = testnode.sendCoin("1", 7)
    print(send.tojson())
