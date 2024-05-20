import sys

input = sys.stdin.readline

N=int(input())
for i in range(N):
    print(" "*i+ "*"*(((N-i)*2)-1))
for i in range(2, N+1):
    print((" "*(N-i)+ "*"*(((i)*2)-1)))