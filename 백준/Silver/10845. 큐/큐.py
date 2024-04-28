import sys

input = sys.stdin.readline

N = int(input())
nlist = []

for _ in range(N):
  order=list(input().split())
  if order[0]=="push":
    nlist.append(order[1])
  elif order[0]=="pop":
    if len(nlist)==0:
      print(-1)
    else:
      ind=nlist.pop(0)
      print(ind)
  elif order[0]=="size":
    print(len(nlist))
  elif order[0]=="empty":
    if len(nlist)==0:
      print(1)
    else:
      print(0)
  elif order[0]=="front":
    if len(nlist)==0:
      print(-1)
    else:
      print(nlist[0])
  elif order[0]=="back":
    if len(nlist)==0:
      print(-1)
    else:
      print(nlist[-1])