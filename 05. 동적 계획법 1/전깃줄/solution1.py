import sys
input = sys.stdin.readline

N = int(input())

lines = []
for _ in range(N):
    a, b = map(int, input().split())
    lines.append((a,b))

lines.sort()
B = [b for a, b in lines]

# 가장 긴 증가하는 부분 수열 문제로 바뀜.
dp = [1] * N # dp[i] : i번째 수를 포함한 부분 수열중 가장 긴 부분 수열의 길이

for i in range(1, N):
    cur_num = B[i]

    dp_val = 1
    for j in range(i):
        pre_num = B[j]

        if pre_num < cur_num:
            dp_val = max(dp_val, dp[j] + 1)
    dp[i] = dp_val

print(N - max(dp))