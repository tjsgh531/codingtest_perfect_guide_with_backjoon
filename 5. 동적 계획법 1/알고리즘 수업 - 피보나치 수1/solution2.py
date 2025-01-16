import sys
input = sys.stdin.readline

n = int(input())

f = {}
for i in range(1, n+1):
    f[i] = 0

def fibonacci(n):
    global f

    f[1], f[2] = 1, 1
    for i in range(3, n+1):
        f[i] = f[i - 1] + f[i - 2];  # 코드2
    return f[n]


print(fibonacci(n), n-2)