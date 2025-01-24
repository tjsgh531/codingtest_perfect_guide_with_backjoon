import sys
input = sys.stdin.readline

n = int(input())
drinks = [int(input()) for _ in range(n)]

# dp[i][0] : i번째 포도주를 마시는데 이전 포도주를 마셨을때 최댓값
# dp[i][1] : i번째 포도주를 마시는데 이전 포도주를 마시지 않았을 때 최댓값
if n == 1:
    print(drinks[0])
else:
    dp = [[0] * 2 for _ in range(n)]
    dp[0] = [drinks[0], drinks[0]]
    dp[1] = [drinks[1] + drinks[0], drinks[1]]

    for i in range(2, n):
        cur_drink = drinks[i]
        dp[i][0] = dp[i-1][1] + cur_drink
    
        if i - 3 > 0:
            dp[i][1] = max(dp[i-2] + dp[i-3]) + cur_drink
        else:
            dp[i][1] = max(dp[i-2]) + cur_drink

        
    answer = 0
    for item in dp:
        answer = max(answer, item[0], item[1])
    print(answer)
