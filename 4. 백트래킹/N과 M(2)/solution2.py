import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
answer = list(combinations(range(1, N+1), M))
for item in answer:
    print(*item)