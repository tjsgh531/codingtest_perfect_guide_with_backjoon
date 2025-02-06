import sys

n, m = map(int, sys.stdin.readline().split())
memory = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

total_cost = sum(cost)
dp = [0] * (total_cost + 1)

for i in range(n):
    mem = memory[i]
    c = cost[i]
    
    for j in range(total_cost, c - 1, -1):
        dp[j] = max(dp[j], dp[j - c] + mem)

# 최소 비용 찾기
for i in range(total_cost + 1):
    if dp[i] >= m:
        print(i)
        break
