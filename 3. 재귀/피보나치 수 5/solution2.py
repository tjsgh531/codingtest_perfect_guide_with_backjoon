import sys
input = sys.stdin.readline

n = int(input())

def fibo(k):
    if k == 0:
        return 0
    elif k == 1:
        return 1

    return fibo(k-1) + fibo(k-2) 

answer = fibo(n)
print(answer)
    
