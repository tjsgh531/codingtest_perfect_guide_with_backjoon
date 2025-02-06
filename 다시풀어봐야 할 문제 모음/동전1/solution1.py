import sys
input = sys.stdin.readline

n, k = map(int, input().split())  # n: 동전 종류 수, k: 목표 금액
coins = [int(input()) for _ in range(n)]  # 동전 종류 입력

dp = [0] * (k + 1)
dp[0] = 1  

for coin in coins:
    print("coin : ", coin)
    for amount in range(coin, k + 1):
        dp[amount] += dp[amount - coin]
        print(dp)
    print("-" * 100)
print(dp[k]) 
