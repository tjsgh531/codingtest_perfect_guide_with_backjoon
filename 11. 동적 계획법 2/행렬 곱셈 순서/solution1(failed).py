import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

for repeat in range(N-1):
    for i in range(N-repeat-1):
        j = i + repeat + 1

        temp = []
        print()
        for k in range(i, j):
            item = dp[i][k] + dp[k+1][j] + arr[i][0]*arr[k][1]*arr[j][1]
            temp.append(item)
            print(f"{dp[i][k]} + {dp[k+1][j]} + {arr[i][0]}*{arr[k][1]}*{arr[j][1]} = {item}")
        dp[i][j] = min(temp)

    print()
    for row in dp:
        print(row)
    print("-" * 100)