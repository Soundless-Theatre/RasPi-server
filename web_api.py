import lis
import subprocess
import json
from flask import Flask, request
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
def get_user_info():
    username =  request.form['username'];
    age = request.form['age'];
    return username+age

app.run()
