#include <stdio.h>
#include <string.h>

def recursion(s, l, r):
    global recursion_count

    recursion_count += 1

    if(l >= r) :
        return 1

    elif(s[l] != s[r]):
        return 0

    else:
        return recursion(s, l+1, r-1)


def isPalindrome(s):
    global recursion_count
    recursion_count = 0
    return recursion(s, 0, len(s)-1)


T = int(input())
recursion_count = 0

for _ in range(T):
    string = input().strip()
    is_palindrome = isPalindrome(string)
    print(is_palindrome, recursion_count)
    


