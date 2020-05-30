from time import time
import json


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
        self.f = f
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
        transaction = {
            "from": self.f,
            "to": self.to,
            "input": [x.tojson() for x in self.input],#self.input,
            "output": [x.tojson() for x in self.output],#self.output,
            "header": self.header,
            "value": self.value,
            "timestamp": self.timestamp
        }
        transaction = json.dumps(transaction, sort_keys = True)
        return transaction

        
       
