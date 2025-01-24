# numpy 라이브러리는 python 내장 라이브러리가 아니었네...
import sys
input = sys.stdin.readline
import numpy as np
from scipy import stats

N = int(input())
num_list = []

for _ in range(N):
    num = int(input())
    num_list.append(num)

num_array = np.array(num_list)

# 산술평균
mean = round(np.mean(num_array))

# 중앙값
median = np.median(num_array)

# 최빈값
modes = stats.mode(num_array)
modes.sort()
if len(modes) > 1:
    mode = modes[1]
else:
    mode = modes[0]

# 범위
num_range = np.ptp(num_array)

print(mean)
print(median)
print(mode)
print(num_range)





