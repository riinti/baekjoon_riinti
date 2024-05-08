import sys

input = sys.stdin.readline

n = int(input())

num=0
n-=1
while n>0:
  num+=1
  n-=(num*6)
print(num+1)