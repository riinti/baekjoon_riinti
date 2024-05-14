import sys

input = sys.stdin.readline

n = int(input())
nlist = []
count = 0

for _ in range(n):
    nlist.append(input().split())

for i,j in nlist:
    count = 0
    for x,y in nlist:
        if int(i)<int(x) and int(j)<int(y):
            count += 1
    print(count+1, end=" ")