import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
dp = [0]

for num in num_list:
    dp.append(dp[-1] + num)

for _ in range(M):
    i, j = map(int, input().split())
    print(dp[j] - dp[i-1])