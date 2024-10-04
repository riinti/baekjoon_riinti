import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
nlist.reverse()
dq = deque()
rlist = [-1]*n

for i in range(n):
  while dq:
    if nlist[i] < dq[-1][1]:
      rlist[i] = dq[-1][1]
      break
    else:
      dq.pop()
  dq.append((i,nlist[i]))
print(*reversed(rlist))