import sys
input = sys.stdin.readline

str_1 = input().strip()
str_2 = input().strip()

# dp[i+1][j+1] : str_1 i번째까지 단어와 str_2 j번째 까지 단어를 비교했을 때, 가장 긴 부분 단어 길이
dp = [[0] * (len(str_1)+1) for _ in range(len(str_2)+1)]

for idx_1, word_1 in enumerate(str_1):
    for idx_2, word_2 in enumerate(str_2):
        # 같으면 dp[i][j] + 1
        if word_1 == word_2:
            dp[idx_2+1][idx_1+1] = dp[idx_2][idx_1] + 1
        # 다르면 max(왼쪽, 위)
        else:
            dp[idx_2+1][idx_1+1] = max(dp[idx_2+1][idx_1], dp[idx_2][idx_1+1])

print(dp[-1][-1])
