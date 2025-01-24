import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

team1 = []
team2 = []
answer = 100 * N

def new_mem_score(team_score, team, new_mem):
    for mem in team:
        team_score += board[mem][new_mem]
        team_score += board[new_mem][mem]

    return team_score


def backtracking(mem, team1_score, team2_score):
    global team1, team2, answer

    if mem == N:
        answer = min(answer, abs(team1_score - team2_score))
        return

    # team1이 다 안찼을 경우
    if len(team1) < (N//2):
        new_team1_score = new_mem_score(team1_score, team1, mem)

        team1.append(mem)
        backtracking(mem+1, new_team1_score, team2_score)
        team1.pop()

    # team2가 다 안찼을 경우
    if len(team2) < (N//2):
        new_team2_score = new_mem_score(team2_score, team2, mem)

        team2.append(mem)
        backtracking(mem+1, team1_score, new_team2_score)
        team2.pop()

backtracking(0, 0, 0)
print(answer)

