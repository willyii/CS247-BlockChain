from flask import Flask, Response   


app = Flask(__name__)

@app.route('/')
def hello():
    return Response("Hello Fucking Bitcoin")

if __name__ == "__main__":
    app.run()
