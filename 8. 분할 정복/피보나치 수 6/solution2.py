import sys
input = sys.stdin.readline

def matrix_multiply(a, b):
    return [
        [(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % 1000000007, (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % 1000000007],
        [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % 1000000007, (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % 1000000007]
    ]

def matrix_power(matrix, n):
    if n == 1:
        return matrix
    if n % 2 == 0:
        half = matrix_power(matrix, n // 2)
        return matrix_multiply(half, half)
    else:
        return matrix_multiply(matrix, matrix_power(matrix, n - 1))

n = int(input())
base_matrix = [[1, 1], [1, 0]]
result = matrix_power(base_matrix, n)
print(result[0][1])
