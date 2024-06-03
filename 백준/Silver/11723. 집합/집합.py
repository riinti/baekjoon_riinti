import sys

input = sys.stdin.readline

N = int(input())
nlist = []

for _ in range(N):
  order=list(input().split())
  if order[0]=="add":
    if int(order[1]) not in nlist:
      nlist.append(int(order[1]))
  elif order[0]=="remove":
    if int(order[1]) in nlist:
      nlist.remove(int(order[1]))
  elif order[0]=="check":
    if int(order[1]) in nlist:
      print(1)
    else:
      print(0)
  elif order[0]=="toggle":
    if int(order[1]) in nlist:
      nlist.remove(int(order[1]))
    else:
      nlist.append(int(order[1]))
  elif order[0]=="all":
    nlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
  elif order[0]=="empty":
    nlist = []