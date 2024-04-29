import sys

input = sys.stdin.readline

N = int(input())
nlist = []

for _ in range(N):
  order=list(input().split())
  
  if order[0]=="push_back":
    nlist.append(order[1])
    
  elif order[0]=="push_front":
    nlist.insert(0,order[1])
    
  elif order[0]=="pop_front":
    if len(nlist)==0:
      print(-1)
    else:
      print(nlist.pop(0))
      
  elif order[0]=="pop_back":
    if len(nlist)==0:
      print(-1)
    else:
      print(nlist.pop())
      
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