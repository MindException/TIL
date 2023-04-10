
# 원반 개수, 시작점, 목적지, 경유지
def hanoi(n, start, to, mid, answer):
    if n == 1:
        return answer.append([start, to])
    hanoi(n-1, start, mid, to, answer) # 하나 적은 원반들을 목적지가 아닌 곳으로 옮긴다
    answer.append([start, to])         # 원하는 원반(마지막 원반)을 목적지로 이동
    hanoi(n-1, mid, to, start, answer) # 나머지 원반을 목적지로 이동한다.

def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer

answer = solution(2)
print(answer)