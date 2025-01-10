import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())

if N > 1:
    answer = len(list(permutations(range(N), 2)))
else:
    answer = 0

print(answer)


