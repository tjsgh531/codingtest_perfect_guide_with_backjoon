import sys
input = sys.stdin.readline

N = int(input())

def draw_star(n):
    # n == 9 일때만 생각하자
    if n == 1:
        return ['*']

    division_n = n //3
    stars = draw_star(division_n)

    L = []

    for star in stars:
        L.append(star * 3)
    for star in stars:
        L.append(star + ' ' * division_n  + star)
    for star in stars:
        L.append(star * 3)
    return L

print('\n'.join(draw_star(N)))