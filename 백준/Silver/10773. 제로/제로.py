import sys

input = sys.stdin.readline

T = int(input())
nlist=[]
for _ in range(T):
  num = int(input())
  if num != 0:
    nlist.append(num)
  else:
    nlist.pop(-1)

print(sum(nlist))