import sys

input = sys.stdin.readline

N = int(input())
result = 1
if N > 0:
    for i in range(1, N+1):
        result *= i
print(result)