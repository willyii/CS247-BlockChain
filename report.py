from transaction import Transaction 
from block import Block
from blockchain import BlockChain
from node import Node

b = Transaction(f="xinlong",to="zhuocheng", inlist=[], outlist=[], header="Xinlong send 5 coins to zhuocheng", value =5)
print(b.tojson())
