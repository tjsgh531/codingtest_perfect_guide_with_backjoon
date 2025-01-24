import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

answer = 0
for idx, val in enumerate(num_list):
    answer += (N-idx) * val
print(answer)