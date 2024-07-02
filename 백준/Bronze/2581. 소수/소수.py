import sys

input = sys.stdin.readline

m = int(input())
n = int(input())
nlist = []

for i in range(m,n+1):
  if i != 1 :
      for j in range(2,int(i**0.5)+1):
          if i % j == 0:
              break
      else:
          nlist.append(i)

if len(nlist):
    print(sum(nlist))
    print(nlist[0])
else:
    print(-1)