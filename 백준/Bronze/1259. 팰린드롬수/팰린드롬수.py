import sys

while True:
  num = sys.stdin.readline().rstrip()
  if num == '0':
    break
  else:
    num_r = num[::-1]
    if num == num_r:
      print("yes")
    else:
      print("no")
