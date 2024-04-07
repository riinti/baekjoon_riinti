import sys

input = sys.stdin.readline

nlist = []

for _ in range(3):
  num = int(input())
  nlist.append(num)


gop = nlist[0]*nlist[1]*nlist[2]
gop = str(gop)

for i in range(10):
    print(gop.count(str(i)))