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
def connect_wifi():
	SSID = request.form["ssid"]
	PASSWORD = request.form["password"]
	cmd = ("nmcli device wifi connect " + SSID + " password " + PASSWORD)
	print(cmd)
	return None

app.run()
