import lis
import subprocess
import json
from flask import Flask, request
import connect
build = lis.list()
build.getcmd()

f = open("/home/kitsuda/Documents/RasPi-server/input.json")
data = f.read()
f.close()
app = Flask(__name__)

@app.route("/list")
def index():
	return data
@app.route("/connect", methods=["POST"])
def try_connct():
    connect.con(request.form['id'],request.form['pass'])
    return username+age

app.run()
