import sys
input = sys.stdin.readline

# dp[i][j] : i번째 추까지 사용 했을 때, j무게를 측정할 수 있는지 여부

# 입력 받기
N = int(input())  # 추 개수
weights = list(map(int, input().split()))  # 추 무게 목록
M = int(input())  # 확인할 구슬 개수
targets = list(map(int, input().split()))  # 확인할 구슬 무게

# 가능한 무게를 저장할 DP 테이블
MAX_WEIGHT = sum(weights)
dp = [[False] * (MAX_WEIGHT + 1) for _ in range(N + 1)]
dp[0][0] = True  # 초기 상태: 무게 0은 항상 가능

# DP 수행
for i in range(1, N + 1):
    w = weights[i - 1]
    for j in range(MAX_WEIGHT + 1):
        if dp[i - 1][j]:  # 이전 상태에서 무게 j가 가능했다면
            dp[i][j] = True  # 현재 상태에서도 가능
            if j + w <= MAX_WEIGHT:
                dp[i][j + w] = True  # 현재 추를 오른쪽에 올림
            dp[i][abs(j - w)] = True  # 현재 추를 왼쪽에 올림

# 결과 출력
result = []
for t in targets:
    if t > MAX_WEIGHT:  # 추의 최대 합보다 크면 절대 만들 수 없음
        result.append("N")
    elif dp[N][t]:  # 마지막 추까지 사용했을 때 무게 t를 만들 수 있다면
        result.append("Y")
    else:
        result.append("N")

print(" ".join(result))
