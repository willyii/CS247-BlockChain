from time import time


class Transaction:
    """
    Initialize the transaction. 
    f, to is the address of the node
    inlist is the transaction list 
    outlist is the transaction list. collected with inlist to generate new transaction
    header is the infomation of this transcation
    value is the value of this Transaction.
    """
    def __init__(self, f=None, to=None,inlist=[], outlist=[], header="", value=0 ):
        self.from = f
        self.to = to
        self.input = inlist
        self.output = outlist
        self.header = header
        self.value = value
        self.timestamp = time()


    """
    return the describtion of this transaction in json format
    """
    def tojson(self):
        pass
