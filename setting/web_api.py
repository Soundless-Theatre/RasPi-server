from flask import Flask, request
from flask.ext.cors import  CORS
app = Flask(__name__)
cors=CORS(app)
f = open("/home/pi/RasPi-server/settong/input.json")
data = f.read()
f.close()
str_data = ""

@app.route("/list",methods=["GET"])
def index():
    return data

@app.route("/connect", methods=["POST"])
def try_connect():
    ssid = request.json['ssid']
    password = request.json['pass']
    str_data = ssid + " " + password
    p = open("/home/pi/RasPi-server/setting/pass.txt","w")
    p.write(str_data)
    p.close()
    return "ok"

@app.route("/connect_app", methods=["POST"])
def try_conncet_app():
    app_data = request.data
    str_data = app_data.decode()
    p_a = open("/home/pi/RasPi-server/setting/pass.txt","w")
    p_a.write(str_data)
    p_a.close()
    return "ok"

@app.route("/settitle",methods=["POST"])
def set_title():
    f=open("/home/pi/RasPi-server/setting/title.txt","w")
    f.write(request.json["title"])
    return "ok"

app.run(host="0.0.0.0")
