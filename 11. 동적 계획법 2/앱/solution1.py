import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bites = list(map(int, input().split()))
costs = list(map(int, input().split()))

# dp[i] : i비용을 사용하여 확보할 수 있는 공간의 최대값
max_cost = sum(costs)
dp = [-1] * (max_cost + 1)

for bite, cost in zip(bites, costs):
    # cost가 0인것은 삭제하는것이 무조건 좋다!
    if cost == 0:
        M -= bite # 삭제하면 목표 M이 줄어든다.

        # cost가 0인것으로도 충분한 공간이 확보된다면 더이상 체크할 필요가 없다.
        if M <= 0 :
            print(0)
            exit()
        continue
    
    # cost가 0이 아닌경우
    for i in range(max_cost-cost, 0, -1):
        if dp[i] != -1:
            dp[i+cost] = max(dp[i+cost], dp[i] + bite)
    
    dp[cost] = max(dp[cost], bite)

for cost, size in enumerate(dp):
    if size >= M:
        print(cost)
        break