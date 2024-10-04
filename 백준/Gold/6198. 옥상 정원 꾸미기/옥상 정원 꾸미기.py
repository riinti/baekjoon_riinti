import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
blist = [int(input()) for x in range(n)]
dq = deque()
result = 0

for i in range(n):
  while dq and dq[-1][1]<=blist[i]:
    dq.pop()
  dq.append((i,blist[i]))
  result += len(dq) -1
print(result)