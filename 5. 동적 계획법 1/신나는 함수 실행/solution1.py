import sys
input = sys.stdin.readline

# dp[0][0][0] : a = 0, b = 0, c = 0 일때 값
dp = [[[None] * 21 for _ in range(21)] for _ in range(21)]
dp[0][0][0] = 1

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c] is None:
        if a < b and b < c:
            dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        else:
            dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        
        return dp[a][b][c]
    else:
        return dp[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    
    print(f"w({a}, {b}, {c}) = ", end='')
    answer = w(a, b, c)
    print(answer)