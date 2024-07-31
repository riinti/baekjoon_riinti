import sys

input = sys.stdin.readline

n = int(input())

nlist=[0,1]
for i in range(1,n):
  nlist.append(nlist[i-1]+nlist[i])

print(nlist[-1])