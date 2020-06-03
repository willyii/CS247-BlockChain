from flask import Flask,Response, request, jsonify
import requests
import time 
import json
from threading import Thread
from node import Node
import random


app = Flask(__name__)

@app.route('/')
def hello():
    to = node.address
    while(to == node.address and node.nodes != []):
        to = random.choice(node.nodes)["address"]
    value = random.uniform(0.001, node.BlockChain.getBalance(node.address))
    # trans_message = node.sendCoin(to="http://0.0.0.0:200",value =40)
    trans_message = node.sendCoin(to=to,value =value)
    d = {
        "message": trans_message,
        "node_info": json.loads(node.tojson(1))
    }
    return jsonify(d), 200
    # return "Balance of this node: " + str(node.BlockChain.getBalance(node.address))

@app.route("/getChain", methods = ["GET"])
def broadChain():
    print("some one is asking for chain")
    d = node.BlockChain.tojson()
    return d, 200
    


@app.route("/handleBlock", methods=["POST"])
def handleBlock():
    block_str = request.data.decode()
    if node.handleBlock(block_str):
        d = {"message":"Good Job"}
        return jsonify(d), 200
    else:
        d = {"message":"Not Good"}
        return jsonify(d), 500

@app.route("/handleTrans", methods=["POST"])
def handleTrans():
    trans_str = request.data.decode()
    if node.handleTransaction(trans_str):
        d = {"message":"Good Job"}
        return jsonify(d), 200
    else:
        return 500


if __name__ == "__main__":
    # Parse the argument
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    address = "http://0.0.0.0:"+ str(port)

    node = Node(address =address, name = str(port), min_ind =1)
    app.run(port=port,debug=True,host='0.0.0.0')
