---
published: true
layout: single
title: "시퀀스 자료형(배열) - 리스트, 튜플"
categories: 파이썬
tag: [python, 배열, 시퀀스, 리스트, 튜플]
---

파이썬에서는 쉽게 4가지의 배열이 있다. list, tuple, dictionary, set가 있다.<br>
그 중, 먼저 리스트와 튜플을 소개해볼까 한다.

## <span style = 'background-color:#dcffe4'>리스트(list)</span>
파이썬에서 사용하는 일반적인 배열이며, 동적 배열이다.
동적 배열을 사용하기 위하여 간단한 ADT(Abstract Data Type)의 연산들을 잠깐 살펴볼까 한다.

```python
test_list = []
#1. 빈 배열 확인
bool(test_list)              #[]는 false를 반환한다.
#2. 원소 추가
for x in range(1,6):
    test_list.append(x)      #원소 x를 추가
#3. 원소 삽입
test_list.insert(2, 3)      
test_list.insert(4, 3)       #1233345과 같은 형태로 만든다.
#4. 마지막 원소 삭제
test_list.pop()              #123334
#5. 인덱스 위치 원소 삭제
test_list.pop(2)
test_list.pop(2)
test_list                    #1234
```
여담으로 항목 수는 len()을 사용하여 반환한다.

### 정렬
자바에서 ArrayList를 사용할 경우 정렬이 필요하면 .sorted()를 사용하여서 정렬하였다. (퀵정렬로 이루어진 것으로 알고 있다.)<br>
주로 객체들이 가지고 있는 시간을 최신순으로 정렬하기 위하여 많이 사용하였는데 파이썬에서 객체 정렬은 추후에 설명하겠다.
 ```python
#객체 1
test_list1 = [x for x in range(1,6) if x%2 == 0]         #컴프리핸션을 통하여 2,4 저장
#객체 2
test_list2 = [1,3,5]                                     # 1,3,5 저장
#리스트 병합
test_list = test_list1 + test_list2                      # 2,4,1,3,5의 형태
#정렬
result_list = sorted(test_list)                          #리스트의 정렬된 복사본을 반환한다.
test_list.sort()                                         #리스트를 내부적으롤 정렬한다.
```

### 시퀀스 순회 - zip, 언패킹
zip() 함수는 여려 시퀀스를 병렬로 순회하는 것이다. 쉽게 말하자면 여러 배열들의 같은 인덱스에 있는 요소들을 엮어주는 역할이다.<br>
동일 개수로 이루어진 자료형을 묶어주며 만약 개수가 다르다면 짝이 없는 인덱스 부분부터 나머지를 버린다.<br>
요소들은 <span style = "background-color:#fff5b1">튜플</span>로 묶어서 반환되어진다. (요소들은 리스트, 튜플, 딕션어리로 패킹이 가능하다.)<br>
zip에 대해서 설명하기 전에 짧게 패킹(packing)과 언패킹(unpacking)에 대하여 소개하여 볼려한다.<br>
```python
list = [1,2,3]  #패킹
a,b,c = list    #언패킹 - 순서대로 저장
total = a+b+c   #6
```
위와 같이 패킹은 객체들을 엮어주는 것이고, 언패킹은 엮어진 객체들을 나누어 준다고 생각하면 편하다.<br>
따라서 zip과 언패킹을 같이 활용한다면 아래와 같이 가능하다.
```python
#요일별 색상 출력
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
for day, color in zip(days, colors):
    print(day, 'is', color)
```

### 리스트 비교
자바를 사용하며 if문에서 제일 많이 사용한 조건은 같은 문자열인지 비교하는 조건이다.<br>
자바에서 <span style = "background-color:#fff5b1">"=="</span>를 사용하게 된다면 같은 메모리 주소인지 확인하는 조건이되어 .equals()를 사용하였다.<br>
하지만 파이썬에서는 <span style = "background-color:#fff5b1">"=="</span>를 사용하여 같은 문자열인지 비교가 가능하다.


## <span style = 'background-color:#dcffe4'>튜플(tuple)</span>
리스트에서 수정을 못하게 막은 배열을 튜플이라고 이해하는 것이 편하다. 그렇기 때문에 append(), insert()등과 같은 함수가 없어서 더 적은 공간을 사용한다.<br>
다양한 생성 방법이 있어서 비일관적이라고 볼 수도 있지만 실수로 튜플의 항목이 손상될 걱정이 없는 것이 큰 장점이다.<br>
여담으로 튜플은 컴프리핸션이 없다. (작동하는 것은 제너레이터 컴프리헨션으로 다른 것이다.)

```python
tuple1 = (1,2,3,4)                              #1,2,3,4
tuple2 = tuple([x for x in range(5,9)])         #5,6,7,8
all_tuple = tuple1 + tuple2                     #1~8
```

<span style = 'background-color:#ffdce0'>(주의)</span> 튜플은 한 개 선언 시 무조건 (요소, )로 ' , '를 붙여서 선언하여야 한다. 안하면 문자열로 선언된다.
