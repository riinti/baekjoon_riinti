import sys

input = sys.stdin.readline

N = int(input())

for i in range(1,N+1):
  num = i + sum([int(j) for j in str(i)])
  if num == N:
    print(i)
    break
  if i == N:
    print(0)