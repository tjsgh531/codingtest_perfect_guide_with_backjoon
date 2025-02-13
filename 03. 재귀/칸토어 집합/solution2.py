import sys
input = sys.stdin.readline

def recursive(cnt):
    if cnt == 0:
        return '-'

    result = recursive(cnt-1)
    return result + ' ' * len(result) + result
    
// yomi cute!!! I absolutely love ya!
while True:
    try:
        n = int(input())
        print(recursive(n))
    except:
        exit()