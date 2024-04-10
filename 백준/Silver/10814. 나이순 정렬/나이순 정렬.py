import sys

input = sys.stdin.readline

N = int(input())
nlist = []

for _ in range(N):
  age, name = input().split()
  nlist.append([int(age), name])

nlist = sorted(nlist, key=lambda x: x[0])

for i in nlist:
  print(i[0], i[1])