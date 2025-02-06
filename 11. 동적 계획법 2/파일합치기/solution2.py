import sys
input = sys.stdin.readline

def solution(n, file_sizes, file_size_sum):
    dp = [[0] * n for _ in range(n)]  # 최소 비용 DP 테이블
    opt = [[0] * n for _ in range(n)]  # 최적 k 값 저장

    for i in range(n-1):
        dp[i][i+1] = file_sizes[i] + file_sizes[i+1]
        opt[i][i+1] = i

    for length in range(2, n):  # 부분 길이 2부터 시작
        for i in range(n - length):
            j = i + length
            dp[i][j] = float('inf')

            # 최적 k 범위를 줄여서 탐색
            k_start, k_end = opt[i][j-1], opt[i+1][j]
            for k in range(k_start, k_end + 1):
                cost = dp[i][k] + dp[k+1][j] + file_size_sum[j+1] - file_size_sum[i]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    opt[i][j] = k  # 최적 k 저장

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

