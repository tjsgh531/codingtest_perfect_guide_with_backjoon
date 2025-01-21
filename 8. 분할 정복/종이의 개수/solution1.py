import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

paper_0 = 0
paper_1 = 0
paper_minus_1 = 0

def check_graph(sub_graph):
    if len(sub_graph) == 1:
        return True

    number = sub_graph[0][0]
    for row in sub_graph:
        for item in row:
            if number != item:
                return False
    return True

def slice_graph(sub_graph):
    global paper_1, paper_0, paper_minus_1
    if check_graph(sub_graph): ## 하나로 압축 가능하면
        number = sub_graph[0][0]
        if number == -1:
            paper_minus_1 += 1
        elif number == 0:
            paper_0 += 1
        else:
            paper_1 += 1
        return

    else: # 잘라야하는 경우
        n = len(sub_graph)
        upper = sub_graph[:n//3]
        middle = sub_graph[n//3: (n*2)//3]
        lower = sub_graph[(n*2)//3:]

        upper_left = [row[:n//3] for row in upper]
        upper_middle = [row[n//3: (n*2)//3] for row in upper]
        upper_right = [row[(n*2)//3:] for row in upper]

        middle_left = [row[:n//3] for row in middle]
        middle_middle = [row[n//3: (n*2)//3] for row in middle]
        middle_right = [row[(n*2)//3:] for row in middle]

        lower_left = [row[:n//3] for row in lower]
        lower_middle = [row[n//3: (n*2)//3] for row in lower]
        lower_right = [row[(n*2)//3:] for row in lower]

        slice_graph(upper_left)
        slice_graph(upper_middle)
        slice_graph(upper_right)

        slice_graph(middle_left)
        slice_graph(middle_middle)
        slice_graph(middle_right)

        slice_graph(lower_left)
        slice_graph(lower_middle)
        slice_graph(lower_right)

slice_graph(graph)
print(paper_minus_1)
print(paper_0)
print(paper_1)