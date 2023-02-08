from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def test1():                           
    return "Server Open!!"

@app.route("/hello/<username>")
def test2(username):                           
    return "Hello Flask!"

@app.route("/jsontest")
def jsontest():
    data = {'file' : 'jsontest', 'text' : 'hi! jsontest!'}
    return jsonify(data)

if __name__ == "__main__":              
    app.run(host="127.0.0.1", port="8123")