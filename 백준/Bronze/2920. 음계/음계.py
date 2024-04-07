nlist = list(map(int,input().split()))
mlist = sorted(nlist)
olist = sorted(nlist,reverse=True)

if nlist == mlist:
  print("ascending")
elif nlist == olist:
  print("descending")
else:
  print("mixed")