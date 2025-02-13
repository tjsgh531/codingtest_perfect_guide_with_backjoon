import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
stack = [] # 아직 나보다 큰 수가 오른쪽에 안나온 것들
answer = [-1] * N

for idx, num in enumerate(num_list):
    while stack and stack[-1][0] < num:
        _, idx_ = stack.pop()
        answer[idx_] = num

    stack.append((num, idx))

print(' '.join(list(map(str, answer))))



