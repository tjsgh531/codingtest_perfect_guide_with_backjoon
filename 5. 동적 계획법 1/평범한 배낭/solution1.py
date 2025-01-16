import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# dp[i] : 무게 i를 채울때 가치의 최댓값
dp = [0] * (K+1)

for _ in range(N):
    W, V = map(int, input().split())
    # 담을 수 없는 물건
    if W > K:
        continue

    temp = [0] * (K+1)
    temp[W] = V
    for idx, pre_v in enumerate(dp):
        # 이전에 담겨있는 것이 없으면 넘어가기
        if pre_v == 0:
            continue

        sum_w = W + idx
        sum_v = V + pre_v

        # 무게 합이 담는 한계초과시
        if sum_w > K:
            break

        temp[sum_w] = sum_v
    
    for i in range(K+1):
        dp[i] = max(dp[i], temp[i])

print(max(dp))
    

    