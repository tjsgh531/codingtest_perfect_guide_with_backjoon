import sys
input = sys.stdin.readline

text = input().strip()

# dp[i][j] : text의 i 번째 글까지 j번째 알파벳이 등장한 수
dp = [[0] * 26]

for idx, word in enumerate(text):
    temp = dp[-1][::]
    alpha_num = ord(word) - ord('a')
    temp[alpha_num] += 1
    dp.append(temp)

q = int(input())
for _ in range(q):
    alphabet, l, r = input().split()
    l, r = int(l), int(r)

    alpha_num = ord(alphabet) - ord('a')
    
    print(dp[r+1][alpha_num] - dp[l][alpha_num])

