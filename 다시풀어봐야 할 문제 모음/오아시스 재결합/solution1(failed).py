import sys
input = sys.stdin.readline

n = int(input())
heights = [int(input()) for _ in range(n)]

stack = [] # 오른쪽 사람이 볼 수 있는 사람들 모임 => 나보다 큰사람이 나타면 오른쪽 사람을 볼 수 없게 됨
answer = 0

for h in heights:
    if stack: # stack에 뭐가 들어있으면
        if stack[-1] > h : # 나보다 큰 경우 내 윗공기로 서로 마주 볼 가능성 있음.
            answer += 1
        else:
            temp = []
            while stack:
                pre_h = stack.pop()
                answer += 1
                if pre_h == h: # 같으면 pop하지 않고 다음것 비교 해야해
                    temp.append(pre_h)
                elif pre_h > h: # 더 크면 pop하면 안되요.
                    stack.append(pre_h)
                    stack.extend(temp)
                    break
            else:
                stack.extend(temp)
    stack.append(h)
print(answer)
