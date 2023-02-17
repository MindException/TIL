from flask import Flask, jsonify, request, render_template, make_response, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET','POST'])
def sample():
    
    # 들어온 파라미터 확인
    parameter_dict = request.args.to_dict()

    # 반환 json 양식
    text_dict = {}

    print("양식:", request.method)

    if len(parameter_dict) == 0:
        if request.method == "GET":
            # 처음 접속한 경우
            return render_template("test_axios.html")
        else:
            # POST로 받은 경우
            print(request.files.get)
            f = request.files['test123']  # html에서 보내는 name이랑 맞아야한다.
            # f = request.form.get("test123") # form 태그는 이게 맞다.
            print(type(f))
            path = "./image.jpg"
            f.save(path) # 파일이 저장된다. (단, 한글 파일 불가능)
            # image/형식 설정 가능
            return send_file("./flask_img.png", mimetype='image/png')
    else:
        #파라미터 받은 경우
        response_data = request.args.get("text")       #html 파라미터 확인하기
        text_dict = {"text" : response_data + " 가 전송에 성공하였습니다."}
        return jsonify(text_dict)

if __name__ == "__main__":              
    app.run(host="127.0.0.1", port="8123")