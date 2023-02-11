from flask import Flask, jsonify, request, render_template, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def test1():

    parameter_dict = request.args.to_dict()
    if len(parameter_dict)  == 0:
        return render_template("07.Vue-01.html")
    else:
        # json 받기
        print(request.is_json) # json으로 넘어오나 확인용

        # 파라미터
        response_data = request.args.get("text")    # args는 파라미터를 받는 용도이다.
        print(response_data)

        # 응답 json으로 넘기기
        data2 = {'text1' : 'json 넘기기', 'text2' : '성공!'}
        return make_response(jsonify(data2), 200)

if __name__ == "__main__":              
    app.run(host="127.0.0.1", port="8123")

