from flask import Flask, request
import connect
from flask.ext.cors import  CORS

app = Flask(__name__)
cors=CORS(app)

@app.route("/list")
def index():
        f = open("/home/pi/workspace/RasPi-server/setting/input.json")
        data = f.read()
        f.close()
        return data
@app.route("/connect", methods=["POST"])
def try_connct():
    f=open("home/pi/workspace/RasPi-server/setting/pass.txt","w")
    f.write(request.form['ssid']+" "+request.form['pass'])
    f.close()
    return "ok"
@app.route("/settitle",methods=["POST"])
def set_title():
    f=open("/home/pi/workspace/RasPi-server/title.txt","w")
    f.writes(request.form["title"])


app.run(host="0.0.0.0")
