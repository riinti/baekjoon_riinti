import sys

input = sys.stdin.readline

N=int(input())
for i in range(N-1):
    print(" "*(N-i-1) + "*"*((i+1)*2-1))
for i in range(N):
    print(" "*i + "*"*((N-i)*2-1))