import sys
input = sys.stdin.readline

n = int(input())
stairs = [int(input()) for _ in range(n)]

# dp[i][0] = 이전 계단을 밟고 i번째 계단을 밟을때 최댓값
# dp[i][1] = 이전 계단을 밟지 않고 i번째 계단을 밟을 때 최댓값

if n == 1:
    print(stairs[0])
else:
    dp = [[0, 0] for _ in range(n)]
    dp[0] = [stairs[0], stairs[0]]
    dp[1] = [stairs[0] + stairs[1], stairs[1]]

    for i in range(2, n):
        dp[i][0] = dp[i-1][1] + stairs[i]
        dp[i][1] = max(dp[i-2]) + stairs[i]

    print(max(dp[-1]))