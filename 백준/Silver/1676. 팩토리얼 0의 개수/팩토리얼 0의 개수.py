N = int(input())
nlist=[]
num=1
mlist =[]

for i in range(1,N+1):
  nlist.append(i)

for j in nlist:
  num *= j

num =str(num)

for k in num:
  mlist.append(k)

mlist = list(reversed(mlist))
cou = 0

for l in range(len(mlist)):
  if mlist[l]=="0":
    cou+=1
  else:
    break

print(cou)