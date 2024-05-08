import sys

input = sys.stdin.readline

N = int(input())
count = 0
num = 0

while True:
  num+=1
  if count == N:
    print(int(num)-1)
    break
  else:
    if "666" in str(num):
      count+=1