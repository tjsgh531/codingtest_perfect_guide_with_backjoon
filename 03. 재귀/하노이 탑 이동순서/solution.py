import sys
input = sys.stdin.readline

N = int(input())

def hanoi(n , start, end):
    if n == 1:
        print(start, end)
        return

    mid = [i for i in range(1, 3+1) if (i != start) and (i!=end)]
    mid = mid[0]
    hanoi(n-1, start, mid)
    hanoi(1, start, end)
    hanoi(n-1, mid, end)
    

hanoi(N, 1, 3)