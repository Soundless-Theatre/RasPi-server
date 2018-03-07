from flask import Flask, request
from flask.ext.cors import  CORS

app = Flask(__name__)
cors=CORS(app)

@app.route("/list")
def index():
        f1 = open("/home/pi/workspace/RasPi-server/setting/input.json")
        data = f1.read()
        f1.close()
        return data
@app.route("/connect", methods=["POST"])
def try_connct():
    f2=open("home/pi/workspace/RasPi-server/setting/pass.txt","w")
    f2.write(request.form['ssid']+" "+request.form['pass'])
    f2.close()
    return "ok"
@app.route("/settitle",methods=["POST"])
def set_title():
    f3 = open("/home/pi/workspace/RasPi-server/title.txt","w")
    f3.write(request.form["title"])
    f3.close()
    

app.run(host="0.0.0.0")
