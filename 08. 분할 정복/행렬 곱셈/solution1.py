import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)] 

# 행렬 계산
def calculate(row, col):
    answer = 0
    for r, c in zip(row, col):
        answer += (r*c)

    return answer

# 열과 행 바꾸기
def reverse_array(array, row, col):
    answer = [[0] * row for _ in range(col)]

    for row_idx, row in enumerate(array):
        for col_idx, val in enumerate(row):
            answer[col_idx][row_idx] = val
    
    return answer

reversed_B = reverse_array(B, M, K)
answer = []

# 행렬 계산
for row in A:
    for col in reversed_B:
        temp = calculate(row, col)
        answer.append(temp)

# 결과 출력
for i in range(N):
    print(' '.join(list(map(str, answer[i*K:(i+1)*K]))))
