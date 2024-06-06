import sys

input = sys.stdin.readline

peole = int(input())
tlist = list(map(int, input().split()))
t, p = map(int, input().split())
t_count = 0 

for i in tlist:
  if (i%t) == 0:
    t_count += (i//t)
  else:
    t_count += (i//t)+1

print(t_count)
print(peole//p, peole%p)