import sys

input = sys.stdin.readline

nlist = list(map(int,input().split()))

if nlist[0]==nlist[1] and nlist[0]==nlist[2]:
  print(10000+nlist[0]*1000)
elif nlist[0]==nlist[1] or nlist[0]==nlist[2]:
  print(1000+nlist[0]*100)
elif nlist[1]==nlist[2] or nlist[1]==nlist[0]:
  print(1000+nlist[1]*100)
elif nlist[1]==nlist[2] or nlist[2]==nlist[0]:
  print(1000+nlist[2]*100)
else:
  print(max(nlist)*100)