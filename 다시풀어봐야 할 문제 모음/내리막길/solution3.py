import sys

sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 증가
input = sys.stdin.readline

# 입력
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    h = graph[x][y]
    # 도착
    if x == M-1 and y == N-1:
        return 1

    # 이미 왔으면
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 다음칸이 갈 수 있는 조건이라면
        if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] < h:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

dfs(0, 0)
print(dp[0][0])


