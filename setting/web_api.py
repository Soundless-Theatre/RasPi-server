import lis
from flask import Flask, request
import connect
from flask.ext.cors import  CORS

app = Flask(__name__)
cors=CORS(app)

l=lis.list()

@app.route("/list")
def index():
        l.getcmd()
        f = open("/home/pi/RasPi-server/setting/input.json")
        data = f.read()
        f.close()
        return data
@app.route("/connect", methods=["POST"])
def try_connct():
    connect.con(request.form['id'],request.form['pass'])
    return "ok"
@app.route("/settitle",methods=["POST"])
def set_title():
    f=open("/home/pi/workspace/RasPi-server/title.txt","w")
    f.writes(request.form["title"])


app.run(host="0.0.0.0")
