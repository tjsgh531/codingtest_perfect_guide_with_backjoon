import sys
input = sys.stdin.readline

N, K = map(int, input().split())
answer = 1

for i in range(N, N-K, -1):
    answer *= i

for i in range(1, K+1):
    answer /=i

print(int(answer))