import sys
input = sys.stdin.readline

N = int(input())

cur_list = []
answer = 0

def backtracking():
    global cur_list, answer

    if len(cur_list) == 2:
        answer += 1
        return

    for i in range(N):
        if i not in cur_list:
            cur_list.append(i)
            backtracking()
            cur_list.pop()

backtracking()
print(answer)