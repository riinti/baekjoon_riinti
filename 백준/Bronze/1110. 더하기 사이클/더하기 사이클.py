import sys

input = sys.stdin.readline

num = int(input())
num_ = num
count = 0
while True:
    ten = num // 10
    one = num % 10
    total = ten + one
    count += 1
    num = int(str(num % 10) + str(total % 10))
    if(num_ == num):
        break
print(count)