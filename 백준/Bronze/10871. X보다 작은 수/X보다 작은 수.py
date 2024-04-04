import sys

input = sys.stdin.readline
  

N, X = map(int,input().split())
nlist=list(map(int,input().split()))
mlist=[]
for i in nlist:
  if i<X:
    mlist.append(i)
print(*mlist)