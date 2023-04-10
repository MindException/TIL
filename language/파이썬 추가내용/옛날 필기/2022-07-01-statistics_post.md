---
layout: single
title: "1.기초 판다스"
categories: 통계
tag: [python, pandas]
---

파이썬을 R과 같이 데이터를 분석하기 위해 사용하는 API로 R에 대한 선수 지식이 있다면 보기 편할 것이다.<br>

## <span style = 'background-color:#dcffe4'>시리즈(series)와 데이터 프레임(dataframe)</span>
시리즈는 하나의 열이다. R의 벡터라고 생각하는 편이 쉽다. 여러 개의 열을 바인드(R의 cbind)하면 행과 열이 된다.<br>
우리는 이와같이 행과 열이 된 시퀀스를 <span style = "background-color:#fff5b1">데이터 프레임</span>이라고 한다.

```python
import pandas as pd

pd.DataFrame(data = None, index = None, columns = None ,dtype = None, copy = False)         #defualt 값
```

* <span style = "background-color:#fff5b1">data</span>는 list, tuple, dict와 같은 시퀀스 자료형(배열)를 매개 변수로 받아서 데이터 프레임으로 만든다.
* <span style = "background-color:#fff5b1">index</span>는 행의 이름이다. 대부분 0,1,2... 으로 가지만 문자열로도 가능하다.
* <span style = "background-color:#fff5b1">columns</span>는 열의 이름이다.
* <span style = "background-color:#fff5b1">dtype</span>는 데이터프레임에 들어가는 자료형을 지정한다. 하지만 데이터프레임 자체가 여러 자료형을 다음 시퀀스들을 바인드 한 것으로 특수한 경우 이외에는 잘 안쓰인다.
* <span style = "background-color:#fff5b1">copy</span>는 얕은 복사(False)와 깊은 복사(True)다. 좀 더 쉽게 설명하면 얕은 복사로 이루어진 데이터프레임은 기존에 힙메모리에 있던 데이터를 참조하는 형태로 기존 데이터가 수정되면 자료가 같이 변동하는 방면, 깊은 복사는 힙메모리에 데이터를 새로 만들어서 복사하는 형태로 기존 데이터가 수정이되어도 데이터프레임에 변동이 없다.

```python
#사용 예시
import pandas as pd

list1 = [[x,y] for x,y in zip(range(1,5),range(5,9))]
pd1 = pd.DataFrame(data = list1)
pd1.columns = ['열이름1', '열이름2']
pd1.index = ['행이름1', '행이름2', '행이름3', '행이름4']
```

| \ | 열이름1  | 열이름2|
|:---:|:---:|:---:|
|행이름1  | 1 | 5 |
|행이름2  | 2 | 6 |
|행이름3  | 3 | 7 |
|행이름4  | 4 | 8 |

---
R을 사용하다 보면 행과 열에 names()로 이름을 지정한 경험이 있을 것이다.<br>
파이썬에도 존재하며 column에 이름을 붙이는 것은 <span style = "background-color:#fff5b1">딕션어리(dictionary)</span>를 사용하여 좀 더 편하게 할 수 있다.

```python
import pandas as pd

#요알변 색상 데이터프레임
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
row_index = [x for x in range(1,8)]

day_color_df = pd.DataFrame(data = {'day':days, 'color':colors}, index = row_index)
```

| \ | day  | color|
|:---:|:---:|:---:|
|1  | Monday | red |
|2  | Tuesday | orange |
|3  | Wednesday | yellow |
|4  | Thursday | green |
|5  | Friday | blue |
|6  | Saturday | indigo |
|7  | Sunday | purple |

위와 같이 딕션어리의 키값이 column들의 이름이 된 것을 볼 수 있다.<br>
열을 호출할 경우에는 딕션어리와 똑같이 열의 이름을 키라고 생각하고 호출하면 된다.<br>
위의 코드에서 한다면 아래와 같이 한다.
~~~python
day_color_df['color']     #color 시리즈를 호출한다.
~~~

그렇다면 행도 호출하는 것이 궁금할 것이다.<br>
행을 호출하는 방법은 2가지가 있는데 여기서<br>
여기서 생각하는 인덱스는 기존에 생각하는 인덱스와 조금 다르다. 컴퓨터공학과에 나와서 맨 처음 인덱스라는 말을 들으면 아마 배열의 인덱스가 떠오르며 0,1,2,3.... 을 생각한다.<br>
하지만 데이터프레임에서의 인덱스는 말 그대로의 뜻으로 row들의 이름을 뜻한다. 따라서 아래의 예제를 보며 이해를 도운다.

~~~python
#인덱스를 기준으로 행 데이터 추출
day_color_df.loc[1]                 # Monday, red 추출
#행(raw) 번호를 기준으로 행 데이터 추출
day_color_df.iloc[1]                # Tuesday, orange 추출
~~~

위와 같이 평소 우리가 생각하는 배열의 인덱스는 <span style = "background-color:#fff5b1"> iloc </span>이라고 생각하면 편하다.

## <span style = 'background-color:#dcffe4'>조회</span>

*추후 추가예정

## <span style = 'background-color:#dcffe4'>테이블 탐색</span>

*추후 추가예정