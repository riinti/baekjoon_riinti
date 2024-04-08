N = int(input())
nlist=[]

for _ in range(N):
  word = str(input())
  nlist.append(word)

nlist = set(nlist)
nlist = list(nlist)
nlist.sort()
nlist.sort(key=len)

for j in range(len(nlist)):
  print(nlist[j])