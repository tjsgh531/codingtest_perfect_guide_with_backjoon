import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
# dp[i][j] : (0, 0) 부터 (i, j)까지 합
dp = [[0] * (N+1)]

for row in range(N):
    temp_row = [0]
    for col in range(N):
        cur_num = board[row][col]
        cur_sum_num = temp_row[-1] + dp[-1][col+1] + cur_num - dp[-1][col]
        temp_row.append(cur_sum_num)
    dp.append(temp_row)

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    answer = dp[x2][y2] + dp[x1-1][y1-1] - dp[x1-1][y2] - dp[x2][y1-1]
    print(answer)