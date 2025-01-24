import sys
input = sys.stdin.readline

n = int(input())

# dp[i][j] : i자리수 수에 일의 자리가 j인 계단수 개수 

dp = [[0] * 10 for _ in range(n)]
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, n):
    for j in range(10):
        if (j-1 >= 0) and (j+1) < 10:   
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        elif j-1 >= 0:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j+1]

print(sum(dp[-1]) % 1000000000)