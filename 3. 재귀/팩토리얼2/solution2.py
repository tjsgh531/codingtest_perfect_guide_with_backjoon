import sys
input = sys.stdin.readline

N = int(input())
def factorial(result, n):
    if n >= N:
        return result * n
    return factorial(result * n, n+1)

answer = factorial(1, 1)
print(answer)
