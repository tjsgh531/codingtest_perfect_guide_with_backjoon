import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

def obtained_tree_length(slice_length):
    answer = 0
    for tree in trees:
        sliced_tree_length = tree - slice_length
        if sliced_tree_length > 0 :
            answer += sliced_tree_length
    return answer

def binary_search(wanted_length):
    left = 0
    right = max(trees)

    answer = 0
    while left <= right:
        mid = (left + right) // 2
        tree_length = obtained_tree_length(mid)

        # 내가 원하는 만큼 얻을 수 있다.
        if tree_length >= wanted_length:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer

print(binary_search(M))


