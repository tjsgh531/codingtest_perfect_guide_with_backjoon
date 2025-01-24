import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [A[0]] # dp[i] 증가 부분수열의 길이가 i인 수중 가장 작은 값

def binary_search(arr, num):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left+right) // 2
        
        if arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return left

for num in A[1:]:
    if dp[-1] < num:
        dp.append(num)
    else: # i 번째는 num보다 작고 i+1번째는 num보다 큰 i를 찾아서 i+1번째 수를 num으로 바꿔줌
        idx = binary_search(dp, num)
        dp[idx] = num

print(len(dp))