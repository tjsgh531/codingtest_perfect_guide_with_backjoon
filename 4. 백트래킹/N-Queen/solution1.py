import sys
input = sys.stdin.readline

N = int(input())

board = []
answer = 0

def backtracking(cnt):
    global answer, board

    if cnt == N:
        answer += 1
        return
    
    for cur_col in range(N):
        for idx, col in enumerate(board):
            # 같은 열 안되요
            if cur_col == col:
                break
            # 대각선 안되요
            if abs(cur_col - col) == abs(cnt - idx):
                break
        else:
            board.append(cur_col)
            backtracking(cnt+1)
            board.pop()

backtracking(0)
print(answer)