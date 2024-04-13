import sys

input = sys.stdin.readline

N = int(input())
nlist = []

for _ in range(N):
  x, y = map(int,input().split())
  nlist.append([x, y])

nlist = sorted(nlist, key= lambda x : x[0]) 
nlist = sorted(nlist, key= lambda x : x[1]) 

for i in nlist:
  print(i[0], i[1])