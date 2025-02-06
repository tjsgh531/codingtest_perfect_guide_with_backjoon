import sys
input = sys.stdin.readline

N, M = map(int, input().split())

vocabulary_book = {}
for _ in range(N):
    word = input().strip()

    # M 보다 짧은 단어는 기록하지 않음
    if len(word) < M:
        continue

    if word in vocabulary_book:
        vocabulary_book[word] += 1
    else:
        vocabulary_book[word] = 1

sorted_vocabulary_book = sorted(vocabulary_book.items(), key = lambda x :(-x[1], -len(x[0]), x[0]))

for word in sorted_vocabulary_book:
    print(word[0])