import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e6)
dp = [INF] * (n+1)
dp[n] = 0

# dp[i] = i 최소 연산 횟수
# dp[i] = min(dp[i*3], dp[i*2], dp[i+1]) +1

for i in range(n-1, 0, -1):
    if (i * 3) <= n and (i*2) <= n:
        dp[i] = min(dp[i*3], dp[i*2], dp[i+1]) +1
    elif i*2 <= n:
        dp[i] = min(dp[i*2], dp[i+1]) + 1
    else:
        dp[i] = dp[i+1] + 1

print(dp[1])