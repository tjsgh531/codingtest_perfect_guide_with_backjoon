import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    r, c = map(int, input().split())
    arr.append((r, c))

# dp[i][j] : i~j번째 행렬 곱 할때 최소 곱연산 수
# opt[i][j] : i~j번째 행렬 곱 할때 최적 k
dp = [[0] * N for _ in range(N)]
opt = [[0] * N for _ in range(N)]

# 초기화
for i in range(N-1):
    j = i + 1
    dp[i][j] = arr[i][0] * arr[i][1] * arr[j][1]
    opt[i][j] = i

# dp[i][j] = min(dp[i][k] + dp[k+1][j] + arr[i][0] * arr[k][1] * arr[j][1])
# dp[i][j]의 최적의 k는 dp[i][j-1]의 최적 k ~ dp[i+1][j] 최적 k
for length in range(2, N):
    for i in range(N-length):
        j = i + length
        temp = []
        for k in range(opt[i][j-1], opt[i+1][j]+1):
            temp.append((dp[i][k] + dp[k+1][j] + arr[i][0] * arr[k][1] * arr[j][1], k))

        dp[i][j], opt[i][j] = min(temp)
    
print(dp[0][-1])

