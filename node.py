"""
Initialize the node.
address: address of this node
name: name of this node
min_ind: if this node a miner or not. default 0
"""
class Node:
    def __init__(self, address="", name="", min_ind = 0):
        self.address = address
        self.name = name
        self.miner_indicator = min_ind
        self.public_key = self.generate_key() """TODO function generate key of this Node"""
        self.private_key = self.generate_key()
        self.BlockChain = self.getChain() """TODO function to get chain from net or generate empty one"""
        self.nodes = self.getNodes() """TODO fucntion to get other nodes information in the network"""
        self.WhoIam() """TODO function to broad the self information to other nodes"""

        
