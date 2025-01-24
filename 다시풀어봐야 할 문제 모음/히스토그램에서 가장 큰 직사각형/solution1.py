import sys
input = sys.stdin.readline

def mid_max_size(num_list):
    n = len(num_list)
    mid = n // 2

    height = num_list[mid]
    width = 1
    max_size = height * width

    left = mid - 1
    right = mid + 1

    while (left >= 0) or (right < n):
        # 왼쪽으로 확장할 조건 
        # 1. 왼쪽이 0 보다 크거나 같아야함.
        # 2. 오른쪽이 n 이거나 오른쪽으로 확장 하는 경우보다 왼쪽으로 확장하는 height가 더 커야함.
        if (left >= 0) and ((right == n) or num_list[left] > num_list[right]):
            height = min(num_list[left], height)
            width += 1
            max_size = max(max_size, width * height)
            left -= 1
        # 오른쪽으로 확장
        else:
            height = min(num_list[right], height)
            width += 1
            max_size = max(max_size, width * height)
            right += 1

    return max_size

def solution(num_list):
    if len(num_list) == 1:
        return num_list[0]

    n = len(num_list)
    mid = n // 2

    left_num_list = num_list[:mid]
    right_num_list = num_list[mid:]

    left_max_size = solution(left_num_list)
    right_max_size = solution(right_num_list)
    cur_max_size = mid_max_size(num_list)

    return max(left_max_size, right_max_size, cur_max_size)

while True:
    input_list = list(map(int, input().split()))
    if len(input_list) == 1:
        break
    
    n = input_list[0]
    num_list = input_list[1:]
    print(solution(num_list))