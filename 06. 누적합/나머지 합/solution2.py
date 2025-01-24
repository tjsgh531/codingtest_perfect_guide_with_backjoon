import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))

# dp[i] = (0~n까지 합) % M == i 가나오는 n의 개수
dp = [0] * M
sum_list = [0]

for num in num_list:
    item = (sum_list[-1] + num) % M
    sum_list.append(item)
    dp[item] += 1

answer = 0
for idx, val in enumerate(dp):
    # 다른 구간 생각 할 필요없는 경우 answer 에 바로 그 구간 개수 만큼 더함
    if idx == 0:
        answer += val

    # 같은 나머지 나오는 구간 두개를 고르는 경우의 수
    # 같은 나머지 나오는 서로 다른 구간을 빼면 M으로 나눠 떨어지는 연속합 구간 이다.
    if val >= 2:
        answer += val * (val-1) //2

print(answer)
    

