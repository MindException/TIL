---
published: true
layout: single
title: "변수&메모리"
categories: 파이썬
tag: [python, 변수, 메모리, 바다코끼리 연산자]
---
대학을 다니며 주로 사용하였던 언어는 Java였다. (여담으로 졸업 작품도 안드로이드 프레임워크와 파이어베이스를 사용하였다.)<br>
공부의 기본 베이스가 c와 c++이기 때문에 자바를 사용하면서도 참조에 대한 메모리 관리를 중요하게 생각하였다.<br>
Opencv 등을 통하여 파이썬으로 코딩을 할 줄은 알지만 파이썬에 대한 이해가 부족하다고 느껴서 중요한 것만 빠르게 다시 공부해볼까 한다.<br>


## <span style = 'background-color:#dcffe4'>객체</span>

제일 중요한 것은 파이썬은 모든 것이 <span style = 'background-color:#fff5b1'>객체</span>로 래핑(wrapping) 되어있다!!<br>
Java의 경우는 a라는 Integer 객체를 10을 할당하고, b도 같은 방법으로 할당할 경우 2개의 객체가 생기는 것이 정상이다.
하지만 파이썬은 10을 가지고 있는 Integer 객체가 생성되면 다음 10을 가지고 있는 변수도 같은 객체를 참조하게 되어 <span style = "background-color:#fff5b1">1개의 객체</span>만으로 이루어져 있다.<br>
또한, int형이 객체이기 때문에 메모리 사이즈가 4byte가 아닌 24byte가 출력되는 것을 확인할 수 있다.
(여담으로 Integer 기준으로는 256까지만 같은 객체로 생성한다.)

```python
import sys

a = 10
b = 10
a is b                          #같은 곳을 참조하기 때문에 True를 반환한다.
print(id(a))                    #id를 통하여 메모리 주소를 확인할 수 있다.
byte_size = sys.getsizeof(a)    #24byte가 출력되는 것을 확인이 가능하다.
```

## <span style = 'background-color:#dcffe4'>True와 False</span>

다른 언어와 다르게 python이 false로 인식하는 경우를 모았다. if문에서 쓰이기 때문에 정리하여 보았다.

| boolean | false |
|---------|-------|
|  null   |  none |
| 정수, 부동소수점 | 0 ,  0.0 |
|빈 문자열, 리스트, 튜플, 딕셔너리 | '',  [],  (),  {} | 
| 빈 셋 | Set() |
| in | 존재하지 않는 경우 |

## <span style = 'background-color:#dcffe4'>바다코끼리 연산자 :=</span>

python에만 존재하는 독특한 연산자이다. 조건식 혹은 리스트와 같은 배열 안에서 변수를 선언하기 위하여 사용되는 연산자다
```python
a = [ x:= 1 , 2, 3, 4]
if (trigger := len(a)) > 0:
    print(a[0])                 #1이 출력되는 것을 볼 수 있다.
```