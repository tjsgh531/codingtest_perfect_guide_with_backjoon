import sys
input = sys.stdin.readline

N = int(input())
roads = list(map(int, input().split()))
oil_prices = list(map(int, input().split()))

answer = 0
min_oil_price = int(1e9)
for road, price in zip(roads, oil_prices[:-1]):
    min_oil_price = min(min_oil_price, price) # 이전 최저가와 현재 기름값을 비교해서 가장 싼 값으로 다음 도시로 향함.
    answer += (min_oil_price * road)
print(answer)