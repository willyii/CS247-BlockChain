# transaction class
import hashlib
import json
from time import time
from flask import Flask, jsonify, request
#class transaction(object):
 #   def __init__(self):
  #      self.sender = ""
   #     self.reciver = ""
    #    self.value = 0
     #   self.timestampe = 0
    
def newTrans(from_p,to_p,value):
    # should add signiture variable later
    trans = {
        'sender': from_p,
        'reciver':to_p,
        'value':value,
        'timestamp':time()
    }
    return trans