import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement

N, M = map(int, input().split())
answer = list(combinations_with_replacement(range(1, N+1), M))
for item in answer:
    print(*item)