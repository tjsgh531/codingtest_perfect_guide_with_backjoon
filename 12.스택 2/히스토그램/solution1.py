import sys
input = sys.stdin.readline

N = int(input())
hist = [int(input()) for _ in range(N)]
hist.append(0)

answer = 0
stack = [] # 아직 자기보다 작은 막대를 못 만남. (높이, 왼쪽 최소 idx)
for idx, num in enumerate(hist):
    
    left_idx = idx
    while stack and stack[-1][0] > num: # 자기보다 작은 막대가 나타났다!
        h, left_idx = stack.pop()
        answer = max(answer, (idx-left_idx) * h)
    stack.append((num, left_idx))

print(answer)

