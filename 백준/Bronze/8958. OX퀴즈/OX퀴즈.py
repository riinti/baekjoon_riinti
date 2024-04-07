T = int(input())
nlist=[]


for _ in range(0, T):
  q = str(input())
  nlist=[]
  score=0
  com=1
  for j in q:
    nlist.append(j)
    if j == "O":
      score = score+com
      com += 1
    else:
      com = 1
  print(score)
