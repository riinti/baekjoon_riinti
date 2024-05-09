import sys

input = sys.stdin.readline

n = int(input())
word = input()
res = 0

for i in range(n):
  res += (ord(word[i])-96) * (31 ** i)
print(res % 1234567891)
