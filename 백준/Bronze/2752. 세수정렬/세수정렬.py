import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
nlist = []
nlist.append(a)
nlist.append(b)
nlist.append(c)

nlist.sort()

print(*nlist)