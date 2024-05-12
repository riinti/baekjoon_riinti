import sys

input = sys.stdin.readline

nlist = []
for _ in range(9):
  nlist.append(int(input()))
nlist.sort()

s = sum(nlist)
mlist=[]

for i in range(9):
    for j in range(i+1,9):
        if len(mlist)==2:
          break
        if s-nlist[i]-nlist[j] ==100:
          mlist.append(nlist[i])
          mlist.append(nlist[j])

for i in nlist:
    if i in mlist:
        continue
    else:
      print(i)