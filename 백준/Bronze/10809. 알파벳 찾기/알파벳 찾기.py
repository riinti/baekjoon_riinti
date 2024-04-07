S = str(input())
nlist = []
mlist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in S:
  nlist.append(i)
for j in mlist:
  if j in nlist:
    print(nlist.index(j))
  else:
    print(-1)