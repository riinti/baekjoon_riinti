import sys

input = sys.stdin.readline

N = int(input())
count = 1
num = 0

while True:
  num+=1
  if "666" in str(num):
    if count == N:
      print(int(num))
      break
    else:
      count+=1