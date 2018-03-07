from flask import Flask, request
from flask.ext.cors import  CORS
app = Flask(__name__)
cors=CORS(app)
f = open("./input.json")
data = f.read()
f.close()
@app.route("/list",methods=["GET"])
def index():
    print("list request")
    return data
@app.route("/connect", methods=["POST"])
def try_connct():
    print(request.data)
    print("connect request",request.form['ssid'],request.form['pass'])
    return "ok"
@app.route("/connect_app", methods=["POST"])
def try_connct():
    app_data = request.data
    str_data = app_data.decode()
    p = open("./pass.txt", "w")
    p.write(str_data)
    p.close
    print("connect request",str_data)
    return "ok"
@app.route("/settitle",methods=["POST"])
def set_title():
    print("settitle request",request.form["title"])
    return "ok"

app.run(host="0.0.0.0")
