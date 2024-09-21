import sys

input = sys.stdin.readline

N,K= map(int,input().split())
nlist=[]

for i in range(1,N+1):
  nlist.append(i)

ind = K-1

print("<",end="")
for _ in range(N-1):
  print(nlist[ind], end=", ")
  del nlist[ind]
  ind = ind+K-1
  
  if ind>=len(nlist):
    ind = ind%len(nlist)

print(nlist[0],end="")
print(">")