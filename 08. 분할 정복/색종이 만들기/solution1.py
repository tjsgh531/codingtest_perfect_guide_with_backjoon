import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0

def check_graph(sub_graph):
    if len(sub_graph) == 1:
        return True
    
    color = sub_graph[0][0]

    for row in sub_graph:
        for item in row:
            if item != color:
                return False
    return True

def slice_graph(sub_graph):
    global white, blue
    if check_graph(sub_graph): # 모두 같은 색이면
        if sub_graph[0][0] == 0:
            white += 1
        else:
            blue += 1
        return
    else: # 색이 석여 있으면 잘라야 해요.
        n = len(sub_graph)
        upper = sub_graph[:n//2]
        lower = sub_graph[n//2:]

        upper_left = [row[:n//2] for row in upper]
        upper_right = [row[n//2:] for row in upper]
        lower_left = [row[:n//2] for row in lower]
        lower_right = [row[n//2:] for row in lower]

        slice_graph(upper_left)
        slice_graph(upper_right)
        slice_graph(lower_left)
        slice_graph(lower_right)

slice_graph(graph)
print(white)
print(blue)
