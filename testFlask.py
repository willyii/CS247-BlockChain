from flask import Flask,Response, request, jsonify
import requests
import time 
import json
from threading import Thread

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
    return Response("Hello Fucking Bitcoin")


@app.route("/testpost",  methods=['POST'])
def fucking():
    values = json.loads(request.data)

    print("This is what I got: ", values["message"])
    response = {
        "message": "I'm fucking know that"
    }
    return jsonify(response), 200



if __name__ == "__main__":
    # Parse the argument
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    parser.add_argument("-t", type = int)
    args = parser.parse_args()
    
    port = args.port
    indicator = args.t

    if indicator:
        t = Thread(target=sendFuckMessage)
        t.start()

    app.run("0.0.0.0",port=port,debug=True)
