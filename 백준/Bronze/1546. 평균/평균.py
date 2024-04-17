import sys

input = sys.stdin.readline

T = int(input())
tlist = list(map(float,input().split()))

tlist = sorted(tlist, reverse=True)

high_t = tlist[0]

for i in range(T):
  tlist[i] = tlist[i]/high_t*100

print(sum(tlist)/len(tlist))