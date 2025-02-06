# 시간 초과
# pypy로 제출할 시 성공
import sys
input = sys.stdin.readline

#dp[i][j] : i~j까지 페이지를 합칠 때 최소값
def solution(n, file_sizes, file_size_sum):
    dp = [[0] * n for _ in range(n)]

    for repeat in range(n-1):
        for i in range(n-1-repeat):
            j = i+repeat+1
            temp = []
            for k in range(i, j):
                sum_i_to_j = file_size_sum[j+1] - file_size_sum[i]
                temp.append(dp[i][k]+dp[k+1][j]+sum_i_to_j)
            dp[i][j] = min(temp)
    return dp[0][-1]

T = int(input())
for _ in range(T):
    K = int(input())
    file_sizes = list(map(int, input().split()))
    
    # i~j까지 파일 합 값을 빠르게 계산하기위해 누적합 응용
    file_size_sum = [0]
    for size in file_sizes:
        file_size_sum.append(file_size_sum[-1] + size)

    # solution 시작
    print(solution(K, file_sizes, file_size_sum))
