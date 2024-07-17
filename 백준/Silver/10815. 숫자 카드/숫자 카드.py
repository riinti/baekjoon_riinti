import sys

input = sys.stdin.readline

N = int(input())
nlist = list(map(int,input().split()))
M =int(input())
mlist = list(map(int,input().split()))

dict = {}

for i in nlist:
    if i in dict:
        dict[i] += 1 
    else:
        dict[i] = 1

for i in mlist:
    if i in dict:
        print(1, end=' ')
    else:
        print(0, end=' ')