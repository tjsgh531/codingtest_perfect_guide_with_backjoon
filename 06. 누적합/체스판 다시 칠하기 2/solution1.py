import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [input().strip() for _ in range(N)]

# start_b_board
# start_w_board
def start_b_board():
    change_board = [[0] * (M+1)]
    for row_idx, row in enumerate(board):
        new_row = [0]
        for col_idx, ele in enumerate(row):
            # 행 인덱스 + 열 인덱스 값이 짝수인데 B가 안 들어가 있으면 바꿔야함.
            if (row_idx + col_idx) % 2 == 0 and ele == 'W':
                item = change_board[-1][col_idx+1] + new_row[-1] - change_board[-1][col_idx] + 1
            # 행 인덱스 + 열 인덱스 값이 홀수인데 W가 안들어가 있으면 바꿔야함
            elif (row_idx + col_idx) % 2 == 1 and ele == 'B':
                item = change_board[-1][col_idx+1] + new_row[-1] - change_board[-1][col_idx] + 1
            else:
                item = change_board[-1][col_idx+1] + new_row[-1] - change_board[-1][col_idx]
            new_row.append(item)
        change_board.append(new_row)

    return change_board

def start_w_board():
    change_board = [[0] * (M+1)]
    for row_idx, row in enumerate(board):
        new_row = [0]
        for col_idx, ele in enumerate(row):
            # 행 인덱스 + 열 인덱스 값이 짝수인데 W가 안 들어가 있으면 바꿔야함.
            if (row_idx + col_idx) % 2 == 0 and ele == 'B':
                item = change_board[-1][col_idx+1] + new_row[-1] - change_board[-1][col_idx] + 1
            # 행 인덱스 + 열 인덱스 값이 홀수인데 W가 안들어가 있으면 바꿔야함
            elif (row_idx + col_idx) % 2 == 1 and ele == 'W':
                item = change_board[-1][col_idx+1] + new_row[-1] - change_board[-1][col_idx] + 1
            else:
                item = change_board[-1][col_idx+1] + new_row[-1] - change_board[-1][col_idx]
            new_row.append(item)
        change_board.append(new_row)

    return change_board

def cal_minimum_change(change_board):
    # (i, j) ~ (i+K, j+k)까지를 체스판으로 했을 때 바뀌어야하는 총 합
    answer = int(1e9)
    for i in range(N-K+1):
        for j in range(M-K+1):
            result = change_board[i+K][j+K] - change_board[i+K][j] - change_board[i][j+K] + change_board[i][j]
            answer = min(answer, result)
    return answer


b_change_board = start_b_board()
w_change_board = start_w_board()

b_answer = cal_minimum_change(b_change_board)
w_answer = cal_minimum_change(w_change_board)
print(min(b_answer, w_answer))
