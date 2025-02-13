import sys
input = sys.stdin.readline

input_str = input().strip()
exp_str = input().strip()

exp_str_length = len(exp_str)
last_word = exp_str[-1]

stack = []
for word in input_str:
    stack.append(word)
    if (word == last_word) and (len(stack) >= exp_str_length):
        if ''.join(stack[-exp_str_length:]) == exp_str: # 폭발 문자열이면
            del stack[-exp_str_length:]


result = ''.join(stack)
print(result if result else "FRULA")