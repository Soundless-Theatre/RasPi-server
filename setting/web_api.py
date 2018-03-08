from flask import Flask, request
from flask.ext.cors import  CORS
app = Flask(__name__)
cors=CORS(app)
f = open("./home/pi/RasPi-server/settong/input.json")
data = f.read()
f.close()
str_data = ""

<<<<<<< HEAD
@app.route("/list")
def index():
        f1 = open("/home/pi/workspace/RasPi-server/setting/input.json")
        data = f1.read()
        f1.close()
        return data
@app.route("/connect", methods=["POST"])
def try_connct():
    f2=open("/home/pi/workspace/RasPi-server/setting/pass.txt","w")
    f2.write(request.form['ssid']+" "+request.form['pass'])
    f2.close()
=======
@app.route("/list",methods=["GET"])
def index():
    return data

@app.route("/connect", methods=["POST"])
def try_connect():
    ssid = request.form['ssid']
    password = request.form['pass']
    str_data = ssid + " " + password
    writepass()
>>>>>>> develop_wifi_setting
    return "ok"

@app.route("/connect_app", methods=["POST"])
def try_conncet_app():
    app_data = request.data
    str_data = app_data.decode()
    weitepass()
    return "ok"

@app.route("/settitle",methods=["POST"])
def set_title():
<<<<<<< HEAD
    f3 = open("/home/pi/workspace/RasPi-server/title.txt","w")
    f3.write(request.form["title"])
    f3.close()
    
=======
    f=open("./home/pi/RasPi-server/setting/title.txt","w")
    f.write(request.form["title"])
    str_data = ""
    return "ok"

def writepass():
    p = open("./home/pi/RasPi-server/setting/pass.txt", "w")
    p.write(str_data)
    p.close()
>>>>>>> develop_wifi_setting

app.run(host="0.0.0.0")
