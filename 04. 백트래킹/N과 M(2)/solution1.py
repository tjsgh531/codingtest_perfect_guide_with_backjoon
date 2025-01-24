import sys
input = sys.stdin.readline

N, M = map(int, input().split())

results = []
def backtracking(n):
    global results
    if len(results) == M:
        print(*results)
        return

    for i in range(n+1, N+1):
        if i not in results:
            results.append(i)
            backtracking(i)
            results.pop()

backtracking(0)
