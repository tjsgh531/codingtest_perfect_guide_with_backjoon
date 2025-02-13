import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
num_list = list(map(int, input().split()))

answer = [-1] * N
num_count_dict = Counter(num_list)
stack = [] # 아직 등장횟수가 자신 보다 더 많은 값 못만난 모임. (등장 횟수, idx)

# 등장 횟수가 더 많으면서 오른쪽 중 가장 왼쪽에 있는 수
for idx, num in enumerate(num_list):
    cnt = num_count_dict[num]

    while stack and stack[-1][0] < cnt:
        _, idx_ = stack.pop()
        answer[idx_] = num
    stack.append((cnt, idx))

print(' '.join(list(map(str, answer))))

