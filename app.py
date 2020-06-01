from flask import Flask,Response, request, jsonify
import requests
import time 
import json
from threading import Thread
from node import Node

def sendFuckMessage():
    
    for i in range(100):
        d = {
            "message": "caonimabi"
        }
        r = requests.post("http://0.0.0.0:101/testpost", data = json.dumps(d))
        if r.status_code!=200:
            print("jia de IP cao ni ma r=: ", r)
        else:
            print("This is response message: ", r.json()["message"])
        time.sleep(10)


app = Flask(__name__)

@app.route('/')
def hello():

    test_tran = node.sendCoin(to="13131313")
    test_block = node.handleTransaction(test_tran.tojson())
    return json.loads(node.tojson(1))


@app.route("/testpost",  methods=['POST'])
def fucking():
    values = json.loads(request.data)

    print("This is what I got: ", values["message"])
    response = {
        "message": "I'm fucking know that"
    }
    return jsonify(response), 200


@app.route("/handleBlock", methods=["POST"])
def handleBlock():
    block_str = request.data
    if node.handleBlock(block_str):
        d = {"message":"Good Job"}
        return jsonify(d), 200
    else:
        return 500

@app.route("/handleTrans", methods=["POST"])
def handleTrans():
    trans_str = request.data
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

    address = "http://0.0.0.0/"+ str(port)
    node = Node(address = address, name = "mother fucker", min_ind =1)

    app.run("0.0.0.0",port=port,debug=True)
