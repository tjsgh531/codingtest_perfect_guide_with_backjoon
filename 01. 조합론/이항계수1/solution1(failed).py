import sys
input = sys.stdin.readline
from itertools import combinations

N, K = map(int, input().split())
answer = len(list(combinations(range(N), K)))
print(answer)