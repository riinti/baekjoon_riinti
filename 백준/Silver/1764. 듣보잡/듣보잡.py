import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nlist = set()
mlist = set()


for _ in range(n):
  nlist.add(input())
for _ in range(m):
  mlist.add(input())

                  
result = sorted(nlist&mlist)
print(len(result))
print(*result, sep="")