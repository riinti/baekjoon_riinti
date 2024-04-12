import sys

input = sys.stdin.readline

T = int(input())
C_list =[25, 10, 5,1]

for _ in range(T):
  C=int(input())
  for i in C_list:
    print(C//i, end=" ")
    C=C%i
  print()