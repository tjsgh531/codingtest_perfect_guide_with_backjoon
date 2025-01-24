import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
opers = list(map(int, input().split()))

answers = []
def calculate(num1, num2, oper):
    # 더하기
    if oper == 0:
        return num1 + num2
    # 빼기
    elif oper == 1:
        return num1 - num2
    # 곱하기
    elif oper == 2:
        return num1 * num2
    # 나누기
    else:
        if num1 < 0:
            return -(-num1 // num2)
        else:
            return num1 // num2

def backtracking(cnt, num):
    global opers, answers

    # 백트래킹 정지 
    if cnt == N:
        answers.append(num)
        return

    # 백트래킹 반복
    cur_num = num_list[cnt]
    for i in range(4):
        oper = opers[i]
        # 사칙연산 사용가능하면 실행
        if oper > 0:
            opers[i] -= 1
            new_num = calculate(num, cur_num, i)
            backtracking(cnt+1, new_num)
            opers[i] += 1

backtracking(1, num_list[0])
print(max(answers))
print(min(answers))