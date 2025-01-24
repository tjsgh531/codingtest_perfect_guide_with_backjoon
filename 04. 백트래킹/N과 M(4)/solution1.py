import sys
input = sys.stdin.readline

N, M = map(int, input().split())
results = []

def backtracking(n):
    global results
    if len(results) == M:
        print(*results)
        return

    for i in range(n, N+1):
        results.append(i)
        backtracking(i)
        results.pop()

backtracking(1)
