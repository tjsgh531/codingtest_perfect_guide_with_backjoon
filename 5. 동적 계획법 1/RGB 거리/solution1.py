import sys
input = sys.stdin.readline

N = int(input())
prices = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j] : i번째 집을 j색으로 칠 할때 최솟값
# dp[i][j] = min(dp[i-1][k], dp[i-1][h]) + prices[i][j]
dp = [[0] * 3 for _ in range(N)]
dp[0] = prices[0]

for i in range(1, N):
    for j in range(3):
        another_colors = [k for k in range(3) if k != j]
        dp[i][j] = min(dp[i-1][another_colors[0]], dp[i-1][another_colors[1]]) + prices[i][j]

print(min(dp[-1]))