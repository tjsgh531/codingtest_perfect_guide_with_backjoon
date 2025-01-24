import sys
input = sys.stdin.readline

def merge_sort(A):
    global cnt
    if len(A) == 1:
        return A

    end = len(A)
    mid = (len(A)+1) // 2

    left_A = merge_sort(A[:mid])
    right_A = merge_sort(A[mid:])

    cur_left = 0
    cur_right = 0
    temp = []

    while (cur_left < len(left_A)) and (cur_right < len(right_A)):
        if left_A[cur_left] <= right_A[cur_right]:
            temp.append(left_A[cur_left])
            cnt += 1
            check_cnt(temp[-1])
            cur_left += 1
        else:
            temp.append(right_A[cur_right])
            cnt += 1
            check_cnt(temp[-1])
            cur_right += 1
    
    # 왼쪽이 남아 있으면 
    while cur_left < len(left_A):
        temp.append(left_A[cur_left])
        cnt += 1
        check_cnt(temp[-1])
        cur_left += 1
    
    # 오른쪽이 남아 있으면
    while cur_right < len(right_A):
        temp.append(right_A[cur_right])
        cnt += 1
        check_cnt(temp[-1])
        cur_right += 1

    return temp

def check_cnt(n):
    if cnt == K:
        print(n)
        exit()

N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0

merge_sort(A)
print(-1)