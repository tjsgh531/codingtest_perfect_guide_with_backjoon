# 시간 초과 발생
import sys
input = sys.stdin.readline

n = int(input())

fib_cnt = 0
def fib(n):
    global fib_cnt
    if n == 1 or n == 2:
        fib_cnt += 1
        return 1
    else:
        return (fib(n-1) + fib(n-2))

def fibonacci(n):
    cnt = 0
    f = [0, 1, 1]
    for i in range(3, n+1):
        cnt += 1
        f.append(f[i-1] + f[i-2])

    return f[n], cnt

fib(n)
result, cnt = fibonacci(n)
print(fib_cnt, cnt)
