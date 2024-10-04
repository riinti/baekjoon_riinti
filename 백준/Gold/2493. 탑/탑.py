import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
dq = deque()
rlist = [0]*n

for i in range(n):
  while dq:
    if nlist[i] < dq[-1][1]:
      rlist[i] = dq[-1][0] + 1
      break
    else:
      dq.pop()
  dq.append((i,nlist[i]))
print(*rlist)
