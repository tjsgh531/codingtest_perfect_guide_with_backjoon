# 비트 연산을 활용한 풀이방법 -> 너무 매니악, 씹덕 스럽다
def solve_n_queens(n):
    def dfs(row, ld, rd):
        if row == all_queens:
            nonlocal count
            count += 1
            return
        
        pos = all_queens & ~(row | ld | rd)
        while pos:
            p = pos & -pos
            pos -= p
            dfs(row | p, (ld | p) << 1, (rd | p) >> 1)

    count = 0
    all_queens = (1 << n) - 1
    dfs(0, 0, 0)
    return count

# 입력 받기
n = int(input())

# 결과 출력
print(solve_n_queens(n))