import sys

input = sys.stdin.readline

T=int(input())
lst=[]

for _ in range(T):
  A, B = map(int,input().split())
  lst.append(A+B)
  
for i in range(T):
  print(lst[i])