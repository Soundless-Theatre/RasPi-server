from flask import Flask, request
from flask.ext.cors import  CORS
app = Flask(__name__)
cors=CORS(app)
@app.route("/list")
def index():
    print("list request")
    f = open("./input.json")
    data = f.read()
    f.close()
    return data
@app.route("/connect", methods=["POST"])
def try_connct():
    print("connect request",request.form['id'],request.form['pass'])
    return "ok"
@app.route("/settitle",methods=["POST"])
def set_title():
    print("settitle request",request.form["title"])
    return "ok"

app.run(host="0.0.0.0")