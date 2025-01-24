import sys
input = sys.stdin.readline
from itertools import product

N = int(input())

answer = len(list(product(range(2), repeat = N)))
print(answer)

