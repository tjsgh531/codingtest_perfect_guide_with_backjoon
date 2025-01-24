import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

sum_list = [num_list[0]]
for i in num_list[1:]:
    sum_list.append(sum_list[-1] + i)

answer = max(sum_list)
for i in range(1, n):
    for j in range(i):
        temp = sum_list[i] - sum_list[j] # j번째 부터 i 번째 까지 숫자합
        answer = max(answer, temp)

print(answer)