import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
answer = len(list(permutations(range(N), N)))
print(answer)
