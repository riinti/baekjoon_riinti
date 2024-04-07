nlist=[]
mlist=[]

while True:
  nlist = list(map(int,input().split()))
  mlist = sorted(nlist, reverse=False)
  a = mlist[0]
  b = mlist[1]
  c = mlist[2]
  
  if a != 0 and b !=0 and c !=0:
    if c**2 == (a**2) + (b**2):
      print("right")
    else:
      print("wrong")
  else:
    break