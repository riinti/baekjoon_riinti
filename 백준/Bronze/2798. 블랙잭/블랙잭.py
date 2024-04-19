import sys

input = sys.stdin.readline

N, M = map(int,input().split())
nlist = list(map(int,input().split()))
mlist = []

for i in nlist:
  for j in nlist:
    for k in nlist:
      hap = i+j+k
      if i==j or i==k or j==k or hap>M:
        continue
      else:
        mlist.append(hap)

print(max(mlist))