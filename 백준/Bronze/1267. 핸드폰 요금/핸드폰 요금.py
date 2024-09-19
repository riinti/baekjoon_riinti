import sys

input = sys.stdin.readline

t = int(input())
y = 0
m = 0

nlist = list(map(int, input().split()))
for i in nlist:
    y += (10*(i//30))+10
    m += (15*(i//60))+15
if y<m:
    print("Y",end=" ")
    print(y)
elif m<y:
    print("M",end=" ")
    print(m)
else:
    print("Y M",end=" ")
    print(y)