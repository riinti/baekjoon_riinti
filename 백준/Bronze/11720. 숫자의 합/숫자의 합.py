import sys

input = sys.stdin.readline

N = input()
nums = input()

total = 0

for i in range(int(N)):
    total += int(nums[i])
print(total)