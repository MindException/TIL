from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def test1():                           
    return "Server Open!!"

@app.route("/id_test/<username>")
def test2(username):
    if username == "admin":
        return_data = {"auth" : 'success'}
    else:
        return_data = {"auth" : "failed"}

    return jsonify(return_data)

@app.route("/jsontest")
def jsontest():
    data = {'file' : 'jsontest', 'text' : 'hi! jsontest!'}
    return jsonify(data)

@app.route("/login")
def login_test():

    username = request.args.get('id')
    passwd = request.args.get('password')

    if username == "admin":
        return_data = {"auth" : 'success'}
        if passwd == "1234":
            return_data = {"auth" : 'success'}
        else:
            return_data = {"auth" : "failed"}
    else:
        return_data = {"auth" : "failed"}

    return jsonify(return_data)

if __name__ == "__main__":              
    app.run(host="127.0.0.1", port="8123")