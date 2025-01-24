# 시간 초과
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    cur_num = A[i]
    for j in range(i):
        pre_num = A[j]

        if pre_num < cur_num:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))