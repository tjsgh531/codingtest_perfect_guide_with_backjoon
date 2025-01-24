import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

num_dict = {}
for num in num_list:
    if num_dict.get(num):
        num_dict[num] += 1
    else:
        num_dict[num] = 1

answer = []
for num in numbers:
    if num_dict.get(num):
        answer.append(num_dict[num])
    else:
        answer.append(0)
print(' '.join(list(map(str, answer))))
