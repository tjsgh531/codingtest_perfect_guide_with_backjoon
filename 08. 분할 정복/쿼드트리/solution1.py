import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]

def check_graph(sub_graph):
    if len(sub_graph) == 1:
        return True

    try:
        number = sub_graph[0][0]
    except:
        for row in sub_graph:
            print(row)
        exit()

    for row in sub_graph:
        for item in row:
            if item != number:
                return False
    return True

def zip_graph(sub_graph):
    if check_graph(sub_graph): ## 하나의 수로 압축가능하면
        number = sub_graph[0][0]
        return number

    else: ## 잘라야 하는 경우
        n = len(sub_graph)
        upper = sub_graph[:n//2]
        lower = sub_graph[n//2:]

        upper_left = [row[:n//2] for row in upper]
        upper_right = [row[n//2:] for row in upper]
        lower_left = [row[:n//2] for row in lower]
        lower_right = [row[n//2:] for row in lower]

        upper_left_num = zip_graph(upper_left)
        upper_right_num = zip_graph(upper_right)
        lower_left_num = zip_graph(lower_left)
        lower_right_num = zip_graph(lower_right)

        return f"({upper_left_num}{upper_right_num}{lower_left_num}{lower_right_num})"

print(zip_graph(graph))