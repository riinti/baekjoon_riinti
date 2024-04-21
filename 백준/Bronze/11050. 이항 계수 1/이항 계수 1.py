import sys

input = sys.stdin.readline

def factorial(n):
  num = 1
  for i in range(1, n+1):
    num *= i
  return num

N,K= map(int,input().split())

print(factorial(N) // factorial(K) // factorial(N-K))