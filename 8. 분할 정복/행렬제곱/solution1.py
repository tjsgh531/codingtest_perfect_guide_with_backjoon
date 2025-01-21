import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def array_calculator(arr_a, arr_b, c):
    n = len(arr_a)
    answer = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            for i in range(n):
                answer[row][col] += arr_a[row][i] * arr_b[i][col]
                answer[row][col] %= c
    return answer

def power(a, b, c):
    if b == 1:
        return [[item % c for item in row] for row in a]

    temp = power(a, b//2, c)
    if b % 2 == 0:
        return array_calculator(temp, temp, c)
    else:
        return array_calculator(array_calculator(temp, temp, c), a, c)

answer = power(A, B, 1000)
for row in answer:
    print(' '.join(list(map(str, row))))