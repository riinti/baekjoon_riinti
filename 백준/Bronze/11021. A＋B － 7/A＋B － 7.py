import sys

input = sys.stdin.readline

T = int(input())

for i in range(1,T+1):
    a,b = map(int,input().split())
    print("Case #{}: {}".format(i,a+b))