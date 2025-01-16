import sys
input = sys.stdin.readline

# dp{n} : n개의 타일을 사용하여 만들 수 있는 수
dp = {}
dp[1] = 1
dp[2] = 2

n = int(input())

for i in range(3, n+1):
    if dp.get(i) is None:
        dp[i] = (dp[i-2] + dp[i-1]) % 15746
print(dp[n])