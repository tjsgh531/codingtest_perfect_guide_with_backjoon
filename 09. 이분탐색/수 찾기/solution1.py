import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

num_dict = {num : True for num in num_list}

for num in numbers:
    if num_dict.get(num):
        print(1)
    else:
        print(0)