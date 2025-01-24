import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

num_list.sort()

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        # 중앙값이 타겟보다 작으면 왼쪽을 미드로 당겨야함
        elif arr[mid] < target:
            left = mid + 1
        # 중앙값이 타겟보다 크면 오른쪽을 미드로 당겨야함
        else:
            right = mid - 1
    return False

for num in numbers:
    if binary_search(num_list, num):
        print(1)
    else:
        print(0)

