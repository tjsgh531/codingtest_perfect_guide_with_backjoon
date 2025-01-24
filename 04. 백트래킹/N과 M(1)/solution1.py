import sys
input = sys.stdin.readline

N, M = map(int, input().split())

results = []
def backtracking():
    global results
    if len(results) == M:
        print(*results)
        return

    for i in range(1, N+1):
        if i not in results:
            results.append(i)
            backtracking()
            results.pop()
    
backtracking()

