# Counter 를 활용한 최빈값 구현 => 시간 복잡도면에서 불리... 그래도 구현 난이도는 좀 더 쉬움
import sys
input = sys.stdin.readline
from collections import Counter

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
num_counter = Counter(num_list)
max_count = max(num_counter.values())

modes = [num for num, count in num_counter.items() if count == max_count]
if len(modes) > 1:
    mode = modes[1]
else:
    mode = modes[0]

# 범위
num_range = num_list[-1] - num_list[0]

print(mean)
print(median)
print(mode)
print(num_range)
