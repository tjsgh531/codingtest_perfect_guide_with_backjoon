import sys
input = sys.stdin.readline

def largest_rectangle(heights, start, end):
    if start > end:
        return 0
    if start == end:
        return heights[start]
    
    mid = (start + end) // 2
    
    # 왼쪽, 오른쪽 부분에서의 최대 넓이
    left_area = largest_rectangle(heights, start, mid)
    right_area = largest_rectangle(heights, mid + 1, end)
    
    # 중간을 걸치는 직사각형의 최대 넓이
    height = min(heights[mid], heights[mid + 1])
    width = 2
    area = height * width
    left = mid - 1
    right = mid + 2
    
    while left >= start or right <= end:
        if right <= end and (left < start or heights[right] > heights[left]):
            height = min(height, heights[right])
            right += 1
        else:
            height = min(height, heights[left])
            left -= 1
        width += 1
        area = max(area, height * width)
    
    return max(left_area, right_area, area)

# 입력 처리
while True:
    input_list = list(map(int, input().split()))
    if input_list[0] == 0:
        break
    print(largest_rectangle(input_list[1:], 0, len(input_list) - 2))
