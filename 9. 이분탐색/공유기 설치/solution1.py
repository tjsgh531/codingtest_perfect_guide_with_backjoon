import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house_pos = [int(input()) for _ in range(N)]
house_pos.sort()

def count_house(dist):
    pre_house_pos = house_pos[0]
    cnt = 1

    for pos in house_pos[1:]:
        between_dist = pos - pre_house_pos
        if between_dist >= dist: # 두집 사이 공유기 거리가 원하는 거리보다 같거나 멀다.
            cnt += 1
            pre_house_pos = pos

    return cnt

def binary_search():
    left = 1 # 두 집 사이 공유기 거리 최솟값
    right = house_pos[-1] - house_pos[0] # 두 집 사이 공유기 최댓값

    answer = 0
    while left <= right:
        mid = (left+right) // 2 # mid = 두 집사이 공유기 거리
        cnt = count_house(mid)

        if C <= cnt: # 목표 개수보다 많거나 같게 설치 가능하다. # 더 간격을 늘려도 괜찮음
            answer = mid
            left = mid + 1
        else: # 간격을 좁혀 더 많이 설치해야 함.
            right = mid - 1

    return answer

print(binary_search())


