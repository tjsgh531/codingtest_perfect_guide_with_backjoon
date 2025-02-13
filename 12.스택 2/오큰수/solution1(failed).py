import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
dp = [-1] * N

for idx, num in enumerate(num_list):
    for i in range(idx):
        if dp[i] == -1: # 아직 오큰수가 없으면
            if num_list[i] < num:
                dp[i] = num

print(' '.join(list(map(str, dp))))