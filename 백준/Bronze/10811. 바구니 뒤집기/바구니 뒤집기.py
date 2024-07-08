import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nlist = list(range(n+1))
for _ in range(m):
    a, b = map(int, input().split())
    nlist[a:b+1] = reversed(nlist[a:b+1])
print(*nlist[1:])