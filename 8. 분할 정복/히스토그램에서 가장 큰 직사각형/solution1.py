import sys
input = sys.stdin.readline

def largest_rectangle(heights):
    stack = []
    max_area = 0
    heights.append(0)  # 마지막에 0을 추가하여 모든 높이를 처리할 수 있게 함
    
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index
        stack.append((start, h))
    
    return max_area

# 입력 처리
while True:
    input_list = list(map(int, input().split()))
    if input_list[0] == 0:
        break
    print(largest_rectangle(input_list[1:]))



