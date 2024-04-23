from collections import deque
import sys

input = sys.stdin.readline

N=int(input())
nlist = deque(range(1, N + 1))

while len(nlist) > 1:
  nlist.popleft()
  num = nlist.popleft()
  nlist.append(num)
  

print(nlist[0])