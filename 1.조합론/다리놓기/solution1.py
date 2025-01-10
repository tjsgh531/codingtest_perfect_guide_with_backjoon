import sys
input = sys.stdin.readline
from itertools import combinations

T = int(input())

def solution(N, M):
    answer = len(list(combinations(range(M), N)))
    return answer

for _ in range(T):
    N, M = map(int, input().split())
    print(solution(N, M))