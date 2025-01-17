# 시간 초과
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))

# dp[i] : i번째 수 까지 수의 합
dp = [0]
for num in num_list:
    dp.append(dp[-1] + num)

answer = 0
for i in range(1, N+1):
    for j in range(i):
        if (dp[i] - dp[j]) % M == 0:
            answer += 1
print(answer)