import sys
input = sys.stdin.readline

N = int(input())

greeting_members = {}
answer = 0

for _ in range(N):
    text = input().strip()
    if text == 'ENTER':
        greeting_members = {}
    else:
        if greeting_members.get(text) is None:
            greeting_members[text] = True
            answer += 1

print(answer)
