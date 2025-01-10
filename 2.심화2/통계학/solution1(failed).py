# statistics 라이브러리를 활용하면 구현이 매우 편하지만 시간초과 문제가 발생한다.
import sys
import statistics

N = int(input())
num_list = []

for _ in range(N):
    num = int(input())
    num_list.append(num)

num_list.sort()

# 산술평균
mean = statistics.mean(num_list)
mean = round(mean)

# 중앙값
median = statistics.median(num_list)

# 최빈값
modes = statistics.multimode(num_list)
modes.sort()
if len(modes) > 1:
    mode = modes[1]
else:
    mode = modes[-1]
    
# 범위
num_range = max(num_list) - min(num_list)

print(mean)
print(median)
print(mode)
print(num_range)