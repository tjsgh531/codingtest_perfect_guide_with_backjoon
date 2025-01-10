import sys
input = sys.stdin.readline

N = int(input())

dance_members = {'ChongChong':True}
answer = 1
def check_dance_member(mem1, mem2):
    global dance_members, answer

    # mem1이 춤추는 멤버이고 mem2는 춤추지 않았다면
    if dance_members.get(mem1) and (dance_members.get(mem2) is None):
        dance_members[mem2] = True
        answer += 1

    # mem2는 춤추는 멤버이고 mem1이 춤추지 않았다면
    elif (dance_members.get(mem1) is None) and dance_members.get(mem2):
        dance_members[mem1] = True
        answer += 1

for _ in range(N):
    mem1, mem2 = input().split()
    check_dance_member(mem1, mem2)

print(answer)
