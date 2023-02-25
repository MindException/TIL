import cv2
import base64
import io
from PIL import Image
import numpy as np
from flask_socketio import emit, SocketIO
from flask import Flask, render_template
from flask_cors import CORS


app = Flask(__name__, template_folder="templates")
CORS(app)
sio = SocketIO(app)

@sio.on('image')
def image(data_image):

    print(type(data_image))
    data_image = data_image.split(",")[1]
    # print("전: ", type(data_image))
    # sbuf = io.StringIO() # 문자열을 파일 객체처럼 만든다.
    # sbuf.write(data_image)
    # print("후: ", type(data_image))
    b = io.BytesIO(base64.b64decode(data_image))
    # 당연하겠지만 타입:  <class 'bytes'>으로 base64는 출력한다.
    # b는 <class '_io.BytesIO'>를 출력한다.
    print("타입: ", type(b))
    pimg = Image.open(b)

    # DO WHATEVER IMAGE PROCESSING HERE{
    frame = cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)
    frame = cv2.flip(frame, flipCode=0)
    imgencode = cv2.imencode('.jpg', frame)[1]
    #}

    stringData = base64.b64encode(imgencode).decode('utf-8')
    b64_src = 'data:image/jpeg;base64,'
    stringData = b64_src + stringData
    emit('response_back', stringData)

@app.route("/")
@app.route("/home")
def index():
    return render_template("video_test.html")


if __name__ == "__main__":
    sio.run(app, host="127.0.0.1", port="8123", debug=True)