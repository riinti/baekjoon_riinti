import sys

input = sys.stdin.readline

word = input().rstrip()

word_r = word[::-1]
if word == word_r:
  print(1)
else:
  print(0)