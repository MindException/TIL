import numpy as np

# 행렬 A를 출력하는 함수
def pprint(msg, A):
    print("[[[", msg, "]]]")
    (n,m) = A.shape
    for i in range(0, n):
        line = ""
        for j in range(0,m):
            line += "{0:.3f}".format(A[i,j])+"\t"
            if j == n - 1:
                line += "|"
        print(line)
    print("")


# 가우스 조단 소거법을 수행하는 함수
def gauss(A):
    (n,m) = A.shape

    for i in range(0, n):
        #i번째 열에서 절댓값이 최대인 성분의 행 선택
        maxEI = abs(A[i, i])
        maxRow =  i
        for k in range(i+1, n):
            if abs(A[k, i]) > maxEI:
                maxEI = abs(A[k,i])
                maxRow = k

        # 현재 i번째 행과 절댓값이 최대인 행 maxRow의 행교환
        for k in range(i, m):
            tmp = A[maxRow, k]
            A[maxRow,k] = A[i,k]
            A[i,k] = tmp
        pprint(str(i+1) + "행 과" + str(maxRow+1) + "행을 교환: R" + str(i+1) + "<--> R" + str(maxRow+1), A)

        # 피벗을 1로 만들기
        piv = A[i,i]
        for k in range(i,m):
            A[i,k] = A[i,k] / piv
        pprint(str(i+1) + "행" + str(i+1) + "열 피벗을 1로 변환: R" + str(i+1) + "<- (1/" + "{0:.3f}".format(piv) + ") * " + str(i+1) + "행", A)

        # 현재 i번째 열의 i번째 행을 제외한 모든 성분을 0으로 만들기
        for k in range(0, n):
            if k != i:
                c = A[k,i]/A[i,i]
                for j in range(i, m):
                    if i == j:
                        A[k,j] = 0
                    else:
                        A[k,j] = A[k,j] - c*A[i,j]
                pprint(str(k+1) + "행" + str(i+1) + "열 성분을 0으로 변환: R" + str(k+1) + "<- -" + "{0:.3f}".format(c) + " * " + "R" +str(i+1) + " + R" + str(k+1), A)

    # Ax = b의 해 반환
    x = np.zeros(n)
    for i in range(0, n):
        x[i] = A[i, n]
    return x

matrix = np.array([[3, 6, -3, 6], [2, 7, 4, 28], [2, -6, 4, 2]])
A = matrix.astype(np.float32) # <- 이거 형 변환 안해주면 넘파이 요소 값 변경할 때 정수말고는 절대 안들어간다.

pprint("선형연립방정식 예제", A)
x = gauss(A)

# 최종 해 출력
(n, m) = A.shape
line="해:\t"
for i in range(0, n):
    line += "{0:.3f}".format(x[i]) + "\t"
print(line)

# a = np.array([-2, 3])
# a[0] = a[0] / a[1]
# print(a[0])