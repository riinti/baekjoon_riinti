import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nlist = list(range(n+1))
for _ in range(m):
    temp = 0
    a, b = map(int, input().split())
    temp = nlist[a]
    nlist[a] = nlist[b]
    nlist[b]  = temp
print(*nlist[1:])