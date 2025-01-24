import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

num_dict = {}
for num in num_list:
    if num_dict.get(num):
        num_dict[num] += 1
    else:
        num_dict[num] = 1

def binary_search(arr, target):
    left = 0
    right = len(arr) -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return num_dict[target]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

answer = []
sorted_num = sorted(list(num_dict.keys()))

for num in numbers:
    answer.append(binary_search(sorted_num, num))

print(' '.join(list(map(str, answer))))