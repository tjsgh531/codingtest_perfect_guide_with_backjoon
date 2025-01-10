# 리스트를 이용하면 시간초과가 발생한다.
import sys
input = sys.stdin.readline

N = int(input())

greeting_members = []
answer = 0

for _ in range(N):
    text = input().strip()
    if text == 'ENTER':
        greeting_members = []
    else:
        if text in greeting_members:
            greeting_members.append(text)
            answer += 1

print(answer)
