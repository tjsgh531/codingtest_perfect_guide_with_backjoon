import sys
input = sys.stdin.readline

def kantoa(string):
    if len(string) == 1:
        return '-'
    
    division_length = len(string) // 3
    return kantoa('-'*division_length) + ' ' * division_length + kantoa('-'*division_length)

while True:
    try:
        N = int(input())
        string_length = 3 ** N
        string = '-' * string_length

        kantoa_string = kantoa(string)
        print(kantoa_string)
    except:
        break
