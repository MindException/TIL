import io
from PIL import Image
import cv2
import numpy as np
import base64

# IOStream 형태로 만든 것
f = open("test.jpg", "rb")
data = f.read()
# print(data)
# bf = io.BytesIO(data)
# print(type(bf))

# PIL로 읽는 법
# pimg = Image.open(bf)
# pimg.show()

# cv2로 읽는 법
# data = f.read()
# print(data)

edata = base64.b64encode(data)
ddata = base64.b64decode(edata)

print(ddata)

encoded_img = np.fromstring(ddata, dtype = np.uint8)
img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)
cv2.imshow("test", img)
cv2.waitKey()

# print(f.readable())
# io_img = f.read()
# print(type(io_img))

f.close()

# pimg = Image.open(io_img)
# cv2.imshow("test", pimg)
# cv2.waitKey()