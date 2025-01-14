import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
blanks = []

for row in range(9):
    for col in range(9):
        if board[row][col] == 0:
            blanks.append((row, col))

def check_row(num, row):
    if num in board[row]:
        return False
    else:
        return True

def check_col(num, col):
    for row in board:
        if row[col] == num:
            return False
    return True

def check_box(num, row, col):
    box_row = row // 3
    box_col = col // 3

    for row in range(box_row*3, (box_row+1)*3):
        for col in range(box_col*3, (box_col+1)*3):
            if board[row][col] == num:
                return False
    return True
        
def backtracking(cnt):
    global board

    if cnt == len(blanks):
        for row in board:
            print(*row)
        exit()
    
    blank_row = blanks[cnt][0]
    blank_col = blanks[cnt][1]
    for num in range(1, 10):
        if check_row(num, blank_row) and check_col(num, blank_col) and check_box(num, blank_row, blank_col):
            board[blank_row][blank_col] = num
            backtracking(cnt+1)
            board[blank_row][blank_col] = 0

backtracking(0)