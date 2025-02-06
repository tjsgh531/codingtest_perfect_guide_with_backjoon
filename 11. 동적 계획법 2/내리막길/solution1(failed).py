import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

dx = [1, -1, 0, 0] 
dy = [0, 0, 1, -1] 

def bfs():
    answer = 0
    q = deque([(0, 0, board[0][0])])

    while q:
        cur_x, cur_y, cur_h = q.popleft()

        # 도착
        if cur_x == (M-1) and cur_y == (N-1):
            answer += 1
            continue

        for i in range(4):
            nx = cur_x + dx[i] # 다음 행
            ny = cur_y + dy[i] # 다음 열

            # board 밖이면 안됨
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            # height 가 낮은것만
            if board[nx][ny] < cur_h:
                q.append((nx, ny, board[nx][ny]))
    
    return answer

print(bfs())
    