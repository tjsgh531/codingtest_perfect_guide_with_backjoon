import sys
input = sys.stdin.readline

def merge_sort(A, p, r):
    if (p < r):
        q = (p+r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global cnt

    i = p
    j = q+1
    tmp = []

    while (i <= q ) and (j <= r):
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    # 왼쪽이 남아 있으면
    while i <= q:
        tmp.append(A[i])
        i += 1
    
    # 오른쪽이 남아 있으면
    while j <= r:
        tmp.append(A[j])
        j += 1

    # 저장
    i = p
    for item in tmp:
        A[i] = item
        i += 1
        cnt += 1
        if cnt == K:
            print(item)
            exit()

N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
merge_sort(A, 0, N-1)
print(-1)
