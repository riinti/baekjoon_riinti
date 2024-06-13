import sys

input = sys.stdin.readline

x, y, w, h = map(int, input().split())

a = x
b = y
c = w -x
d = h - y

nlist = [a, b, c, d]
print(min(nlist))