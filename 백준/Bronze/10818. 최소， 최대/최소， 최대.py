import sys

input = sys.stdin.readline

N = int(input())
nlist=list(map(int,input().split()))

print(min(nlist),max(nlist))