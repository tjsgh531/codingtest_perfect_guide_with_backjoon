import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

answer = 0
for coin in coins[::-1]:
    if K >= coin:
        times = K // coin
        K -= (times * coin)
        answer += times
    
    if K == 0:
        break

print(answer)