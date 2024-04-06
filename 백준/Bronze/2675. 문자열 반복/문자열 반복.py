import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  R, word =input().split()
  
  for j in word:
      print(j * int(R), end = "")
  print("")