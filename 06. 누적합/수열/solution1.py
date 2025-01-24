import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num_list = list(map(int, input().split()))

dp = [0]
for num in num_list:
    dp.append(num + dp[-1])

answer = []
for i in range(N-K+1):
    answer.append(dp[i+K]- dp[i])

print(max(answer))