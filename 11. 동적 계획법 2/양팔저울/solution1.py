import sys
input = sys.stdin.readline

N = int(input())
weights = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

# dp[i] : i 무게를 측정 가능
max_weight = sum(weights)
dp = [False] * (max_weight+1)
dp[-1] = True

# visited{weight : weight_sum} weight 무게추로 weight_sum에서 측정한 적 있음
visited = {w : [] for w in set(weights)}

for w in weights:
    temp = []
    for weight_sum in range(sum(weights), 1, -1):
        if dp[weight_sum]:
            # 이미 해당 무게로 측정한 적 있는 경우
            if weight_sum in visited[w]: 
                continue
            # 측정한 적이 없다면
            else:
                visited[w].append(weight_sum)
                temp.append(weight_sum - w)
                temp.append(weight_sum - 2*w)

    for temp_w in temp:
        if temp_w >= 0:
            dp[temp_w] = True

for t in targets:
    if max_weight < t:
        print('N', end=" ")
    else:
        if dp[t]:
            print('Y', end=" ")
        else:
            print('N', end=" ")
        



