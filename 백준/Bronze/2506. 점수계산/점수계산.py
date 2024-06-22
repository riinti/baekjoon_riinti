import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

count = 0
score = 0
for i in range(n) :
  if data[i] == 1 :
    count += 1
    score += count
  else :
    count = 0

print(score)