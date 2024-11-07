import sys

input = sys.stdin.readline

t = int(input())
nlist = []

for _ in range(t):
    num = int(input())
    nlist.append(num)
nlist.sort()

for j in nlist:
    print(j)