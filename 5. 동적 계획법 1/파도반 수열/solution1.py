import sys
input = sys.stdin.readline

dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
# dp[i] = dp[i-2] + dp[i-3]

T = int(input())
for _ in range(T):
    N = int(input())
    length = len(dp)

    for i in range(length, N+1):
        dp.append(dp[i-3] + dp[i-2])
        
    print(dp[N])