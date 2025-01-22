import sys
input = sys.stdin.readline

def large_rectangle(num_list):
    # stack에는 오른쪽으로 더 갈 수 있는 h들을 저장함. 이때 시작 idx도 함께 저장해야 width를 계산 할 수 있다.
    # 오른쪽으로 더 갈 수 있을 조건은 h가 right_h 보다 작아야 함.
    num_list.append(0)
    stack = []
    max_area = 0

    for idx, right_h in enumerate(num_list):
        start = idx
        # right_h 보다 크면 더이상 오른쪽으로 갈 수 없음
        while stack and stack[-1][1] > right_h:
            # right_h는 stack에서 pop된 start_index까지는 왼쪽으로 갈 수 있음
            start, h = stack.pop()
            width = idx - start
            max_area = max(max_area, width * h)
        stack.append((start, right_h))

    return max_area

while True:
    input_list = list(map(int, input().split()))
    if len(input_list) == 1:
        break

    print(large_rectangle(input_list[1:]))
