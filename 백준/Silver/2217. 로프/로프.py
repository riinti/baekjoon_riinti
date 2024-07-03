import sys

input = sys.stdin.readline

n = int(input())
nlist = []
rlist = []
for _ in range(n):
    nlist.append(int(input()))

nlist.sort()

for i in nlist:
    rlist.append(i*n)
    n -= 1

print(max(rlist))