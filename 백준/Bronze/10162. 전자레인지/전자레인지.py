import sys

input = sys.stdin.readline

T = int(input())
T_list =[300,60,10]

if T%10==0:
  for i in T_list:
    print(T//i, end=" ")
    T=T%i
  print()
else:
  print(-1)