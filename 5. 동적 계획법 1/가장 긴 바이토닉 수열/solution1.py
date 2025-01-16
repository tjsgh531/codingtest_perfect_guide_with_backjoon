import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

def get_asc_dp(num_list):
    # dp[i] : i번째 수를 포함한 가장 긴 증가하는 부분수열 길이
    dp = [1] * N

    for i in range(1, N):
        cur_num = num_list[i]
        max_dp_val = 1

        for j in range(i):
            pre_num = num_list[j]
            if pre_num < cur_num:
                max_dp_val = max(max_dp_val, dp[j] + 1)

        dp[i] = max_dp_val

    return dp

asc_dp = get_asc_dp(A)
des_dp = get_asc_dp(A[::-1])[::-1]

answer = 0
for asc_elem, des_elem in zip(asc_dp, des_dp):
    answer = max(answer, asc_elem + des_elem)
print(answer-1)
