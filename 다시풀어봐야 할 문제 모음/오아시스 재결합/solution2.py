import sys
input = sys.stdin.readline

n = int(input())
heights = [int(input()) for _ in range(n)]

stack = [] # 오른쪽을 볼 수 있는 사람들 저장
answer = 0

for h in heights:
    count = 1  # 같은 키를 가진 사람의 개수
    
    while stack and stack[-1][0] <= h: # 이전 키가 현재보다 작으면 팝/ 같으면 하나로 취급시킬 생각
        pre_h, pre_count = stack.pop()
        answer += pre_count  # pop되는 사람들은 지금 사람을 볼 수 있음

        if pre_h == h:
            count += pre_count  # 같은 키라면 그룹을 합침

    if stack:
        answer += 1  # 현재 사람은 스택의 top과 서로 볼 수 있음

    stack.append((h, count))  # (키, 같은 키 사람 수) 형태로 저장

print(answer)
