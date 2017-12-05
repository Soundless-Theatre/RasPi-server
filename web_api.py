import lis
import json
from flask import Flask 
hoge = lis.list()
hoge.getcmd()

f = open("input.json")
data = f.read()
f.close()
app = Flask(__name__)

@app.route("/list")
def index():
	return data
app.run()
