# 무엇을 묻고 싶은 문제인가?
import sys
input = sys.stdin.readline

T = int(input())
measures = list(map(int, input().split()))
measures.sort()

answer = measures[0] * measures[-1]
print(answer)