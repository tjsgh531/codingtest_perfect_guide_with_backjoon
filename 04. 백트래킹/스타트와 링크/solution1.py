# itertools 풀이법
import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

team_comb = list(combinations(range(N), N//2))
answer = 100 * N

for team1 in team_comb:
    team2 = [i for i in range(N) if i not in team1]

    team1_score = 0
    team2_score = 0
    for i in range(N//2):
        team1_mem1 = team1[i]
        team2_mem1 = team2[i]

        for j in range(N//2):
            team1_mem2 = team1[j]
            team2_mem2 = team2[j]

            team1_score += board[team1_mem1][team1_mem2]
            team2_score += board[team2_mem1][team2_mem2]

    answer = min(answer, abs(team1_score-team2_score))
print(answer)