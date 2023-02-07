---
published: true
layout: single
title: "시퀀스 자료형(배열) - 딕션어리, 셋"
categories: 파이썬
tag: [python, 배열, 시퀀스, 딕션어리, 셋]
---

## <span style = 'background-color:#dcffe4'>딕션어리(dictionary)</span>
자바와 같은 언어에서는 해시(hash), 해시맵(hashmap)으로 부르며, 파이썬에서는 <span style = "background-color:#fff5b1">딕트(dict)</span>라고 부른다.<br>
키:값(key:value)의 형태로 이루어져 있으며, 파이썬에서 특이한 점은 키는 대부분 문자열로 이루어져 있는데 모든 것을 객체화 시킨 파이썬 입장에서는 다른 타입(정수, 부동소수점, 불리언, 튜플 등)도 가능하다. 실제로 문자열 외에 다른 것을 키값으로 쓸지는 잘 모르겠다.<br>
값을 얻고 싶은 경우에는 <span style = "background-color:#fff5b1">[   ]</span>에 인덱스가 아닌 <span style = "background-color:#fff5b1">키 값</span>을 입력하면 된다.

```python
#요알변 색상 딕션어리
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
day_color_dict = {day:color for day, color in zip(days, colors)}    #기본 { } 딕트 선언

#변환
#1. 두 글자인 문자열
sample_tuple = ("ab", "cd", "ef")                                   #문자가 3개 이상이면 에러가 발생한다.
dict(sample_tuple)
#2. 두 항목으로 구성된 시퀀스
sample_list = [("Monday", 'red'), ('Thursday', 'green'), ('Sunday', 'purple')]
dict(sample_list)
```
당연히 하나의 키에는 하나의 값임으로 키는 고유한 값이여야 한다.<br>

딕션어리를 사용할 경우, 자주 사용하고 중요시하는 것이 병합(merge)가 아닐까 생각한다.

*추후 추가 예정
