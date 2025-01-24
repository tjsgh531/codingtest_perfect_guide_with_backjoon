import sys
input = sys.stdin.readline

N = int(input())

num_list = []
num_dict = {}
for _ in range(N):
    num = int(input())
    num_list.append(num)
    
    if num_dict.get(num):
        num_dict[num] += 1
    else:
        num_dict[num] = 1

num_list.sort()

# 산술 평균
mean = round(sum(num_list) / N)

# 중앙값
median = num_list[N//2]

# 최빈값
max_count = 0
max_numbers = []
for num, count in num_dict.items():
    if max_count < count:
        max_count = count
        max_numbers = [num]

    elif max_count == count:
        max_numbers.append(num)

if len(max_numbers) == 1:
    mode = max_numbers[0]
else:
    max_numbers.sort()
    mode = max_numbers[1]

# 범위
num_range = num_list[-1] - num_list[0]

print(mean)
print(median)
print(mode)
print(num_range)
