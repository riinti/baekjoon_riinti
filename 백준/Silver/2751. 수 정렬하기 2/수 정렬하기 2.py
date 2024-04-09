import sys

input = sys.stdin.readline

N = int(input())
nlist =[]

for _ in range(N):
  nlist.append(int(input()))

nlist= sorted(nlist)

print(*nlist, sep="\n")