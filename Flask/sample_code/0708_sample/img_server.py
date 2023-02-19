from flask import Flask, jsonify, request, render_template, make_response, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET','POST'])
def sample():
    
    # 들어온 파라미터 확인
    parameter_dict = request.args.to_dict()

    if len(parameter_dict) == 0:
        if request.method == "GET":
            # 처음 접속한 경우
            return render_template("img_axios.html")
        else:
            f = request.files['test123']  # html에서 보내는 name이랑 맞아야한다.
            path = "./image.jpg"
            f.save(path)
            return send_file("./image.jpg", mimetype='image/png')

if __name__ == "__main__":              
    app.run(host="127.0.0.1", port="8123")