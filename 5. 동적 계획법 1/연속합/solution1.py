import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

# dp[i] : i번째 수를 더할때 최대 연속합
dp = [num_list[0]]

for i in range(1, n):
    if dp[-1] < 0:
        dp.append(num_list[i])
    else:
        dp.append(dp[-1] + num_list[i])

print(max(dp))

