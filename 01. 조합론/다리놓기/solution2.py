import sys
input = sys.stdin.readline

T = int(input())

def solution(N, M):
    answer = 1
    for i in range(M, M-N, -1):
        answer *= i

    for i in range(N, 1, -1):
        answer //= i
    
    return int(answer)

for _ in range(T):
    N, M = map(int, input().split())
    print(solution(N, M))