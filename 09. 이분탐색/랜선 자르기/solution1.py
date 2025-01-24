import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

def num_lines(line_length):
    answer = 0
    for line in lines:
        answer += (line // line_length)
    return answer

def binary_search():
    left = 1
    right = max(lines)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        line_cnt = num_lines(mid)

        # 원하는 개수만큼 잘림
        if line_cnt >= N:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

print(binary_search())
