import sys

input = sys.stdin.readline

num = 0

for i in range(3):
  a = input().rstrip()
  if a != "Fizz" and a != "Buzz" and a != "FizzBuzz":
    a = int(a)
  if isinstance(a, int):
    if i == 0:
      num = int(a) + 3
      break
    elif i == 1:
      num = int(a) + 2
      break
    elif i == 2:
      num = int(a) + 1
      break

if (num % 3) == 0 and (num % 5) == 0:
  print("FizzBuzz")
elif (num % 3) == 0 and (num % 5) != 0:
  print("Fizz")
elif (num % 3) != 0 and (num % 5) == 0:
  print("Buzz")
else:
  print(num)