from flask import Flask, jsonify, request, render_template, make_response
from flask_cors import CORS
from werkzeug.utils import secure_filename
import cv2

app = Flask(__name__)
CORS(app)

# 라우트팅은 기본이 GET이라 methods로 POST도 추가해줘야 한다.
@app.route("/", methods=['GET','POST'])
def test1():

    # method 구분
    print(request.method)
    
    # json 받기
    # 파일이 json인지는 GET에서도 읽을 수 있다.
    if request.is_json:
        print("json 출력")
        json_data = request.get_json()      #json 형식은 Post에서만 읽을 수 있다.
        print("json 데이터: ", json_data)

    parameter_dict = request.args.to_dict()
    if len(parameter_dict)  == 0:
        if request.method == "GET":
            return render_template("07.Vue-01.html")
        else:
            data1 = {'text1' : 'POST json 넘기기', 'text2' : '성공!'}
            return make_response(jsonify(data1), 200)
    else:

        # 파라미터
        response_data = request.args.get("text")    # args는 파라미터를 받는 용도이다.
        print(response_data)
        
        # post도 파라미터가 가능하다.
        if request.method == "POST":
            print("들어옴")
            response_data = request.args.get("par_test")    # args는 파라미터를 받는 용도이다.
            print(response_data)

        # 응답 json으로 넘기기
        data2 = {'text1' : 'GET json', 'text2' : '성공!'}
        return make_response(jsonify(data2), 200)

# 라우트팅은 기본이 GET이라 methods로 POST도 추가해줘야 한다.
@app.route("/send_img", methods=['GET','POST'])
def test2():
    
    parameter_dict = request.args.to_dict()

    if len(parameter_dict)  == 0:
        if request.method == "GET":
            return render_template("07.Vue-02.html")

    if request.method == "POST":
        f = request.files['file123']  # html에서 보내는 name이랑 맞아야한다.
        f.save(secure_filename(f.filename))
        print(type(f))
        return "파일 저장 완료"


if __name__ == "__main__":              
    app.run(host="127.0.0.1", port="8123")

