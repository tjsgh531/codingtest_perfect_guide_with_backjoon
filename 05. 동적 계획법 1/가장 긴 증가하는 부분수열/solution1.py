import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# dp[i] : i번째 수를 포함 했을 때 부분수열의 길이 최댓값
dp = [1] * N

for i in range(1, N):
    cur_num = A[i]

    max_dp_val = 1
    for j in range(i):
        pre_num = A[j]
        
        # 이전 값 보다 크면
        if pre_num < cur_num:
            max_dp_val = max(max_dp_val, dp[j]+1)

    dp[i] = max_dp_val

print(max(dp))

