# re를 사용한 해결법
import sys
input = sys.stdin.readline
import re

problem = input().strip()
num_list = list(map(int, re.split(r'[+-]', problem)))
opers = re.findall(r'[+-]', problem)

answer = num_list[0]
for idx, oper in enumerate(opers):
    if oper == '-':
        answer -= sum(num_list[idx+1:])
        break
    else:
        answer += num_list[idx+1]
print(answer)