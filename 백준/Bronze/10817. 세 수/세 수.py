import sys

input = sys.stdin.readline

nlist = list(map(int, input().split()))
nlist.sort()

print(nlist[1])