import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    for _ in range(m):
        u, v = map(int, input().split())
    print(n - 1)