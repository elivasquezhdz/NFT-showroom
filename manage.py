from flask import Flask,render_template
#from flask import  jsonify, flash,request, Flask, make_response,redirect,
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/1")
def home1():
    return render_template("1.html")


@app.route("/test")
def test():
    return render_template("test.html")

if __name__ == '__main__':
    app.run(debug=True,port=80,host="0.0.0.0")