import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) + [0] * (n-i-1) for i in range(n)]

# dp[i][j] : i번째 행의 j번째 수를 더할때 최댓값
# dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

dp = [[0] * n for _ in range(n)]
dp[0] = triangle[0]

for i in range(1, n):
    for j in range(i+1):
        if j-1 < 0:
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

print(max(dp[-1]))
            


