import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

def count_small_num(mid):
    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid//i, N)
    return cnt

def binary_search():
    left = 1
    right = min(int(10e9), N**2)

    answer = 0
    while left <= right:
        mid = (left+right)//2
        cnt = count_small_num(mid)

        if cnt >= K: # mid 보다 작은 수들이 많다. => mid를 작게 만들어야함 => right를 당김
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

print(binary_search())