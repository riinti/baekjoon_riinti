import sys

input = sys.stdin.readline

N = int(input())
nlist = list(map(int, input().split()))
nlist = set(nlist)
M = int(input())
mlist = list(map(int, input().split()))

for i in mlist:				 
  if i in nlist:
    print(1) 
  else:
    print(0)