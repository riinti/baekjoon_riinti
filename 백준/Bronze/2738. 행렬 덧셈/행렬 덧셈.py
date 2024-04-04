import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nlist = []
mlist = []

for _ in range(N):
  nlist.append(list(map(int, input().split())))

for _ in range(N):
  mlist.append(list(map(int, input().split())))

for i in range(N):
  for j in range(M):
    print(nlist[i][j] + mlist[i][j], end=" ")
  print("")