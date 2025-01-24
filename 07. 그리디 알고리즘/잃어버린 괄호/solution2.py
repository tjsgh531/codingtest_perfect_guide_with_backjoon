# re 사용하지 않은 해결법
import sys
input = sys.stdin.readline

equation = input()

numbers = "0123456789"
temp = ""
answer = 0
is_minus_appeared = False

for one_string in equation:
    # 숫자면 temp에 string형태로 더함
    if one_string in numbers:
        temp += one_string
    else: # 기호면 temp에 있는 수를 answer에 기호에따라 더하거나 뺌
        if is_minus_appeared: # -가 앞에 나왔으면 기호에 상관 없이 뺌
            answer -= int(temp)
        else: # 앞에 -가 나오지 않았으면
            if one_string == '-': # 지금 나온 기호가 -인지 판단
                is_minus_appeared = True
            answer += int(temp) # 일단 지금 나온 기호와 상관 없이 결과 더하기
        temp = ''
print(answer)


        