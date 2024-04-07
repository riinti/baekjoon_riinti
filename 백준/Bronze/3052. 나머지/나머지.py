mlist=[]
nlist=[]

for _ in range(10):
  nlist.append(int(input()))

for i in range(10):
  mlist.append(nlist[i]%42)

print(len(set(mlist)))