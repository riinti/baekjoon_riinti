import sys

input = sys.stdin.readline
  
nlist =[]
mlist =[]
for _ in range(28):
  number = int(input())
  nlist.append(number)
for i in range(1,31):
  if i not in nlist:
    mlist.append(i)
print(mlist[0])
print(mlist[1])