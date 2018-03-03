import lis
import subprocess
import json
from flask import Flask, request
import connect

f = open("./input.json")
data = f.read()
f.close()
app = Flask(__name__)

@app.route("/list")
def index():
        lis.list.getcmd()
        f = open("./input.json")
        data = f.read()
        f.close()
        return data
@app.route("/connect", methods=["POST"])
def try_connct():
    connect.con(request.form['id'],request.form['pass'])
    return "ok"
@app.route("/settitle",methods=["POST"])
def set_title():
    f=open("../title.txt","w")
    f.writes(request.form["title"])


app.run()
