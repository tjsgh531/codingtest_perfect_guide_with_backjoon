import sys
input = sys.stdin.readline

N = int(input())

conferences = []
for _ in range(N):
    start, end = map(int, input().split())
    conferences.append((start, end))

conferences.sort()

cur_time = 0
answer = 0
for start, end in conferences:
    # 두 회의다 할 수 있는 경우
    if cur_time <= start:
        cur_time = end
        answer += 1

    # 두 회의가 겹치는 경우
    else:
        if end < cur_time:
            cur_time = end

print(answer)
