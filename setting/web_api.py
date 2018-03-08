from flask import Flask, request
from flask.ext.cors import  CORS
app = Flask(__name__)
cors=CORS(app)
f = open("./home/pi/RasPi-server/settong/input.json")
data = f.read()
f.close()
str_data = ""

@app.route("/list",methods=["GET"])
def index():
    return data

@app.route("/connect", methods=["POST"])
def try_connect():
    ssid = request.form['ssid']
    password = request.form['pass']
    str_data = ssid + " " + password
    writepass()
    return "ok"

@app.route("/connect_app", methods=["POST"])
def try_conncet_app():
    app_data = request.data
    str_data = app_data.decode()
    weitepass()
    return "ok"

@app.route("/settitle",methods=["POST"])
def set_title():
    f=open("./home/pi/RasPi-server/setting/title.txt","w")
    f.write(request.form["title"])
    str_data = ""
    return "ok"

def writepass():
    p = open("./home/pi/RasPi-server/setting/pass.txt", "w")
    p.write(str_data)
    p.close()

app.run(host="0.0.0.0")
