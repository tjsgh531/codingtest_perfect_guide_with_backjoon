import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

num_count = Counter(num_list)

for num in numbers:
    print(num_count[num], end=' ')