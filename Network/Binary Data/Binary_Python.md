# 파이썬 이진데이터

## byte 자료형
* 파이썬의 byte 자료형은 __bytes__ 와 __bytearray__ 가 있다.

### bytes
* 1바이트 단위의 값을 연속적으로 저장하는 시퀀스 자료형이다.
* 튜플과 같이 요소의 변경이 불가능한 특징이 있다.<br>

다른 언어에서는 string과 char을 구분하여서 사용하였지만 파이썬에서는 " "를 사용하여 선언 시 한 문자여도 str 자료형으로 귀속되는 것을 볼 수 있다. 그와 같이 이진 데이터에서도 1 byte의 문자인 자료형은 없고 bytes로 저장하게 된다.

```py
>>> bytes(5)    # 0이 5개 들어있는 바이트 객체 생성
b'\x00\x00\x00\x00\x00'
>>> bytes([10, 20, 30, 40, 50])    # 리스트로 바이트 객체 생성
b'\n\x14\x1e(2'
>>> bytes(b'test')    # 바이트 객체로 바이트 객체 생성
b'test'
```

### bytearray
* 1바이트 단위의 값을 연속적으로 저장하는 시퀀스 자료형이다.
* bytes 자료형과의 차이점은 리스트와 같이 요소를 변경할 수 있다.

```py
>>> x = bytearray(b'Kanada')
>>> x[0] = ord('C')    # ord는 문자의 ASCII 코드를 반환
>>> x
bytearray(b'Canada')
```

## Stream
기본적인 io 입출력 원리는 자료를 입출력하기 위한 통로인 스트림(Stream)을 만든다. 그 후 그 안에 일정 크기의 자료들을 저장 후 내용을 한 번에 전송하는데 일정 크기의 데이터를 저장하는 공간을 버퍼(buffer)라고 한다.

```py
import io

# open 스트림
f = open("test.jpg", "rb")

# iostream
bdata = f.read() # bytes 자료형을 반환한다.
iostream = io.BytesIO(data)
```

* 외부와 연결해서 가져오는 스트림은 open만 가능하다.
* open의 buffer의 크기는 buffering 매개변수로 설정이 가능하다.
* buffering : 버퍼링끄기는 0(바이너리모드에서만 동작), 라인모드는 1 (텍스트 모드에서만 가능), 고정 크기로 보내려면 임의의 바이트수를 1보다 큰 양의 수로 입력, 기본 정책은 아래와 같다.
    * 이진 파일은 고정 크기 청크로 버퍼링됩니다. 버퍼의 크기는 기본 장치의 "블록 크기"를 결정하고 다시 떨어지는 경험적 방법을 사용하여 선택됩니다 io.DEFAULT_BUFFER_SIZE. 많은 시스템에서 버퍼는 일반적으로 4096 또는 8192 바이트 길이입니다.
    * "대화식"텍스트 파일 ( isatty() 반환 되는 파일 True)은 회선 버퍼링을 사용합니다. 다른 텍스트 파일은 바이너리 파일에 대해 위에서 설명한 정책을 사용합니다.

스트림만으로는 데이터가 전송이 되지 않는다. 따라서 데이터를 읽기 위해서는 read와 write 등이 필요하다.  
여기서 주의할 부분은 readline()이다.
* readline()은 개행문자('\n')까지 읽는 특징이 있다. 하지만 ASCii에서 255 개의 문자 중 개행문자가 들어가며 그 때문에 이미지와 같은 파일을 읽었을 경우에 전부 읽어오지 못하는 경우가 있다.
* 따라서 이미지와 같은 이진 파이을 읽을 때는 read()를 사용하여 읽어야 한다.

## byte 자료형 이미지 출력

### PIL을 사용한 이미지 출력
* PIL의 __PIL.open(바이트 스트림)__ 을 통하여 이미지를 열 수 있다.

```py
import io
from PIL import Image

# open으로 이미지 열기
f = open("test.jpg", "rb")
pimg = Image.open(bf)
pimg.show()

# io.BytesIO으로 이미지 열기
iob = open("test.jpg", "rb")
data = data = f.read()
bf = io.BytesIO(data)
pimg = Image.open(bf)
pimg.show()
```
위와 같이 read를 사용하여 스트림에서 이진 data를 읽을 수 있다.

### PIL에서 cv2로 변환 및 사용하기
PIL과 cv2의 궁금적인 차이는 numpy다.
* PIL은 기본 라이브러리인 모듈이기 때문에 list를 바탕으로 구현되어 있다.
* cv2는 numpy로 구현되어 있다.<br>

따라서 cv2를 사용하기 위해서는 numpy로 변환해 주어야 한다.

```py
import cv2

f = open("test.jpg", "rb")
data = f.read()

encoded_img = np.fromstring(data, dtype = np.uint8)
img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)
cv2.imshow("image", img)
cv2.waitKey()
```

## base64
* Base64는 3byte(총24bit)를 6bit로 나누어서 4개의 문자로 표현한다.
* 따라서 기존보다 33% 이상의 메모리를 사용한다.
* 사용하는 이유는 json파일에 base64를 사용하여 이미지를 함께 보낼 수 있기 때문이다.

```py
import base64

f = open("test.jpg", "rb")
data = f.read()

edata = base64.b64encode(data)          #인코딩
ddata = base64.b64decode(edata)         #디코딩
```