import sys

input = sys.stdin.readline

H, M = map(int,input().split())
min = int(input())
hor = min//60
min = min%60

H+=hor
M+=min
  
if M >= 60:
  H += 1
  M-=60
if H >=24:
  H-=24
  

print(H,M)