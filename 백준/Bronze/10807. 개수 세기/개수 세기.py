import sys

input = sys.stdin.readline
  

N = int(input())
nlist=list(map(int,input().split()))
v = int(input())
mlist=[]
for i in nlist:
  if v == i:
    mlist.append(i)
print(len(mlist))