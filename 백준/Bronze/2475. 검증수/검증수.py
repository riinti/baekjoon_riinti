def koi():
  nlist = list(map(int, input().split()))
  mlist = []
  for i in range(len(nlist)):
    mlist.append(nlist[i]**2)
  num = sum(mlist)
  num2 = num % 10
  print(num2)


koi()