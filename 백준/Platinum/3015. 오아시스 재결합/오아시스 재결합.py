import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
blist = [int(input()) for x in range(n)]
dq = deque()
result = 0

for i in blist:
  while dq and dq[-1][0]<i:
    result += dq.pop()[1]
    
  if not dq:
    dq.append((i, 1))
    continue
    
  if dq[-1][0]==i:
    cnt = dq.pop()[1]
    result += cnt
    if dq: 
      result += 1
    dq.append((i, cnt+1))

  else:
    dq.append((i, 1))
    result += 1

print(result)